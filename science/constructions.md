# Passive constructions and finite error bounds

The target is fixed throughout. Its nonzero Gaussian Schmidt squeezings are $`\mathbf r=(r_1,\ldots,r_k)`$, with $`k\ge1`$ and $`r_j>0`$, in the standard convention

```math
|r\rangle=\mathrm{sech}\,r\sum_{m=0}^{\infty}(\tanh r)^m|m,m\rangle .
```

The resource $`n`$ counts nonzero catalyst Schmidt pairs, and $`E`$ is the initial mean photon number of the catalyst, summed over both parties. The error is the infidelity $`1-F`$, where $`F`$ is the squared overlap with the entire desired product of catalyst and target. The [model](model.md) gives the operational conventions; the [tradeoff theorem](tradeoff.md) identifies the resource boundary.

Write

```math
\begin{aligned}
R&=\sum_{j=1}^k r_j,
&
K&=\sum_{j=1}^k(\cosh r_j-1),\\
H&=\sum_{j=1}^k\int_0^{r_j}\sinh^2x\,dx
  =\sum_{j=1}^k\left(\frac{\sinh(2r_j)}4-\frac{r_j}2\right),
&
T&=\sum_{j=1}^k\sinh^2r_j,\\
r_*&=\max_j r_j,
&
L_*&=\cosh r_* .
\end{aligned}
```

Here $`T`$ is the target's photon inventory on one side in Gaussian Schmidt form.

## 1. Exact cyclic protocol

For each target pair choose a finite decreasing ladder

```math
r_j=x_{j,0}>x_{j,1}>\cdots>x_{j,n_j}>x_{j,n_j+1}=0.
```

A ladder with $`n_j=0`$ is permitted. Prepare the pure catalyst

```math
|C\rangle=
\bigotimes_{j=1}^k\bigotimes_{i=1}^{n_j}|x_{j,i}\rangle,
\qquad
n=\sum_{j=1}^k n_j.
```

On each side, cyclically permute the local modes in each target-and-ladder block. The first catalyst pair moves into the target slot, the remaining catalyst pairs move one slot forward, and the vacuum target pair moves into the last catalyst slot. Both parties perform the same permutation. The output is a product of TMSVs, with no correlation between the retained catalyst and target.

For any nonnegative $`a,b`$, summing the geometric Schmidt series gives

```math
\langle a|b\rangle
=\frac{\mathrm{sech}\,a\,\mathrm{sech}\,b}
       {1-\tanh a\tanh b}
=\mathrm{sech}(a-b).
```

Consequently, with $`\Delta_{j,i}=x_{j,i}-x_{j,i+1}`$,

```math
\boxed{
\begin{aligned}
F&=\prod_{j=1}^k\prod_{i=0}^{n_j}
       \mathrm{sech}^2\,\Delta_{j,i},\\
E&=2\sum_{j=1}^k\sum_{i=1}^{n_j}\sinh^2x_{j,i}.
\end{aligned}}
\tag{1}
```

There is one deterministic branch. The permutations are passive Gaussian unitaries and conserve the actual total photon number exactly. A target in another local Gaussian frame is obtained by applying its specified local Gaussian unitaries to the target slots after the permutations. This preserves the joint fidelity and the initial catalyst inventory; those final frame changes may require active controls.

## 2. Converting a mesh bound into a prescribed error

Define the squared-gap sum, largest gap, and logarithmic loss by

```math
S=\sum_{j,i}\Delta_{j,i}^2,
\qquad
d_{\max}=\max_{j,i}\Delta_{j,i},
\qquad
\mathcal L=-\log F.
```

For $`t\ge0`$, the inequalities $`\tanh t\le t`$ and
$`(\tanh t)'=1-\tanh^2t\ge1-t^2`$ imply

```math
0\le t^2-2\log\cosh t\le\frac{t^4}{6}.
```

Indeed, integrate the derivative inequality once to obtain
$`\tanh t\ge t-t^3/3`$, and then integrate again. Summing over the gaps yields

```math
\begin{aligned}
S-\frac{d_{\max}^2S}{6}\le\mathcal L\le S.
\end{aligned}
\tag{2}
```

