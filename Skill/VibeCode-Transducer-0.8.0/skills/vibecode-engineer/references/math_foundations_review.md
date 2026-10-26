# Mathematical Foundations for Declarative DSL — Annotated Open-Access Review
**Date:** 2026-10-23  |  **Status:** literature synthesis / design hypotheses only — NOT a runnable DSL or verified coding pipeline.

## 0. Scope and source policy
This is a purposive coverage map spanning proofs, arithmetic, set cardinality, algebra, statistics, graphs, geometry, topology, inverse problems, MDE, and KRR; it is not every theorem in mathematics, a systematic-review saturation claim, or a certified formal proof library. Open-to-read is not the same as permission to redistribute full PDFs. Source links and original texts remain under the respective authors' licenses. Each registry row records conditions, inverse limits, aliases, a potential falsifier, and source anchors.

## 1. Object and inference ontology
A proposed metamodel: `M=(D,R,O,A,C,T,I,P,E)`, with **domain/types**, **relations**, **operators**, **assumptions**, **constraints**, **theorems**, **inference routes**, **proof obligations**, **evidence/provenance**. This is an original integration proposal, not a formal standard.

Primitive categories should not be conflated: `Entity`, `Scalar`, `Set`, `FiniteSet`, `Cardinal`, `Relation`, `Function`, `Parameter`, `EstimatedParameter`, `Constant`, `RandomVariable`, `Distribution`, `Matrix`, `Graph`, `MetricSpace`, `TopologicalSpace`, `SimplicialComplex`, `Observation`, `ForwardModel`, `InverseQuery`, `ProofClaim`, `EvidenceReceipt`.

Three meanings of 'graph' are separate: discrete adjacency structure, a plotted statistical chart, and the graph of a function. Mathematical *topology* and graph-theoretic *topological sort* are different concepts. Numeric coefficients, statistical effect estimates, tuning hyperparameters, mathematical constants, integration constants, and ontology cardinality restrictions must be different roles, even when notation collides.

## 2. Four classes of reconstruction
1. **Exact algebraic inverse**: solve `F(x)=y`; if `F` is injective on the declared domain and onto the target y, unique solution. Noninjective `x²=9` has `{−3,3}`; output must be a solution set, not an arbitrary scalar.
2. **Linear/optimization inverse**: `y=Ax+ε`. When `A` has full column rank, LS minimizer is unique; noise and small singular values may make it unstable. If rank deficient, many coefficient vectors may give the same fitted values. SVD and regularization quantify/stabilize estimation, not prove ground-truth recovery.
3. **Statistical inverse**: `y~p(y given θ)`, then estimate θ using likelihood, Bayes posterior, or constraints. Report uncertainty, priors/regularizers, diagnostics, and out-of-sample behavior. Predicting `Y|X` is not identifying `Y|do(X)`.
4. **Structural/geometric/topological inverse**: infer feasible graphs/shapes/complexes from partial invariants. Observations determine a class of realizations, sometimes none. A degree sequence can admit multiple nonisomorphic graphs; distances fix coordinates only up to admissible isometries; Betti numbers summarize holes, not exact object geometry.
A fifth, different notion is **bidirectional model update**: lenses permit consistent source/view round trips, but do not invert erased information without retaining source context.

**Well-posedness gate:** existence, uniqueness, and stability must be tested separately. `DETERMINED` vs `UNDERDETERMINED` vs `INCONSISTENT` vs `UNIDENTIFIABLE` vs `ESTIMATED` is a semantic result classification, not just a tool success message.

## 3. Worked boundary cases / negative controls
- `F(x)=x², F(x)=9`: two real roots. Restrict `x≥0` if a unique positive root is required; without the restriction, a unique inverse claim is false.
- Graph degree sequence `(2,2,2,2,2,2)` is consistent both with cycle `C6` and disconnected `C3 ⊔ C3`: exact degree information does not identify the original graph.
- An antiderivative of `2x` is `x²+C`; derivative data alone cannot determine `C`. A boundary value can.
- `y=Ax` with nonzero `ker(A)` admits `x+v` with same output for every `v∈ker(A)`; injectivity is necessary for a unique unregularized inverse.
- Graph-as-one-dimensional-complex: cycle rank `E−V+c`. Filling a triangle as a 2-simplex changes homology; do not silently treat network cycles as unfilled topological holes.
- Two different photos/scene parameter combinations can share projected pixels; image inverse needs priors/multiple views and uncertainty reporting.
- OWL permits unasserted individuals and does not adopt unique-name assumption; missing RDF edge ≠ OWL contradiction. SHACL's constraint validation has different semantics.
- A theorem proved in Lean may be formally correct but prove the wrong user proposition when the model is mistranslated.

## 4. Syntax and search lexicon (code-oriented, non-executable)
`proof`: axiom, assume, premises, theorem, lemma, proposition, entail, implies, iff, forall, exists, exists_unique, witness, contradiction, induction, counterexample, invariant, proof_obligation.
`set/cardinality`: union, intersection, subset, power_set, cardinality, finite, countable, injection, surjection, bijection, minCount, maxCount, exactCardinality, multiplicity, functional_dependency.
`algebra`: factor, expand, gcd, modulo, inverse_mod, roots, rank, nullspace, eigenvalue, singular_value, pseudo_inverse, solve, inverse, transpose, determinant.
`statistics`: coefficient, intercept, beta, alpha, sigma, likelihood, prior, posterior, mean, median, MAD, variance, covariance, correlation, regression, OLS, MLE, kde, confidence_interval, credible_interval, p_value, multiple_testing, FDR, bootstrap, model_diagnostics.
`calculus/optimization`: limit, derivative, differential, gradient, jacobian, hessian, integrand, integral, ode, pde, boundary_condition, initial_condition, Taylor, regularization, least_squares, convex, constraints, KKT, convergence.
`graphs/geometry/topology`: edge, vertex, adjacency, connectivity, strongly_connected, degree_sequence, cycle_basis, laplacian_matrix, spectral_clustering, stochastic_block_model, topological_sort, planar, shortest_path, max_flow, coordinates, transform, affine, isometry, point_in_polygon, metric, topology, open_set, continuity, homeomorphism, simplicial_complex, boundary_operator, homology, Betti, filtration, rips_complex, bottleneck_distance, barcode, persistence.
`MDE/KRR`: metamodel, model_instance, abstract_syntax, concrete_syntax, AST, typed_IR, RDF, OWL, SHACL, Datalog, SMT, rule, shape, entailment, closed_world, open_world, source_map, roundtrip_law, lens_get, lens_put, model_to_model, model_to_text, provenance.
`evaluation`: counterexample, negative_control, held_out, reproducibility, seed, unit, type_check, static_validation, runtime_test, error_budget, falsifier, idempotence, evidence_receipt.

