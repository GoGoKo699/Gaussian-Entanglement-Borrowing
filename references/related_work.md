# Related work and conventions

This project studies the physical resources required to borrow a fixed entangled bosonic Gaussian state while returning a **pure Gaussian catalyst approximately in joint state fidelity**. For a two-mode squeezed vacuum target with parameter $`r>0`$, the resources are the catalyst's nonzero Gaussian Schmidt-pair count, $`n`$, and its total initial mean photon number, $`E`$. Each party has at least $`n`$ physical catalyst modes, and the attaining constructions use exactly that number. Local Gaussian operations, local unentangled Gaussian ancillas, classical communication, and conditioning are allowed. Photon inventory is measured at fixed equal frequencies, with vacuum energy subtracted.

The target starts in vacuum. The error condition is $`F=\langle C\otimes r|\rho_{\rm out}|C\otimes r\rangle\ge1-\varepsilon`$, where $`|C\rangle`$ is the original catalyst. Thus $`F`$ tests the returned catalyst and extracted target jointly.

The distinction between existence of embezzlement and its optimal physical resource requirements matters. The contribution here is the matching asymptotic mode and photon laws, together with their joint tradeoff, within this specified operational model. The independent endpoints are

```math
\lim_{\varepsilon\downarrow0}\varepsilon n_{\min}(\varepsilon;r)=r^2,
\qquad
\lim_{\varepsilon\downarrow0}\varepsilon E_{\rm opt}(\varepsilon;r)
=2(\cosh r-1)^2.
```

The two endpoints optimize different catalyst families. A uniform squeezing ladder achieves the mode coefficient; a different distribution achieves the photon coefficient. These are asymptotic optimality statements. The explicit finite-size overlap of an aligned ladder is not asserted to be the optimum over all Gaussian protocols.

## Closest operational comparisons

