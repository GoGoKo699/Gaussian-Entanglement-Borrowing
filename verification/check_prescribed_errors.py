"""Check the finite prescribed-error bounds in science/constructions.md.

This reproduces the fixed finite audit of the graded, uniform, and photon
ladders, including zero-catalyst cases and requested infidelity 0.99.
Numerical checks test the formulas; the written proofs establish the bounds.
"""
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.integrate import quad


SEED = 20261106
RELATIVE_TOLERANCE = 2e-9


def joint_integrals(rs, lam):
    def f(x):
        return math.sqrt(math.sinh(x)**2 + lam)

    def integrate(fn):
        return sum(quad(fn, 0, r, epsabs=2e-11, epsrel=2e-11)[0]
                   for r in rs)

    return (integrate(f), integrate(lambda x: 1/f(x)),
            integrate(lambda x: math.sinh(x)**2/f(x)))


def joint_statistics(blocks):
    gaps = np.concatenate([a[:-1] - a[1:] for a in blocks])
    n = sum(len(a) - 2 for a in blocks)
    energy = 2*sum(float(np.sum(np.sinh(a[1:-1])**2))
                   for a in blocks)
    squared_gaps = float(gaps @ gaps)
    # log(cosh d) = log(1 + 2 sinh(d/2)^2), stable for small gaps.
    loss = 2*float(np.sum(np.log1p(2*np.sinh(gaps/2)**2)))
    return n, energy, squared_gaps, loss, float(np.max(gaps))


def check_le(left, right, label):
    tolerance = RELATIVE_TOLERANCE*max(1, abs(left), abs(right))
    assert left <= right + tolerance, (label, left, right)


def cases():
    rng = np.random.default_rng(SEED)
    rows = []
    for _ in range(72):
        rs = rng.uniform(.08, 2.5, int(rng.integers(1, 4)))
        eps = float(10**rng.uniform(-3, -.1))
        lam = float(10**rng.uniform(-3, 2))
        rows.append((rs, eps, lam))
    explicit = [
        ([.1], .99, .01),
        ([.1, .2, .3], .99, 100.),
        ([1.], .001, .1),
        ([.3, 1., 1.7], .001, 1.),
    ]
    rows.extend((np.array(rs), eps, lam) for rs, eps, lam in explicit)
    return rows


