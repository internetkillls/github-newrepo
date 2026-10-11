# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 457

13.1
UNIVERSAL CODES AND CHANNEL CAPACITY
431
The distribution q that achieves the minimum in (13.11) is the output
distribution q∗(x) induced be the capacity-achieving input distribution
π∗(θ):
q∗(x) = qπ∗(x) =

θ
π∗(θ)pθ(x).
(13.12)
Proof:
Let π(θ) be an input distribution on θ ∈{1, 2, . . . , m}, and let
the induced output distribution be qπ:
(qπ)j =
m

i=1
πipij,
(13.13)
where pij = pθ(x) for θ = i, x = j. Then for any distribution q on the
output, we have
Iπ(θ; X) =

i,j
πipij log pij
(qπ)j
(13.14)
=

i
πiD(pi∥qπ)
(13.15)
=

i,j
πipij log pij
qj
qj
(qπ)j
(13.16)
=

i,j
πipij log pij
qj
+

i,j
πipij log
qj
(qπ)j
(13.17)
=

i,j
πipij log pij
qj
+

j
(qπ)j log
qj
(qπ)j
(13.18)
=

i,j
πipij log pij
qj
−D(qπ∥q)
(13.19)
=

i
πiD(pi∥q) −D(qπ∥q)
(13.20)
≤

i
πiD(pi∥q)
(13.21)
for all q, with equality iff q = qπ. Thus, for all q,

i
πiD(pi∥q) ≥

i
πiD(pi∥qπ),
(13.22)


## PDF page 458

432
UNIVERSAL SOURCE CODING
and therefore
Iπ(θ; X) = min
q

i
πiD(pi∥q)
(13.23)
is achieved when q = qπ. Thus, the output distribution that minimizes the
average distance to all the rows of the transition matrix is the the output
distribution induced by the channel (Lemma 10.8.1).
The channel capacity can now be written as
C = max
π
Iπ(θ; X)
(13.24)
= max
π
min
q

i
πiD(pi∥q).
(13.25)
We can now apply a fundamental theorem of game theory, which states
that for a continuous function f (x, y), x ∈X, y ∈Y, if f (x, y) is convex
in x and concave in y, and X, Y are compact convex sets, then
min
x∈X max
y∈Y f (x, y) = max
y∈Y min
x∈X f (x, y).
(13.26)
The proof of this minimax theorem can be found in [305, 392].
By convexity of relative entropy (Theorem 2.7.2), 
i πiD(pi∥q) is
convex in q and concave in π, and therefore
C = max
π
min
q

i
πiD(pi∥q)
(13.27)
= min
q max
π

i
πiD(pi∥q)
(13.28)
= min
q max
i
D(pi∥q),
(13.29)
where the last equality follows from the fact that the maximum is achieved
by putting all the weight on the index i maximizing D(pi∥q) in (13.28).
It also follows that q∗= qπ∗. This completes the proof.
□
Thus, the channel capacity of the channel from θ to X is the minimax
expected redundancy in source coding.
Example 13.1.1
Consider the case when X = {1, 2, 3} and θ takes only
two values, 1 and 2, and the corresponding distributions are p1 = (1 −α,
α, 0) and p2 = (0, α, 1 −α). We would like to encode a sequence of
symbols from X without knowing whether the distribution is p1 or p2.
The arguments above indicate that the worst-case optimal code uses the


## PDF page 459

13.2
UNIVERSAL CODING FOR BINARY SEQUENCES
433
codeword lengths corresponding to the distribution that has a minimal
relative entropy distance from both distributions, in this case, the midpoint
of the two distributions. Using this distribution, q =
1−α
2 , α, 1−α
2

, we
achieve a redundancy of
D(p1∥q) = D(p2∥q) = (1 −α) log
1 −α
(1 −α)/2 + α log α
α + 0 = 1 −α.
(13.30)
The channel with transition matrix rows equal to p1 and p2 is equivalent
to the erasure channel (Section 7.1.5), and the capacity of this channel can
easily be calculated to be (1 −α), achieved with a uniform distribution on
the inputs. The output distribution corresponding to the capacity-achieving
input distribution is equal to
1−α
2 , α, 1−α
2

