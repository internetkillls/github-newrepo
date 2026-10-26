# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 313

9.6
GAUSSIAN CHANNELS WITH FEEDBACK
287
(b)
≥
n

i=1
h(Xi −Zi|Xi−1, Zi−1, Xi)
(9.145)
(c)
=
n

i=1
h(Zi|Xi−1, Zi−1, Xi)
(9.146)
(d)
=
n

i=1
h(Zi|Zi−1)
(9.147)
(e)
= h(Zn).
(9.148)
Here (a) follows from the chain rule, (b) follows from conditioning
h(A|B) ≥h(A|B, C), (c) follows from the conditional determinism of
Xi and the invariance of differential entropy under translation, (d) fol-
lows from the causal relationship of Xn and Zn, and (e) follows from the
chain rule.
Finally, suppose that Xn and Zn are causally related and the associ-
ated covariance matrices for Zn and Xn −Zn are KZ and KX−Z. There
obviously exists a multivariate normal (causally related) pair of random
vectors ˜Xn, ˜Zn with the same covariance structure. Thus, from (9.148),
we have
1
2 ln(2πe)n|KX−Z| = h( ˜Xn −˜Zn)
(9.149)
≥h( ˜Zn)
(9.150)
= 1
2 ln(2πe)n|KZ|,
(9.151)
thus proving (9.143).
□
We are now in a position to prove that feedback increases the capacity
of a nonwhite Gaussian additive noise channel by at most half a bit.
Theorem 9.6.2
Cn,FB ≤Cn + 1
2
bits per transmission.
(9.152)
Proof:
Combining all the lemmas, we obtain
Cn,FB ≤
max
tr(KX)≤nP
1
2n log |KY|
|KZ|
(9.153)


## PDF page 314

288
GAUSSIAN CHANNEL
≤
max
tr(KX)≤nP
1
2n log 2n|KX + KZ|
|KZ|
(9.154)
=
max
tr(KX)≤nP
1
2n log |KX + KZ|
|KZ|
+ 1
2
(9.155)
≤Cn + 1
2
bits per transmission,
(9.156)
where the inequalities follow from Theorem 9.6.1, Lemma 9.6.3, and the
deﬁnition of capacity without feedback, respectively.
□
We now prove Pinsker’s statement that feedback can at most double
the capacity of colored noise channels.
Theorem 9.6.3
Cn,FB ≤2Cn.
Proof:
It is enough to show that
1
2
1
2n log |KX+Z|
|KZ|
≤1
2n log |KX + KZ|
|KZ|
,
(9.157)
for it will then follow that by maximizing the right side and then the left
side that
1
2Cn,FB ≤Cn.
(9.158)
We have
1
2n log |KX + KZ|
|KZ|
(a)
= 1
2n log |1
2KX+Z + 1
2KX−Z|
|KZ|
(9.159)
(b)
≥1
2n log |KX+Z|
1
2|KX−Z|
1
2
|KZ|
(9.160)
(c)
≥1
2n log |KX+Z|
1
2 |KZ|
1
2
|KZ|
(9.161)
(d)
= 1
2
1
2n log |KX+Z|
|KZ|
(9.162)
and the result is proved. Here (a) follows from Lemma 9.6.1, (b) is the
inequality in Lemma 9.6.4, and (c) is Lemma 9.6.5 in which causality is
used.
□


## PDF page 315

SUMMARY
289
Thus, we have shown that Gaussian channel capacity is not increased
by more than half a bit or by more than a factor of 2 when we have
feedback; feedback helps, but not by much.
SUMMARY
Maximum entropy. maxEX2=α h(X) = 1
2 log 2πeα.
Gaussian channel.
Yi = Xi + Zi; Zi ∼N(0, N); power constraint
1
n
n
i=1 x2
i ≤P ; and
C = 1
2 log

1 + P
N

bits per transmission.
(9.163)
Bandlimited additive white Gaussian noise channel. Bandwidth W;
two-sided power spectral density N0/2; signal power P ; and
C = W log

1 +
P
N0W