Given any requested $`0\lt \varepsilon\lt 1`$, put

```math
\ell_\varepsilon=-\log(1-\varepsilon).
```

The exact condition $`S\le\ell_\varepsilon`$ guarantees $`F\ge1-\varepsilon`$. The elementary integral formula for $`\ell_\varepsilon`$ also gives

```math
\begin{aligned}
\varepsilon\le\ell_\varepsilon
\le\frac{\varepsilon}{1-\varepsilon},
\qquad
\frac{\ell_\varepsilon}{\varepsilon}\longrightarrow1.
\end{aligned}
\tag{3}
```

All constructions below meet the requested error for every $`\varepsilon`$, rather than only along a selected sequence of errors.

## 3. Graded ladders for a positive tradeoff parameter

For $`\lambda>0`$, define

```math
\begin{aligned}
f_\lambda(x)&=\sqrt{\sinh^2x+\lambda},\\
A_\lambda&=\sum_{j=1}^k\int_0^{r_j}f_\lambda(x)\,dx,\\
B_\lambda&=\sum_{j=1}^k\int_0^{r_j}\frac{dx}{f_\lambda(x)},\\
C_\lambda&=\sum_{j=1}^k\int_0^{r_j}
                  \frac{\sinh^2x}{f_\lambda(x)}\,dx
           =A_\lambda-\lambda B_\lambda,\\
M_\lambda&=\sqrt{\sinh^2r_*+\lambda}.
\end{aligned}
\tag{4}
```

Choose a common step parameter $`h>0`$ for all target pairs. Starting from $`x_{j,0}=r_j`$, iterate

```math
\begin{aligned}
x_{j,i+1}=\max\{0,\;x_{j,i}-h f_\lambda(x_{j,i})\}
\end{aligned}
\tag{5}
```

until zero is first reached. The positive interior points are the catalyst squeezings. Every full step removes at least $`h\sqrt\lambda`$, so every ladder is finite. All its gaps except the last obey
$`\Delta_{j,i}=h f_\lambda(x_{j,i})`$; the last obeys
$`0\lt \Delta_{j,n_j}\le h f_\lambda(x_{j,n_j})`$.

### 3.1 Explicit estimates

For $`0\lt h\lt 2/L_*`$, the construction satisfies

```math
\begin{aligned}
\boxed{
hA_\lambda-\frac{h^2}{4}(T+k\lambda)
\le S
\le\frac{hA_\lambda}{1-L_*h/2}.
}
\end{aligned}
\tag{6}
```

It also satisfies

```math
\begin{aligned}
\boxed{
0\le B_\lambda-hn
\le\frac{L_*}{2\lambda}S
   +\frac{k h M_\lambda}{\sqrt\lambda},
}
\end{aligned}
\tag{7}
```

and

```math
\begin{aligned}
\boxed{
C_\lambda-hT
\le \frac{hE}{2}
\le C_\lambda+L_*S,
\qquad
d_{\max}\le hM_\lambda .
}
\end{aligned}
\tag{8}
```

These bounds retain their constants at finite $`h`$.

**Proof of (6).** On $`[0,r_*]`$,

```math
0\le f_\lambda'(x)
=\frac{\sinh x\cosh x}{\sqrt{\sinh^2x+\lambda}}
\le L_*.
```

The upper-endpoint sum $`U=\sum_{j,i} f_\lambda(x_{j,i})\Delta_{j,i}`$ therefore obeys

```math
A_\lambda\le U\le A_\lambda+\frac{L_*}{2}S.
```

For the full steps, the contribution to $`S`$ is exactly $`h`$ times the contribution to $`U`$. For a last step with upper endpoint $`x`$ and gap $`d`$, the discrepancy is

```math
0\le h f_\lambda(x)d-d^2
\le\frac{h^2 f_\lambda(x)^2}{4}
\le\frac{h^2(\sinh^2r_j+\lambda)}4.
```

Summing the last-step discrepancies gives the lower bound in (6). The upper bound follows from
$`S\le hU\le hA_\lambda+(hL_*/2)S`$.

