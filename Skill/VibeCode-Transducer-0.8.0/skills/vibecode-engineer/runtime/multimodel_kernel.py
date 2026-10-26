"""Read-only prototype for applied-math verification across representations.
Synthetic examples; not a universal model selector or certified proof assistant.
Stdlib only, deterministic outputs, no eval/network/side effects.
"""
from __future__ import annotations
import math
from typing import Sequence


def dimension_compatible(lhs: Sequence[int], rhs: Sequence[int]) -> bool:
    if not lhs or len(lhs) != len(rhs) or any(isinstance(z, bool) or not isinstance(z, int) for z in tuple(lhs)+tuple(rhs)):
        raise ValueError('nonempty exponent vectors of equal length required')
    return tuple(lhs) == tuple(rhs)


def regions_3d(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError('n must be nonnegative integer')
    return sum(math.comb(n, k) for k in range(min(n,3)+1))


def discriminate_regions(observations: dict[int,int], next_n: int|None=None) -> dict:
    if not observations or any(isinstance(n,bool) or not isinstance(n,int) or n < 0 or isinstance(v,bool) or not isinstance(v,int) for n,v in observations.items()):
        raise ValueError('finite count observations required')
    fit_pow2=all(2**n == value for n,value in observations.items())
    fit_reg=all(regions_3d(n) == value for n,value in observations.items())
    candidate={'pow2':fit_pow2,'regions3':fit_reg}
    if next_n is None:
        next_n=max(observations)+1
    if next_n < 0: raise ValueError('invalid extrapolation')
    return {'fit_on_observed':candidate,'unresolved':sum(candidate.values()) != 1,
            'next_probe':next_n,'conditional_predictions':{'pow2':2**next_n,'regions3':regions_3d(next_n)},
            'scope':'within 2 nominated model families only; no universal proof'}


def euler_decay(rate: float, step: float, duration: float=1.0) -> dict:
    for x in [rate,step,duration]:
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite real inputs required')
    if rate < 0 or step <= 0 or duration < 0:raise ValueError('rate>=0, step>0, duration>=0')
    n=round(duration/step)
    if not math.isclose(n*step,duration,abs_tol=1e-10,rel_tol=1e-10):raise ValueError('duration must be integer number of steps')
    p=rate*step
    if p>1:raise ValueError('invalid transition probability rate*step >1; refine step')
    discrete=(1-p)**n
    continuum=math.exp(-rate*duration)
    return {'discrete':discrete,'continuum':continuum,'absolute_bridge_error':abs(discrete-continuum),
            'steps':n,'transition_probability':p,'assumptions':'independent survival, fixed rate; continuum limit as step decreases'}


def periodic_graph_eigenvalue(n:int,k:int=1)->dict:
    if isinstance(n,bool) or isinstance(k,bool) or not isinstance(n,int) or not isinstance(k,int) or n < 3 or k < 1 or k >= n//2:
        raise ValueError('n>=3 and 1<=k<n/2 integers')
    discrete=4*n*n*math.sin(math.pi*k/n)**2
    continuous=(2*math.pi*k)**2
    return {'scaled_discrete':discrete,'continuum_limit':continuous,
            'relative_error':abs(discrete-continuous)/continuous,
            'construction':'unit-periodic circle, equispaced nodes, nearest-neighbor Laplacian scaled by n^2'}


def external_decay(rate:float, gain:float, initial:float, times:Sequence[float])->list[float]:
    if any(not isinstance(v,(int,float)) or isinstance(v,bool) or not math.isfinite(v) for v in [rate,gain,initial,*times]):raise ValueError('finite inputs required')
    if rate<0 or gain<=0 or initial<0 or len(times)<2:raise ValueError('rate>=0, gain>0, initial>=0, >=2 times')
    return [gain*initial*math.exp(-rate*t) for t in times]


def inverse_ambiguity(rate:float,gain:float,initial:float,scale:float,times:Sequence[float])->dict:
    if scale<=0 or not math.isfinite(scale):raise ValueError('positive finite scale required')
    a=external_decay(rate,gain,initial,times)
    b=external_decay(rate,gain*scale,initial/scale,times)
    same=all(math.isclose(x,y,rel_tol=1e-13,abs_tol=1e-13) for x,y in zip(a,b))
    return {'indistinguishable_outputs':same,'different_parameters':scale!=1,
            'observed_output':a,'identifiable_product':gain*initial,
            'conclusion':'gain and initial separately nonidentifiable if gain unknown'}


def degrees_underdetermine_connectivity()->dict:
    edges_cycle=[(i,(i+1)%6) for i in range(6)]
    edges_tri=[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)]
    def stats(edges):
        deg=[0]*6;adj={i:set() for i in range(6)}
        for a,b in edges:deg[a]+=1;deg[b]+=1;adj[a].add(b);adj[b].add(a)
        remaining=set(range(6));parts=[]
        while remaining:
            start=next(iter(remaining));q=[start];part=set([start]);remaining.remove(start)
            while q:
                for b in adj[q.pop()]:
                    if b in remaining:remaining.remove(b);part.add(b);q.append(b)
            parts.append(part)
        return sorted(deg),len(parts)
    dc,cc=stats(edges_cycle);dt,ct=stats(edges_tri)
    return {'same_degree_sequence':dc==dt,'degrees':dc,'cycle_components':cc,'triangles_components':ct,
            'conclusion':'degree sequence alone cannot recover graph connectivity'}