| Work | Established setting or result | Relation to the present task |
|---|---|---|
| [van Dam and Hayden (2003)](https://doi.org/10.1103/PhysRevA.67.060302) | General finite-dimensional entanglement embezzlement through local operations without communication | Establishes the embezzlement mechanism; does not impose bosonic Gaussian states or photon inventory. |
| [Giedke et al. (2003)](https://arxiv.org/pdf/quant-ph/0301038) | Exact pure Gaussian conversion is characterized by componentwise ordered squeezing monotonicity | Supplies the operational converse input, including stochastic transformations. A quantitative fidelity bound is still required. |
| [Kera et al., v2 (2026)](https://arxiv.org/html/2509.15749v2) | Fermionic Gaussian embezzlement using local Gaussian unitaries and dense covariance spectra | Direct antecedent for Gaussian embezzlement and spectral shifts. The particle statistics and charged resources differ. |
| [Hackl and Jonsson (2019)](https://doi.org/10.22331/q-2019-07-15-165) | Minimum increase of source energy when extracting an entangled pair from a quadratic ground state | Studies a change of source energy without catalytic return; the present cost is initial photon inventory with return. |
| [Yadin et al. (2022)](https://doi.org/10.1088/1751-8121/ac7e09) | Catalytic Gaussian thermal operations, including stability under approximate covariance return | Both the operation class and the error topology differ from Gaussian LOCC with joint state fidelity. |

### General and Gaussian embezzlement

[van Dam and Hayden](https://arxiv.org/abs/quant-ph/0201041) established that suitable entangled catalysts permit arbitrarily accurate pure-state entanglement transformations without communication. Their construction is the general conceptual predecessor of borrowing entanglement through a small disturbance to a large resource. We do not claim a new discovery of that phenomenon.

[Kera, van Luijk, Stottmeister, and Wilming](https://arxiv.org/html/2509.15749v2) are the closest Gaussian predecessor. Their March 2026 revision proves fermionic Gaussian embezzlement, including a sufficient density condition on one-particle covariance spectra and finite-size estimates. Spectral insertion and rearrangement are therefore established ideas. Their Theorem 1 bounds a reduced mixed-state orbit trace distance; Section 3 then transfers this to joint pure-state embezzlement. Its error exponent should not be compared directly with a squared joint-fidelity error. The present problem instead optimizes a designed bosonic catalyst's mode count and unbounded photon occupation. The cited fermionic result does not give the bosonic photon coefficient or the joint mode–photon boundary.

### Pure Gaussian conversion and squeezing conventions

Theorem 1 of [Giedke, Eisert, Cirac, and Plenio](https://arxiv.org/pdf/quant-ph/0301038) states that an exact pure Gaussian conversion is possible precisely when the ordered squeezing vector decreases componentwise. Section 4 explicitly addresses stochastic transformations: they introduce no additional pure-state conversion possibilities. This is inherited input to the converse, not a new postselection theorem. Applying it to mixed outputs requires the additional refinement into pure Gaussian branches; linearity of overlap with the fixed pure reference then bounds their mixtures as well.

Our convention is

```math
|r\rangle=\operatorname{sech}r
\sum_{k=0}^{\infty}(\tanh r)^k|k,k\rangle,
\qquad V_{\rm vac}=I/2,
\qquad E(|r\rangle)=2\sinh^2r.
```

Equation (28) of Giedke et al. uses $`\tanh(r_{\mathrm{G}}/2)`$. Consequently $`r_{\mathrm{G}}=2r`$; their covariance convention also has vacuum covariance $`I`$. Conversion inequalities survive this uniform rescaling, while numerical resource coefficients require consistent conventions.

### Initial energy and energy change

[Hackl and Jonsson](https://arxiv.org/html/1904.06246v4) minimize the increase of a quadratic source Hamiltonian's expectation when an entangled partner-mode pair is swapped into initially unentangled targets and the source pair is replaced by a product state. Their source is not required to return close to its original state. Here $`E`$ is the initial catalyst photon inventory, not preparation work, control work, or energy consumed. A large initial reservoir can lose a finite number of photons while remaining close in fidelity. The two optimizations therefore constrain different physical quantities, even though both use Gaussian extraction protocols.

### Error topology and Gaussian thermal catalysis

Section VI.A, Definition 3, and Theorem 6 of [Yadin et al.](https://arxiv.org/pdf/2112.05540) quantify approximate strong catalysis using trace norms of differences of their second-moment matrices $`M`$ and $`A`$, and establish a dimension-independent stability statement in that error measure. The authors explicitly distinguish this from fidelity or trace distance between quantum states. Their Gaussian thermal operations use energy-preserving interactions with thermal ancillas. The present task allows Gaussian LOCC and measures the joint quantum state. Thus their stability result is not a prohibition of the state-fidelity embezzlement considered here. In a growing number of modes, summing covariance errors and accumulating quadratic contributions to state infidelity need not yield the same limiting condition.

## Gaussian fidelity and symplectic perturbation theory

[Banchi, Braunstein, and Pirandola](https://arxiv.org/html/1507.01941v1) give a general multimode Gaussian fidelity formula. Their covariance normalization is $`V_{\rm vac}=I/2`$, matching ours, but their $`\mathcal F`$ is **root fidelity**. Our $`F=\mathcal F^2`$ is squared fidelity. In particular, when one state is pure,

```math
F(\rho_1,\rho_2)
=\frac{\exp[-\tfrac12\Delta d^T(V_1+V_2)^{-1}\Delta d]}
{\sqrt{\det(V_1+V_2)}}.
```

The fidelity formula and the underlying phase-space formalism are established tools. They do not by themselves optimize over local Gaussian coordinate changes or over Gaussian protocols.

There is likewise substantial existing perturbation theory for symplectic eigenvalues. [Bhatia and Jain (2015)](https://arxiv.org/pdf/1803.04647) prove variational, perturbation, and log-majorization results, including inequalities along geometric means. [Jain and Mishra (2022)](https://arxiv.org/pdf/2004.11024) develop derivatives, analytic dependence, and a symplectic Lidskii theorem. Most directly, Theorem 3.6 of [Mishra (2020)](https://arxiv.org/pdf/2007.10572) expresses directional derivatives at repeated symplectic eigenvalues through a Hermitian compression in a Williamson basis. The treatment of degeneracies in our geometric argument uses this established structure.

Theorem 2.5 of [Hiai and Lim (2018)](https://arxiv.org/pdf/1710.00494) proves that the **extended** symplectic spectrum, with every eigenvalue listed twice, is 1-Lipschitz for the Thompson metric. Their stated Riemannian trace-metric bound has constant $`\sqrt{2n}`$ for $`2n\times2n`$ matrices. Our proof needs the dimension-free estimate

```math
\|\log\nu(A)-\log\nu(B)\|_2
\le \frac{1}{\sqrt2}
\|\log(A^{-1/2}BA^{-1/2})\|_F,
```

where $`\nu`$ lists each symplectic eigenvalue once, in order. The repository gives the tangent estimate and path integration explicitly, with attribution to the derivative machinery above. We make **no separate priority claim** for this matrix inequality. The scientific claim rests on the resulting physical resource optimization; it does not require the auxiliary metric statement to be historically new.

## Scope of the comparison

This comparison was checked on **6 November 2026** using primary papers and publisher metadata. The focused search covered bosonic/Gaussian embezzlement with photon, energy, or mode constraints; approximate Gaussian catalysis and conversion fidelity; and symplectic-eigenvalue perturbation in affine-invariant or Riemannian metrics. The March 2026 version of Kera et al. was read directly. The matrix comparison above is based on inspected theorem statements, rather than abstract-level similarity. A September 2026 directional-derivative Lidskii preprint, [arXiv:2609.21620](https://arxiv.org/abs/2609.21620), also surfaced; only its indexed abstract was accessible, so no claim about its full contents or implications is made here. This is a bounded comparison, not an exhaustive priority certificate.

Within the inspected literature, the distinct contribution is a sharp asymptotic requirement on **both** the number of input catalyst modes and their total photon inventory, with a joint tradeoff achieved by passive local permutations of prepared squeezed-pair ladders. Increasing photon occupation cannot replace unbounded mode count, and increasing mode count cannot replace unbounded photon inventory, for vanishing error at fixed nonzero target squeezing. These statements concern pure Gaussian catalysts and the stated joint-fidelity contract; they are not claims about arbitrary mixed catalysts, preparation complexity, or universal borrowing of unknown targets.

## Background references

[Weedbrook et al. (2012)](https://doi.org/10.1103/RevModPhys.84.621) review Gaussian states, symplectic decompositions, measurements, and information protocols. [Adesso, Ragy, and Lee (2014)](https://arxiv.org/pdf/1401.4679) provide a didactic treatment of phase space, Gaussian operations, and correlations. [Serafini's textbook, second edition (2024)](https://www.routledge.com/Quantum-Continuous-Variables-A-Primer-of-Theoretical-Methods/Serafini/p/book/9781032169170) develops the formalism through Gaussian dynamics and continuous-variable entanglement. Bibliographic entries, stable identifiers, and inspected preprint versions are recorded in [references.bib](references.bib).
