# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 297

9.3
BANDLIMITED CHANNELS
271
Theorem 9.3.1
Suppose that a function f (t) is bandlimited to W,
namely, the spectrum of the function is 0 for all frequencies greater than
W. Then the function is completely determined by samples of the function
spaced
1
2W seconds apart.
Proof:
Let F(ω) be the Fourier transform of f (t). Then
f (t) = 1
2π
 ∞
−∞
F(ω)eiωt dω
(9.55)
= 1
2π
 2πW
−2πW
F(ω)eiωt dω,
(9.56)
since F(ω) is zero outside the band −2πW ≤ω ≤2πW. If we consider
samples spaced
1
2W seconds apart, the value of the signal at the sample
points can be written
f
 n
2W

= 1
2π
 2πW
−2πW
F(ω)eiω n
2W dω.
(9.57)
The right-hand side of this equation is also the deﬁnition of the coefﬁcients
of the Fourier series expansion of the periodic extension of the function
F(ω), taking the interval −2πW to 2πW as the fundamental period. Thus,
the sample values f ( n
2W ) determine the Fourier coefﬁcients and, by exten-
sion, they determine the value of F(ω) in the interval (−2πW, 2πW).
Since a function is uniquely speciﬁed by its Fourier transform, and since
F(ω) is zero outside the band W, we can determine the function uniquely
from the samples.
Consider the function
sinc(t) = sin(2πWt)
2πWt
.
(9.58)
This function is 1 at t = 0 and is 0 for t = n/2W, n ̸= 0. The spectrum
of this function is constant in the band (−W, W) and is zero outside this
band. Now deﬁne
g(t) =
∞

n=−∞
f
 n
2W

sinc

t −n
2W

.
(9.59)
From the properties of the sinc function, it follows that g(t) is bandlim-
ited to W and is equal to f (n/2W) at t = n/2W. Since there is only


## PDF page 298

272
GAUSSIAN CHANNEL
one function satisfying these constraints, we must have g(t) = f (t). This
provides an explicit representation of f (t) in terms of its samples.
□
A general function has an inﬁnite number of degrees of freedom—the
value of the function at every point can be chosen independently. The
Nyquist–Shannon sampling theorem shows that a bandlimited function
has only 2W degrees of freedom per second. The values of the function
at the sample points can be chosen independently, and this speciﬁes the
entire function.
If a function is bandlimited, it cannot be limited in time. But we can
consider functions that have most of their energy in bandwidth W and
have most of their energy in a ﬁnite time interval, say (0, T ). We can
describe these functions using a basis of prolate spheroidal functions. We
do not go into the details of this theory here; it sufﬁces to say that there
are about 2T W orthonormal basis functions for the set of almost time-
limited, almost bandlimited functions, and we can describe any function
within the set by its coordinates in this basis. The details can be found
in a series of papers by Landau, Pollak, and Slepian [340, 341, 500].
Moreover, the projection of white noise on these basis vectors forms
an i.i.d. Gaussian process. The above arguments enable us to view the
bandlimited, time-limited functions as vectors in a vector space of 2T W
dimensions.
Now we return to the problem of communication over a bandlimited
channel. Assuming that the channel has bandwidth W, we can represent
both the input and the output by samples taken 1/2W seconds apart. Each
of the input samples is corrupted by noise to produce the corresponding
output sample. Since the noise is white and Gaussian, it can be shown
that each noise sample is an independent, identically distributed Gaussian
random variable.
If the noise has power spectral density N0/2 watts/hertz and bandwidth
W hertz, the noise has power N0
2 2W = N0W and each of the 2WT noise
samples in time T has variance N0WT /2WT = N0/2. Looking at the
input as a vector in the 2T W-dimensional space, we see that the received
signal is spherically normally distributed about this point with covariance
N0
2 I.
Now we can use the theory derived earlier for discrete-time Gaussian
channels, where it was shown that the capacity of such a channel is
C = 1
2 log

1 + P
N

bits per transmission.
(9.60)
Let the channel be used over the time interval [0, T ]. In this case, the
energy per sample is P T /2WT = P/2W, the noise variance per sample


## PDF page 299

9.3
BANDLIMITED CHANNELS
273
is N0
2 2W
T
2WT = N0/2, and hence the capacity per sample is
C = 1
2 log

1 +
P
2W
N0
2

= 1
2 log

1 +
P
N0W

bits per sample.
(9.61)
Since there are 2W samples each second, the capacity of the channel can
be rewritten as
C = W log

