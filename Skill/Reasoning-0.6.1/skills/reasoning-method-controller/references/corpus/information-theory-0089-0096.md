# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 89

3.3
HIGH-PROBABILITY SETS AND THE TYPICAL SET
63
We argue that B(n)
δ
must have signiﬁcant intersection with A(n)
ϵ
and there-
fore must have about as many elements. In Problem 3.3.11, we outline
the proof of the following theorem.
Theorem 3.3.1
Let X1, X2, . . . , Xn be i.i.d. ∼p(x). For δ < 1
2 and
any δ′ > 0, if Pr{B(n)
δ } > 1 −δ, then
1
n log |B(n)
δ | > H −δ′
for n sufﬁciently large.
(3.25)
Thus, B(n)
δ
must have at least 2nH elements, to ﬁrst order in the expo-
nent. But A(n)
ϵ
has 2n(H±ϵ) elements. Therefore, A(n)
ϵ
is about the same
size as the smallest high-probability set.
We will now deﬁne some new notation to express equality to ﬁrst order
in the exponent.
Deﬁnition
The notation an
.= bn means
lim
n→∞
1
n log an
bn
= 0.
(3.26)
Thus, an
.= bn implies that an and bn are equal to the ﬁrst order in the
exponent.
We can now restate the above results: If δn →0 and ϵn →0, then
|B(n)
δn | .=|A(n)
ϵn | .=2nH.
(3.27)
To illustrate the difference between A(n)
ϵ
and B(n)
δ , let us con-
sider a Bernoulli sequence X1, X2, . . . , Xn with parameter p = 0.9. [A
Bernoulli(θ) random variable is a binary random variable that takes on
the value 1 with probability θ.] The typical sequences in this case are the
sequences in which the proportion of 1’s is close to 0.9. However, this
does not include the most likely single sequence, which is the sequence of
all 1’s. The set B(n)
δ
includes all the most probable sequences and there-
fore includes the sequence of all 1’s. Theorem 3.3.1 implies that A(n)
ϵ
and
B(n)
δ
must both contain the sequences that have about 90% 1’s, and the
two sets are almost equal in size.


## PDF page 90

64
ASYMPTOTIC EQUIPARTITION PROPERTY
SUMMARY
AEP. “Almost all events are almost equally surprising.” Speciﬁcally,
if X1, X2, . . . are i.i.d. ∼p(x), then
−1
n log p(X1, X2, . . . , Xn) →H(X) in probability.
(3.28)
Deﬁnition. The typical set A(n)
ϵ
is the set of sequences x1, x2, . . . , xn
satisfying
2−n(H(X)+ϵ) ≤p(x1, x2, . . . , xn) ≤2−n(H(X)−ϵ).
(3.29)
Properties of the typical set
1. If (x1, x2, . . . , xn) ∈A(n)
ϵ , then p(x1, x2, . . . , xn) = 2−n(H±ϵ).
2. Pr

A(n)
ϵ

> 1 −ϵ for n sufﬁciently large.
3.
A(n)
ϵ
 ≤2n(H(X)+ϵ), where |A| denotes the number of elements in
set A.
Deﬁnition. an
.=bn means that 1
n log an
bn →0 as n →∞.
Smallest probable set. Let X1, X2, . . . , Xn be i.i.d. ∼p(x), and for
δ < 1
2, let B(n)
δ
⊂Xn be the smallest set such that Pr{B(n)
δ } ≥1 −δ.
Then
|B(n)
δ | .=2nH.
(3.30)
PROBLEMS
3.1
Markov’s inequality and Chebyshev’s inequality
(a) (Markov’s inequality) For any nonnegative random variable X
and any t > 0, show that
Pr {X ≥t} ≤EX
t .
(3.31)
Exhibit a random variable that achieves this inequality with
equality.
(b) (Chebyshev’s inequality) Let Y be a random variable with
mean µ and variance σ 2. By letting X = (Y −µ)2, show that


## PDF page 91

PROBLEMS
65
for any ϵ > 0,
Pr {|Y −µ| > ϵ} ≤σ 2
ϵ2 .
(3.32)
(c) (Weak law of large numbers) Let Z1, Z2, . . . , Zn be a sequence
of i.i.d. random variables with mean µ and variance σ 2. Let
Zn = 1
n
n
i=1
Zi be the sample mean. Show that
Pr
Zn −µ
 > ϵ

≤σ 2
nϵ2 .
(3.33)
Thus, Pr
Zn −µ
 > ϵ

→0 as n →∞. This is known as the
weak law of large numbers.
3.2
AEP and mutual information.
Let (Xi, Yi) be i.i.d. ∼p(x, y). We
form the log likelihood ratio of the hypothesis that X and Y are
independent vs. the hypothesis that X and Y are dependent. What
is the limit of
1
n log p(Xn)p(Y n)
p(Xn, Y n) ?
3.3
Piece of cake.
A cake is sliced roughly in half, the largest piece being chosen each
time, the other pieces discarded. We will assume that a random cut
creates pieces of proportions
P =