**Caution:** equivalent spelling in code is a search hint, not semantic equivalence. Eg `rank` can mean matrix rank, a ranking position or graph order; `beta` can be a regression parameter, Beta-distribution parameter or Type-II error; `graph` can denote RDF or geometric network; `minCount` is a SHACL constraint, while `ObjectMinCardinality` is an OWL expression.

## 5. Proposed decision/build flow (not an implemented pipeline)
`Natural request → object/type identification → relations and units → forward-model assumptions → observation model → claim regime [deductive / computational / statistical / causal / abductive] → exact/inexact decision → identifiability/feasibility/stability check → operator selection → symbolic/solver/numeric/graph/topology back-end (only where warranted) → negative control → evidence-typed conclusion → optional model transformation/implementation handoff`.

The **decision stage** decides what counts as a solution; the **build stage** decides how to realize/transform a checked model. The former must not be inferred from the existence of a library function.

Suggested result kinds: `PROVED` (formal theorem in specified axioms), `DERIVED` (deductive consequence with proof), `SAT-WITNESS` (satisfying model under declared theory), `ESTIMATED` (model-dependent estimate), `HYPOTHESIS` (abductive explanation), `MULTI-SOLUTION` (set/class of candidates), `UNIDENTIFIABLE`, `INCONSISTENT`, `UNKNOWN`, `UNVERIFIED`. Don't turn `SAT` into a claim of empirical truth or `model-fit` into a causal proof.

## 6. Metamodel invariants / proof obligations
- Type check all operator inputs/outputs and numerical units (`m/s` is not `m`); state coordinate system and reference frame.
- Specify if equality is exact, floating-point tolerance, probabilistic, structural isomorphism, or homotopy equivalence.
- Distinguish `constant mathematical` (π,e), `physical measured` (unit + uncertainty), `parameter fixed`, `parameter estimated` (β), `hyperparameter` (λ), `statistical threshold` (α), `integration constant` (C), and `cardinal/multiplicity`.
- For reverse queries demand domain/range, observation operator, candidate solution class, noise model if any, identifiability/uniqueness criterion, admissible transformations, and falsifier.
- For a theorem, store explicit quantified statement, assumptions, proof reference, conclusion, and forbidden generalization.
- For statistical results, store source data lineage, sampling design, model specification, uncertainty, and holdout diagnostics.
- For KRR use OWL for ontology entailment, SHACL for closed constraint checking over given data graphs, Datalog for rule-derived relations, SMT for satisfiability over supported theories, and Lean for proof objects if proof is the claim. None replaces all others.
- For MDE keep natural-language task, mathematical semantic IR, metamodel constraints, target implementation, and runtime witness distinct. Lens roundtrip laws do not imply full invertibility.

## 7. Mapping to the VibeCode Transducer's actual scope
The installed VibeCode Transducer reference skill describes a 50-method atlas (031–080), mostly **REFERENCE_ONLY**. Narrow local implementations are specified only for Jaccard similarity (034), median absolute deviation (055), and topological ordering (058), plus Python AST parsing, lexical source search, attempt-safe trace logic, and SHA-scoped patch previews. Merely invoking the skill does not run these operations, deploy MCP, or modify a repository.

For a future mathematical DSL, map tasks to target behavior and discriminating oracles rather than invoke operators by topic similarity. Example: a directed dependency graph can route to topo-sort if acyclic; a graph cycle is a falsifier. A set-token Jaccard score may rank donor code for inspection but does not validate behavior; `AC-3`, MinHash, matrix profile, Wasserstein, or persistent homology should remain design candidates until their data requirements and actual executors are satisfied.

**Recommended next research-first artifact** is a type-and-theorem registry (the CSV companion) with high-priority, separately verified proof obligations. This is a literature compilation, not an authorization to edit code.

## 8. Registry — inspectable theorem/operator rows
The companion CSV is the machine-readable discovery index. Each item below is an *index record*, not a verified runtime or formal proof.


### Logic & proof (8)

- **MATH-001 — Modus ponens** (theorem/rule). Expression: `P, P→Q ⊢ Q`. **Gate:** premises established. **Inverse/limit:** deductive consequence, not inverse implication. **Aliases:** `implies,entails,assert`. **Falsifier:** countermodel to invalid converse. Sources: S01,S02,S20.
- **MATH-002 — Universal instantiation** (theorem/rule). Expression: `∀x P(x) ⊢ P(a)`. **Gate:** a in quantified domain. **Inverse/limit:** not P(a)→∀x P(x). **Aliases:** `forall,all,for`. **Falsifier:** single instance not sufficient. Sources: S01,S02,S20.
- **MATH-003 — Existential construction** (theorem/rule). Expression: `P(w) ⊢ ∃x P(x)`. **Gate:** valid witness w. **Inverse/limit:** a witness proves existence. **Aliases:** `exists,witness,any`. **Falsifier:** witness must satisfy property. Sources: S01,S20.
- **MATH-004 — Existence and uniqueness** (theorem/rule). Expression: `∃!x P(x) ≡ ∃x[P(x)∧∀y(P(y)→y=x)]`. **Gate:** same equality/domain. **Inverse/limit:** separate existence from uniqueness. **Aliases:** `exists_unique,unique`. **Falsifier:** at least two satisfying objects defeat uniqueness. Sources: S01,S20.
- **MATH-005 — Proof by contradiction** (theorem/rule). Expression: `¬P ⊢ ⊥ hence P`. **Gate:** classical logic for unrestricted reductio. **Inverse/limit:** contradiction must be genuine. **Aliases:** `contradiction,not,unsat`. **Falsifier:** inconsistent starting axioms invalidate inference-to-world. Sources: S01,S20.
- **MATH-006 — Mathematical induction** (theorem/rule). Expression: `P(0)∧∀n(P(n)→P(n+1)) ⇒ ∀n∈N P(n)`. **Gate:** proper base and inductive step. **Inverse/limit:** general from all inductive steps not finite testing. **Aliases:** `induction,recursive`. **Falsifier:** missing base or noninductive domain. Sources: S01,S02,S20.
- **MATH-007 — Counterexample** (theorem/rule). Expression: `∃x ¬P(x) refutes ∀x P(x)`. **Gate:** counterexample within domain. **Inverse/limit:** one witness defeats universal. **Aliases:** `counterexample,property_test`. **Falsifier:** test must match quantifier domain. Sources: S01,S20.
- **MATH-008 — Equivalence proof** (theorem/rule). Expression: `P↔Q requires P→Q and Q→P`. **Gate:** both directions valid. **Inverse/limit:** not merely one-direction implication. **Aliases:** `iff,eq,refine`. **Falsifier:** converse failure defeats equivalence. Sources: S01,S20.

