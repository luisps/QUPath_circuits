#!/usr/bin/env python3
"""Plot QUPath CBS RGB and SS ALL path traces as polar diagrams."""

import argparse
import cmath
from collections import Counter, defaultdict
import math
from pathlib import Path


def read_trace(path):
    counts = Counter()
    with path.open() as stream:
        header = stream.readline().split()
        if len(header) != 5 or header[:2] != ["#", "QUPATH_PATHS"]:
            raise ValueError(f"{path}: expected a QUPath trace header")
        _, _, version, mode, layer_count = header
        layers = int(layer_count)
        columns = {("CBS", "1"): layers + 3, ("SS", "1"): layers + 4,
                   ("SS", "2"): 3 * (layers + 1) + 3}.get((mode, version))
        if columns is None or layers < 0:
            raise ValueError(f"{path}: unsupported trace format")
        for number, line in enumerate(stream, start=2):
            fields = line.split()
            if not fields or fields[0].startswith("#"):
                continue
            if len(fields) != columns:
                raise ValueError(f"{path}:{number}: expected {columns} columns")
            real, imag = map(float, fields[-2:])
            if not all(map(math.isfinite, (real, imag))):
                raise ValueError(f"{path}:{number}: nonfinite amplitude")
            if real or imag:
                counts[complex(real, imag)] += 1
    return mode, counts


def amplitude_groups(counts, digits):
    groups = defaultdict(list)
    for z, count in counts.items():
        # Round both components at the scale of |z| to absorb floating-point noise.
        places = digits - 1 - math.floor(math.log10(abs(z)))
        key = complex(round(z.real, places), round(z.imag, places))
        groups[key].append((z, count))

    def weighted_sum(entries):
        return complex(math.fsum(z.real * n for z, n in entries),
                       math.fsum(z.imag * n for z, n in entries))

    lobes = []
    for entries in groups.values():
        count = sum(n for _, n in entries)
        lobes.append((weighted_sum(entries) / count, count))
    total = weighted_sum(counts.items())
    mass = math.fsum(abs(z) * n for z, n in counts.items())
    x = max(1, mass / abs(total)) ** 2 if total else math.inf if mass else None
    return lobes, total, x