**Proof of (7).** The function $`1/f_\lambda`$ is decreasing, with derivative in absolute value at most $`L_*/\lambda`$. Its integral on a full gap is at least
$`\Delta_{j,i}/f_\lambda(x_{j,i})=h`$ and exceeds that lower sum by at most
$`L_*\Delta_{j,i}^2/(2\lambda)`$. The integral over a last gap is at most
$`\Delta_{j,n_j}/\sqrt\lambda\le hM_\lambda/\sqrt\lambda`$.
There are exactly $`n`$ full gaps before the last gaps, giving (7).

**Proof of (8).** Put
$`w_\lambda(x)=\sinh^2x/f_\lambda(x)=f_\lambda(x)-\lambda/f_\lambda(x)`$.
It is increasing, and

```math
0\le w_\lambda'(x)
=f_\lambda'(x)\left(1+\frac{\lambda}{f_\lambda(x)^2}\right)
\le2L_*.
```

Hence its upper-endpoint sum $`U_w`$ lies between $`C_\lambda`$ and
$`C_\lambda+L_*S`$. In block $`j`$, write $`x=x_{j,n_j}`$ and
$`d=\Delta_{j,n_j}`$. Directly separating the full and final gaps gives

```math
\frac{hE_j}{2}
=U_{w,j}-h\sinh^2r_j
+\sinh^2x\left(h-\frac{d}{f_\lambda(x)}\right).
```

The last term lies between zero and $`h\sinh^2r_j`$. This proves the two energy bounds after summing the blocks. The gap bound follows directly from (5).

### 3.2 Choice for every requested infidelity

For a requested $`0\lt \varepsilon\lt 1`$, set

```math
\begin{aligned}
\boxed{
h_\varepsilon(\lambda)
=\frac{\ell_\varepsilon}
       {A_\lambda+(L_*/2)\ell_\varepsilon}.
}
\end{aligned}
\tag{9}
```

This lies below $`2/L_*`$, and the upper bound in (6) is exactly
$`\ell_\varepsilon`$. Thus the finite protocol satisfies
$`F_\varepsilon\ge1-\varepsilon`$.

At every fixed $`\lambda>0`$, equations (6)–(8) imply

```math
hn\longrightarrow B_\lambda,\qquad
\frac{hE}{2}\longrightarrow C_\lambda,\qquad
\frac{S}{h}\longrightarrow A_\lambda.
```

Equation (2) and $`d_{\max}\le hM_\lambda`$ give
$`\mathcal L/h\to A_\lambda`$. Since
$`0\le\mathcal L-(1-e^{-\mathcal L})\le\mathcal L^2/2`$, the actual infidelity divided by $`h`$ has the same limit. Finally, (3) and (9) give
$`\varepsilon/h\to A_\lambda`$. Therefore

```math
\boxed{
\begin{aligned}
\varepsilon n_\varepsilon&\longrightarrow A_\lambda B_\lambda,\\
\varepsilon E_\varepsilon&\longrightarrow 2A_\lambda C_\lambda,\\
\frac{1-F_\varepsilon}{\varepsilon}&\longrightarrow1.
\end{aligned}}
\tag{10}
```

The common step parameter is essential to the joint normalization. Equation (1) evaluates the global fidelity, whose logarithmic loss is the sum over all $`k`$ blocks.

### 3.3 Uniformity on finite positive parameter intervals

Let $`0\lt a\le\lambda\le b\lt \infty`$ and $`0\lt h\le1/L_*`$. Equations (6)–(8) imply the following explicit common bounds:

```math
\begin{aligned}
-\frac{T+kb}{4}h^2
&\le S-hA_\lambda
\le L_*A_bh^2,\\
0\le B_\lambda-hn
&\le h\left(\frac{L_*A_b}{a}
+\frac{kM_b}{\sqrt a}\right),\\
\left|\frac{hE}{2}-C_\lambda\right|
&\le h\max\{T,2L_*A_b\},\\
0\le S-\mathcal L
&\le\frac{M_b^2A_b}{3}h^3.
\end{aligned}
\tag{11}
```

