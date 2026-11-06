# The complete asymptotic photon–mode tradeoff

Fix a pure Gaussian target whose nonzero Gaussian Schmidt squeezings are $`\mathbf r=(r_1,\ldots,r_k)`$, with $`k\ge1`$ and all $`r_j>0`$. The target and $`k`$ remain fixed as the requested infidelity tends to zero. The catalyst is pure Gaussian, operations are those in the [model](model.md), and the fidelity compares the entire output with the desired product of the original catalyst and target.

Throughout, $`n`$ is the number of nonzero catalyst Schmidt pairs and $`E`$ is the initial total mean photon number on both sides. The normalized photon coordinate is $`\varepsilon E`$.

## 1. Target functions and asymptotic budgets

Define

```math
\begin{aligned}
R&=\sum_{j=1}^k r_j,
&
K&=\sum_{j=1}^k(\cosh r_j-1),\\
H&=\sum_{j=1}^k\int_0^{r_j}\sinh^2x\,dx,
&
T&=\sum_{j=1}^k\sinh^2r_j,\\
A_\lambda&=\sum_{j=1}^k\int_0^{r_j}
                 \sqrt{\sinh^2x+\lambda}\,dx,
&&\lambda\ge0,\\
B_\lambda&=\sum_{j=1}^k\int_0^{r_j}
                 \frac{dx}{\sqrt{\sinh^2x+\lambda}},
&&\lambda>0,\\
C_\lambda&=\sum_{j=1}^k\int_0^{r_j}
                 \frac{\sinh^2x\,dx}{\sqrt{\sinh^2x+\lambda}}
=A_\lambda-\lambda B_\lambda,
&&\lambda>0 .
\end{aligned}
\tag{1}
```

In particular, $`A_0=K`$.

A finite pair $`(u,v)\in[0,\infty)^2`$ is an **attainable asymptotic budget** if there are an $`\varepsilon_0>0`$ and a finite catalyst and protocol for every $`0<\varepsilon<\varepsilon_0`$ such that

```math
\begin{aligned}
F_\varepsilon\ge1-\varepsilon,
\qquad
\limsup_{\varepsilon\downarrow0}\varepsilon n_\varepsilon\le u,
\qquad
\limsup_{\varepsilon\downarrow0}\varepsilon E_\varepsilon\le v.
\end{aligned}
\tag{2}
```

The choices may depend on $`\varepsilon`$. Each catalyst has finitely many modes and finite initial photon inventory. Let $`\mathcal B_{\mathbf r}`$ be the set of these budgets. This definition uses upper resource budgets and does not require the two resource sequences to converge.

Define the scalar boundary function

```math
\begin{aligned}
V_{\mathbf r}(u)
=2\sup_{\lambda\ge0}
       \left\{A_\lambda^2-\lambda u\right\}.
\end{aligned}
\tag{3}
```

The factor two converts the scalarization $`E/2+\lambda n`$ into the full-photon coordinate $`v`$.

## 2. Frontier theorem

**Theorem.** The attainable asymptotic budget region is exactly

```math
\begin{aligned}
\boxed{
\mathcal B_{\mathbf r}
=\left\{(u,v)\in[0,\infty)^2:
u\ge R^2,\quad v\ge V_{\mathbf r}(u)\right\}.
}
\end{aligned}
\tag{4}
```

Its boundary has the following complete description.

- At the minimum-mode endpoint,
  $`V_{\mathbf r}(R^2)=2RH`$. There is a family, defined for every requested infidelity, whose resource limits are exactly $`(R^2,2RH)`$.
- For every $`u>R^2`$, there is a unique $`\lambda>0`$ satisfying $`u=A_\lambda B_\lambda`$. At that point,
  $`V_{\mathbf r}(u)=2A_\lambda C_\lambda`$, and another family realizes both resource limits exactly.
- On $`(R^2,\infty)`$, the function $`V_{\mathbf r}`$ is smooth, strictly decreasing, and strictly convex. It is continuous at $`R^2`$.
- The photon infimum is
  $`\inf_{u\ge R^2}V_{\mathbf r}(u)=2K^2`$, approached as $`u\to\infty`$. It is strictly below $`V_{\mathbf r}(u)`$ at every finite $`u`$.

Consequently, the graph of $`V_{\mathbf r}`$ is the entire finite Pareto frontier of the asymptotic budget region.

### 2.1 Necessary support inequalities

The [finite converse](converse.md) proves that every protocol with $`F\ge1-\varepsilon`$ satisfies, for every $`\lambda\ge0`$,

