# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 625

PROBLEMS
599
15.9
Slepian–Wolf .
Let Xi be i.i.d. Bernoulli(p). Let Zi be i.i.d. ∼
Bernoulli(r), and let Z be independent of X. Finally, let Y =
X ⊕Z (mod 2 addition). Let X be described at rate R1 and Y
be described at rate R2. What region of rates allows recovery of
X, Y with probability of error tending to zero?
15.10
Broadcast capacity depends only on the conditional marginals.
Consider the general broadcast channel (X, Y1 × Y2, p(y1, y2 | x)).
Show that the capacity region depends only on p(y1 | x) and p(y2 |
x). To do this, for any given ((2nR1, 2nR2), n) code, let
P (n)
1
= P { ˆW1(Y1) ̸= W1},
(15.373)
P (n)
2
= P { ˆW2(Y2) ̸= W2},
(15.374)
P (n) = P {( ˆW1, ˆW2) ̸= (W1, W2)}.
(15.375)
Then show that
max{P (n)
1 , P (n)
2 } ≤P (n) ≤P (n)
1
+ P (n)
2 .
The result now follows by a simple argument. (Remark: The
probability of error P (n) does depend on the conditional joint
distribution p(y1, y2 | x). But whether or not P (n) can be driven
to zero [at rates (R1, R2)] does not [except through the conditional
marginals p(y1 | x), p(y2 | x)] .)
15.11
Converse for the degraded broadcast channel.
The following
chain of inequalities proves the converse for the degraded dis-
crete memoryless broadcast channel. Provide reasons for each of
the labeled inequalities.
Setup for converse for degraded broadcast channel capacity:
(W1, W2)indep. →Xn(W1, W2) →Y n
1 →Y n
2 .
• Encoding fn : 2nR1 × 2nR2 →Xn
• Decoding:
gn : Yn
1 →2nR1, hn : Yn
2 →2nR2.
Let
Ui =
(W2, Y i−1
1
). Then
nR2
·≤Fano I (W2; Y n
2 )
(15.376)
(a)
=
n

i=1
I (W2; Y2i | Y i−1
2
)
(15.377)


## PDF page 626

600
NETWORK INFORMATION THEORY
(b)
=

i
(H(Y2i | Y i−1
2
) −H(Y2i | W2, Y i−1
2
))
(15.378)
(c)
≤

i
(H(Y2i) −H(Y2i | W2, Y i−1
2
, Y i−1
1
))
(15.379)
(d)
=

i
(H(Y2i) −H(Y2i | W2, Y i−1
1
))
(15.380)
(e)
=
n

i=1
I (Ui; Y2i).
(15.381)
Continuation of converse: Give reasons for the labeled inequali-
ties:
nR1
·≤Fano I (W1; Y n
1 )
(15.382)
(f)
≤I (W1; Y n
1 , W2)
(15.383)
(g)
≤I (W1; Y n
1 | W2)
(15.384)
(h)
=
n

i−1
I (W1; Y1i | Y i−1
1
, W2)
(15.385)
(i)≤
n

i=1
I (Xi; Y1i | Ui).
(15.386)
Now let Q be a time-sharing random variable with Pr(Q = i) =
1/n, i = 1, 2, . . . , n. Justify the following:
R1 ≤I (XQ; Y1Q|UQ, Q),
(15.387)
R2 ≤I (UQ; Y2Q|Q)
(15.388)
for some distribution p(q)p(u|q)p(x|u, q)p(y1, y2|x). By appro-
priately redeﬁning U, argue that this region is equal to the convex
closure of regions of the form
R1 ≤I (X; Y1|U),
(15.389)
R2 ≤I (U; Y2)
(15.390)
for some joint distribution p(u)p(x|u)p(y1, y2|x).


## PDF page 627

