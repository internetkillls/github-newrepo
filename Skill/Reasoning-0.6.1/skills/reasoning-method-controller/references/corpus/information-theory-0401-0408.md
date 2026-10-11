# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 401

11.7
HYPOTHESIS TESTING
375
theorem states that the ﬁrst few elements are asymptotically independent
with common distribution P ∗.
Example 11.6.2
As an example of the conditional limit theorem, let us
consider the case when n fair dice are rolled. Suppose that the sum of the
outcomes exceeds 4n. Then by the conditional limit theorem, the proba-
bility that the ﬁrst die shows a number a ∈{1, 2, . . . , 6} is approximately
P ∗(a), where P ∗(a) is the distribution in E that is closest to the uni-
form distribution, where E = {P :  P (a)a ≥4}. This is the maximum
entropy distribution given by
P ∗(x) =
2λx
6
i=1 2λi ,
(11.173)
with λ chosen so that  iP ∗(i) = 4 (see Chapter 12). Here P ∗is the
conditional distribution on the ﬁrst (or any other) die. Apparently, the
ﬁrst few dice inspected will behave as if they are drawn independently
according to an exponential distribution.
11.7
HYPOTHESIS TESTING
One of the standard problems in statistics is to decide between two alter-
native explanations for the data observed. For example, in medical testing,
one may wish to test whether or not a new drug is effective. Similarly, a
sequence of coin tosses may reveal whether or not the coin is biased.
These problems are examples of the general hypothesis-testing problem.
In the simplest case, we have to decide between two i.i.d. distributions.
The general problem can be stated as follows:
Problem 11.7.1
Let X1, X2, . . . , Xn be i.i.d. ∼Q(x). We consider two
hypotheses:
• H1: Q = P1.
• H2: Q = P2.
Consider the general decision function g(x1, x2, . . . , xn), where g(x1,
x2, . . . , xn) = 1 means that H1 is accepted and g(x1, x2, . . . , xn) = 2
means that H2 is accepted. Since the function takes on only two val-
ues, the test can also be speciﬁed by specifying the set A over which
g(x1, x2, . . . , xn) is 1; the complement of this set is the set where
g(x1, x2, . . . , xn) has the value 2. We deﬁne the two probabilities of error:
α = Pr(g(X1, X2, . . . , Xn) = 2|H1 true) = P n
1 (Ac)
(11.174)


## PDF page 402

376
INFORMATION THEORY AND STATISTICS
and
β = Pr(g(X1, X2, . . . , Xn) = 1|H2 true) = P n
2 (A).
(11.175)
In general, we wish to minimize both probabilities, but there is a trade-
off. Thus, we minimize one of the probabilities of error subject to a
constraint on the other probability of error. The best achievable error
exponent in the probability of error for this problem is given by the
Chernoff–Stein lemma.
We ﬁrst prove the Neyman–Pearson lemma, which derives the form of
the optimum test between two hypotheses. We derive the result for discrete
distributions; the same results can be derived for continuous distributions
as well.
Theorem 11.7.1
(Neyman–Pearson lemma)
Let X1, X2, . . . , Xn be
drawn i.i.d. according to probability mass function Q. Consider the deci-
sion problem corresponding to hypotheses Q = P1 vs. Q = P2. For T ≥0,
deﬁne a region
An(T ) =

xn : P1(x1, x2, . . . , xn)
P2(x1, x2, . . . , xn) > T

.
(11.176)
Let
α∗= P n
1 (Ac
n(T )),
β∗= P n
2 (An(T ))
(11.177)
be the corresponding probabilities of error corresponding to decision re-
gion An. Let Bn be any other decision region with associated probabilities
of error α and β. If α ≤α∗, then β ≥β∗.
Proof:
Let A = An(T ) be the region deﬁned in (11.176) and let B ⊆Xn
be any other acceptance region. Let φA and φB be the indicator func-
tions of the decision regions A and B, respectively. Then for all x =
(x1, x2, . . . , xn) ∈Xn,
(φA(x) −φB(x))(P1(x) −T P2(x)) ≥0.
(11.178)
This can be seen by considering separately the cases x ∈A and x /∈A.
Multiplying out and summing this over the entire space, we obtain
0 ≤

(φAP1 −T φAP2 −P1φB + T P2φB)
(11.179)


## PDF page 403

11.7
HYPOTHESIS TESTING
377
=

A
(P1 −T P2) −