(i.e., the same as the distri-
bution q above). Thus, if we don’t know the distribution for this class of
sources, we code using the distribution q rather than p1 or p2, and incur
an additional cost of 1 −α bits per source symbol above the ideal entropy
bound.
13.2
UNIVERSAL CODING FOR BINARY SEQUENCES
Now we consider an important special case of encoding a binary sequence
xn ∈{0, 1}n. We do not make any assumptions about the probability dis-
tribution for x1, x2, . . . , xn.
We begin with bounds on the size of
n
k

, taken from Wozencraft and
Reiffen [567] proved in Lemma 17.5.1: For k ̸= 0 or n,

n
8k(n −k) ≤

n
k

2−nH(k/n) ≤

n
πk(n −k).
(13.31)
We ﬁrst describe an ofﬂine algorithm to describe the sequence; we
count the number of 1’s in the sequence, and after we have seen the entire
sequence, we send a two-stage description of the sequence. The ﬁrst stage
is a count of the number of 1’s in the sequence [i.e., k = 
i xi (using
⌈log(n + 1)⌉bits)], and the second stage is the index of this sequence
among all sequences that have k 1’s (using ⌈log
n
k

⌉bits). This two-stage
description requires total length
l(xn) ≤log(n + 1) + log

n
k

+ 2
(13.32)
≤log n + nH
k
n

−1
2 log n −1
2 log

π k
n
(n −k)
n

+ 3 (13.33)


## PDF page 460

434
UNIVERSAL SOURCE CODING
= nH
k
n

+ 1
2 log n −1
2 log

π k
n
n −k
n

+ 3.
(13.34)
Thus, the cost of describing the sequence is approximately 1
2 log n bits
above the optimal cost with the Shannon code for a Bernoulli distribution
corresponding to k/n. The last term is unbounded at k = 0 or k = n, so
the bound is not useful for these cases (the actual description length is
log(n + 1) bits, whereas the entropy H(k/n) = 0 when k = 0 or k = n).
This counting approach requires the compressor to wait until he has
seen the entire sequence. We now describe a different approach using a
mixture distribution that achieves the same result on the ﬂy. We choose
the coding distribution q(x1, x2, . . . , xn) = 2−l(x1,x2,...,xn) to be a uniform
mixture of all Bernoulli(θ) distributions on x1, x2, . . . , xn. We will analyze
the performance of a code using this distribution and show that such codes
perform well for all input sequences.
We construct this distribution by assuming that θ, the parameter of
the Bernoulli distribution is drawn according to a uniform distribution on
[0, 1]. The probability of a sequence x1, x2, . . . , xn with k ones is θk(1 −
θ)n−k under the Bernoulli(θ) distribution. Thus, the mixture probability
of the sequence is
p(x1, x2, . . . , xn) =
 1
0
θk(1 −θ)n−kdθ = A(n, k).
(13.35)
Integrating by parts, setting u = (1 −θ)n−k and dv = θkdθ, we have
 1
0
θk(1 −θ)n−kdθ =

1
k + 1θk+1(1 −θ)n−k
1
0
+ n −k
k + 1
 1
0
θk+1(1 −θ)n−k−1dθ,
(13.36)
or
A(n, k) = n −k
k + 1A(n, k + 1).
(13.37)
Now A(n, n) =
 1
0 θndθ =
1
n+1, and we can easily verify from the recur-
sion that
p(x1, x2, . . . , xn) = A(n, k) =
1
n + 1
1

n
k
.
(13.38)


## PDF page 461

13.2
UNIVERSAL CODING FOR BINARY SEQUENCES
435
The codeword length with respect to the mixture distribution is

log
1
q(xn)

≤log(n + 1) + log

n
k

+ 1,
(13.39)
which is within one bit of the length of the two-stage description above.
Thus, we have a similar bound on the codeword length
l(x1, x2, . . . , xn) ≤H
k
n

+ 1
2 log n −1
2 log

π k
n
(n −k)
n

