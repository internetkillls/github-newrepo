# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 561

15.3
MULTIPLE-ACCESS CHANNEL
535
It is not difﬁcult to see that any point in C1 or C2 has x + y < 20, so
any point in the convex hull of the union of C1 and C2 satisﬁes this
property. Thus, the point (15,15), which is in C, is not in the convex hull
of (C1 ∪C2). This example also hints at the cause of the problem—in the
deﬁnition for C1, the constraint x + y ≤100 is not active. If this constraint
were replaced by a constraint x + y ≤a, where a ≤20, the above result
of the equality of the two regions would be true, as we now prove.
We restrict ourselves to the pentagonal regions that occur as compo-
nents of the capacity region of a two-user multiple-access channel. In
this case, the capacity region for a ﬁxed p(x1)p(x2) is deﬁned by three
mutual informations, I (X1; Y|X2), I (X2; Y|X1), and I (X1, X2; Y), which
we shall call I1, I2, and I3, respectively. For each p(x1)p(x2), there is a
corresponding vector, I = (I1, I2, I3), and a rate region deﬁned by
CI = {(R1, R2) : R1 ≥0, R2 ≥0, R1 ≤I1, R2 ≤I2, R1 + R2 ≤I3}.
(15.84)
Also, since for any distribution p(x1)p(x2), we have I (X2; Y|X1) =
H(X2|X1) −H(X2|Y, X1) = H(X2) −H(X2|Y, X1) = I (X2; Y, X1) =
I (X2; Y) + I (X2; X1|Y) ≥I (X2; Y),
and
therefore,
I (X1; Y|X2) +
I (X2; Y|X1) ≥I (X1; Y|X2)+ I (X2; Y) = I (X1, X2; Y), we have for all
vectors I that I1 + I2 ≥I3. This property will turn out to be critical for
the theorem.
Lemma 15.3.1
Let I1, I2 ∈R3 be two vectors of mutual informations
that deﬁne rate regions CI1 and CI2, respectively, as given in (15.84).
For 0 ≤λ ≤1, deﬁne Iλ = λI1 + (1 −λ)I2, and let CIλ be the rate region
deﬁned by Iλ. Then
CIλ = λCI1 + (1 −λ)CI2.
(15.85)
Proof:
We shall prove this theorem in two parts. We ﬁrst show that
any point in the (λ, 1 −λ) mix of the sets CI1 and CI2 satisﬁes the con-
straints Iλ. But this is straightforward, since any point in CI1 satisﬁes the
inequalities for I1 and a point in CI2 satisﬁes the inequalities for I2, so
the (λ, 1 −λ) mix of these points will satisfy the (λ, 1 −λ) mix of the
constraints. Thus, it follows that
λCI1 + (1 −λ)CI2 ⊆CIλ.
(15.86)
To prove the reverse inclusion, we consider the extreme points of the
pentagonal regions. It is not difﬁcult to see that the rate regions deﬁned
in (15.84) are always in the form of a pentagon, or in the extreme case


## PDF page 562

536
NETWORK INFORMATION THEORY
when I3 = I1 + I2, in the form of a rectangle. Thus, the capacity region
CI can be also deﬁned as a convex hull of ﬁve points:
(0, 0), (I1, 0), (I1, I3 −I1), (I3 −I2, I2), (0, I2).
(15.87)
Consider the region deﬁned by Iλ; it, too, is deﬁned by ﬁve points. Take
any one of the points, say (I (λ)
3
−I (λ)
2 , I (λ)
2 ). This point can be written as
the (λ, 1 −λ) mix of the points (I (1)
3
−I (1)
2 , I (1)
2 ) and (I (2)
3
−I (2)
2 , I (2)
2 ),
and therefore lies in the convex mixture of CI1 and CI2. Thus, all extreme
points of the pentagon CIλ lie in the convex hull of CI1 and CI2, or
CIλ ⊆λCI1 + (1 −λ)CI2.
(15.88)
Combining the two parts, we have the theorem.
□
In the proof of the theorem, we have implicitly used the fact that all
the rate regions are deﬁned by ﬁve extreme points (at worst, some of
the points are equal). All ﬁve points deﬁned by the I vector were within
the rate region. If the condition I3 ≤I1 + I2 is not satisﬁed, some of the
points in (15.87) may be outside the rate region and the proof collapses.
As an immediate consequence of the above lemma, we have the fol-
lowing theorem:
Theorem 15.3.3
The convex hull of the union of the rate regions deﬁned
by individual I vectors is equal to the rate region deﬁned by the convex
hull of the I vectors.
These arguments on the equivalence of the convex hull operation on
the rate regions with the convex combinations of the mutual informa-
tions can be extended to the general m-user multiple-access channel. A
proof along these lines using the theory of polymatroids is developed in
Han [271].
Theorem 15.3.4
The set of achievable rates of a discrete memoryless
multiple-access channel is given by the closure of the set of all (R1, R2)
pairs satisfying
R1 < I (X1; Y|X2, Q),
R2 < I (X2; Y|X1, Q),
R1 + R2 < I (X1, X2; Y|Q)
(15.89)


