# AntiSlop research and executable model audit — mathematical DSL registry × VCT

**Tanggal:** 23 Oktober 2026 · **Status:** research prototype; VCT/plugin **not modified** in this run.

## 1. Corpus, provenance, and audit scope

Audited source: `/mnt/data/math_dsl_operator_registry.csv`, SHA-256 `5e4f4462f0b0e4741b5885666f05bf7a2ddff49592961eea2cd52ac5aa87ab9b`.

- Exactly **99** original rows, 12 mathematical/representation domains; IDs `MATH-001`–`MATH-099` unique and sequential. **No `MATH-100`** is present in this uploaded registry.
- All 99 records have values in all ten source columns. **Completeness is not correctness**.
- Original `reference_ids` contain `S01`–`S37`, but the uploaded CSV does not define those IDs; it is therefore **not possible from this CSV alone** to audit their page-level bibliography or validate the original citation-to-theorem links. The PDF is a separate source, not automatic evidence for all 99 entries.
- Research independently identified 22 open/free journal resources, proceedings or institutional source records. They are mapped in `data/oa_source_ledger.csv`. Source-to-operator links in `data/registry_99_antislop_audit.csv` distinguish mechanisms directly covered by reviewed article abstracts/full text from broader *domain context*. **None of the 99 entries has been independently machine-proved by this crosswalk**.
- 39 rows received priority-review notes; that count denotes **review flags**, not 39 confirmed false theorems. 21 rows have article-level applied-method linkages; 78 have contextual linkage only. Full-text access varies; journal/abstract indexing is not the same as reading every full proof.

### High-priority issues with independent discriminating cases

| ID | Audit finding | Evidence class | Required retest |
|---|---|---|---|
| MATH-034 | `lim_{x→a} f(x)=f(a)` encodes continuity *at a*, not a general limit theorem | CONFIRMED conceptual distinction | Compare `f(x)=1` for `x!=0`, `f(0)=0`: limit exists, continuity fails |
| MATH-043 | `Δf(n)=f(n+1)-f(n)` is a unit-grid difference; its relation to a continuum derivative needs `h` and limit/convergence | CONFIRMED missing bridge for proposed use | Compare numerical difference at multiple steps under noise |
| MATH-064 | `L=D-A` does not specify weights, scaling, boundary conditions, or a continuum limit | SUPPORTED-RISK | Periodic scaled cycle graph eigenvalue convergence on refinements |
| MATH-095 | A recursive path rule with no seed rule has empty least fixed-point semantics | CONFIRMED for *that rule alone* | Test recursive-only vs recursive + edge base |
| MATH-097 | GetPut/PutGet are lens laws under a domain/view contract; loss of hidden fields prevents unique inversion | CONFIRMED information-loss counterexample | Test both laws with preserving source context and failure of source recovery from view alone |
| MATH-015/093/094 | OWL cardinality/entailment and SHACL validation cannot be treated as equivalent under open/closed-world assumptions | CONFIRMED distinction from journal abstract | Distinguish absence of asserted triples from logical negation and constraint validation |
| MATH-033/088 | Jacobian rank and solver fit do not by themselves establish global structural identifiability | CONFIRMED for counterexample class | Explicitly exhibit transformed hidden parameter pair with identical observable outputs |
| MATH-085 | Persistence stability requires mathematical conditions on filtrations, comparison metric, and spaces | SUPPORTED-RISK | Establish theorem preconditions before claim |
| MATH-053 | Gauss–Markov BLUE requires the particular linear-unbiased estimator class and covariance assumptions | SUPPORTED-RISK | Supply covariance/exogeneity/rank witness, separate from robust estimators |
| MATH-099 | Proof of an encoded formula does not validate empirical adequacy of encoding | SUPPORTED-RISK | Formalization audit + independent empirical mapping test |

A near-miss positive control: `MATH-097` **is not invalid** merely because `get` discards some source information. A lawful lens retains source context in `put(source,view)` and satisfies both round-trip laws. In contrast `get(source)` alone is not a complete inverse of the source model. Both were implemented and tested.

## 2. Scientific architecture: a network of partially compatible models

Proposed synthesis **(not a cited theorem)**:

\[
\mathfrak{M}=\big(\{M_i\}_{i\in I},\{O_i\},\{D_{ij}\},\{R_{ji}\},\{K_{ij}\},\mathcal{E},\mathcal{P}\big)
\]

`M_i` = model with typed state space and dynamics; `O_i` = observation map (outward behavior); `D_{ij}` = discretization/abstraction/quantization; `R_{ji}` = reconstruction/coarse-graining/lifting; `K_{ij}` = explicit cross-model consistency predicate (not assumed identity); `E` = empirical evidence + uncertainty; `P` = proof obligations and test receipts.