PROBLEMS
601
15.12
Capacity points.
(a) For the degraded broadcast channel X →Y1 →Y2, ﬁnd the
points a and b where the capacity region hits the R1 and R2
axes.
R2
R1
b
a
(b) Show that b ≤a.
15.13
Degraded broadcast channel.
Find the capacity region for the
degraded broadcast channel shown below.
X
p
1 − p
1 − p
1 −a
1 −a
a
a
p
Y2
Y1
15.14
Channels with unknown parameters.
We are given a binary
symmetric channel with parameter p. The capacity is C = 1 −
H(p). Now we change the problem slightly. The receiver knows
only that p ∈{p1, p2} (i.e., p = p1 or p = p2, where p1 and p2
are given real numbers). The transmitter knows the actual value
of p. Devise two codes for use by the transmitter, one to be used
if p = p1, the other to be used if p = p2, such that transmission
to the receiver can take place at rate ≈C(p1) if p = p1 and at
rate ≈C(p2) if p = p2. (Hint: Devise a method for revealing
p to the receiver without affecting the asymptotic rate. Preﬁxing
the codeword by a sequence of 1’s of appropriate length should
work.)


## PDF page 628

602
NETWORK INFORMATION THEORY
15.15
Two-way channel.
Consider the two-way channel shown in
Figure 15.6. The outputs Y1 and Y2 depend only on the current
inputs X1 and X2.
(a) By using independently generated codes for the two senders,
show that the following rate region is achievable:
R1 < I (X1; Y2|X2),
(15.391)
R2 < I (X2; Y1|X1)
(15.392)
for some product distribution p(x1)p(x2)p(y1, y2|x1, x2).
(b) Show that the rates for any code for a two-way channel with
arbitrarily small probability of error must satisfy
R1 ≤I (X1; Y2|X2),
(15.393)
R2 ≤I (X2; Y1|X1)
(15.394)
for some joint distribution p(x1, x2)p(y1, y2|x1, x2).
The inner and outer bounds on the capacity of the two-way
channel are due to Shannon [486]. He also showed that the inner
bound and the outer bound do not coincide in the case of the
binary multiplying channel X1 = X2 = Y1 = Y2 = {0, 1}, Y1 =
Y2 = X1X2. The capacity of the two-way channel is still an open
problem.
15.16
Multiple-access channel.
Let the output Y of a multiple-access
channel be given by
Y = X1 + sgn(X2),
where X1, X2 are both real and power limited,
E(X2
1)
≤P1,
E(X2
2)
≤P2,
and sgn(x) =

1,
x > 0,
−1,
x ≤0.
Note that there is interference but no noise in this channel.
(a) Find the capacity region.
(b) Describe a coding scheme that achieves the capacity region.


## PDF page 629

PROBLEMS
603
15.17
Slepian–Wolf .
Let (X, Y) have the joint probability mass func-
tion p(x, y):
p(x, y)
1
2
3
1
α
β
β
2
β
α
β
3
β
β
α
where β = 1
6 −α
2. (Note: This is a joint, not a conditional, prob-
ability mass function.)
(a) Find the Slepian–Wolf rate region for this source.
(b) What is Pr{X = Y} in terms of α?
(c) What is the rate region if α = 1
3?
(d) What is the rate region if α = 1
9?
15.18
Square channel.
What is the capacity of the following multiple-
access channel?
X1 ∈{−1, 0, 1},
X2 ∈{−1, 0, 1},
Y = X2
1 + X2
2.
(a) Find the capacity region.
(b) Describe p∗(x1), p∗(x2) achieving a point on the boundary of
the capacity region.
15.19
Slepian–Wolf .
Two senders know random variables U1 and U2,
respectively. Let the random variables (U1, U2) have the following
joint distribution:
U1\U2
0
1
2
· · ·
m −1
0
α
β
m−1
β
m−1
· · ·
β
m−1
1
γ
m−1
0
0
· · ·
0
2
γ
m−1
0
0
· · ·
0
...
...
...
...
...
...
m −1
γ
m−1
0
0
· · ·
0
where α + β + γ = 1. Find the region of rates (R1, R2) that would
allow a common receiver to decode both random variables reliably.


## PDF page 630

