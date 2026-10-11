# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 281

8.6
DIFFERENTIAL ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
255
= −h(g) −

φK log φK
(8.75)
= −h(g) + h(φK),
(8.76)
where the substitution

g log φK =

φK log φK follows from the fact
that g and φK yield the same moments of the quadratic form log φK(x).
□
In particular, the Gaussian distribution maximizes the entropy over
all distributions with the same variance. This leads to the estimation
counterpart to Fano’s inequality. Let X be a random variable with differ-
ential entropy h(X). Let ˆX be an estimate of X, and let E(X −ˆX)2 be
the expected prediction error. Let h(X) be in nats.
Theorem 8.6.6
(Estimation error and differential entropy)
For any
random variable X and estimator ˆX,
E(X −ˆX)2 ≥
1
2πee2h(X),
with equality if and only if X is Gaussian and ˆX is the mean of X.
Proof:
Let ˆX be any estimator of X; then
E(X −ˆX)2 ≥min
ˆX
E(X −ˆX)2
(8.77)
= E (X −E(X))2
(8.78)
= var(X)
(8.79)
≥
1
2πee2h(X),
(8.80)
where (8.78) follows from the fact that the mean of X is the best estimator
for X and the last inequality follows from the fact that the Gaussian
distribution has the maximum entropy for a given variance. We have
equality only in (8.78) only if ˆX is the best estimator (i.e., ˆX is the mean
of X and equality in (8.80) only if X is Gaussian).
□
Corollary
Given side information Y and estimator ˆX(Y), it follows that
E(X −ˆX(Y))2 ≥
1
2πee2h(X|Y).


## PDF page 282

256
DIFFERENTIAL ENTROPY
SUMMARY
h(X) = h(f ) = −

S
f (x) log f (x) dx
(8.81)
f (Xn) .=2−nh(X)
(8.82)
Vol(A(n)
ϵ ) .=2nh(X).
(8.83)
H ([X]2−n) ≈h(X) + n.
(8.84)
h(N(0, σ 2)) = 1
2 log 2πeσ 2.
(8.85)
h(Nn(µ, K)) = 1
2 log(2πe)n|K|.
(8.86)
D(f ||g) =

f log f
g ≥0.
(8.87)
h(X1, X2, . . . , Xn) =
n

i=1
h(Xi|X1, X2, . . . , Xi−1).
(8.88)
h(X|Y) ≤h(X).
(8.89)
h(aX) = h(X) + log |a|.
(8.90)
I (X; Y) =

f (x, y) log f (x, y)
f (x)f (y) ≥0.
(8.91)
max
EXXt=K h(X) = 1
2 log(2πe)n|K|.
(8.92)
E(X −ˆX(Y))2 ≥
1
2πee2h(X|Y).
2nH(X) is the effective alphabet size for a discrete random variable.
2nh(X) is the effective support set size for a continuous random variable.
2C is the effective alphabet size of a channel of capacity C.
PROBLEMS
8.1
Differential entropy.
Evaluate the differential entropy h(X) =
−

f ln f for the following:
(a) The exponential density, f (x) = λe−λx , x ≥0.


## PDF page 283

PROBLEMS
257
(b) The Laplace density, f (x) = 1
2λe−λ|x|.
(c) The sum of X1 and X2, where X1 and X2 are independent
normal random variables with means µi and variances σ 2
i , i =
1, 2.
8.2
Concavity of determinants.
Let K1 and K2 be two symmetric non-
negative deﬁnite n × n matrices. Prove the result of Ky Fan [199]:
| λK1 + λK2 |≥| K1 |λ| K2 |λ
for 0 ≤λ ≤1, λ = 1 −λ,
where | K | denotes the determinant of K. [Hint: Let Z = Xθ,
where X1 ∼N(0, K1), X2 ∼N(0, K2) and θ = Bernoulli(λ). Then
use h(Z | θ) ≤h(Z).]
8.3
Uniformly distributed noise.
Let the input random variable X to
a channel be uniformly distributed over the interval −1
2 ≤x ≤+1
2.
Let the output of the channel be Y = X + Z, where the noise ran-
dom variable is uniformly distributed over the interval −a/2 ≤z ≤
+a/2.
(a) Find I (X; Y) as a function of a.
(b) For a = 1 ﬁnd the capacity of the channel when the input X
is peak-limited; that is, the range of X is limited to −1
2 ≤x ≤
+1
2. What probability distribution on X maximizes the mutual
information I (X; Y)?
(c) (Optional) Find the capacity of the channel for all values of a,
again assuming that the range of X is limited to −1
2 ≤x ≤+1
2.
8.4
Quantized random variables.
Roughly how many bits are required
on the average to describe to three-digit accuracy the decay time
(in years) of a radium atom if the half-life of radium is 80 years?
Note that half-life is the median of the distribution.
8.5
Scaling.
Let h(X) = −

f (x) log f (x) dx. Show
h(AX) = log | det(A) | + h(X).
8.6
Variational inequality.
Verify for positive random variables X
that
log EP (X) = sup
Q

EQ(log X) −D(Q||P )

,
(8.93)
where EP (X) = 
x xP (x) and D(Q||P ) = 
x Q(x) log Q(x)
P(x),
and the supremum is over all Q(x)≥0,  Q(x)=1. It is enough
to extremize J(Q)=EQ ln X−D(Q||P )+λ( Q(x)−1).


## PDF page 284

258
DIFFERENTIAL ENTROPY
8.7
Differential entropy bound on discrete entropy.
Let X be a dis-
crete random variable on the set X = {a1, a2, . . .} with Pr(X =
ai) = pi. Show that
H(p1, p2, . . .) ≤1
2 log(2πe)


∞

i=1
pii2 −
 ∞

i=1
ipi
2
+ 1
12

