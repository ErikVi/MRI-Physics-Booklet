# MRI Physics

**From Quantum Spin Dynamics to Advanced Acquisition and Reconstruction**

An advanced, self-contained MRI physics reference for maintaining technical
proficiency, research preparation and graduate-level interview study.

## Current milestone

This is the **initial architecture**, not a completed textbook. It contains
27 modular chapter files, six appendices, a detailed subsection hierarchy,
central notation and sign conventions, a small verified bibliography, and
build tooling. There are no filler chapter paragraphs, completed chapter
derivations, fabricated results or pretend implementations.

The requested chapter order is retained. Six parts group the material:

1. Mathematical foundations and spin dynamics (Chapters 1–4).
2. Encoding, signal formation and pulse sequences (5–8).
3. Contrast, quantification and signal pathways (9–13).
4. Accelerated imaging and reconstruction (14–16).
5. Hardware, sequence design and specialized measurements (17–21).
6. Artifacts, protocols and integrated reasoning (22–27).

See [the detailed outline](docs/OUTLINE.md) for every section and subsection,
[editorial standards](docs/EDITORIAL_STANDARDS.md) for drafting rules, and
[the source ledger](bibliography/SOURCES.md) for bibliography verification.
Each chapter begins with comments defining scope, prerequisites, planned
calculations, figures and challenge-problem types.

## Compilation

Run commands **from the repository root**. Use a current TeX Live distribution
(2023 or later recommended) or MiKTeX with pdfLaTeX, latexmk, Biber and MakeIndex.
The project uses biblatex with Biber; do not run classic BibTeX on main. The .bib
database uses standard BibTeX entry syntax.

On Debian/Ubuntu, the dependencies are:

    sudo apt-get install latexmk biber texlive-latex-extra texlive-fonts-recommended texlive-science

Build and check:

    python scripts/check_structure.py
    latexmk -pdf main.tex
    python scripts/check_build.py

Use python3 if that is your platform's Python command. latexmkrc places all
outputs in build/, runs the required bibliography/index tools, and repeats
LaTeX until references settle. The book is build/main.pdf. No shell escape,
external fonts, network calls or generated figures are needed during TeX runs.

A manual alternative (create build/ first) is:

    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
    biber --input-directory=build --output-directory=build main
    makeindex -o build/main.ind build/main.idx
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex

Run another LaTeX pass if the log asks for one. To remove generated files only:

    latexmk -C main.tex

GitHub Actions runs the same structural and build checks and uploads
mri-physics-book containing the PDF and diagnostics. A workflow file alone
does not establish successful compilation: inspect its run result. The
static Python checker is deliberately not a replacement for TeX.

This is a multi-file repository project. Editors that compile only a single
standalone buffer cannot validate it; open the whole project in a TeX-capable
editor or use the included CI. On Overleaf, import the repository, choose
main.tex and pdfLaTeX, and use its full TeX Live environment.

## Repository map

| Path | Purpose |
| --- | --- |
| main.tex | Title, front matter, part/chapter order and back matter |
| preamble/packages.tex | Package dependencies and bibliography backend |
| preamble/macros.tex | Semantic math commands |
| preamble/styles.tex | Typography, environments, headings and drawing styles |
| preamble/notation.tex | Typeset notation register and mathematical conventions |
| chapters/ | 27 separately editable chapters |
| appendices/ | Mathematical, Fourier, signal, constants, solution and reference-sheet appendices |
| bibliography/ | Verified seed references and source ledger |
| figures/tikz/, figures/generated/ | Editable diagrams and generated vector output |
| code/ | Reserved numerical demonstration modules |
| scripts/ | Structural and build-diagnostic checks |
| docs/ | Reviewable outline and editorial standards |
| .github/workflows/latex.yml | Automated full-project compilation |
| build/ | Ignored PDF and auxiliary output |

## Design decisions

Use A4, 10 pt, a two-sided book layout without forced blank recto pages,
Palatino text/math, restrained blue links and headings, numbered equations
and subsection-level contents. The cover has no author. Pedagogical
environments are unboxed. Index support is enabled; the notation register
serves as the initial symbol glossary. Appendix F is the final book component.

preamble/notation.tex is document content, despite living beside preamble
configuration; it must be loaded after begin-document. This keeps the requested
path while making the distinction explicit.

The source files themselves own the hierarchy. Update docs/OUTLINE.md when
editing headings. During focused drafting, use the documented includeonly
example in main.tex; always build the complete book before a release.

Planned examples and problem types are comments, not substantive chapter prose.
Solutions will be written in Appendix E when their problems are authored.
Numerical directories are reserved with .gitkeep files; no simulations are
claimed in this milestone. The seed references are intentionally selective.

## Open editorial work

No unresolved convention choice blocks drafting. Later chapters must define
their own model assumptions and calibrated units within the central contract.
Verify numerical constants, tissue ranges and current safety-standard editions
when their sections are written. Decide whether a separate acronym glossary is
useful once there is enough prose to assess it. Establish a project license
with the repository owner before distributing the book under a stated license.
