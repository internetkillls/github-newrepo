# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 361

SUMMARY
335
as a double maximization using Lemma 10.8.1,
C = max
q(x|y) max
r(x)

x

y
r(x)p(y|x) log q(x|y)
r(x) .
(10.145)
In this case, the Csisz´ar–Tusnady algorithm becomes one of alternating
maximization—we start with a guess of the maximizing distribution r(x)
and ﬁnd the best conditional distribution, which is, by Lemma 10.8.1,
q(x|y) =
r(x)p(y|x)

x r(x)p(y|x).
(10.146)
For this conditional distribution, we ﬁnd the best input distribution
r(x) by solving the constrained maximization problem with Lagrange
multipliers. The optimum input distribution is
r(x) =

y (q(x|y))p(y|x)

x

y (q(x|y))p(y|x),
(10.147)
which we can use as the basis for the next iteration.
These algorithms for the computation of the channel capacity and the
rate distortion function were established by Blahut [65] and Arimoto [25]
and the convergence for the rate distortion computation was proved by
Csisz´ar [139]. The alternating minimization procedure of Csisz´ar and Tus-
nady can be specialized to many other situations as well, including the EM
algorithm [166], and the algorithm for ﬁnding the log-optimal portfolio
for a stock market [123].
SUMMARY
Rate distortion. The rate distortion function for a source X ∼p(x)
and distortion measure d(x, ˆx) is
R(D) =
min
p(ˆx|x):
(x,ˆx) p(x)p(ˆx|x)d(x,ˆx)≤D I (X; ˆX),
(10.148)
where the minimization is over all conditional distributions p(ˆx|x) for
which the joint distribution p(x, ˆx) = p(x)p(ˆx|x) satisﬁes the expected
distortion constraint.


## PDF page 362

336
RATE DISTORTION THEORY
Rate distortion theorem. If R > R(D), there exists a sequence of
codes
ˆXn(Xn) with the number of codewords | ˆXn(·)| ≤2nR with
Ed(Xn, ˆXn(Xn)) →D. If R < R(D), no such codes exist.
Bernoulli source. For a Bernoulli source with Hamming distortion,
R(D) = H(p) −H(D).
(10.149)
Gaussian source. For a Gaussian source with squared-error distortion,
R(D) = 1
2 log σ 2
D .
(10.150)
Source–channel separation. A source with rate distortion R(D) can
be sent over a channel of capacity C and recovered with distortion D
if and only if R(D) < C.
Multivariate Gaussian source. The rate distortion function for a mul-
tivariate normal vector with Euclidean mean-squared-error distortion is
given by reverse water-ﬁlling on the eigenvalues.
PROBLEMS
10.1
One-bit quantization of a single Gaussian random variable.
Let
X ∼N(0, σ 2) and let the distortion measure be squared error.
Here we do not allow block descriptions. Show that the optimum
reproduction points for 1-bit quantization are ±

2
π σ and that the
expected distortion for 1-bit quantization is π−2
π σ 2. Compare this
with
the
distortion
rate
bound
D = σ 22−2R
for
R = 1.
10.2
Rate distortion function with inﬁnite distortion.
Find the rate dis-
tortion function R(D) = min I (X; ˆX) for X ∼Bernoulli ( 1
2) and
distortion
d(x, ˆx) =



0,
x = ˆx
1,
x = 1, ˆx = 0
∞,
x = 0, ˆx = 1.


## PDF page 363

PROBLEMS
337
10.3
Rate distortion for binary source with asymmetric distortion .
Fix
p(ˆx|x) and evaluate I (X; ˆX) and D for
X ∼Bernoulli
1
2

,
d(x, ˆx) =

0
a
b
0

.
(The rate distortion function cannot be expressed in closed form.)
10.4
Properties of R(D).
Consider a discrete source X ∈X =
{1, 2, . . . , m} with distribution p1, p2, . . . , pm and a distortion
measure d(i, j). Let R(D) be the rate distortion function for
this source and distortion measure. Let d′(i, j) = d(i, j) −wi be
a new distortion measure, and let R′(D) be the corresponding
rate distortion function. Show that R′(D) = R(D + w), where
w =  piwi, and use this to show that there is no essential loss of
generality in assuming that minˆx d(i, ˆx) = 0 (i.e., for each x ∈X,
there is one symbol ˆx that reproduces the source with zero dis-
tortion). This result is due to Pinkston [420].
10.5
Rate distortion for uniform source with Hamming distortion.
Consider a source X uniformly distributed on the set {1, 2, . . . , m}.
Find the rate distortion function for this source with Hamming
distortion; that is,
d(x, ˆx) =

