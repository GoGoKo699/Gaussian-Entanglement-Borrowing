# Weedbrook et al. and the Gaussian borrowing problem

The selected educational source is **Christian Weedbrook et al., “Gaussian quantum information,” Reviews of Modern Physics 84, 621–669 (2012)**: [published article](https://doi.org/10.1103/RevModPhys.84.621), [open author manuscript, arXiv:1110.3234v1, 14 October 2011](https://arxiv.org/pdf/1110.3234v1).

The review supplies the language of optical modes, covariance matrices, symplectic transformations, Gaussian measurements and fidelity. This page translates that language into the repository's conventions and then connects it to the borrowing theorem. The resource optimization itself is developed in the [scientific account](../science/README.md).

## Reading map

Section and equation numbers below refer to the inspected arXiv:1110.3234v1 manuscript. The published reference remains the 2012 RMP article.

| Source location | Connection to this project |
|---|---|
| I.D; II.A, especially II.A.1–2 | Quadrature normalization, moments and Gaussian transformations |
| II.B.1 and II.B.7, Eqs. (41)–(42) | Vacuum, thermal marginals and the squeezed-pair parameter |
| II.B.6; II.C.2 | Passive mode permutations as optical Gaussian operations |
| II.C.1 | Williamson spectra and local Gaussian frames |
| II.D.1 | Partial transpose as a phase-space operation |
| II.E.1–3 | Measurements, conditioning and discarded modes |
| III.A.3, Eq. (79) | Squared fidelity, the project's error convention |

The [30 milestones](milestones.md) organize these foundations and the subsequent research argument into a connected route.

## Convention dictionary

Use a subscript $`W`$ for review coordinates. Unsubscripted quantities below use this repository's convention, and all logarithms below are natural. The factors are fixed by [review Secs. I.D and II.A, Eqs. (5)–(7)](https://arxiv.org/pdf/1110.3234v1).

### Quadratures and covariance

For one mode,

```math
q_W=a+a^\dagger,\qquad p_W=i(a^\dagger-a),
\qquad [q_W,p_W]=2i,
```

whereas this project uses

```math
q=\frac{q_W}{\sqrt2},\qquad
p=\frac{p_W}{\sqrt2},\qquad
[q,p]=i.
```

Both covariance definitions use the symmetrized centered second moment. Therefore, in the same coordinate order,

```math
d=\frac{d_W}{\sqrt2},\qquad V=\frac{V_W}{2}.
```

| Quantity | Review convention | Project convention |
|---|---|---|
| Vacuum covariance | $`I`$ | $`I/2`$ |
| Physical covariance condition | $`V_W+i\Omega\ge0`$ | $`V+iJ/2\ge0`$ |
| Physical symplectic eigenvalues | $`\nu_{W,j}\ge1`$ | $`\nu_j=\nu_{W,j}/2\ge1/2`$ |
| One-mode annihilation operator | $`(q_W+ip_W)/2`$ | $`(q+ip)/\sqrt2`$ |

Changing units does not change the state or its photon number. It changes the numerical entries used to describe that state. In particular, halving the covariance while leaving the vacuum threshold at one would incorrectly classify valid pure states as unphysical.

### Coordinate order

The review uses the interleaved vector
$`\mathbf x_W=(q_{W,1},p_{W,1},\ldots,q_{W,M},p_{W,M})^T`$.
The general matrix arguments in [Gaussian geometry](../science/gaussian_geometry.md) use the grouped vector $`\mathbf x=(q_1,\ldots,q_M,p_1,\ldots,p_M)^T`$, with

```math
J_M=\begin{pmatrix}0&I_M\\-I_M&0\end{pmatrix}.
```

Let $`\Pi`$ send the grouped order to the interleaved order. The complete translation is

```math
\mathbf x=\frac{\Pi^T\mathbf x_W}{\sqrt2},\qquad
V=\frac{\Pi^T V_W\Pi}{2},\qquad
J_M=\Pi^T\Omega\Pi.
```

Transformations obey $`S=\Pi^TS_W\Pi`$. The covariance, symplectic form, means and transformation matrices must all use the same ordering. Subsystem block displays may reorder coordinates again; this is a simultaneous permutation, not a physical operation.

### Symplectic eigenvalues and squeezing

The squeezing magnitude $`r`$ agrees with the review's Fock-series parameter in Eq. (41): its magnitude ratio is $`\tanh r`$. That equation uses alternating signs. A local phase shift $`e^{i\pi a^\dagger a}`$ on either member removes them, giving our chosen frame

```math
|r\rangle=\mathrm{sech}\,r
\sum_{j=0}^{\infty}(\tanh r)^j|j,j\rangle.
```

This phase choice is separate from rescaling the quadrature units. On the selected mode its phase-space matrix is $`-I_2`$, so it changes the full covariance by the corresponding local congruence and reverses the cross-covariance signs. The local marginal covariances are unchanged. All overlaps in the project compare states in the same chosen frame. For the marginal of either member,

```math
V_{W,A}=\cosh(2r)I_2,
\qquad
V_A=\frac{\cosh(2r)}2I_2,
\qquad
\langle a^\dagger a\rangle=\sinh^2r.
```

Thus a local marginal symplectic eigenvalue determines
$`r=\tfrac12\mathrm{arcosh}(2\nu_A)`$.
The **global** pure two-mode state instead has symplectic eigenvalues $`1/2,1/2`$. Global purity and local mixedness encode different information: the local thermal noise is what reveals the shared entanglement.

This distinction explains the Gaussian Schmidt description. Local Gaussian unitaries remove local coordinate choices, leaving a list of paired squeezings and any unpaired local vacuum modes. The number of nonzero entries counts entangled mode pairs; it is not the infinite Hilbert-space dimension of an oscillator.

### Fidelity

**The review already uses squared fidelity.** In [Sec. III.A.3, Eq. (79)](https://arxiv.org/pdf/1110.3234v1),

```math
F(\rho,\sigma)
=\left[\mathrm{Tr}\,
\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\right]^2.
```

No additional square is needed when carrying that definition into this project. For a pure reference $`|\Xi\rangle`$,

```math
F(\rho,|\Xi\rangle)=\langle\Xi|\rho|\Xi\rangle,
\qquad
P(\rho,|\Xi\rangle)=\sqrt{1-F}.
```

The required reference is $`|\Xi\rangle=|C\rangle\otimes|R\rangle`$. Its overlap tests the original catalyst, the desired target and their decoupling together. Using only the target's overlap would not define the same borrowing task.

The multimode pure-state covariance formula used in the proof is derived in [geometry, Section 4](../science/gaussian_geometry.md#4-pure-gaussian-overlap-and-relative-squeezing). A research dependency, [Banchi, Braunstein and Pirandola (2015)](https://arxiv.org/abs/1507.01941), uses root fidelity $`\mathcal F`$ instead, so its formulas require $`F=\mathcal F^2`$. This conversion belongs to that dependency, not to the selected review.

### Photon inventory

The operator identity gives a direct check on all factors:

```math
a^\dagger a
=\frac{q^2+p^2-1}{2}
=\frac{q_W^2+p_W^2-2}{4}.
```

For $`M`$ physical catalyst modes in total, including both parties,

```math
E=\frac{\mathrm{Tr}\,V+\|d\|^2-M}{2}
=\frac{\mathrm{Tr}\,V_W+\|d_W\|^2-2M}{4}.
```

A canonical squeezed pair therefore contributes $`2\sinh^2r`$. For a Gaussian catalyst with entanglement squeezings $`a_1,\ldots,a_n`$, arbitrary local squeezing or displacement can only increase the inventory above

```math
E\ge2\sum_{i=1}^n\sinh^2a_i.
```

The project proves this lower bound explicitly. It charges the actual initial state, while leaving later local control work outside the inventory optimization.

## One catalyst pair and one target pair

Take a desired target squeezing $`r=\log2`$ and one catalyst pair with $`x=r/2`$. Each party swaps its catalyst oscillator with its initially empty target oscillator. In target-then-catalyst order,

```math
|0\rangle_T\otimes|x\rangle_C
\longmapsto
|x\rangle_T\otimes|0\rangle_C.
```

Here $`|0\rangle`$ denotes the two-mode vacuum. The desired reference is $`|r\rangle_T\otimes|x\rangle_C`$.

First check the inventory. Since $`\cosh(2x)=5/4`$, each catalyst marginal has covariance $`5I_2/4`$ in review units and $`5I_2/8`$ in project units. Both give the same per-party photon number:

```math
\frac{\mathrm{Tr}(5I_2/8)-1}{2}
=\frac{\mathrm{Tr}(5I_2/4)-2}{4}
=\frac18.
```

The initial catalyst thus contains $`E=1/4`$ photons on average across both parties. After the swaps these photons are in the target; the returned catalyst is vacuum.

Next calculate the complete return error. The geometric series gives

```math
\langle a|b\rangle
=\frac{\mathrm{sech}\,a\,\mathrm{sech}\,b}
{1-\tanh a\tanh b}
=\mathrm{sech}(a-b).
```

Therefore

```math
F=|\langle r|x\rangle|^2|\langle x|0\rangle|^2
=\mathrm{sech}^4\,x
=\left(\frac89\right)^2
=\frac{64}{81}.
```

The joint infidelity is $`17/81`$, and the purified distance is $`\sqrt{17}/9`$. Each separate squared overlap, or fidelity, is $`8/9`$; reporting either one alone would miss part of the error. This small example is an explicit finite protocol, not an optimality assertion. Many intermediate squeezing levels make each displacement smaller and reduce the joint error.

## From the source to the resource theorem

### 1. Require return of the same shared state

The [model](../science/model.md) specifies a known pure Gaussian catalyst and a fixed pure Gaussian target. The target begins in local vacuum, and the original catalyst appears in the final reference. For the construction, the target gains photons that leave the catalyst. Fidelity closeness does not require the expectation of an unbounded observable such as photon number to remain uniformly close across a family whose inventory diverges.

The resource pair is $`(n,E)`$: entangled catalyst mode pairs and initial photons. Neither an entropy alone nor a covariance norm alone is the stated cost or error.

### 2. Control measurements and postselection

The review's conditional Gaussian framework leads to the covariance update

```math
B_y=B-C^T(M+W)^{-1}C\le B
```

for a Gaussian readout with seed covariance $`W`$. The [converse](../science/converse.md) uses local Gaussian purifications and refined measurements to obtain pure Gaussian outputs on fine records. Their sorted squeezing vectors cannot increase componentwise. This ordering is established in [Giedke et al. (2003)](https://arxiv.org/abs/quant-ph/0301038); the repository also proves the necessary direction for its operational class.

An averaged or success-conditioned output need not be Gaussian. Nevertheless, with a pure reference,

```math
\langle\Xi|\rho_{\rm out}|\Xi\rangle
=\int|\langle\Xi|\psi_\omega\rangle|^2\,\mu(d\omega).
```

Here $`\mu`$ is the normalized distribution of retained records. A bound that holds for almost every fine record also bounds this average. This is why arbitrarily small positive success probabilities cannot improve the resource coefficient.

### 3. Turn state fidelity into a spectral displacement bound

Knowing that squeezings cannot increase is qualitative. A resource theorem also needs to quantify how much joint fidelity is lost when the desired squeezing list differs from an allowed one.

The [geometry chapter](../science/gaussian_geometry.md) combines logarithmic symplectic-spectrum control with the partial-transpose spectrum

```math
\nu(V^\Gamma)
=\left\{\frac12e^{2a_i},\frac12e^{-2a_i}\right\}_i,
```

including additional $`1/2`$ entries for unpaired local modes. It proves that two pure Gaussian states with squeezing lists $`\mathbf a,\mathbf b`$ obey

```math
F\ge1-\varepsilon
\quad\Longrightarrow\quad
\|\mathbf a-\mathbf b\|_2^2\le q_\varepsilon,
\qquad
q_\varepsilon=\frac12\mathrm{arcosh}^2
\left(\frac1{1-\varepsilon}\right)
=\varepsilon+O(\varepsilon^2).
```

The coefficient is independent of the number of modes. That uniformity matters because the constructions use more modes as the error falls. The derivative machinery has an established predecessor in [Mishra (2020), Theorem 3.6](https://doi.org/10.1016/j.laa.2020.07.003); the project includes the matrix estimate and its application, without a separate priority claim for the auxiliary inequality.

### 4. Insert the target into the squeezing list

For one target pair, let $`\mathbf s`$ be the sorted input list $`(a_1,\ldots,a_n,0)`$, and let $`\mathbf t`$ sort $`(a_1,\ldots,a_n,r)`$. Define $`\Delta_i=t_i-s_i\ge0`$. The common catalyst entries cancel in sums, leaving

```math
\sum_i\Delta_i=r,
\qquad
D=\sum_i\Delta_i^2\le q_\varepsilon.
```

Cauchy–Schwarz immediately gives the mode bound

```math
r^2\le(n+1)D\le(n+1)q_\varepsilon.
```

For photons, use a weight that recognizes how costly a squeezing level is:

```math
\begin{aligned}
\cosh r-1
&=\sum_i\int_{s_i}^{t_i}\sinh x\,dx\\
&\le\sum_i\Delta_i\sinh t_i\\
&\le\sqrt{D}
\sqrt{\sum_i\sinh^2t_i}\\
&\le\sqrt{q_\varepsilon}
\sqrt{E/2+\sinh^2r}.
\end{aligned}
```

The integral identity remains true even when its intervals overlap: it is cancellation of endpoint primitives, with multiplicities retained. For $`k`$ fixed target pairs, insert $`k`$ target squeezings in place of $`k`$ zeros. With

```math
R=\sum_jr_j,\qquad
K=\sum_j(\cosh r_j-1),\qquad
T=\sum_j\sinh^2r_j,
```

the finite bounds become

```math
R^2\le(n+k)q_\varepsilon,
\qquad
K^2\le q_\varepsilon(E/2+T).
```

Both the list length and the target-photon term change. The squared sums $`R^2`$ and $`K^2`$ explain the coefficients for several borrowed pairs.

### 5. Match the bounds with passive ladders

The [constructions](../science/constructions.md) extend the worked example to

```math
r=x_0>x_1>\cdots>x_n>x_{n+1}=0,
\qquad
F=\prod_{i=0}^n\mathrm{sech}^2(x_i-x_{i+1}).
```

For small gaps, $`-\log F`$ approaches their squared sum. Equal gaps minimize that sum at a fixed number of gaps, giving the mode coefficient $`r^2`$. Minimizing photons instead favors spending more levels near zero, where they are inexpensive. The photon-optimal tail can be chosen exponential in the index after the change of variable $`\tanh(x_i/2)`$.

The simultaneous optimization uses $`f_\lambda(x)=\sqrt{\sinh^2x+\lambda}`$. The construction chooses gaps approximately proportional to $`f_\lambda`$, while the converse uses the same weight. For the fixed target list and $`\lambda>0`$, define

```math
A_\lambda=\sum_j\int_0^{r_j}f_\lambda(x)\,dx,
\qquad
B_\lambda=\sum_j\int_0^{r_j}\frac{dx}{f_\lambda(x)},
\qquad
C_\lambda=A_\lambda-\lambda B_\lambda.
```

The [tradeoff proof](../science/tradeoff.md) controls the finite discretization and shows that the asymptotic boundary is

```math
(u,v)=(A_\lambda B_\lambda,\;2A_\lambda C_\lambda),
\qquad
u=\lim\varepsilon n,\quad v=\lim\varepsilon E,
\quad\lambda>0.
```

The contact curve approaches the minimum-mode endpoint as $`\lambda\to\infty`$; the separate uniform-ladder construction attains that endpoint. As $`\lambda\downarrow0`$, the photon coefficient approaches its infimum while the normalized mode budget diverges. The boundary is proved for fixed finite targets and vanishing infidelity; it is not an exact finite-error optimum.

## The resulting physical statement

For one fixed nonzero target squeezing, the sharp individual costs are

```math
\varepsilon n_{\min}\longrightarrow r^2,
\qquad
\varepsilon E_{\rm opt}\longrightarrow2(\cosh r-1)^2.
```

The optical construction needs no increasingly squeezed individual mode: every prepared pair has squeezing at most the largest target value. Accuracy comes from a growing collection of pairs and a controlled distribution of their squeezings. The converse explains why extra brightness cannot replace enough entangled modes, and why extra weak modes cannot keep the total initial photons bounded.

These conclusions concern pure Gaussian catalysts, Gaussian processing and joint return in squared fidelity. The [physical interpretation](../science/interpretation.md) separates those limits from control work, preparation complexity, mixed catalysts and non-Gaussian alternatives.