### Sets & cardinality (7)

- **MATH-009 — Union/intersection/difference** (definition). Expression: `A∪B, A∩B, A\B`. **Gate:** well-defined common universe. **Inverse/limit:** reconstruction from union alone generally nonunique. **Aliases:** `union,intersection,setdiff`. **Falsifier:** noninvertible union. Sources: S01,S02.
- **MATH-010 — Inclusion-exclusion** (theorem). Expression: `card(A∪B)=card(A)+card(B)−card(A∩B)`. **Gate:** finite sets. **Inverse/limit:** overlap inferable given other cardinalities. **Aliases:** `union_len,inclusion_exclusion`. **Falsifier:** infinite case needs cardinal arithmetic. Sources: S01,S02.
- **MATH-011 — Power set** (theorem). Expression: `card(P(A))=2^card(A)`. **Gate:** finite A. **Inverse/limit:** infer finite card(A) from known 2^n. **Aliases:** `powerset,subset`. **Falsifier:** do not use finite formula as real exponent for all cardinals. Sources: S01,S02.
- **MATH-012 — Pigeonhole principle** (theorem). Expression: `n+1 objects in n boxes implies collision`. **Gate:** finite bins. **Inverse/limit:** detect unavoidable noninjective mapping. **Aliases:** `pigeonhole,collision`. **Falsifier:** requires known bin count. Sources: S01,S02.
- **MATH-013 — Schröder–Bernstein** (theorem). Expression: `injections A↪B and B↪A imply bijection A↔B`. **Gate:** two witnessed injections. **Inverse/limit:** cardinal equality but not canonical bijection. **Aliases:** `injective,bijective`. **Falsifier:** injections one way insufficient. Sources: S01,S20.
- **MATH-014 — Cantor diagonal** (theorem). Expression: `card(P(A))>card(A)`. **Gate:** set-theoretic framework. **Inverse/limit:** set cardinal cannot be exhausted by enumeration. **Aliases:** `countable,uncountable`. **Falsifier:** does not calculate size of arbitrary finite samples. Sources: S01.
- **MATH-015 — OWL cardinality constraint** (semantic constraint). Expression: `exactly/min/max n successors in a class`. **Gate:** OWL semantics; distinctness not automatic. **Inverse/limit:** logical entailment not closed-world count check. **Aliases:** `ObjectExactCardinality,sh:minCount`. **Falsifier:** missing triple not always contradiction under OWL. Sources: S15,S16.

### Arithmetic & number theory (7)

- **MATH-016 — Division algorithm** (theorem). Expression: `a=bq+r, 0≤r<abs(b) `. **Gate:** integer a,b with b≠0. **Inverse/limit:** recover quotient and remainder uniquely under convention. **Aliases:** `divmod,mod,floordiv`. **Falsifier:** division by zero. Sources: S02.
- **MATH-017 — Euclid algorithm** (algorithm/theorem). Expression: `gcd(a,b)=gcd(b,a mod b)`. **Gate:** integers, valid remainder. **Inverse/limit:** recover common divisor. **Aliases:** `gcd,euclid`. **Falsifier:** negative convention must be specified. Sources: S02.
- **MATH-018 — Bézout identity** (theorem). Expression: `ax+by=gcd(a,b)`. **Gate:** integers. **Inverse/limit:** compute integer witnesses x,y. **Aliases:** `extended_gcd,egcd`. **Falsifier:** witness verification. Sources: S02.
- **MATH-019 — Prime factorization uniqueness** (theorem). Expression: `n>1 product of primes uniquely up to order`. **Gate:** positive integers. **Inverse/limit:** reverse multiplication to prime factors. **Aliases:** `factorint,prime`. **Falsifier:** not arbitrary real factorization. Sources: S02.
- **MATH-020 — Modular congruence** (definition/theorem). Expression: `a≡b (mod n)`. **Gate:** n positive integer. **Inverse/limit:** inverse only if gcd(a,n)=1. **Aliases:** `mod,mod_inverse`. **Falsifier:** nonunit divisor has no multiplicative inverse. Sources: S02.
- **MATH-021 — Quadratic roots** (algebraic result). Expression: `x²=a gives ±√a (real a>0)`. **Gate:** real domain; sign information absent. **Inverse/limit:** two-valued inverse. **Aliases:** `solveset,roots`. **Falsifier:** do not arbitrarily choose positive root. Sources: S27.
- **MATH-022 — Sequence recurrence** (model law). Expression: `a_{n+1}=F(a_n)`. **Gate:** initial state required. **Inverse/limit:** backward unique only when F injective. **Aliases:** `recurrence,iterate`. **Falsifier:** initial condition absent. Sources: S02.

### Combinatorics (3)

- **MATH-023 — Permutations/combinations** (theorem). Expression: `P(n,k)=n!/(n−k)!, C(n,k)=n!/[k!(n−k)!]`. **Gate:** integers 0≤k≤n. **Inverse/limit:** count arrangements vs selections distinctly. **Aliases:** `permutations,combinations`. **Falsifier:** order sensitivity. Sources: S02.
- **MATH-024 — Binomial theorem** (theorem). Expression: `(a+b)^n=Σ C(n,k)a^{n−k}b^k`. **Gate:** n nonnegative integer. **Inverse/limit:** coefficient extraction exact. **Aliases:** `expand,binomial`. **Falsifier:** avoid nonintegral generalized cases without convergence. Sources: S02.
- **MATH-025 — Generating function** (method). Expression: `G(z)=Σ a_n z^n`. **Gate:** formal series or analytic convergence specified. **Inverse/limit:** recover coefficients formally by coefficient operator. **Aliases:** `series,coeff,genfunc`. **Falsifier:** formal vs numerical confusion. Sources: S02.

