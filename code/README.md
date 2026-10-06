# Numerical companions

The subject directories are reserved for Python demonstrations, not completed
implementations. Use SI internally and convert display units explicitly.
Adopt the conventions in preamble/notation.tex, especially RF rotations,
DFT normalization, receive weighting, noise variance and EPG order shifts.

Planned modules:
- bloch/: rotating-frame propagators, FID, spin echo and gradient echo.
- epg/: signed-order operators, echo trains and isochromat comparisons.
- reconstruction/: DFT/aliasing, SENSE, GRAPPA concepts and NUFFT examples.
- diffusion/: waveform b-matrices, ADC and tensor fitting.
- qMRI/: relaxometry, calibration, likelihood and uncertainty.
- mrf/: signal dictionaries, matching and parameter ambiguity.

Keep reusable routines separate from figure-generation scripts. Document
dependencies when introduced; no numerical package is required by this
architecture. Fix random seeds, report units and exercise analytic limiting
cases before referring to a numerical result in the book.

The root scripts/ directory contains editorial structural checks, not MRI
simulators. Run python scripts/check_structure.py before compiling.
