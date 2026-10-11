# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 673

16.8
SHANNON–MCMILLAN–BREIMAN THEOREM (GENERAL AEP)
647
Proof:
Functions Yn = f (Xn
−∞) of ergodic processes {Xi} are ergodic
processes. Thus, log p(Xn|Xn−1
n−k) and log p(Xn|Xn−1, Xn−2, . . . , ) are also
ergodic processes, and
−1
n log pk(Xn−1
0
) = −1
n log p(Xk−1
0
) −1
n
n−1

i=k
log p(Xi|Xi−1
i−k) (16.189)
→0 + H k
with probability 1,
(16.190)
by the ergodic theorem. Similarly, by the ergodic theorem,
−1
n log p(Xn−1
0
|X−1, X−2, . . .) = −1
n
n−1

i=0
log p(Xi|Xi−1, Xi−2, . . .)
(16.191)
→H ∞
with probability 1.
□(16.192)
Lemma 16.8.2
(No gap)
H k ↘H ∞and H = H ∞.
Proof:
We know that for stationary processes, H k ↘H, so it remains
to show that H k ↘H ∞, thus yielding H = H ∞. Levy’s martingale
convergence theorem for conditional probabilities asserts that
p(x0|X−1
−k) →p(x0|X−1
−∞)
with probability 1
(16.193)
for all x0 ∈X. Since X is ﬁnite and p log p is bounded and continuous in
p for all 0 ≤p ≤1, the bounded convergence theorem allows interchange
of expectation and limit, yielding
lim
k→∞H k = lim
k→∞E

−

x0∈X
p(x0|X−1
−k) log p(x0|X−1
−k)

(16.194)
= E

−

x0∈X
p(x0|X−1
−∞) log p(x0|X−1
−∞)

(16.195)
= H ∞.
(16.196)
Thus, H k ↘H = H ∞.
□


## PDF page 674

648
INFORMATION THEORY AND PORTFOLIO THEORY
Lemma 16.8.3
(Sandwich)
lim sup
n→∞
1
n log pk(Xn−1
0
)
p(Xn−1
0
)
≤0,
(16.197)
lim sup 1
n log
p(Xn−1
0
)
p(Xn−1
0
|X−1
−∞)
≤0.
(16.198)
Proof:
Let A be the support set of p(Xn−1
0
). Then
E

pk(Xn−1
0
)
p(Xn−1
0
)

=

xn−1
0
∈A
p(xn−1
0
)pk(xn−1
0
)
p(xn−1
0
)
(16.199)
=

xn−1
0
∈A
pk(xn−1
0
)
(16.200)
= pk(A)
(16.201)
≤1.
(16.202)
Similarly, let B(X−1
−∞) denote the support set of p(·|X−1
−∞). Then we have
E

p(Xn−1
0
)
p(Xn−1
0
|X−1
−∞)

= E

E

p(Xn−1
0
)
p(Xn−1
0
|X−1
−∞)
					 X−1
−∞

(16.203)
= E



xn∈B(X−1
−∞)
p(xn)
p(xn|X−1
−∞)
p(xn|X−1
−∞)

(16.204)
= E



xn∈B(X−1
−∞)
p(xn)


(16.205)
≤1.
(16.206)
By Markov’s inequality and (16.202), we have
Pr

pk(Xn−1
0
)
p(Xn−1
0
)
≥tn

≤1
tn
(16.207)


## PDF page 675

SUMMARY
649
or
Pr

1
n log pk(Xn−1
0
)
p(Xn−1
0
)
≥1
n log tn

≤1
tn
.
(16.208)
Letting
tn = n2
and
noting
that
∞
n=1
1
n2 < ∞,
we
see
by
the
Borel–Cantelli lemma that the event

1
n log pk(Xn−1
0
)
p(Xn−1
0
)
≥1
n log tn

(16.209)
occurs only ﬁnitely often with probability 1. Thus,
lim sup 1
n log pk(Xn−1
0
)
p(Xn−1
0
)
≤0
with probability 1.
(16.210)
Applying the same arguments using Markov’s inequality to (16.206), we
obtain
lim sup 1
n log
p(Xn−1
0
)
p(Xn−1
0
|X−1
−∞)
≤0
with probability 1,
(16.211)
proving the lemma.
□
The arguments used in the proof can be extended to prove the AEP for
the stock market (Theorem 16.5.3).
SUMMARY
Growth rate. The growth rate of a stock market portfolio b with
respect to a distribution F(x) is deﬁned as
W(b, F) =