For an underlying continuum evolution `F_t` and discretization `Q_h`, numerical update `U_h` should be assessed by an *approximate commuting relation*, when applicable:

\[
 d\big(R_h U_h Q_h x,\;F_h x\big)\leq
\varepsilon_{\mathrm{discretization}}(h)+\varepsilon_{\mathrm{observation}}+\varepsilon_{\mathrm{model}}
\]

This bound is a **goal/contract template**; each term requires a defined metric, underlying assumptions, and an independent bound or estimate. It is not proven for an arbitrary plugin operation. For domain-incompatible models, use a *consistency relation* instead of inventing a shared scalar distance.

The **observation inverse** is a different question: `y(t)=O_i(x(t),θ)`. If two parameter/state assignments generate indistinguishable output under all available experiments, they belong to an observational-equivalence class, not to a uniquely recovered hidden truth. Model mismatch and noise make practical identification still weaker.

### Distinguish five kinds of uncertainty

1. Numerical/discretization error: refine step/mesh and test convergence.
2. Measurement error and selection/censoring: quantify under an explicit observation model.
3. Parameter uncertainty: identifiable parameters may remain weakly estimated.
4. Structural/model-class uncertainty: different causal/mechanistic models fit observations.
5. Interpretive/construct uncertainty: symbolic unit may not preserve the purported empirical meaning.

**Do not collapse all five into a single residual `δ`, likelihood, or confidence score.**

## 3. Research evidence and what it licenses

