# Comprehensive Engineering & Physics Study Master Plan

This document outlines the integrated strategy and individual curriculums for balancing active academic coursework (Optics and Dynamics) with self-directed study (Advanced Mathematics and Electronics).

## The Weekly Balance Strategy
Taking two heavy academic classes while self-studying two massive textbooks requires treating the self-study as a playground for the academic work, rather than isolated tasks.

*   **Dynamics (Retake Focus):** FBDs first, always. Avoid the "illusion of competence" by forcing the rotational equations and collision algorithms into software—verifying mechanics through a custom physics engine written in C++ or Rust ensures the math is bulletproof.
*   **Optics (First-Time Focus):** Anchor the abstraction. When wave math gets heavy, visualize the physical hardware. Ground the ray-tracing matrices in reality by calculating the resolving limits of a Newtonian reflector paired with a DSLR sensor.
*   **Advanced Math (Self-Study):** Remove deadlines. Treat Kreyszig as an encyclopedia. When Optics introduces PDEs, jump to Kreyszig Chapter 12. When Dynamics hits 3D rotational matrices, jump to Chapter 7.
*   **Electronics (Self-Study):** Use hardware as a mental break from calculus. Breadboarding and microcontroller logic (like configuring an ESP32 or LoRa node) keeps you moving forward without draining the same cognitive reserves.

