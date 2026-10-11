# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 321

PROBLEMS
295
(a) What is the capacity of this channel? This should be a pleasant
surprise.
(b) How would you signal to achieve capacity?
9.15
Discrete input, continuous output channel.
Let Pr{X = 1} = p,
Pr{X = 0} = 1 −p, and let Y = X + Z, where Z is uniform over
the interval [0, a], a > 1, and Z is independent of X.
(a) Calculate
I (X; Y) = H(X) −H(X|Y).
(b) Now calculate I (X; Y) the other way by
I (X; Y) = h(Y) −h(Y|X).
(c) Calculate the capacity of this channel by maximizing over p.
9.16
Gaussian mutual information.
Suppose that (X, Y, Z) are jointly
Gaussian and that X →Y →Z forms a Markov chain. Let X and
Y have correlation coefﬁcient ρ1 and let Y and Z have correlation
coefﬁcient ρ2. Find I (X; Z).
9.17
Impulse power.
Consider the additive white Gaussian channel
Zi
Yi
Xi
∑
where Zi ∼N(0, N), and the input signal has average power con-
straint P .
(a) Suppose that we use all our power at time 1 (i.e., EX2
1 = nP
and EX2
i = 0 for i = 2, 3, . . . , n). Find
max
f (xn)
I (Xn; Y n)
n
,
where the maximization is over all distributions f (xn) subject
to the constraint EX2
1 = nP and EX2
i = 0 for i = 2, 3, . . . , n.


## PDF page 322

296
GAUSSIAN CHANNEL
(b) Find
max
f (xn): E

1
n
n
i=1 X2
i

≤P
1
nI (Xn; Y n)
and compare to part (a).
9.18
Gaussian channel with time-varying mean.
Find the capacity of
the following Gaussian channel:
Zi
Xi
Yi
Let Z1, Z2, . . . be independent and let there be a power constraint
P on xn(W). Find the capacity when:
(a) µi = 0, for all i.
(b) µi = ei,
i = 1, 2, . . .. Assume that µi is known to the trans-
mitter and receiver.
(c) µi unknown, but µi i.i.d. ∼N(0, N1) for all i.
9.19
Parametric form for channel capacity.
Consider m parallel Gaus-
sian channels, Yi = Xi + Zi, where Zi ∼N(0, λi) and the noises
Xi are independent random variables. Thus, C = m
i=1
1
2 log(1 +
(λ−λi)+
λi
), where λ is chosen to satisfy m
i=1(λ −λi)+ = P . Show
that this can be rewritten in the form
P (λ)
= 
i:λi≤λ(λ −λi)
C(λ)
= 
i:λi≤λ
1
2 log λ
λi
.
Here P (λ) is piecewise linear and C(λ) is piecewise logarithmic
in λ.
9.20
Robust decoding.
Consider an additive noise channel whose out-
put Y is given by
Y = X + Z,
where the channel input X is average power limited,
EX2 ≤P,


## PDF page 323

PROBLEMS
297
and the noise process {Zk}∞
k=−∞is i.i.d. with marginal distribution
pZ(z) (not necessarily Gaussian) of power N,
EZ2 = N.
(a) Show that the channel capacity, C = maxEX2≤P I (X; Y), is
lower bounded by CG, where
CG = 1
2 log

1 + P
N

(i.e., the capacity CG corresponding to white Gaussian noise).
(b) Decoding the received vector to the codeword that is closest to
it in Euclidean distance is in general suboptimal if the noise is
non-Gaussian. Show, however, that the rate CG is achievable
even if one insists on performing nearest-neighbor decoding
(minimum Euclidean distance decoding) rather than the optimal
maximum-likelihood or joint typicality decoding (with respect
to the true noise distribution).
(c) Extend the result to the case where the noise is not i.i.d. but is
stationary and ergodic with power N.
(Hint for b and c: Consider a size 2nR random codebook whose
codewords are drawn independently of each other according to a
uniform distribution over the n-dimensional sphere of radius
√
nP .)
(a) Using a symmetry argument, show that conditioned on the
noise vector, the ensemble average probability of error depends
on the noise vector only via its Euclidean norm ∥z∥.
(b) Use a geometric argument to show that this dependence is
monotonic.
(c) Given a rate R < CG, choose some N′ > N such that
R < 1
2 log

1 + P
N′

.
Compare the case where the noise is i.i.d. N(0, N′) to the case
at hand.
(d) Conclude the proof using the fact that the above ensemble of
codebooks can achieve the capacity of the Gaussian channel
(no need to prove that).


## PDF page 324

298
GAUSSIAN CHANNEL
9.21
Mutual information game.
Consider the following channel:
Z
X
Y
Throughout this problem we shall constrain the signal power
EX = 0,
EX2 = P,
(9.176)
and the noise power
EZ = 0,
EZ2 = N,
(9.177)
and assume that X and Z are independent. The channel capacity is
given by I (X; X + Z).
Now for the game. The noise player chooses a distribution on Z to
minimize I (X; X + Z), while the signal player chooses a distribu-
tion on X to maximize I (X; X + Z). Letting X∗∼N(0, P ), Z∗∼
N(0, N), show that Gaussian X∗and Z∗satisfy the saddlepoint
conditions
I (X; X + Z∗) ≤I (X∗; X∗+ Z∗) ≤I (X∗; X∗+ Z).
(9.178)
Thus,
min
Z max
X I (X; X + Z) = max
X min
Z I (X; X + Z)
(9.179)
= 1
2 log

