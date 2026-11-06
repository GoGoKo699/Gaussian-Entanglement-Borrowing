# Gaussian geometry, fidelity, and photon inventory

This chapter proves the geometric estimates used in the [finite-resource converse](converse.md). The covariance convention is vacuum covariance $`I/2`$, and fidelity is **squared** Uhlmann fidelity. For two pure states this means $`F(\psi,\phi)=|\langle\psi|\phi\rangle|^2`$.

The central estimate is
```math
\|\mathbf a-\mathbf b\|_2^2
\le \frac12\operatorname{arcosh}^2\!\left(\frac1{F(\psi,\phi)}\right),
\tag{G1}
```
where $`\mathbf a`$ and $`\mathbf b`$ are the sorted Gaussian Schmidt squeezing vectors of arbitrary pure bipartite Gaussian states on the same modes. Local squeezing, displacement, mode mixing, and degeneracies are all allowed.

## 1. Positive matrices and symplectic spectra

For $`m`$ canonical modes, write
```math
J_m=
\begin{pmatrix}
0&I_m\\
-I_m&0
\end{pmatrix}.
```
A real matrix $`S`$ is symplectic if $`S^T J_m S=J_m`$. Canonical coordinate reorderings will occasionally put a subsystem or a group of modes together; $`J`$ is reordered with the coordinates.

For a real positive-definite $`2m\times2m`$ matrix $`A`$, Williamson's theorem gives a symplectic matrix $`S`$ such that
```math
S^TAS=D
=\operatorname{diag}(\nu_1,\ldots,\nu_m,\nu_1,\ldots,\nu_m),
\qquad \nu_i>0.
```
The ordered numbers $`\nu_i(A)`$ are the symplectic eigenvalues, listed **once** each. Equivalently, the Hermitian matrix
```math
K(A)=iA^{1/2}J_mA^{1/2}
```
has eigenvalues $`\{\nu_i(A),-\nu_i(A)\}_{i=1}^m`$.

For completeness, the Williamson congruence follows from the ordinary orthogonal normal form of the invertible real skew-symmetric matrix $`A^{1/2}J_mA^{1/2}`$. Choose an orthogonal $`O`$ for which
```math
O^T A^{1/2}J_mA^{1/2}O=DJ_m,
```
and set $`S=A^{-1/2}OD^{1/2}`$. Then $`S^TAS=D`$. Using
```math
A^{-1/2}J_mA^{-1/2}
=-\bigl(A^{1/2}J_mA^{1/2}\bigr)^{-1}
```
also gives $`S^T J_mS=J_m`$.

Define the affine-invariant positive-matrix distance
```math
\delta(A,B)
=\left\|\log\!\left(A^{-1/2}BA^{-1/2}\right)\right\|_F.
\tag{G2}
```
It is invariant under every invertible real congruence:
```math
\delta(L^TAL,L^TBL)=\delta(A,B).
\tag{G3}
```
Indeed, the square of (G2) is the sum of the squared logarithms of the eigenvalues of $`A^{-1}B`$, and those eigenvalues are unchanged by the congruence. The corresponding tangent norm is
```math
\|X\|_A^2
=\operatorname{Tr}(A^{-1}XA^{-1}X)
=\|A^{-1/2}XA^{-1/2}\|_F^2,
\tag{G4}
```
which is likewise invariant under simultaneous congruence of $`A`$ and $`X`$.

## 2. Logarithmic Williamson contraction

**Theorem 1.** For positive-definite $`A,B`$ of the same size, with symplectic eigenvalues in the same sorted order,
```math
\boxed{
\|\log\boldsymbol\nu(A)-\log\boldsymbol\nu(B)\|_2
\le \frac{\delta(A,B)}{\sqrt2}.
}
\tag{G5}
```
Equivalently, the extended symplectic spectrum that repeats each eigenvalue twice is 1-Lipschitz for $`\delta`$. The constant is independent of the number of modes.

### 2.1. The derivative at a degenerate Williamson block

Let $`A(t)`$ be a differentiable positive-matrix path and fix a time $`t_0`$. Choose a Williamson matrix at that time, and **hold it fixed while transforming the tangent**:
```math
S^T A(t_0)S=D,\qquad
X=S^T A'(t_0)S,\qquad
G=D^{-1/2}XD^{-1/2}.
\tag{G6}
```
By (G4), the squared speed of the path at this time is $`\|G\|_F^2`$. No derivative of a moving Williamson basis is being taken.

