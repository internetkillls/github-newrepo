# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 537

NETWORK INFORMATION THEORY
511
(X1, Y1)
(X2, Y2)
(Xm, Ym)
FIGURE 15.3. Communication network.
and on past received symbols at the node. The simultaneous transmis-
sion of the symbols (x1, x2, . . . , xm) results in random received symbols
(Y1, Y2, . . . , Ym) drawn according to the conditional probability distribu-
tion p(y(1), y(2), . . . , y(m)|x(1), x(2), . . . , x(m)). Here p(·|·) expresses the
effects of the noise and interference present in the network. If p(·|·) takes
on only the values 0 and 1, the network is deterministic.
Associated with some of the nodes in the network are stochastic data
sources, which are to be communicated to some of the other nodes in the
network. If the sources are independent, the messages sent by the nodes
are also independent. However, for full generality, we must allow the
sources to be dependent. How does one take advantage of the dependence
to reduce the amount of information transmitted? Given the probability
distribution of the sources and the channel transition function, can one
transmit these sources over the channel and recover the sources at the
destinations with the appropriate distortion?
We consider various special cases of network communication. We con-
sider the problem of source coding when the channels are noiseless and
without interference. In such cases, the problem reduces to ﬁnding the set
of rates associated with each source such that the required sources can
be decoded at the destination with a low probability of error (or appro-
priate distortion). The simplest case for distributed source coding is the
Slepian–Wolf source coding problem, where we have two sources that
must be encoded separately, but decoded together at a common node. We
consider extensions to this theory when only one of the two sources needs
to be recovered at the destination.
The theory of ﬂow in networks has satisfying answers in such domains
as circuit theory and the ﬂow of water in pipes. For example, for the
single-source single-sink network of pipes shown in Figure 15.4, the max-
imum ﬂow from A to B can be computed easily from the Ford–Fulkerson
theorem . Assume that the edges have capacities Ci as shown. Clearly,


## PDF page 538

512
NETWORK INFORMATION THEORY
C1
A
B
C2
C4
C5
C = min{C1 + C2, C2 + C3 + C4, C4 + C5, C1 + C5}
C3
FIGURE 15.4. Network of water pipes.
the maximum ﬂow across any cut set cannot be greater than the sum
of the capacities of the cut edges. Thus, minimizing the maximum ﬂow
across cut sets yields an upper bound on the capacity of the network. The
Ford–Fulkerson theorem [214] shows that this capacity can be achieved.
The theory of information ﬂow in networks does not have the same
simple answers as the theory of ﬂow of water in pipes. Although we
prove an upper bound on the rate of information ﬂow across any cut set,
these bounds are not achievable in general. However, it is gratifying that
some problems, such as the relay channel and the cascade channel, admit
a simple max-ﬂow min-cut interpretation. Another subtle problem in the
search for a general theory is the absence of a source–channel separation
theorem, which we touch on brieﬂy in Section 15.10. A complete theory
combining distributed source coding and network channel coding is still
a distant goal.
In the next section we consider Gaussian examples of some of the
basic channels of network information theory. The physically motivated
Gaussian channel lends itself to concrete and easily interpreted answers.
Later we prove some of the basic results about joint typicality that we use
to prove the theorems of multiuser information theory. We then consider
various problems in detail: the multiple-access channel, the coding of cor-
related sources (Slepian–Wolf data compression), the broadcast channel,
the relay channel, the coding of a random variable with side information,
and the rate distortion problem with side information. We end with an
introduction to the general theory of information ﬂow in networks. There
are a number of open problems in the area, and there does not yet exist a
comprehensive theory of information networks. Even if such a theory is
found, it may be too complex for easy implementation. But the theory will
be able to tell communication designers how close they are to optimality
and perhaps suggest some means of improving the communication rates.


## PDF page 539