### Linear algebra (8)

- **MATH-026 — Matrix dimensions** (type rule). Expression: `A_(m×n) x_(n×1)→b_(m×1)`. **Gate:** inner dimensions agree. **Inverse/limit:** shape check before numerical solving. **Aliases:** `shape,matmul,transpose`. **Falsifier:** dimension mismatch. Sources: S05.
- **MATH-027 — Rank-nullity** (theorem). Expression: `dim ker A+rank A=n`. **Gate:** linear A: R^n→R^m. **Inverse/limit:** nonzero nullspace signals nonuniqueness of inverse. **Aliases:** `matrix_rank,null_space`. **Falsifier:** rank depends on exact vs tolerance semantics. Sources: S05.
- **MATH-028 — Invertible matrix theorem** (theorem). Expression: `square A invertible iff rank(A)=n`. **Gate:** square over field. **Inverse/limit:** unique solution of Ax=b for all b. **Aliases:** `linalg.solve,det`. **Falsifier:** det near zero ill conditioning. Sources: S05.
- **MATH-029 — Least squares** (optimization result). Expression: `argmin norm2(Ax−b)^2`. **Gate:** objective, matrix, residual metric. **Inverse/limit:** estimate x; unique if full column rank. **Aliases:** `lstsq,least_squares`. **Falsifier:** rank deficient may have multiple minimizers. Sources: S05,S06,S26.
- **MATH-030 — SVD** (decomposition). Expression: `A=UΣV*`. **Gate:** finite matrix. **Inverse/limit:** condition number diagnoses inverse sensitivity. **Aliases:** `svd,pinv,cond`. **Falsifier:** small singular values amplify error. Sources: S05,S29.
- **MATH-031 — Spectral theorem** (theorem). Expression: `A=QΛQᵀ for real symmetric A`. **Gate:** real symmetric matrix. **Inverse/limit:** recover modes/eigenvectors up to eigenspace freedoms. **Aliases:** `eigh,spectral`. **Falsifier:** nonsymmetric matrix not covered by stated form. Sources: S05.
- **MATH-032 — Projection** (theorem). Expression: `P²=P`. **Gate:** linear projection on vector space. **Inverse/limit:** projection loses null directions. **Aliases:** `project,orthogonal_projection`. **Falsifier:** cannot reconstruct discarded component. Sources: S05.
- **MATH-033 — Jacobian rank local diagnostic** (diagnostic). Expression: `J_F(x) sensitivity of outputs to inputs`. **Gate:** smooth forward map; local claims only. **Inverse/limit:** rank deficiency suggests local first-order nonidentifiability. **Aliases:** `jacobian,rank`. **Falsifier:** full rank does not give global uniqueness. Sources: S10,S26.

### Analysis & calculus (10)

- **MATH-034 — Limit and continuity** (definition). Expression: `lim_{x→a}f(x)=f(a)`. **Gate:** function/domain; limit exists. **Inverse/limit:** needed for differentiation/integration theorems. **Aliases:** `limit,continuous`. **Falsifier:** jump discontinuity. Sources: S04.
- **MATH-035 — Derivative** (definition). Expression: `f'(x)=lim_h [f(x+h)−f(x)]/h`. **Gate:** limit exists. **Inverse/limit:** recover local rate, not unique original function. **Aliases:** `diff,derivative`. **Falsifier:** derivative loses additive constant. Sources: S04.
- **MATH-036 — Chain rule** (theorem). Expression: `(f∘g)'=(f'∘g)g'`. **Gate:** differentiability conditions. **Inverse/limit:** compose local sensitivities. **Aliases:** `diff,chain_rule`. **Falsifier:** nondifferentiable join. Sources: S04.
- **MATH-037 — Fundamental theorem of calculus** (theorem). Expression: `d/dx ∫_a^x f(t)dt=f(x)`. **Gate:** continuity on interval for stated form. **Inverse/limit:** inverse up to integration constant under antiderivative. **Aliases:** `integrate,diff`. **Falsifier:** derivative of F+C identical. Sources: S04.
- **MATH-038 — Mean value theorem** (theorem). Expression: `f(b)−f(a)=f'(c)(b−a)`. **Gate:** continuous [a,b], differentiable (a,b). **Inverse/limit:** connect average and local change. **Aliases:** `derivative,mean_value`. **Falsifier:** fails for discontinuous case. Sources: S04.
- **MATH-039 — Taylor theorem** (theorem). Expression: `f(x)=Σ_{k=0}^n f^(k)(a)(x−a)^k/k!+R_n`. **Gate:** regularity and remainder control. **Inverse/limit:** approximate local reconstruction with error bound. **Aliases:** `series,taylor`. **Falsifier:** truncation not equality in general. Sources: S04.
- **MATH-040 — Inverse function theorem** (theorem). Expression: `det Df(x0)≠0 ⇒ local C¹ inverse`. **Gate:** f C¹ from R^n to R^n near x0. **Inverse/limit:** local not global inverse. **Aliases:** `jacobian,det`. **Falsifier:** f(x)=x² on R has local but not global inverses for x≠0. Sources: S33.
- **MATH-041 — Antiderivative arbitrary constant** (theorem). Expression: `∫ f'(x)dx=f(x)+C`. **Gate:** connected interval; differentiable f. **Inverse/limit:** must provide boundary/initial condition for C. **Aliases:** `integrate,constant_of_integration`. **Falsifier:** C unconstrained. Sources: S04,S27.
- **MATH-042 — ODE initial-value solution** (theorem/method). Expression: `y'=F(t,y), y(t0)=y0`. **Gate:** existence/uniqueness conditions e.g. local Lipschitz in y. **Inverse/limit:** trajectory reconstruction conditional on initial state. **Aliases:** `dsolve,solve_ivp`. **Falsifier:** without initial state many trajectories. Sources: S04.
- **MATH-043 — Finite difference** (definition). Expression: `Δf(n)=f(n+1)−f(n)`. **Gate:** discrete indexed sequence. **Inverse/limit:** inverse indefinite summation up to initial value. **Aliases:** `diff,discrete_diff,cumsum`. **Falsifier:** missing starting term. Sources: S02.