For the requested-error choice (9),

```math
\begin{aligned}
\left|\frac{\varepsilon}{h_\varepsilon(\lambda)}
-A_\lambda\right|
\le\left(A_b+\frac{L_*}{2}\right)\varepsilon,
\qquad
h_\varepsilon(\lambda)
\le\frac{\varepsilon}{(1-\varepsilon)A_a}.
\end{aligned}
\tag{12}
```

The functions $`A_\lambda,B_\lambda,C_\lambda`$ are bounded on $`[a,b]`$.
For $`0\lt \varepsilon\le\min\{1/2,A_a/(2L_*)\}`$, equation (12) ensures $`h_\varepsilon(\lambda)\le1/L_*`$, so all bounds in (11) apply simultaneously. Equations (11)–(12) therefore prove that both resource limits in (10) are uniform on that interval. No interchange with $`\lambda=0`$ or $`\lambda=\infty`$ is used.

## 4. The minimum-mode endpoint

Uniform ladders attain the endpoint of the tradeoff curve with the smallest normalized mode count. For every $`0\lt \varepsilon\lt 1`$, put

```math
\begin{aligned}
\delta=\frac{\ell_\varepsilon}{R},
\qquad
m_j=\left\lceil\frac{r_j}{\delta}\right\rceil,
\qquad
x_{j,i}=r_j\left(1-\frac{i}{m_j}\right),
\quad 0\le i\le m_j.
\end{aligned}
\tag{13}
```

The block has $`n_j=m_j-1`$ catalyst pairs and gap size
$`\delta_j=r_j/m_j\le\delta`$. Thus

```math
\begin{aligned}
S=\sum_j\frac{r_j^2}{m_j}
\le\delta R=\ell_\varepsilon,
\qquad
F=\prod_j\mathrm{sech}^{\,2m_j}(r_j/m_j)
\ge1-\varepsilon.
\end{aligned}
\tag{14}
```

The integer rounding obeys

```math
\begin{aligned}
\frac{R^2}{\ell_\varepsilon}-k
\le n
\lt \frac{R^2}{\ell_\varepsilon}
\lt \frac{R^2}{\varepsilon}.
\end{aligned}
\tag{15}
```

For $`H_j=\int_0^{r_j}\sinh^2x\,dx`$ and
$`J=\sum_j H_j/r_j`$, the left and right Riemann sums for the increasing function $`\sinh^2x`$ give

```math
\begin{aligned}
\frac{H}{\delta}-T
\le\frac E2
\le\frac{H}{\delta}+J.
\end{aligned}
\tag{16}
```

To see the upper bound, use
$`1/\delta_j=m_j/r_j\lt 1/\delta+1/r_j`$; for the lower bound, use
$`1/\delta_j\ge1/\delta`$.
Combining (3), (15), and (16) proves

```math
\begin{aligned}
\boxed{
\varepsilon n_\varepsilon\longrightarrow R^2,
\qquad
\varepsilon E_\varepsilon\longrightarrow2RH.
}
\end{aligned}
\tag{17}
```

In particular, the minimum normalized mode coefficient is attained, including equality at the endpoint. Equation (15) also supplies an exact finite mode cap for this construction. The energy coefficient in (17) is the value at this endpoint of the asymptotic frontier.

## 5. The minimum-photon limit

A different family attains the smallest photon coefficient. For a common $`h>0`$, let

```math
\begin{aligned}
z_j(t)=2\mathrm{artanh}
\left[\tanh(r_j/2)e^{-t}\right],
\qquad
\frac{dz_j}{dt}=-\sinh z_j.
\end{aligned}
\tag{18}
```

Set $`x_{j,i}=z_j(ih)`$. Stop at the first nonnegative integer $`n_j`$ with
$`x_{j,n_j}\le h`$, and append the final point zero. This gives a finite ladder; if $`r_j\le h`$, it has no catalyst pairs.

The exact bounds are

```math
\begin{aligned}
\boxed{
\frac{h[K-k(\cosh h-1)]}{1+L_*h/2}
\le S
\le hK+kh^2,
}
\end{aligned}
\tag{19}
```

