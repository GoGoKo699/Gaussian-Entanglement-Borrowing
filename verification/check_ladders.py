"""Finite scientific checks for the Gaussian borrowing resource law.

This checks the explicitly specified passive cyclic construction and numerical
asymptotics. It does not prove the all-protocol Gaussian geometry converse.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad


def constants(r, lam):
    a = quad(lambda x: math.sqrt(math.sinh(x)**2 + lam), 0, r,
             epsabs=2e-12, epsrel=2e-12)[0]
    if lam == 0:
        return {"A": a, "epsilon_E_limit": 2*a*a,
                "epsilon_n_limit": None}
    b = quad(lambda x: 1/math.sqrt(math.sinh(x)**2 + lam), 0, r,
             epsabs=2e-12, epsrel=2e-12)[0]
    c = quad(lambda x: math.sinh(x)**2/math.sqrt(math.sinh(x)**2 + lam),
             0, r, epsabs=2e-12, epsrel=2e-12)[0]
    return {"A": a, "B": b, "C": c,
            "epsilon_E_limit": 2*a*c, "epsilon_n_limit": a*b}


def ladder(r, lam, alpha):
    vals = [r]
    if lam == 0:
        i = 1
        while True:
            x = 2*math.atanh(math.tanh(r/2)*math.exp(-alpha*i))
            vals.append(x)
            if x <= alpha:
                break
            i += 1
    else:
        x = r
        while x > 0:
            x = max(0., x-alpha*math.sqrt(math.sinh(x)**2+lam))
            vals.append(x)
        vals.pop()  # zero is appended once below
    vals.append(0.)
    return np.array(vals)


def evaluate(vals):
    r = float(vals[0])
    delta = vals[:-1]-vals[1:]
    n = len(vals)-2
    energy = float(2*np.sum(np.sinh(vals[1:-1])**2))
    log_f = -2*float(np.sum(np.log(np.cosh(delta))))
    eps = -math.expm1(log_f)
    f = math.exp(log_f)
    g = 0.5*math.acosh(1/f)**2
    d2 = float(delta@delta)
    return {"r": r, "n": n, "E": energy, "F": f,
            "epsilon": eps, "epsilon_n": eps*n,
            "epsilon_E": eps*energy, "d2": d2, "gF": g}


def main():
    records = []
    min_weighted_ratio = math.inf
    for r in (0.25, 1., 2.):
        for lam in (0., .01, .1, 1., 10.):
            c = constants(r, lam)
            for alpha in (.01, .002, .0004):
                obs = evaluate(ladder(r, lam, alpha))
                assert obs["d2"] <= obs["gF"]*(1+2e-8)
                ratios = []
                for test_lam in (0., .001, .01, .1, 1., 10., 100.):
                    at = constants(r, test_lam)["A"]
                    lhs = (obs["E"]/2 + math.sinh(r)**2 +
                           test_lam*(obs["n"]+1))*obs["gF"]
                    ratios.append(lhs/(at*at))
                min_weighted_ratio = min(min_weighted_ratio, *ratios)
                assert min(ratios) >= 1-1e-9
                records.append({"lambda": lam, "alpha": alpha,
                                "prediction": c, "observed": obs,
                                "min_tested_support_ratio": min(ratios)})
    rng = np.random.default_rng(773)
    random_min = math.inf
    for _ in range(300):
        r = float(rng.uniform(.1, 3))
        n = int(rng.integers(2, 250))
        vals = np.r_[r, np.sort(rng.uniform(0, r, n))[::-1], 0.]
        obs = evaluate(vals)
        for lam in (0., .1, 1., 10.):
            a = constants(r, lam)["A"]
            ratio = (obs["E"]/2+math.sinh(r)**2+lam*(n+1))*obs["gF"]/(a*a)
            random_min = min(random_min, ratio)
            assert ratio >= 1-1e-9
    out = {"scope": "Cyclic passive construction; 45 asymptotic cases and 300 random ladders.",
           "all_assertions_passed": True,
           "minimum_tested_weighted_bound_ratio": min_weighted_ratio,
           "random_ladder_minimum_ratio": random_min,
           "records": records}
    Path(__file__).with_name("ladder_results.json").write_text(json.dumps(out, indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!="records"}, indent=2))
    print("r=1, finest alpha=0.0004:")
    for row in records:
        if row["observed"]["r"] == 1 and row["alpha"] == .0004:
            print(json.dumps({"lambda": row["lambda"],
                 "epsilon": row["observed"]["epsilon"],
                 "n": row["observed"]["n"],
                 "epsilon_n": row["observed"]["epsilon_n"],
                 "predicted_epsilon_n": row["prediction"]["epsilon_n_limit"],
                 "epsilon_E": row["observed"]["epsilon_E"],
                 "predicted_epsilon_E": row["prediction"]["epsilon_E_limit"]}))


if __name__ == "__main__":
    main()
