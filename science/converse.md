# Finite-resource converse under Gaussian LOCC

This chapter proves a resource bound for preparing a fixed pure bipartite Gaussian target while approximately returning a pure Gaussian catalyst. The bound applies to arbitrary local Gaussian processing, mixtures of its measurement branches, postselection with any positive success probability, and trace-norm limits of the normalized retained outputs.

With the conventions in [the model](model.md), every such protocol with squared joint fidelity at least $`1-\varepsilon`$ satisfies
```math
\begin{aligned}
\boxed{
q_\varepsilon
\left[\frac E2+T+\lambda(n+k)\right]
\ge A_\lambda^2
\qquad\text{for every }\lambda\ge0,
}
\end{aligned}
\tag{C1}
```
where
```math
\begin{aligned}
q_\varepsilon
&=\frac12\mathrm{arcosh}^2\!\left(\frac1{1-\varepsilon}\right),
\\
T&=\sum_{j=1}^k\sinh^2r_j,
\\
A_\lambda
&=\sum_{j=1}^k\int_0^{r_j}\sqrt{\sinh^2x+\lambda}\,dx.
\end{aligned}
\tag{C2}
```
The proof does not assume that a protocol is a passive permutation or that its retained output is pure.

## 1. States, resources, and sorted insertion

Let $`|C\rangle`$ be an arbitrary finite-mode pure Gaussian catalyst. Its nonzero Gaussian Schmidt squeezings are
$`\mathbf a=(a_1,\ldots,a_n)`$,
listed in descending order. All other local catalyst modes contribute zero squeezing entries. The physical catalyst mode count at either party is therefore at least $`n`$.

The fixed target has $`k\ge1`$ nonzero Gaussian Schmidt squeezings
$`\mathbf r=(r_1,\ldots,r_k)`$,
with each $`r_j>0`$. Its canonical state is
```math
|R\rangle=\bigotimes_{j=1}^k|r_j\rangle,
\qquad
|r\rangle=\mathrm{sech}\,r
\sum_{\ell=0}^\infty(\tanh r)^\ell|\ell,\ell\rangle.
```
Arbitrary fixed local Gaussian dressing of the target is also allowed: the converse uses its entanglement vector, and a local change of target frame does not change the charged initial catalyst inventory.

Target modes start in local vacuum. The desired final reference is the entire pure product
```math
|\Xi\rangle=|C\rangle\otimes|R\rangle.
```
For a normalized retained output $`\rho`$, including a success-conditioned output, write
```math
\begin{aligned}
F=\langle\Xi|\rho|\Xi\rangle.
\end{aligned}
\tag{C3}
```
This is squared fidelity, and it requires joint return and decoupling of the catalyst and target. It is not merely a condition on either marginal.

The charged photon inventory is
```math
E=\sum_{\text{initial catalyst modes at both parties}}
\langle a_j^\dagger a_j\rangle.
```
The [photon minimum theorem](gaussian_geometry.md) gives
```math
\begin{aligned}
\frac E2\ge\sum_{i=1}^n\sinh^2a_i.
\end{aligned}
\tag{C4}
```
It includes arbitrary initial displacement, local squeezing, and local mode mixing.

Define two vectors of length $`n+k`$:
```math
\begin{aligned}
\mathbf s&=\mathrm{sort}_{\downarrow}
(a_1,\ldots,a_n,\underbrace{0,\ldots,0}_{k}),
\\
\mathbf t&=\mathrm{sort}_{\downarrow}
(a_1,\ldots,a_n,r_1,\ldots,r_k).
\end{aligned}
\tag{C5}
```
The input and desired output Gaussian Schmidt vectors are respectively $`\mathbf s`$ and $`\mathbf t`$, apart from common trailing zeros. Since (C5) replaces zeros by nonnegative entries,
```math
\begin{aligned}
t_i\ge s_i
\qquad\text{for all }i.
\end{aligned}
\tag{C6}
```
For example, (C6) follows by comparing the number of entries above each threshold in the two lists.

The squared insertion displacement is
```math
\begin{aligned}
D(\mathbf a;\mathbf r)
=\sum_{i=1}^{n+k}(t_i-s_i)^2.
\end{aligned}
\tag{C7}
```
This number is unchanged by adding common trailing zeros. It is strictly positive for a nonzero target and a finite catalyst, since
```math
\begin{aligned}
\sum_i(t_i-s_i)=\sum_{j=1}^k r_j>0.
\end{aligned}
\tag{C8}
```

## 2. Physical Gaussian instruments and branch refinement

