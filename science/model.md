# Model and resource theorems

Alice and Bob share a pure Gaussian state of optical modes. They use local Gaussian processing to place a prescribed entangled Gaussian state in initially empty target modes. The entire catalyst must be returned close to its original state, jointly with the target. The resources are the number of entangled catalyst mode pairs and the catalyst's initial photon inventory.

## States, normalization and return criterion

Use quadratures with $`[q_j,p_\ell]=i\delta_{j\ell}`$ and vacuum covariance $`I/2`$. The standard two-mode squeezed vacuum is

```math
|r\rangle=\mathrm{sech}\,r
\sum_{m=0}^{\infty}(\tanh r)^m|m,m\rangle,
\qquad r\ge0.
```

Its mean photon number is $`\sinh^2r`$ at each party. The fixed target has $`k\ge1`$ nonzero Gaussian Schmidt squeezings $`\mathbf r=(r_1,\ldots,r_k)`$, with every $`r_j>0`$. Its canonical form is $`|R\rangle=\bigotimes_{j=1}^k|r_j\rangle`$. Any fixed pure bipartite Gaussian target is locally Gaussian equivalent to this form, with local vacuum factors as needed; a final local change of frame implements that target without changing the catalyst costs below.

The known catalyst $`|C\rangle`$ is an arbitrary finite-mode pure bipartite Gaussian state. Its nonzero Gaussian Schmidt squeezings are $`a_1,\ldots,a_n`$. Thus $`n`$ counts entangled mode pairs, and the physical number of catalyst modes at each party is at least $`n`$. Locally unentangled modes contribute zero Schmidt parameters. The optimal constructions use exactly $`n`$ physical catalyst modes at each party.

The input is $`|C\rangle`$ tensored with local target vacua. For the normalized retained output $`\rho_{\rm out}`$, define

```math
F=\langle C,R|\rho_{\rm out}|C,R\rangle,
\qquad
F\ge1-\varepsilon,\qquad 0<\varepsilon<1.
```

This is squared fidelity with a pure reference. It controls return of the original catalyst, preparation of the target and their joint decoupling in one criterion. The purified distance from the desired state is exactly $`\sqrt{1-F}`$. For the pure attaining outputs, this also equals half the trace distance. For a general mixed output, trace distance and infidelity are distinct error parameters.

The target list $`\mathbf r`$ is fixed as $`\varepsilon\downarrow0`$. The finite inequalities hold for every finite target list; the asymptotic theorem does not assert uniform estimates for a list growing with $`1/\varepsilon`$.

## Operations and charged resources

A finite Gaussian LOCC protocol consists of local Gaussian ancillas, finite Gaussian unitary dilations, Gaussian measurement instruments, discarding, classical communication and outcome-dependent Gaussian processing. Ancillas contain no shared entanglement. Their local number and energy, as well as the number of protocol outcomes, are unrestricted. A success event may have any strictly positive probability; $`\rho_{\rm out}`$ then denotes its normalized conditional output.

The converse also covers the trace-norm closure of these normalized retained outputs for each fixed input and target. This is an output-state closure: a formal unbounded filter is not included merely because it is written as a Gaussian expression. The [branch reduction](converse.md) explains why refining instruments and local environments gives a bound uniform over all outcomes and success events.

All charged catalyst oscillators have the same fixed frequency $`\omega>0`$. With vacuum energy subtracted, their initial total excitation energy is $`\hbar\omega E`$, where

```math
E=\sum_{\text{all catalyst modes}}\langle a_j^\dagger a_j\rangle.
```

Both parties' photons are counted. Initial local squeezing and displacements are included. At a fixed entanglement-squeezing vector,

```math
E\ge2\sum_{i=1}^{n}\sinh^2a_i,
```

with equality for a centered tensor product of canonical squeezed pairs; see [Gaussian geometry](gaussian_geometry.md). This inequality prevents a local change of Gaussian coordinates from lowering the charged inventory.

Local control work and preparation complexity are not charged by $`E`$. For canonical targets, the attaining protocol uses passive local permutations and conserves the actual initial total photon number. General target frame changes may require active local controls.

## Finite resource inequality

Define

```math
q_\varepsilon=
\frac12\mathrm{arcosh}^2\!\left(\frac1{1-\varepsilon}\right),
\qquad
T=\sum_{j=1}^{k}\sinh^2r_j,
\qquad
R=\sum_{j=1}^{k}r_j,
```

and, for $`\lambda\ge0`$,

```math
A_\lambda
=\sum_{j=1}^{k}\int_0^{r_j}\sqrt{\sinh^2x+\lambda}\,dx.
```

**Theorem 1 (finite converse).** Every protocol in the stated class with joint infidelity at most $`\varepsilon`$ satisfies

```math
\boxed{
q_\varepsilon
\left[\frac E2+T+\lambda(n+k)\right]
\ge A_\lambda^2
\quad\text{for every }\lambda\ge0.
}
```

