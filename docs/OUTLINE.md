# Detailed Book Outline

Architecture edition: headings are a writing plan, not completed chapters.
The authoritative hierarchy is in the chapter and appendix TeX files. Keep this
review copy synchronized when changing that hierarchy.


## Part 1: Mathematical Foundations and Spin Dynamics

### 1. Mathematical and Physical Foundations

Develop only the mathematics and electromagnetism needed for spin dynamics, encoding, noise and estimation; derive prerequisites at their first useful level.

- **1.1 Complex representation and dimensional reasoning**: Complex numbers, Euler's formula and phasors; Frequency, angular frequency and phase; SI units, scaling and dimensional checks.
- **1.2 Linear algebra for spin and encoding**: Vector spaces, inner products and adjoints; Eigenvalues, eigenvectors and matrix exponentials; Singular values, rank and conditioning.
- **1.3 Fourier analysis and linear systems**: Transform pairs and distributions; Convolution, filtering and impulse responses; Sampling, Nyquist limits and discrete transforms.
- **1.4 Probability and measurement noise**: Random variables, expectations and covariance; Gaussian complex noise and magnitude statistics; Likelihood, bias and propagation of uncertainty.
- **1.5 Estimation and experimental information**: Least squares and maximum likelihood; Fisher information and the Cramer--Rao bound; Identifiability and nuisance parameters.
- **1.6 Fields, dipoles and angular momentum**: Maxwell equations and quasistatic limits; Magnetic dipole energy and torque; Angular momentum and rotating coordinates.
- **1.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **1.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Phasor signs, sampling limits and covariance propagation. Planned figures: Complex plane, convolution, sampling replicas.

### 2. Quantum Spin Physics

Derive spin-half dynamics, thermal polarization and the density-matrix bridge to ensemble magnetization; distinguish single-spin coherence from ensemble averages.

- **2.1 Spin as intrinsic angular momentum**: States, measurement bases and superposition; Pauli matrices and spin operators; Commutators, uncertainty and eigenstates.
- **2.2 Magnetic moments and Zeeman splitting**: Gyromagnetic ratio and Hamiltonian; Energy levels and transition frequencies; Positive and negative gyromagnetic ratios.
- **2.3 Unitary time evolution**: Schrodinger evolution and propagators; Relative phase and Larmor precession; Expectation values and the classical torque equation.
- **2.4 Density operators and ensembles**: Pure states, mixtures and coherence; Bloch-vector representation and positivity; Dephasing versus loss of single-spin coherence.
- **2.5 Thermal equilibrium and polarization**: Partition function and Boltzmann populations; High-temperature expansion and its accuracy; Spin density and macroscopic magnetization.
- **2.6 Driven spins and the classical limit**: RF interaction Hamiltonian; Rotating-wave approximation and resonance; Ensemble Bloch dynamics and hidden microscopic physics.
- **2.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **2.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Larmor frequencies at 1.5, 3 and 7 T; Boltzmann population differences and magnetization. Planned figures: Zeeman levels, measurement bases and Bloch sphere.

### 3. Classical Magnetization and the Bloch Equations

Construct the phenomenological Bloch model from torque and equilibration; solve free evolution and connect reversibility, relaxation and exchange.

- **3.1 From magnetic torque to ensemble dynamics**: Torque equation and conserved magnitude; Equilibrium magnetization and phenomenological relaxation; Assumptions of the single-pool Bloch model.
- **3.2 Solutions in a static field**: Longitudinal recovery and inversion; Complex transverse solution and phase; Affine propagators and piecewise-constant fields.
- **3.3 Inhomogeneous ensembles**: Frequency distributions and free induction decay; T2, T2-star and reversible broadening; Limits of exponential effective relaxation.
- **3.4 Driven and time-dependent dynamics**: Constant effective-field solution; Numerical integration and operator splitting; Accuracy, stability and conservation checks.
- **3.5 Beyond independent stationary spins**: Bloch--Torrey transport and diffusion; Bloch--McConnell exchange structure; Where phenomenology requires microscopic input.
- **3.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **3.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Longitudinal recovery, transverse decay and an inhomogeneous ensemble. Planned figures: Relaxation curves and isochromat refocusing.

### 4. RF Excitation and the Rotating Frame

Establish exact frame transformations and RF phase conventions before treating excitation, inversion and selective pulses.

- **4.1 Rotating coordinate systems**: Active rotations versus passive coordinates; Transformation of time derivatives; Detuning and the effective field.
- **4.2 Circular RF components**: Real fields and complex phasors; Co-rotating B1-plus and counter-rotating fields; Linear polarization and the rotating-wave approximation.
- **4.3 Hard-pulse dynamics**: Flip angle, RF phase and rotation axis; On-resonance excitation and inversion; Off-resonance excitation and bandwidth.
- **4.4 Pulse imperfections and calibration**: Transmit inhomogeneity and flip-angle errors; Finite-duration effects and relaxation; Phase cycling and receiver phase.
- **4.5 Selective excitation as an introduction**: Slice-selection gradients and RF bandwidth; Small-tip response and pulse envelopes; Boundaries of the hard-pulse approximation.
- **4.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **4.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Rotating-frame transformation and flip angle of a rectangular RF pulse. Planned figures: Laboratory and rotating axes; effective-field trajectories.


## Part 2: Encoding, Signal Formation and Pulse Sequences

### 5. Spatial Encoding and k-Space

Derive spatial phase accumulation and trajectory geometry, with sampling definitions separated from effective resolution.

- **5.1 Gradient fields and spatial phase**: Linear field expansion and gradient units; Phase accumulation and trajectory origin; Refocusing pulses and effective gradient signs.
- **5.2 Slice selection and partition encoding**: Frequency-to-position mapping; Slice rephasing and finite pulse duration; Two-dimensional slices versus three-dimensional slabs.
- **5.3 Frequency and phase encoding**: Readout gradients and dwell time; Phase-encoding steps and Cartesian grids; Echo position and prephasing.
- **5.4 Sampling geometry**: Field of view and k-space spacing; Finite extent, nominal resolution and voxel grid; Nyquist sampling, aliasing and zero filling.
- **5.5 Trajectory families and ordering**: Cartesian and echo-planar trajectories; Radial and spiral sampling; Linear, centric and interleaved view ordering.
- **5.6 Gradient moments and trajectory fidelity**: Zeroth and higher moments; Gradient delays and eddy-current errors; Concomitant fields and nonlinear encoding.
- **5.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **5.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Slice thickness, gradient strength, FOV, k-space extent and pixel spacing. Planned figures: Slice selection, Cartesian, radial, spiral and EPI trajectories.

### 6. Signal Formation and Fourier Imaging

Derive reception and the MRI forward model, then identify exactly when Fourier inversion is justified; establish PSF and complex-noise language.

- **6.1 From precession to received voltage**: Faraday induction and reciprocity; Complex demodulation and receiver phase; Receive sensitivity and signal normalization.
- **6.2 The MRI signal equation**: Spatial integration of transverse magnetization; Encoding, relaxation and off-resonance during readout; Motion, multiple species and model limitations.
- **6.3 The Fourier imaging limit**: Stationary object and time-independent weighting; Forward and inverse transform conventions; Discrete sampling and voxel integration.
- **6.4 Image formation and point-spread functions**: Finite support and truncation; Apodization, convolution and effective resolution; Center and periphery without oversimplification.
- **6.5 Incomplete and modified Fourier data**: Partial Fourier and conjugate-symmetry assumptions; Phase estimation and homodyne concepts; Zero padding, interpolation and display grids.
- **6.6 Complex images and noise**: DFT normalization and covariance; Phase images, magnitude images and noise floors; Receive weighting and the meaning of image intensity.
- **6.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **6.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Two-point object, finite readout blur and noise through a DFT. Planned figures: Receive sensitivity, Fourier pairs and point-spread functions.

### 7. Basic Pulse Sequences

Build FID, spin echo, gradient echo, spoiled GRE and inversion recovery from explicit magnetization histories; establish the sequence vocabulary used later.

- **7.1 Reading a sequence diagram**: RF, gradient and ADC event tracks; TR, TE, TI and timing references; Two-dimensional and three-dimensional acquisition loops.
- **7.2 Free induction and Hahn spin echo**: FID and static phase dispersion; Refocusing and echo formation; What a spin echo does and does not reverse.
- **7.3 Gradient echoes**: Gradient reversal and echo time; T2-star weighting and signal phase; Comparison with RF refocusing.
- **7.4 Spoiled gradient echo**: Longitudinal recurrence and steady state; FLASH and SPGR families; Ernst angle and the limits of perfect spoiling.
- **7.5 Inversion and saturation recovery**: Finite-TR signal equations; Null times and imperfect inversion; STIR, FLAIR and contrast-selective suppression.
- **7.6 Sequence comparisons**: Transient versus steady-state acquisition; SNR efficiency and scan-time accounting; Clinical examples and hidden model assumptions.
- **7.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **7.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Spin-echo signal, spoiled-GRE signal, Ernst angle and inversion null time. Planned figures: FID, Hahn echo, GRE and inversion-recovery timing diagrams.

### 8. Advanced Pulse Sequences

Develop echo trains, coherent steady states and prepared acquisitions; introduce pathway effects physically and defer their full algebra to Chapter 13.

- **8.1 Fast and turbo spin echo**: CPMG conditions, RARE and FSE/TSE; Stimulated echoes and variable refocusing angles; Echo-train modulation, effective TE and blurring.
- **8.2 Balanced steady-state free precession**: Balanced gradient moments and coherent steady state; Frequency response, phase cycling and banding; Startup transients and cardiac cine.
- **8.3 Echo-planar imaging**: Gradient-echo and spin-echo EPI; Echo spacing, segmentation and readout duration; Odd-even phase errors and distortion mechanisms.
- **8.4 Multi-echo and hybrid acquisitions**: Multi-echo GRE and spin-echo trains; GRASE and mixed relaxation weighting; Temporal ordering and contrast consistency.
- **8.5 Prepared three-dimensional imaging**: Magnetization preparation and readout perturbation; MPRAGE and inversion efficiency; MP2RAGE combination and residual dependencies.
- **8.6 Chemical-species and multislice strategies**: Dixon phase evolution and echo placement; Simultaneous multislice acquisition; Preparation modules and links to MT, diffusion and ASL.
- **8.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **8.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: bSSFP off-resonance response, effective TE and prepared GRE transients. Planned figures: TSE, bSSFP, EPI and MPRAGE timing.


## Part 3: Contrast, Quantification and Signal Pathways

### 9. Contrast and Relaxation

Connect relaxation models, exchange and susceptibility to sequence-dependent tissue contrast without treating tissue constants as universal.

- **9.1 Microscopic origins of relaxation**: Fluctuating fields and correlation functions; Spectral density, T1 and T2; Field strength and molecular-motion regimes.
- **9.2 Susceptibility and transverse dephasing**: Microscopic and macroscopic field variation; Reversible and irreversible signal loss; Spin-echo versus gradient-echo contrast.
- **9.3 Exchange and magnetization transfer**: Two-pool exchange models; Bound-pool saturation and MT contrast; MTR, quantitative MT and model dependence.
- **9.4 Contrast preparation**: Inversion, saturation and T2 preparation; Fat suppression and spectral selectivity; Spin locking and T1-rho concepts.
- **9.5 Contrast agents and tissue models**: Relaxivity, concentration and nonlinear effects; Compartmentation and exchange limitations; Tissue variability and sequence dependence.
- **9.6 Contrast interpretation**: Weighting versus parameter measurement; Clinical uses of T1, T2 and susceptibility; Failure of simple contrast heuristics.
- **9.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **9.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Competing tissue contrast and multi-pool relaxation. Planned figures: Spectral densities, exchange and contrast curves.

### 10. Diffusion MRI

Derive diffusion encoding from stochastic motion and gradient waveforms; progress from ADC to tensor and limited non-Gaussian models with clear identifiability boundaries.

- **10.1 Stochastic motion and transport**: Brownian motion and the diffusion equation; Gaussian propagator and mean-square displacement; Characteristic functions and displacement encoding.
- **10.2 Gradient-waveform encoding**: Stejskal--Tanner experiment and finite pulses; General waveform b-value and b-matrix; Imaging-gradient cross-terms and diffusion time.
- **10.3 Apparent diffusion and tensor imaging**: ADC and log-signal fitting; Diffusion tensor, eigenvectors and eigenvalues; Mean diffusivity, fractional anisotropy and invariants.
- **10.4 Beyond Gaussian diffusion**: Restricted diffusion and time dependence; Diffusion kurtosis and cumulant limits; Multi-compartment models and IVIM.
- **10.5 Acquisition and correction**: Spin-echo EPI and diffusion preparation; Motion, eddy currents and susceptibility distortion; Gradient nonlinearity, b-vector rotation and noise-floor bias.
- **10.6 Interpretation and advanced encoding**: Acute ischemia and oncologic examples; Tractography, crossing fibers and inference limits; Oscillating gradients and tensor-valued encoding.
- **10.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **10.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Stejskal--Tanner b-value, general b-matrix and tensor metrics. Planned figures: Brownian propagators, diffusion gradients and tensor ellipsoids.

### 11. Quantitative MRI

Organize quantitative measurements around forward models, calibration, identifiability and uncertainty; provide balanced coverage across parameter families.

- **11.1 Quantification as an inverse problem**: Forward models, nuisance parameters and calibration; Likelihoods for complex and magnitude data; Bias, precision, accuracy and repeatability.
- **11.2 Longitudinal relaxometry**: Inversion and saturation recovery; Variable flip angles and B1-plus correction; Look--Locker readout perturbation and mapping strategies.
- **11.3 Transverse relaxometry and proton density**: Multi-echo T2 and stimulated-echo contamination; T2-star, nonexponential decay and echo sampling; Proton density, receive bias and scaling ambiguity.
- **11.4 Field and transmit mapping**: B0 phase differences and phase unwrapping; B1-plus mapping and flip-angle calibration; Spatial regularization and calibration transfer.
- **11.5 Susceptibility, exchange and perfusion**: QSM forward dipole model and inversion ambiguity; MTR, quantitative MT and exchange estimates; Perfusion parameters and ASL quantification links.
- **11.6 Multiparametric estimation**: Joint models and parameter coupling; Fisher information, uncertainty and noise propagation; Multi-parametric mapping and synthetic MRI.
- **11.7 Validation and experimental design**: Ground truth, phantoms and repeat scans; Model mismatch and residual analysis; Sampling design under scan-time constraints.
- **11.8 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **11.9 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: T1/T2 fits, B0 phase unwrapping, uncertainty and protocol optimization. Planned figures: Signal families, likelihood contours and parameter covariance.

### 12. Magnetic Resonance Fingerprinting

Treat MRF as one transient quantitative acquisition family; connect spin dynamics, sampling and inference without duplicating the general qMRI or inverse-problem chapters.

- **12.1 Transient multiparametric encoding**: Variable flip angles, TR and preparation; Bloch and EPG signal evolution; Sequence diversity versus parameter sensitivity.
- **12.2 Dictionary inference**: Simulation grids and normalization; Matching metrics and proton-density scaling; Discretization, interpolation and nuisance parameters.
- **12.3 Acquisition and reconstruction**: Undersampling and temporal artifacts; Low-rank subspaces and compressed dictionaries; Model-based and iterative alternatives.
- **12.4 Experiment design and uncertainty**: Identifiability and correlated fingerprints; Fisher information and sequence optimization; B0, B1-plus, motion and model mismatch.
- **12.5 Validation and comparison**: Repeatability and phantom validation; Fair scan-time and resolution comparisons; Clinical opportunities and unresolved limitations.
- **12.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **12.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Normalized matching, proton-density recovery and dictionary discretization error. Planned figures: Transient fingerprints and parameter ambiguity.

### 13. Extended Phase Graphs and Signal Pathways

Derive EPG from spatial Fourier coefficients and the declared rotation convention; track transverse and longitudinal states through RF, relaxation and gradients.

- **13.1 Configuration-state representation**: Spatial harmonics and averaging; F-plus, F-minus and longitudinal Z states; Signed orders, conjugacy and observable echoes.
- **13.2 EPG operators**: RF transition matrix from Bloch rotations; Relaxation, recovery and off-resonance; Gradient shifts and state truncation.
- **13.3 Echo pathways**: Hahn echoes and stimulated echoes; Crushers, spoiling and coherence selection; Phase cycling and pathway interference.
- **13.4 Echo trains and steady states**: CPMG and variable-angle FSE/TSE; Spoiled GRE and incomplete spoiling; SSFP and transient MRF applications.
- **13.5 Extensions and numerical verification**: Diffusion weighting along pathways; Slice profiles and noninteger dephasing; Convergence and comparison with Bloch ensembles.
- **13.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **13.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Stimulated echo, CPMG echo train and imperfect spoiling. Planned figures: Signed-order EPG state evolution and pathway diagrams.


## Part 4: Accelerated Imaging and Reconstruction

### 14. Parallel Imaging

Derive coil encoding, SENSE, GRAPPA and noise amplification; separate acceleration geometry from reconstruction assumptions.

- **14.1 Receive arrays as encoding systems**: Sensitivity fields and folded voxels; Noise covariance and prewhitening; Optimal coil combination and normalization.
- **14.2 SENSE reconstruction**: Local unfolding equations; Weighted least squares and conditioning; Noise propagation and g-factor.
- **14.3 GRAPPA reconstruction**: Autocalibration and neighborhood kernels; Calibration fits and synthesized samples; Noise correlations and calibration failure.
- **14.4 Simultaneous multislice reconstruction**: Slice separation and coil geometry; CAIPIRINHA shifts and controlled aliasing; Slice leakage and reconstruction trade-offs.
- **14.5 Practical acceleration limits**: Calibration overhead and net acceleration; Motion and sensitivity mismatch; Regularization, residual aliasing and SNR efficiency.
- **14.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **14.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Two-coil SENSE inversion and g-factor SNR penalty. Planned figures: Aliased voxels, sensitivity vectors and GRAPPA neighborhoods.

### 15. Non-Cartesian and Accelerated Imaging

Connect nonuniform sampling to gridding and operator-based reconstruction; explain acceleration as a joint sampling and prior-design problem.

- **15.1 Radial and spiral acquisition**: Angular sampling and golden-angle ordering; Spiral geometry and variable density; Stack-of-stars and three-dimensional trajectories.
- **15.2 Nonuniform Fourier reconstruction**: Gridding kernels and oversampling; Deapodization and density compensation; NUFFT forward and adjoint operators.
- **15.3 Trajectory and field errors**: Gradient delays and measured trajectories; Off-resonance blur and time segmentation; Motion robustness and self-navigation limits.
- **15.4 Sampling for acceleration**: Variable-density masks and incoherence; Partial Fourier with complex phase; Joint coil and sampling design.
- **15.5 Dynamic imaging**: Temporal interleaving and view sharing; Spatiotemporal undersampling and low-rank structure; Temporal footprint versus nominal frame rate.
- **15.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **15.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Radial sampling density, spiral off-resonance and adjoint checks. Planned figures: Trajectories, interpolation kernels and undersampling PSFs.

### 16. Reconstruction and Inverse Problems

Build an operator-based account of reconstruction from least squares to regularization and model-based inference; restrict learned methods to physics, stability and validation.

- **16.1 The discrete forward model**: Encoding operators and discretization; Adjoint versus inverse and inner-product tests; Noise whitening and likelihood.
- **16.2 Linear reconstruction**: Least squares, pseudoinverses and rank; Tikhonov regularization and singular-value filtering; Conditioning, resolution matrices and uncertainty.
- **16.3 Sparsity and compressed sensing**: Transform sparsity and incoherent measurements; L1 and total-variation objectives; Sampling assumptions and failure cases.
- **16.4 Iterative algorithms**: Conjugate gradients and normal equations; Proximal gradients and variable splitting; Stopping rules, preconditioning and data consistency.
- **16.5 Low-rank and model-based reconstruction**: Dynamic subspaces and low-rank penalties; Joint image and parameter estimation; Nonconvexity, initialization and identifiability.
- **16.6 Learned reconstruction**: Learned priors and unrolled optimization; Distribution shift, hallucination and uncertainty; Validation with residuals and task-based metrics.
- **16.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **16.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Tikhonov solution, adjoint consistency and iterative convergence. Planned figures: Singular spectra, bias-variance curves and reconstruction residuals.


## Part 5: Hardware, Sequence Design and Specialized Measurements

### 17. MRI Hardware

Explain the magnet, gradient and RF subsystems as physical implementations of earlier models; connect imperfections to encoding and safety limits.

- **17.1 Main magnet and field control**: Superconductivity, persistent currents and cryogenics; Homogeneity, drift and passive shimming; Active shims and field monitoring.
- **17.2 Gradient subsystem**: Maxwell pairs, Golay coils and linearity; Amplifiers, inductance, amplitude and slew; Eddy currents, mechanical vibration and PNS links.
- **17.3 RF transmit subsystem**: Birdcage coils, quadrature and loading; B1-plus fields and transmit calibration; Parallel transmission and coupling.
- **17.4 RF receive subsystem**: Surface coils and phased arrays; Coil sensitivity, sample noise and preamplifiers; Decoupling, matching and transmit-receive protection.
- **17.5 Receiver and control chain**: Mixing, filtering and complex demodulation; ADC bandwidth, dynamic range and quantization; Timing, synchronization and gradient monitoring.
- **17.6 System-level limitations**: Field strength and noise regimes; Calibration drift and quality assurance; Hardware constraints in sequence design.
- **17.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **17.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Gradient slew, receive-noise budget and digitization timing. Planned figures: Magnet cross-section, Maxwell/Golay coils and receiver chain.

### 18. RF Pulses and Sequence Design

Develop selective excitation and constrained sequence synthesis using the established RF conventions; distinguish mathematical designs from scanner-feasible waveforms.

- **18.1 Selective excitation theory**: Small-tip-angle integral and excitation k-space; Sinc pulses, apodization and slice profiles; RF bandwidth and time-bandwidth product.
- **18.2 Large-tip and robust pulses**: Composite rotations and error compensation; Adiabatic following and inversion; SLR design and excitation-refocusing differences.
- **18.3 Multidimensional and multiband excitation**: Spatially selective trajectories; Multiband phases and peak RF power; Parallel transmit design and local heating constraints.
- **18.4 Joint RF and gradient design**: VERSE and waveform reparameterization; Off-resonance and relaxation limitations; Gradient amplitude, slew and raster constraints.
- **18.5 Sequence timing and gradient moments**: Trapezoid design and minimum duration; Rephasing, crushers and flow compensation; TE, TR and echo-spacing feasibility.
- **18.6 Design verification**: Bloch simulation across position and detuning; Slice-profile and pathway validation; SAR implications and scanner implementation checks.
- **18.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **18.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Time-bandwidth product, slice thickness and minimum gradient timing. Planned figures: Sinc profiles, excitation k-space and gradient ramps.

### 19. Flow, Perfusion and Angiography

Derive motion-induced phase and inflow contrast; develop phase contrast, TOF and ASL with explicit timing, calibration and physiological assumptions.

- **19.1 Motion in gradient fields**: Position expansion and gradient moments; Constant velocity, acceleration and intravoxel dispersion; Flow compensation and residual sensitivity.
- **19.2 Phase-contrast imaging**: Bipolar encoding and velocity phase; VENC, phase wrapping and noise; Background phase and multi-directional flow.
- **19.3 Inflow and angiographic contrast**: Time-of-flight saturation and fresh spins; Slice/slab geometry and venous suppression; Contrast-enhanced angiography and timing.
- **19.4 Arterial spin labeling**: Pulsed, continuous and pseudocontinuous labeling; Label-control subtraction and kinetic models; Transit time, labeling efficiency and quantification.
- **19.5 Applications and limitations**: Vascular stenosis and complex flow; Cardiac gating and four-dimensional flow; Perfusion versus macrovascular contamination.
- **19.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **19.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Gradient moments, velocity encoding and ASL timing. Planned figures: Bipolar gradients, inflow saturation and label-control timing.

### 20. Magnetic Resonance Spectroscopy

Connect spin interactions and localization to measured spectra, including acquisition constraints and fitting ambiguity.

- **20.1 Chemical shifts and spin interactions**: Shielding and ppm references; J-coupling and coupled-spin Hamiltonians; Weak coupling, multiplets and evolution.
- **20.2 From FID to spectrum**: Spectral Fourier transform and frequency sign; Linewidth, T2-star and apodization; Dwell time, spectral width and frequency resolution.
- **20.3 Localization**: Slice-selective localization and chemical-shift displacement; PRESS spin echoes; STEAM stimulated echoes and mixing time.
- **20.4 Acquisition practice**: Shimming and field stability; Water and lipid suppression; Single-voxel and spectroscopic imaging.
- **20.5 Spectral modeling and interpretation**: Basis spectra, phase and baseline; Metabolites, concentration and reference scaling; Fitting uncertainty, artifacts and biological specificity.
- **20.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **20.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Chemical shift in ppm, spectral resolution and linewidth. Planned figures: Coupled levels, spectra, PRESS and STEAM timing.

### 21. Functional MRI

Develop BOLD signal formation and acquisition trade-offs before a limited statistical treatment; distinguish vascular inference from direct neuronal measurement.

- **21.1 BOLD contrast physics**: Deoxyhemoglobin and susceptibility; Intravascular and extravascular contributions; Gradient-echo and spin-echo sensitivity.
- **21.2 Neurovascular coupling**: Blood flow, volume and oxygen metabolism; Hemodynamic response and temporal variability; Vascular specificity and limitations.
- **21.3 Acquisition design**: EPI, TE and echo spacing; Spatial resolution, temporal resolution and SMS; Distortion, dropout and physiological noise.
- **21.4 Time-series inference**: Drift, motion and nuisance regressors; General linear model and correlated noise; Multiple comparisons and statistical interpretation.
- **21.5 Limits and validation**: Confounding and causal claims; Task and resting-state measurements; Reproducibility and acquisition-dependent bias.
- **21.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **21.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: TE dependence, temporal sampling and physiological-noise limits. Planned figures: Hemodynamic response and temporal sampling.


## Part 6: Artifacts, Protocols and Integrated Reasoning

### 22. Artifacts and Corrections

Use a uniform causal account for each artifact: physics, mathematical model, appearance, parameter dependence, diagnosis, mitigation and cost.

- **22.1 Motion and flow artifacts**: Inconsistent phase encoding and ghosting; Rigid motion, deformation and intra-readout motion; Navigators, gating and prospective correction.
- **22.2 EPI-specific errors**: Odd-even mismatch and Nyquist ghosts; Off-resonance geometric distortion and pile-up; Signal dropout and correction limits.
- **22.3 Chemical shift and field inhomogeneity**: Frequency displacement and fat-water cancellation; Susceptibility, B0 drift and shimming; B1 inhomogeneity, dielectric shading and fat-suppression failure.
- **22.4 Sampling and finite resolution**: Aliasing and wraparound; Gibbs ringing and truncation; Partial volume and interpolation artifacts.
- **22.5 Hardware-related errors**: RF interference and zipper artifacts; Eddy currents and trajectory delays; Gradient nonlinearity and concomitant fields.
- **22.6 Reconstruction-related errors**: Parallel-imaging residual aliasing and noise; Non-Cartesian streaking and blur; Regularization, learned priors and synthetic structure.
- **22.7 Diagnosis and correction trade-offs**: Parameter perturbations as controlled experiments; Correction-induced noise and resolution loss; Validation against raw data and independent acquisitions.
- **22.8 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **22.9 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Chemical-shift displacement, EPI distortion and ghost offsets. Planned figures: Artifact-producing k-space errors and corrected/uncorrected PSFs.

### 23. Clinical Protocol Physics

Synthesize sequence and parameter choices by clinical objective, with anatomy used for examples rather than the book's organizing principle.

- **23.1 From diagnostic task to acquisition**: Target contrast and spatial scale; Motion, timing and patient constraints; Redundancy, uncertainty and protocol robustness.
- **23.2 Brain protocols**: Structural MPRAGE and FLAIR suppression; Acute ischemia and diffusion interpretation; Susceptibility, hemorrhage and T2-star.
- **23.3 Cardiac protocols**: bSSFP cine and off-resonance management; Gating, motion and temporal resolution; Late gadolinium enhancement and inversion timing.
- **23.4 Liver and abdominal protocols**: Breath holding and respiratory motion; Dixon, fat fraction and iron-sensitive decay; Diffusion and dynamic contrast timing.
- **23.5 Musculoskeletal and oncologic protocols**: Fat suppression and fluid-sensitive imaging; Spatial resolution and partial-volume control; Multiparametric tumor assessment and specificity.
- **23.6 Vascular protocol synthesis**: TOF, phase contrast and contrast enhancement; Velocity range and flow artifacts; Choosing coverage, resolution and scan time.
- **23.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **23.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Brain FLAIR, cardiac cine/LGE and liver fat-water protocol comparisons. Planned figures: Protocol decision maps tied to physical contrast.

### 24. Image Quality and Optimization

Quantify coupled parameter trade-offs with acquisition and reconstruction assumptions stated; optimize task performance rather than isolated image appearance.

- **24.1 Image-quality measures**: SNR, CNR and noise definitions; PSF, effective resolution and detectability; Repeatability and task-based assessment.
- **24.2 Sampling and averaging trade-offs**: FOV, matrix, voxel volume and slice thickness; Number of averages and scan-time scaling; Two-dimensional versus three-dimensional efficiency.
- **24.3 Timing and contrast trade-offs**: TR, TE, TI and flip angle; Echo train length, turbo factor and effective TE; Contrast, blurring and motion sensitivity.
- **24.4 Bandwidth and gradient trade-offs**: Receiver bandwidth, dwell time and noise; RF bandwidth and slice selection; Echo spacing, readout duration, distortion and slew.
- **24.5 Acceleration and incomplete sampling**: Parallel-imaging SNR and calibration overhead; Partial Fourier and phase uncertainty; SMS, compressed sensing and nonlinear image quality.
- **24.6 Constrained optimization**: Fixed-time versus fixed-resolution comparisons; SAR, motion and hardware constraints; Pareto design and sensitivity to model assumptions.
- **24.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **24.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: SNR scaling, bandwidth displacement, scan time and acceleration penalty. Planned figures: Pareto curves, SNR efficiency and contrast surfaces.

### 25. Modern MRI Methods

Integrate mature modern methods through their physical opportunities and limitations; point back to full derivations and avoid a catalogue of recent papers.

- **25.1 Low-field and portable MRI**: Polarization, relaxation and noise regimes; Magnet design, bandwidth and encoding constraints; Resolution, accessibility and reconstruction trade-offs.
- **25.2 High-field and parallel transmission**: Wavelength effects and B1-plus control; Joint pulse and field design; SAR, susceptibility and calibration constraints.
- **25.3 Short-lived and alternative signals**: Ultrashort- and zero-echo-time acquisition; Nonproton and hyperpolarized imaging concepts; Hardware and quantification limitations.
- **25.4 Integrated quantitative imaging**: Synthetic MRI and multiparametric acquisitions; MRF and model-based reconstruction in context; Calibration, harmonization and uncertainty.
- **25.5 Modern reconstruction in practice**: Compressed sensing, low-rank and learned methods; Prospective validation and distribution shift; Evidence maturity and reproducible comparisons.
- **25.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **25.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: Field-strength scaling and comparison of quantitative acquisition strategies. Planned figures: Method dependency map and low-field trade-offs.

### 26. Safety and System Limits

Explain static, RF, gradient, acoustic and cryogenic hazards from their mechanisms; keep operational limits tied to current authoritative standards when drafted.

- **26.1 Static-field interactions**: Forces, torques and projectile mechanisms; Spatial gradients and active shielding; Implant interactions and screening principles.
- **26.2 RF energy deposition**: Electric fields, dissipated power and SAR; Global versus local heating and duty cycle; Conductive loops, implants and model uncertainty.
- **26.3 Gradient and acoustic effects**: Induced electric fields and PNS; Waveform dependence beyond peak slew; Mechanical forces, acoustic noise and protection.
- **26.4 Cryogenics and system failures**: Stored energy and quench mechanisms; Cryogen release and oxygen displacement; Fault response and system interlocks.
- **26.5 Limits and responsible interpretation**: Scanner operating modes and standards; MR Safe, MR Conditional and MR Unsafe labeling; Physics estimates versus device-specific conditions.
- **26.6 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **26.7 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: RF duty-cycle scaling and gradient slew comparisons without patient-specific clearance. Planned figures: Energy deposition and induced electric-field pathways.

### 27. Integrated Worked Problems

Reserve substantial synthesis problems and worked cases integrating spin physics, design, reconstruction and clinical objectives; solutions to challenge problems remain in Appendix E.

- **27.1 End-to-end acquisition design**: From target resolution to gradient waveform; Sequence timing, contrast and scan time; Hardware and safety feasibility.
- **27.2 Signal and pathway prediction**: Imperfect pulses and stimulated echoes; Transient preparation and steady-state limits; Comparing Bloch, EPG and measured signals.
- **27.3 Reconstruction and identifiability**: Joint coil, field and image estimation; Undersampling ambiguity and prior dependence; Noise amplification and uncertainty bounds.
- **27.4 Quantitative experimental design**: Competing relaxation and diffusion models; Sampling schedules and nuisance parameters; Bias-variance trade-offs under fixed time.
- **27.5 Artifact diagnosis and protocol repair**: Coupled field, motion and sampling errors; Controlled tests and competing hypotheses; Correction limits and remaining uncertainty.
- **27.6 Research and interview synthesis**: Derive an unfamiliar sequence from its diagram; Critique an apparently convincing result; Design a falsifiable MRI experiment.
- **27.7 Worked examples**: Derivation and quantitative calculation; Assumptions, limiting cases and scanner interpretation.
- **27.8 Challenge problems**: Derivation and quantitative design; Model criticism and integrated reasoning.

