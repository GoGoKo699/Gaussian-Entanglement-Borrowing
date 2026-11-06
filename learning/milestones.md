# Thirty milestones for Gaussian entanglement borrowing

This map follows the scientific argument from individual optical modes to the complete photon and mode tradeoff. Its single educational anchor is [Weedbrook et al., Gaussian quantum information][W]. The [anchor bridge](anchor.md) supplies the notation dictionary and a complete example with one catalyst pair and one target pair.

The allocation is **12 milestones for background/preliminaries** and **18 for narrative/innovation**. The foundations assemble the state description, operations, error criterion, and resource model. The larger second phase connects the construction to the universal converse and the full optimization. M12 and M30 integrate their respective phases.

| Phase | Milestones | Scientific destination |
|---|---|---|
| Background/preliminaries | M01–M12 | A precise operational account of the borrowing problem |
| Narrative/innovation | M13–M30 | The mechanism, universal bounds, attaining families, complete boundary, and physical meaning |

Section pointers to Weedbrook refer to the linked author manuscript. They identify foundations. The dimension-independent metric estimate, borrowing converse, discretization bounds, and resource frontier are supplied in the canonical project chapters. Research dependencies and their attribution remain in those chapters. This map selects the load-bearing understanding targets; the specialist sources contain the detailed calculations.

## Phase I: Background/preliminaries

### M01. One bosonic mode

**Central question.** What physical object does one optical mode describe?

**Understanding target.** Relate an oscillator's photon-number states to its two quadratures, and recognize a covariance convention as a choice of units. Translate the review's vacuum covariance $`I`$ and commutator $`2i`$ to the project's $`I/2`$ and $`i`$.

**Dependencies and story role.** No earlier milestone. Establishes the elementary system before introducing shared states or resource costs.

**Conceptual connection.** The infinite state space of one oscillator is distinct from the number of physical modes available to a protocol.