1 +
P
N0W

bits per second.
(9.62)
This equation is one of the most famous formulas of information theory. It
gives the capacity of a bandlimited Gaussian channel with noise spectral
density N0/2 watts/Hz and power P watts.
A more precise version of the capacity argument [576] involves con-
sideration of signals with a small fraction of their energy outside the
bandwidth W of the channel and a small fraction of their energy outside
the time interval (0, T ). The capacity above is then obtained as a limit as
the fraction of energy outside the band goes to zero.
If we let W →∞in (9.62), we obtain
C = P
N0
log2 e
bits per second
(9.63)
as the capacity of a channel with an inﬁnite bandwidth, power P , and
noise spectral density N0/2. Thus, for inﬁnite bandwidth channels, the
capacity grows linearly with the power.
Example 9.3.1
(Telephone line)
To allow multiplexing of many chan-
nels, telephone signals are bandlimited to 3300 Hz. Using a bandwidth of
3300 Hz and a SNR (signal-to-noise ratio) of 33 dB (i.e., P/N0W =
2000) in (9.62), we ﬁnd the capacity of the telephone channel to be
about 36,000 bits per second. Practical modems achieve transmission rates
up to 33,600 bits per second in both directions over a telephone channel.
In real telephone channels, there are other factors, such as crosstalk, inter-
ference, echoes, and nonﬂat channels which must be compensated for to
achieve this capacity.
The V.90 modems that achieve 56 kb/s over the telephone channel
achieve this rate in only one direction, taking advantage of a purely digital
channel from the server to ﬁnal telephone switch in the network. In this
case, the only impairments are due to the digital-to-analog conversion at
this switch and the noise in the copper link from the switch to the home;


## PDF page 300

274
GAUSSIAN CHANNEL
these impairments reduce the maximum bit rate from the 64 kb/s for the
digital signal in the network to the 56 kb/s in the best of telephone lines.
The actual bandwidth available on the copper wire that links a home to
a telephone switch is on the order of a few megahertz; it depends on the
length of the wire. The frequency response is far from ﬂat over this band.
If the entire bandwidth is used, it is possible to send a few megabits per
second through this channel; schemes such at DSL (Digital Subscriber
Line) achieve this using special equipment at both ends of the telephone
line (unlike modems, which do not require modiﬁcation at the telephone
switch).
9.4
PARALLEL GAUSSIAN CHANNELS
In this section we consider k independent Gaussian channels in parallel
with a common power constraint. The objective is to distribute the total
power among the channels so as to maximize the capacity. This channel
models a nonwhite additive Gaussian noise channel where each parallel
component represents a different frequency.
Assume that we have a set of Gaussian channels in parallel as illustrated
in Figure 9.3. The output of each channel is the sum of the input and
Gaussian noise. For channel j,
Yj = Xj + Zj,
j = 1, 2, . . . , k,
(9.64)
with
Zj ∼N(0, Nj),
(9.65)
and the noise is assumed to be independent from channel to channel. We
assume that there is a common power constraint on the total power used,
that is,
E
k

j=1
X2
j ≤P.
(9.66)
We wish to distribute the power among the various channels so as to
maximize the total capacity.
The information capacity of the channel C is
C =
max
f (x1,x2,...,xk): E X2
i ≤P
I (X1, X2, . . . , Xk ; Y1, Y2, . . . , Yk).
(9.67)


## PDF page 301

9.4
PARALLEL GAUSSIAN CHANNELS
275
Z1
Y1
X1
Zk
Yk
Xk
FIGURE 9.3. Parallel Gaussian channels.
We calculate the distribution that achieves the information capacity for
this channel. The fact that the information capacity is the supremum of
achievable rates can be proved by methods identical to those in the proof
of the capacity theorem for single Gaussian channels and will be omitted.
Since Z1, Z2, . . . , Zk are independent,
I (X1, X2, . . . , Xk ; Y1, Y2, . . . , Yk)
= h(Y1, Y2, . . . , Yk) −h(Y1, Y2, . . . , Yk|X1, X2, . . . , Xk)
= h(Y1, Y2, . . . , Yk) −h(Z1, Z2, . . . , Zk|X1, X2, . . . , Xk)
= h(Y1, Y2, . . . , Yk) −h(Z1, Z2, . . . , Zk)
(9.68)
= h(Y1, Y2, . . . , Yk) −

i
h(Zi)
(9.69)
≤

