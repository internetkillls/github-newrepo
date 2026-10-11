# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 369

PROBLEMS
343
(i) For all (a, b) ∈X × Y with V (b|a) > 0,
1
n
N(a, b|xn, yn) −V (b|a)N(a|xn)
 ≤
ϵ
|Y| + 1.
(10.172)
(ii) N(a, b|xn, yn) = 0 for all (a, b) such that V (b|a) = 0.
The set of such sequences is called the conditionally typi-
cal set and is denoted A∗(n)
ϵ
(Y|xn). Show that the number
of sequences yn that are conditionally typical with a given
xn ∈Xn is bounded by
1
(n + 1)|X||Y| 2n(H(Y|X)−ϵ1) ≤|A∗(n)
ϵ
(Y|xn)|
≤(n + 1)|X||Y|2n(H(Y|X)+ϵ1), (10.173)
where ϵ1 →0 as ϵ →0.
(e) For a pair of random variables (X, Y) with joint distribution
p(x, y), the ϵ-strongly typical set A∗(n)
ϵ
is the set of sequences
(xn, yn) ∈Xn × Yn satisfying
(i)

1
nN(a, b|xn, yn) −p(a, b)
 <
ϵ
|X||Y|
(10.174)
for every pair (a, b) ∈X × Y with p(a, b) > 0.
(ii) N(a, b|xn, yn) = 0
for
all
(a, b) ∈X × Y
with
p(a, b) = 0.
The set of ϵ-strongly jointly typical sequences is called the
ϵ-strongly jointly typical set and is denoted A∗(n)
ϵ
(X, Y). Let
(X, Y) be drawn i.i.d. ∼p(x, y). For any xn such that there
exists at least one pair (xn, yn) ∈A∗(n)
ϵ
(X, Y), the set of se-
quences yn such that (xn, yn) ∈A∗(n)
ϵ
satisﬁes
1
(n + 1)|X||Y| 2n(H(Y|X)−δ(ϵ)) ≤|{yn : (xn, yn) ∈A∗(n)
ϵ
}|
≤(n + 1)|X||Y|2n(H(Y|X)+δ(ϵ)),
(10.175)
where δ(ϵ) →0 as ϵ →0. In particular, we can write
2n(H(Y|X)−ϵ2) ≤|{yn : (xn, yn) ∈A∗(n)
ϵ
}| ≤2n(H(Y|X)+ϵ2),
(10.176)


## PDF page 370

344
RATE DISTORTION THEORY
where we can make ϵ2 arbitrarily small with an appropriate
choice of ϵ and n.
(f) Let Y1, Y2, . . . , Yn be drawn i.i.d. ∼ p(yi). For xn ∈A∗(n)
ϵ
,
the probability that (xn, Y n) ∈A∗(n)
ϵ
is bounded by
2−n(I(X;Y)+ϵ3) ≤Pr((xn, Y n) ∈A∗(n)
ϵ
) ≤2−n(I(X;Y)−ϵ3),
(10.177)
where ϵ3 goes to 0 as ϵ →0 and n →∞.
10.17
Source–channel separation theorem with distortion.
Let V1,
V2, . . . , Vn be a ﬁnite alphabet i.i.d. source which is encoded
as a sequence of n input symbols Xn of a discrete memoryless
channel. The output of the channel Y n is mapped onto the recon-
struction alphabet ˆV n = g(Y n). Let D = Ed(V n, ˆV n) = 1
n
n
i=1
Ed(Vi, ˆVi) be the average distortion achieved by this combined
source and channel coding scheme.
Channel Capacity C
Vn
Vn
Yn
Xn(Vn)
^
(a) Show that if C > R(D), where R(D) is the rate distortion
function for V , it is possible to ﬁnd encoders and decoders
that achieve a average distortion arbitrarily close to D.
(b) (Converse) Show that if the average distortion is equal to D,
the capacity of the channel C must be greater than R(D).
10.18
Rate distortion.
Let d(x, ˆx) be a distortion function. We have
a source X ∼p(x). Let R(D) be the associated rate distortion
function.
(a) Find
˜R(D) in terms of R(D), where
˜R(D) is the rate
distortion function associated with the distortion ˜d(x, ˆx) =
d(x, ˆx) + a for some constant a > 0. (They are not equal.)
(b) Now suppose that d(x, ˆx) ≥0 for all x, ˆx and deﬁne a new
distortion function d∗(x, ˆx) = bd(x, ˆx), where b is some num-
ber ≥0. Find the associated rate distortion function R∗(D) in
terms of R(D).
(c) Let X ∼N(0, σ 2) and d(x, ˆx) = 5(x −ˆx)2 + 3. What is
R(D)?