bits per second.
(9.164)
Water-ﬁlling (k parallel Gaussian channels). Yj = Xj + Zj, j = 1,
2, . . . , k; Zj ∼N(0, Nj); k
j=1 X2
j ≤P ; and
C =
k

i=1
1
2 log

1 + (ν −Ni)+
Ni

,
(9.165)
where ν is chosen so that (ν −Ni)+ = nP .
Additive nonwhite Gaussian noise channel. Yi = Xi + Zi; Zn ∼
N(0, KZ); and
C = 1
n
n

i=1
1
2 log

1 + (ν −λi)+
λi

,
(9.166)
where λ1, λ2, . . . , λn are the eigenvalues of KZ and ν is chosen so that

i(ν −λi)+ = P .
Capacity without feedback
Cn =
max
tr(KX)≤nP
1
2n log |KX + KZ|
|KZ|
.
(9.167)


## PDF page 316

290
GAUSSIAN CHANNEL
Capacity with feedback
Cn,FB =
max
tr(KX)≤nP
1
2n log |KX+Z|
|KZ| .
(9.168)
Feedback bounds
Cn,FB ≤Cn + 1
2.
(9.169)
Cn,FB ≤2Cn.
(9.170)
PROBLEMS
9.1
Channel with two independent looks at Y .
Let Y1 and Y2 be condi-
tionally independent
and conditionally
identically distributed
given X.
(a) Show that I (X; Y1, Y2) = 2I (X; Y1) −I (Y1; Y2).
(b) Conclude that the capacity of the channel
X
(Y1, Y2)
is less than twice the capacity of the channel
X
Y1
9.2
Two-look Gaussian channel
X
(Y1, Y2)
Consider the ordinary Gaussian channel with two correlated looks
at X, that is, Y = (Y1, Y2), where
Y1 = X + Z1
(9.171)
Y2 = X + Z2
(9.172)


## PDF page 317

