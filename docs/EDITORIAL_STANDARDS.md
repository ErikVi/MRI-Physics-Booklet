# Editorial and mathematical standards

The scope is a self-contained graduate reference for an applied physicist with
medical-physics training and prior quantitative MRI research. Completeness
determines length. The first milestone is architecture only.

## Derivation and pedagogy

Develop motivation, formal model, derivation, interpretation, implementation,
consequences, assumptions and a worked example where useful. State the domain
and dimensions of every variable at first use. Explain approximations before
using them; test limiting cases. Number equations that will be referenced.
Distinguish a model prediction from an empirical observation.

Use continuous technical prose. The available unboxed environments are
definition, physicalinterpretation, derivation, workedexample,
importantresult, commonmisconception, clinicalconnection, researchnote and
challengeproblem. Do not wrap every paragraph in an environment.

The conventions in preamble/notation.tex are normative. In particular:
- positive proton gamma, M+ = Mx + i My and negative precession phase;
- negative forward spatial Fourier exponent, positive inverse exponent;
- B1+ uses the explicitly stated negative-time phasor convention;
- a phase-zero positive flip magnitude sends +z toward +y;
- signed EPG orders and conjugate symmetry are explicit;
- complex noise covariance is twice a real-quadrature variance in one channel.

Never silently import a formula or RF matrix with another sign convention.
Keep spin density distinct from a density operator; keep receive weighting
distinct from a transmit field. Do not present exponential T2-star decay,
perfect spoiling, conjugate k-space symmetry or linear SNR scaling as universal.

## Scope ownership and reading dependencies

Chapter 1 owns mathematical prerequisites; Appendix A is their lookup reference.
Chapter 4 owns basic rotating-frame and RF signs; Chapter 18 owns pulse design.
Chapter 5 owns encoding geometry; Chapter 6 owns the receive forward model.
Chapters 7 and 8 own sequence dynamics. Chapter 13 revisits those dynamics in EPG.
Chapter 9 owns contrast mechanisms; Chapter 11 owns quantitative measurements.
Chapter 12 treats MRF as one family, using forward references to EPG and inverse
methods when needed. Chapter 14 owns coil acceleration; Chapter 15 owns
nonuniform sampling; Chapter 16 owns inverse problems and solvers.
Chapter 19 owns flow and ASL models, with qMRI cross-references from Chapter 11.
Chapter 22 owns artifact diagnosis; Chapter 24 owns coupled optimization.
Chapter 25 synthesizes mature developments and must not duplicate these chapters.
Chapter 26 explains hazard physics; verify operational standards when drafting.

The numerical order is retained from the request. Readers wanting EPG before
MRF may read Chapter 13 immediately after Chapter 8. This is a declared
forward dependency, not a circular derivation.

## Problems and solutions

Every major chapter has separate worked-example and challenge-problem sections.
Create difficult, multi-step problems, mixing derivation, design, estimation,
limiting cases, false reasoning and artifact diagnosis. State sufficient
numerical data and units; distinguish open-ended design from a unique answer.
Include cross-chapter integration. Avoid superficial recall questions.

Use a stable label such as prob:07:finite-tr-null inside challengeproblem.
Write the complete solution under the corresponding chapter section of
Appendix E using \begin{solution}{prob:07:finite-tr-null}. Include derivation,
numerical result, dimensions, interpretation and checks. Never put challenge
solutions next to questions. Chapter 27 can contain fully worked synthesis
examples, but its challenge solutions still belong in Appendix E.

## References, figures and reproducibility

Use ch:NN, sec:NN:topic, eq:NN:topic, fig:NN:topic, tab:NN:topic and
prob:NN:topic labels. Preserve existing labels when moving material. Prefer
cref/Cref rather than hard-coded numbers. Appendix labels are app:a through app:f.

Cite real sources for claims and methods, not decorative reading lists.
Record bibliographic metadata and use publisher DOI links when available.
Add foundational primary papers during substantive writing. Do not treat the
eight-entry seed database as comprehensive. Document standards by edition.

Use vector figures, units, consistent axes and the shared drawing styles.
Keep executable examples outside TeX. Compare simulations to analytic limits
and verify noise, sampling and sign conventions. No dependence on shell escape.

Use semantic index entries as prose is written. The notation register is a
symbol glossary; a separate acronym glossary can be added only if it reduces
duplication. Keep Appendix F compact and at the end; annotate formulas with
their assumptions and chapter references.