def draw(ax, lobes, total, title):
    from matplotlib.ticker import MaxNLocator
    import numpy as np

    blue, red = "#316a9a", "#c92435"
    ax.set_title(title, pad=24, fontsize=12, fontweight="bold")
    ax.set_axisbelow(True)
    ax.grid(color="#8a9aab", alpha=.32)
    ax.tick_params(labelsize=8)
    ax.set_rlabel_position(87)
    ax.yaxis.set_major_locator(MaxNLocator(4))
    ax.yaxis.set_major_formatter(lambda value, _: f"{value:.3g}")
    peak = max((abs(z) for z, _ in lobes), default=0)
    magnitude = abs(total)
    rim = 1.27 * (peak or 1)
    if peak and rim < magnitude <= 1.6 * peak:
        rim = 1.08 * magnitude
    ax.set_ylim(0, rim)
    if not lobes:
        ax.text(.5, .5, "No nonzero paths", transform=ax.transAxes, ha="center")
        return

    phases = sorted(set(round(cmath.phase(z) % math.tau, 11) % round(math.tau, 11)
                        for z, _ in lobes))
    gaps = [b - a for a, b in zip(phases, phases[1:])]
    gaps.append(math.tau + phases[0] - phases[-1])
    half_width = min(math.radians(22), .43 * min(gaps))
    max_count = max(n for _, n in lobes)
    curve = np.linspace(-1, 1, 161)
    for z, n in sorted(lobes, key=lambda item: abs(item[0]), reverse=True):
        angle, radius = cmath.phase(z), abs(z)
        angles = angle + half_width * n / max_count * curve
        radii = radius * np.cos(np.pi * curve / 2)
        ax.fill_between(angles, 0, radii, color=blue, alpha=.24)
        ax.plot(angles, radii, color=blue, linewidth=1.15)
        ax.plot(angle, radius, "o", color=blue, markersize=3)
        ax.annotate(f"{n:,}", (angle, radius),
                    xytext=(7 * math.cos(angle), 7 * math.sin(angle)),
                    textcoords="offset points", ha="center", va="center",
                    color=blue, fontsize=8, fontweight="bold")

    if not total:
        return None
    angle = cmath.phase(total)
    ax.plot([angle, angle], [0, min(magnitude, rim)], color=red,
            linewidth=2.2, zorder=5)
    if magnitude <= rim:
        ax.plot(angle, magnitude, "o", color=red, markersize=5, zorder=6)
        return None

    # A dashed continuation and arrowhead indicate that the endpoint is off scale.
    ax.annotate("", xy=(angle, rim * 1.10), xytext=(angle, rim),
                annotation_clip=False,
                arrowprops=dict(arrowstyle="-|>", color=red, lw=2.2,
                                linestyle="--", shrinkA=0, shrinkB=0),
                zorder=6)
    return magnitude / rim


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("traces", metavar="TRACE", type=Path, nargs="+")
    parser.add_argument("-o", "--output", type=Path, required=True,
                        help="output file, e.g. paths.svg, paths.png or paths.pdf")
    parser.add_argument("--title", help="figure title (default: first circuit name)")
    parser.add_argument("--digits", type=int, default=12, choices=range(1, 17),
                        metavar="1–16", help="precision for grouping lobes (default: 12)")
    args = parser.parse_args()

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    panels = []
    for path in args.traces:
        try:
            mode, counts = read_trace(path)
        except (OSError, ValueError) as error:
            parser.error(str(error))
        lobes, total, x = amplitude_groups(counts, args.digits)
        label = f"{mode} {'RGB' if mode == 'CBS' else 'ALL'}"
        n = sum(counts.values())
        phase = "undefined" if x is None else "∞" if math.isinf(x) else f"{x:.5g}"
        summary = f"{n:,} nonzero paths     |     X = {phase}"
        amplitude = "0" if not total else f"{total.real:.5g} {total.imag:+.5g}i"
        panels.append((lobes, total, label, summary, f"A = {amplitude}"))
        print(f"{path.name}: {summary}; A = {total!r}; {len(lobes)} amplitude groups")

    columns = min(len(panels), 3)
    rows = math.ceil(len(panels) / columns)
    fig = plt.figure(figsize=(4.8 * columns, 5.55 * rows), layout="constrained",
                     facecolor="white")
    grid = fig.add_gridspec(rows, columns)
    name = args.traces[0].stem.removesuffix("_paths").removesuffix("_CBS").removesuffix("_SS")
    fig.suptitle(args.title or f"{name} · Path amplitudes", fontsize=16, fontweight="bold")
    for index, (lobes, total, label, summary, caption) in enumerate(panels):
        cell = grid[index // columns, index % columns].subgridspec(
            2, 1, height_ratios=[9, 1.8])
        ax = fig.add_subplot(cell[0], projection="polar")
        overflow = draw(ax, lobes, total, label)
        footer = fig.add_subplot(cell[1])
        footer.axis("off")
        footer.text(.5, .80, summary, ha="center", va="center", fontsize=9.5,
                    bbox=dict(boxstyle="round,pad=.45", facecolor="#eef3f8", edgecolor="none"))
        footer.text(.5, .43, caption, ha="center", va="center", fontsize=9,
                    color="#c92435")
        if overflow:
            footer.text(.5, .10, f"Off scale · |A| is {overflow:.3g}× the rim radius",
                        ha="center", va="center", fontsize=8.5, color="#c92435")

    fig.savefig(args.output, dpi=210, bbox_inches="tight")


if __name__ == "__main__":
    main()