### Probability & statistics (14)

- **MATH-044 — Probability axioms** (axioms). Expression: `P(Ω)=1, P(A)≥0, σ-additive`. **Gate:** probability measure. **Inverse/limit:** constraints on valid probability models. **Aliases:** `probability,normalize`. **Falsifier:** negative probability invalid. Sources: S03.
- **MATH-045 — Conditional probability** (definition). Expression: `P(A given B)=P(A∩B)/P(B)`. **Gate:** P(B)>0. **Inverse/limit:** conditioning not cause inference. **Aliases:** `conditional,likelihood`. **Falsifier:** zero-prob event needs separate framework. Sources: S03.
- **MATH-046 — Bayes theorem** (theorem/method). Expression: `P(θ given y)∝P(y given θ)P(θ)`. **Gate:** proper prior/likelihood and finite positive evidence. **Inverse/limit:** posterior rather than single definitive inverse. **Aliases:** `posterior,bayes,mcmc`. **Falsifier:** prior sensitivity. Sources: S03,S11.
- **MATH-047 — Expectation** (definition). Expression: `E[X]=∫ x dP(x)`. **Gate:** integrability. **Inverse/limit:** mean does not reconstruct distribution. **Aliases:** `expectation,mean`. **Falsifier:** different distributions may share mean. Sources: S03.
- **MATH-048 — Variance/covariance** (definition). Expression: `Var(X)=E[(X−μ)²]`. **Gate:** finite second moment. **Inverse/limit:** covariance not sufficient for dependence structure. **Aliases:** `var,cov,corr`. **Falsifier:** uncorrelated need not imply independent. Sources: S03.
- **MATH-049 — Law of large numbers** (theorem). Expression: `sample average → expectation (conditions)`. **Gate:** i.i.d. integrable for standard strong form. **Inverse/limit:** sample convergence not per-sample certainty. **Aliases:** `mean,lln`. **Falsifier:** dependent/heavy-tail issues. Sources: S03.
- **MATH-050 — Central limit theorem** (theorem). Expression: `standardized mean ⇒ N(0,1)`. **Gate:** i.i.d. finite nonzero variance standard form. **Inverse/limit:** sampling uncertainty approximation. **Aliases:** `clt,normal,standard_error`. **Falsifier:** small n / infinite variance issue. Sources: S03.
- **MATH-051 — Likelihood/MLE** (estimation method). Expression: `θhat=argmaxθ p(y given θ)`. **Gate:** parametric model identifiable for stronger claims. **Inverse/limit:** parameter estimate with sampling uncertainty. **Aliases:** `fit,mle,loglike`. **Falsifier:** model misspecification. Sources: S03,S06.
- **MATH-052 — Linear regression slope** (estimator). Expression: `βhat_1=Σ(x−xbar)(y−ybar)/Σ(x−xbar)²`. **Gate:** nonzero x variance. **Inverse/limit:** recover fitted coefficient not causal effect. **Aliases:** `linregress,coef`. **Falsifier:** zero denominator. Sources: S06.
- **MATH-053 — Gauss–Markov BLUE** (theorem). Expression: `OLS BLUE given linear-model exogeneity homoscedastic uncorrelated errors and full rank`. **Gate:** classical Gauss-Markov assumptions. **Inverse/limit:** optimality limited to linear unbiased class. **Aliases:** `ols,standard_errors`. **Falsifier:** no normality needed for BLUE. Sources: S06.
- **MATH-054 — Confidence interval coverage** (statistical guarantee). Expression: `Pθ(θ∈CI(Y))=1−α for exact procedure`. **Gate:** specified sampling distribution and procedure. **Inverse/limit:** interval not posterior probability by default. **Aliases:** `confidence_interval,bootstrap`. **Falsifier:** posthoc probability misinterpretation. Sources: S03.
- **MATH-055 — Hypothesis test** (inference method). Expression: `H0 vs H1 and test statistic`. **Gate:** test assumptions/α predeclared. **Inverse/limit:** reject/fail reject not prove true hypothesis. **Aliases:** `ttest,pvalue,fdr`. **Falsifier:** multiple testing, selection bias. Sources: S03.
- **MATH-056 — Kernel density estimation** (estimator). Expression: `fhat_h(x)=Σ_i K((x−x_i)/h)/(n h)`. **Gate:** kernel and bandwidth, sample dimension. **Inverse/limit:** smooth estimate loses pointwise sample identity and can smear modes. **Aliases:** `gaussian_kde,kde,bandwidth`. **Falsifier:** bandwidth changes peak structure. Sources: S37.
- **MATH-057 — Regularization** (optimization method). Expression: `argmin loss(θ)+λR(θ)`. **Gate:** loss, prior penalty and λ declared. **Inverse/limit:** biased but stabilized inverse. **Aliases:** `ridge,lasso,regularize`. **Falsifier:** regularizer affects solution. Sources: S10,S11,S26.

### Graphs & networks (13)

