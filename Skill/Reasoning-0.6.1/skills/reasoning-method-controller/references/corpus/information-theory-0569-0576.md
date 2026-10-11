# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 569

15.3
MULTIPLE-ACCESS CHANNEL
543
cannot be any larger than the region in (15.96), and this is the capacity
region of the multiple-access channel.
15.3.5
m-User Multiple-Access Channels
We will now generalize the result derived for two senders to m senders,
m ≥2. The multiple-access channel in this case is shown in Figure 15.15.
We send independent indices w1, w2, . . . , wm over the channel from
the senders 1, 2, . . . , m, respectively. The codes, rates, and achievability
are all deﬁned in exactly the same way as in the two-sender case.
Let S ⊆{1, 2, . . . , m}. Let Sc denote the complement of S. Let
R(S) = 
i∈S Ri, and let X(S) = {Xi : i ∈S}. Then we have the follow-
ing theorem.
Theorem 15.3.6
The capacity region of the m-user multiple-access
channel is the closure of the convex hull of the rate vectors satisfying
R(S) ≤I (X(S); Y|X(Sc))
for all S ⊆{1, 2, . . . , m}
(15.132)
for some product distribution p1(x1)p2(x2) · · · pm(xm).
Proof:
The proof contains no new ideas. There are now 2m −1 terms in
the probability of error in the achievability proof and an equal number of
inequalities in the proof of the converse. Details are left to the reader. □
In general, the region in (15.132) is a beveled box.
p(y|x1,x2,...,xm)
X1
X2
Xm
...
Y
FIGURE 15.15. m-user multiple-access channel.


## PDF page 570

544
NETWORK INFORMATION THEORY
15.3.6
Gaussian Multiple-Access Channels
We now discuss the Gaussian multiple-access channel of Section 15.1.2
in somewhat more detail.
Two senders, X1 and X2, communicate to the single receiver, Y. The
received signal at time i is
Yi = X1i + X2i + Zi,
(15.133)
where {Zi} is a sequence of independent, identically distributed, zero-
mean Gaussian random variables with variance N (Figure 15.16). We
assume that there is a power constraint Pj on sender j; that is, for each
sender, for all messages, we must have
1
n
n

i=1
x2
ji(wj) ≤Pj,
wj ∈{1, 2, . . . , 2nRj },
j = 1, 2. (15.134)
Just as the proof of achievability of channel capacity for the discrete
case (Chapter 7) was extended to the Gaussian channel (Chapter 9), we
can extend the proof for the discrete multiple-access channel to the Gaus-
sian multiple-access channel. The converse can also be extended similarly,
so we expect the capacity region to be the convex hull of the set of rate
pairs satisfying
R1 ≤I (X1; Y|X2),
(15.135)
R2 ≤I (X2; Y|X1),
(15.136)
R1 + R2 ≤I (X1, X2; Y)
(15.137)
for some input distribution f1(x1)f2(x2) satisfying EX2
1 ≤P1 and
EX2
2 ≤P2.
Zn
Xn
1
W1
W2
P1
Xn
2
P2
Yn
(W1, W2)
^
^
FIGURE 15.16. Gaussian multiple-access channel.


## PDF page 571

15.3
MULTIPLE-ACCESS CHANNEL
545
Now, we can expand the mutual information in terms of relative
entropy, and thus
I (X1; Y|X2) = h(Y|X2) −h(Y|X1, X2)
(15.138)
= h(X1 + X2 + Z|X2) −h(X1 + X2 + Z|X1, X2)
(15.139)
= h(X1 + Z|X2) −h(Z|X1, X2)
(15.140)
= h(X1 + Z|X2) −h(Z)
(15.141)
= h(X1 + Z) −h(Z)
(15.142)
= h(X1 + Z) −1
2 log(2πe)N
(15.143)
≤1
2 log(2πe)(P1 + N) −1
2 log(2πe)N
(15.144)
= 1
2 log

1 + P1
N

,
(15.145)
where (15.141) follows from the fact that Z is independent of X1 and
X2, (15.142) from the independence of X1 and X2, and (15.144) from
the fact that the normal maximizes entropy for a given second moment.
Thus, the maximizing distribution is X1 ∼N(0, P1) and X2 ∼N(0, P2)
with X1 and X2 independent. This distribution simultaneously maximizes
the mutual information bounds in (15.135)–(15.137).
Deﬁnition
We deﬁne the channel capacity function
C(x)
△= 1
2 log(1 + x),
(15.146)
corresponding to the channel capacity of a Gaussian white-noise channel
with signal-to-noise ratio x (Figure 15.17). Then we write the bound on
R1 as
R1 ≤C
P1
N

.
(15.147)
Similarly,
R2 ≤C
P2
N

(15.148)


## PDF page 572

546
NETWORK INFORMATION THEORY
R2
R1
D
P2
N
C
C
B
A
0
P1
N
C
P2
P1+ N
C
P1
P2 + N
C
FIGURE 15.17. Gaussian multiple-access channel capacity.
and
R1 + R2 ≤C
P1 + P2
N

.
(15.149)
These upper bounds are achieved when X1 ∼N(0, P1) and X2 =
N(0, P2) and deﬁne the capacity region. The surprising fact about these
inequalities is that the sum of the rates can be as large as C

P1+P2
N

,
which is that rate achieved by a single transmitter sending with a power
equal to the sum of the powers.
The interpretation of the corner points is very similar to the interpre-
tation of the achievable rate pairs for a discrete multiple-access channel
for a ﬁxed input distribution. In the case of the Gaussian channel, we can
consider decoding as a two-stage process: In the ﬁrst stage, the receiver
decodes the second sender, considering the ﬁrst sender as part of the noise.
This decoding will have low probability of error if R2 < C(
P2
P1+N ). After
the second sender has been decoded successfully, it can be subtracted out
and the ﬁrst sender can be decoded correctly if R1 < C(P1
N ). Hence, this
argument shows that we can achieve the rate pairs at the corner points
of the capacity region by means of single-user operations. This process,
called onion-peeling, can be extended to any number of users.
If we generalize this to m senders with equal power, the total rate
is C
mP
N

, which goes to ∞as m →∞. The average rate per sender,
1
mC( mP
N ), goes to 0. Thus, when the total number of senders is very large,


## PDF page 573

15.3
MULTIPLE-ACCESS CHANNEL
547
so that there is a lot of interference, we can still send a total amount of
information that is arbitrarily large even though the rate per individual
sender goes to 0.
The capacity region described above corresponds to code-division mul-
tiple access (CDMA), where separate codes are used for the different
senders and the receiver decodes them one by one. In many practical situ-
ations, though, simpler schemes, such as frequency-division multiplexing
or time-division multiplexing, are used. With frequency-division multiplex-
ing, the rates depend on the bandwidth allotted to each sender. Consider
the case of two senders with powers P1 and P2 using nonintersecting
frequency bands with bandwidths W1 and W2, where W1 + W2 = W (the
total bandwidth). Using the formula for the capacity of a single-user ban-
dlimited channel, the following rate pair is achievable:
R1 = W1 log

1 +
P1
NW1

,
(15.150)
R2 = W2 log

1 +
P2
NW2

.
(15.151)
As we vary W1 and W2, we trace out the curve as shown in Figure 15.18.
This curve touches the boundary of the capacity region at one point,
which corresponds to allotting bandwidth to each channel proportional to
the power in that channel. We conclude that no allocation of frequency
bands to radio stations can be optimal unless the allocated powers are
proportional to the bandwidths.
In time-division multiple access (TDMA), time is divided into slots,
and each user is allotted a slot during which only that user will transmit
and every other user remains quiet. If there are two users, each of power
P , the rate that each sends when the other is silent is C(P/N). Now if
time is divided into equal-length slots, and every odd slot is allocated
to user 1 and every even slot to user 2, the average rate that each user
achieves is 1
2C(P/N). This system is called naive time-division multiple
access (TDMA). However, it is possible to do better if we notice that since
user 1 is sending only half the time, it is possible for him to use twice
the power during his transmissions and still maintain the same average
power constraint. With this modiﬁcation, it is possible for each user to
send information at a rate
1
2C(2P/N). By varying the lengths of the
slots allotted to each sender (and the instantaneous power used during the
slot), we can achieve the same capacity region as FDMA with different
bandwidth allocations.
As Figure 15.18 illustrates, in general the capacity region is larger than
that achieved by time- or frequency-division multiplexing. But note that


## PDF page 574

548
NETWORK INFORMATION THEORY
R2
R1
P2
N
C
0
P1
N
C
P2
P1+ N
C
P1
P2+ N
C
FIGURE 15.18. Gaussian multiple-access channel capacity with FDMA and TDMA.
the multiple-access capacity region derived above is achieved by use of
a common decoder for all the senders. However, it is also possible to
achieve the capacity region by onion-peeling, which removes the need
for a common decoder and instead, uses a sequence of single-user codes.
CDMA achieves the entire capacity region, and in addition, allows new
users to be added easily without changing the codes of the current users.
On the other hand, TDMA and FDMA systems are usually designed for
a ﬁxed number of users and it is possible that either some slots are empty
(if the actual number of users is less than the number of slots) or some
users are left out (if the number of users is greater than the number
of slots). However, in many practical systems, simplicity of design is
an important consideration, and the improvement in capacity due to the
multiple-access ideas presented earlier may not be sufﬁcient to warrant
the increased complexity.
For a Gaussian multiple-access system with m sources with powers
P1, P2, . . . , Pm and ambient noise of power N, we can state the equivalent
of Gauss’s law for any set S in the form

i∈S
Ri = total rate of information ﬂow from S
(15.152)
≤C

i∈S Pi
N

.
(15.153)


## PDF page 575

15.4
ENCODING OF CORRELATED SOURCES
549
15.4
ENCODING OF CORRELATED SOURCES
We now turn to distributed data compression. This problem is in many
ways the data compression dual to the multiple-access channel problem.
We know how to encode a source X. A rate R > H(X) is sufﬁcient. Now
suppose that there are two sources (X, Y) ∼p(x, y). A rate H(X, Y)
is sufﬁcient if we are encoding them together. But what if the X and
Y sources must be described separately for some user who wishes to
reconstruct both X and Y? Clearly, by separately encoding X and Y, it is
seen that a rate R = Rx + Ry > H(X) + H(Y) is sufﬁcient. However, in
a surprising and fundamental paper by Slepian and Wolf [502], it is shown
that a total rate R = H(X, Y) is sufﬁcient even for separate encoding of
correlated sources.
Let (X1, Y1), (X2, Y2), . . . be a sequence of jointly distributed random
variables i.i.d. ∼p(x, y). Assume that the X sequence is available at a
location A and the Y sequence is available at a location B. The situation
is illustrated in Figure 15.19.
Before we proceed to the proof of this result, we will give a few
deﬁnitions.
Deﬁnition
A ((2nR1, 2nR2), n) distributed source code for the joint
source (X, Y) consists of two encoder maps,
f1 : Xn →{1, 2, . . . , 2nR1},
(15.154)
f2 : Yn →{1, 2, . . . , 2nR2},
(15.155)
X
(X, Y )
(X, Y )
Encoder
Decoder
R1
Y
Encoder
R2
^
^
FIGURE 15.19. Slepian–Wolf coding.


## PDF page 576

550
NETWORK INFORMATION THEORY
and a decoder map,
g : {1, 2, . . . , 2nR1} × {1, 2, . . . , 2nR2} →Xn × Yn.
(15.156)
Here f1(Xn) is the index corresponding to Xn, f2(Y n) is the index cor-
responding to Y n, and (R1, R2) is the rate pair of the code.
Deﬁnition
The probability of error for a distributed source code is
deﬁned as
P (n)
e
= P (g(f1(Xn), f2(Y n)) ̸= (Xn, Y n)).
(15.157)
Deﬁnition
A rate pair (R1, R2) is said to be achievable for a distributed
source if there exists a sequence of ((2nR1, 2nR2), n) distributed source
codes with probability of error P (n)
e
→0. The achievable rate region is
the closure of the set of achievable rates.
Theorem 15.4.1
(Slepian–Wolf )
For the distributed source coding
problem for the source (X, Y) drawn i.i.d ∼p(x, y), the achievable rate
region is given by
R1 ≥H(X|Y),
(15.158)
R2 ≥H(Y|X),
(15.159)
R1 + R2 ≥H(X, Y).
(15.160)
Let us illustrate the result with some examples.
Example 15.4.1
Consider the weather in Gotham and Metropolis. For
the purposes of our example, we assume that Gotham is sunny with prob-
ability 0.5 and that the weather in Metropolis is the same as in Gotham
with probability 0.89. The joint distribution of the weather is given as
follows:
Metropolis
p(x, y)
Rain
Shine
Gotham
Rain
0.445
0.055
Shine
0.055
0.445