## PDF page 563

15.3
MULTIPLE-ACCESS CHANNEL
537
for some choice of the joint distribution p(q)p(x1|q)p(x2|q)p(y|x1, x2)
with |Q| ≤4.
Proof:
We will show that every rate pair lying in the region deﬁned in
(15.89) is achievable (i.e., it lies in the convex closure of the rate pairs
satisfying Theorem 15.3.1). We also show that every point in the convex
closure of the region in Theorem 15.3.1 is also in the region deﬁned
in (15.89).
Consider a rate point R satisfying the inequalities (15.89) of the theo-
rem. We can rewrite the right-hand side of the ﬁrst inequality as
I (X1; Y|X2, Q) =
m

q=1
p(q)I (X1; Y|X2, Q = q)
(15.90)
=
m

q=1
p(q)I (X1; Y|X2)p1q,p2q,
(15.91)
where m is the cardinality of the support set of Q. We can expand the
other mutual informations similarly.
For simplicity in notation, we consider a rate pair as a vector and
denote a pair satisfying the inequalities in (15.58) for a speciﬁc input
product distribution p1q(x1)p2q(x2) as Rp1,p2 as Rq. Speciﬁcally, let Rq =
(R1q, R2q) be a rate pair satisfying
R1q < I (X1; Y|X2)p1q(x1)p2q(x2),
(15.92)
R2q < I (X2; Y|X1)p1q(x1)p2q(x2),
(15.93)
R1q + R2q < I (X1, X2; Y)p1q(x1)p2q(x2).
(15.94)
Then by Theorem 15.3.1, Rq = (R1q, R2q) is achievable. Then since R
satisﬁes (15.89) and we can expand the right-hand sides as in (15.91),
there exists a setof pairs Rq satisfying (15.94) such that
R =
m

q=1
p(q)Rq.
(15.95)
Since a convex combination of achievable rates is achievable, so is R.
Hence, we have proven the achievability of the region in the theorem.
The same argument can be used to show that every point in the convex
closure of the region in (15.58) can be written as the mixture of points
satisfying (15.94) and hence can be written in the form (15.89).


## PDF page 564

538
NETWORK INFORMATION THEORY
The converse is proved in the next section. The converse shows that
all achievable rate pairs are of the form (15.89), and hence establishes
that this is the capacity region of the multiple-access channel. The cardi-
nality bound on the time-sharing random variable Q is a consequence of
Carath´eodory’s theorem on convex sets. See the discussion below.
□
The proof of the convexity of the capacity region shows that any convex
combination of achievable rate pairs is also achievable. We can continue
this process, taking convex combinations of more points. Do we need to
use an arbitrary number of points ? Will the capacity region be increased?
The following theorem says no.
Theorem 15.3.5
(Carath´eodory)
Any point in the convex closure of a
compact set A in a d-dimensional Euclidean space can be represented as
a convex combination of d + 1 or fewer points in the original set A.
Proof:
The proof may be found in Eggleston [183] and Gr¨unbaum
[263].
□
This theorem allows us to restrict attention to a certain ﬁnite convex
combination when calculating the capacity region. This is an important
property because without it, we would not be able to compute the capacity
region in (15.89), since we would never know whether using a larger
alphabet Q would increase the region.
In the multiple-access channel, the bounds deﬁne a connected compact
set in three dimensions. Therefore, all points in its closure can be deﬁned
as the convex combination of at most four points. Hence, we can restrict
the cardinality of Q to at most 4 in the above deﬁnition of the capacity
region.
Remark
Many of the cardinality bounds may be slightly improved by
introducing other considerations. For example, if we are only interested
in the boundary of the convex hull of A as we are in capacity theorems,
a point on the boundary can be expressed as a mixture of d points of
A, since a point on the boundary lies in the intersection of A with a
(d −1)-dimensional support hyperplane.
15.3.4
Converse for the Multiple-Access Channel
We have so far proved the achievability of the capacity region. In this
section we prove the converse.