( 2
3, 1
3)
with probability 3
4
( 2
5, 3
5)
with probability 1
4
Thus, for example, the ﬁrst cut (and choice of largest piece) may
result in a piece of size 3
5. Cutting and choosing from this piece
might reduce it to size
3
5
  2
3

at time 2, and so on. How large, to
ﬁrst order in the exponent, is the piece of cake after n cuts?
3.4
AEP.
Let Xi be iid ∼p(x), x ∈{1, 2, . . . , m}. Let µ = EX and
H = − p(x) log p(x). Let An = {xn ∈Xn : | −1
n log p(xn) −
H| ≤ϵ}. Let Bn = {xn ∈Xn : | 1
n
n
i=1 Xi −µ| ≤ϵ}.
(a) Does Pr{Xn ∈An} −→1?
(b) Does Pr{Xn ∈An ∩Bn} −→1?


## PDF page 92

66
ASYMPTOTIC EQUIPARTITION PROPERTY
(c) Show that |An ∩Bn| ≤2n(H+ϵ) for all n.
(d) Show that |An ∩Bn| ≥
1
2

2n(H−ϵ) for n sufﬁciently large.
3.5
Sets deﬁned by probabilities.
Let X1, X2, . . . be an i.i.d. sequence
of discrete random variables with entropy H(X). Let
Cn(t) = {xn ∈Xn : p(xn) ≥2−nt}
denote the subset of n-sequences with probabilities ≥2−nt.
(a) Show that |Cn(t)| ≤2nt.
(b) For what values of t does P ({Xn ∈Cn(t)}) →1?
3.6
AEP-like limit.
Let X1, X2, . . . be i.i.d. drawn according to prob-
ability mass function p(x). Find
lim
n→∞(p(X1, X2, . . . , Xn))
1
n.
3.7
AEP and source coding.
A discrete memoryless source emits a
sequence of statistically independent binary digits with probabilities
p(1) = 0.005 and p(0) = 0.995. The digits are taken 100 at a time
and a binary codeword is provided for every sequence of 100 digits
containing three or fewer 1’s.
(a) Assuming that all codewords are the same length, ﬁnd the min-
imum length required to provide codewords for all sequences
with three or fewer 1’s.
(b) Calculate the probability of observing a source sequence for
which no codeword has been assigned.
(c) Use Chebyshev’s inequality to bound the probability of observ-
ing a source sequence for which no codeword has been assign-
ed. Compare this bound with the actual probability computed
in part (b).
3.8
Products.
Let
X =



1,
with probability 1
2
2,
with probability 1
4
3,
with probability 1
4
Let X1, X2, . . . be drawn i.i.d. according to this distribution. Find
the limiting behavior of the product
(X1X2 · · · Xn)
1
n .


## PDF page 93

PROBLEMS
67
3.9
AEP.
Let X1, X2, . . . be independent, identically distributed ran-
dom variables drawn according to the probability mass function
p(x), x ∈{1, 2, . . . , m}. Thus, p(x1, x2, . . . , xn) = n
i=1 p(xi). We
know that −1
n log p(X1, X2, . . . , Xn) →H(X) in probability. Let
q(x1, x2, . . . , xn) = n
i=1 q(xi), where q is another probability
mass function on {1, 2, . . . , m}.
(a) Evaluate lim −1
n log q(X1, X2, . . . , Xn), where X1, X2, . . . are
i.i.d. ∼p(x).
(b) Now
evaluate
the
limit
of
the
log
likelihood
ratio
1
n log q(X1,...,Xn)
p(X1,...,Xn) when X1, X2, . . . are i.i.d. ∼p(x). Thus, the
odds favoring q are exponentially small when p is true.
3.10
Random box size.
An n-dimensional rectangular box with sides X1, X2, X3, . . . , Xn is
to be constructed. The volume is Vn = n
i=1 Xi. The edge length l
of a n-cube with the same volume as the random box is l = V 1/n
n
.
Let X1, X2, . . . be i.i.d. uniform random variables over the unit
interval [0, 1]. Find limn→∞V 1/n
n
and compare to (EVn)
1
n . Clearly,
the expected edge length does not capture the idea of the volume
of the box. The geometric mean, rather than the arithmetic mean,
characterizes the behavior of products.
3.11
Proof of Theorem 3.3.1.
This problem shows that the size of the
smallest “probable” set is about 2nH. Let X1, X2, . . . , Xn be i.i.d.
∼p(x). Let B(n)
δ
⊂Xn such that Pr(B(n)
δ ) > 1 −δ. Fix ϵ < 1
2.
(a) Given any two sets A, B such that Pr(A) > 1 −ϵ1 and Pr(B) >
1 −ϵ2, show that Pr(A ∩B) > 1 −ϵ1 −ϵ2. Hence, Pr(A(n)
ϵ
∩
B(n)
δ ) ≥1 −ϵ −δ.
(b) Justify the steps in the chain of inequalities
1 −ϵ −δ ≤Pr(A(n)
ϵ
∩B(n)
δ )
(3.34)
=

A(n)
ϵ ∩B(n)
δ
p(xn)
(3.35)
≤

A(n)
ϵ ∩B(n)
δ
2−n(H−ϵ)
(3.36)
= |A(n)
ϵ
∩B(n)
δ |2−n(H−ϵ)
(3.37)
≤|B(n)
δ |2−n(H−ϵ).
(3.38)
(c) Complete the proof of the theorem.


## PDF page 94

68
ASYMPTOTIC EQUIPARTITION PROPERTY
3.12
Monotonic convergence of the empirical distribution.
Let ˆpn denote the empirical probability mass function correspond-
ing to X1, X2, . . . , Xn i.i.d. ∼p(x), x ∈X. Speciﬁcally,
ˆpn(x) = 1
n
n

i=1
I (Xi = x)
is the proportion of times that Xi = x in the ﬁrst n samples, where
I is the indicator function.
(a) Show for X binary that
ED( ˆp2n ∥p) ≤ED( ˆpn ∥p).
Thus, the expected relative entropy “distance” from the empir-
ical distribution to the true distribution decreases with sample
size. (Hint: Write ˆp2n = 1
2 ˆpn + 1
2 ˆp′
n and use the convexity
of D.)
(b) Show for an arbitrary discrete X that
ED( ˆpn ∥p) ≤ED( ˆpn−1 ∥p).
(Hint: Write ˆpn as the average of n empirical mass functions
with each of the n samples deleted in turn.)
3.13
Calculation of typical set.
To clarify the notion of a typical set
A(n)
ϵ
and the smallest set of high probability B(n)
δ , we will calculate
the set for a simple example. Consider a sequence of i.i.d. binary
random variables, X1, X2, . . . , Xn, where the probability that Xi =
1 is 0.6 (and therefore the probability that Xi = 0 is 0.4).
(a) Calculate H(X).
(b) With n = 25 and ϵ = 0.1, which sequences fall in the typi-
cal set A(n)
ϵ ? What is the probability of the typical set? How
many elements are there in the typical set? (This involves com-
putation of a table of probabilities for sequences with k 1’s,
0 ≤k ≤25, and ﬁnding those sequences that are in the typi-
cal set.)
(c) How many elements are there in the smallest set that has prob-
ability 0.9?
(d) How many elements are there in the intersection of the sets in
parts (b) and (c)? What is the probability of this intersection?


## PDF page 95

HISTORICAL NOTES
69
k
n
k

n
k

pk(1 −p)n−k
−1
n log p(xn)
0
1
0.000000
1.321928
1
25
0.000000
1.298530
2
300
0.000000
1.275131
3
2300
0.000001
1.251733
4
12650
0.000007
1.228334
5
53130
0.000054
1.204936
6
177100
0.000227
1.181537
7
480700
0.001205
1.158139
8
1081575
0.003121
1.134740
9
2042975
0.013169
1.111342
10
3268760
0.021222
1.087943
11
4457400
0.077801
1.064545
12
5200300
0.075967
1.041146
13
5200300
0.267718
1.017748
14
4457400
0.146507
0.994349
15
3268760
0.575383
0.970951
16
2042975
0.151086
0.947552
17
1081575
0.846448
0.924154
18
480700
0.079986
0.900755
19
177100
0.970638
0.877357
20
53130
0.019891
0.853958
21
12650
0.997633
0.830560
22
2300
0.001937
0.807161
23
300
0.999950
0.783763
24
25
0.000047
0.760364
25
1
0.000003
0.736966
HISTORICAL NOTES
The asymptotic equipartition property (AEP) was ﬁrst stated by Shan-
non in his original 1948 paper [472], where he proved the result for
i.i.d. processes and stated the result for stationary ergodic processes.
McMillan [384] and Breiman [74] proved the AEP for ergodic ﬁnite
alphabet sources. The result is now referred to as the AEP or the Shan-
non–McMillan–Breiman theorem. Chung [101] extended the theorem to
the case of countable alphabets and Moy [392], Perez [417], and Kieffer
[312] proved the L1 convergence when {Xi} is continuous valued and
ergodic. Barron [34] and Orey [402] proved almost sure convergence for
real-valued ergodic processes; a simple sandwich argument (Algoet and
Cover [20]) will be used in Section 16.8 to prove the general AEP.


## PDF page 96