.
(8.94)
Moreover, for every permutation σ,
H(p1, p2, . . .) ≤1
2 log(2πe)


∞

i=1
pσ(i)i2 −
 ∞

i=1
ipσ(i)
2
+ 1
12

.
(8.95)
[Hint: Construct a random variable X′ such that Pr(X′ = i) = pi.
Let U be a uniform (0,1] random variable and let Y = X′ + U,
where X′ and U are independent. Use the maximum entropy bound
on Y to obtain the bounds in the problem. This bound is due to
Massey (unpublished) and Willems (unpublished).]
8.8
Channel with uniformly distributed noise.
Consider a additive
channel whose input alphabet X = {0,±1,±2} and whose output
Y = X+Z, where Z is distributed uniformly over the interval
[−1, 1]. Thus, the input of the channel is a discrete random vari-
able, whereas the output is continuous. Calculate the capacity C =
maxp(x) I (X; Y) of this channel.
8.9
Gaussian mutual information.
Suppose that (X, Y, Z) are jointly
Gaussian and that X →Y →Z forms a Markov chain. Let X and
Y have correlation coefﬁcient ρ1 and let Y and Z have correlation
coefﬁcient ρ2. Find I (X; Z).
8.10
Shape of the typical set.
Let Xi be i.i.d. ∼f (x), where
f (x) = ce−x4.
Let h = −

f ln f . Describe the shape (or form) or the typical set
A(n)
ϵ
= {xn ∈Rn : f (xn) ∈2−n(h±ϵ)}.
8.11
Nonergodic Gaussian process.
Consider a constant signal V in
the presence of iid observational noise {Zi}. Thus, Xi = V + Zi,
where V ∼N(0, S) and Zi are iid ∼N(0, N). Assume that V and
{Zi} are independent.
(a) Is {Xi} stationary?


## PDF page 285

HISTORICAL NOTES
259
(b) Find limn−→∞1
n
n
i=1 Xi. Is the limit random?
(c) What is the entropy rate h of {Xi}?
(d) Find the least-mean-squared error predictor ˆXn+1(Xn), and ﬁnd
σ 2
∞= limn−→∞E( ˆXn −Xn)2.
(e) Does {Xi} have an AEP? That is, does −1
n log f (Xn) −→h?
HISTORICAL NOTES
Differential entropy and discrete entropy were introduced in Shannon’s
original paper [472]. The general rigorous deﬁnition of relative entropy
and mutual information for arbitrary random variables was developed by
Kolmogorov [319] and Pinsker [425], who deﬁned mutual information as
supP,Q I ([X]P; [Y]Q), where the supremum is over all ﬁnite partitions P
and Q.


## PDF page 286



## PDF page 287

CHAPTER 9
GAUSSIAN CHANNEL
The most important continuous alphabet channel is the Gaussian channel
depicted in Figure 9.1. This is a time-discrete channel with output Yi at
time i, where Yi is the sum of the input Xi and the noise Zi. The noise
Zi is drawn i.i.d. from a Gaussian distribution with variance N. Thus,
Yi = Xi + Zi,
Zi ∼N(0, N).
(9.1)
The noise Zi is assumed to be independent of the signal Xi. This channel
is a model for some common communication channels, such as wired and
wireless telephone channels and satellite links. Without further conditions,
the capacity of this channel may be inﬁnite. If the noise variance is zero,
the receiver receives the transmitted symbol perfectly. Since X can take
on any real value, the channel can transmit an arbitrary real number with
no error.
If the noise variance is nonzero and there is no constraint on the input,
we can choose an inﬁnite subset of inputs arbitrarily far apart, so that
they are distinguishable at the output with arbitrarily small probability of
error. Such a scheme has an inﬁnite capacity as well. Thus if the noise
variance is zero or the input is unconstrained, the capacity of the channel
is inﬁnite.
The most commonlimitationonthe input is anenergyorpowerconstraint.
We assume an average power constraint. For any codeword (x1, x2, . . . , xn)
transmitted over the channel, we require that
1
n
n

i=1
x2
i ≤P.
(9.2)
This communication channel models many practical channels, includ-
ing radio and satellite links. The additive noise in such channels may be
due to a variety of causes. However, by the central limit theorem, the
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
261


## PDF page 288

262
GAUSSIAN CHANNEL
Zi
Yi
Xi
FIGURE 9.1. Gaussian channel.
cumulative effect of a large number of small random effects will be
approximately normal, so the Gaussian assumption is valid in a large
number of situations.
We ﬁrst analyze a simple suboptimal way to use this channel. Assume
that we want to send 1 bit over the channel in one use of the channel.
Given the power constraint, the best that we can do is to send one of
two levels, +
√
P or −
√
P . The receiver looks at the corresponding Y
received and tries to decide which of the two levels was sent. Assuming
that both levels are equally likely (this would be the case if we wish to
send exactly 1 bit of information), the optimum decoding rule is to decide
that +
√
P was sent if Y > 0 and decide −
√
P was sent if Y < 0. The
probability of error with such a decoding scheme is
Pe = 1
2 Pr(Y < 0|X = +
√
P) + 1
2 Pr(Y > 0|X = −
√
P )
(9.3)
= 1
2 Pr(Z < −
√
P|X = +
√
P ) + 1
2 Pr(Z >
√
P |X = −
√
P ) (9.4)
= Pr(Z >
√
P )
(9.5)
= 1 −

P/N

,
(9.6)
where (x) is the cumulative normal function
(x) =
 x
−∞
1
√
2π
e
−t2
2 dt.
(9.7)
Using such a scheme, we have converted the Gaussian channel into a dis-
crete binary symmetric channel with crossover probability Pe. Similarly,
by using a four-level input signal, we can convert the Gaussian channel