### Example Weekly Schedule
*   **Monday (Theory & Geometry):** Optics (Visual pass & diagram analysis) + Dynamics (Readings & Fundamental FBDs).
*   **Tuesday (The Math Gauntlet):** Optics (Mathematical derivations of wave/ray behavior) + Dynamics (Core problem sets, forcing FBDs on every problem).
*   **Wednesday (Math Integration):** Self-Study (Targeted Kreyszig reading directly supporting the week's Optics PDEs or Dynamics matrices).
*   **Thursday (Application & Code):** Optics (Advanced problem sets) + Dynamics (Verifying problem answers by coding the kinematics/mechanics).
*   **Friday (Synthesis & Hardware):** Optics/Dynamics (Weekly review/homework wrap-up) + Electronics (Breadboarding, reading AoE intuition).
*   **Weekend:** Overflow for class assignments, and dedicated time for physical prototyping, astrophotography imaging runs, or software architecture.

---

## Curriculum 1: Engineering Mechanics - Statics & Dynamics (Hibbeler)
*Class Focus: 16-Week Plan*

**The Daily Study Loop:**
*   **Day 1:** Theory and Kinematics. Focus heavily on geometric constraints.
*   **Day 2:** The "Fundamental" Gauntlet. Do every F-problem to isolate mechanics.
*   **Day 3:** Core Problem Solving. Draw an FBD and Kinetic Diagram for *every* problem.
*   **Day 4:** Alternative Methods (e.g., verifying Force/Acceleration with Work/Energy).
*   **Day 5:** Synthesis. Ask "what if" (e.g., doubling mass, shortening linkages).

**Part 1: The Statics Refresher**
*   **Week 1:** Equilibrium & Internal Forces (Ch 3, 5, 7). 2D/3D equilibrium.
*   **Week 2:** Friction & Center of Gravity (Ch 8, 9). Slipping vs. tipping, centroids.
*   **Week 3:** Moments of Inertia (Ch 10). Mass moment of inertia and Parallel-Axis Theorem. (Crucial for rigid body dynamics).

**Part 2: Particle Dynamics**
*   **Week 4:** Particle Kinematics (Ch 12). Normal/tangential coordinates, dependent motion.
*   **Week 5:** Kinetics: Force and Acceleration (Ch 13). Newton’s Second Law in different coordinate systems.
*   **Week 6:** Kinetics: Work and Energy (Ch 14). Path-dependent vs. position-dependent problems.
*   **Week 7:** Kinetics: Impulse and Momentum (Ch 15). Collisions and coefficient of restitution.

**Part 3: Planar Rigid Body Dynamics**
*   **Week 8:** Rigid Body Kinematics I - Velocity (Ch 16). Instantaneous Center (IC) of Zero Velocity.
*   **Week 9:** Rigid Body Kinematics II - Acceleration (Ch 16). Relative-motion analysis.
*   **Week 10:** Rigid Body Kinetics: Force & Acceleration (Ch 17). Translation, rotation, general plane motion.
*   **Week 11:** Rigid Body Kinetics: Work, Energy, & Momentum (Ch 18, 19). Conservation of angular momentum.

**Part 4: Advanced Dynamics**
*   **Week 12:** 3D Kinematics (Ch 20). Euler angles and Coriolis acceleration.
*   **Week 13 & 14:** 3D Kinetics (Ch 21). Euler equations of motion and gyroscopic motion.
*   **Week 15 & 16:** Vibrations (Ch 22). Undamped, damped, and forced vibrations (resonance).

---

## Curriculum 2: Optics (Hecht)
*Class Focus: 15-Week Plan*

**The Daily Study Loop:**
*   **Day 1:** Visual/Conceptual Pass. Memorize the geometry of wave propagation diagrams.
*   **Day 2:** Mathematical Derivation. Work through in-text PDEs with pencil and paper.
*   **Day 3:** Core Mechanics & Ray Tracing. Use a ruler for physical ray drawing.
*   **Day 4:** Complex Problems. Calculate resolving power, fringe separation, etc.
*   **Day 5:** Synthesis. Summarize physical constraints and boundary conditions.

**Part 1: The Electromagnetic Nature of Light**
*   **Week 1:** Wave Motion (Ch 2). 1D/3D wave equations, phase velocity.
*   **Week 2:** Electromagnetic Theory & Photons (Ch 3). Deriving the wave equation, Poynting vector.
*   **Week 3:** The Propagation of Light (Ch 4). Fermat’s Principle, Fresnel Equations.

**Part 2: Geometrical Optics**
*   **Week 4:** Lenses and Mirrors (Ch 5). Thin lenses, spherical mirrors, reflecting systems.
*   **Week 5:** Optical Instruments (Ch 5 cont.). Analyzing objective-to-sensor imaging trains.
*   **Week 6:** Thick Lenses & Aberrations (Ch 6). Ray-tracing matrices, Seidel aberrations (coma, spherical).

**Part 3: Physical Optics**
*   **Week 7:** Superposition of Waves (Ch 7). Group vs. phase velocity.
*   **Week 8:** Polarization (Ch 8). Linear/circular polarization, wave plates.
*   **Week 9:** Interference I - Division of Wavefront (Ch 9). Young’s Double-Slit, fringe visibility.
*   **Week 10:** Interference II - Division of Amplitude (Ch 9). Thin-film interference, Michelson Interferometer.

**Part 4: Diffraction and Fourier Optics**
*   **Week 11:** Fraunhofer Diffraction (Ch 10). The Rayleigh Criterion and diffraction limits.
*   **Week 12:** Fresnel Diffraction (Ch 10 cont.). Near-field diffraction, Cornu spiral.
*   **Week 13 & 14:** Fourier Optics (Ch 11). 2D Fourier transforms through lenses, spatial frequency filtering.

**Part 5: Modern Concepts**
*   **Week 15:** Coherence & Lasers (Ch 12, 13). Spatial/temporal coherence, Gaussian beam propagation.

---

## Curriculum 3: Advanced Engineering Mathematics (Kreyszig)
*Self-Study: 22-Week Plan (Adjust pace to support coursework)*

**The Daily Study Loop:**
*   **Day 1:** Theory & First Pass (Recreate in-text examples).
*   **Day 2:** Core Practice (Odd-numbered mechanical problems).
*   **Day 3:** Theory & Second Pass (Remaining sections).
*   **Day 4:** Core Practice (Odd-numbered application problems).
*   **Day 5:** Synthesis (Chapter review and formula sheet).

**Part A: Ordinary Differential Equations (ODEs)**
*   **Week 1:** First-Order ODEs (Ch 1)
*   **Week 2:** Second & Higher-Order Linear ODEs (Ch 2, 3)
*   **Week 3:** Systems of ODEs & Phase Plane (Ch 4)
*   **Week 4:** Series Solutions & Special Functions (Ch 5)
*   **Week 5:** Laplace Transforms (Ch 6)

**Part B: Linear Algebra and Vector Calculus**
*   **Week 6:** Matrices, Vectors, Linear Systems (Ch 7)
*   **Week 7:** Matrix Eigenvalue Problems (Ch 8)
*   **Week 8:** Vector Differential Calculus (Ch 9)
*   **Week 9:** Vector Integral Calculus (Ch 10)

**Part C: Fourier Analysis and PDEs**
*   **Week 10:** Fourier Series & Transforms (Ch 11)
*   **Week 11:** Partial Differential Equations (Ch 12)

**Part D: Complex Analysis**
*   **Week 12:** Complex Numbers & Functions (Ch 13)
*   **Week 13:** Complex Integration (Ch 14)
*   **Week 14:** Series and Residues (Ch 15, 16)
*   **Week 15:** Conformal Mapping & Potential Theory (Ch 17, 18)

**Part E: Numeric Analysis**
*   **Week 16:** Numerics in General (Ch 19)
*   **Week 17:** Numeric Linear Algebra (Ch 20)
*   **Week 18:** Numerics for ODEs and PDEs (Ch 21)

**Part F & G: Optimization, Graphs, Statistics**
*   **Week 19:** Unconstrained Optimization & Linear Programming (Ch 22)
*   **Week 20:** Graphs and Combinatorial Optimization (Ch 23)
*   **Week 21:** Data Analysis & Probability Theory (Ch 24)
*   **Week 22:** Mathematical Statistics (Ch 25)

---

## Curriculum 4: The Art of Electronics (Horowitz & Hill)
*Self-Study: 20-Week Plan (Hardware break from calculus)*

**The Daily Study Loop:**
*   **Day 1:** Read for Intuition. Focus on rules of thumb, ignore deep math.
*   **Day 2:** Circuit Analysis. Analyze the "Bad Circuits" sections to learn failure modes.
*   **Day 3:** Simulation/Breadboarding. Build and probe the circuits physically or in LTspice.
*   **Day 4:** Deep Dive & Data Sheets. Learn absolute maximum ratings and performance graphs.
*   **Day 5:** Synthesis. Sketch sub-system block diagrams.

**Part 1: Analog Fundamentals**
*   **Week 1:** Foundations (Ch 1). Voltage dividers, Thevenin equivalents.
*   **Week 2:** Bipolar Junction Transistors (Ch 2). Emitter followers, basic switching.
*   **Week 3:** Field-Effect Transistors (Ch 3). MOSFET switching, gate capacitance, driving high-current loads.
*   **Week 4:** Operational Amplifiers (Ch 4). Golden rules, comparators.
*   **Week 5:** Precision Circuits & Filters (Ch 5, 6). Active filters, offsets.

**Part 2: Power and Signal Integrity**
*   **Week 6:** Oscillators and Timers (Ch 7). The 555 timer, RC oscillators.
*   **Week 7:** Low-Noise Techniques (Ch 8). Grounding, shielding, isolation.
*   **Week 8 & 9:** Voltage Regulation & Power (Ch 9). Switching regulators, battery management.
*   **Week 10:** Analog Review. Simulate mixed analog/power systems.

**Part 3: Digital Logic and Interfacing**
*   **Week 11:** Digital Logic (Ch 10). CMOS logic, state machines.
*   **Week 12:** Programmable Logic Devices (Ch 11). HDL concepts, FPGAs.
*   **Week 13:** Logical Interfacing (Ch 12). Level shifting, debouncing.
*   **Week 14:** Digital Meets Analog (Ch 13). ADCs, DACs, multiplexing.

**Part 4: Microcontrollers and System Architecture**
*   **Week 15:** Computers & Data Links (Ch 14). Serial protocols (I2C, SPI, UART).
*   **Week 16 & 17:** Microcontrollers (Ch 15). Architecture, interrupts, hardware registers.
*   **Week 18:** System Design. PCB layout, decoupling, heat dissipation.
*   **Week 19 & 20:** Capstone Design. Full schematic design for a mixed-signal system (e.g., sensor node with actuation).