and

```math
\begin{aligned}
\boxed{
K-k(\cosh h-1)-hT
\le\frac{hE}{2}
\le K.
}
\end{aligned}
\tag{20}
```

**Proof.** On a full time interval of length $`h`$, Cauchy–Schwarz gives

```math
(x_{j,i-1}-x_{j,i})^2
\le h\int_{(i-1)h}^{ih}\sinh^2z_j(t)\,dt.
```

The full integral is $`\int_0^{n_jh}\sinh^2z_j(t)\,dt=\cosh r_j-\cosh x_{j,n_j}`$.
The final gap is at most $`h`$. Summing proves the upper bound in (19).

For the lower bound, every full gap $`d=x_{j,i-1}-x_{j,i}`$ obeys
$`d\ge h\sinh x_{j,i}`$. Since the derivative of $`\sinh x`$ is at most $`L_*`$ on these ladders, its lower-endpoint Riemann sum differs from its integral by at most $`L_*S_{\rm full}/2`$. Consequently,

```math
S_{\rm full}
\ge h\left[K-\sum_j(\cosh x_{j,n_j}-1)
-\frac{L_*}{2}S_{\rm full}\right].
```

Use $`x_{j,n_j}\le h`$ and $`S\ge S_{\rm full}`$ to obtain the lower bound in (19).

For (20), the function $`\sinh^2z_j(t)`$ is decreasing. Its right Riemann sum is $`hE_j/2`$; its integral exceeds that sum by at most
$`h[\sinh^2r_j-\sinh^2x_{j,n_j}]`$.
Substitute the displayed integral and sum over $`j`$.

For every requested $`0\lt \varepsilon\lt 1`$, choose the positive solution of
$`Kh+kh^2=\ell_\varepsilon`$:

```math
\begin{aligned}
\boxed{
h_\varepsilon
=\frac{2\ell_\varepsilon}
       {K+\sqrt{K^2+4k\ell_\varepsilon}}.
}
\end{aligned}
\tag{21}
```

Then (19) gives $`F_\varepsilon\ge1-\varepsilon`$. Equation (20) supplies the finite energy bound

```math
\begin{aligned}
E_\varepsilon
\le
\frac{K\left(K+\sqrt{K^2+4k\ell_\varepsilon}\right)}
     {\ell_\varepsilon}.
\end{aligned}
\tag{22}
```

As $`\varepsilon\downarrow0`$, equations (3), (19)–(21) give
$`\varepsilon/h\to K`$, $`S/h\to K`$, and $`hE/2\to K`$.
Every full gap is at most $`h\sinh r_*`$, and every final gap is at most $`h`$.
Equation (2) therefore also gives $`(1-F_\varepsilon)/\varepsilon\to1`$.
In particular,

```math
\begin{aligned}
\boxed{
\varepsilon E_\varepsilon\longrightarrow2K^2.
}
\end{aligned}
\tag{23}
```

The mode count can be read directly from (18). For $`h\lt \min_jr_j`$, define

```math
\tau_j(h)
=\log\frac{\tanh(r_j/2)}{\tanh(h/2)}.
```

Then $`n_j=\lceil\tau_j(h)/h\rceil`$ and

```math
\begin{aligned}
\sum_j\tau_j(h)\le hn
\lt \sum_j\tau_j(h)+kh.
\end{aligned}
\tag{24}
```

Because $`\tanh(h/2)/(h/2)\to1`$, the sum in (24), divided by
$`\log(1/h)`$, tends to $`k`$. Thus this explicit family has

```math
\begin{aligned}
\boxed{
\frac{\varepsilon n_\varepsilon}{\log(1/\varepsilon)}
\longrightarrow kK,
\qquad
\varepsilon n_\varepsilon\longrightarrow\infty.
}
\end{aligned}
\tag{25}
```

The logarithm describes this particular construction. The tradeoff theorem proves that a divergent normalized mode count is necessary for the optimal photon coefficient, and that any prescribed divergent overhead can be accommodated by a slower diagonal choice of positive-parameter ladders.
