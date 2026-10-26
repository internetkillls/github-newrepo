# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 265

PROBLEMS
239
(c) BSC and a ternary channel:
p
p
1
2
1
2
p
4
X
Y
5
4
3
3
5
1
2
1
2
1
2
1
2
1
2
1
2
1
2
1
2
1
2
1
2
(d) Ternary channel:
p(y|x) =
 
2
3
1
3
0
0
1
3
2
3
!
.
(7.167)
7.35
Capacity. Suppose that channel P has capacity C, where P is an
m × n channel matrix.
(a) What is the capacity of
˜P =

P
0
0
1

?
(b) What about the capacity of
ˆP =

P
0
0
Ik

?
where Ik if the k × k identity matrix.
7.36
Channel with memory. Consider the discrete memoryless channel
Yi = ZiXi with input alphabet Xi ∈{−1, 1}.
(a) What is the capacity of this channel when {Zi} is i.i.d. with
Zi =

1,
p = 0.5
−1,
p = 0.5?
(7.168)


## PDF page 266

240
CHANNEL CAPACITY
Now consider the channel with memory. Before transmission
begins, Z is randomly chosen and ﬁxed for all time. Thus,
Yi = ZXi.
(b) What is the capacity if
Z =

1,
p = 0.5
−1,
p = 0.5?
(7.169)
7.37
Joint typicality. Let (Xi, Yi, Zi) be i.i.d. according to p(x, y, z). We
will say that (xn, yn, zn) is jointly typical [written (xn, yn, zn) ∈
A(n)
ϵ ] if
• p(xn) ∈2−n(H(X)±ϵ).
• p(yn) ∈2−n(H(Y)±ϵ).
• p(zn) ∈2−n(H(Z)±ϵ).
• p(xn, yn) ∈2−n(H(X,Y)±ϵ).
• p(xn, zn) ∈2−n(H(X,Z)±ϵ).
• p(yn, zn) ∈2−n(H(Y,Z)±ϵ).
• p(xn, yn, zn) ∈2−n(H(X,Y,Z)±ϵ).
Now suppose that ( ˜Xn, ˜Y n, ˜Zn) is drawn according to p(xn)p(yn)
p(zn). Thus, ˜Xn, ˜Y n, ˜Zn have the same marginals as p(xn, yn, zn)
but are independent. Find (bounds on) Pr{( ˜Xn, ˜Y n, ˜Zn) ∈A(n)
ϵ } in
terms
of
the
entropies
H(X),H(Y),H(Z),H(X, Y),H(X, Z),
H(Y, Z), and H(X, Y, Z).
HISTORICAL NOTES
The idea of mutual information and its relationship to channel capacity
was developed by Shannon in his original paper [472]. In this paper, he
stated the channel capacity theorem and outlined the proof using typical
sequences in an argument similar to the one described here. The ﬁrst
rigorous proof was due to Feinstein [205], who used a painstaking “cookie-
cutting” argument to ﬁnd the number of codewords that can be sent with a
low probability of error. A simpler proof using a random coding exponent
was developed by Gallager [224]. Our proof is based on Cover [121] and
on Forney’s unpublished course notes [216].
The converse was proved by Fano [201], who used the inequality bear-
ing his name. The strong converse was ﬁrst proved by Wolfowitz [565],
using techniques that are closely related to typical sequences. An iterative
algorithm to calculate the channel capacity was developed independently
by Arimoto [25] and Blahut [65].


## PDF page 267

HISTORICAL NOTES
241
The idea of the zero-error capacity was developed by Shannon [474];
in the same paper, he also proved that feedback does not increase the
capacity of a discrete memoryless channel. The problem of ﬁnding the
zero-error capacity is essentially combinatorial; the ﬁrst important result
in this area is due to Lovasz [365]. The general problem of ﬁnding the
zero error capacity is still open; see a survey of related results in K¨orner
and Orlitsky [327].
Quantum information theory, the quantum mechanical counterpart to
the classical theory in this chapter, is emerging as a large research area in
its own right and is well surveyed in an article by Bennett and Shor [49]
and in the text by Nielsen and Chuang [395].


## PDF page 268



## PDF page 269

CHAPTER 8
DIFFERENTIAL ENTROPY
We now introduce the concept of differential entropy, which is the entropy
of a continuous random variable. Differential entropy is also related to the
shortest description length and is similar in many ways to the entropy of
a discrete random variable. But there are some important differences, and
there is need for some care in using the concept.
8.1
DEFINITIONS
Deﬁnition
Let X be a random variable with cumulative distribution
function F(x) = Pr(X ≤x). If F(x) is continuous, the random variable
is said to be continuous. Let f (x) = F ′(x) when the derivative is deﬁned.
If
 ∞
−∞f (x) = 1, f (x) is called the probability density function for X. The
set where f (x) > 0 is called the support set of X.
Deﬁnition
The differential entropy h(X) of a continuous random vari-
able X with density f (x) is deﬁned as
h(X) = −

S
f (x) log f (x) dx,
(8.1)
where S is the support set of the random variable.
As in the discrete case, the differential entropy depends only on the
probability density of the random variable, and therefore the differential
entropy is sometimes written as h(f ) rather than h(X).
Remark
As in every example involving an integral, or even a density,
we should include the statement if it exists. It is easy to construct examples
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
243


## PDF page 270

