# Learning Gaussian Entanglement Borrowing

The central question is how a shared optical state can supply entanglement to new modes while remaining close to its original state. Two physical resources enter separately: the number of catalyst modes and their initial photon inventory. The project's result determines their sharp asymptotic tradeoff under a joint return criterion.

## One source, one project map

The educational anchor is **Weedbrook et al., _Gaussian Quantum Information_, Reviews of Modern Physics 84, 621–669 (2012)**, [DOI](https://doi.org/10.1103/RevModPhys.84.621), with an [open author manuscript](https://arxiv.org/abs/1110.3234v1).

Use the [anchor bridge](anchor.md) for the relevant sections, exact convention translations and the steps supplied by this project. The review provides the Gaussian-information foundations. The canonical scientific chapters prove the resource theorem and its attaining constructions.

The [milestone map](milestones.md) contains exactly **M01–M30** in two phases:

- **Background and preliminaries:** connect individual modes, covariance matrices, Gaussian transformations, entanglement and fidelity into a precise borrowing task.
- **Narrative and innovation:** assemble the fidelity constraint and Gaussian branch ordering into resource bounds, then connect explicit catalysts to the complete asymptotic tradeoff.

Each milestone states a central question, understanding target, earlier dependencies, conceptual connection and source pointers. The map describes the project's ideas in a stable order. Specialist derivations remain in the linked science pages.

## Reading routes

| Purpose | Route |
|---|---|
| Understand the physical question first | [Scientific overview](../science/README.md) → [interpretation](../science/interpretation.md) |
| Build the prerequisites and follow the argument | [Anchor bridge](anchor.md) → [M01–M30](milestones.md) |
| Check the exact claim and proof | [Model](../science/model.md) → [geometry](../science/gaussian_geometry.md) → [converse](../science/converse.md) → [constructions](../science/constructions.md) → [tradeoff](../science/tradeoff.md) |
| Reproduce the finite calculations | [Verification guide](../verification/README.md) |
| Check attribution and the comparison scope | [Related work](../references/related_work.md) |

## The distinctions to carry through the route

The fidelity compares the entire retained catalyst and target with their desired product. Good marginal fidelity alone is a weaker return contract.

The mode resource counts nonzero Gaussian Schmidt pairs; the attaining catalysts use exactly that many physical modes per party. The photon resource counts both parties' initial catalyst photons. Local control work and preparation complexity are separate costs.

The target is fixed, the catalyst is pure Gaussian, and the refined quantum operations are Gaussian. The finite converse applies to measurements and positive-probability postselection. The resource frontier is sharp in the stated small-error upper-budget sense.

Finally, the fewest modes and the lowest photon coefficient require different families. Understanding why those optima separate, and how the full frontier connects them, completes the scientific story.