def main():
    if sys.flags.optimize:
        raise SystemExit("Run without -O: this script uses Python assertions.")

    counts = {"graded": 0, "uniform": 0, "photon": 0,
              "support_contacts": 0}
    zero_catalysts = {"graded": 0, "uniform": 0, "photon": 0}
    maximum_error_ratio = 0.
    rows = cases()

    for rs, eps, lam in rows:
        k = len(rs)
        lipschitz = math.cosh(max(rs))
        target_photons = sum(math.sinh(r)**2 for r in rs)
        r_sum = sum(rs)
        k_sum = sum(math.cosh(r) - 1 for r in rs)
        h_sum = sum(math.sinh(2*r)/4 - r/2 for r in rs)
        j_sum = sum((math.sinh(2*r)/4 - r/2)/r for r in rs)
        ell = -math.log1p(-eps)

        # Positive-parameter Euler construction: equations (6)--(9).
        a, b, c = joint_integrals(rs, lam)
        maximum_f = math.sqrt(math.sinh(max(rs))**2 + lam)
        step = ell/(a + lipschitz*ell/2)
        blocks = []
        for r in rs:
            values = [float(r)]
            while values[-1] > 0:
                values.append(max(
                    0., values[-1] - step*math.sqrt(
                        math.sinh(values[-1])**2 + lam)))
            blocks.append(np.array(values))
        n, energy, s, loss, largest_gap = joint_statistics(blocks)
        check_le(step*a - step**2*(target_photons + k*lam)/4,
                 s, "graded lower squared-gap bound")
        check_le(s, step*a/(1 - lipschitz*step/2),
                 "graded upper squared-gap bound")
        check_le(step*n, b, "graded lower mode bound")
        check_le(b - step*n,
                 lipschitz*s/(2*lam) + k*step*maximum_f/math.sqrt(lam),
                 "graded upper mode bound")
        check_le(c - step*target_photons, step*energy/2,
                 "graded lower photon bound")
        check_le(step*energy/2, c + lipschitz*s,
                 "graded upper photon bound")
        check_le(largest_gap, step*maximum_f, "graded largest gap")
        check_le(loss, ell, "graded prescribed infidelity")
        maximum_error_ratio = max(
            maximum_error_ratio, -math.expm1(-loss)/eps)
        counts["graded"] += 1
        zero_catalysts["graded"] += int(n == 0)

        # Uniform construction: equations (14)--(16), including rounding.
        delta = ell/r_sum
        numbers_of_gaps = [math.ceil(r/delta) for r in rs]
        blocks = [np.linspace(r, 0, m + 1)
                  for r, m in zip(rs, numbers_of_gaps)]
        n, energy, s, loss, largest_gap = joint_statistics(blocks)
        check_le(s, ell, "uniform prescribed squared-gap bound")
        check_le(r_sum**2/ell - k, n, "uniform lower mode bound")
        check_le(n, r_sum**2/ell, "uniform upper mode bound")
        check_le(h_sum/delta - target_photons, energy/2,
                 "uniform lower photon bound")
        check_le(energy/2, h_sum/delta + j_sum,
                 "uniform upper photon bound")
        counts["uniform"] += 1
        zero_catalysts["uniform"] += int(n == 0)

        # Hyperbolic-flow construction: equations (19)--(21).
        step = 2*ell/(k_sum + math.sqrt(k_sum**2 + 4*k*ell))
        blocks = []
        for r in rs:
            if r <= step:
                blocks.append(np.array([r, 0.]))
            else:
                tau = math.log(math.tanh(r/2)/math.tanh(step/2))
                n_j = math.ceil(tau/step)
                values = 2*np.arctanh(
                    math.tanh(r/2)*np.exp(-step*np.arange(n_j + 1)))
                blocks.append(np.r_[values, 0.])
        n, energy, s, loss, largest_gap = joint_statistics(blocks)
        check_le(step*(k_sum - k*(math.cosh(step) - 1))
                 /(1 + lipschitz*step/2),
                 s, "photon lower squared-gap bound")
        check_le(s, step*k_sum + k*step**2,
                 "photon upper squared-gap bound")
        check_le(k_sum - k*(math.cosh(step) - 1)
                 - step*target_photons,
                 step*energy/2, "photon lower inventory bound")
        check_le(step*energy/2, k_sum, "photon upper inventory bound")
        check_le(loss, ell, "photon prescribed infidelity")
        counts["photon"] += 1
        zero_catalysts["photon"] += int(n == 0)

    # The same finite cross-support and contact-order checks as the audit.
    parameters = (.001, .01, .1, 1., 10., 100.)
    for rs in ([1.], [.25, 1., 1.7], [.7, .7]):
        contacts = []
        for lam in parameters:
            a, b, c = joint_integrals(rs, lam)
            u, v = a*b, 2*a*c
            contacts.append((u, v))
            for mu in parameters:
                support_a, _, _ = joint_integrals(rs, mu)
                check_le(support_a**2, v/2 + mu*u, "contact support")
                counts["support_contacts"] += 1
        assert all(contacts[i+1][0] < contacts[i][0]
                   and contacts[i+1][1] > contacts[i][1]
                   for i in range(len(contacts) - 1))

    result = {
        "scope": (
            "Prescribed-error finite bounds for three passive ladder "
            "constructions, integer rounding, and finite contact supports."
        ),
        "all_checks_passed": True,
        "seed": SEED,
        "random_target_error_cases": 72,
        "explicit_target_error_cases": 4,
        "requested_infidelity_0_99_cases": 2,
        "counts": counts,
        "zero_catalyst_cases": zero_catalysts,
        "largest_actual_to_requested_error_ratio_graded": maximum_error_ratio,
        "inequality_tolerance": {
            "relative_coefficient": RELATIVE_TOLERANCE,
            "scale": "max(1, abs(left), abs(right))",
        },
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
    }
    output = Path(__file__).with_name("prescribed_error_results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