244
DIFFERENTIAL ENTROPY
of random variables for which a density function does not exist or for
which the above integral does not exist.
Example 8.1.1
(Uniform distribution)
Consider a random variable dis-
tributed uniformly from 0 to a so that its density is 1/a from 0 to a and 0
elsewhere. Then its differential entropy is
h(X) = −
 a
0
1
a log 1
a dx = log a.
(8.2)
Note: For a < 1, log a < 0, and the differential entropy is negative. Hence,
unlike discrete entropy, differential entropy can be negative. However,
2h(X) = 2log a = a is the volume of the support set, which is always non-
negative, as we expect.
Example 8.1.2
(Normal distribution)
Let X ∼φ(x) =
1
√
2πσ 2e
−x2
2σ2 .
Then calculating the differential entropy in nats, we obtain
h(φ) = −

φ ln φ
(8.3)
= −

φ(x)

−x2
2σ 2 −ln

2πσ 2

(8.4)
= EX2
2σ 2 + 1
2 ln 2πσ 2
(8.5)
= 1
2 + 1
2 ln 2πσ 2
(8.6)
= 1
2 ln e + 1
2 ln 2πσ 2
(8.7)
= 1
2 ln 2πeσ 2
nats.
(8.8)
Changing the base of the logarithm, we have
h(φ) = 1
2 log 2πeσ 2
bits.
(8.9)


## PDF page 271

8.2
AEP FOR CONTINUOUS RANDOM VARIABLES
245
8.2
AEP FOR CONTINUOUS RANDOM VARIABLES
One of the important roles of the entropy for discrete random variables
is in the AEP, which states that for a sequence of i.i.d. random variables,
p(X1, X2, . . . , Xn) is close to 2−nH(X) with high probability. This enables
us to deﬁne the typical set and characterize the behavior of typical sequences.
We can do the same for a continuous random variable.
Theorem 8.2.1
Let X1, X2, . . . , Xn be a sequence of random vari-
ables drawn i.i.d. according to the density f (x). Then
−1
n log f (X1, X2, . . . , Xn) →E[−log f (X)] = h(X)
in probability.
(8.10)
Proof:
The proof follows directly from the weak law of large numbers.
□
This leads to the following deﬁnition of the typical set.
Deﬁnition
For ϵ > 0 and any n, we deﬁne the typical set A(n)
ϵ
with
respect to f (x) as follows:
A(n)
ϵ
=

(x1, x2, . . . , xn) ∈Sn :
−1
n log f (x1, x2, . . . , xn) −h(X)
 ≤ϵ

,
(8.11)
where f (x1, x2, . . . , xn) = 	n
i=1 f (xi).
The properties of the typical set for continuous random variables par-
allel those for discrete random variables. The analog of the cardinality of
the typical set for the discrete case is the volume of the typical set for
continuous random variables.
Deﬁnition
The volume Vol(A) of a set A ⊂Rn is deﬁned as
Vol(A) =

A
dx1 dx2 · · · dxn.
(8.12)
Theorem 8.2.2
The typical set A(n)
ϵ
has the following properties:
1. Pr

A(n)
ϵ

> 1 −ϵ for n sufﬁciently large.
2. Vol

A(n)
ϵ

≤2n(h(X)+ϵ) for all n.
3. Vol

A(n)
ϵ

≥(1 −ϵ)2n(h(X)−ϵ) for n sufﬁciently large.


## PDF page 272

246
DIFFERENTIAL ENTROPY
Proof:
By Theorem 8.2.1, −1
n log f (Xn) = −1
n
 log f (Xi) →h(X) in
probability, establishing property 1. Also,
1 =

Sn f (x1, x2, . . . , xn) dx1 dx2 · · · dxn
(8.13)
≥

A(n)
ϵ
f (x1, x2, . . . , xn) dx1 dx2 · · · dxn
(8.14)
≥

A(n)
ϵ
2−n(h(X)+ϵ) dx1 dx2 · · · dxn
(8.15)
= 2−n(h(X)+ϵ)

A(n)
ϵ
dx1 dx2 · · · dxn
(8.16)
= 2−n(h(X)+ϵ) Vol

A(n)
ϵ

.
(8.17)
Hence we have property 2. We argue further that the volume of the typical
set is at least this large. If n is sufﬁciently large so that property 1 is
satisﬁed, then
1 −ϵ ≤

A(n)
ϵ
f (x1, x2, . . . , xn) dx1 dx2 · · · dxn
(8.18)
≤

A(n)
ϵ
2−n(h(X)−ϵ) dx1 dx2 · · · dxn
(8.19)
= 2−n(h(X)−ϵ)

A(n)
ϵ
dx1 dx2 · · · dxn
(8.20)
= 2−n(h(X)−ϵ) Vol

A(n)
ϵ

,
(8.21)
establishing property 3. Thus for n sufﬁciently large, we have
(1 −ϵ)2n(h(X)−ϵ) ≤Vol(A(n)
ϵ ) ≤2n(h(X)+ϵ).
□
(8.22)
Theorem 8.2.3
The set A(n)
ϵ
is the smallest volume set with probability
≥1 −ϵ, to ﬁrst order in the exponent.
Proof:
Same as in the discrete case.
□
This theorem indicates that the volume of the smallest set that contains
most of the probability is approximately 2nh. This is an n-dimensional
volume, so the corresponding side length is (2nh)
1
n = 2h. This provides