604
NETWORK INFORMATION THEORY
15.20
Multiple access
(a) Find the capacity region for the multiple-access channel
Y = XX2
1 ,
where
X1ϵ{2, 4} , X2ϵ{1, 2}.
(b) Suppose that the range of X1 is {1, 2}. Is the capacity region
decreased? Why or why not?
15.21
Broadcast channel.
Consider the following degraded broadcast
channel.
1 −a1
1 −a1
a1
a1
0
1
0
1
1
E
X
Y1
1 −a2
1 −a2
a2
a2
0
1
E
Y2
(a) What is the capacity of the channel from X to Y1?
(b) What is the channel capacity from X to Y2?
(c) What is the capacity region of all (R1, R2) achievable for this
broadcast channel? Simplify and sketch.
15.22
Stereo.
The sum and the difference of the right and left ear sig-
nals are to be individually compressed for a common receiver. Let
Z1 be Bernoulli (p1) and Z2 be Bernoulli (p2) and suppose that
Z1 and Z2 are independent. Let X = Z1 + Z2, and Y = Z1 −Z2.
(a) What is the Slepian–Wolf rate region of achievable (RX, RY)?
RX
Decoder
(X, Y)
X
RY
Y
^
^


## PDF page 631

PROBLEMS
605
(b) Is this larger or smaller than the rate region of (RZ1, RZ2)?
Why?
RZ1
Decoder
(Z1, Z2)
Z1
RZ2
Z2
^
^
There is a simple way to do this part.
15.23
Multiplicative multiple-access channel.
Find and sketch the ca-
pacity region of the following multiplicative multiple-access chan-
nel:
X1
X2
Y
with X1 ∈{0, 1}, X2 ∈{1, 2, 3}, and Y = X1X2.
15.24
Distributed data compression.
Let Z1, Z2, Z3 be independent
Bernoulli(p). Find the Slepian–Wolf rate region for the description
of (X1, X2, X3), where
X1 = Z1
X2 = Z1 + Z2
X3 = Z1 + Z2 + Z3.
X1
(X1, X2, X3)
X2
X3
^
^
^


## PDF page 632

606
NETWORK INFORMATION THEORY
15.25
Noiseless multiple-access channel.
Consider
the
following
multiple-access channel with two binary inputs X1, X2 ∈{0, 1}
and output Y = (X1, X2).
(a) Find the capacity region. Note that each sender can send at
capacity.
(b) Now consider the cooperative capacity region, R1 ≥0, R2 ≥
0, R1 + R2 ≤maxp(x1,x2) I (X1, X2; Y).
Argue
that
the
throughput R1 + R2 does not increase but the capacity region
increases.
15.26
Inﬁnite bandwidth multiple-access channel.
Find the capacity
region for the Gaussian multiple-access channel with inﬁnite band-
width. Argue that all senders can send at their individual capacities
(i.e., inﬁnite bandwidth eliminates interference).
15.27
Multiple-access identity.
Let C(x) = 1
2 log(1 + x) denote the
channel capacity of a Gaussian channel with signal-to-noise ratio
x. Show that
C
P1
N

+ C

P2
P1 + N

= C
P1 + P2
N

.
This suggests that two independent users can send information as
well as if they had pooled their power.
15.28
Frequency-division
multiple
access (FDMA).
Maximize
the
throughput
R1+R2 = W1 log(1 +
P1
NW1) + (W −W1) log(1 +
P2
N(W−W1)) over W1 to show that bandwidth should be proportional
to transmitted power for FDMA.
15.29
Trilingual-speaker broadcast channel.
A speaker of Dutch,
Spanish, and French wishes to communicate simultaneously to
three people: D, S, and F. D knows only Dutch but can distin-
guish when a Spanish word is being spoken as distinguished from
a French word; similarly for the other two, who know only Span-
ish and French, respectively, but can distinguish when a foreign
word is spoken and which language is being spoken. Suppose
that each language, Dutch, Spanish, and French, has M words: M
words of Dutch, M words of French, and M words of Spanish.
(a) What is the maximum rate at which the trilingual speaker can
speak to D?
(b) If he speaks to D at the maximum rate, what is the maximum
rate at which he can speak simultaneously to S?