1 + P
N

,
(9.180)
and the game has a value. In particular, a deviation from normal
for either player worsens the mutual information from that player’s
standpoint. Can you discuss the implications of this?
Note: Part of the proof hinges on the entropy power inequality from
Section 17.8, which states that if X and Y are independent random
n-vectors with densities, then
2
2
nh(X+Y) ≥2
2
nh(X) + 2
2
nh(Y).
(9.181)


## PDF page 325

HISTORICAL NOTES
299
9.22
Recovering the noise.
Consider a standard Gaussian channel Y n =
Xn + Zn, where Zi is i.i.d. ∼N(0, N), i = 1, 2, . . . , n, and
1
n
n
i=1 X2
i ≤P. Here we are interested in recovering the noise Zn
and we don’t care about the signal Xn. By sending Xn = (0, 0, . . . ,
0), the receiver gets Y n = Zn and can fully determine the value of
Zn. We wonder how much variability there can be in Xn and still
recover the Gaussian noise Zn. Use of the channel looks like
Zn
Zn(Yn)
Xn
Yn
^
Argue that for some R > 0, the transmitter can arbitrarily send one
of 2nR different sequences of xn without affecting the recovery of
the noise in the sense that
Pr{ ˆZn ̸= Zn} →0
as n →∞.
For what R is this possible?
HISTORICAL NOTES
The Gaussian channel was ﬁrst analyzed by Shannon in his original
paper [472]. The water-ﬁlling solution to the capacity of the colored
noise Gaussian channel was developed by Shannon [480] and treated in
detail by Pinsker [425]. The time-continuous Gaussian channel is treated
in Wyner [576], Gallager [233], and Landau, Pollak, and Slepian [340,
341, 500].
Pinsker [421] and Ebert [178] argued that feedback at most doubles
the capacity of a nonwhite Gaussian channel; the proof in the text is
from Cover and Pombra [136], who also show that feedback increases
the capacity of the nonwhite Gaussian channel by at most half a bit.
The most recent feedback capacity results for nonwhite Gaussian noise
channels are due to Kim [314].


## PDF page 326



## PDF page 327

CHAPTER 10
RATE DISTORTION THEORY
The description of an arbitrary real number requires an inﬁnite number
of bits, so a ﬁnite representation of a continuous random variable can
never be perfect. How well can we do? To frame the question appropri-
ately, it is necessary to deﬁne the “goodness” of a representation of a
source. This is accomplished by deﬁning a distortion measure which is a
measure of distance between the random variable and its representation.
The basic problem in rate distortion theory can then be stated as follows:
Given a source distribution and a distortion measure, what is the minimum
expected distortion achievable at a particular rate? Or, equivalently, what
is the minimum rate description required to achieve a particular distortion?
One of the most intriguing aspects of this theory is that joint descriptions
are more efﬁcient than individual descriptions. It is simpler to describe an
elephant and a chicken with one description than to describe each alone. This
is true even for independent random variables. It is simpler to describe X1
and X2 together (at a given distortion for each) than to describe each by itself.
Why don’t independent problems have independent solutions? The answer
is found in the geometry. Apparently, rectangular grid points (arising from
independent descriptions) do not ﬁll up the space efﬁciently.
Rate distortion theory can be applied to both discrete and continuous
random variables. The zero-error data compression theory of Chapter 5
is an important special case of rate distortion theory applied to a discrete
source with zero distortion. We begin by considering the simple problem
of representing a single continuous random variable by a ﬁnite number
of bits.
10.1
QUANTIZATION
In this section we motivate the elegant theory of rate distortion by showing
how complicated it is to solve the quantization problem exactly for a single
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
301


## PDF page 328

302
RATE DISTORTION THEORY
random variable. Since a continuous random source requires inﬁnite preci-
sion to represent exactly, we cannot reproduce it exactly using a ﬁnite-rate
code. The question is then to ﬁnd the best possible representation for any
given data rate.
We ﬁrst consider the problem of representing a single sample from the
source. Let the random variable be represented be X and let the represen-
tation of X be denoted as ˆX(X). If we are given R bits to represent X,
the function ˆX can take on 2R values. The problem is to ﬁnd the optimum
set of values for ˆX (called the reproduction points or code points) and
the regions that are associated with each value ˆX.
For example, let X ∼N(0, σ 2), and assume a squared-error distortion
measure. In this case we wish to ﬁnd the function ˆX(X) such that ˆX takes
on at most 2R values and minimizes E(X −ˆX(X))2. If we are given one
bit to represent X, it is clear that the bit should distinguish whether or
not X > 0. To minimize squared error, each reproduced symbol should
be the conditional mean of its region. This is illustrated in Figure 10.1.
Thus,
ˆX(x) =




2
π σ
if x ≥0,
−

2
π σ
if x < 0.
(10.1)
If we are given 2 bits to represent the sample, the situation is not as
simple. Clearly, we want to divide the real line into four regions and use
0
0.05
0.1
0.15
0.2
0.25
0.3
0.35
0.4
−2.5
−2
−1.5
−.79
+.79
−1
−0.5
0
0.5
1
1.5
2
2.5
x
f(x)
FIGURE 10.1. One-bit quantization of Gaussian random variable.