In particular,

```math
n\ge\frac{R^2}{q_\varepsilon}-k,
\qquad
E\ge\frac{2A_0^2}{q_\varepsilon}-2T,
\qquad
K=A_0=\sum_{j=1}^{k}(\cosh r_j-1).
```

A negative finite lower bound is superseded by the nonnegativity of its resource. The theorem also bounds the physical catalyst mode count because that count is no smaller than $`n`$.

The proof has two distinct inputs. [Gaussian geometry](gaussian_geometry.md) bounds the displacement of the entanglement-squeezing vector by joint fidelity. [The converse](converse.md) combines the established pure Gaussian-LOCC ordering criterion with a weighted inequality for inserting the target squeezings into the sorted catalyst spectrum. The resource bound does not assume that the protocol is a permutation or that its output is pure.

## Sharp individual costs

Let $`n_{\min}(\varepsilon;\mathbf r)`$ be the smallest feasible number of catalyst Schmidt pairs, with no independent photon cap. Let $`E_{\rm opt}(\varepsilon;\mathbf r)`$ be the infimum of initial photon inventory over all finite-mode catalysts and allowed protocols. The infimum notation does not assume that a finite-mode minimizer exists.

**Theorem 2 (individual optima).** For a fixed target,

```math
\boxed{
\lim_{\varepsilon\downarrow0}
\varepsilon n_{\min}(\varepsilon;\mathbf r)=R^2,
\qquad
\lim_{\varepsilon\downarrow0}
\varepsilon E_{\rm opt}(\varepsilon;\mathbf r)=2A_0^2.
}
```

The same mode optimum holds when physical catalyst modes per party are minimized: the converse applies to their number, and the construction has no unused local catalyst modes.

For one target pair, these constants are $`r^2`$ and $`2(\cosh r-1)^2`$. For $`k`$ identical target pairs, they are $`k^2r^2`$ and $`2k^2(\cosh r-1)^2`$, with $`k`$ fixed in the limit.

The two optima are achieved by different families. Uniform squeezing spacings attain the mode optimum. An exponentially graded tail attains the energy coefficient with logarithmic mode overhead, $`n=O(\varepsilon^{-1}\log(1/\varepsilon))`$. [The construction account](constructions.md) gives finite catalysts and controls their errors.

## Full asymptotic tradeoff

A finite pair of normalized budgets $`(u,v)`$ is achievable if there are protocols for all sufficiently small $`\varepsilon`$ with

```math
F\ge1-\varepsilon,\qquad
\limsup_{\varepsilon\downarrow0}\varepsilon n\le u,
\qquad
\limsup_{\varepsilon\downarrow0}\varepsilon E\le v.
```

For $`\lambda>0`$, also define

```math
B_\lambda=\sum_{j=1}^{k}\int_0^{r_j}
\frac{dx}{\sqrt{\sinh^2x+\lambda}},
\qquad
C_\lambda=\sum_{j=1}^{k}\int_0^{r_j}
\frac{\sinh^2x\,dx}{\sqrt{\sinh^2x+\lambda}}.
```

Thus $`C_\lambda=A_\lambda-\lambda B_\lambda`$.

**Theorem 3 (joint boundary).** The achievable finite budget region is

```math
\boxed{
u\ge R^2,\qquad
v\ge V(u):=
2\sup_{\lambda\ge0}\bigl(A_\lambda^2-\lambda u\bigr).
}
```

For every $`u>R^2`$, there is a unique $`\lambda>0`$ with

```math
u=A_\lambda B_\lambda,\qquad
V(u)=2A_\lambda C_\lambda.
```

At the minimum-mode endpoint,

```math
V(R^2)=2RH,\qquad
H=\sum_{j=1}^{k}\int_0^{r_j}\sinh^2x\,dx.
```

As $`u\to\infty`$, $`V(u)\downarrow2A_0^2`$. Every finite $`u`$ has strictly larger photon coefficient. The energy-optimal coefficient therefore requires an unbounded normalized mode budget.

[The tradeoff proof](tradeoff.md) establishes the range and monotonicity of the contact parameter, the minimum-mode endpoint, and attainability for the prescribed accuracy. The result is an asymptotic boundary. The finite inequality in Theorem 1 is not asserted to be an exact finite-error resource frontier.

## Scope and reading route

Catalyst purity and Gaussian processing are essential assumptions of the converse. Purifying a mixed catalyst would generally introduce shared entanglement and photon resources that are not counted here. The return criterion also matters: exact marginal return, repeated use, or a trace-distance error budget defines a different optimization.

Read [the scientific overview](README.md) for the proof dependencies, [the physical interpretation](interpretation.md) for resource examples, and [related work](../references/related_work.md) for the inherited conversion criterion and spectral-shift mechanism.