PROBLEMS
291
with a power constraint P on X, and (Z1, Z2) ∼N2(0, K), where
K =
'
N
Nρ
Nρ
N
(
.
(9.173)
Find the capacity C for
(a) ρ = 1
(b) ρ = 0
(c) ρ = −1
9.3
Output power constraint.
Consider an additive white Gaussian
noise channel with an expected output power constraint P . Thus,
Y = X + Z, Z ∼N(0, σ 2), Z is independent of X, and EY 2 ≤P .
Find the channel capacity.
9.4
Exponential noise channels.
Yi = Xi + Zi, where Zi is i.i.d. ex-
ponentially distributed noise with mean µ. Assume that we have
a mean constraint on the signal (i.e., EXi ≤λ). Show that the
capacity of such a channel is C = log(1 + λ
µ).
9.5
Fading channel.
Consider an additive noise fading channel
V
X
Z
Y
Y = XV + Z,
where Z is additive noise, V is a random variable representing
fading, and Z and V are independent of each other and of X.
Argue that knowledge of the fading factor V improves capacity by
showing that
I (X; Y|V ) ≥I (X; Y).
9.6
Parallel channels and water-ﬁlling.
Consider a pair of parallel
Gaussian channels:

Y1
Y2

=

X1
X2

+

Z1
Z2

,
(9.174)


## PDF page 318

292
GAUSSIAN CHANNEL
where

Z1
Z2

∼N

0,
'
σ 2
1
0
0
σ 2
2
(
,
(9.175)
and there is a power constraint E(X2
1 + X2
2) ≤2P . Assume that
σ 2
1 > σ 2
2 . At what power does the channel stop behaving like a
single channel with noise variance σ 2
2 , and begin behaving like a
pair of channels?
9.7
Multipath Gaussian channel.
Consider a Gaussian noise channel
with power constraint P , where the signal takes two different paths
and the received noisy signals are added together at the antenna.
∑
X
Y
Z1
Y1
Y2
Z2
(a) Find the capacity of this channel if Z1 and Z2 are jointly normal
with covariance matrix
KZ =
'
σ 2
ρσ 2
ρσ 2
σ 2
(
.
(b) What is the capacity for ρ = 0, ρ = 1, ρ = −1?
9.8
Parallel Gaussian channels.
Consider the following parallel
Gaussian channel:
Z1 ~
(0,N1)
X1
Y1
Z2 ~
(0,N2)
X2
Y2


## PDF page 319

PROBLEMS
293
where Z1 ∼N(0,N1) and Z2 ∼N(0,N2) are independent Gaussian
random variables and Yi = Xi + Zi. We wish to allocate power
to the two parallel channels. Let β1 and β2 be ﬁxed. Consider
a total cost constraint β1P1 + β2P2 ≤β, where Pi is the power
allocated to the ith channel and βi is the cost per unit power in
that channel. Thus, P1 ≥0 and P2 ≥0 can be chosen subject to
the cost constraint β.
(a) For what value of β does the channel stop acting like a single
channel and start acting like a pair of channels?
(b) Evaluate the capacity and ﬁnd P1 and P2 that achieve capacity
for β1 = 1, β2 = 2, N1 = 3, N2 = 2, and β = 10.
9.9
Vector Gaussian channel.
Consider the vector Gaussian noise
channel
Y = X + Z,
where
X = (X1, X2, X3),
Z = (Z1, Z2, Z3), Y = (Y1, Y2, Y3),
E∥X∥2 ≤P, and
Z ∼N

0,


1
0
1
0
1
1
1
1
2



.
Find the capacity. The answer may be surprising.
9.10
Capacity of photographic ﬁlm.
Here is a problem with a nice
answer that takes a little time. We’re interested in the capacity
of photographic ﬁlm. The ﬁlm consists of silver iodide crystals,
Poisson distributed, with a density of λ particles per square inch.
The ﬁlm is illuminated without knowledge of the position of the
silver iodide particles. It is then developed and the receiver sees
only the silver iodide particles that have been illuminated. It is
assumed that light incident on a cell exposes the grain if it is there
and otherwise results in a blank response. Silver iodide particles
that are not illuminated and vacant portions of the ﬁlm remain
blank. The question is: What is the capacity of this ﬁlm?
We make the following assumptions. We grid the ﬁlm very ﬁnely
into cells of area dA. It is assumed that there is at most one sil-
ver iodide particle per cell and that no silver iodide particle is
intersected by the cell boundaries. Thus, the ﬁlm can be consid-
ered to be a large number of parallel binary asymmetric channels
with crossover probability 1 −λdA. By calculating the capacity of
this binary asymmetric channel to ﬁrst order in dA (making the


## PDF page 320

294
GAUSSIAN CHANNEL
necessary approximations), one can calculate the capacity of the
ﬁlm in bits per square inch. It is, of course, proportional to λ. The
question is: What is the multiplicative constant?
The answer would be λ bits per unit area if both illuminator and
receiver knew the positions of the crystals.
9.11
Gaussian mutual information.
Suppose that (X, Y, Z) are jointly
Gaussian and that X →Y →Z forms a Markov chain. Let X and
Y have correlation coefﬁcient ρ1 and let Y and Z have correlation
coefﬁcient ρ2. Find I (X; Z).
9.12
Time-varying channel.
A train pulls out of the station at constant
velocity. The received signal energy thus falls off with time as
1/i2. The total received signal at time i is
Yi = 1
i Xi + Zi,
where Z1, Z2, . . . are i.i.d. ∼N(0, N). The transmitter constraint
for block length n is
1
n
n

i=1
x2
i (w) ≤P,
w ∈{1, 2, . . . , 2nR}.
Using Fano’s inequality, show that the capacity C is equal to zero
for this channel.
9.13
Feedback
capacity.
Let
(Z1, Z2) ∼N(0, K), K =
'
1
ρ
ρ
1
(
.
Find the maximum of 1
2 log |KX+Z|
|KZ|
with and without feedback given
a trace (power) constraint tr(KX) ≤2P.
9.14
Additive noise channel.
Consider the channel Y = X + Z, where
X is the transmitted signal with power constraint P , Z is indepen-
dent additive noise, and Y is the received signal. Let
Z =
)
0
with probability
1
10
Z∗
with probability
9
10,
where Z∗∼N(0, N). Thus, Z has a mixture distribution that is
the mixture of a Gaussian distribution and a degenerate distribution
with mass 1 at 0.


