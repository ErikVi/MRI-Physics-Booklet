# Figure standards

Keep editable TikZ/PGFPlots sources in tikz/ and programmatically generated
vector PDFs in generated/. Avoid raster output for curves and diagrams.
Figure data and generation scripts belong in code/. Do not externalize TikZ
by default: the normal book build needs no shell escape.

Use the mri axis, mri rf, mri gradient, mri signal, mri guide and mri label
styles in preamble/styles.tex. Label axes with quantities and units; make RF
phase, gradient polarity and ADC windows explicit in timing diagrams. Use
line styles as well as restrained color so figures remain legible in grayscale.
State whether a diagram is schematic or quantitatively scaled.

Every generated figure should record its script, parameters, random seed
where relevant, and output filename. Caption the physical question answered
and the model assumptions. Add a stable fig:<chapter>:<topic> label.
No illustrative figures have been generated in this architecture pass.