def noisy_central_derivative(h:float,epsilon:float=.001)->dict:
    if h<=0 or epsilon<0:raise ValueError('positive step and nonnegative noise')
    # Input perturbation: +epsilon on right measurement, -epsilon on left measurement.
    # Not a stochastic sampling claim: adversarial bounded additive error.
    observed=(math.exp(-h)+epsilon-(math.exp(h)-epsilon))/(2*h)
    exact=-1.0
    clean=(math.exp(-h)-math.exp(h))/(2*h)
    return {'step':h,'observed_derivative':observed,'exact_derivative':exact,
            'noiseless_absolute_error':abs(clean-exact),'with_noise_absolute_error':abs(observed-exact),
            'worst_case_noise_term':epsilon/h,'adversarial_noise_not_random':True}


def robust_decision(lower:float,upper:float,threshold:float)->str:
    if not all(math.isfinite(x) for x in [lower,upper,threshold]) or lower>upper:raise ValueError('valid bounds')
    if lower>=threshold:return 'ROBUST_YES'
    if upper<threshold:return 'ROBUST_NO'
    return 'UNDETERMINED'


def observability_linear(A:Sequence[Sequence[float]],C:Sequence[float])->dict:
    """Rank of observability matrix for 2D linear ODE, single linear output.
    Rank=2 is necessary and sufficient for observability of this declared LTI pair.
    """
    if len(A)!=2 or any(len(r)!=2 for r in A) or len(C)!=2:
        raise ValueError('2x2 A and 1x2 C required')
    c0,c1=C
    ca0=c0*A[0][0]+c1*A[1][0]
    ca1=c0*A[0][1]+c1*A[1][1]
    determinant=c0*ca1-c1*ca0
    norm=max(1,*(abs(v) for row in A for v in row),abs(c0),abs(c1))
    # Float rank threshold is an engineering tolerance, not symbolic certification.
    full=abs(determinant)>1e-12*norm**2
    return {'observable':full,'rank':2 if full else (1 if c0 or c1 or ca0 or ca1 else 0),
            'determinant':determinant,'numerical_tolerance_note':'rank threshold heuristic; exact proof needs symbolic algebra'}


def example_results()->dict:
    return {'regions_before':discriminate_regions({0:1,1:2,2:4,3:8},4),
            'regions_after':discriminate_regions({0:1,1:2,2:4,3:8,4:15},5),
            'decay_refinement':[{'step':1/n,**euler_decay(.7,1/n)} for n in [2,4,8,16,32,64]],
            'graph_refinement':[{'n':n,**periodic_graph_eigenvalue(n)} for n in [8,16,32,64]],
            'hidden_inverse':inverse_ambiguity(.7,3,2,2,[0,.5,1,2]),
            'graph_ambiguity':degrees_underdetermine_connectivity(),
            'derivative_resolution':[noisy_central_derivative(h) for h in [.5,.1,.01,.001]],
            'observability_yes':observability_linear([[0,1],[-2,-3]],[1,0]),
            'observability_no':observability_linear([[-1,0],[0,-2]],[1,0]),
            'robust_decision_demo':[robust_decision(*r) for r in [(8,9,7),(2,4,7),(5,9,7)]]}

if __name__=='__main__':
    import json
    print(json.dumps(example_results(),indent=2,ensure_ascii=False))


def datalog_paths(edges: Sequence[tuple[str,str]], base_rule: bool) -> set[tuple[str,str]]:
    """Least fixed point of path(X,Z) :- edge(X,Y), path(Y,Z).
    Without path(X,Y) :- edge(X,Y), the least fixed point is empty.
    """
    edges=set(tuple(e) for e in edges)
    paths=set(edges) if base_rule else set()
    while True:
        new=paths | {(a,c) for a,b in edges for x,c in paths if x==b}
        if new==paths:return paths
        paths=new


def lens_get(source:dict)->dict:
    return {'name':source['name']}


def lens_put(source:dict,view:dict)->dict:
    if set(view)!={'name'} or not isinstance(view['name'],str):raise ValueError('typed view {name} required')
    return {**source,'name':view['name']}