- **MATH-058 — Graph definition** (definition). Expression: `G=(V,E) with edge semantics`. **Gate:** directed/undirected, multigraph, weights declared. **Inverse/limit:** observations rarely determine unique G. **Aliases:** `Graph,DiGraph`. **Falsifier:** graph flavor mismatch. Sources: S02,S23.
- **MATH-059 — Handshaking lemma** (theorem). Expression: `Σ_v deg(v)=2 card(E) `. **Gate:** finite undirected graph, loops counted twice. **Inverse/limit:** recover number of edges from degrees. **Aliases:** `degree,size`. **Falsifier:** not enough to recover adjacency. Sources: S02.
- **MATH-060 — Connected components** (algorithm/definition). Expression: `V partition into maximally connected subsets`. **Gate:** undirected graph. **Inverse/limit:** infer β0, not full shape. **Aliases:** `connected_components,bfs,dfs`. **Falsifier:** directed case needs weak/strong notion. Sources: S23.
- **MATH-061 — DAG topological order** (theorem/algorithm). Expression: `u→v ⇒ u precedes v`. **Gate:** directed acyclic graph. **Inverse/limit:** detect impossible dependency ordering via cycles. **Aliases:** `topological_sort,is_dag`. **Falsifier:** cycle defeats ordering. Sources: S23.
- **MATH-062 — Shortest path** (algorithm). Expression: `d(u,v)=min path length`. **Gate:** nonnegative weights for Dijkstra. **Inverse/limit:** metric summary loses original edges. **Aliases:** `shortest_path,dijkstra`. **Falsifier:** negative edges invalidate Dijkstra guarantee. Sources: S23.
- **MATH-063 — Erdős–Gallai/Havel–Hakimi** (theorem/algorithm). Expression: `degree-sequence realizability`. **Gate:** nonincreasing nonnegative integer degree sequence. **Inverse/limit:** construct possible graph(s), not unique original. **Aliases:** `is_graphical,havel_hakimi_graph`. **Falsifier:** multiple nonisomorphic realizations. Sources: S24.
- **MATH-064 — Graph Laplacian** (operator). Expression: `L=D−A`. **Gate:** finite weighted undirected graph with compatible degrees. **Inverse/limit:** spectrum summarizes graph but not unique adjacency. **Aliases:** `laplacian_matrix,laplacian_spectrum`. **Falsifier:** different graphs can share spectral information. Sources: S34.
- **MATH-065 — Spectral graph clustering** (estimation method). Expression: `eigenvectors of normalized graph Laplacian → grouping`. **Gate:** affinity weights, normalization and number of clusters fixed. **Inverse/limit:** cluster assignment is model-dependent not true ontology. **Aliases:** `spectral_clustering,normalized_laplacian`. **Falsifier:** different affinities produce different clusters. Sources: S35.
- **MATH-066 — Erdos-Renyi random graph** (probabilistic model). Expression: `P(edge uv)=p independently for each pair in G(n,p)`. **Gate:** finite n and p∈[0,1], independent edges. **Inverse/limit:** infer p statistically from observed graph, not unique generative history. **Aliases:** `erdos_renyi_graph,gnp_random_graph`. **Falsifier:** fit does not prove true generator. Sources: S36.
- **MATH-067 — Stochastic block model** (probabilistic model). Expression: `P(edge uv)=B[z_u,z_v] under conditionally independent edges`. **Gate:** membership classes and edge probability matrix. **Inverse/limit:** community labels only identifiable up to permutation under suitable conditions. **Aliases:** `stochastic_block_model,community`. **Falsifier:** nonidentifiability when blocks indistinguishable. Sources: S36.
- **MATH-068 — Graph Betti number** (theorem). Expression: `β1=card(E)−card(V)+c`. **Gate:** finite undirected graph seen as 1-complex. **Inverse/limit:** counts independent cycles not positions. **Aliases:** `cycle_basis,cycle_rank`. **Falsifier:** not valid unchanged after filling faces. Sources: S07,S08.
- **MATH-069 — Graph isomorphism** (definition/problem). Expression: `G≈H preserving adjacency bijection`. **Gate:** same directed/weighted semantics. **Inverse/limit:** recover only equivalence class of relabelings. **Aliases:** `is_isomorphic`. **Falsifier:** degree sequence equality insufficient. Sources: S23.
- **MATH-070 — Min cut/max flow** (theorem). Expression: `max_flow=min_cut`. **Gate:** directed capacitated flow network. **Inverse/limit:** diagnose bottleneck capacity. **Aliases:** `maximum_flow,minimum_cut`. **Falsifier:** flow conservation/capacity required. Sources: S02,S23.

### Geometry (6)

- **MATH-071 — Euclidean distance** (definition). Expression: `d(x,y)=sqrt(Σ(x_i−y_i)²)`. **Gate:** metric embedding and units fixed. **Inverse/limit:** coordinates only up to isometry given distances. **Aliases:** `distance,pdist`. **Falsifier:** rigid transforms preserve distances. Sources: S04.
- **MATH-072 — Affine transformation** (theorem). Expression: `y=Ax+b`. **Gate:** dimension/rank constraints. **Inverse/limit:** inverse iff A nonsingular square (global affine case). **Aliases:** `affine,transform`. **Falsifier:** rank-loss projection not invertible. Sources: S05.
- **MATH-073 — Rigid transformation** (definition). Expression: `x' = Rx+t, RᵀR=I`. **Gate:** Euclidean metric; orientation choice. **Inverse/limit:** coordinates ambiguous up to isometries. **Aliases:** `rotation,translation,procrustes`. **Falsifier:** reflection vs proper rotation must be distinguished. Sources: S05.
- **MATH-074 — Point in polygon** (geometric predicate). Expression: `inside/boundary/outside predicate`. **Gate:** valid polygon and boundary convention. **Inverse/limit:** categorical observation cannot uniquely recover polygon. **Aliases:** `contains,within,intersects`. **Falsifier:** boundary included/excluded. Sources: S31.
- **MATH-075 — Distance geometry reconstruction** (inverse geometry). Expression: `pairwise distances d_ij constrain point configurations`. **Gate:** metric consistency and embedding dimension. **Inverse/limit:** realizations at best up to Euclidean isometry, some distance sets infeasible. **Aliases:** `distance_matrix,mds,trilateration`. **Falsifier:** reflection or rotation yields equal distances. Sources: S05.
- **MATH-076 — Triangulation** (algorithm). Expression: `partition region into triangles`. **Gate:** valid planar topology/geometry. **Inverse/limit:** many triangulations can realize same shape. **Aliases:** `triangulate,delaunay`. **Falsifier:** Delaunay degeneracy/cocircular points. Sources: S32.

### Topology (11)

