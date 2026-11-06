"""Finite numerical challenge of covariance-metric constants and Gaussian ladders.

These checks do not prove the matrix inequalities or asymptotic statements.
"""
import json
import sys
from pathlib import Path
import scipy
import numpy as np
from scipy.linalg import eigvalsh, expm

rng = np.random.default_rng(20261106)

def J(m):
    return np.block([[np.zeros((m,m)), np.eye(m)],[-np.eye(m),np.zeros((m,m))]])

def symplectic_eigs(v):
    e,u=np.linalg.eigh(v)
    if np.min(e)<=0:
        raise ValueError('not SPD')
    z=(u*np.sqrt(e))@u.T
    vals=np.linalg.eigvalsh(1j*z@J(v.shape[0]//2)@z)
    return vals[len(vals)//2:]

def delta_sq(v,w):
    return np.sum(np.log(eigvalsh(w,v))**2)

def ent(v,n):
    # Coordinates are q_1,...,q_2n,p_1,...,p_2n.
    p=np.ones(4*n); p[3*n:]=-1
    pt=p[:,None]*v*p[None,:]
    ls=np.sort(np.log(2*symplectic_eigs(pt)))
    return ls[n:]/2

def tmsv(rs):
    n=len(rs); m=2*n
    v=np.zeros((2*m,2*m))
    for k,r in enumerate(rs):
        c=np.cosh(2*r)/2; s=np.sinh(2*r)/2
        a=k; b=n+k
        for q in [a,b,m+a,m+b]:v[q,q]=c
        v[a,b]=v[b,a]=s
        v[m+a,m+b]=v[m+b,m+a]=-s
    return v

out={'seed':20261106,'general_spd_trials':0,'pure_gaussian_trials':0,
     'max_spd_ratio':0.,'max_pure_ratio':0.,'saturating_cases':[],
     'energy_ladder_checks':[]}
for m in [1,2,3,4,6,8]:
    for k in range(60):
        x=rng.normal(size=(2*m,2*m)); x=(x+x.T)/2/np.sqrt(2*m)
        v=expm(x)
        y=rng.normal(size=x.shape); y=(y+y.T)/2/np.sqrt(2*m)
        w=expm(y if k%2 else x+0.02*y)
        lhs=np.sum((np.log(symplectic_eigs(v))-np.log(symplectic_eigs(w)))**2)
        rhs=delta_sq(v,w)/2
        ratio=lhs/rhs
        out['max_spd_ratio']=max(out['max_spd_ratio'],float(ratio))
        out['general_spd_trials']+=1
        assert ratio<=1+1e-7,(m,k,ratio)
for n in [1,2,3,4]:
    m=2*n
    for k in range(60):
        rs=rng.uniform(0,1.4,n)
        v=tmsv(rs)
        x=rng.normal(size=v.shape); x=(x+x.T)/2/np.sqrt(4*n)
        z=expm(J(m)@x*(0.02 if k%2 else 0.7))
        w=z@v@z.T
        sign,ld=np.linalg.slogdet(v+w)
        assert sign>0
        f=float(np.exp(-ld/2))
        lhs=float(np.sum((ent(v,n)-ent(w,n))**2))
        rhs=float(np.arccosh(1/f)**2/2)
        ratio=lhs/rhs if rhs else 0
        out['max_pure_ratio']=max(out['max_pure_ratio'],ratio)
        out['pure_gaussian_trials']+=1
        assert ratio<=1+1e-6,(n,k,ratio)
for n in [1,2,5,20]:
    for d in [1e-2,1e-3]:
        f=float(np.exp(-2*n*np.log(np.cosh(d))))
        ratio=n*d*d/(np.arccosh(1/f)**2/2)
        out['saturating_cases'].append({'n':n,'delta':d,'ratio':ratio})
for r in [.3,1.,2.]:
    for h in [1e-2,1e-3,1e-4]:
        z=np.tanh(r/2)
        M=int(np.ceil(np.log(z/np.tanh(h/2))/h))
        xs=2*np.arctanh(z*np.exp(-h*np.arange(1,M+1)))
        ds=-np.diff(np.r_[r,xs,0])
        logf=-2*np.sum(np.logaddexp(ds,-ds)-np.log(2))
        eps=float(-np.expm1(logf))
        E=float(2*np.sum(np.sinh(xs)**2))
        out['energy_ladder_checks'].append({'r':r,'h':h,'N':M,'epsilon':eps,
            'energy':E,'epsilon_E':eps*E,'claimed_limit':2*(np.cosh(r)-1)**2,
            'ratio':eps*E/(2*(np.cosh(r)-1)**2)})
out['environment'] = {'python': sys.version.split()[0], 'numpy': np.__version__, 'scipy': scipy.__version__}
Path(__file__).with_name('geometry_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('saturating_cases','energy_ladder_checks')},indent=2))
