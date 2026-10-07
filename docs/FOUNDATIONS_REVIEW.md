# Foundational block review

Reviewed 2026-10-07. Scope: Chapters 1–6 and their 30 solutions in Appendix E.

## Content and mathematical review

The six chapters contain derivations, worked numerical examples and five
challenge problems each. Seven TikZ/PGFPlots figures are included as vectors.
The later chapters and reference appendices remain explicitly identified
outlines; this milestone does not claim that the whole textbook is complete.

Reviewed the equations and solutions against the central notation contract:
positive proton gamma, negative transverse precession phase, negative forward
Fourier exponent, active RF rotation by minus the flip magnitude, and receive
weights defined without an extra implicit conjugation. The lower density-matrix
off-diagonal entry encodes M-plus. Co-rotating RF amplitude is distinguished from
the peak amplitude of a linearly polarized field.

Checked dimensions of magnetic moment and energy, induction flux, gradient
strength/area/moments, spatial frequency, Fourier quadrature, diffusion
attenuation and noise covariance. The complex covariance convention is twice
one quadrature variance for a scalar proper complex channel. Temperature,
spin density, density operators and receive sensitivity have distinct roles.

Major limits reviewed include zero drive, zero detuning, zero relaxation,
static-offset echo refocusing, high-temperature polarization, finite-aperture
versus finite-spacing sampling, and singular/noninvertible encoding maps.
The solutions distinguish linear optimality from statistical independence.

## Reproducible verification

Run from the repository root:

    python scripts/check_structure.py
    python scripts/check_foundations.py
    latexmk -pdf main.tex
    python scripts/check_build.py

The numerical check requires NumPy 1.26 or newer. It passed 123 numerical and
dimensional assertions, including:
- random density-matrix unitary evolution versus independent Rodrigues rotations;
- arbitrary-phase pi-pulse conjugation and static-offset echoes;
- Cartesian RK4 integration versus closed-form detuned RF and recovery;
- weak-drive Bloch integration versus small-tip quadrature;
- biphasic excitation, Gaussian Fourier transforms and exact voxel integration;
- DFT inversion and full windowed-noise covariance;
- Fisher-information Schur complements and optimal linear weights.

These checks validate selected independent identities and numerical examples;
they do not constitute a formal proof of every equation. The source check also
verifies exactly one solution for each of the 30 problems, all seven figure
inputs, and substantive content in every foundational subsection.

The structural checker resolves chapter/appendix inclusion, labels and citation
keys. The bibliography now contains 16 real references; new source records and
their uses are documented in bibliography/SOURCES.md.

## Compilation and layout

The complete multi-file project was built with pdfLaTeX, Biber and MakeIndex
using TeX Live 2026. The book is build/main.pdf (112 pages, including the retained
later-chapter outlines and detailed contents). Final build diagnostics must pass
the command above: no unresolved references/citations, Biber errors or overfull
boxes.

All 112 pages were rendered for layout review. All seven figure pages and
representative derivation/problem/solution pages were inspected, with detailed
views of PDF pages 29, 34, 40, 44, 50, 52, 58, 103 and 108. A raster ink-bound
check found no horizontal content outside the outer 7.5% safety margins.
The sampling-axis label overlap, equation wrapping, cover-rule indentation and
an unbreakable chain of future-solution outline headings were corrected.

The open main.tex source was edited in place. The built-in editor compiler was
invoked but returned an environment error: "Unable to find standard directories
for platform". The successful full-project build above supplies compilation
verification; the editor preview's compiler remains an environment limitation.
No replacement source document was created. Generated PDFs and diagnostics stay
in the ignored build directory; the reusable sources and verification scripts
are committed.