B
(P1 −T P2)
(11.180)
= (1 −α∗) −Tβ∗−(1 −α) + Tβ
(11.181)
= T (β −β∗) −(α∗−α).
(11.182)
Since T ≥0, we have proved the theorem.
□
The Neyman–Pearson lemma indicates that the optimum test for two
hypotheses is of the form
P1(X1, X2, . . . , Xn)
P2(X1, X2, . . . , Xn) > T.
(11.183)
This is the likelihood ratio test and the quantity P1(X1,X2,...,Xn)
P2(X1,X2,...,Xn) is called the
likelihood ratio. For example, in a test between two Gaussian distributions
[i.e., between f1 = N(1, σ 2) and f2 = N(−1, σ 2)], the likelihood ratio
becomes
f1(X1, X2, . . . , Xn)
f2(X1, X2, . . . , Xn) =
n
i=1
1
√
2πσ 2e−(Xi−1)2
2σ2
n
i=1
1
√
2πσ 2e−(Xi+1)2
2σ2
(11.184)
= e+
2 n
i=1 Xi
σ2
(11.185)
= e+ 2nXn
σ2 .
(11.186)
Hence, the likelihood ratio test consists of comparing the sample mean
Xn with a threshold. If we want the two probabilities of error to be equal,
we should set T = 1. This is illustrated in Figure 11.8.
In Theorem 11.7.1 we have shown that the optimum test is a likelihood
ratio test. We can rewrite the log-likelihood ratio as
L(X1, X2, . . . , Xn) = log P1(X1, X2, . . . , Xn)
P2(X1, X2, . . . , Xn)
(11.187)
=
n

i=1
log P1(Xi)
P2(Xi)
(11.188)
=

a∈X
nPXn(a) log P1(a)
P2(a)
(11.189)
=

a∈X
nPXn(a) log P1(a)
P2(a)
PXn(a)
PXn(a)
(11.190)


## PDF page 404

378
INFORMATION THEORY AND STATISTICS
0.35
0.3
0.25
0.2
0.15
0.1
0.05
0
−4
−3
−2
−1
0
1
2
3
4
5
x
−5
0.4
f(x)
f(x)
FIGURE 11.8. Testing between two Gaussian distributions.
=

a∈X
nPXn(a) log PXn(a)
P2(a)
−

a∈X
nPXn(a) log PXn(a)
P1(a)
(11.191)
= nD(PXn||P2) −nD(PXn||P1),
(11.192)
the difference between the relative entropy distances of the sample type
to each of the two distributions. Hence, the likelihood ratio test
P1(X1, X2, . . . , Xn)
P2(X1, X2, . . . , Xn) > T
(11.193)
is equivalent to
D(PXn||P2) −D(PXn||P1) > 1
n log T.
(11.194)
We can consider the test to be equivalent to specifying a region of the sim-
plex of types that corresponds to choosing hypothesis H1. The optimum
region is of the form (11.194), for which the boundary of the region is the
set of types for which the difference between the distances is a constant.
This boundary is the analog of the perpendicular bisector in Euclidean
geometry. The test is illustrated in Figure 11.9.
We now offer some informal arguments based on Sanov’s theorem to
show how to choose the threshold to obtain different probabilities of error.
Let B denote the set on which hypothesis 1 is accepted. The probability


## PDF page 405

11.7
HYPOTHESIS TESTING
379
P2
D(P||P1) = D(P||P2) =
log T
Pl
P1
1
n
FIGURE 11.9. Likelihood ratio test on the probability simplex.
of error of the ﬁrst kind is
αn = P n
1 (PXn ∈Bc).
(11.195)
Since the set Bc is convex, we can use Sanov’s theorem to show that the
probability of error is determined essentially by the relative entropy of
the closest member of Bc to P1. Therefore,
αn
.= 2−nD(P ∗
1 ||P1),
(11.196)
where P ∗
1 is the closest element of Bc to distribution P1. Similarly,
βn
.= 2−nD(P ∗
2 ||P2),
(11.197)
where P ∗
2 is the closest element in B to the distribution P2.
Now minimizing D(P ||P2) subject to the constraint D(P ||P2) −
D(P ||P1) ≥1
n log T will yield the type in B that is closest to P2. Set-
ting up the minimization of D(P ||P2) subject to D(P ||P2) −D(P ||P1) =
1
n log T using Lagrange multipliers, we have
J(P ) =

P (x) log P (x)
P2(x) + λ

P (x) log P1(x)
P2(x) + ν

P (x).
(11.198)
Differentiating with respect to P (x) and setting to 0, we have
log P (x)
P2(x) + 1 + λ log P1(x)
P2(x) + ν = 0.
(11.199)


## PDF page 406

380
INFORMATION THEORY AND STATISTICS
Solving this set of equations, we obtain the minimizing P of the form
P ∗
2 = Pλ∗=
P λ
1 (x)P 1−λ
2
(x)