Consider a block in which the symplectic eigenvalue $`\nu`$ has multiplicity $`\ell`$. Order its coordinates as its $`\ell`$ positions followed by its $`\ell`$ momenta, and write
```math
G_\nu=
\begin{pmatrix}
Q&C\\
C^T&P
\end{pmatrix},
\qquad Q=Q^T,\quad P=P^T.
```
The first-order changes of the $`\ell`$ logarithmic symplectic eigenvalues in this block are the eigenvalues of
```math
H_\nu
=\frac{Q+P}{2}+\frac{i(C^T-C)}2.
\tag{G7}
```

Here is the compression calculation, including its normalization. In the Williamson coordinates, let
$`R(t)=(D+(t-t_0)X+o(t-t_0))^{1/2}`$.
Its derivative solves
```math
D^{1/2}R'+R'D^{1/2}=X.
```
Within the chosen block, $`R'_\nu=X_\nu/(2\sqrt\nu)`$. Thus the block of the derivative of $`iRJR`$ is
```math
K'_\nu
=\frac{i}{2}(X_\nu J_\ell+J_\ell X_\nu).
```
The $`+\nu`$ eigenspace of $`i\nu J_\ell`$ is the range of the isometry
```math
U=\frac1{\sqrt2}\begin{pmatrix}I_\ell\\-iI_\ell\end{pmatrix}.
```
Consequently,
```math
U^\dagger K'_\nu U
=U^\dagger X_\nu U
=\nu U^\dagger G_\nu U
=\nu H_\nu.
```
First-order Hermitian perturbation theory says that the derivatives of the eigenvalue cluster are the eigenvalues of this compression. Dividing by $`\nu`$ gives (G7) for the logarithms. Cross-block tangent entries do not enter the first-order compression. If a sorted eigenvalue is not two-sided differentiable at a crossing, the same statement applies to its one-sided derivatives as an unordered cluster; the squared norm of the cluster derivative is unchanged.

The compression rule can also be seen directly. Split the Hermitian matrix into the eigenspace of $`\nu`$ and its orthogonal complement. In this basis a differentiable perturbation has the form
```math
\begin{pmatrix}
\nu I+\tau L+o(\tau)&O(\tau)\\
O(\tau)&K_\perp+O(\tau)
\end{pmatrix},
```
where $`K_\perp-\nu I`$ is invertible. For the eigenvalues within $`O(\tau)`$ of $`\nu`$, eliminating the complementary block changes the first block by $`O(\tau^2)`$. The first-order eigenvalue shifts are therefore exactly the eigenvalues of $`L`$. Here $`L=U^\dagger K'_\nu U`$.

