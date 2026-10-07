# Source verification ledger

Metadata checked on 2026-10-07. These entries seed the architecture; extend them
when a substantive derivation needs a source. Do not add citations for appearance.

| Key | Verified record | Intended role |
| --- | --- | --- |
| bernstein2004 | [Publisher record](https://www.sciencedirect.com/book/monograph/9780120928613/handbook-of-mri-pulse-sequences) | Sequence design, RF and gradient timing |
| levitt2008 | [Publisher's bibliographic record in its book review](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/nbm.1356) | Quantum spin and NMR foundations; the entry cites the book, not the review |
| stejskal1965 | [Original published article, university-hosted copy](https://bayes.wustl.edu/Manual/SpinDiffusion.pdf) | Diffusion gradient derivation |
| pruessmann1999 | [Publisher DOI](https://doi.org/10.1002/(SICI)1522-2594(199911)42:5%3C952::AID-MRM16%3E3.0.CO;2-S) | SENSE and noise amplification |
| griswold2002 | [Publisher record](https://onlinelibrary.wiley.com/doi/10.1002/mrm.10171) | GRAPPA calibration and reconstruction |
| lustig2007 | [Publisher record](https://onlinelibrary.wiley.com/doi/10.1002/mrm.21391) | Compressed-sensing MRI |
| ma2013 | [Publisher record](https://www.nature.com/articles/nature11971) | Foundational MRF |
| weigel2015 | [Publisher record](https://onlinelibrary.wiley.com/doi/10.1002/jmri.24619) | EPG formalism; issue year 2015, online publication 2014 |

Before importing a source's formulas, translate its gyromagnetic, RF,
Fourier, reception and configuration-order conventions to this book's.
The seed database is deliberately selective. It is not a complete reading
list for the eventual 27 chapters. In particular, hardware, spectroscopy,
fMRI and safety require targeted sources during drafting. Safety limits
must cite the applicable edition and jurisdiction at that time.

## Foundational block (2026-10-07)

The chapter derivations use the book's declared conventions. New primary anchors:

| Key | Record | Use |
| --- | --- | --- |
| bloch1946 | [APS](https://journals.aps.org/pr/abstract/10.1103/PhysRev.70.460) | Induction and phenomenological Bloch dynamics; pages 460–474 also checked against publisher-deposited Crossref metadata |
| hahn1950 | [APS](https://journals.aps.org/pr/abstract/10.1103/PhysRev.80.580) | Spin-echo refocusing |
| torrey1956 | [APS](https://journals.aps.org/pr/abstract/10.1103/PhysRev.104.563) | Diffusion terms in magnetization evolution |
| mcconnell1958 | [Publisher DOI](https://doi.org/10.1063/1.1744152) | Coupled exchange equations; metadata checked against publisher-deposited Crossref record |
| shannon1949 | [IEEE](https://ieeexplore.ieee.org/document/1697831) | Sampling and recoverability |
| gudbjartsson1995 | [Author manuscript at NIH](https://pmc.ncbi.nlm.nih.gov/articles/PMC2254141/) | Rician magnitude noise and Rayleigh limit |
| hoult1976 | [Publisher DOI](https://doi.org/10.1016/0022-2364(76)90233-X) | Receive reciprocity and signal normalization; authors and pages checked against publisher-deposited Crossref record |
| lauterbur1973 | [Nature](https://www.nature.com/articles/242190a0) | Spatial encoding and image formation |

The examples specify rounded physical constants and model parameters explicitly.
No tissue relaxation value or example coil response is asserted as a universal
clinical constant. Later safety and operational standards remain outside this
foundational milestone.