log btx dF(x) = E

log btx

.
(16.212)
Log-optimal portfolio. The optimal growth rate with respect to a dis-
tribution F(x) is
W ∗(F) = max
b
W(b, F).
(16.213)


## PDF page 676

650
INFORMATION THEORY AND PORTFOLIO THEORY
The portfolio b∗that achieves the maximum of W(b, F) is called the
log-optimal portfolio.
Concavity. W(b, F) is concave in b and linear in F. W ∗(F) is convex
in F.
Optimality conditions. The portfolio b∗is log-optimal if and only if
E
 Xi
b∗tX

= 1
if b∗
i > 0,
≤1
if b∗
i = 0.
(16.214)
Expected ratio optimality. If S∗
n = 
n
i=1 b∗tXi, Sn = 
n
i=1 bt
iXi, then
E Sn
S∗n
≤1
if and only if
E ln Sn
S∗n
≤0.
(16.215)
Growth rate (AEP)
1
n log S∗
n →W ∗(F)
with probability 1.
(16.216)
Asymptotic optimality
lim sup
n→∞
1
n log Sn
S∗n
≤0
with probability 1.
(16.217)
Wrong information. Believing g when f is true loses
W = W(b∗
f , F) −W(b∗
g, F) ≤D(f ||g).
(16.218)
Side information Y
W ≤I (X; Y).
(16.219)
Chain rule
W ∗(Xi|X1, X2, . . . , Xi−1) =
max
bi(x1,x2,...,xi−1) E log bt
iXi
(16.220)
W ∗(X1, X2, . . . , Xn) =
n

i=1
W ∗(Xi|X1, X2, . . . , Xi−1).
(16.221)


## PDF page 677

SUMMARY
651
Growth rate for a stationary market.
W ∗
∞= lim W ∗(X1, X2, . . . , Xn)
n
(16.222)
1
n log S∗
n →W ∗
∞.
(16.223)
Competitive optimality of log-optimal portfolios.
Pr(V S ≥U ∗S∗) ≤1
2.
(16.224)
Universal portfolio.
max
ˆbi(·)
min
xn,b

n
i=1 ˆbt
i(xi−1)xi

n
i=1 btxi
= Vn,
(16.225)
where
Vn =


n1+···+nm=n

n
n1, n2, . . . , nm

2−nH(n1/n,...,nm/n)
−1
.
(16.226)
For m = 2,
Vn ∼
$
2/πn
(16.227)
The causal universal portfolio
ˆbi+1(xi) =

bSi(b, xi) dµ(b)

Si(b, xi) dµ(b)
(16.228)
achieves
ˆSn(xn)
S∗n(xn) ≥
1
2
√
n + 1
(16.229)
for all n and all xn.
AEP. If {Xi} is stationary ergodic, then
−1
n log p(X1, X2, . . . , Xn) →H(X)
with probability 1. (16.230)


## PDF page 678

652
INFORMATION THEORY AND PORTFOLIO THEORY
PROBLEMS
16.1
Growth rate.
Let
X =



(1, a)
with probability 1
2
(1, 1/a)
with probability 1
2
where a > 1. This vector X represents a stock market vector of
cash vs. a hot stock. Let
W(b, F) = E log btX
and
W ∗= max
b
W(b, F)
be the growth rate.
(a) Find the log optimal portfolio b∗.
(b) Find the growth rate W ∗.
(c) Find the asymptotic behavior of
Sn =
n

i=1
btXi
for all b.
16.2
Side information.
Suppose, in Problem 16.1, that
Y =
 1
if (X1, X2) ≥(1, 1),
0
if (X1, X2) ≤(1, 1).
Let the portfolio b depend on Y. Find the new growth rate W ∗∗
and verify that W = W ∗∗−W ∗satisﬁes
W ≤I (X; Y).
16.3
Stock dominance.
Consider a stock market vector
X = (X1, X2).
Suppose that X1 = 2 with probability 1. Thus an investment in
the ﬁrst stock is doubled at the end of the day.


## PDF page 679

