# Scientific overview

A large entangled state can lend entanglement while changing little in state fidelity. For optical Gaussian resources, that statement leaves two practical questions open: how many catalyst modes are needed, and how many photons must those modes initially contain?

The [model and resource theorems](model.md) answer these questions for a known pure Gaussian catalyst, a fixed pure Gaussian target and local Gaussian processing. The error is assessed against the original catalyst and desired target jointly. The main result is a sharp asymptotic tradeoff between catalyst mode count, initial photon inventory and this return error.

For one target pair of squeezing $`r`$, the separate optimal coefficients are

```math
\varepsilon n_{\min}\longrightarrow r^2,
\qquad
\varepsilon E_{\rm opt}\longrightarrow2(\cosh r-1)^2.
```

Here $`n`$ counts entangled catalyst mode pairs and $`E`$ counts photons across both parties. The constructions use exactly $`n`$ physical catalyst modes per party. A finite normalized mode budget imposes a photon coefficient strictly larger than the energy-only infimum.

## How the proof works

The [Gaussian geometry](gaussian_geometry.md) controls changes of entanglement squeezings through global state fidelity. It uses a dimension-independent estimate for logarithmic symplectic spectra and the partially transposed covariance of a pure bipartite Gaussian state. It also proves that local Gaussian dressing cannot lower the photon inventory below that of canonical squeezed pairs.

The [converse](converse.md) then applies componentwise Gaussian squeezing monotonicity to every fine measurement branch. Inserting the target squeezings into the catalyst's sorted spectrum produces a positive displacement. A weighted integral inequality converts that displacement into simultaneous lower bounds on modes and photons. The bound is uniform over classical mixing, postselection and free local Gaussian ancillas.

The [constructions](constructions.md) prepare a product of squeezed pairs along decreasing ladders. Each party cyclically permutes its modes. The shifted product approximates the original catalyst together with the target, and its joint overlap is an explicit product of hyperbolic secants. Grading the ladder controls the tradeoff.

Finally, the [tradeoff analysis](tradeoff.md) proves that every supporting resource bound is attained. Its contact parameter covers the entire finite-budget boundary, with separate treatment of the minimum-mode endpoint and the photon infimum.

| Question | Authoritative account |
|---|---|
| What is allowed, counted and returned? | [Model and exact statements](model.md) |
| Why does fidelity constrain entanglement squeezings in every local frame? | [Gaussian geometry](gaussian_geometry.md) |
| Why do measurements and postselection not evade the bound? | [Finite-resource converse](converse.md) |
| Which prepared catalysts attain the costs? | [Passive constructions](constructions.md) |
| How do the two resource budgets interact? | [Sharp tradeoff](tradeoff.md) |
| What do the limits mean physically? | [Interpretation and examples](interpretation.md) |
| Which tools and mechanisms are inherited? | [Related work](../references/related_work.md) |
| Which calculations can be reproduced? | [Verification guide](../verification/README.md) |

The target may contain any fixed finite list of nonzero Gaussian Schmidt squeezings. The account treats this general case directly, so the one-pair formulas are special cases of the same argument. Exact finite-error optimality and mixed-catalyst borrowing are separate questions; the finite converse and the stated asymptotic frontier are the results established here.
