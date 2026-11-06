"""Check the multimode support inequality and the claimed Pareto contacts.

Finite numerical calculations check formulas and normalizations. The written
proofs establish the continuum optimization and all-protocol converse.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from check_ladders import constants, evaluate, ladder


def joint_constants(rs, lam):
    rows = [constants(r, lam) for r in rs]
    a = sum(row["A"] for row in rows)
    if lam == 0:
        return {"A": a, "v": 2*a*a}
    b = sum(row["B"] for row in rows)
    c = sum(row["C"] for row in rows)
    d = sum(quad(lambda x: (math.sinh(x)**2+lam)**(-1.5),
                 0, r, epsabs=1e-10, epsrel=1e-10)[0] for r in rs)
    return {"A": a, "B": b, "C": c, "D": d,
            "u": a*b, "v": 2*a*c, "du": (b*b-a*d)/2}


def joint_ladder(rs, lam, alpha):
    pieces = [evaluate(ladder(r, lam, alpha)) for r in rs]
    log_f = sum(math.log(p["F"]) for p in pieces)
    eps = -math.expm1(log_f)
    energy = sum(p["E"] for p in pieces)
    n = sum(p["n"] for p in pieces)
    return {"epsilon": eps, "F": math.exp(log_f),
            "n": n, "E": energy, "u": eps*n, "v": eps*energy}


def main():
    targets = [(1.,), (.4, 1.1), (.5, .5, .5)]
    contacts = []
    convergence = []
    min_support_ratio = math.inf
    for rs in targets:
        previous_u = math.inf
        previous_v = 0.
        for lam in np.logspace(-5, 3, 33):
            c = joint_constants(rs, float(lam))
            assert c["du"] < 0
            assert c["u"] < previous_u
            assert c["v"] > previous_v
            assert abs(c["v"]/2+lam*c["u"]-c["A"]**2) < 1e-9*max(1,c["A"]**2)
            previous_u, previous_v = c["u"], c["v"]
            # A contact point must satisfy every other supporting inequality.
            for test_lam in (0., .0001, .01, .1, 1., 10., 1000.):
                at = joint_constants(rs, test_lam)["A"]
                assert c["v"]/2+test_lam*c["u"] >= at*at-2e-8*max(1,at*at)
            contacts.append({"target": list(rs), "lambda": float(lam), **c})
        for lam in (.03, .3, 3.):
            c = joint_constants(rs, lam)
            errors = []
            for alpha in (.01, .002, .0004):
                obs = joint_ladder(rs, lam, alpha)
                g = .5*math.acosh(1/obs["F"])**2
                t = sum(math.sinh(r)**2 for r in rs)
                for test_lam in (0., .01, .1, 1., 10.):
                    at = joint_constants(rs, test_lam)["A"]
                    ratio = g*(obs["E"]/2+t+test_lam*(obs["n"]+len(rs)))/(at*at)
                    min_support_ratio = min(min_support_ratio, ratio)
                    assert ratio >= 1-1e-9
                err = max(abs(obs["u"]/c["u"]-1), abs(obs["v"]/c["v"]-1))
                errors.append(err)
                convergence.append({"target": list(rs), "lambda": lam,
                    "alpha": alpha, "observed": obs,
                    "limit_u": c["u"], "limit_v": c["v"],
                    "relative_error": err})
            assert errors[-1] < errors[0]
            assert errors[-1] < .01
    # Direct permutation covariance overlap, independently of the pair formula.
    from scipy.linalg import block_diag
    def pair_cov(r):
        c, s = math.cosh(2*r)/2, math.sinh(2*r)/2
        return np.array([[c,0,s,0],[0,c,0,-s],[s,0,c,0],[0,-s,0,c]])
    direct = []
    for vals in ([1,.8,.5,.1,0], [.4,.3,.17,0], [1.2,.9,.7,.4,.05,0]):
        ideal = block_diag(*(pair_cov(x) for x in vals[:-1]))
        actual = block_diag(*(pair_cov(x) for x in vals[1:]))
        f_cov = float(np.exp(-np.linalg.slogdet(ideal+actual)[1]/2))
        f_pair = math.prod(1/math.cosh(a-b)**2 for a,b in zip(vals[:-1],vals[1:]))
        assert math.isclose(f_cov, f_pair, rel_tol=2e-12)
        direct.append({"ladder": vals, "covariance_fidelity": f_cov,
                       "pair_fidelity": f_pair})
    result = {"scope": "Fixed multimode support, contact curvature, Euler ladder convergence, independent covariance overlaps.",
              "contact_cases": len(contacts), "ladder_cases": len(convergence),
              "minimum_finite_support_ratio": min_support_ratio,
              "direct_covariance_checks": direct, "contacts": contacts,
              "convergence": convergence}
    Path(__file__).with_name("tradeoff_results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("contacts","convergence")},indent=2))


if __name__ == "__main__":
    main()