## PDF page 565

15.3
MULTIPLE-ACCESS CHANNEL
539
Proof:
(Converse to Theorems 15.3.1 and 15.3.4). We must show that
given any sequence of ((2nR1, 2nR2), n) codes with P (n)
e
→0, the rates
must satisfy
R1 ≤I (X1; Y|X2, Q),
R2 ≤I (X2; Y|X1, Q),
R1 + R2 ≤I (X1, X2; Y|Q)
(15.96)
for some choice of random variable Q deﬁned on {1, 2, 3, 4} and joint
distribution p(q)p(x1|q)p(x2|q)p(y|x1, x2). Fix n. Consider the given
code of block length n. The joint distribution on W1 × W2 × Xn
1 × Xn
2 ×
Yn is well deﬁned. The only randomness is due to the random uniform
choice of indices W1 and W2 and the randomness induced by the channel.
The joint distribution is
p(w1, w2, xn
1, xn
2, yn) =
1
2nR1
1
2nR2 p(xn
1|w1)p(xn
2|w2)
n

i=1
p(yi|x1i, x2i),
(15.97)
where p(xn
1|w1) is either 1 or 0, depending on whether xn
1 = x1(w1), the
codeword corresponding to w1, or not, and similarly, p(xn
2|w2) = 1 or 0,
according to whether xn
2 = x2(w2) or not. The mutual informations that
follow are calculated with respect to this distribution.
By the code construction, it is possible to estimate (W1, W2) from the
received sequence Y n with a low probability of error. Hence, the condi-
tional entropy of (W1, W2) given Y n must be small. By Fano’s inequality,
H(W1, W2|Y n) ≤n(R1 + R2)P (n)
e
+ H(P (n)
e
)
△= nϵn.
(15.98)
It is clear that ϵn →0 as P (n)
e
→0. Then we have
H(W1|Y n) ≤H(W1, W2|Y n) ≤nϵn,
(15.99)
H(W2|Y n) ≤H(W1, W2|Y n) ≤nϵn.
(15.100)
We can now bound the rate R1 as
nR1 = H(W1)
(15.101)
= I (W1; Y n) + H(W1|Y n)
(15.102)
(a)
≤I (W1; Y n) + nϵn
(15.103)


## PDF page 566

540
NETWORK INFORMATION THEORY
(b)
≤I (Xn
1(W1); Y n) + nϵn
(15.104)
= H(Xn
1(W1)) −H(Xn
1(W1)|Y n) + nϵn
(15.105)
(c)
≤H(Xn
1(W1)|Xn
2(W2)) −H(Xn
1(W1)|Y n, Xn
2(W2)) + nϵn
(15.106)
= I (Xn
1(W1); Y n|Xn
2(W2)) + nϵn
(15.107)
= H(Y n|Xn
2(W2)) −H(Y n|Xn
1(W1), Xn
2(W2)) + nϵn
(15.108)
(d)
= H(Y n|Xn
2(W2)) −
n

i=1
H(Yi|Y i−1, Xn
1(W1), Xn
2(W2)) + nϵn
(15.109)
(e)
= H(Y n|Xn
2(W2)) −
n

i=1
H(Yi|X1i, X2i) + nϵn
(15.110)
(f)
≤
n

i=1
H(Yi|Xn
2(W2)) −
n

i=1
H(Yi|X1i, X2i) + nϵn
(15.111)
(g)
≤
n

i=1
H(Yi|X2i) −
n

i=1
H(Yi|X1i, X2i) + nϵn
(15.112)
=
n