a∈X P λ
1 (a)P 1−λ
2
(a)
,
(11.200)
where λ is chosen so that D(Pλ∗||P1) −D(Pλ∗||P2) = 1
n log T .
From the symmetry of expression (11.200), it is clear that P ∗
1 = P ∗
2 and
that the probabilities of error behave exponentially with exponents given
by the relative entropies D(P ∗||P1) and D(P ∗||P2). Also note from the
equation that as λ →1, Pλ →P1 and as λ →0, Pλ →P2. The curve
that Pλ traces out as λ varies is a geodesic in the simplex. Here Pλ is a
normalized convex combination, where the combination is in the exponent
(Figure 11.9).
In the next section we calculate the best error exponent when one of
the two types of error goes to zero arbitrarily slowly (the Chernoff–Stein
lemma). We will also minimize the weighted sum of the two probabilities
of error and obtain the Chernoff information bound.
11.8
CHERNOFF–STEIN LEMMA
We consider hypothesis testing in the case when one of the probabili-
ties of error is held ﬁxed and the other is made as small as possible.
We will show that the other probability of error is exponentially small,
with an exponential rate equal to the relative entropy between the two
distributions. The method of proof uses a relative entropy version of the
AEP.
Theorem 11.8.1
(AEP for relative entropy)
Let X1, X2, . . . , Xn be
a sequence of random variables drawn i.i.d. according to P1(x), and let
P2(x) be any other distribution on X. Then
1
n log P1(X1, X2, . . . , Xn)
P2(X1, X2, . . . , Xn) →D(P1||P2)
in probability.
(11.201)
Proof:
This follows directly from the weak law of large numbers.
1
n log P1(X1, X2, . . . , Xn)
P2(X1, X2, . . . , Xn) = 1
n log
n
i=1 P1(Xi)
n
i=1 P2(Xi)
(11.202)


## PDF page 407

11.8
CHERNOFF–STEIN LEMMA
381
= 1
n
n

i=1
log P1(Xi)
P2(Xi)
(11.203)
→EP1 log P1(X)
P2(X) in probability (11.204)
= D(P1||P2).
□
(11.205)
Just as for the regular AEP, we can deﬁne a relative entropy typical
sequence as one for which the empirical relative entropy is close to its
expected value.
Deﬁnition
For a ﬁxed n and ϵ > 0, a sequence (x1, x2, . . . , xn) ∈Xn
is said to be relative entropy typical if and only if
D(P1||P2) −ϵ ≤1
n log P1(x1, x2, . . . , xn)
P2(x1, x2, . . . , xn) ≤D(P1||P2) + ϵ.
(11.206)
The set of relative entropy typical sequences is called the relative entropy
typical set A(n)
ϵ (P1||P2).
As a consequence of the relative entropy AEP, we can show that the
relative entropy typical set satisﬁes the following properties:
Theorem 11.8.2
1. For (x1, x2, . . . , xn) ∈A(n)
ϵ (P1||P2),
P1(x1, x2, . . . , xn)2−n(D(P1||P2)+ϵ)
≤P2(x1, x2, . . . , xn)
≤P1(x1, x2, . . . , xn)2−n(D(P1||P2)−ϵ).
(11.207)
2. P1(A(n)
ϵ (P1||P2)) > 1 −ϵ, for n sufﬁciently large.
3. P2(A(n)
ϵ (P1||P2)) < 2−n(D(P1||P2)−ϵ).
4. P2(A(n)
ϵ (P1||P2)) > (1 −ϵ)2−n(D(P1||P2)+ϵ), for n sufﬁciently large.
Proof:
The proof follows the same lines as the proof of Theorem 3.1.2,
with the counting measure replaced by probability measure P2. The proof
of property 1 follows directly from the deﬁnition of the relative entropy


## PDF page 408

382
INFORMATION THEORY AND STATISTICS
typical set. The second property follows from the AEP for relative entropy
(Theorem 11.8.1). To prove the third property, we write
P2(A(n)
ϵ (P1||P2)) =

xn∈A(n)
ϵ (P1||P2)
P2(x1, x2, . . . , xn)
(11.208)
≤

xn∈A(n)
ϵ (P1||P2)
P1(x1, x2, . . . , xn)2−n(D(P1||P2)−ϵ)
(11.209)
= 2−n(D(P1||P2)−ϵ)

xn∈A(n)
ϵ (P1||P2)
P1(x1, x2, . . . , xn) (11.210)
= 2−n(D(P1||P2)−ϵ)P1(A(n)
ϵ (P1||P2))
(11.211)
≤2−n(D(P1||P2)−ϵ),
(11.212)
where the ﬁrst inequality follows from property 1, and the second inequal-
ity follows from the fact that the probability of any set under P1 is less
than 1.
To prove the lower bound on the probability of the relative entropy
typical set, we use a parallel argument with a lower bound on the proba-
bility:
P2(A(n)
ϵ (P1||P2)) =

xn∈A(n)
ϵ (P1||P2)
P2(x1, x2, . . . , xn)
(11.213)
≥

xn∈A(n)
ϵ (P1||P2)
P1(x1, x2, . . . , xn)2−n(D(P1||P2)+ϵ)
(11.214)
= 2−n(D(P1||P2)+ϵ)

xn∈A(n)
ϵ (P1||P2)
P1(x1, x2, . . . , xn) (11.215)
= 2−n(D(P1||P2)+ϵ)P1(A(n)
ϵ (P1||P2))
(11.216)
≥(1 −ϵ)2−n(D(P1||P2)+ϵ),
(11.217)
where the second inequality follows from the second property of A(n)
ϵ
(P1||P2).
□
With the standard AEP in Chapter 3, we also showed that any set that
has a high probability has a high intersection with the typical set, and
therefore has about 2nH elements. We now prove the corresponding result
for relative entropy.