Planned calculations: End-to-end scanner design and quantitative protocol audits. Planned figures: Complete timing diagrams and simulated failure cases.

## Appendices

### A. Mathematical Reference

Collect reusable identities with assumptions and links to their derivations; do not replace Chapter 1's development.

- **A.1 Complex analysis and vector identities**: Phasors and complex differentiation; Vector products and rotation identities.
- **A.2 Linear operators and matrix calculus**: Spectral decompositions and matrix exponentials; Gradients, Jacobians and Hessians.
- **A.3 Probability and estimation identities**: Gaussian likelihoods and covariance propagation; Fisher information and constrained estimation.
- **A.4 Differential equations and propagators**: Linear systems and affine evolution; Numerical accuracy and limiting cases.

### B. Fourier Reference

Provide transform pairs and discrete conventions consistent with the front matter, including normalization and units.

- **B.1 Continuous transform pairs**: Gaussian, rectangle and sinc; Shifts, modulation and convolution.
- **B.2 Discrete transforms and sampling**: DFT normalization and index ordering; Sampling combs and aliasing.
- **B.3 Imaging and spectral conventions**: Spatial forward and inverse transforms; Temporal spectra and signed frequency axes.
- **B.4 Resolution and windowing**: Point-spread functions and apodization; Zero filling and interpolation.

### C. Common Signal Equations

Collect validated signal models only after their derivations exist, with assumptions, units and failure modes next to each equation.

- **C.1 Equilibrium and elementary evolution**: Thermal magnetization and Bloch free evolution; FID, spin echo and gradient echo.
- **C.2 Steady-state and prepared acquisitions**: Spoiled GRE and bSSFP; Inversion recovery and prepared readouts.
- **C.3 Quantitative signal families**: Relaxometry, diffusion and exchange; Flow, ASL and chemical-species models.
- **C.4 Noise and estimation**: Complex likelihoods and magnitude statistics; SNR scaling and uncertainty relations.

### D. Constants, Units and Typical Values

Separate physical constants from field-, tissue-, vendor- and protocol-dependent representative values; record sources and measurement conditions.

- **D.1 Constants and unit conversions**: Gyromagnetic ratios and fundamental constants; SI conversions and cycles versus radians.
- **D.2 Tissue and field-dependent quantities**: Relaxation and diffusion ranges; Susceptibility and chemical shifts.
- **D.3 System and acquisition quantities**: Gradients, slew, bandwidth and timing; Nominal values versus measured performance.

### E. Solutions to Challenge Problems

Provide complete derivations and numerical checks keyed to stable problem labels; keep all challenge solutions separate from questions.

- **E.1 Mathematical and Physical Foundations**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.2 Quantum Spin Physics**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.3 Classical Magnetization and the Bloch Equations**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.4 RF Excitation and the Rotating Frame**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.5 Spatial Encoding and k-Space**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.6 Signal Formation and Fourier Imaging**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.7 Basic Pulse Sequences**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.8 Advanced Pulse Sequences**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.9 Contrast and Relaxation**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.10 Diffusion MRI**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.11 Quantitative MRI**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.12 Magnetic Resonance Fingerprinting**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.13 Extended Phase Graphs and Signal Pathways**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.14 Parallel Imaging**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.15 Non-Cartesian and Accelerated Imaging**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.16 Reconstruction and Inverse Problems**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.17 MRI Hardware**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.18 RF Pulses and Sequence Design**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.19 Flow, Perfusion and Angiography**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.20 Magnetic Resonance Spectroscopy**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.21 Functional MRI**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.22 Artifacts and Corrections**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.23 Clinical Protocol Physics**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.24 Image Quality and Optimization**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.25 Modern MRI Methods**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.26 Safety and System Limits**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.
- **E.27 Integrated Worked Problems**: Derivations and numerical checks; Interpretation, limiting cases and alternative approaches.

### F. Compact MRI Physics Reference Sheet

End the book with a compact synthesis of established equations, conventions and parameter trade-offs; this pass creates headings only.

- **F.1 Spin and sequence essentials**: Signs, units and rotations; Relaxation and sequence signal models.
- **F.2 Encoding and reconstruction essentials**: Gradients, k-space and sampling; Coil encoding, noise and inverse problems.
- **F.3 Quantification and design essentials**: Diffusion, flow and parameter estimation; Timing, bandwidth, SNR and system constraints.