The finite operational class consists of local Gaussian ancillas, finite Gaussian unitary dilations, Gaussian measurement instruments, discarding, classical communication, and outcome-dependent Gaussian operations. No ancilla supplies shared entanglement. Classical randomization and measurable selection of success events are allowed. There is no bound on the finite number or energy of local ancillas, nor a positive lower bound on a success probability.

The word “Gaussian” concerns the quantum states and operations on a fine measurement branch. Forgetting outcomes, grouping them into a success event, or using nonlinear classical processing of records may produce a retained state that is a non-Gaussian mixture. Such mixtures are included in the proof below.

A finite dilation uses normalizable finite-mode Gaussian ancillary states and Gaussian unitaries with finite parameters. Its readout can use Gaussian POVMs and proper quadrature measurement instruments. A homodyne measurement is an operator-valued measurement with continuous outcomes; it does not supply an infinite-squeezed state as a free ancillary resource. A formal unbounded expression such as $`g^{a^\dagger a}`$ with $`g>1`$ is not, by itself, an allowed trace-nonincreasing quantum operation.

### Lemma 1. Pure Gaussian refinement

Every finite protocol in this class, on the pure input $`|C\rangle`$ and local target vacua, admits a refinement such that:

1. Each complete fine record has a pure Gaussian retained output for almost every outcome of nonzero probability density.
2. Ignoring the extra records reproduces the original retained state.
3. A coarse success event is the corresponding measurable set of fine records, with the same success probability.
4. The refinement introduces no interparty entanglement.

**Proof.** Purify every local mixed Gaussian ancilla using additional modes at that same party. Such a purification is finite: after a local Williamson transformation, each thermal mode is the reduction of a finite-squeezing two-mode Gaussian state, and both purifying modes remain local. This adds no shared entanglement.

Use the local Gaussian dilation of every instrument. Keep any local environment that would otherwise be discarded until it is read by a rank-one Gaussian measurement, for example heterodyne. The added readout is ignored by the later controls unless it was already part of the original record. Completeness of the local POVM implies that averaging this readout is exactly the original partial trace.

A Gaussian POVM with a mixed seed can likewise be refined into rank-one Gaussian seeds. To see this explicitly, if the seed covariance is
```math
W=S\mathrm{diag}(\boldsymbol\nu,\boldsymbol\nu)S^T,
\qquad \nu_i\ge\frac12,
```
then the pure covariance $`W_0=SS^T/2`$ obeys $`W_0\le W`$. A centered Gaussian seed with covariance $`W`$ is the Gaussian mixture of displacements of the pure seed with covariance $`W_0`$, with classical displacement covariance $`W-W_0`$. Recording this additional variable gives the rank-one refinement. For a measurement performed inside a dilation, all modes not belonging to its retained output are read out in the same way.

The full state, including the local purifications and dilation modes, begins pure. A Gaussian unitary preserves purity. Contraction against a rank-one Gaussian measurement vector leaves a pure Gaussian vector on the unmeasured modes whenever its probability density is nonzero. After all unused local modes have been read out, the retained conditional state is therefore pure Gaussian.

For homodyne readout, the same assertion is understood through the proper quadrature measurement instrument. In a position representation, a normalizable pure Gaussian wavefunction is restricted to the measured quadrature values. For almost every value with nonzero density, the remaining wavefunction is a normalizable pure Gaussian wavefunction; Fubini's theorem provides the usual conditional normalization. No quadrature eigenvector is treated as a normalizable ancillary state or a finite-probability isolated event.

Finally, original controls and success decisions depend on the original records. The refined protocol uses the same controls and forgets the additional records when reproducing the original protocol. Integrating them restores every original instrument and every original success event. All purifications, unitary dilations and refinements are local. ∎

This argument concerns physical Gaussian instruments with a dilation and a proper outcome measure. It does not infer physical implementability from a formal covariance transformation alone.

## 3. Ordered squeezing cannot increase on a fine branch