The compression formula is standard symplectic perturbation machinery; see [Mishra, Theorem 3.6](https://doi.org/10.1016/j.laa.2020.07.003). Its derivation is included here to make the treatment of degeneracies and factors of two explicit.

### 2.2. A dimension-independent tangent estimate

The squared Euclidean norm of the logarithmic derivative vector in this block is
```math
\begin{aligned}
\operatorname{Tr}H_\nu^2
&=\frac14\|Q+P\|_F^2+\frac14\|C^T-C\|_F^2\\
&\le \frac12\bigl(\|Q\|_F^2+\|P\|_F^2\bigr)+\|C\|_F^2\\
&=\frac12\|G_\nu\|_F^2.
\end{aligned}
\tag{G8}
```
Summing over the distinct Williamson blocks and retaining the nonnegative contribution of all cross-block entries gives
```math
\left\|\frac{d}{dt}\log\boldsymbol\nu(A(t))\right\|_2^2
\le \frac12\|A'(t)\|_{A(t)}^2
\tag{G9}
```
at almost every time.

This almost-everywhere assertion is sufficient even when eigenvalues coincide over intervals. The map $`A\mapsto K(A)`$ is smooth on the positive cone. Ordered Hermitian eigenvalues are locally Lipschitz, and the positive eigenvalues of $`K(A)`$ stay away from zero on a compact positive path. The sorted logarithmic symplectic eigenvalues are therefore absolutely continuous along the path. Their endpoint difference is bounded by the integral of the norm of their almost-everywhere derivative.

### 2.3. Integration along an explicit path

Use
```math
A(t)=A^{1/2}
\left(A^{-1/2}BA^{-1/2}\right)^t
A^{1/2},
\qquad 0\le t\le1.
```
Let $`C=A^{-1/2}BA^{-1/2}`$. In the congruence coordinates in which this path is $`C^t`$,
```math
(C^t)^{-1}\frac{d}{dt}C^t=\log C.
```
Its speed in (G4) is consequently the constant $`\|\log C\|_F=\delta(A,B)`$. Integrating (G9) proves (G5).

The constant is attained, for example, by $`A=aI_{2m}`$ and $`B=bI_{2m}`$: the left side is $`\sqrt m\,|\log(b/a)|`$ and the right side is the same number.

**Literature relation.** [Hiai and Lim, Theorem 2.5](https://doi.org/10.1016/j.laa.2018.04.029) proves symplectic-spectrum monotonicity and gives a dimension-dependent $`\sqrt{2m}`$ Lipschitz bound for the extended spectrum in this metric. The proof above supplies the particular dimension-independent estimate needed here; it does not assume that stronger constant from their theorem.

### 2.4. Symplectic Loewner monotonicity

**Corollary 2.** If $`0<A\le B`$, then
```math
\nu_i(A)\le\nu_i(B)
\quad\text{for every }i
\tag{G10}
```
in a common sorted order.

**Proof.** Along $`A(t)=A+t(B-A)`$, the tangent is positive semidefinite. In (G6), $`G\ge0`$, so every principal block $`G_\nu`$ and every compression $`H_\nu=U^\dagger G_\nu U`$ is positive semidefinite. All almost-everywhere derivatives of the sorted logarithmic symplectic eigenvalues are nonnegative. Absolute continuity then gives (G10). This is also the monotonicity theorem discussed in the sources above. ∎

## 3. Pure bipartite Gaussian normal form

For quadratures $`R`$ satisfying $`[R_j,R_\ell]=iJ_{j\ell}`$, define
```math
d_j=\langle R_j\rangle,\qquad
V_{j\ell}
=\frac12\langle\{R_j-d_j,R_\ell-d_\ell\}\rangle.
```
A finite-mode pure Gaussian covariance obeys
```math
VJV=\frac J4.
\tag{G11}
```
Equivalently, $`2V`$ is a positive symplectic matrix. Displacements affect neither this condition nor bipartite entanglement.

Every pure bipartite Gaussian state is equivalent, under local Gaussian unitaries, to a product of two-mode squeezed vacua and local vacuum modes. Write its nonnegative squeezing vector in descending order as $`\mathbf a=(a_1,a_2,\ldots)`$, padded by zeros. We use the standard parameter
```math
|a\rangle
=\operatorname{sech}a\sum_{j=0}^{\infty}(\tanh a)^j|j,j\rangle.
\tag{G12}
```
For one pair, in the order of Alice's quadratures followed by Bob's,
```math
V_a=\frac12
\begin{pmatrix}
\cosh(2a)I_2&\sinh(2a)Z\\
\sinh(2a)Z&\cosh(2a)I_2
\end{pmatrix},
\qquad
Z=\operatorname{diag}(1,-1).
\tag{G13}
```
This normal form is the Gaussian Schmidt decomposition; see [Giedke, Eisert, Cirac and Plenio, Lemma 1](https://arxiv.org/pdf/quant-ph/0301038). Their squeezing variable is twice the one in (G12).

A short covariance proof also fixes the role of degeneracies and unpaired local modes. Let $`\Gamma=2V`$, and use local Williamson transformations to put its local blocks in the forms $`A=\bigoplus_i c_iI_2`$ and $`B=\bigoplus_j d_jI_2`$, with $`c_i,d_j\ge1`$. If $`C_{ij}`$ is a two-mode block of its cross covariance, purity implies
```math
c_iJ_1C_{ij}+d_jC_{ij}J_1=0.
```
It follows that $`C_{ij}=0`$ unless $`c_i=d_j`$. Within a common value $`c`$, the cross block anticommutes with the corresponding symplectic forms, and the diagonal purity equations give
```math
CC^T=(c^2-1)I,\qquad C^TC=(c^2-1)I.
```
For $`c>1`$, the multiplicities on the two parties agree and $`C/\sqrt{c^2-1}`$ is orthogonal and antisymplectic. A local orthogonal symplectic transformation converts it into the direct sum of copies of $`Z`$. For $`c=1`$, the cross block vanishes and the corresponding modes are local vacua. Setting $`c=\cosh(2a)`$ gives (G13).

### Partial-transpose symplectic spectrum

Partial transpose on Bob acts on covariance matrices by
```math
V^\Gamma=PVP,
```
where $`P`$ reverses Bob's momenta and leaves all other quadratures unchanged. Although $`V^\Gamma`$ need not satisfy the quantum uncertainty relation, it remains an ordinary positive-definite matrix.

For the pair (G13), partial transpose changes the cross block to $`\sinh(2a)I_2/2`$. A balanced passive mode transformation diagonalizes it into
```math
\frac12e^{2a}I_2
\quad\text{and}\quad
\frac12e^{-2a}I_2.
```
Thus the symplectic spectrum of $`V^\Gamma`$ is
```math
\left\{\frac12e^{2a_i},\frac12e^{-2a_i}\right\}_i,
\tag{G14}
```
together with $`1/2`$ for any unpaired local vacuum modes.

This spectrum is unaffected by arbitrary local Gaussian dressing. Indeed, if $`S_A\oplus S_B`$ is local symplectic, then after partial transpose it becomes
$`S_A\oplus(P_BS_BP_B)`$.
Since $`P_BJ_BP_B=-J_B`$, the matrix $`P_BS_BP_B`$ is again symplectic.

## 4. Pure Gaussian overlap and relative squeezing

For two pure Gaussian states with covariances $`V,W`$ and means $`d,e`$, their squared fidelity is
```math
F(\psi,\phi)
=
\frac{
\exp\!\left[-\frac12(d-e)^T(V+W)^{-1}(d-e)\right]
}{
\sqrt{\det(V+W)}
}.
\tag{G15}
```
One way to obtain (G15) is to use
$`\operatorname{Tr}(\rho\sigma)=(2\pi)^m\int W_\rho(z)W_\sigma(z)\,dz`$,
insert the two normalized Gaussian Wigner functions, and complete the square. For pure states this Hilbert–Schmidt overlap is squared fidelity. The same convention follows by squaring the root fidelity used by [Banchi, Braunstein and Pirandola](https://doi.org/10.1103/PhysRevLett.115.260501).

Apply a common global symplectic congruence sending $`V`$ to $`I/2`$. The other covariance becomes $`M/2`$, where $`M`$ is positive and symplectic. Its ordinary eigenvalues occur in reciprocal pairs:
```math
\operatorname{spec}(M)=\{e^{2\kappa_j},e^{-2\kappa_j}\}_{j=1}^m,
\qquad \kappa_j\ge0.
```
For example, $`MJM=J`$ implies $`MJ=JM^{-1}`$, which pairs an eigenvector of eigenvalue $`e^{2\kappa_j}`$ with one of eigenvalue $`e^{-2\kappa_j}`$.

The metric and the centered overlap are therefore
```math
\delta(V,W)^2=8\sum_{j=1}^m\kappa_j^2,
\qquad
F_0=\prod_{j=1}^m\operatorname{sech}\kappa_j.
\tag{G16}
```
Here $`F_0`$ is (G15) with relative displacement zero. In particular, $`F\le F_0`$. The global congruence is used only to evaluate the metric and overlap, both invariant under applying the same Gaussian unitary to the two states. It is not used to identify the bipartite entanglement of the transformed states.

## 5. Fidelity controls Gaussian entanglement distance

**Theorem 3.** Let $`\psi,\phi`$ be pure Gaussian states on the same bipartite mode space, with sorted Gaussian Schmidt vectors $`\mathbf a,\mathbf b`$. Include all zero entries needed to give the vectors the same length. Then (G1) holds. Equivalently,
```math
\boxed{
F(\psi,\phi)
\le \operatorname{sech}\!\left(\sqrt2\,\|\mathbf a-\mathbf b\|_2\right).
}
\tag{G17}
```

**Proof.** By (G14), the positive and negative logarithmic branches of the partially transposed symplectic spectra give
```math
\|\log\boldsymbol\nu(V^\Gamma)
-\log\boldsymbol\nu(W^\Gamma)\|_2^2
=8\|\mathbf a-\mathbf b\|_2^2.
```
The constant shift $`-\log2`$ and all extra local vacuum eigenvalues cancel. Since partial transpose is an invertible congruence, (G3) and (G5) imply
```math
\|\mathbf a-\mathbf b\|_2^2
\le\frac{\delta(V,W)^2}{16}
=\frac12\sum_j\kappa_j^2.
\tag{G18}
```

For $`x\ge0`$, the function $`g(x)=\log\cosh\sqrt x`$ is concave and satisfies $`g(0)=0`$. To verify concavity, note that
```math
g'(x)=\frac{\tanh\sqrt x}{2\sqrt x}
```
with its continuous value at zero. The function $`\tanh u/u`$ is decreasing because
$`u\operatorname{sech}^2u-\tanh u\le0`$.
A nonnegative concave function vanishing at zero is subadditive: applying concavity with weights $`x/(x+y)`$ and $`y/(x+y)`$ yields $`g(x)+g(y)\ge g(x+y)`$. Hence
```math
\cosh\sqrt{\sum_j\kappa_j^2}
\le\prod_j\cosh\kappa_j
=\frac1{F_0}
\le\frac1F.
```
Combine this with (G18) to obtain (G1), and invert the monotone function to obtain (G17). ∎

For $`0<\varepsilon<1`$, it is convenient to define
```math
q_\varepsilon
=\frac12\operatorname{arcosh}^2\!\left(\frac1{1-\varepsilon}\right)
=\varepsilon+\frac56\varepsilon^2+O(\varepsilon^3).
\tag{G19}
```
Thus squared fidelity at least $`1-\varepsilon`$ implies squared entanglement-vector distance at most $`q_\varepsilon`$.

The leading constant cannot be improved uniformly. Two aligned TMSVs whose squeezings differ by $`h`$ have $`F=\operatorname{sech}^2h`$ and squared entanglement-vector distance $`h^2`$. Their ratio in (G1) tends to one as $`h\to0`$. This is a statement about the small-error constant; (G17) is not asserted to be the exact maximum overlap at every fixed pair of entanglement vectors.

## 6. Minimum photon inventory at fixed Gaussian entanglement

Let $`\psi`$ be a pure bipartite Gaussian state with finite physical mode counts and Gaussian Schmidt squeezings $`a_1,\ldots,a_n>0`$. Its total initial mean photon number, summed over both parties, is
```math
E=\sum_j\langle a_j^\dagger a_j\rangle.
```
Here the annihilation operators in the sum label physical modes; their label is unrelated to the squeezing parameters $`a_i`$.

**Theorem 4.** Arbitrary displacement and local Gaussian dressing satisfy
```math
\boxed{
E\ge 2\sum_{i=1}^n\sinh^2a_i.
}
\tag{G20}
```
Equality is attained by the centered tensor product of the corresponding TMSVs, with any additional physical modes in vacuum.

**Proof.** A local covariance with symplectic eigenvalues $`\mu_i`$ can be written
```math
V_A=S\operatorname{diag}(\boldsymbol\mu,\boldsymbol\mu)S^T.
```
Write the paired columns of the symplectic matrix $`S`$ as $`u_i,v_i`$. Since $`u_i^TJv_i=1`$ and $`J`$ is orthogonal,
```math
\|u_i\|^2+\|v_i\|^2
\ge2\|u_i\|\,\|v_i\|
\ge2|u_i^TJv_i|
=2.
```
Consequently,
```math
\operatorname{Tr}V_A
=\sum_i\mu_i(\|u_i\|^2+\|v_i\|^2)
\ge2\sum_i\mu_i.
\tag{G21}
```
If Alice has $`N_A`$ physical modes, her photon count is
```math
E_A=\frac12\left(\operatorname{Tr}V_A+\|d_A\|^2-N_A\right).
```
The Gaussian Schmidt form gives local symplectic eigenvalues
$`\cosh(2a_i)/2`$ for the entangled modes and $`1/2`$ for the remaining local modes. By (G21) and the nonnegative displacement contribution,
```math
E_A\ge\frac12\sum_{i=1}^n\bigl(\cosh(2a_i)-1\bigr)
=\sum_{i=1}^n\sinh^2a_i.
```
The same inequality holds for Bob. Adding the two proves (G20). In the centered Schmidt form every column norm inequality is saturated and there is no displacement contribution. ∎

The photon count is fixed at the input. Supplying local squeezing or local energy later in a protocol does not alter (G20). If mode frequencies are all the same, multiplying $`E`$ by the common photon energy converts this statement to an energy inventory. No assertion is made for a Hamiltonian whose mode energies may approach zero while resources are optimized.

## References

- G. Giedke, J. Eisert, J. I. Cirac and M. B. Plenio, “Entanglement transformations of pure Gaussian states,” *Quantum Information and Computation* **3**, 211–223 (2003). [Primary preprint](https://arxiv.org/abs/quant-ph/0301038).
- L. Banchi, S. L. Braunstein and S. Pirandola, “Quantum fidelity for arbitrary Gaussian states,” *Physical Review Letters* **115**, 260501 (2015). [DOI](https://doi.org/10.1103/PhysRevLett.115.260501), [primary preprint](https://arxiv.org/abs/1507.01941).
- F. Hiai and Y. Lim, “Log-majorizations for the (symplectic) eigenvalues of the Cartan barycenter,” *Linear Algebra and its Applications* **553**, 129–144 (2018). [DOI](https://doi.org/10.1016/j.laa.2018.04.029), [primary preprint](https://arxiv.org/abs/1710.00494).
- H. K. Mishra, “First order sensitivity analysis of symplectic eigenvalues,” *Linear Algebra and its Applications* **604**, 324–345 (2020). [DOI](https://doi.org/10.1016/j.laa.2020.07.003), [primary preprint](https://arxiv.org/abs/2007.10572).