**Source pointers.** Anchor: [I.D and II.A][W]. Project: [state conventions](../science/model.md#states-normalization-and-return-criterion) and the [convention dictionary](anchor.md#convention-dictionary).

### M02. Photons as an initial inventory

**Central question.** What does it mean to charge the photons in a catalyst?

**Understanding target.** Interpret photon number as an expectation in the initial state. Distinguish vacuum, thermal occupation, and locally supplied control energy. Count both parties' catalyst photons and keep the common oscillator frequency fixed.

**Dependencies and story role.** Uses M01. Adds a physical cost to the elementary oscillator without yet assigning it an information-processing role.

**Conceptual connection.** An excitation inventory describes a state resource; it does not by itself describe the work needed to prepare or manipulate that state.

**Source pointers.** Anchor: [II.B.1][W]. Project: [charged resources](../science/model.md#operations-and-charged-resources) and [photon conventions](anchor.md#photon-inventory).

### M03. A Gaussian state in phase space

**Central question.** Which information about a Gaussian state is carried by its first and second moments?

**Understanding target.** Distinguish the displacement vector from the covariance matrix, understand the quantum uncertainty constraint, and see why a finite matrix description is possible even though each mode has infinitely many photon-number states.

**Dependencies and story role.** Uses M01–M02. Moves from a physical oscillator to the state representation used throughout the proofs.

**Conceptual connection.** Covariances make Gaussian calculations finite-dimensional, while photon expectations and the number of modes remain physically distinct quantities.

**Source pointers.** Anchor: [II.A.1][W]. Project: [Gaussian covariance and purity](../science/gaussian_geometry.md#3-pure-bipartite-gaussian-normal-form) and [quadrature translation](anchor.md#quadratures-and-covariance).

### M04. Passive and active Gaussian transformations

**Central question.** Which changes of a Gaussian state redistribute modes, and which can change its photon inventory?

**Understanding target.** Recognize symplectic transformations as Gaussian unitary actions on quadratures. Distinguish passive mixing and permutations from active squeezing, and separate a coordinate reordering from a physical operation.

**Dependencies and story role.** Uses M01–M03. Supplies the elementary controls before restricting them to Alice's and Bob's separate laboratories.

**Conceptual connection.** A broad converse can allow active controls even when its attaining protocol uses only passive permutations.

**Source pointers.** Anchor: [II.A.2, II.B.6, and II.C.2][W]. Project: [allowed operations](../science/model.md#operations-and-charged-resources) and [exact cyclic protocol](../science/constructions.md#1-exact-cyclic-protocol).

### M05. One shared squeezed pair

**Central question.** How does one two-mode squeezed vacuum connect shared entanglement to local thermal noise?

**Understanding target.** Read the standard squeezing parameter $`r`$ in the Schmidt series, recognize the thermal marginal, and associate a canonical pair with $`2\sinh^2r`$ total photons. Keep local phase conventions separate from quadrature rescaling.

**Dependencies and story role.** Uses M02–M04. Introduces the elementary shared resource and the elementary target.

**Conceptual connection.** The global state is pure while each local marginal is mixed; that local mixedness encodes entanglement.

**Source pointers.** Anchor: [II.B.7][W]. Project: [pure bipartite normal form](../science/gaussian_geometry.md#3-pure-bipartite-gaussian-normal-form) and [squeezing conventions](anchor.md#symplectic-eigenvalues-and-squeezing).

### M06. Williamson spectra

**Central question.** What does a symplectic eigenvalue retain when Gaussian coordinates change?

**Understanding target.** Distinguish ordinary eigenvalues from symplectic eigenvalues and interpret Williamson form as a covariance decomposition. Keep the covariance matrix and symplectic form in the same coordinate order.

**Dependencies and story role.** Uses M03–M05. Extends the one-pair description to many modes and identifies the invariant quantities needed for comparison.

**Conceptual connection.** A covariance's apparent anisotropy depends on its Gaussian frame; its symplectic spectrum does not.

**Source pointers.** Anchor: [II.C and II.C.1][W]. Project: [positive matrices and symplectic spectra](../science/gaussian_geometry.md#1-positive-matrices-and-symplectic-spectra) and [coordinate order](anchor.md#coordinate-order).

### M07. The Gaussian Schmidt list

**Central question.** What information remains after local Gaussian frames are removed from a pure shared state?

**Understanding target.** Describe a pure bipartite Gaussian state by its paired squeezing list and local vacuum factors. Distinguish the global pure-state spectrum from the spectra of local marginals, and identify $`n`$ as the number of nonzero shared squeezing entries.

**Dependencies and story role.** Uses M05–M06. Assembles many local mode descriptions into one invariant account of the catalyst.

**Conceptual connection.** The resource list has a finite length even though every physical oscillator has an infinite-dimensional state space.

**Source pointers.** Anchor foundations: [II.B.7 and II.C.1][W]. Project normal-form argument: [geometry, Section 3](../science/gaussian_geometry.md#3-pure-bipartite-gaussian-normal-form).

### M08. Partial transpose as a spectral probe

**Central question.** Why does reversing Bob's momenta reveal shared squeezing?

**Understanding target.** Identify partial transpose as a covariance congruence and distinguish ordinary matrix positivity from the quantum uncertainty condition. For a pure squeezed pair, understand the significance of the symplectic eigenvalues $`e^{2r}/2`$ and $`e^{-2r}/2`$.

**Dependencies and story role.** Uses M03, M05, and M06. Introduces the spectral probe that will connect entanglement to a matrix-distance estimate.

**Conceptual connection.** A transformed covariance can remain a positive matrix without representing a physical quantum state, allowing positive-matrix tools to expose entanglement.

**Source pointers.** Anchor: [II.D.1][W]. Project calculation: [partial-transpose symplectic spectrum](../science/gaussian_geometry.md#partial-transpose-symplectic-spectrum).

### M09. Joint fidelity and the meaning of error

**Central question.** What does a high overlap with the entire desired product guarantee?

**Understanding target.** Use $`F=\langle C,R|\rho_{\rm out}|C,R\rangle`$ and distinguish the actual infidelity $`1-F`$ from a requested tolerance $`\varepsilon`$ satisfying $`1-F\le\varepsilon`$. Distinguish joint return from checking only one marginal. Recognize that Weedbrook already defines squared fidelity and that purified distance is $`\sqrt{1-F}`$.

**Dependencies and story role.** Uses M03, M05, and M07. Adds the accuracy criterion before deciding which operations can satisfy it.

**Conceptual connection.** Returning the catalyst and preparing the target must be judged together, including their decoupling.

**Source pointers.** Anchor: [III.A.3, Eq. (79)][W]. Project: [return criterion](../science/model.md#states-normalization-and-return-criterion) and [fidelity dictionary](anchor.md#fidelity).

### M10. Gaussian instruments and retained outputs

**Central question.** How do ancillary modes, measurements, and discarded records enter a local Gaussian protocol?

**Understanding target.** Distinguish a conditional state from an averaged output, and a quantum instrument from a formal covariance expression. Understand Gaussian dilation, Gaussian readout, and local purification as descriptions of physical operations.

**Dependencies and story role.** Uses M03–M04 and M09. Extends the operational setting beyond unitary mode rearrangements.

**Conceptual connection.** The state retained by the parties depends on which quantum and classical information is discarded, so a converse must account for that information explicitly.

**Source pointers.** Anchor: [II.E.1–3 and V.A][W]. Project operational account: [physical instruments and refinement](../science/converse.md#2-physical-gaussian-instruments-and-branch-refinement).

### M11. Local controls and shared resources

**Central question.** Which quantities remain charged when local ancillary modes and local control energy are unrestricted?

**Understanding target.** Distinguish physical mode slots, nonzero Gaussian Schmidt pairs, and initial photons. Understand why local pure ancillary modes add zero shared squeezing entries and why changing a local Gaussian frame does not change the entanglement list.

**Dependencies and story role.** Uses M02, M04, M07, and M10. Collects the local descriptions into the resource rules of a bipartite task.

**Conceptual connection.** A free local resource can enlarge a laboratory without supplying the shared entanglement required by the target.

**Source pointers.** Anchor foundations: [II.A.2 and II.C.2][W]. Project: [operations and charged resources](../science/model.md#operations-and-charged-resources) and [ordered squeezing under local processing](../science/converse.md#3-ordered-squeezing-cannot-increase-on-a-fine-branch).

### M12. Integration: the complete borrowing task

**Central question.** What precisely must a Gaussian borrowing protocol accomplish, and which resources may grow?

**Understanding target.** Assemble the known pure catalyst, initially vacant target slots, fixed target list, allowed local processing, joint infidelity, and resource pair $`(n,E)`$ into one model. Explain why improving accuracy defines a family of finite catalysts rather than an exact transformation of one fixed catalyst.

**Dependencies and story role.** Integrates M01–M11. Completes the background phase with the operational problem that every subsequent argument addresses.

**Conceptual connection.** State description, locality, return accuracy, and resource accounting jointly determine what an impossibility or optimality statement means.

**Source pointers.** Anchor foundations: [II.B.7, II.E.1–3, and III.A.3][W]. Project synthesis: [the model](../science/model.md) and [one complete finite example](anchor.md#one-catalyst-pair-and-one-target-pair).

## Phase II: Narrative/innovation

### M13. The error of one squeezing gap

**Central question.** How much joint-overlap error is introduced by replacing one squeezing value with a nearby one?

**Understanding target.** Obtain $`\langle a|b\rangle=\mathrm{sech}(a-b)`$ in a common local frame and connect the small-gap infidelity to the square of the gap. Keep this aligned-pair calculation distinct from a bound over arbitrary Gaussian states.

**Dependencies and story role.** Uses M05, M09, and M12. Begins the project argument with the local error contribution that can be accumulated across a ladder.

**Conceptual connection.** A fixed total squeezing displacement can be divided into many smaller contributions whose errors add approximately quadratically.

**Source pointers.** Anchor prerequisites: [II.B.7 and III.A.3][W]. Project derivation: [exact cyclic overlap](../science/constructions.md#1-exact-cyclic-protocol) and [mesh-to-error bounds](../science/constructions.md#2-converting-a-mesh-bound-into-a-prescribed-error).

### M14. Passive borrowing by a cyclic shift

**Central question.** How can local permutations produce an approximate target while nearly returning a shared catalyst?

**Understanding target.** Track the target and catalyst slots through one cyclic permutation at each party. Explain why the actual output remains a product across target and catalyst, why the total photons are conserved, and where the return error appears.

**Dependencies and story role.** Uses M04, M11, and M13. Turns the local overlap calculation into a concrete finite protocol before addressing universal optimality.

**Conceptual connection.** The protocol redistributes already shared pairs; its approximate reference has more entanglement than the actual output without requiring the operation to create entanglement.

**Source pointers.** Anchor prerequisites: [II.B.6 and II.C.2][W]. Project: [exact cyclic protocol](../science/constructions.md#1-exact-cyclic-protocol) and [passive extraction](../science/interpretation.md#4-passive-extraction-and-approximate-return).

### M15. Inserting a target into an ordered spectrum

**Central question.** What invariant mismatch must every borrowing protocol confront?

**Understanding target.** Compare the sorted input list $`\mathbf s=\mathrm{sort}(\mathbf a,0^{\times k})`$ with the desired list $`\mathbf t=\mathrm{sort}(\mathbf a,\mathbf r)`$. Understand $`t_i\ge s_i`$, common zero padding, and the squared insertion distance $`D=\|\mathbf t-\mathbf s\|_2^2`$.

**Dependencies and story role.** Uses M07, M11, and M14. Replaces a particular circuit with a task-dependent spectral obstruction.

**Conceptual connection.** The catalyst appears on both sides of the task, but inserting a nonzero target still changes its ordered shared-squeezing inventory.

**Source pointers.** Anchor prerequisites: [II.C.1 and II.D][W]. Project definition: [states, resources, and sorted insertion](../science/converse.md#1-states-resources-and-sorted-insertion).

### M16. Relative covariance and Gaussian overlap

**Central question.** How can two arbitrary pure Gaussian states be compared without choosing their local normal forms simultaneously?

**Understanding target.** Interpret the affine-invariant distance between positive covariances and the relative squeezing parameters that determine their centered overlap. Explain why applying the same global Gaussian frame change evaluates overlap and distance even though it need not preserve each state's bipartite entanglement.

**Dependencies and story role.** Uses M03–M04, M06, and M09. Supplies a comparison tool that is insensitive to arbitrary local dressing of the catalyst.

**Conceptual connection.** Relative covariance geometry controls distinguishability, while the physical bipartition must be tracked by a separate invariant.

**Source pointers.** Anchor prerequisites: [II.A.2, II.C.2, and III.A.3][W]. Project proof: [positive-matrix distance](../science/gaussian_geometry.md#1-positive-matrices-and-symplectic-spectra) and [relative squeezing](../science/gaussian_geometry.md#4-pure-gaussian-overlap-and-relative-squeezing).

### M17. A dimension-independent Williamson estimate

**Central question.** Why can the logarithmic symplectic spectrum be controlled without a factor growing with the number of modes?

**Understanding target.** Understand the role of a fixed Williamson frame, compression within a degenerate eigenvalue block, and integration of a local norm bound. Identify why eigenvalue collisions must be included and why a positive tangent also gives symplectic monotonicity.

**Dependencies and story role.** Uses M06 and M16. Supplies the mathematical uniformity required when increasingly accurate catalysts use increasingly many modes.

**Conceptual connection.** A local perturbation estimate becomes a global spectral bound through a path of positive matrices. The review's normal form is a prerequisite; this estimate needs its own proof.

**Source pointers.** Anchor prerequisite: [II.C.1][W]. Project proof: [logarithmic Williamson contraction and monotonicity](../science/gaussian_geometry.md#2-logarithmic-williamson-contraction).

### M18. Fidelity controls the entanglement list

**Central question.** How does high global fidelity constrain the displacement of Gaussian Schmidt squeezings?

**Understanding target.** Combine the partial-transpose spectrum, the dimension-independent matrix estimate, and the relative-overlap formula to obtain $`\|\mathbf a-\mathbf b\|_2^2\le q_\varepsilon`$ when $`F\ge1-\varepsilon`$. Track the factors associated with squared fidelity and the two spectral branches.

```math
q_\varepsilon=\frac12\mathrm{arcosh}^2\!\left(\frac1{1-\varepsilon}\right),
\qquad q_\varepsilon/\varepsilon\longrightarrow1.
```

**Dependencies and story role.** Uses M08 and M16–M17. Converts a geometric statement into the quantitative entanglement constraint needed by the borrowing problem.

**Conceptual connection.** Approximate equality of full quantum states forces closeness of their Gaussian entanglement spectra even when local bases differ.

**Source pointers.** Anchor prerequisites: [II.D.1 and III.A.3][W]. Project theorem: [fidelity and Gaussian entanglement distance](../science/gaussian_geometry.md#5-fidelity-controls-gaussian-entanglement-distance).

### M19. Pure branches and componentwise monotonicity

**Central question.** What prevents a general local Gaussian protocol from increasing an ordered shared squeezing entry on a fine record?

**Understanding target.** Follow local purification and rank-one readout to pure Gaussian branches. Relate conditional covariance subtraction to symplectic monotonicity and then to the ordered squeezing criterion. Distinguish these branches from coarse outputs, which can be non-Gaussian mixtures.

**Dependencies and story role.** Uses M07, M10–M11, and M17. Extends the argument from local unitaries to the full operational class.

**Conceptual connection.** Conditioning changes the other party's covariance in a direction that cannot supply a larger pure-state entanglement spectrum.

**Source pointers.** Anchor prerequisites: [II.E.2–3 and V.A][W]. Project proof and attribution of the established ordering criterion: [refinement](../science/converse.md#2-physical-gaussian-instruments-and-branch-refinement) and [componentwise monotonicity](../science/converse.md#3-ordered-squeezing-cannot-increase-on-a-fine-branch).

### M20. A uniform ceiling for retained states

**Central question.** Why do mixing, postselection, and arbitrarily small positive success probabilities leave the same fidelity obstruction?

**Understanding target.** Combine branchwise squeezing monotonicity with the insertion distance and the pure-state geometric bound to obtain a common ceiling for almost every fine record. Explain why fidelity with a pure reference averages linearly, and why the ceiling survives trace-norm limits at a fixed input and target.

**Dependencies and story role.** Uses M15 and M18–M19. Integrates the geometric and operational ingredients into an all-protocol statement.

**Conceptual connection.** A bound uniform outside a null set of fine records cannot be improved by selecting a rare event of positive probability or forgetting the record.

**Source pointers.** Anchor prerequisites: [III.A.3 and V.A][W]. Project theorem: [uniform fidelity ceiling](../science/converse.md#4-a-uniform-fidelity-ceiling).

### M21. From spectral displacement to charged resources

**Central question.** How does the insertion mismatch force simultaneous mode and photon costs?

**Understanding target.** Explain the cancellation of catalyst endpoint primitives in the weighted integral, the use of Cauchy–Schwarz, and the minimum photon inventory at a fixed squeezing list. Interpret the finite inequality for every $`\lambda\ge0`$:

```math
q_\varepsilon\left[\frac E2+T+\lambda(n+k)\right]\ge A_\lambda^2.
```

Here $`T=\sum_j\sinh^2r_j`$ is the target's canonical photon inventory on one side, and $`A_\lambda=\sum_j\int_0^{r_j}\sqrt{\sinh^2x+\lambda}\,dx`$.

**Dependencies and story role.** Uses M02, M07, M15, and M20. Turns the universal fidelity obstruction into an explicit resource statement, including its finite corrections.

**Conceptual connection.** The weight $`\sqrt{\sinh^2x+\lambda}`$ combines the photon cost of a squeezing level with a price for occupying another mode.

**Source pointers.** Anchor prerequisites: [II.B.1, II.B.7, and II.C.1][W]. Project proof: [minimum photon inventory](../science/gaussian_geometry.md#6-minimum-photon-inventory-at-fixed-gaussian-entanglement) and [weighted converse](../science/converse.md#5-weighted-finite-resource-inequality).

### M22. Graded ladders that balance the costs

**Central question.** Which distribution of squeezing levels can approach a weighted resource bound?

**Understanding target.** For $`\lambda>0`$, relate gaps proportional to $`f_\lambda(x)=\sqrt{\sinh^2x+\lambda}`$ to near-equality in the weighted argument. Interpret $`A_\lambda`$, $`B_\lambda=\sum_j\int_0^{r_j}dx/f_\lambda(x)`$, and $`C_\lambda=A_\lambda-\lambda B_\lambda`$ as the quantities controlling error, mode count, and photons in a discrete passive ladder.

**Dependencies and story role.** Uses M14 and M21. Builds an attaining family whose resource allocation is guided by the same weight used in the converse.

**Conceptual connection.** The lower bound identifies a useful distribution of resources; the explicit protocol determines whether that distribution can actually be implemented.

**Source pointers.** Anchor prerequisites: [II.B.7 and II.C.2][W]. Project construction: [positive-parameter graded ladders](../science/constructions.md#3-graded-ladders-for-a-positive-tradeoff-parameter).

### M23. Meeting every requested joint infidelity

**Central question.** How does a small-gap idea become a finite protocol guaranteed to meet a specified error?

**Understanding target.** Use additive logarithmic loss, finite mesh estimates, and $`\ell_\varepsilon=-\log(1-\varepsilon)`$ to understand the prescribed step size. Account for the final truncated gap and the product fidelity of all target blocks. Separate proved convergence from numerical examples approaching a predicted limit.

**Dependencies and story role.** Uses M13 and M22. Closes the gap between a continuum resource profile and actual finite catalysts for every requested accuracy.

**Conceptual connection.** Accuracy is a global constraint on the entire returned state, and endpoint rounding must be controlled before taking a limit.

**Source pointers.** Anchor prerequisite: [III.A.3][W]. Project proof: [prescribed-error choice](../science/constructions.md#32-choice-for-every-requested-infidelity) and [uniform positive-parameter estimates](../science/constructions.md#33-uniformity-on-finite-positive-parameter-intervals).

### M24. Interior contacts between a bound and a protocol

**Central question.** Why does each positive tradeoff parameter identify an attained supporting point?

**Understanding target.** Match $`(u_\lambda,v_\lambda)=(A_\lambda B_\lambda,2A_\lambda C_\lambda)`$ to the support inequality $`v/2+\lambda u\ge A_\lambda^2`$. Understand the strict derivative signs and why one contact exchanges a smaller mode coefficient for a larger photon coefficient.

**Dependencies and story role.** Uses M21–M23. Connects the all-protocol lower bound to the explicit family at finite positive parameter values.

**Conceptual connection.** Optimality comes from matching an attainable resource pair to a universal support, rather than from optimizing the chosen protocol in isolation.

**Source pointers.** Anchor prerequisite for the photon cost: [II.B.7][W]. Project optimization: [contact monotonicity](../science/tradeoff.md#22-strict-monotonicity-of-the-contact-curve), [support supremum](../science/tradeoff.md#24-evaluation-of-the-support-supremum), and [attainment](../science/tradeoff.md#25-achievability-of-every-boundary-point).

### M25. The minimum-mode endpoint

**Central question.** What happens when using the fewest entangled catalyst modes is the priority?

**Understanding target.** With $`R=\sum_jr_j`$ and $`H=\sum_j\int_0^{r_j}\sinh^2x\,dx`$, explain why uniform squeezing gaps attain $`\varepsilon n\to R^2`$ and why the corresponding smallest photon coefficient is $`2RH`$. Distinguish equality of the asymptotic mode coefficient from exact optimization of the finite integer mode count.

**Dependencies and story role.** Uses M21, M23, and M24. Completes the finite-width end of the contact curve, including its endpoint.

**Conceptual connection.** Additional brightness cannot remove the need to distribute a fixed insertion displacement over enough shared modes.

**Source pointers.** Anchor prerequisites: [II.C.2 and III.A.3][W]. Project proof: [uniform endpoint construction](../science/constructions.md#4-the-minimum-mode-endpoint) and [individual resource minima](../science/tradeoff.md#4-the-two-individual-resource-minima).

### M26. The photon infimum and mode overhead

**Central question.** Why does the smallest photon coefficient require an unbounded normalized mode budget?

**Understanding target.** With $`K=\sum_j(\cosh r_j-1)`$, connect the hyperbolic-flow tail to $`\varepsilon E\to2K^2`$ and $`\varepsilon n\to\infty`$. Distinguish the explicit logarithmic overhead from the weaker necessary condition of divergence. Understand why an arbitrarily slowly divergent budget can be treated with fixed-parameter thresholds and diagonalization.

**Dependencies and story role.** Uses M21–M25. Completes the opposite end of the curve and separates the two individual resource optima.

**Conceptual connection.** Very weak pairs are inexpensive in photons, but occupying enough of them becomes the limiting resource.

**Source pointers.** Anchor prerequisites: [II.B.1 and II.B.7][W]. Project proof: [photon-limit construction](../science/constructions.md#5-the-minimum-photon-limit), [distinct minima](../science/tradeoff.md#4-the-two-individual-resource-minima), and [arbitrarily slow overhead](../science/tradeoff.md#5-any-divergent-mode-overhead-suffices-for-the-photon-coefficient).

### M27. The complete closed budget region

**Central question.** In what precise sense do the support inequalities describe the full attainable frontier?

**Understanding target.** Interpret upper budgets as $`\limsup\varepsilon n\le u`$ and $`\limsup\varepsilon E\le v`$. Combine the interior contacts and attained minimum-mode endpoint into the boundary $`V(u)=2\sup_{\lambda\ge0}(A_\lambda^2-\lambda u)`$; the photon infimum is approached only as $`u\to\infty`$. Distinguish this closed asymptotic region from exact finite caps at every boundary point.

**Dependencies and story role.** Uses M20–M21 and M23–M26. Integrates converse, attainment, and limiting quantifiers into one optimization theorem.

**Conceptual connection.** A frontier is complete only when every excluded budget is ruled out and every boundary budget has an attaining family.

**Source pointers.** Anchor prerequisite for the error convention: [III.A.3][W]. Project theorem: [frontier](../science/tradeoff.md#2-frontier-theorem) and [hard budgets and closure](../science/tradeoff.md#3-hard-finite-budgets-and-closure).

### M28. Several targets under one accuracy requirement

**Central question.** Why does borrowing several fixed pairs have a quadratic leading cost under joint accuracy?

**Understanding target.** Track the sum over target squeezings in $`A_\lambda`$, the common step across ladders, and the product of their fidelities. For $`k`$ identical pairs, explain $`V_k(u)=k^2V_1(u/k^2)`$. Keep the fixed finite target assumption separate from a limit in which $`k`$ grows.

**Dependencies and story role.** Uses M15, M21, M23, and M27. Extends the complete resource picture from one elementary pair to a fixed multimode target.

**Conceptual connection.** Additive target contributions become squares of sums because all outputs share one global error allowance.

**Source pointers.** Anchor prerequisites: [II.B.7 and II.D][W]. Project result: [identical and multimode targets](../science/tradeoff.md#6-identical-target-pairs-and-the-single-pair-case) and [weighted insertion](../science/converse.md#5-weighted-finite-resource-inequality).

### M29. What the resource law means physically

**Central question.** Which physical limitation is established by the frontier?

**Understanding target.** Explain how a diverging initial inventory can hide a finite photon transfer in a vanishing state error, while every prepared pair has bounded squeezing. Separate inventory from work and preparation complexity. Identify the pure-catalyst and Gaussian-control assumptions, and interpret the two non-Gaussian comparisons as separate resource tradeoffs.

**Dependencies and story role.** Uses M02, M11, M14, and M25–M28. Places the complete optimization in its physical setting and fixes its scope.

**Conceptual connection.** Photon number is unbounded, so fidelity closeness alone does not force its expectation difference to vanish across this family.

**Source pointers.** Anchor prerequisites: [II.A.2, II.C.2, and III.A.3][W]. Project account: [passive transfer](../science/interpretation.md#4-passive-extraction-and-approximate-return), [Gaussian restriction](../science/interpretation.md#6-why-the-gaussian-model-matters), and [implementation boundaries](../science/interpretation.md#7-accuracy-and-implementation-boundaries).

### M30. Integration: the complete scientific contribution

**Central question.** How do the mechanism, universal converse, and attaining families establish the resource law as a whole?

**Understanding target.** Give a connected account from the pure Gaussian borrowing task through spectral insertion, dimension-independent fidelity control, branchwise monotonicity, weighted resource bounds, and passive attainment. Reconcile approximate borrowing with the impossibility of exact finite-resource return, then state the full frontier and its distinct endpoint meanings under the correct assumptions.

**Dependencies and story role.** Integrates M13–M29 with the operational framework of M12. Completes the narrative phase by joining the proof, construction, optimization, and physical interpretation.

**Conceptual connection.** The same ordered squeezing structure explains both why borrowing becomes possible with growing resources and why its photon and mode costs cannot be jointly reduced beyond the frontier.

**Source pointers.** Anchor foundations: [II.B.7, II.C.1–2, II.D.1, II.E.1–3, and III.A.3][W]. Project synthesis: [scientific overview](../science/README.md), [canonical model and theorems](../science/model.md), [full tradeoff proof](../science/tradeoff.md), and [physical interpretation](../science/interpretation.md).

[W]: https://arxiv.org/pdf/1110.3234v1