15.1
GAUSSIAN MULTIPLE-USER CHANNELS
513
15.1
GAUSSIAN MULTIPLE-USER CHANNELS
Gaussian multiple-user channels illustrate some of the important features
of network information theory. The intuition gained in Chapter 9 on the
Gaussian channel should make this section a useful introduction. Here the
key ideas for establishing the capacity regions of the Gaussian multiple-
access, broadcast, relay, and two-way channels will be given without
proof. The proofs of the coding theorems for the discrete memoryless
counterparts to these theorems are given in later sections of the chapter.
The basic discrete-time additive white Gaussian noise channel with
input power P and noise variance N is modeled by
Yi = Xi + Zi,
i = 1, 2, . . . ,
(15.1)
where the Zi are i.i.d. Gaussian random variables with mean 0 and vari-
ance N. The signal X = (X1, X2, . . . , Xn) has a power constraint
1
n
n

i=1
X2
i ≤P.
(15.2)
The Shannon capacity C is obtained by maximizing I (X; Y) over all
random variables X such that EX2 ≤P and is given (Chapter 9) by
C = 1
2 log

1 + P
N

bits per transmission.
(15.3)
In this chapter we restrict our attention to discrete-time memoryless chan-
nels; the results can be extended to continuous-time Gaussian channels.
15.1.1
Single-User Gaussian Channel
We ﬁrst review the single-user Gaussian channel studied in Chapter 9.
Here Y = X + Z. Choose a rate R < 1
2 log(1 + P
N ). Fix a good (2nR, n)
codebook of power P . Choose an index w in the set 2nR. Send the
wth codeword X(w) from the codebook generated above. The receiver
observes Y = X(w) + Z and then ﬁnds the index ˆw of the codeword
closest to Y. If n is sufﬁciently large, the probability of error Pr(w ̸= ˆw)
will be arbitrarily small. As can be seen from the deﬁnition of joint typ-
icality, this minimum-distance decoding scheme is essentially equivalent
to ﬁnding the codeword in the codebook that is jointly typical with the
received vector Y.


## PDF page 540

514
NETWORK INFORMATION THEORY
15.1.2
Gaussian Multiple-Access Channel with m Users
We consider m transmitters, each with a power P . Let
Y =
m

i=1
Xi + Z.
(15.4)
Let
C
P
N

= 1
2 log

1 + P
N

(15.5)
denote the capacity of a single-user Gaussian channel with signal-to-noise
ratio P/N. The achievable rate region for the Gaussian channel takes on
the simple form given in the following equations:
Ri < C
P
N

(15.6)
Ri + Rj < C
2P
N

(15.7)
Ri + Rj + Rk < C
3P
N

(15.8)
...
(15.9)
m

i=1
Ri < C
mP
N

.
(15.10)
Note that when all the rates are the same, the last inequality dominates
the others.
Here we need m codebooks, the ith codebook having 2nRi codewords
of power P . Transmission is simple. Each of the independent transmitters
chooses an arbitrary codeword from its own codebook. The users send
these vectors simultaneously. The receiver sees these codewords added
together with the Gaussian noise Z.
Optimal decoding consists of looking for the m codewords, one from
each codebook, such that the vector sum is closest to Y in Euclidean
distance. If (R1, R2, . . . , Rm) is in the capacity region given above, the
probability of error goes to 0 as n tends to inﬁnity.


## PDF page 541