```math
\begin{aligned}
\left[\frac E2+T+\lambda(n+k)\right]q_\varepsilon
&\ge A_\lambda^2,
\\
q_\varepsilon
&=\frac12\mathrm{arcosh}^2\!\left(\frac1{1-\varepsilon}\right),
\\
\frac{q_\varepsilon}{\varepsilon}&\longrightarrow1.
\end{aligned}
\tag{5}
```

Equivalently,

```math
\begin{aligned}
\frac{\varepsilon E}{2}
+\lambda\varepsilon n
\ge
\frac{\varepsilon}{q_\varepsilon}A_\lambda^2
-\varepsilon(T+\lambda k).
\end{aligned}
\tag{6}
```

For a family obeying (2), take $`\varepsilon\downarrow0`$ at a fixed $`\lambda`$. Equation (6) implies

```math
\begin{aligned}
\frac v2+\lambda u\ge A_\lambda^2.
\end{aligned}
\tag{7}
```

This holds for every fixed $`\lambda\ge0`$. Taking their supremum gives
$`v\ge V_{\mathbf r}(u)`$. The parameter limit $`\lambda\to\infty`$ is taken after the error limit; it is not interchanged with the finite-error correction in (6).

### 2.2 Strict monotonicity of the contact curve

For $`\lambda>0`$, put

```math
\begin{aligned}
D_\lambda
=\sum_{j=1}^k\int_0^{r_j}
         \frac{dx}{(\sinh^2x+\lambda)^{3/2}},
\qquad
u_\lambda=A_\lambda B_\lambda,
\qquad
v_\lambda=2A_\lambda C_\lambda.
\end{aligned}
\tag{8}
```

On any compact positive parameter interval, the integrands and all their parameter derivatives are bounded. Differentiation under the integrals therefore gives

```math
\begin{aligned}
A_\lambda'=\frac{B_\lambda}{2},
\qquad
B_\lambda'=-\frac{D_\lambda}{2},
\qquad
u_\lambda'
=\frac{B_\lambda^2-A_\lambda D_\lambda}{2}.
\end{aligned}
\tag{9}
```

View the integrals as a single integral over the disjoint union of the intervals $`[0,r_j]`$, with Lebesgue measure. Let
$`f(x)=\sqrt{\sinh^2x+\lambda}`$. Cauchy–Schwarz applied to
$`f^{1/2}`$ and $`f^{-3/2}`$ yields

```math
B_\lambda^2
=\left(\int f^{-1}\right)^2
\le\left(\int f\right)\left(\int f^{-3}\right)
=A_\lambda D_\lambda.
```

Equality would require $`f^2`$ to be constant almost everywhere. It is strictly increasing on each interval of positive length, so equality is impossible. Hence

```math
\begin{aligned}
u_\lambda'<0.
\end{aligned}
\tag{10}
```

Since $`v_\lambda=2(A_\lambda^2-\lambda u_\lambda)`$, equations (9)–(10) give

```math
\begin{aligned}
v_\lambda'=-2\lambda u_\lambda'>0.
\end{aligned}
\tag{11}
```

Thus increasing $`\lambda`$ strictly reduces the normalized mode cost and strictly increases the normalized photon cost.

### 2.3 Both parameter endpoints

As $`\lambda\to\infty`$, bounded convergence on the fixed target intervals gives

```math
\frac{A_\lambda}{\sqrt\lambda}\longrightarrow R,
\qquad
\sqrt\lambda B_\lambda\longrightarrow R,
\qquad
\sqrt\lambda C_\lambda\longrightarrow H.
```

Therefore

```math
\begin{aligned}
u_\lambda\longrightarrow R^2,
\qquad
v_\lambda\longrightarrow2RH.
\end{aligned}
\tag{12}
```

For every finite $`\lambda>0`$, Cauchy–Schwarz also gives
$`A_\lambda B_\lambda>R^2`$, with the same strictness condition.

As $`\lambda\downarrow0`$, dominated convergence gives

```math
A_\lambda\longrightarrow K,
\qquad
C_\lambda\longrightarrow K.
```

For $`L_*=\cosh(\max_jr_j)`$, the inequality
$`\sinh x\le L_*x`$ on all target intervals gives

```math
B_\lambda
\ge\frac1{L_*}
\sum_{j=1}^k
\mathrm{arsinh}\,\!\left(\frac{L_*r_j}{\sqrt\lambda}\right)
\longrightarrow\infty.
```

Consequently,

```math
\begin{aligned}
u_\lambda\longrightarrow\infty,
\qquad
v_\lambda\longrightarrow2K^2
\quad\text{as }\lambda\downarrow0.
\end{aligned}
\tag{13}
```

