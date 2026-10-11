# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 425

PROBLEMS
399
Chernoff–Stein lemma. The best achievable error exponent βϵ
n if
αn ≤ϵ:
βϵ
n =
min
An ⊆Xn
αn < ϵ
βn,
(11.306)
lim
n→∞
1
n log βϵ
n = −D(P1||P2).
(11.307)
Chernoff information. The best achievable exponent for a Bayesian
probability of error is
D∗= D(Pλ∗||P1) = D(Pλ∗||P2),
(11.308)
where
Pλ =
P λ
1 (x)P 1−λ
2
(x)

a∈X P λ
1 (a)P 1−λ
2
(a)
(11.309)
with λ = λ∗chosen so that
D(Pλ||P1) = D(Pλ||P2).
(11.310)
Fisher information
J(θ) = Eθ
 ∂
∂θ ln f (x; θ)
2
.
(11.311)
Cram´er–Rao inequality. For any unbiased estimator T of θ,
Eθ(T (X) −θ)2 = var(T ) ≥
1
J(θ).
(11.312)
PROBLEMS
11.1
Chernoff–Stein lemma.
Consider the two-hypothesis test
H1 : f = f1
vs.
H2 : f = f2.
Find D(f1 ∥f2) if


## PDF page 426

400
INFORMATION THEORY AND STATISTICS
(a) fi(x) = N(0, σ 2
i ), i = 1, 2.
(b) fi(x) = λie−λix, x ≥0, i = 1, 2.
(c) f1(x) is the uniform density over the interval [0, 1] and f2(x)
is the uniform density over [a, a + 1]. Assume that 0 < a < 1.
(d) f1 corresponds to a fair coin and f2 corresponds to a two-
headed coin.
11.2
Relation between D(P ∥Q) and chi-square.
Show that the χ2
statistic
χ2 = x
(P (x) −Q(x))2
Q(x)
is (twice) the ﬁrst term in the Taylor series expansion of D(P ∥
Q) about Q. Thus, D(P ∥Q) = 1
2χ2 + · · · . [Suggestion: Write
P
Q = 1 + P−Q
Q
and expand the log.]
11.3
Error exponent for universal codes.
A universal source code of
rate R achieves a probability of error P (n)
e
.= e−nD(P ∗∥Q), where
Q is the true distribution and P ∗achieves min D(P ∥Q) over all
P such that H(P ) ≥R.
(a) Find P ∗in terms of Q and R.
(b) Now let X be binary. Find the region of source probabili-
ties Q(x), x ∈{0, 1}, for which rate R is sufﬁcient for the
universal source code to achieve P (n)
e
→0.
11.4
Sequential projection.
We wish to show that projecting Q onto
P1 and then projecting the projection ˆQ onto P1
 P2 is the same
as projecting Q directly onto P1
 P2. Let P1 be the set of prob-
ability mass functions on X satisfying

x
p(x) = 1,
(11.313)

x
p(x)hi(x) ≥αi,
i = 1, 2, . . . , r.
(11.314)
Let P2 be the set of probability mass functions on X satisfying

x
p(x) = 1,
(11.315)

x
p(x)gj(x) ≥βj,
j = 1, 2, . . . , s.
(11.316)


## PDF page 427

PROBLEMS
401
Suppose that Q ̸∈P1
 P2. Let P ∗minimize D(P ∥Q) over all
P ∈P1. Let R∗minimize D(R ∥Q) over all R ∈P1
 P2. Argue
that R∗minimizes D(R ∥P ∗) over all R ∈P1
 P2.
11.5
Counting.
Let X = {1, 2, . . . , m}. Show that the number of se-
quences xn ∈Xn satisfying
1
n
n
i=1 g(xi) ≥α is approximately
equal to 2nH ∗, to ﬁrst order in the exponent, for n sufﬁciently large,
where
H ∗=
max
P:m
i=1 P(i)g(i)≥α H(P ).
(11.317)
11.6
Biased estimates may be better.
Consider the problem of esti-
mating µ and σ 2 from n samples of data drawn i.i.d. from a
N(µ, σ 2) distribution.
(a) Show that Xn is an unbiased estimator of µ.
(b) Show that the estimator
S2
n = 1
n
n

i=1
(Xi −Xn)2
(11.318)
is a biased estimator of σ 2 and the estimator
S2
n−1 =
1
n −1
n

i=1
(Xi −Xn)2
(11.319)
is unbiased.
(c) Show that S2
n has a lower mean-squared error than that of
S2
n−1. This illustrates the idea that a biased estimator may be
“better” than an unbiased estimator.
11.7
Fisher information and relative entropy.
Show for a parametric
family {pθ(x)} that
lim
θ′→θ
1
(θ −θ′)2 D(pθ||pθ′) =
1
ln 4J(θ).
(11.320)
11.8
Examples of Fisher information.
The Fisher information J()
for the family fθ(x), θ ∈R is deﬁned by
J(θ) = Eθ
∂fθ(X)/∂θ
fθ(X)
2
=
 (f
′
θ)2
fθ
.
Find the Fisher information for the following families:


## PDF page 428

402
INFORMATION THEORY AND STATISTICS
(a) fθ(x) = N(0, θ) =
1
√
2πθ e−x2
2θ
(b) fθ(x) = θe−θx, x ≥0
(c) What is the Cram`er–Rao lower bound on Eθ( ˆθ(X) −θ)2,
where ˆθ(X) is an unbiased estimator of θ for parts (a) and
(b)?
11.9
Two conditionally independent looks double the Fisher informa-
tion.
Let gθ(x1, x2) = fθ(x1)fθ(x2). Show that Jg(θ) = 2Jf (θ).
11.10
Joint distributions and product distributions.
Consider a joint
distribution Q(x, y) with marginals Q(x) and Q(y). Let E be
the set of types that look jointly typical with respect to Q:
E = {P (x, y) : −

x,y
P (x, y) log Q(x) −H(X) = 0,
−

x,y
P (x, y) log Q(y) −H(Y) = 0,
−

x,y
P (x, y) log Q(x, y)
−H(X, Y) = 0}.
(11.321)
(a) Let Q0(x, y) be another distribution on X × Y. Argue
that the distribution P ∗in E that is closest to Q0 is of the
form
P ∗(x, y) = Q0(x, y)eλ0+λ1 log Q(x)+λ2 log Q(y)+λ3 log Q(x,y),
(11.322)
where λ0, λ1, λ2, and λ3 are chosen to satisfy the constraints.
Argue that this distribution is unique.
(b) Now let Q0(x, y) = Q(x)Q(y). Verify that Q(x, y) is of the
form (11.322) and satisﬁes the constraints. Thus, P ∗(x, y) =
Q(x, y) (i.e., the distribution in E closest to the product dis-
tribution is the joint distribution).
11.11
Cram´er–Rao inequality with a bias term.
Let X ∼f (x; θ) and
let T (X) be an estimator for θ. Let bT (θ) = EθT −θ be the bias
of the estimator. Show that
E(T −θ)2 ≥[1 + b′
T (θ)]2
J(θ)
+ b2
T (θ).
(11.323)


## PDF page 429

PROBLEMS
403
11.12
Hypothesis testing.
Let X1, X2, . . . , Xn be i.i.d. ∼p(x). Con-
sider the hypothesis test H1 : p = p1 vs. H2 : p = p2 . Let
p1(x) =



1
2,
x = −1
1
4,
x = 0
1
4,
x = 1
and
p2(x) =



1
4,
x = −1
1
4,
x = 0
1
2,
x = 1.
Find the error exponent for Pr{Decide H2|H1 true} in the best
hypothesis test of H1 vs. H2 subject to Pr{Decide H1|H2 true}
≤1
2.
11.13
Sanov’s theorem.
Prove a simple version of Sanov’s theorem for
Bernoulli(q) random variables.
Let the proportion of 1’s in the sequence X1, X2, . . . , Xn be
Xn = 1
n
n

i=1
Xi.
(11.324)
By the law of large numbers, we would expect Xn to be close
to q for large n. Sanov’s theorem deals with the probability that
pXn is far away from q. In particular, for concreteness, if we take
p > q > 1
2, Sanov’s theorem states that
−1
n log Pr

(X1, X2, . . . , Xn) : Xn ≥p
 
→p log p
q + (1 −p) log 1 −p
1 −q
= D((p, 1 −p)||(q, 1 −q)).
(11.325)
Justify the following steps:
• Pr

(X1, X2, . . . , Xn) : Xn ≥p
 
≤
n

i=⌊np⌋
n
i

qi(1 −q)n−i.
(11.326)


## PDF page 430

404
INFORMATION THEORY AND STATISTICS
• Argue that the term corresponding to i = ⌊np⌋is the largest
term in the sum on the right-hand side of the last equation.
• Show that this term is approximately 2−nD.
• Prove an upper bound on the probability in Sanov’s theorem
using the steps above. Use similar arguments to prove a lower
bound and complete the proof of Sanov’s theorem.
11.14
Sanov.
Let Xi be i.i.d. ∼N(0, σ 2).
(a) Find the exponent in the behavior of Pr{ 1
n
n
i=1 X2
i ≥α2}.
This can be done from ﬁrst principles (since the normal dis-
tribution is nice) or by using Sanov’s theorem.
(b) What do the data look like if 1
n
n
i=1 X2
i ≥α? That is, what
is the P ∗that minimizes D(P ∥Q)?
11.15
Counting states.
Suppose that an atom is equally likely to be in
each of six states, X ∈{s1, s2, s3, . . . , s6}. One observes n atoms
X1, X2, . . . , Xn independently drawn according to this uniform
distribution. It is observed that the frequency of occurrence of
state s1 is twice the frequency of occurrence of state s2.
(a) To ﬁrst order in the exponent, what is the probability of
observing this event?
(b) Assuming n large, ﬁnd the conditional distribution of the state
of the ﬁrst atom X1, given this observation.
11.16
Hypothesis testing.
Let {Xi} be i.i.d. ∼p(x), x ∈{1, 2, . . .}.
Consider two hypotheses, H0 : p(x) = p0(x) vs. H1 : p(x) =
p1(x), where p0(x) =
	1
2

x and p1(x) = qpx−1, x = 1, 2, 3, . . . .
(a) Find D(p0 ∥p1).
(b) Let Pr{H0} = 1
2. Find the minimal probability of error test for
H0 vs. H1 given data X1, X2, . . . , Xn ∼p(x).
11.17
Maximum likelihood estimation.
Let {fθ(x)} denote a parametric
family of densities with parameter θϵR. Let X1, X2, . . . , Xn be
i.i.d. ∼fθ(x). The function
lθ(xn) = ln
 n

i=1
fθ(xi)

is known as the log likelihood function. Let θ0 denote the true
parameter value.


## PDF page 431

PROBLEMS
405
(a) Let the expected log likelihood be
Eθ0lθ(Xn) =
 
ln
n

i=1
fθ(xi)

n

i=1
fθ0(xi)dxn,
and show that
Eθ0(l(Xn)) = (−h(fθ0) −D(fθ0||fθ))n.
(b) Show that the maximum over θ of the expected log likelihood
is achieved by θ = θ0.
11.18
Large deviations.
Let X1, X2, . . . be i.i.d. random variables
drawn according to the geometric distribution
Pr{X = k} = pk−1(1 −p),
k = 1, 2, . . . .
Find good estimates (to ﬁrst order in the exponent) of:
(a) Pr{ 1
n
n
i=1 Xi ≥α}.
(b) Pr{X1 = k| 1
n
n
i=1 Xi ≥α}.
(c) Evaluate parts (a) and (b) for p = 1
2, α = 4.
11.19
Another expression for Fisher information.
Use integration by
parts to show that
J(θ) = −E ∂2 ln fθ(x)
∂θ2
.
11.20
Stirling’s approximation.
Derive a weak form of Stirling’s
approximation for factorials; that is, show that
n
e
n
≤n! ≤n
n
e
n
(11.327)
using the approximation of integrals by sums. Justify the following
steps:
ln(n!) =
n−1

i=2
ln(i) + ln(n) ≤
 n−1
2
ln x dx + ln n = · · ·
(11.328)


## PDF page 432

406
INFORMATION THEORY AND STATISTICS
and
ln(n!) =
n

i=1
ln(i) ≥
 n
0
ln x dx = · · · .
(11.329)
11.21
Asymptotic value of
n
k

.
Use the simple approximation of Prob-
lem 11.20 to show that if 0 ≤p ≤1, and k = ⌊np⌋(i.e., k is the
largest integer less than or equal to np), then
lim
n→∞
1
n log
n
k

= −p log p −(1 −p) log(1 −p) = H(p).
(11.330)
Now let pi, i = 1, . . . , m be a probability distribution on m sym-
bols (i.e., pi ≥0 and 
i pi = 1). What is the limiting value of
1
n log

n
⌊np1⌋⌊np2⌋. . . ⌊npm−1⌋n −m−1
j=0 ⌊npj⌋

= 1
n log
n!
⌊np1⌋! ⌊np2⌋! . . . ⌊npm−1⌋! (n −m−1
j=0 ⌊npj⌋)!
?
(11.331)
11.22
Running difference.
Let X1, X2, . . . , Xn be i.i.d. ∼Q1(x), and
Y1, Y2, . . . , Yn be i.i.d. ∼Q2(y). Let Xn and Y n be independent.
Find an expression for Pr{n
i=1 Xi −n
i=1 Yi ≥nt} good to ﬁrst
order in the exponent. Again, this answer can be left in parametric
form.
11.23
Large likelihoods.
Let X1, X2, . . . be i.i.d. ∼Q(x), x ∈{1, 2,
. . . , m}. Let P (x) be some other probability mass function. We
form the log likelihood ratio
1
n log P n(X1, X2, . . . , Xn)
Qn(X1, X2, . . . , Xn) = 1
n
n

i=1
log P (Xi)
Q(Xi)
of the sequence Xn and ask for the probability that it exceeds a
certain threshold. Speciﬁcally, ﬁnd (to ﬁrst order in the exponent)
Qn
1
n log P (X1, X2, . . . , Xn)
Q(X1, X2, . . . , Xn) > 0

.
There may be an undetermined parameter in the answer.