i
h(Yi) −h(Zi)
(9.70)
≤

i
1
2 log

1 + Pi
Ni

,
(9.71)


## PDF page 302

276
GAUSSIAN CHANNEL
where Pi = EX2
i , and  Pi = P . Equality is achieved by
(X1, X2, . . . , Xk) ∼N

0,


P1
0
· · ·
0
0
P2
· · ·
0
...
...
...
...
0
0
· · ·
Pk



.
(9.72)
So the problem is reduced to ﬁnding the power allotment that max-
imizes the capacity subject to the constraint that  Pi = P . This is a
standard optimization problem and can be solved using Lagrange multi-
pliers. Writing the functional as
J(P1, . . . , Pk) =
 1
2 log

1 + Pi
Ni

+ λ

Pi

(9.73)
and differentiating with respect to Pi, we have
1
2
1
Pi + Ni
+ λ = 0
(9.74)
or
Pi = ν −Ni.
(9.75)
However, since the Pi’s must be nonnegative, it may not always be possi-
ble to ﬁnd a solution of this form. In this case, we use the Kuhn–Tucker
conditions to verify that the solution
Pi = (ν −Ni)+
(9.76)
is the assignment that maximizes capacity, where ν is chosen so that

(ν −Ni)+ = P.
(9.77)
Here (x)+ denotes the positive part of x:
(x)+ =
!
x
if x ≥0,
0
if x < 0.
(9.78)
This solution is illustrated graphically in Figure 9.4. The vertical levels
indicate the noise levels in the various channels. As the signal power is
increased from zero, we allot the power to the channels with the lowest


## PDF page 303

9.5
CHANNELS WITH COLORED GAUSSIAN NOISE
277
Power
Channel 1
Channel 2
Channel 3
P1
n
P2
N1
N2
N3
FIGURE 9.4. Water-ﬁlling for parallel channels.
noise. When the available power is increased still further, some of the
power is put into noisier channels. The process by which the power is
distributed among the various bins is identical to the way in which water
distributes itself in a vessel, hence this process is sometimes referred to
as water-ﬁlling.
9.5
CHANNELS WITH COLORED GAUSSIAN NOISE
In Section 9.4, we considered the case of a set of parallel independent
Gaussian channels in which the noise samples from different channels
were independent. Now we will consider the case when the noise is depen-
dent. This represents not only the case of parallel channels, but also the
case when the channel has Gaussian noise with memory. For channels
with memory, we can consider a block of n consecutive uses of the chan-
nel as n channels in parallel with dependent noise. As in Section 9.4, we
will calculate only the information capacity for this channel.
Let KZ be the covariance matrix of the noise, and let KX be the input
covariance matrix. The power constraint on the input can then be writ-
ten as
1
n

i
EX2
i ≤P,
(9.79)
or equivalently,
1
ntr(KX) ≤P.
(9.80)


## PDF page 304

278
GAUSSIAN CHANNEL
Unlike Section 9.4, the power constraint here depends on n; the capacity
will have to be calculated for each n.
Just as in the case of independent channels, we can write
I (X1, X2, . . . , Xn; Y1, Y2, . . . , Yn) = h(Y1, Y2, . . . , Yn)
−h(Z1, Z2, . . . , Zn). (9.81)
Here h(Z1, Z2, . . . , Zn) is determined only by the distribution of the noise
and is not dependent on the choice of input distribution. So ﬁnding the
capacity amounts to maximizing h(Y1, Y2, . . . , Yn). The entropy of the
output is maximized when Y is normal, which is achieved when the input
is normal. Since the input and the noise are independent, the covariance
of the output Y is KY = KX + KZ and the entropy is
h(Y1, Y2, . . . , Yn) = 1
2 log

(2πe)n|KX + KZ|

.
(9.82)
Now the problem is reduced to choosing KX so as to maximize |KX +
KZ|, subject to a trace constraint on KX. To do this, we decompose KZ
into its diagonal form,
KZ = QQt,
where QQt = I.
(9.83)
Then
|KX + KZ| = |KX + QQt|
(9.84)
= |Q||QtKXQ + ||Qt|
(9.85)
= |QtKXQ + |
(9.86)
= |A + |,
(9.87)
where A = QtKXQ. Since for any matrices B and C,
tr(BC) = tr(CB),
(9.88)
we have
tr(A) = tr(QtKXQ)
(9.89)
= tr(QQtKX)
(9.90)
= tr(KX).
(9.91)