15.1
GAUSSIAN MULTIPLE-USER CHANNELS
515
Remarks
It is exciting to see in this problem that the sum of the rates
of the users C(mP/N) goes to inﬁnity with m. Thus, in a cocktail party
with m celebrants of power P in the presence of ambient noise N, the
intended listener receives an unbounded amount of information as the
number of people grows to inﬁnity. A similar conclusion holds, of course,
for ground communications to a satellite. Apparently, the increasing inter-
ference as the number of senders m →∞does not limit the total received
information.
It is also interesting to note that the optimal transmission scheme here
does not involve time-division multiplexing. In fact, each of the transmit-
ters uses all of the bandwidth all of the time.
15.1.3
Gaussian Broadcast Channel
Here we assume that we have a sender of power P and two distant
receivers, one with Gaussian noise power N1 and the other with Gaussian
noise power N2. Without loss of generality, assume that N1 < N2. Thus,
receiver Y1 is less noisy than receiver Y2. The model for the channel is
Y1 = X + Z1 and Y2 = X + Z2, where Z1 and Z2 are arbitrarily corre-
lated Gaussian random variables with variances N1 and N2, respectively.
The sender wishes to send independent messages at rates R1 and R2 to
receivers Y1 and Y2, respectively.
Fortunately, all scalar Gaussian broadcast channels belong to the class
of degraded broadcast channels discussed in Section 15.6.2. Specializing
that work, we ﬁnd that the capacity region of the Gaussian broadcast
channel is
R1 < C
αP
N1

(15.11)
R2 < C
(1 −α)P
αP + N2

,
(15.12)
where α may be arbitrarily chosen (0 ≤α ≤1) to trade off rate R1 for
rate R2 as the transmitter wishes.
To encode the messages, the transmitter generates two codebooks, one
with power αP at rate R1, and another codebook with power αP at rate
R2, where R1 and R2 lie in the capacity region above. Then to send
an index w1 ∈{1, 2, . . . , 2nR1} and w2 ∈{1, 2, . . . , 2nR2} to Y1 and Y2,
respectively, the transmitter takes the codeword X(w1) from the ﬁrst code-
book and codeword X(w2) from the second codebook and computes the
sum. He sends the sum over the channel.


## PDF page 542

516
NETWORK INFORMATION THEORY
The receivers must now decode the messages. First consider the bad
receiver Y2. He merely looks through the second codebook to ﬁnd the clos-
est codeword to the received vector Y2. His effective signal-to-noise ratio is
αP/(αP + N2), since Y1’s messageacts as noise toY2. (This canbe proved.)
The good receiver Y1 ﬁrst decodes Y2’s codeword, which he can accom-
plish because of his lower noise N1. He subtracts this codeword ˆX2 from
Y1. He then looks for the codeword in the ﬁrst codebook closest to
Y1 −ˆX2. The resulting probability of error can be made as low as desired.
A nice dividend of optimal encoding for degraded broadcast channels is
that the better receiver Y1 always knows the message intended for receiver
Y2 in addition to the message intended for himself.
15.1.4
Gaussian Relay Channel
For the relay channel, we have a sender X and an ultimate intended
receiver Y. Also present is the relay channel, intended solely to help the
receiver. The Gaussian relay channel (Figure 15.31 in Section 15.7) is
given by
Y1 = X + Z1,
(15.13)
Y = X + Z1 + X1 + Z2,
(15.14)
where Z1 and Z2 are independent zero-mean Gaussian random variables
with variance N1 and N2, respectively. The encoding allowed by the relay
is the causal sequence
X1i = fi(Y11, Y12, . . . , Y1i−1).
(15.15)
Sender X has power P and sender X1 has power P1. The capacity is
C = max
0≤α≤1 min

C
P + P1 + 2√αP P1
N1 + N2

, C
αP
N1

,
(15.16)
where α = 1 −α. Note that if
P1
N2
≥P
N1
,
(15.17)
it can be seen that C = C(P/N1),which is achieved by α = 1. The channel
appears to be noise-free after the relay, and the capacity C(P/N1) from
X to the relay can be achieved. Thus, the rate C(P/(N1 + N2)) without
the relay is increased by the presence of the relay to C(P/N1). For large


## PDF page 543