0
if x = ˆx,
1
if x ̸= ˆx.
10.6
Shannon lower bound for the rate distortion function.
Consider
a source X with a distortion measure d(x, ˆx) that satisﬁes the
following property: All columns of the distortion matrix are per-
mutations of the set {d1, d2, . . . , dm}. Deﬁne the function
φ(D) =
max
p:m
i=1 pidi≤D H(p).
(10.151)
The Shannon lower bound on the rate distortion function [485]
is proved by the following steps:
(a) Show that φ(D) is a concave function of D.
(b) Justify the following series of inequalities for I (X; ˆX) if
Ed(X, ˆX) ≤D,
I (X; ˆX) = H(X) −H(X| ˆX)
(10.152)


## PDF page 364

338
RATE DISTORTION THEORY
= H(X) −

ˆx
p(ˆx)H(X| ˆX = ˆx)
(10.153)
≥H(X) −

ˆx
p(ˆx)φ(Dˆx)
(10.154)
≥H(X) −φ
	
ˆx
p(ˆx)Dˆx

(10.155)
≥H(X) −φ(D),
(10.156)
where Dˆx = 
x p(x|ˆx)d(x, ˆx).
(c) Argue that
R(D) ≥H(X) −φ(D),
(10.157)
which is the Shannon lower bound on the rate distortion func-
tion.
(d) If, in addition, we assume that the source has a uniform
distribution and that the rows of the distortion matrix are per-
mutations of each other, then R(D) = H(X) −φ(D) (i.e., the
lower bound is tight).
10.7
Erasure distortion.
Consider X ∼Bernoulli (1
2), and let the dis-
tortion measure be given by the matrix
d(x, ˆx) =

0
1
∞
∞
1
0

.
(10.158)
Calculate the rate distortion function for this source. Can you
suggest a simple scheme to achieve any value of the rate distortion
function for this source?
10.8
Bounds on the rate distortion function for squared-error distortion.
For the case of a continuous random variable X with mean zero
and variance σ 2 and squared-error distortion, show that
h(X) −1
2 log(2πeD) ≤R(D) ≤1
2 log σ 2
D .
(10.159)
For the upper bound, consider the following joint distribution:


## PDF page 365

PROBLEMS
339
Z ~
0,
Ds2
s2 − D
X 
X 
^
X
(X + Z )
=
^
s2 − D
s2
s2 − D
s2
Are Gaussian random variables harder or easier to describe than
other random variables with the same variance?
10.9
Properties of optimal rate distortion code.
A good (R, D) rate
distortion code with R ≈R(D) puts severe constraints on the rela-
tionship of the source Xn and the representations ˆXn. Examine the
chain of inequalities (10.58–10.71) considering the conditions for
equality and interpret as properties of a good code. For example,
equality in (10.59) implies that ˆXn is a deterministic function
of Xn.
10.10
Rate distortion.
Find and verify the rate distortion function R(D)
for X uniform on X = {1, 2, . . . , 2m} and
d(x, ˆx) =

1
for x −ˆx odd,
0
for x −ˆx even,
where ˆX is deﬁned on ˆX = {1, 2, . . . , 2m}. (You may wish to use
the Shannon lower bound in your argument.)
10.11
Lower bound.
Let
X ∼
e−x4
 ∞
−∞e−x4dx
and

x4e−x4dx

e−x4dx
= c.
Deﬁne g(a) = max h(X) over all densities such that EX4 ≤a.
Let R(D) be the rate distortion function for X with the density
above and with distortion criterion d(x, ˆx) = (x −ˆx)4. Show that
R(D) ≥g(c) −g(D).


## PDF page 366

340
RATE DISTORTION THEORY
10.12
Adding a column to the distortion matrix.
Let R(D) be the rate
distortion function for an i.i.d. process with probability mass func-
tion p(x) and distortion function d(x, ˆx), x ∈X, ˆx ∈ˆX. Now
suppose that we add a new reproduction symbol ˆx0 to ˆX with asso-
ciated distortion d(x, ˆx0), x ∈X. Does this increase or decrease
R(D), and why?
10.13
Simpliﬁcation.
Suppose that X = {1, 2, 3, 4}, ˆX = {1, 2, 3, 4},
p(i) = 1
4, i = 1, 2, 3, 4, and X1, X2, . . . are i.i.d. ∼p(x). The
distortion matrix d(x, ˆx) is given by
1
2
3
4
1
0
0
1
1
2
0
0
1
1
3
1
1
0
0
4
1
1
0
0
(a) Find R(0), the rate necessary to describe the process with
zero distortion.
(b) Find the rate distortion function R(D). There are some irrel-
evant distinctions in alphabets X and ˆX, which allow the
problem to be collapsed.
(c) Suppose that we have a nonuniform distribution p(i) = pi,
i = 1, 2, 3, 4. What is R(D)?
10.14
Rate distortion for two independent sources.
Can one compress
two independent sources simultaneously better than by compress-
ing the sources individually? The following problem addresses this
question. Let {Xi} be i.i.d. ∼p(x) with distortion d(x, ˆx) and rate
distortion function RX(D). Similarly, let {Yi} be i.i.d. ∼p(y) with
distortion d(y, ˆy) and rate distortion function RY(D). Suppose we
now wish to describe the process {(Xi, Yi)} subject to distortions
Ed(X, ˆX) ≤D1 and Ed(Y, ˆY) ≤D2. Thus, a rate RX,Y(D1, D2)
is sufﬁcient, where
RX,Y(D1, D2) =
min
p(ˆx, ˆy|x,y):Ed(X, ˆX)≤D1,Ed(Y, ˆY)≤D2
I (X, Y; ˆX, ˆY).
Now suppose that the {Xi} process and the {Yi} process are inde-
pendent of each other.
(a) Show that
RX,Y(D1, D2) ≥RX(D1) + RY(D2).