PROBLEMS
653
(a) Find necessary and sufﬁcient conditions on the distribution of
stock X2 such that the log-optimal portfolio b∗invests all the
wealth in stock X2 [i.e., b∗= (0, 1)].
(b) Argue for any distribution on X2 that the growth rate satisﬁes
W ∗≥1.
16.4
Including experts and mutual funds.
Let X ∼F(x), x ∈Rm
+, be
the vector of price relatives for a stock market. Suppose that an
“expert” suggests a portfolio b. This would result in a wealth
factor btX. We add this to the stock alternatives to form ˜X =
(X1, X2, . . . , Xm, btX). Show that the new growth rate,
˜W ∗=
max
b1,...,bm,bm+1

ln(bt ˜x) dF(˜x),
(16.231)
is equal to the old growth rate,
W ∗= max
b1,...,bm

ln(btx) dF(x).
(16.232)
16.5
Growth rate for symmetric distribution.
Consider a stock vec-
tor X ∼F(x),
X ∈Rm,
X ≥0, where the component stocks
are exchangeable. Thus, F(x1, x2, . . . , xm) = F(xσ(1), xσ(2), . . . ,
xσ(m)) for all permutations σ.
(a) Find the portfolio b∗optimizing the growth rate and establish
its optimality. Now assume that X has been normalized so
that 1
m
m
i=1 Xi = 1, and F is symmetric as before.
(b) Again assuming X to be normalized, show that all symmetric
distributions F have the same growth rate against b∗.
(c) Find this growth rate.
16.6
Convexity.
We are interested in the set of stock market densities
that yield the same optimal porfolio. Let Pb0 be the set of all
probability densities on Rm
+ for which b0 is optimal. Thus, Pb0 =
{p(x) :

ln(btx)p(x) dx is maximized by b = b0}. Show that Pb0
is a convex set. It may be helpful to use Theorem 16.2.2.
16.7
Short selling.
Let
X =
 (1, 2),
p,
(1, 1
2),
1 −p.
Let B = {(b1, b2) : b1 + b2 = 1}. Thus, this set of portfolios B
does not include the constraint bi ≥0. (This allows short selling.)


## PDF page 680

654
INFORMATION THEORY AND PORTFOLIO THEORY
(a) Find the log optimal portfolio b∗(p).
(b) Relate the growth rate W ∗(p) to the entropy rate H(p).
16.8
Normalizing x.
Suppose that we deﬁne the log-optimal portfolio
b∗to be the portfolio maximizing the relative growth rate

ln
btx
1
m
m
i=1 xi
dF(x1, . . . , xm).
The virtue of the normalization 1
m
 Xi, which can be viewed as
the wealth associated with a uniform portfolio, is that the relative
growth rate is ﬁnite even when the growth rate

ln btxdF(x)
is not. This matters, for example, if X has a St. Petersburg-like
distribution. Thus, the log-optimal portfolio b∗is deﬁned for all
distributions F, even those with inﬁnite growth rates W ∗(F).
(a) Show that if b maximizes

ln(btx) dF(x), it also maximizes

ln btx
utx dF(x), where u = ( 1
m, 1
m, . . . , 1
m).
(b) Find the log optimal portfolio b∗for
X =

(22k+1, 22k),
2−(k+1),
(22k, 22k+1),
2−(k+1),
where k = 1, 2, . . . .
(c) Find EX and W ∗.
(d) Argue that b∗is competitively better than any portfolio b in
the sense that Pr{btX > cb∗tX} ≤1
c.
16.9
Universal portfolio.
We examine the ﬁrst n = 2 steps of the
implementation of the universal portfolio in (16.7.2) for µ(b) uni-
form for m = 2 stocks. Let the stock vectors for days 1 and 2 be
x1 = (1, 1
2), and x2 = (1, 2). Let b = (b, 1 −b) denote a portfo-
lio.
(a) Graph S2(b) = 
2
i=1 btxi,
0 ≤b ≤1.
(b) Calculate S∗
2 = maxb S2(b).
(c) Argue that log S2(b) is concave in b.
(d) Calculate the (universal) wealth ˆS2 =
 1
0 S2(b)db.
(e) Calculate the universal portfolio at times n = 1 and n = 2:
ˆb1 =
 1
0
b db