Equations (10), (12), and (13) show that $`\lambda\mapsto u_\lambda`$ is a continuous, strictly decreasing bijection from $`(0,\infty)`$ onto $`(R^2,\infty)`$.

### 2.4 Evaluation of the support supremum

For $`u>R^2`$, differentiate the expression inside (3):

```math
\begin{aligned}
\frac{d}{d\lambda}\bigl(A_\lambda^2-\lambda u\bigr)
=u_\lambda-u.
\end{aligned}
\tag{14}
```

This derivative is positive before the unique point $`u_\lambda=u`$ and negative after it. That point is the global maximizer. It follows that

```math
\begin{aligned}
V_{\mathbf r}(u)
=2(A_\lambda^2-\lambda A_\lambda B_\lambda)
=2A_\lambda C_\lambda
\quad\text{when }u=A_\lambda B_\lambda.
\end{aligned}
\tag{15}
```

At $`u=R^2`$, Cauchy–Schwarz gives the upper bound

```math
\begin{aligned}
A_\lambda^2
\le R\sum_j\int_0^{r_j}(\sinh^2x+\lambda)\,dx
=\lambda R^2+RH.
\end{aligned}
\tag{16}
```

This upper bound is approached as $`\lambda\to\infty`$. To verify the constant directly, rationalize the difference:

```math
\sqrt\lambda\,(A_\lambda-\sqrt\lambda R)
=
\sum_j\int_0^{r_j}
\frac{\sinh^2x}
     {\sqrt{1+\sinh^2x/\lambda}+1}\,dx
\longrightarrow\frac H2.
```

Together with
$`(A_\lambda+\sqrt\lambda R)/\sqrt\lambda\to2R`$, this proves
$`A_\lambda^2-\lambda R^2\to RH`$ and hence
$`V_{\mathbf r}(R^2)=2RH`$.

If $`u\lt R^2`$, then $`A_\lambda\ge\sqrt\lambda R`$ implies
$`A_\lambda^2-\lambda u\ge\lambda(R^2-u)`$.
The supremum in (3) is infinite. This excludes all finite budgets with $`u\lt R^2`$.

The inverse function $`\lambda(u)`$ is smooth because $`u_\lambda'<0`$. Differentiating (15) along the curve gives

```math
\begin{aligned}
V_{\mathbf r}'(u)=-2\lambda(u),
\qquad
V_{\mathbf r}''(u)=-\frac{2}{u_\lambda'}>0.
\end{aligned}
\tag{17}
```

The endpoint limits are

```math
\lim_{u\downarrow R^2}V_{\mathbf r}(u)=2RH,
\qquad
\lim_{u\to\infty}V_{\mathbf r}(u)=2K^2,
```

and

```math
\begin{aligned}
\lim_{u\downarrow R^2}V_{\mathbf r}'(u)=-\infty,
\qquad
\lim_{u\to\infty}V_{\mathbf r}'(u)=0.
\end{aligned}
\tag{18}
```

Strict increase of $`v_\lambda`$ with $`\lambda`$, together with (13), proves
$`V_{\mathbf r}(u)>2K^2`$ for every finite $`u`$.

### 2.5 Achievability of every boundary point