## PDF page 367

PROBLEMS
341
(b) Does equality hold?
Now answer the question.
10.15
Distortion rate function.
Let
D(R) =
min
p(ˆx|x):I(X; ˆX)≤R
Ed(X, ˆX)
(10.160)
be the distortion rate function.
(a) Is D(R) increasing or decreasing in R?
(b) Is D(R) convex or concave in R?
(c) Converse for distortion rate functions: We now wish to prove
the converse by focusing on D(R). Let X1, X2, . . . , Xn be
i.i.d. ∼p(x). Suppose that one is given a (2nR, n) rate dis-
tortion code Xn →i(Xn) →ˆXn(i(Xn)), with i(Xn) ∈2nR,
and suppose that the resulting distortion is D = Ed(Xn, ˆXn
(i(Xn))). We must show that D ≥D(R). Give reasons for the
following steps in the proof:
D = Ed(Xn, ˆXn(i(Xn)))
(10.161)
(a)
= E 1
n
n

i=1
d(Xi, ˆXi)
(10.162)
(b)
= 1
n
n

i=1
Ed(Xi, ˆXi)
(10.163)
(c)
≥1
n
n

i=1
D

I (Xi; ˆXi)
 
(10.164)
(d)
≥D
	
1
n
n

i=1
I (Xi; ˆXi)

(10.165)
(e)
≥D
1
nI (Xn; ˆXn)

(10.166)
(f)≥D(R).
(10.167)
10.16
Probability of conditionally typical sequences.
In Chapter 7 we
calculated the probability that two independently drawn sequences
Xn and Y n are weakly jointly typical. To prove the rate distor-
tion theorem, however, we need to calculate this probability when


## PDF page 368

342
RATE DISTORTION THEORY
one of the sequences is ﬁxed and the other is random. The tech-
niques of weak typicality allow us only to calculate the average
set size of the conditionally typical set. Using the ideas of strong
typicality, on the other hand, provides us with stronger bounds
that work for all typical xn sequences. We outline the proof that
Pr{(xn, Y n) ∈A∗(n)
ϵ
} ≈2−nI(X;Y) for all typical xn. This approach
was introduced by Berger [53] and is fully developed in the book
by Csisz´ar and K¨orner [149].
Let (Xi, Yi) be drawn i.i.d. ∼p(x, y). Let the marginals of X and
Y be p(x) and p(y), respectively.
(a) Let A∗(n)
ϵ
be the strongly typical set for X. Show that
|A∗(n)
ϵ
| .=2nH(X).
(10.168)
(Hint: Theorems 11.1.1 and 11.1.3.)
(b) The joint type of a pair of sequences (xn, yn) is the proportion
of times (xi, yi) = (a, b) in the pair of sequences:
pxn,yn(a, b) = 1
nN(a, b|xn, yn) = 1
n
n

i=1
I (xi = a, yi = b).
(10.169)
The conditional type of a sequence yn given xn is a stochastic
matrix that gives the proportion of times a particular element
of Y occurred with each element of X in the pair of sequences.
Speciﬁcally, the conditional type Vyn|xn(b|a) is deﬁned as
Vyn|xn(b|a) = N(a, b|xn, yn)
N(a|xn)
.
(10.170)
Show that the number of conditional types is bounded by (n +
1)|X||Y|.
(c) The set of sequences yn ∈Yn with conditional type V with
respect to a sequence xn is called the conditional type class
TV (xn). Show that
1
(n + 1)|X||Y| 2nH(Y|X) ≤|TV (xn)| ≤2nH(Y|X).
(10.171)
(d) The sequence yn ∈Yn is said to be ϵ-strongly conditionally
typical with the sequence xn with respect to the conditional
distribution V (·|·) if the conditional type is close to V . The
conditional type should satisfy the following two conditions:


