# Circuit catalogue

Machine-readable catalogue: [`catalog.csv`](catalog.csv). Amplitudes are for the listed initial and target states.

RGB metrics unavailable for IQP_n25, SU_n25, RND_n16, and RND_n25: their Deucalion ARM RGB jobs timed out at the requested 8-hour limit (6 November 2026). The reference amplitudes remain as catalogued; nonzero-path count, X, and N_eff are left blank until an RGB run completes.

CLIFFORD output states and amplitudes were selected with Qiskit 2.6.1 Statevector from initial state `|0⟩`; the highest-probability state was used, with ties resolved by lowest state index.

RND_n08 output state and amplitude were computed with Qiskit 2.6.1 Statevector from `|0⟩`, selecting the highest-probability state (ties resolved by lowest state index). The RND_n12 target state and amplitude were computed with Qiskit 2.6.1 Statevector; the RND_n16 state and amplitude were computed with Qiskit 2.6.1 Statevector; the RND_n25 amplitude was supplied by the user. Qubit counts were checked against QASM declarations; layer counts are Qiskit circuit depths.

IQP output states and amplitudes were computed from `|0⟩` with Qiskit 2.6.1. `IQP_n05`, `IQP_n15` and `circuit_22` use `Statevector`; `IQP_n25` uses vectorized NumPy statevector evolution on the Qiskit-parsed circuit, validated against Qiskit `Statevector` on `IQP_n05` (maximum absolute difference `1.14e-16`). Ties for maximum probability are resolved by lowest state index.

SU output states and amplitudes were computed from `|0⟩` using Qiskit 2.6.1 `Statevector`, selecting the maximum-probability state (ties resolved by lowest state index).

HSC amplitudes come from the supplied transition specification. RND_8x9 amplitudes were computed with Qiskit 2.6.1 `Statevector`, starting at `|0⟩`; the state with the largest amplitude magnitude was selected (ties go to the lowest state index). All QASM files are OpenQASM 2.0, and filename/qubit counts were checked.

| Family | Circuit file | Qubits | Layers | Initial state | Target final state | Transition amplitude | nonZero paths | X | N_eff |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| CLIFFORD | [`CLIF_n12_T0.qasm`](CLIFFORD/CLIF_n12_T0.qasm) | 12 | 12 | 0 | 0 | `0.0441941738241591+4.93132006517368e-19i` | 131072 | 16384 | 131072 |
| CLIFFORD | [`CLIF_n12_T1.qasm`](CLIFFORD/CLIF_n12_T1.qasm) | 12 | 12 | 0 | 0 | `0.0441941738241591+4.93132006517368e-19i` | 131072 | 16384 | 131072 |
| CLIFFORD | [`CLIF_n12_T12.qasm`](CLIFFORD/CLIF_n12_T12.qasm) | 12 | 12 | 0 | 0 | `0.0441941738241591-0.0441941738241591i` | 131072 | 8192 | 131072 |
| CLIFFORD | [`CLIF_n12_T2.qasm`](CLIFFORD/CLIF_n12_T2.qasm) | 12 | 12 | 0 | 0 | `0.0533470869120795-0.0220970869120796i` | 131072 | 9597.52 | 131072 |
| CLIFFORD | [`CLIF_n12_T4.qasm`](CLIFFORD/CLIF_n12_T4.qasm) | 12 | 12 | 0 | 0 | `0.0533470869120795-0.0220970869120796i` | 131072 | 9597.52 | 131072 |
| CLIFFORD | [`CLIF_n12_T8.qasm`](CLIFFORD/CLIF_n12_T8.qasm) | 12 | 12 | 0 | 0 | `0.0441941738241591-0.0441941738241591i` | 131072 | 8192 | 131072 |
| CLIFFORD | [`CLIF_n4_T0.qasm`](CLIFFORD/CLIF_n4_T0.qasm) | 4 | 4 | 0 | 0 | `0.25+0.25i` | 4 | 2 | 4 |
| CLIFFORD | [`CLIF_n4_T1.qasm`](CLIFFORD/CLIF_n4_T1.qasm) | 4 | 4 | 0 | 0 | `0.25+0.25i` | 4 | 2 | 4 |
| CLIFFORD | [`CLIF_n4_T2.qasm`](CLIFFORD/CLIF_n4_T2.qasm) | 4 | 4 | 0 | 0 | `0.426776695296637+0.176776695296637i` | 4 | 1.17157 | 4 |
| CLIFFORD | [`CLIF_n4_T4.qasm`](CLIFFORD/CLIF_n4_T4.qasm) | 4 | 4 | 0 | 0 | `0.426776695296637+0.176776695296637i` | 4 | 1.17157 | 4 |
| CLIFFORD | [`CLIF_n8_T0.qasm`](CLIFFORD/CLIF_n8_T0.qasm) | 8 | 8 | 0 | 0 | `0+0.125i` | 128 | 64 | 128 |
| CLIFFORD | [`CLIF_n8_T1.qasm`](CLIFFORD/CLIF_n8_T1.qasm) | 8 | 8 | 0 | 0 | `0+0.125i` | 128 | 64 | 128 |
| CLIFFORD | [`CLIF_n8_T2.qasm`](CLIFFORD/CLIF_n8_T2.qasm) | 8 | 8 | 0 | 0 | `0+0.125i` | 128 | 64 | 128 |
| CLIFFORD | [`CLIF_n8_T4.qasm`](CLIFFORD/CLIF_n8_T4.qasm) | 8 | 8 | 0 | 0 | `0+0.125i` | 128 | 64 | 128 |
| CLIFFORD | [`CLIF_n8_T8.qasm`](CLIFFORD/CLIF_n8_T8.qasm) | 8 | 8 | 0 | 0 | `0+0.125i` | 128 | 64 | 128 |
| IQP | [`IQP_n05.qasm`](IQP/IQP_n05.qasm) | 5 | 17 | 0 | 24 | `0.4526650429449551+0.06249999999999989i` | 32 | 4.789 | 32 |
| IQP | [`IQP_n15.qasm`](IQP/IQP_n15.qasm) | 15 | 55 | 0 | 197 | `0.008984128387017364+0.014818966018026108i` | 32768 | 3329.82 | 32768 |
| IQP | [`IQP_n25.qasm`](IQP/IQP_n25.qasm) | 25 | 97 | 0 | 4895738 | `0.00025669238243816847-0.00065978780922006i` |  |  |  |
| IQP | [`circuit_22.qasm`](IQP/circuit_22.qasm) | 4 | 8 | 0 | 7 | `-0.35355339059327373-0.3017766952966365i` |  |  |  |
| SU | [`SU_n5.qasm`](SU/SU_n5.qasm) | 5 | 8 | 0 | 14 | `-0.1016833481405383+0.890063483521799i` | 32 | 1.00556 | 1.01117 |
| SU | [`SU_n6.qasm`](SU/SU_n6.qasm) | 6 | 13 | 0 | 22 | `0.3556027372283176-0.6353640336677097i` |  |  |  |
| SU | [`SU_n15.qasm`](SU/SU_n15.qasm) | 15 | 22 | 0 | 21858 | `-0.36158910429829016+0.2602722561313453i` | 1073741824 | 1.55695 | 1.58111 |
| SU | [`SU_n25.qasm`](SU/SU_n25.qasm) | 25 | 32 | 0 | 11061802 | `-0.03552666001884239+0.07270352937915184i` |  |  |  |
| RND | [`RND_n08.qasm`](RND/RND_n08.qasm) | 8 | 9 | 0 | 97 | `-0.2575825214724773-0.10669417382415909i` | 512 | 25.7293 | 512 |
| RND | [`RND_n10.qasm`](RND/RND_n10.qasm) | 10 | 13 | 0 | 0 | `0.02209708691207956+0.0533470869120795i` | 262144 | 76780.2 | 262144 |
| RND | [`RND_n12.qasm`](RND/RND_n12.qasm) | 12 | 15 | 0 | 17 | `0.05334708691207941-0.022097086912079525i` | 1073741824 | 7.86229e+07 | 1.07374e+09 |
| RND | [`RND_n16.qasm`](RND/RND_n16.qasm) | 16 | 22 | 0 | 78 | `-0.00804945379601487+0.004310755432004946i` |  |  |  |
| RND | [`RND_n25.qasm`](RND/RND_n25.qasm) | 25 | 31 | 0 | 0 | `0.00035204+0.00038255i` |  |  |  |
| HSC | [`HSC_n10.qasm`](HSC/HSC_n10.qasm) | 10 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n20.qasm`](HSC/HSC_n20.qasm) | 20 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n30.qasm`](HSC/HSC_n30.qasm) | 30 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n40.qasm`](HSC/HSC_n40.qasm) | 40 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n50.qasm`](HSC/HSC_n50.qasm) | 50 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n60.qasm`](HSC/HSC_n60.qasm) | 60 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n70.qasm`](HSC/HSC_n70.qasm) | 70 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n80.qasm`](HSC/HSC_n80.qasm) | 80 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n90.qasm`](HSC/HSC_n90.qasm) | 90 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n256.qasm`](HSC/HSC_n256.qasm) | 256 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n512.qasm`](HSC/HSC_n512.qasm) | 512 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n1024.qasm`](HSC/HSC_n1024.qasm) | 1024 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n2048.qasm`](HSC/HSC_n2048.qasm) | 2048 | — | 0 | 1023 | `1+0i` |  |  |  |
| HSC | [`HSC_n4096.qasm`](HSC/HSC_n4096.qasm) | 4096 | — | 0 | 1023 | `1+0i` |  |  |  |
| RND_8x9 | [`RND_8x9_900000.qasm`](RND_8x9/RND_8x9_900000.qasm) | 8 | 9 | 0 | 1 | `0.0625-0.0625i` | 32 | 16 | 32 |
| RND_8x9 | [`RND_8x9_900100.qasm`](RND_8x9/RND_8x9_900100.qasm) | 8 | 9 | 0 | 6 | `0.0625+0.150888347648318i` | 16 | 4.68629 | 16 |
| RND_8x9 | [`RND_8x9_900200.qasm`](RND_8x9/RND_8x9_900200.qasm) | 8 | 9 | 0 | 0 | `0.125+0i` | 1024 | 256 | 1024 |
| RND_8x9 | [`RND_8x9_900300.qasm`](RND_8x9/RND_8x9_900300.qasm) | 8 | 9 | 0 | 19 | `-0.125+0.088388347648318i` | 8192 | 1365.33 | 8192 |
| RND_8x9 | [`RND_8x9_900400.qasm`](RND_8x9/RND_8x9_900400.qasm) | 8 | 9 | 0 | 64 | `-0.150888347648318-0.0625i` | 4096 | 1199.69 | 4096 |
| RND_8x9 | [`RND_8x9_900500.qasm`](RND_8x9/RND_8x9_900500.qasm) | 8 | 9 | 0 | 36 | `-0.088388347648318+0.088388347648318i` | 256 | 64 | 256 |
| RND_8x9 | [`RND_8x9_900600.qasm`](RND_8x9/RND_8x9_900600.qasm) | 8 | 9 | 0 | 142 | `-0.150888347648318-0.150888347648318i` | 1024 | 87.8453 | 1024 |
| RND_8x9 | [`RND_8x9_900700.qasm`](RND_8x9/RND_8x9_900700.qasm) | 8 | 9 | 0 | 132 | `0-0.213388347648318i` | 4096 | 351.381 | 4096 |
| RND_8x9 | [`RND_8x9_900800.qasm`](RND_8x9/RND_8x9_900800.qasm) | 8 | 9 | 0 | 214 | `0.150888347648318+0.150888347648318i` | 4096 | 351.381 | 4096 |
| RND_8x9 | [`RND_8x9_900900.qasm`](RND_8x9/RND_8x9_900900.qasm) | 8 | 9 | 0 | 132 | `-0.125+0.301776695296636i` | 8192 | 299.923 | 8192 |
| RND_8x9 | [`RND_8x9_901000.qasm`](RND_8x9/RND_8x9_901000.qasm) | 8 | 9 | 0 | 8 | `0.125-0.301776695296636i` | 512 | 74.9807 | 512 |
| RND_8x9 | [`RND_8x9_901100.qasm`](RND_8x9/RND_8x9_901100.qasm) | 8 | 9 | 0 | 67 | `-0.03125+0.075444173824159i` | 33554432 | 1.96557e+07 | 3.35544e+07 |
| RND_8x9 | [`RND_8x9_901200.qasm`](RND_8x9/RND_8x9_901200.qasm) | 8 | 9 | 0 | 35 | `-0.301776695296636-0.125i` | 8192 | 599.845 | 8192 |
| RND_8x9 | [`RND_8x9_901300.qasm`](RND_8x9/RND_8x9_901300.qasm) | 8 | 9 | 0 | 8 | `0.150888347648318-0.150888347648318i` | 4096 | 702.762 | 4096 |
| RND_8x9 | [`RND_8x9_901400.qasm`](RND_8x9/RND_8x9_901400.qasm) | 8 | 9 | 0 | 8 | `0.044194173824159+0.106694173824159i` | 512 | 149.961 | 512 |
| RND_8x9 | [`RND_8x9_901500.qasm`](RND_8x9/RND_8x9_901500.qasm) | 8 | 9 | 0 | 64 | `-0.0625-0.364276695296636i` | 524288 | 14992.3 | 524288 |
| RND_8x9 | [`RND_8x9_901600.qasm`](RND_8x9/RND_8x9_901600.qasm) | 8 | 9 | 0 | 96 | `-0.150888347648318+0.0625i` | 256 | 74.9807 | 256 |
| RND_8x9 | [`RND_8x9_901700.qasm`](RND_8x9/RND_8x9_901700.qasm) | 8 | 9 | 0 | 61 | `-0.132582521472477-0.106694173824159i` | 2048 | 276.226 | 2048 |
| RND_8x9 | [`RND_8x9_901800.qasm`](RND_8x9/RND_8x9_901800.qasm) | 8 | 9 | 0 | 6 | `0.106694173824159+0.106694173824159i` | 32 | 5.49033 | 32 |
| RND_8x9 | [`RND_8x9_901900.qasm`](RND_8x9/RND_8x9_901900.qasm) | 8 | 9 | 0 | 56 | `0.213388347648318-0.088388347648318i` | 64 | 4.68629 | 64 |
| RND_8x9 | [`RND_8x9_902000.qasm`](RND_8x9/RND_8x9_902000.qasm) | 8 | 9 | 0 | 64 | `-0.132582521472477+0.132582521472477i` | 2048 | 455.111 | 2048 |
| RND_8x9 | [`RND_8x9_902100.qasm`](RND_8x9/RND_8x9_902100.qasm) | 8 | 9 | 0 | 8 | `0-0.0625i` | 4096 | 4096 | 4096 |
| RND_8x9 | [`RND_8x9_902200.qasm`](RND_8x9/RND_8x9_902200.qasm) | 8 | 9 | 0 | 0 | `-0.097541260736239-0.02209708691208i` | 8192 | 3199.17 | 8192 |
| RND_8x9 | [`RND_8x9_902300.qasm`](RND_8x9/RND_8x9_902300.qasm) | 8 | 9 | 0 | 104 | `-0.106694173824159-0.257582521472477i` | 262144 | 26346.8 | 262144 |
| RND_8x9 | [`RND_8x9_902400.qasm`](RND_8x9/RND_8x9_902400.qasm) | 8 | 9 | 0 | 0 | `0.075444173824159+0.03125i` | 32 | 18.7452 | 32 |
| RND_8x9 | [`RND_8x9_902500.qasm`](RND_8x9/RND_8x9_902500.qasm) | 8 | 9 | 0 | 0 | `0.213388347648318+0.088388347648318i` | 1024 | 74.9807 | 1024 |
| RND_8x9 | [`RND_8x9_902600.qasm`](RND_8x9/RND_8x9_902600.qasm) | 8 | 9 | 0 | 160 | `-0.106694173824159+0.169194173824159i` | 512 | 99.9742 | 512 |
| RND_8x9 | [`RND_8x9_902700.qasm`](RND_8x9/RND_8x9_902700.qasm) | 8 | 9 | 0 | 27 | `-0.213388347648318+0.088388347648318i` | 1024 | 74.9807 | 1024 |
| RND_8x9 | [`RND_8x9_902800.qasm`](RND_8x9/RND_8x9_902800.qasm) | 8 | 9 | 0 | 168 | `-0.075444173824159-0.075444173824159i` | 8192 | 2811.05 | 8192 |
| RND_8x9 | [`RND_8x9_902900.qasm`](RND_8x9/RND_8x9_902900.qasm) | 8 | 9 | 0 | 105 | `-0.728553390593273+0i` | 512 | 7.53594 | 512 |
| RND_8x9 | [`RND_8x9_903000.qasm`](RND_8x9/RND_8x9_903000.qasm) | 8 | 9 | 0 | 162 | `-0.275888347648318+0.0625i` | 16384 | 799.794 | 16384 |
| RND_8x9 | [`RND_8x9_903100.qasm`](RND_8x9/RND_8x9_903100.qasm) | 8 | 9 | 0 | 128 | `-0.182138347648318+0.03125i` | 512 | 58.5635 | 512 |
| RND_8x9 | [`RND_8x9_903200.qasm`](RND_8x9/RND_8x9_903200.qasm) | 8 | 9 | 0 | 146 | `-0.301776695296636+0.125i` | 256 | 18.7452 | 256 |
| RND_8x9 | [`RND_8x9_903300.qasm`](RND_8x9/RND_8x9_903300.qasm) | 8 | 9 | 0 | 2 | `-0.125-0.125i` | 8192 | 1024 | 8192 |
| RND_8x9 | [`RND_8x9_903400.qasm`](RND_8x9/RND_8x9_903400.qasm) | 8 | 9 | 0 | 25 | `-0.106694173824159+0.106694173824159i` | 256 | 87.8453 | 256 |
| RND_8x9 | [`RND_8x9_903500.qasm`](RND_8x9/RND_8x9_903500.qasm) | 8 | 9 | 0 | 104 | `0.213388347648318+0.088388347648318i` | 524288 | 38390.1 | 524288 |
| RND_8x9 | [`RND_8x9_903600.qasm`](RND_8x9/RND_8x9_903600.qasm) | 8 | 9 | 0 | 1 | `-0.0625-0.0625i` | 512 | 256 | 512 |
| RND_8x9 | [`RND_8x9_903700.qasm`](RND_8x9/RND_8x9_903700.qasm) | 8 | 9 | 0 | 8 | `0.125+0.125i` | 16384 | 4096 | 16384 |
| RND_8x9 | [`RND_8x9_903800.qasm`](RND_8x9/RND_8x9_903800.qasm) | 8 | 9 | 0 | 44 | `0.150888347648318+0.150888347648318i` | 16384 | 2811.05 | 16384 |
| RND_8x9 | [`RND_8x9_903900.qasm`](RND_8x9/RND_8x9_903900.qasm) | 8 | 9 | 0 | 16 | `-0.301776695296636-0.125i` | 4096 | 299.923 | 4096 |
| RND_8x9 | [`RND_8x9_904000.qasm`](RND_8x9/RND_8x9_904000.qasm) | 8 | 9 | 0 | 81 | `-0.301776695296636+0.301776695296636i` | 1024 | 21.9613 | 1024 |
| RND_8x9 | [`RND_8x9_904100.qasm`](RND_8x9/RND_8x9_904100.qasm) | 8 | 9 | 0 | 16 | `-0.125+0.088388347648318i` | 2048 | 341.333 | 2048 |
| RND_8x9 | [`RND_8x9_904200.qasm`](RND_8x9/RND_8x9_904200.qasm) | 8 | 9 | 0 | 134 | `-0.106694173824159-0.257582521472477i` | 8192 | 411.669 | 8192 |
| RND_8x9 | [`RND_8x9_904300.qasm`](RND_8x9/RND_8x9_904300.qasm) | 8 | 9 | 0 | 36 | `-0.106694173824159-0.106694173824159i` | 512 | 87.8453 | 512 |
| RND_8x9 | [`RND_8x9_904400.qasm`](RND_8x9/RND_8x9_904400.qasm) | 8 | 9 | 0 | 83 | `0.213388347648318+0i` | 128 | 21.9613 | 128 |
| RND_8x9 | [`RND_8x9_904500.qasm`](RND_8x9/RND_8x9_904500.qasm) | 8 | 9 | 0 | 16 | `-0.088388347648318-0.088388347648318i` | 4096 | 1024 | 4096 |
| RND_8x9 | [`RND_8x9_904600.qasm`](RND_8x9/RND_8x9_904600.qasm) | 8 | 9 | 0 | 18 | `-0.119638347648318-0.075444173824159i` | 16384 | 3199.17 | 16384 |
| RND_8x9 | [`RND_8x9_904700.qasm`](RND_8x9/RND_8x9_904700.qasm) | 8 | 9 | 0 | 8 | `-0.075444173824159-0.075444173824159i` | 32768 | 11244.2 | 32768 |
| RND_8x9 | [`RND_8x9_904800.qasm`](RND_8x9/RND_8x9_904800.qasm) | 8 | 9 | 0 | 45 | `-0.275888347648318+0.0625i` | 512 | 24.9936 | 512 |
| RND_8x9 | [`RND_8x9_904900.qasm`](RND_8x9/RND_8x9_904900.qasm) | 8 | 9 | 0 | 10 | `0-0.125i` | 128 | 64 | 128 |
| RND_8x9 | [`RND_8x9_905000.qasm`](RND_8x9/RND_8x9_905000.qasm) | 8 | 9 | 0 | 7 | `-0.176776695296637+0.176776695296637i` | 128 | 32 | 128 |

## Extending the catalogue

Add one CSV row per circuit. Use paths relative to this directory. To add a property, append a named column to the CSV header and populate it for existing rows when known. Update this Markdown table when adding circuits or changing displayed fields. `sha256` identifies the exact QASM file contents.