15.1
GAUSSIAN MULTIPLE-USER CHANNELS
517
N2 and for P1/N2 ≥P/N1, we see that the increment in rate is from
C(P/(N1 + N2)) ≈0 to C(P/N1).
Let R1 < C(αP/N1). Two codebooks are needed. The ﬁrst codebook
has 2nR1 words of power αP . The second has 2nR0 codewords of power
αP . We shall use codewords from these codebooks successively to cre-
ate the opportunity for cooperation by the relay. We start by sending a
codeword from the ﬁrst codebook. The relay now knows the index of
this codeword since R1 < C(αP/N1), but the intended receiver has a list
of possible codewords of size 2n(R1−C(αP/(N1+N2))). This list calculation
involves a result on list codes.
In the next block, the transmitter and the relay wish to cooperate to
resolve the receiver’s uncertainty about the codeword sent previously that
is on the receiver’s list. Unfortunately, they cannot be sure what this list
is because they do not know the received signal Y. Thus, they randomly
partition the ﬁrst codebook into 2nR0 cells with an equal number of code-
words in each cell. The relay, the receiver, and the transmitter agree on
this partition. The relay and the transmitter ﬁnd the cell of the partition
in which the codeword from the ﬁrst codebook lies and cooperatively
send the codeword from the second codebook with that index. That is, X
and X1 send the same designated codeword. The relay, of course, must
scale this codeword so that it meets his power constraint P1. They now
transmit their codewords simultaneously. An important point to note here
is that the cooperative information sent by the relay and the transmitter
is sent coherently. So the power of the sum as seen by the receiver Y is
(
√
αP + √P1)2.
However, this does not exhaust what the transmitter does in the second
block. He also chooses a fresh codeword from the ﬁrst codebook, adds it
“on paper” to the cooperative codeword from the second codebook, and
sends the sum over the channel.
The reception by the ultimate receiver Y in the second block involves
ﬁrst ﬁnding the cooperative index from the second codebook by looking
for the closest codeword in the second codebook. He subtracts the code-
word from the received sequence and then calculates a list of indices of
size 2nR0 corresponding to all codewords of the ﬁrst codebook that might
have been sent in the second block.
Now it is time for the intended receiver to complete computing the
codeword from the ﬁrst codebook sent in the ﬁrst block. He takes his list
of possible codewords that might have been sent in the ﬁrst block and
intersects it with the cell of the partition that he has learned from the
cooperative relay transmission in the second block. The rates and powers
have been chosen so that it is highly probable that there is only one


## PDF page 544

518
NETWORK INFORMATION THEORY
codeword in the intersection. This is Y’s guess about the information sent
in the ﬁrst block.
We are now in steady state. In each new block, the transmitter and the
relay cooperate to resolve the list uncertainty from the previous block. In
addition, the transmitter superimposes some fresh information from his
ﬁrst codebook to this transmission from the second codebook and trans-
mits the sum. The receiver is always one block behind, but for sufﬁciently
many blocks, this does not affect his overall rate of reception.
15.1.5
Gaussian Interference Channel
The interference channel has two senders and two receivers. Sender 1
wishes to send information to receiver 1. He does not care what receiver
2 receives or understands; similarly with sender 2 and receiver 2. Each
channel interferes with the other. This channel is illustrated in Figure 15.5.
It is not quite a broadcast channel since there is only one intended receiver
for each sender, nor is it a multiple access channel because each receiver
is only interested in what is being sent by the corresponding transmitter.
For symmetric interference, we have
Y1 = X1 + aX2 + Z1
(15.18)
Y2 = X2 + aX1 + Z2,
(15.19)
where Z1, Z2 are independent N(0, N) random variables. This channel has
not been solved in general even in the Gaussian case. But remarkably, in
the case of high interference, it can be shown that the capacity region of
this channel is the same as if there were no interference whatsoever.
To achieve this, generate two codebooks, each with power P and rate
C(P/N). Each sender independently chooses a word from his book and
X1
Y1
X2
Y2
Z1 ~
(0,N )
Z2 ~
(0,N )
a
a
FIGURE 15.5. Gaussian interference channel.