| Research track | Selected open/free article | Operational lesson and limits |
|---|---|---|
| Dynamical model discovery | Brunton et al. (2016), *PNAS* ([OA01](https://pmc.ncbi.nlm.nih.gov/articles/PMC4839439/)) | Sparse regression can infer compact dynamics *in a suitable coordinate/basis*; can fail under a bad basis or noisy differentiation. It does not identify every governing law from arbitrary outputs. |
| Hidden-state identifiability | Villaverde et al. (2023), *Bioinformatics* ([OA02](https://pmc.ncbi.nlm.nih.gov/articles/PMC9913045/)) | Analyze parameter identifiability and state observability before fitting. Structural local versus global identification must be distinguished. |
| Hybrid multi-scale modeling | Hybrid ABM review (2015) ([OA03](https://pmc.ncbi.nlm.nih.gov/articles/PMC4564133/)) | Couple discrete agents with continuous environmental models using explicit scale interface and synchronization. |
| Graph to continuum | Bungert & Slepčev (2026) ([OA04](https://link.springer.com/article/10.1007/s00526-026-03414-1)) | Graph Laplacian/convergence is conditional on graph construction and scaling, not automatically true for arbitrary graphs. |
| Topology from finite samples | Chazal & Michel (2021) ([OA05](https://pmc.ncbi.nlm.nih.gov/articles/PMC8511823/)) | Scale-dependent simplicial filtrations and Betti/persistence inference require sampling assumptions and stability conditions. |
| Formal hybrid verification | Event-B hybrid proceedings (2020) ([OA06](https://pmc.ncbi.nlm.nih.gov/articles/PMC7242035/)) | Discrete transitions + continuous dynamics create explicit proof obligations; a simulation PASS is not a refinement proof. |
| Purpose-relative choice | Model-selection guide (2021) ([OA07](https://pmc.ncbi.nlm.nih.gov/articles/PMC8187274/)) | Exploration, inference and prediction call for different model selection/evaluation criteria, even with the same data. |
| Against naive model averaging | Critical multimodel paper (2024) ([OA08](https://pmc.ncbi.nlm.nih.gov/articles/PMC11202409/)) | Simple multimodel averaging can underestimate uncertainty; avoid treating weighted averaging as universal epistemic reconciliation. |
| Mesh / error estimator | Ahmed Blal et al. (2021) ([OA09](https://link.springer.com/article/10.1007/s40314-021-01426-5)) | Adaptive FEM requires a posteriori indicators and mesh assumptions; several mesh points are not a theoretical error certificate. |
| Bidirectional model transformations | City MDE lens study (2021) ([OA11](https://link.springer.com/article/10.1007/s10270-020-00851-0)); digital multi-scale lenses (2022) ([OA21](https://doi.org/10.1098/rspa.2022.0156)) | Test GetPut/PutGet laws and source-context retention; inverse reconstruction from a lossy view cannot be presumed. |
| Open vs closed-world | Oudshoorn et al. (2026) ([OA12](https://www.sciencedirect.com/science/article/pii/S0004370226000093)) | OWL entailment and SHACL constraint checking require a declared model of missing knowledge. |
| Research validation | Oberkampf & Trucano (2002) ([OA15](https://www.sandia.gov/research/publications/details/verification-and-validation-in-computational-fluid-dynamics-2002-03-01/)) | Distinguish numerical verification, model validation and predictive uncertainty. Source here is public institutional record/report metadata. |

The 22-reference ledger lists additional studies. Not every journal link could be inspected beyond its indexed abstract in this session, and that limitation is intentional provenance disclosure.

## 4. Mahajan: heuristic synthesis, not final proof

The supplied *Street-Fighting Mathematics* (Mahajan 2010) describes **Dimensions** (chapter 1), **Easy cases** (2), **Lumping** (3), **Pictorial proofs** (4), **Taking out the big part** (5), **Analogy** (6). MIT OCW *Syllabus* for 18.098 (2008) explicitly includes **discretization** among its techniques: https://ocw.mit.edu/courses/18-098-street-fighting-mathematics-january-iap-2008/pages/syllabus/ .

- Book printed p. 20 / PDF page 37: a frustum model missing interaction term `ab` fails a boundary test. Proper repair is to change model class `V=h(αa²+βab+γb²)`; not merely refit old coefficients.
- Book printed pp. 24–26: dimensionless groups reduce an unknown multivariate drag function to an unknown function of Reynolds number. Dimensionless reduction constrains form but does **not** supply the missing function.
- Book printed pp. 32–35: population rectangle, 1/e and FWHM are expedient approximations; whether the error is tolerable is task-relative.
- Book printed pp. 37–40: `f/x` secant can be wildly inaccurate when the omitted baseline `f(0)` matters, e.g. `f(x)=x²+100`.
- Book printed pp. 50–54: the pendulum transforms a nonlinear factor into a linearized effective term *only over controlled amplitude regimes*. At large amplitude, the linearized conclusion fails.
- Book printed pp. 103–106: initial observations may be consistent with rival combinatorial models; the `n=4` easy case discriminates their predictions, but a finite PASS is no universal proof.

VCT should represent *heuristic license, declared approximation tolerance, proof debt, and information loss* separately.

## 5. Runnable case studies and measured results

Source: `multimodel_kernel.py`; observations are **synthetic/analytic constructed examples**, not measurements of the user's app or reality. Run `python -m unittest discover -s tests -v`.

**A. Discrete to continuous (MATH-022/035/039/043/088).**

For fixed rate `r`, the single-step discrete survival model is `x[k+1]=(1-rh)x[k]`, with physical-step precondition `0≤rh≤1`. At time `T` its result is `(1-rh)^(T/h)`, while the candidate continuum approximation is `e^(-rT)`. As `h→0+`, `log(1-rh)/h→-r`, implying convergence for fixed `T`.

When `r=.7`, `T=1`, computed absolute error is **0.074085** at `h=.5`, **0.033335** at `h=.25`, and decreases on 6 tested refinements. `r=2,h=1` is rejected because the implied transition probability exceeds 1. **The analytic limiting argument is conditional on this model, not a theorem about arbitrary discretizations.**

**B. Graph versus continuum (MATH-064/065/083).**

For *periodic, equispaced, nearest-neighbor* cycle graph on a circle of length 1 and `L=D-A`, scale `n²L`. Frequency `k=1` eigenvalue is `λ_{1,n}=4n² sin²(π/n)→4π²`. Computed relative error decreases from **5.04% (n=8)** to **0.0803% (n=64)**. A generic graph Laplacian lacks this specific limit without analogous hypotheses.

**C. Unobserved state / inverse (MATH-027/033/088).**

`x(t)=x0 e^{-rt}`; observation `y(t)=c x(t)`. Transformation `(c,x0)→(qc,x0/q)` for nonzero `q` leaves *every* measured output identical. Tested `(c,x0)=(3,2)` and `(6,1)` produce the same output. Thus, even noiseless arbitrarily dense `y(t)` cannot recover `c` and `x0` individually without additional assumptions. In a 2-state linear system, the observability matrix `[C; CA]` has rank 2 in the coupled positive control and rank 1 in the uncoupled negative control.

**D. Noise–resolution tradeoff (MATH-035/043).**

Clean central finite difference on `e^{-t}` improves with smaller `h`, but deliberately perturbed measurements `f(h)+ε` and `f(-h)-ε` induce an error term `ε/h`. With `ε=.001`, the total derivative error can worsen as `h` shrinks. Therefore `refine grid` must not be a universal gate for noisy observations.

**E. Multi-model induction versus proof (MATH-007/023/091).**

`R_3(n)=sum_{k=0}^{3} binom(n,k)` and `2^n` both fit `n=0,1,2,3`, but at `n=4` predict 15 and 16. Python rejects the latter after seeing 15; it does not prove the former universally. Additional structural/proof argument is needed.

**F. Graph compression and nonunique inverse (MATH-059/060/068).**

`C6` and `C3⊔C3` have identical degrees `[2,2,2,2,2,2]` yet 1 versus 2 connected components. A degree histogram is not an invertible encoding of adjacency.

**G. KRR/Datalog and lens laws (MATH-095/097).**

The registry's displayed recursive Datalog path clause alone yields the empty least fixed point. Adding the base clause `path(x,y) :- edge(x,y)` recovers transitive reachability. Lens examples satisfy `put(s,get(s))=s` and `get(put(s,v))=v`, while separately demonstrating that the view cannot recover hidden source fields by itself.

## 6. Proposed DSL/MDE/KRR intermediate representation

A model contract should at minimum carry:

- `phenomenon`, `observable`, `entity_identity`, `scope`, `source_fingerprint`, `units`, `measurement_scale`;
- `representation`: state type, what is preserved, what is lost, and what transformations are admissible;
- `models[]`: separate, typed mechanistic/statistical/graph/topological/formal hypotheses with forward maps;
- `bridges[]`: source model, target model, direction, `discretize|reconstruct|coarse_grain|lens|compare`, metric and assumptions;
- `inference`: `abductive_candidate|inductive_estimate|deductive_consequence|formal_theorem`, not a unified opaque score;
- `checks[]`: typed premise, operator, numeric test/proof oracle, negative control, tolerance, error decomposition;
- `decision`: target loss, acceptable ambiguity, robust/unknown/rejected outcome, remaining evidence debt;
- `engineering_tasks[]`: dependency graph whose nodes reference exactly which model assumptions and test witnesses license the task.

A **cross-model proof obligation** is not simply `model A ≈ model B`. It is `assumptions A + bridge semantics B + metric/target C ⇒ bounded discrepancy/invariant preservation D`. If the representation map is many-to-one, `round-trip exact inverse` is usually an inadmissible obligation; instead test lawful lens updates or equivalence classes.

### Suggested non-linear task flow

`P00 Scope/Claim` → `P01 Identify units/relations` → `P02 Construct observations & missingness` → `P03 Rival model family discovery` → `P04 Formal map & admissible transformations` → `P05 Select bridges (D/R/aggregation)` → `P06 Python compute/simulate` → `P07 Falsifier and independent controls` → `P08 Identifiability/observability` → `P09 Convergence/error budget` → `P10 Proof obligation dispatch` → `P11 Decision threshold and uncertainty` → `P12 Engineering task graph`. Failure at P08/P09/P10 must loop back to the *earliest invalid assumption*, often P01–P04, not merely retune coefficients.

Three proof classes must be explicit: **formal symbolic proof of an encoded mathematical statement**, **numerical verification/conditional convergence evidence**, and **empirical validation of representational adequacy against independently observed behavior**. None subsumes the other.

## 7. Execution record and residual debts

- Executed: `python multimodel_kernel.py > data/model_results.json`; `python -m unittest discover -s tests -v`.
- Result: **36 tests passed** in local Python; see `tests_receipt.txt`, source tests and JSON output for direct inspection.
- Test types: deterministic numeric regression, input-contract negative controls, near-miss legitimate lens examples, least-fixed-point Datalog, observational nonidentifiability, and cross-scale refinement checks.
- Unexecuted: 99 independent implementations; symbolic proof assistant/SMT on all 99; realistic stochastic parameter inference; production VCT end-to-end plugin integration; data-driven validation on external real-world measurements.
- Research limitations: the uploaded CSV omits the original `Sxx` bibliography. Verified article abstracts are relevant external work, **not confirmation that source IDs are correctly attached to every mathematical entry**. Bibliography ledger labels are research mappings, not peer-review of this prototype.
- Excluded inference: asymptotic proof from finite convergence table; unique internal mechanism from outward behavior; causal structure from correlation; numerical fit means ontological truth; full model averaging is always valid; installed plugin means hosted Python MCP.

**Recommendation:** insert this as a separately testable *cross-representation & proof-obligations* layer adjacent to VCT v0.4's `heuristic_inference.py`; keep old `MATH-001..099` unchanged and add namespace `VCT-BRIDGE-001..`, rather than silently changing historic numbering. Verify existing plugin source in a fresh snapshot before any merge.