- **MATH-077 — Topological space** (definition). Expression: `(X,τ), τ closed under arbitrary unions and finite intersections`. **Gate:** valid topology τ. **Inverse/limit:** not inferred from finite points without modelling rule. **Aliases:** `open_sets,topology`. **Falsifier:** a fully specified metric canonically induces a topology; a finite sample does not fix the unknown continuum topology. Sources: S07.
- **MATH-078 — Continuity (topological)** (definition). Expression: `f^−1(U) open for each open U`. **Gate:** topological spaces. **Inverse/limit:** continuous map need not be invertible. **Aliases:** `continuous,preimage`. **Falsifier:** inverse continuity not guaranteed. Sources: S07.
- **MATH-079 — Homeomorphism** (definition). Expression: `continuous bijection with continuous inverse`. **Gate:** spaces and maps stated. **Inverse/limit:** invariants only under homeomorphisms. **Aliases:** `homeomorphism`. **Falsifier:** continuity/bijection alone not enough in arbitrary spaces. Sources: S07.
- **MATH-080 — Simplicial complex** (definition). Expression: `faces of simplex must also be present`. **Gate:** downward closed face collection. **Inverse/limit:** graph to filled complex is extra modelling decision. **Aliases:** `simplex,clique_complex`. **Falsifier:** missing faces invalidate complex. Sources: S25.
- **MATH-081 — Boundary operator** (theorem). Expression: `∂_k: C_k→C_(k−1), ∂²=0`. **Gate:** oriented chain complex. **Inverse/limit:** cycles modulo boundaries. **Aliases:** `boundary_matrix`. **Falsifier:** orientation signs/mod field. Sources: S07,S25.
- **MATH-082 — Betti numbers** (invariant). Expression: `β_k=dim H_k`. **Gate:** finite-dimensional homology over field for rank. **Inverse/limit:** topological features, not unique geometry. **Aliases:** `betti_numbers,homology`. **Falsifier:** same β vector can arise from different spaces. Sources: S07,S09.
- **MATH-083 — Euler–Poincaré** (theorem). Expression: `χ=Σ_k (−1)^k n_k=Σ_k (−1)^k β_k`. **Gate:** finite simplicial complex. **Inverse/limit:** summary invariant, not full inverse. **Aliases:** `euler_characteristic`. **Falsifier:** χ equality does not imply homeomorphism. Sources: S07,S08.
- **MATH-084 — Vietoris-Rips complex** (construction). Expression: `simplex σ enters at scale r when all pairwise distances ≤r`. **Gate:** finite metric data and scale convention. **Inverse/limit:** sample topology depends on threshold and noise. **Aliases:** `rips_complex,filtration`. **Falsifier:** proximity graph alone does not entail filled simplices without rule. Sources: S09,S25.
- **MATH-085 — Persistence stability** (theorem). Expression: `small admissible filtration perturbations give bounded bottleneck change under theorem assumptions`. **Gate:** tame/q-tame persistence with appropriate interleaving assumptions. **Inverse/limit:** stable summary does not determine unique geometry. **Aliases:** `bottleneck_distance,interleaving`. **Falsifier:** stability is not inverse identifiability. Sources: S09.
- **MATH-086 — Persistent homology** (method). Expression: `filtration K_a⊆K_b for a≤b`. **Gate:** nested complexes and field coefficients. **Inverse/limit:** birth/death of features across scales. **Aliases:** `rips,filtration,persistence`. **Falsifier:** filtration choice materially changes features. Sources: S09,S25.
- **MATH-087 — Homotopy equivalence** (definition). Expression: `maps f,g compositions homotopic to identities`. **Gate:** spaces and homotopies. **Inverse/limit:** homotopy invariants not precise metric shape. **Aliases:** `homotopy,fundamental_group`. **Falsifier:** homology equality does not imply homotopy equivalence. Sources: S07.

### Inverse & decision (4)

- **MATH-088 — Hadamard well-posedness** (criterion). Expression: `existence + uniqueness + continuous dependence`. **Gate:** forward map observation space declared. **Inverse/limit:** failure requires regularization/candidate sets. **Aliases:** `identifiability,stability`. **Falsifier:** invertible yet ill-conditioned. Sources: S10,S11.
- **MATH-089 — Inverse rendering ambiguity** (empirical problem). Expression: `pixels←geometry, material, lighting`. **Gate:** forward renderer + images + priors. **Inverse/limit:** recovery nonunique across compensating variables. **Aliases:** `inverse_render,differentiable_render`. **Falsifier:** multiple scenes same image. Sources: S30.
- **MATH-090 — Causal identification** (framework). Expression: `P(Y given do(X)) not identical generally to P(Y given X)`. **Gate:** SCM assumptions, adjustment conditions. **Inverse/limit:** cannot infer interventions from correlation alone. **Aliases:** `causal_graph,do_calculus`. **Falsifier:** confounding counterexample. Sources: S12.
- **MATH-091 — Abductive model selection** (inference pattern). Expression: `select explanatory hypothesis from candidate models`. **Gate:** candidate universe/prior/criteria. **Inverse/limit:** conjectural inference, not logical proof. **Aliases:** `abduction,model_select`. **Falsifier:** best of considered set may still be false. Sources: S28.

### Model engineering & KRR (8)

- **MATH-092 — RDF triple** (standard). Expression: `(subject,predicate,object)`. **Gate:** RDF term types. **Inverse/limit:** graph of assertions, not numeric graph automatically. **Aliases:** `rdflib,triple,iri`. **Falsifier:** RDF absence not negative fact by default. Sources: S14.
- **MATH-093 — OWL entailment** (standard). Expression: `class/property axioms + DL consequence`. **Gate:** ontology profile and semantics. **Inverse/limit:** not closed-world validation. **Aliases:** `reasoner,entailment`. **Falsifier:** distinct names not automatically distinct individuals. Sources: S15.
- **MATH-094 — SHACL validation** (standard). Expression: `data graph ⊨ shape constraints`. **Gate:** declared shape/data graphs. **Inverse/limit:** validates graph against explicit constraints. **Aliases:** `shacl,sh_min_count`. **Falsifier:** validation result is not theorem about physical world. Sources: S16.
- **MATH-095 — Datalog recursion** (language method). Expression: `path(x,z) :- edge(x,y),path(y,z)`. **Gate:** grounded typed relations, fixed semantics. **Inverse/limit:** derive transitive consequences from facts. **Aliases:** `souffle,datalog,rule`. **Falsifier:** unsafe ungrounded variables. Sources: S18.
- **MATH-096 — SMT satisfiability** (solver semantics). Expression: `SAT/UNSAT/UNKNOWN in selected theory`. **Gate:** logic fragment and solver assumptions. **Inverse/limit:** SAT witness ≠ independent theorem unless checked. **Aliases:** `smt,assert,check_sat`. **Falsifier:** UNKNOWN or timeout not UNSAT. Sources: S19.
- **MATH-097 — Lens round trips** (transformation laws). Expression: `get(put(s,v))=v; put(s,get(s))=s`. **Gate:** lawful source-view transformations. **Inverse/limit:** update back to source not inverse of information loss. **Aliases:** `get,put,lens`. **Falsifier:** transformation lacking roundtrip tests. Sources: S17.
- **MATH-098 — Model/metamodel separation** (MDE principle). Expression: `instance conforms to declared schema`. **Gate:** typed metamodel version. **Inverse/limit:** source model→IR→target model. **Aliases:** `ecore,metamodel,xtext`. **Falsifier:** syntax acceptance ≠ semantic correctness. Sources: S13,S21,S22.
- **MATH-099 — Formal proof assistant** (verification mechanism). Expression: `theorem statement checked against kernel`. **Gate:** valid axioms/library and type-checked proof term. **Inverse/limit:** formal proof only of encoded proposition. **Aliases:** `lean,exact,rw,apply,induction`. **Falsifier:** incorrect formalization may still be proved. Sources: S20.