+ 2 (13.40)
for all sequences x1, x2, . . . , xn. This mixture distribution achieves a code-
word length within 1
2 log n bits of the optimal code length nH(k/n) that
would be required if the source were really Bernoulli(k/n), without any
assumptions about the distribution of the source.
Thismixturedistributionyieldsaniceexpressionfortheconditionalprob-
ability of the next symbol given the previous symbols of x1, x2, . . . , xn. Let
ki be the number of 1’s in the ﬁrst i symbols of x1, x2, . . . , xn. Using (13.38),
we have
q(xi+1 = 1|xi) = q(xi, 1)
q(xi)
(13.41)
=

1
i + 2
1
 i+1
ki+1

  
1
i + 1
1
 i
ki


(13.42)
=
1
i + 2
(ki + 1)!(n −ki)!
(i + 1)!
(i + 1)ki!(i −ki)!
i!
(13.43)
= ki + 1
i + 2 .
(13.44)
This is the Bayesian posterior probability of 1 given the uniform prior
on θ, and is called the Laplace estimate for the probability of the next
symbol. We can use this posterior probability as the probability of the next
symbol for arithmetic coding, and achieve the codeword length log
1
q(xn)
in a sequential manner with ﬁnite-precision arithmetic. This is a horizon-
free result, in that the procedure does not depend on the length of the
sequence.
One issue with the uniform mixture approach or the two-stage approach
is that the bound does not apply for k = 0 or k = n. The only uni-
form bound that we can give on the extra redundancy is log n, which
we can obtain by using the bounds of (11.40). The problem is that


## PDF page 462

436
UNIVERSAL SOURCE CODING
we are not assigning enough probability to sequences with k = 0 or
k = n. If instead of using a uniform distribution on θ, we used the
Dirichlet
1
2, 1
2

distribution, also called the Beta
1
2, 1
2

distribution, the
probability of a sequence x1, x2, . . . , xn becomes
q 1
2 (xn) =
 1
0
θk(1 −θ)n−k
1
π√θ(1 −θ) dθ
(13.45)
and it can be shown that this achieves a description length
log
1
q 1
2(xn)
≤H(k/n) + 1
2 log n + log π
8
(13.46)
for all xn ∈{0, 1}n, achieving a uniform bound on the redundancy of the
universal mixture code. As in the case of the uniform prior, we can cal-
culate the conditional distribution of the next symbol, given the previous
observations, as
q 1
2(xi+1 = 1|xi) = ki + 1
2
i + 1 ,
(13.47)
which can be used with arithmetic coding to provide an online algorithm
to encode the sequence. We will analyze the performance of the mix-
ture algorithm in greater detail when we analyze universal portfolios in
Section 16.7.
13.3
ARITHMETIC CODING
The Huffman coding procedure described in Chapter 5 is optimal for
encoding a random variable with a known distribution that has to be
encoded symbol by symbol. However, due to the fact that the codeword
lengths for a Huffman code were restricted to be integral, there could be a
loss of up to 1 bit per symbol in coding efﬁciency. We could alleviate this
loss by using blocks of input symbols—however, the complexity of this
approach increases exponentially with block length. We now describe a
method of encoding without this inefﬁciency. In arithmetic coding, instead
of using a sequence of bits to represent a symbol, we represent it by a
subinterval of the unit interval.
The code for a sequence of symbols is an interval whose length decreases
as we add more symbols to the sequence. This property allows us to have a
coding scheme that is incremental (the code for an extension to a sequence
can be calculated simply from the code for the original sequence) and for
which the codeword lengths are not restricted to be integral. The motivation


## PDF page 463

