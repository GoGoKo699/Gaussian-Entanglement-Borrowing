# Reproducing the scientific checks

The written proofs establish the Gaussian-LOCC converse and the asymptotic frontier. These numerical calculations check constants, formulas, finite constructions and their normalization. They use no downloaded data.

## Environment and commands

The checked environment was Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8. The library versions are pinned in [requirements.txt](requirements.txt).

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_checks.py
```

Run Python without `-O`: assertions implement the scientific inequalities, and the runner rejects optimized mode. Each script exits unsuccessfully if a checked inequality fails. A successful full run ends with:

```text
PASS: all finite scientific checks completed.
```

## Scope and stored outputs

| Script | What it checks | Output |
|---|---|---|
| [check_geometry.py](check_geometry.py) | 360 positive-matrix pairs and 240 pure Gaussian pairs challenge the dimension-free symplectic metric and state-fidelity constants; aligned and photon-endpoint examples record approach to equality | [geometry_results.json](geometry_results.json) |
| [check_ladders.py](check_ladders.py) | 45 graded-ladder cases and 300 random ladders check squared-gap fidelity and finite weighted resource bounds | [ladder_results.json](ladder_results.json) |
| [check_tradeoff.py](check_tradeoff.py) | 99 contacts for three fixed target lists check strict parameter ordering and supporting inequalities; 27 multimode ladders check convergence; three independent covariance determinants check the pair-overlap formula | [tradeoff_results.json](tradeoff_results.json) |
| [check_prescribed_errors.py](check_prescribed_errors.py) | 76 cases for each of three requested-error constructions, including empty catalyst blocks, check the explicit mesh, mode and photon estimates; 108 contact comparisons check the support bounds | [prescribed_error_results.json](prescribed_error_results.json) |

The positive-matrix, pure-state and prescribed-error comparisons use seed `20261106`; the random ladder test uses seed `773`. The remaining sweeps specify their target squeezings, parameters and step sizes in source. Numerical integration uses explicit absolute and relative tolerances.

The stored geometry run has maximum tested left/right bound ratios of approximately `0.927107` for general positive matrices and `0.661473` for the sampled pure states. Separate aligned cases approach equality. The smallest finite weighted-bound ratios in the ladder and multimode sweeps are approximately `1.000238` and `1.000763`, respectively, on the permitted side of the inequality. These are finite observations, not estimates of the optimal constants.

## Analytical tradeoff figure

Run:

```bash
python verification/plot_tradeoff.py
```

This evaluates the boundary at 400 positive tradeoff parameters for one target with squeezing $`r=1`$, adds the exact minimum-mode endpoint, and writes [tradeoff.svg](tradeoff.svg) and [tradeoff_curve.json](tradeoff_curve.json). The SVG displays the attainable upper-budget region and the photon infimum. Its plotted values come from the analytical integrals in [the tradeoff theorem](../science/tradeoff.md), with no fitted parameters.

The minimum-mode point is $`(u,v)=(1,0.8134302039\ldots)`$, and the photon infimum is $`0.5898731518\ldots`$. These coordinates use the **total** photon inventory across both parties. The plot generator also writes a temporary PNG preview in the parent directory of the repository.

## What the checks establish

The calculations can detect a missing factor of two in the fidelity or photon convention, a wrong endpoint coefficient, inconsistent multimode normalization, and finite discretization errors in the explicit catalysts. The covariance determinant check evaluates the full pure-state overlap independently of the product-of-pair formula.

The general Gaussian-instrument reduction, degenerate symplectic perturbation argument, closure under normalized postselection limits and continuum optimality are analytical statements proved in [Gaussian geometry](../science/gaussian_geometry.md), [the converse](../science/converse.md), [constructions](../science/constructions.md) and [the tradeoff account](../science/tradeoff.md). Random samples cannot establish them. The checks also do not establish a mixed-catalyst result or an exact finite-error frontier.