## 9. Public source set (accessible-to-read, rights vary)

- [S01] Hammack, R. (2025 revision 3.4). Book of Proof. https://richardhammack.github.io/BookOfProof/
- [S02] Lehman, E., Leighton, F. T., & Meyer, A. R. (2015). Mathematics for Computer Science. MIT OCW. https://www.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook_pdf/
- [S03] Illowsky, B., & Dean, S. (2023). Introductory Statistics 2e. OpenStax. https://openstax.org/books/introductory-statistics-2e/pages/preface
- [S04] OpenStax. (2016). Calculus, Volumes 1–3. https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus
- [S05] MIT OCW. (2010). 18.06 Linear Algebra (course). https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/
- [S06] Pennsylvania State University. STAT 501: Regression Methods. https://online.stat.psu.edu/statprogram/stat501
- [S07] Hatcher, A. (2002; corrected electronic version). Algebraic Topology. https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
- [S08] Ghrist, R. (2014). Elementary Applied Topology (free personal-use chapters). https://www2.math.upenn.edu/~ghrist/notes.html
- [S09] Chazal, F., & Michel, B. (2021). An Introduction to Topological Data Analysis. Frontiers in AI. https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.667963/full
- [S10] Springer open chapter. Inverse Problems: well-posedness and regularization. https://link.springer.com/chapter/10.1007/978-3-030-34413-9_5
- [S11] Stuart, A. M. (2010). Inverse Problems: A Bayesian Perspective (repository manuscript). https://authors.library.caltech.edu/records/fk9j9-5tq15
- [S12] Pearl, J. (2010). Causal Inference. Proceedings of Machine Learning Research. https://proceedings.mlr.press/v6/pearl10a
- [S13] Object Management Group. Model-Driven Architecture specifications. https://www.omg.org/mda/specs.htm
- [S14] W3C. (2014). RDF 1.1 Concepts and Abstract Syntax. https://www.w3.org/TR/rdf11-concepts/
- [S15] W3C. (2012). OWL 2 Web Ontology Language Primer (second edition). https://www.w3.org/TR/owl-primer/
- [S16] W3C. (2017). Shapes Constraint Language (SHACL). https://www.w3.org/TR/shacl/
- [S17] Foster, J. N., et al. (2007). Combinators for Bidirectional Tree Transformations. https://hal.science/inria-00484971/
- [S18] Soufflé. Datalog language and rules. https://souffle-lang.org/datalog-language
- [S19] SMT-LIB initiative. Language and background theories. https://smt-lib.org/language.shtml
- [S20] Avigad, J., & Massot, P. Mathematics in Lean. https://avigad.github.io/mathematics_in_lean/
- [S21] Eclipse Xtext. The Grammar Language and runtime validation. https://eclipse.dev/Xtext/documentation/301_grammarlanguage.html
- [S22] Eclipse Modeling Framework. Ecore metamodel. https://eclipse.dev/emf/
- [S23] NetworkX. Algorithm reference. https://networkx.org/documentation/stable/reference/algorithms/index.html
- [S24] Sage Math. Degree sequences: Erdős–Gallai and Havel–Hakimi. https://sporadic.stanford.edu/reference/combinat/sage/combinat/degree_sequences.html
- [S25] GUDHI. Persistent Cohomology and filtered complexes. https://pages.saclay.inria.fr/vincent.rouvreau/gudhi/doxygen1.9.3/group__persistent__cohomology.html
- [S26] SciPy. Least-squares and optimization tutorial. https://docs.scipy.org/doc/scipy/tutorial/optimize.html
- [S27] SymPy. Solvers and solution sets. https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html
- [S28] Stanford Encyclopedia of Philosophy. (2025). Abduction. https://plato.stanford.edu/entries/abduction/
- [S29] The Matrix Cookbook. (Petersen & Pedersen, 2012). https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
- [S30] Kouros et al. (2024). Ambiguity in Neural Inverse Rendering. CVPRW. https://openaccess.thecvf.com/content/CVPR2024W/NRI/html/Kouros_Unveiling_the_Ambiguity_in_Neural_Inverse_Rendering_A_Parameter_Compensation_CVPRW_2024_paper.html
- [S31] Shapely developers. (2026). Geometric predicates. https://shapely.readthedocs.io/en/latest/predicates.html
- [S32] SciPy. scipy.spatial.Delaunay documentation. https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html
- [S33] University of Toronto. Transformations and the Inverse Function Theorem. https://www.math.utoronto.ca/courses/mat237y1/20199/notes/Chapter3/S3.3.html
- [S34] NetworkX. Graph linear algebra and Laplacian matrices. https://networkx.org/documentation/stable/reference/linalg.html
- [S35] Scikit-learn. Spectral clustering. https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html
- [S36] NetworkX. Random graph generators. https://networkx.org/documentation/stable/reference/generators.html
- [S37] SciPy. Gaussian kernel density estimation. https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html

## 10. Evidence and completeness audit
**Source coverage:** authoritative textbook/course materials for proof/discrete/math/stats; original free online topology text; academic inverse-problem and TDA literature; official standards/specifications for MDE/KRR; official code-library documentation. **Not covered comprehensively:** functional analysis, measure-theoretic statistics, stochastic processes, category/topos theory, statistical geometry beyond sampled points, formal semantics of a proposed grammar, numerical performance benchmarks, security threat modelling, verified solver integrations, every theorem or every VibeCode registry method. **Validation status:** theoretical checks and hand-authored counterexamples only; no DSL parser, executable math backend, theorem checker, KRR store, MCP server, GitHub project, or runtime build executed.