For any $`u>R^2`$, choose its unique positive parameter $`\lambda(u)`$.
The graded ladders in [constructions, Section 3](constructions.md#3-graded-ladders-for-a-positive-tradeoff-parameter) are finite for every requested $`0<\varepsilon<1`$, satisfy $`F_\varepsilon\ge1-\varepsilon`$, and obey

```math
\varepsilon n_\varepsilon\longrightarrow u,
\qquad
\varepsilon E_\varepsilon\longrightarrow
2A_{\lambda(u)}C_{\lambda(u)}
=V_{\mathbf r}(u).
```

The endpoint $`u=R^2`$ is attained by the uniform ladders in
[constructions, Section 4](constructions.md#4-the-minimum-mode-endpoint), which give the limits $`(R^2,2RH)`$.

For a larger photon budget $`v\ge V_{\mathbf r}(u)`$, the same boundary construction meets both upper budgets in (2). This proves sufficiency in (4). Necessity was established in Section 2.1, completing the theorem.

Every point on the graph is Pareto optimal: moving to a smaller mode coordinate strictly raises the necessary photon coordinate, and the mode endpoint has the smallest feasible mode coordinate. Every point strictly above the graph is dominated by the point on the graph at the same mode coordinate.

## 3. Hard finite budgets and closure

The theorem concerns asymptotic upper budgets. To make its connection to exact finite caps explicit, let $`\mathcal H_{\mathbf r}`$ consist of pairs for which, for every sufficiently small requested $`\varepsilon`$, there is a protocol satisfying

```math
\begin{aligned}
F_\varepsilon\ge1-\varepsilon,
\qquad
n_\varepsilon\le\frac u\varepsilon,
\qquad
E_\varepsilon\le\frac v\varepsilon.
\end{aligned}
\tag{19}
```

Then

```math
\begin{aligned}
\mathcal H_{\mathbf r}\subseteq\mathcal B_{\mathbf r},
\qquad
\overline{\mathcal H_{\mathbf r}}=\mathcal B_{\mathbf r},
\end{aligned}
\tag{20}
```

where the closure is in the finite $`(u,v)`$ plane.

For $`u>R^2`$ and $`v>V_{\mathbf r}(u)`$, continuity of the boundary lets one choose
$`u_0\in(R^2,u)`$ with $`V_{\mathbf r}(u_0)\lt v`$.
The construction at $`u_0`$ has strict slack in both limiting resources, so it obeys (19) for all sufficiently small $`\varepsilon`$.

At $`u=R^2`$ and $`v>2RH`$, the uniform construction has the exact bound

```math
n_\varepsilon<
\frac{R^2}{-\log(1-\varepsilon)}
<
\frac{R^2}{\varepsilon},
```

and its photon limit is $`2RH`$. It therefore also meets (19) eventually.

Every point of $`\mathcal B_{\mathbf r}`$ is a limit of points with strict slack.
Conversely, $`\mathcal B_{\mathbf r}`$ is closed by (4) and the continuity of its boundary, and contains $`\mathcal H_{\mathbf r}`$. This proves (20).

In particular, equality at the minimum normalized mode coefficient is attained in (2), including the photon value $`2RH`$. The theorem does not identify which boundary points satisfy both exact finite caps (19) without any slack, nor the exact finite-error optimum over Gaussian protocols.

## 4. The two individual resource minima

Let $`n_{\min}(\varepsilon)`$ be the smallest possible catalyst Schmidt-pair count among all finite catalysts and allowed protocols with fidelity at least $`1-\varepsilon`$, with no photon budget. The feasible integer counts are nonempty, so this minimum exists. Let $`E_{\rm opt}(\varepsilon)`$ be the infimum of the initial photon inventory with the same fidelity condition and any finite mode count.

The individual sharp asymptotic laws are

```math
\begin{aligned}
\boxed{
\lim_{\varepsilon\downarrow0}
\varepsilon n_{\min}(\varepsilon)=R^2,
\qquad
\lim_{\varepsilon\downarrow0}
\varepsilon E_{\rm opt}(\varepsilon)=2K^2.
}
\end{aligned}
\tag{21}
```

For the mode law, the finite converse and the uniform construction give

```math
\begin{aligned}
\max\left\{0,\left\lceil\frac{R^2}{q_\varepsilon}-k\right\rceil\right\}
\le n_{\min}(\varepsilon)
\le
\sum_{j=1}^k
\left\lceil\frac{r_jR}{-\log(1-\varepsilon)}\right\rceil-k.
\end{aligned}
\tag{22}
```

For photons, the finite converse at $`\lambda=0`$ gives

```math
E_{\rm opt}(\varepsilon)
\ge\frac{2K^2}{q_\varepsilon}-2T.
```

The hyperbolic-flow ladders in
[constructions, Section 5](constructions.md#5-the-minimum-photon-limit) meet every requested error and have $`\varepsilon E_\varepsilon\to2K^2`$.
These lower and upper bounds prove (21).

The two optima correspond to different families. At the minimum mode coefficient, (7) implies

```math
\begin{aligned}
\varepsilon n_\varepsilon\longrightarrow R^2
\quad\Longrightarrow\quad
\liminf_{\varepsilon\downarrow0}\varepsilon E_\varepsilon\ge2RH,
\end{aligned}
\tag{23}
```

and the uniform construction attains equality. To obtain (23), fix $`\lambda`$, apply (6), pass to the error limit, and then let $`\lambda\to\infty`$.

Cauchy–Schwarz on the target intervals gives the strict inequality

```math
\begin{aligned}
K^2=
\left(\sum_j\int_0^{r_j}\sinh x\,dx\right)^2
<
\left(\sum_jr_j\right)
\left(\sum_j\int_0^{r_j}\sinh^2x\,dx\right)
=RH.
\end{aligned}
\tag{24}
```

The integrand $`\sinh x`$ is not almost everywhere constant, which gives strictness. Thus a mode-optimal family has a strictly larger optimal photon coefficient than the photon-only infimum.

Conversely,

```math
\begin{aligned}
\varepsilon E_\varepsilon\longrightarrow2K^2
\quad\Longrightarrow\quad
\varepsilon n_\varepsilon\longrightarrow\infty.
\end{aligned}
\tag{25}
```

If (25) failed, some sequence of errors tending to zero would have bounded
$`\varepsilon n_\varepsilon\le M`$ while $`\varepsilon E_\varepsilon\to2K^2`$.
Applying (6) along that sequence would imply
$`2K^2\ge V_{\mathbf r}(M)`$, contrary to the theorem. If $`M\lt R^2`$, the mode converse already supplies the contradiction.

The mode minimum in (21) is an exact finite integer optimization whose leading coefficient is known. The frontier endpoint specifies its optimal leading photon coefficient when the mode coefficient tends to that minimum; it does not assert that the uniform ladder attains the smallest integer $`n`$ at every nonzero error.

## 5. Any divergent mode overhead suffices for the photon coefficient

The explicit photon-optimal family uses
$`\varepsilon n_\varepsilon/\log(1/\varepsilon)\to kK`$.
That logarithm is not a necessary overhead.

More precisely, let $`w:(0,\varepsilon_0)\to(0,\infty)`$ be any function with
$`w(\varepsilon)\to\infty`$ as $`\varepsilon\downarrow0`$.
There is a family with

```math
\begin{aligned}
F_\varepsilon\ge1-\varepsilon,
\qquad
\varepsilon n_\varepsilon\le w(\varepsilon)
\quad\text{for all sufficiently small }\varepsilon,
\qquad
\varepsilon E_\varepsilon\longrightarrow2K^2.
\end{aligned}
\tag{26}
```

**Proof.** Choose any sequence $`\lambda_m\downarrow0`$. Its contact resources satisfy
$`u_m=A_{\lambda_m}B_{\lambda_m}\to\infty`$ and
$`v_m=2A_{\lambda_m}C_{\lambda_m}\to2K^2`$.

For each fixed $`m`$, the construction at $`\lambda_m`$ is defined for every requested error and has normalized resource limits $`(u_m,v_m)`$.
Choose a strictly decreasing sequence $`\eta_m\downarrow0`$ such that, whenever
$`0<\varepsilon\le\eta_m`$, this construction obeys

```math
|\varepsilon n_\varepsilon-u_m|\le\frac1m,
\qquad
|\varepsilon E_\varepsilon-v_m|\le\frac1m,
\qquad
w(\varepsilon)\ge u_m+1.
```

Such thresholds exist by the fixed-parameter limits and the defining limit of
$`w`$. For $`0<\varepsilon\le\eta_1`$, take the construction at
$`\lambda_{m(\varepsilon)}`$, where
$`m(\varepsilon)=\max\{m:\varepsilon\le\eta_m\}`$.
This index is finite for every positive error and tends to infinity as the error vanishes. The three displayed inequalities imply (26).

This argument uses successively smaller error thresholds for fixed positive parameters. It requires no unproved uniform limit as $`\lambda\downarrow0`$.

## 6. Identical target pairs and the single-pair case

For $`k`$ identical target pairs of squeezing $`r`$, all three integrals in (1) are $`k`$ times their single-pair values. Consequently,

```math
\begin{aligned}
\boxed{
V_{(r,\ldots,r)}(u)
=k^2 V_{(r)}(u/k^2),
\qquad
u\ge k^2r^2.
}
\end{aligned}
\tag{27}
```

In particular,

```math
\begin{aligned}
\lim_{\varepsilon\downarrow0}\varepsilon n_{\min}(\varepsilon)
&=k^2r^2,\\
\lim_{\varepsilon\downarrow0}\varepsilon E_{\rm opt}(\varepsilon)
&=2k^2(\cosh r-1)^2,\\
V_{(r,\ldots,r)}(k^2r^2)
&=2k^2r\left(\frac{\sinh(2r)}4-\frac r2\right).
\end{aligned}
\tag{28}
```

The factor $`k^2`$ is for a joint infidelity budget on the complete returned catalyst and all target pairs. All limits in this account keep $`k`$ fixed.

For a single target pair, the mode-optimal endpoint and the photon infimum are therefore

```math
\begin{aligned}
\left(r^2,\;\frac r2\sinh(2r)-r^2\right),
\qquad
\inf_{u\ge r^2}V_{(r)}(u)=2(\cosh r-1)^2.
\end{aligned}
\tag{29}
```

These are statements about initial catalyst inventory under the pure-catalyst model. The passive constructions conserve actual photons during the permutations; the asymptotic resource theorem does not assign a work cost to preparing the catalyst or to general local Gaussian controls.