i=1
I (X1i; Yi|X2i) + nϵn,
(15.113)
where
(a) follows from Fano’s inequality
(b) follows from the data-processing inequality
(c) follows from the fact that since W1 and W2 are independent,
so are Xn
1(W1) and Xn
2(W2), and hence H(Xn
1(W1)|Xn
2(W2)) =
H(Xn
1(W1)), and H(Xn
1(W1)|Y n, Xn
2(W2)) ≤H(Xn
1(W1)|Y n) by
conditioning
(d) follows from the chain rule
(e) follows from the fact that Yi depends only on X1i and X2i by the
memoryless property of the channel
(f) follows from the chain rule and removing conditioning
(g) follows from removing conditioning
Hence, we have
R1 ≤1
n
n

i=1
I (X1i; Yi|X2i) + ϵn.
(15.114)


## PDF page 567

15.3
MULTIPLE-ACCESS CHANNEL
541
Similarly, we have
R2 ≤1
n
n

i=1
I (X2i; Yi|X1i) + ϵn.
(15.115)
To bound the sum of the rates, we have
n(R1 + R2) = H(W1, W2)
(15.116)
= I (W1, W2; Y n) + H(W1, W2|Y n)
(15.117)
(a)
≤I (W1, W2; Y n) + nϵn
(15.118)
(b)
≤I (Xn
1(W1), Xn
2(W2); Y n) + nϵn
(15.119)
= H(Y n) −H(Y n|Xn
1(W1), Xn
2(W2)) + nϵn
(15.120)
(c)
= H(Y n) −
n

i=1
H(Yi|Y i−1, Xn
1(W1), Xn
2(W2)) + nϵn
(15.121)
(d)
= H(Y n) −
n

i=1
H(Yi|X1i, X2i) + nϵn
(15.122)
(e)
≤
n

i=1
H(Yi) −
n

i=1
H(Yi|X1i, X2i) + nϵn
(15.123)
=
n

i=1
I (X1i, X2i; Yi) + nϵn,
(15.124)
where
(a) follows from Fano’s inequality
(b) follows from the data-processing inequality
(c) follows from the chain rule
(d) follows from the fact that Yi depends only on X1i and X2i and is
conditionally independent of everything else
(e) follows from the chain rule and removing conditioning
Hence, we have
R1 + R2 ≤1
n
n

i=1
I (X1i, X2i; Yi) + ϵn.
(15.125)


## PDF page 568

542
NETWORK INFORMATION THEORY
The expressions in (15.114), (15.115), and (15.125) are the averages of the
mutual informations calculated at the empirical distributions in column i
of the codebook. We can rewrite these equations with the new variable Q,
where Q = i ∈{1, 2, . . . , n} with probability 1
n. The equations become
R1 ≤1
n
n

i=1
I (X1i; Yi|X2i) + ϵn
(15.126)
= 1
n
n

i=1
I (X1q; Yq|X2q, Q = i) + ϵn
(15.127)
= I (X1Q; YQ|X2Q, Q) + ϵn
(15.128)
= I (X1; Y|X2, Q) + ϵn,
(15.129)
where X1
△= X1Q, X2
△= X2Q, and Y
△= YQ are new random variables
whose distributions depend on Q in the same way as the distributions
of X1i, X2i and Yi depend on i. Since W1 and W2 are independent, so are
X1i(W1) and X2i(W2), and hence
Pr (X1i(W1) = x1, X2i(W2) = x2)
△= Pr{X1Q = x1|Q = i} Pr{X2Q = x2|Q = i}.
(15.130)
Hence, taking the limit as n →∞, P (n)
e
→0, we have the following
converse:
R1 ≤I (X1; Y|X2, Q),
R2 ≤I (X2; Y|X1, Q),
R1 + R2 ≤I (X1, X2; Y|Q)
(15.131)
for some choice of joint distribution p(q)p(x1|q)p(x2|q)p(y|x1, x2). As
in Section 15.3.3, the region is unchanged if we limit the cardinality of
Q to 4.
This completes the proof of the converse.
□
Thus, the achievability of the region of Theorem 15.3.1 was proved in
Section 15.3.1. In Section 15.3.3 we showed that every point in the region
deﬁned by (15.96) was also achievable. In the converse, we showed that
the region in (15.96) was the best we can do, establishing that this is
indeed the capacity region of the channel. Thus, the region in (15.58)


