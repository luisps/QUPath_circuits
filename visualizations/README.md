# QUPath visualizations

## Paths trace diagram

Open `clifford-ht-paths.html` in a web browser and use **Trace files** to select one or more QUPath `.data` files. The browser reads them locally, so the viewer works offline without a server. Select both `<circuit>_CBS_paths.data` and `<circuit>_SS_paths.data` for a side-by-side comparison. Select files for several circuits at once to switch among them using the **Circuit** menu. Use traces generated for the same input and output when comparing the two modes.

Time runs from top to bottom. Hover over nodes and edges for details, or use **Highlight state sequence** to inspect a path. In SS version 2 traces, nodes split when paths share a state ID but have different phase-adjusted prefix weights at the viewer's 12-significant-digit grouping precision. Older SS version 1 traces show state IDs only.

The viewer draws the polar diagrams below the path diagrams using the same loaded traces and **Circuit** selection. Hover over a lobe for its path count, amplitude magnitude, and phase.

## Polar diagram exports

`plot_path_amplitudes.py` reads one or more QUPath path traces and writes a static figure. From this directory, run the following commands with a Python environment that has Matplotlib installed.

```sh
python3 -m pip install matplotlib
python3 plot_path_amplitudes.py \
  ../CLIFFORD_H_T/CLIFFORD_H8_T8_CBS_paths.data \
  ../CLIFFORD_H_T/CLIFFORD_H8_T8_SS_paths.data \
  -o CLIFFORD_H8_T8_polar.svg
```

Pass a single trace for one panel. Choose an `.svg`, `.png`, or `.pdf` extension for the desired output format. Use `--help` to see the available options.

Each blue lobe groups paths with the same complex amplitude at the selected precision. The angle shows the phase, the radial length shows the magnitude of one path, and the angular width and label show the number of paths in the group. The red vector shows the coherent sum. A dashed arrow past the rim marks an off-scale sum, with its true magnitude relative to the rim shown below the panel. Each panel reports the nonzero path count and the inverse squared magnitude of the average phase, weighted by path magnitude.

### Generating the input traces

If the `.data` files are missing, build QUPath with the CMake option `-DQUPATH_BUILD_PATHS=ON` and build the `QUPath_paths` target. Run the instrumented executable with `/a RGB /c CBS` or `/a ALL /c SS`, using the same circuit and endpoints for both. For example, from this directory, replacing `/path/to/build` with your build directory:

```sh
/path/to/build/QUPath_paths /p "$PWD/../CLIFFORD_H_T" /f CLIFFORD_H8_T8.qasm /a RGB /c CBS /i 0 /o 0 /t 4
/path/to/build/QUPath_paths /p "$PWD/../CLIFFORD_H_T" /f CLIFFORD_H8_T8.qasm /a ALL /c SS /i 0 /o 0 /t 4
```

The executable saves each trace beside the QASM file. A new run replaces an existing trace of the same name.