The componentwise ordering criterion for pure Gaussian LOCC is established by [Giedke, Eisert, Cirac and Plenio](https://arxiv.org/abs/quant-ph/0301038). Only its necessary direction is needed here. The following direct covariance proof makes that direction explicit for the refined instruments and their continuous outcomes.

### Lemma 2. Branchwise componentwise monotonicity

Along almost every complete fine record of a finite protocol, the nonnegative Gaussian Schmidt squeezing vector never increases componentwise when it is sorted in descending order and padded by zeros. If the retained pure output vector is $`\mathbf b`$, then
```math
\begin{aligned}
b_i\le s_i
\quad\text{for every }i,
\end{aligned}
\tag{C9}
```
where additional physical output slots are included as common trailing zeros.

**Proof.** A local Gaussian unitary preserves the vector. Adding a pure Gaussian ancillary state at one party changes only the zero padding.

Consider a rank-one Gaussian measurement at Alice after any chosen local dilation and Gaussian unitary. Fix the preceding fine history, so all covariance matrices and measurement settings are fixed. Let $`M`$ be the covariance of the modes being measured, $`B`$ Bob's covariance, and $`C`$ their cross covariance. A measurement with Gaussian seed covariance $`W`$ gives
```math
\begin{aligned}
B_y=B-C^T(M+W)^{-1}C\le B.
\end{aligned}
\tag{C10}
```
The result is independent of the current outcome $`y`$ except for first moments. Formula (C10) is the conditional Gaussian Schur complement, obtained by multiplying the joint Gaussian Wigner density by the Gaussian measurement effect and completing the square; see also [Adesso, Ragy and Lee, Sec. 3.4, Eq. (97)](https://arxiv.org/pdf/1401.4679).

For a measurement of commuting quadratures, let $`M_q`$ be the covariance of just those quadratures and $`C_q`$ their cross covariance with Bob. Ordinary Gaussian conditioning gives
```math
\begin{aligned}
B_y=B-C_q^T M_q^{-1}C_q\le B.
\end{aligned}
\tag{C11}
```
The premeasurement state has finite positive covariance, so the measured principal covariance $`M_q`$ is positive definite. This proves the needed inequality directly for the homodyne instrument as well.

The [symplectic Loewner monotonicity theorem](gaussian_geometry.md) now gives
```math
\nu_i(B_y)\le\nu_i(B)
```
in a common sorted order. The global state before this fine measurement and after it is pure. Its local symplectic eigenvalues are $`\cosh(2a_i)/2`$, together with $`1/2`$ for local pure modes. Since $`a\mapsto\cosh(2a)/2`$ is increasing for $`a\ge0`$, every sorted entanglement squeeze is nonincreasing.

The same reasoning applies when Bob measures, by looking at Alice's untouched covariance. Outcome-dependent local Gaussian unitaries may change these covariance matrices by local congruence, but do not change their symplectic eigenvalues. Iterate over the finite refined history to obtain (C9). ∎

The zero padding is substantive. An arbitrary number of free local Gaussian ancillary modes can enlarge the local Hilbert spaces, but it cannot add a positive entry to the shared Gaussian Schmidt vector. The proof uses no bound on their local energy.

## 4. A uniform fidelity ceiling

### Theorem 3. Spectrum-insertion fidelity bound

For every finite protocol in the stated class, every positive-probability success event, and every retained output in their trace-norm closure for the fixed input and target,
```math
\begin{aligned}
\boxed{
F\le\mathrm{sech}\,\!\left(\sqrt{2D(\mathbf a;\mathbf r)}\right).
}
\end{aligned}
\tag{C12}
```
Consequently, if $`F\ge1-\varepsilon`$, then
```math
\begin{aligned}
D(\mathbf a;\mathbf r)\le q_\varepsilon.
\end{aligned}
\tag{C13}
```

**Proof for a fine branch.** Let $`|\psi_\omega\rangle`$ be a retained pure Gaussian fine branch, with squeezing vector $`\mathbf b_\omega`$. By (C6) and (C9),
```math
t_i-b_{\omega,i}\ge t_i-s_i\ge0.
```
All entries beyond those in (C5) are common zeros. Therefore
```math
\begin{aligned}
\|\mathbf t-\mathbf b_\omega\|_2^2
\ge\|\mathbf t-\mathbf s\|_2^2
=D(\mathbf a;\mathbf r).
\end{aligned}
\tag{C14}
```
The [pure Gaussian fidelity bound](gaussian_geometry.md) gives
```math
\begin{aligned}
|\langle\Xi|\psi_\omega\rangle|^2
\le\mathrm{sech}
\!\left(\sqrt2\,\|\mathbf t-\mathbf b_\omega\|_2\right)
\le\mathrm{sech}\,\!\left(\sqrt{2D(\mathbf a;\mathbf r)}\right).
\end{aligned}
\tag{C15}
```
Both $`|C\rangle`$ and the fine branch may have arbitrary local Gaussian dressing and displacement: these were already included in the geometric bound.

**Mixtures and postselection.** Let $`\mu(d\omega)`$ be the probability measure on fine records, and let $`S`$ be any success event with $`p_S=\mu(S)>0`$. The retained state conditioned on success is
```math
\rho_S=\frac1{p_S}\int_S
|\psi_\omega\rangle\langle\psi_\omega|\,\mu(d\omega).
```
Since the reference is pure, its squared fidelity is affine:
```math
F_S
=\frac1{p_S}\int_S
|\langle\Xi|\psi_\omega\rangle|^2\,\mu(d\omega).
```
The bound (C15) is the same for every fine record outside a null set. Integrating it proves (C12) for $`\rho_S`$. There is no factor depending on $`p_S`$. No exact point of a continuous outcome distribution is selected as a finite-probability branch.

**Trace-norm closure.** Fix the catalyst, target, and retained mode space. Let $`\rho_\ell`$ be normalized retained outputs of finite protocols, with arbitrary positive success probabilities, and suppose
$`\|\rho_\ell-\rho\|_1\to0`$.
The reference projector is bounded, so
```math
\left|
\langle\Xi|\rho_\ell|\Xi\rangle
-\langle\Xi|\rho|\Xi\rangle
\right|
\le\|\rho_\ell-\rho\|_1\longrightarrow0.
```
The right side of (C12) depends only on the fixed input and target. It therefore also bounds $`\rho`$. The success probabilities may tend to zero; every **normalized** output already obeys the uniform bound.

This is a closure of retained states for each fixed input and target. It makes no assumption about convergence of covariances or photon expectations, neither of which follows from trace-norm convergence without additional hypotheses. It also does not assign an output to a zero limiting success map unless its normalized retained outputs actually converge.

Finally, inversion of (C12) gives (C13) with (C2). ∎

Because $`D>0`$ for every finite catalyst and nonzero target, (C12) also excludes exact joint borrowing with $`F=1`$ in this operational class. The asymptotic constructions instead let the catalyst resources grow while $`D`$ tends to zero.

## 5. Weighted finite-resource inequality

### Theorem 4. Weighted converse

Under the assumptions above, for every $`\lambda\ge0`$,
```math
\begin{aligned}
A_\lambda^2
\le
D(\mathbf a;\mathbf r)
\left[\frac E2+T+\lambda(n+k)\right].
\end{aligned}
\tag{C16}
```
Combining with (C13) proves (C1).

**Proof.** Define the continuous increasing function and its primitive
```math
f_\lambda(x)=\sqrt{\sinh^2x+\lambda},
\qquad
G_\lambda(x)=\int_0^x f_\lambda(y)\,dy,
\qquad x\ge0.
```
The case $`\lambda=0`$ is included: then $`f_0(x)=\sinh x`$.

Set $`\Delta_i=t_i-s_i\ge0`$. Because the two lists in (C5) differ by replacing $`k`$ zeros by the target squeezings, cancellation of the catalyst entries gives the exact identity
```math
\begin{aligned}
\sum_{i=1}^{n+k}\int_{s_i}^{t_i} f_\lambda(x)\,dx
&=\sum_i G_\lambda(t_i)-\sum_i G_\lambda(s_i)\\
&=\sum_{j=1}^kG_\lambda(r_j)\\
&=A_\lambda.
\end{aligned}
\tag{C17}
```
There is no disjointness assumption on these intervals; overlaps are counted with their natural multiplicity. This is why the same argument handles an arbitrary fixed finite target list.

Monotonicity of $`f_\lambda`$ and Cauchy–Schwarz now give
```math
\begin{aligned}
A_\lambda
&\le\sum_i\Delta_i f_\lambda(t_i)\\
&\le
\left(\sum_i\Delta_i^2\right)^{1/2}
\left(\sum_i f_\lambda(t_i)^2\right)^{1/2}.
\end{aligned}
\tag{C18}
```
The first factor squared is $`D`$. For the second,
```math
\begin{aligned}
\sum_i f_\lambda(t_i)^2
&=\sum_i\sinh^2t_i+\lambda(n+k)\\
&=\sum_{\ell=1}^n\sinh^2a_\ell
+\sum_{j=1}^k\sinh^2r_j+\lambda(n+k)\\
&\le \frac E2+T+\lambda(n+k),
\end{aligned}
\tag{C19}
```
where the final inequality is (C4). Squaring (C18) yields (C16). ∎

The finite target term $`T`$ arises from using the upper endpoint of every interval in (C18). It is part of this finite inequality. It drops out of the normalized small-error bound because the target is fixed.

Local Gaussian control work supplied during the protocol does not enter the proof. The photon estimate (C4) charges the actual initial catalyst state, while the branch ordering controls the interparty entanglement available to every later fine branch.

## 6. Finite mode and photon projections

Write
```math
R=\sum_{j=1}^k r_j,
\qquad
K=A_0=\sum_{j=1}^k(\cosh r_j-1).
```
Equation (C8) and Cauchy–Schwarz give
```math
R^2
=\left(\sum_{i=1}^{n+k}\Delta_i\right)^2
\le(n+k)\sum_i\Delta_i^2
=(n+k)D.
```
Hence any output with squared joint fidelity at least $`1-\varepsilon`$ obeys
```math
\begin{aligned}
n\ge\frac{R^2}{q_\varepsilon}-k.
\end{aligned}
\tag{C20}
```
The same bound applies to the physical catalyst mode count at either party, since it is no smaller than $`n`$. Equivalently, (C20) is the $`\lambda\to\infty`$ projection of (C1), using
$`A_\lambda/\sqrt\lambda\to R`$.

At $`\lambda=0`$, (C1) gives
```math
\begin{aligned}
E\ge\frac{2K^2}{q_\varepsilon}-2T.
\end{aligned}
\tag{C21}
```
When either displayed lower bound is negative, the nonnegativity of the resource gives the stronger statement.

For a fixed target list and $`\varepsilon\downarrow0`$, the geometric formula gives
$`q_\varepsilon=\varepsilon+O(\varepsilon^2)`$.
Thus every feasible resource family satisfies
```math
\begin{aligned}
\liminf_{\varepsilon\downarrow0}\varepsilon n
\ge R^2,
\qquad
\liminf_{\varepsilon\downarrow0}\varepsilon E
\ge2K^2.
\end{aligned}
\tag{C22}
```
For one target pair these coefficients are $`r^2`$ and $`2(\cosh r-1)^2`$. For several target pairs, the coefficients involve the squares of the **sums**, as shown in (C22).

More generally, any finite achievable normalized budgets $`(u,v)`$ with
$`\limsup\varepsilon n\le u`$ and $`\limsup\varepsilon E\le v`$
must satisfy
```math
\begin{aligned}
\frac v2+\lambda u\ge A_\lambda^2
\qquad\text{for every fixed }\lambda\ge0.
\end{aligned}
\tag{C23}
```
These are necessary bounds. The [construction chapter](constructions.md) and [tradeoff theorem](tradeoff.md) establish the matching small-error statements. Neither (C12) nor (C1) is asserted to be the exact optimum at finite resources.

## 7. Assumptions used by the converse

The proof permits arbitrary local Gaussian dressing of the initial catalyst and target, arbitrarily many free local Gaussian modes, outcome-dependent local Gaussian processing, discarded local environments, success probabilities approaching zero, and non-Gaussian mixtures formed by classical coarse graining. Its use of Gaussianity is on the refined quantum branches.

Two restrictions remain essential:

- **The shared catalyst is pure Gaussian.** Purifying a mixed shared catalyst is not the local ancillary refinement used above: its purification can add shared entanglement or alter the charged system. The converse therefore does not cover mixed catalysts.
- **The quantum processing is Gaussian.** A genuinely non-Gaussian local measurement or filter need not obey the covariance Schur complement or the componentwise ordering. Such operations are outside the stated class.

The target list is fixed in the asymptotic projections. The finite inequalities hold for each finite list, but no uniform large-target limit follows by silently replacing $`k`$ or $`r_j`$ by error-dependent values.

## References

- G. Giedke, J. Eisert, J. I. Cirac and M. B. Plenio, “Entanglement transformations of pure Gaussian states,” *Quantum Information and Computation* **3**, 211–223 (2003). [Primary preprint](https://arxiv.org/abs/quant-ph/0301038). The necessary componentwise ordering is used in the explicit form proved in Lemma 2; the source's squeeze parameter is twice the standard one used here.
- G. Adesso, S. Ragy and A. R. Lee, “Continuous variable quantum information: Gaussian states and beyond,” *Open Systems & Information Dynamics* **21**, 1440001 (2014). [DOI](https://doi.org/10.1142/S1230161214400010), [primary preprint](https://arxiv.org/abs/1401.4679). Section 3.4 gives the Gaussian conditional covariance formula.
- [Gaussian geometry, fidelity, and photon inventory](gaussian_geometry.md): the degeneracy-safe Williamson estimate, symplectic Loewner monotonicity, pure-state fidelity bound, and initial photon minimum used above.