13.3
ARITHMETIC CODING
437
for arithmetic coding is based on Shannon–Fano–Elias coding (Section 5.9)
and the following lemma:
Lemma 13.3.1
Let Y be a random variable with continuous probability
distribution function F(y). Let U = F(Y) (i.e., U is a function of Y deﬁned
by its distribution function). Then U is uniformly distributed on [0, 1].
Proof:
Since F(y) ∈[0, 1], the range of U is [0, 1]. Also, for u ∈[0, 1],
FU(u) = Pr(U ≤u)
(13.48)
= Pr(F(Y) ≤u)
(13.49)
= Pr(Y ≤F −1(u))
(13.50)
= F(F −1(u))
(13.51)
= u,
(13.52)
which proves that U has a uniform distribution in [0, 1].
□
Now consider an inﬁnite sequence of random variables X1, X2, . . . from
a ﬁnite alphabet X = 0, 1, 2, . . . , m. For any sequence x1, x2, . . . , from
this alphabet, we can place 0. in front of the sequence and consider it as
a real number (base m + 1) between 0 and 1. Let X be the real-valued
random variable X = 0.X1X2 . . . . Then X has the following distribution
function:
FX(x) = Pr{X ≤x = 0.x1x2 · · ·}
(13.53)
= Pr{0.X1X2 · · · ≤0.x1x2 · · ·}
(13.54)
= Pr{X1 < x1} + Pr{X1 = x1, X2 < x2} + · · · .
(13.55)
Now let U = FX(X) = FX(0.X1X2 . . .) = 0.F1F2 . . . . If the distribution
on inﬁnite sequences X∞has no atoms, then, by the lemma above, U has a
uniform distribution on [0, 1], and therefore the bits F1F2 . . . in the binary
expansion of U are Bernoulli(1
2) (i.e., they are independent and uniformly
distributed on {0, 1}). These bits are therefore incompressible, and form a
compressed representation of the sequence 0.X1X2 . . . . For Bernoulli or
Markov models, it is easy to calculate the cumulative distribution function,
as illustrated in the following example.
Example 13.3.1
Let X1, X2, . . . , Xn be Bernoulli(p). Then the sequence
xn = 110101 maps into


## PDF page 464

438
UNIVERSAL SOURCE CODING
F(xn) = Pr(X1 < 1) + Pr(X1 = 1, X2 < 1)
+ Pr(X1 = 1, X2 = 1, X3 < 0)
+ Pr(X1 = 1, X2 = 1, X3 = 0, X4 < 1)
+ Pr(X1 = 1, X2 = 1, X3 = 0, X4 = 1, X5 < 0)
+ Pr(X1 = 1, X2 = 1, X3 = 0, X4 = 1, X5 = 0, X6 < 1)
(13.56)
= q + pq + p2·0 + p2q·q + p2qp·0 + p2qpqq
(13.57)
= q + pq + p2q2 + p3q3.
(13.58)
Note that each term is easily computed from the previous terms. In general,
for an arbitrary binary process {Xi},
F(xn) =
n

k=1
p(xk−10)xk.
(13.59)
The probability transform thus forms an invertible mapping from inﬁ-
nite source sequences to incompressible inﬁnite binary sequences. We
now consider the compression achieved by this transformation on ﬁnite
sequences. Let X1, X2, . . . , Xn be a sequence of binary random vari-
ables of length n, and let x1, x2, . . . , xn be a particular outcome. We
can treat this sequence as representing an interval [0.x1x2 . . . xn000 . . . ,
0.x1x2 . . . xn1111 . . .),
or
equivalently,
[0.x1x2 . . . xn, 0.x1x2 . . . xn +
( 1
2)n). This is the set of inﬁnite sequences that start with 0.x1x2 · · · xn.
Under the probability transform, this interval gets mapped into another
interval, [FY(0.x1x2 · · · xn), FY(0.x1x2 · · · xn + ( 1
2)n)), whose length is
equal to PX(x1, x2, . . . , xn), the sum of the probabilities of all inﬁnite
sequences that start with 0.x1x2 · · · xn. Under the probability inverse trans-
form, any real number u within this interval maps into a sequence that
starts with x1, x2, . . . , xn, and therefore given u and n, we can recon-
struct x1, x2, . . . , xn. The Shannon–Fano–Elias coding scheme described
earlier allows one to construct a preﬁx-free code of length log
1
p(x1,x2,...,xn) + 2 bits, and therefore it is possible to encode the sequence
x1, x2, . . . , xn with this length. Note that log
1
p(x1,...,xn) is the ideal code-
word length for xn.
The process of encoding the sequence with the cumulative distribution
function described above assumes arbitrary accuracy for the computa-
tion. In practice, though, we have to implement all numbers with ﬁnite
precision, and we describe such an implementation. The key is to consider