## PDF page 371

HISTORICAL NOTES
345
10.19
Rate distortion with two constraints.
Let Xi be iid ∼p(x). We
are given two distortion functions, d1(x, ˆx) and d2(x, ˆx). We
wish to describe Xn at rate R and reconstruct it with distortions
Ed1(Xn, ˆXn
1) ≤D1, and Ed2(Xn, ˆXn
2) ≤D2, as shown here:
Xn −→i(Xn) −→( ˆXn
1(i), ˆXn
2(i))
D1 = Ed1(Xn
1, ˆXn
1)
D2 = Ed2(Xn
1, ˆXn
2).
Here i(·) takes on 2nR values. What is the rate distortion function
R(D1, D2)?
10.20
Rate distortion.
Consider the standard rate distortion problem,
Xi i.i.d. ∼p(x), Xn →i(Xn) →ˆXn, |i(·)| = 2nR. Consider two
distortion criteria d1(x, ˆx) and d2(x, ˆx). Suppose that d1(x, ˆx) ≤
d2(x, ˆx) for all x ∈X, ˆx ∈ˆX. Let R1(D) and R2(D) be the cor-
responding rate distortion functions.
(a) Find the inequality relationship between R1(D) and R2(D).
(b) Suppose that we must describe the source {Xi} at the mini-
mum rate R achieving d1(Xn, ˆXn
1) ≤D and d2(Xn, ˆXn
2) ≤D.
Thus,
Xn →i(Xn) →
 ˆXn
1(i(Xn))
ˆXn
2(i(Xn))
and |i(·)| = 2nR.
Find the minimum rate R.
HISTORICAL NOTES
The idea of rate distortion was introduced by Shannon in his original
paper [472]. He returned to it and dealt with it exhaustively in his 1959
paper [485], which proved the ﬁrst rate distortion theorem. Meanwhile,
Kolmogorov and his school in the Soviet Union began to develop rate
distortion theory in 1956. Stronger versions of the rate distortion theorem
have been proved for more general sources in the comprehensive book by
Berger [52].
The inverse water-ﬁlling solution for the rate distortion function for
parallel Gaussian sources was established by McDonald and Schultheiss


## PDF page 372

346
RATE DISTORTION THEORY
[381]. An iterative algorithm for the calculation of the rate distortion
function for a general i.i.d. source and arbitrary distortion measure was
described by Blahut [65], Arimoto [25], and Csisz´ar [139]. This algorithm
is a special case of a general alternating minimization algorithm due to
Csisz´ar and Tusn´ady [155].


## PDF page 373

CHAPTER 11
INFORMATION THEORY
AND STATISTICS
We now explore the relationship between information theory and statistics.
We begin by describing the method of types, which is a powerful technique
in large deviation theory. We use the method of types to calculate the
probability of rare events and to show the existence of universal source
codes. We also consider the problem of testing hypotheses and derive the
best possible error exponents for such tests (the Chernoff–Stein lemma).
Finally, we treat the estimation of the parameters of a distribution and
describe the role of Fisher information.
11.1
METHOD OF TYPES
The AEP for discrete random variables (Chapter 3) focuses our attention
on a small subset of typical sequences. The method of types is an even
more powerful procedure in which we consider sequences that have the
same empirical distribution. With this restriction, we can derive strong
bounds on the number of sequences with a particular empirical distribution
and the probability of each sequence in this set. It is then possible to derive
strong error bounds for the channel coding theorem and prove a variety
of rate distortion results. The method of types was fully developed by
Csisz´ar and K¨orner [149], who obtained most of their results from this
point of view.
Let X1, X2, . . . , Xn be a sequence of n symbols from an alphabet X =
{a1, a2, . . . , a|X|}. We use the notation xn and x interchangeably to denote
a sequence x1, x2, . . . , xn.
Deﬁnition
The type Px (or empirical probability distribution) of a se-
quence x1, x2, . . . , xn is the relative proportion of occurrences of each
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
347


## PDF page 374

348
INFORMATION THEORY AND STATISTICS
symbol of X (i.e., Px(a) = N(a|x)/n for all a ∈X, where N(a|x) is the
number of times the symbol a occurs in the sequence x ∈Xn).
The type of a sequence x is denoted as Px. It is a probability mass
function on X. (Note that in this chapter, we will use capital letters to
denote types and distributions. We also loosely use the word distribution
to mean a probability mass function.)
Deﬁnition
The probability simplex in Rm is the set of points x =
(x1, x2, . . . , xm) ∈Rm such that xi ≥0, m
i=1 xi = 1.
The probability simplex is an (m −1)-dimensional manifold in
m-dimensional space. When m = 3, the probability simplex is the
set
of
points
{(x1, x2, x3) : x1 ≥0, x2 ≥0, x3 ≥0, x1 + x2 + x3 = 1}
(Figure 11.1). Since this is a triangular two-dimensional ﬂat in R3, we
use a triangle to represent the probability simplex in later sections of this
chapter.
Deﬁnition
Let Pn denote the set of types with denominator n.
For example, if X = {0, 1}, the set of possible types with denominator
n is
Pn =

(P (0), P (1)) :
0
n, n
n

,
1
n, n −1
n

, . . . ,
n
n, 0
n

.
(11.1)
Deﬁnition
If P ∈Pn, the set of sequences of length n and type P is
called the type class of P , denoted T (P ):
T (P ) = {x ∈Xn : Px = P }.
(11.2)
The type class is sometimes called the composition class of P .
x2
x3
x1
x1 + x2 + x3 = 1
1
1
1
FIGURE 11.1. Probability simplex in R3.


## PDF page 375

11.1
METHOD OF TYPES
349
Example 11.1.1
Let X = {1, 2, 3}, a ternary alphabet. Let x = 11321.
Then the type Px is
Px(1) = 3
5,
Px(2) = 1
5,
Px(3) = 1
5.
(11.3)
The type class of Px is the set of all sequences of length 5 with three 1’s,
one 2, and one 3. There are 20 such sequences, and
T (Px) = {11123, 11132, 11213, . . . , 32111}.
(11.4)
The number of elements in T (P ) is
|T (P )| =

5
3, 1, 1

=
5!
3! 1! 1! = 20.
(11.5)
The essential power of the method of types arises from the following
theorem, which shows that the number of types is at most polynomial
in n.
Theorem 11.1.1
|Pn| ≤(n + 1)|X|.
(11.6)
Proof:
There are |X| components in the vector that speciﬁes Px. The
numerator in each component can take on only n + 1 values. So there are
at most (n + 1)|X| choices for the type vector. Of course, these choices
are not independent (e.g., the last choice is ﬁxed by the others). But this
is a sufﬁciently good upper bound for our needs.
□
The crucial point here is that there are only a polynomial number of
types of length n. Since the number of sequences is exponential in n, it
follows that at least one type has exponentially many sequences in its
type class. In fact, the largest type class has essentially the same number
of elements as the entire set of sequences, to ﬁrst order in the exponent.
Now, we assume that the sequence X1, X2, . . . , Xn is drawn i.i.d.
according to a distribution Q(x). All sequences with the same type have
the same probability, as shown in the following theorem. Let Qn(xn) =
n
i=1 Q(xi) denote the product distribution associated with Q.
Theorem 11.1.2
If X1, X2, . . . , Xn are drawn i.i.d. according to Q(x),
the probability of x depends only on its type and is given by
Qn(x) = 2−n(H(Px)+D(Px||Q)).
(11.7)


## PDF page 376

350
INFORMATION THEORY AND STATISTICS
Proof
Qn(x) =
n

i=1
Q(xi)
(11.8)
=

a∈X
Q(a)N(a|x)
(11.9)
=

a∈X
Q(a)nPx(a)
(11.10)
=

a∈X
2nPx(a) log Q(a)
(11.11)
=

a∈X
2n(Px(a) log Q(a)−Px(a) log Px(a)+Px(a) log Px(a))
(11.12)
= 2n 
a∈X (−Px(a) log Px(a)
Q(a) +Px(a) log Px(a))
(11.13)
= 2n(−D(Px||Q)−H(Px)).
□
(11.14)
Corollary
If x is in the type class of Q, then
Qn(x) = 2−nH(Q).
(11.15)
Proof:
If x ∈T (Q), then Px = Q, which can be substituted into (11.14).
□
Example 11.1.2
The probability that a fair die produces a particular
sequence of length n with precisely n/6 occurrences of each face (n is a
multiple of 6) is 2−nH( 1
6, 1
6,..., 1
6) = 6−n. This is obvious. However, if the
die has a probability mass function ( 1
3, 1
3, 1
6, 1
12, 1
12, 0), the probability of
observing a particular sequence with precisely these frequencies is pre-
cisely 2−nH( 1
3, 1
3, 1
6, 1
12, 1
12,0) for n a multiple of 12. This is more interesting.
We now give an estimate of the size of a type class T (P ).
Theorem 11.1.3
(Size of a type class T (P ))
For any type P ∈Pn,
1
(n + 1)|X| 2nH(P) ≤|T (P )| ≤2nH(P).
(11.16)
Proof:
The exact size of T (P ) is easy to calculate. It is a simple combi-
natorial problem—the number of ways of arranging nP (a1), nP (a2), . . . ,


