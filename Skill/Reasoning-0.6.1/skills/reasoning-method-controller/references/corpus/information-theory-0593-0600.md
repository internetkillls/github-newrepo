# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 593

15.6
BROADCAST CHANNEL
567
that the third term goes to 0. We can also bound the fourth term in the
probability of error as
P ( ˜EY1j) = P ((U(1), X(1, j), Y1) ∈A(n)
ϵ )
(15.221)
=

(U,X,Y1)∈A(n)
ϵ
P ((U(1), X(1, j), Y1))
(15.222)
=

(U,X,Y1)∈A(n)
ϵ
P (U(1))P (X(1, j)|U(1))P (Y1|U(1))
(15.223)
≤

(U,X,Y1)∈A(n)
ϵ
2−n(H(U)−ϵ)2−n(H(X|U)−ϵ)2−n(H(Y1|U)−ϵ)
(15.224)
≤2n(H(U,X,Y1)+ϵ)2−n(H(U)−ϵ)2−n(H(X|U)−ϵ)2−n(H(Y1|U)−ϵ)
(15.225)
= 2−n(I(X;Y1|U)−4ϵ).
(15.226)
Hence, if R1 < I (X; Y1|U), the fourth term in the probability of error
goes to 0. Thus, we can bound the probability of error
P (n)
e
(1) ≤ϵ + ϵ + 2nR22−n(I(U;Y1)−3ϵ) + 2nR12−n(I(X;Y1|U)−4ϵ)
(15.227)
≤4ϵ
(15.228)
if n is large enough and R2 < I (U; Y1) and R1 < I (X; Y1|U). The above
bounds show that we can decode the messages with total probability
of error that goes to 0. Hence, there exists a sequence of good ((2nR1,
2nR2), n) codes C∗
n with probability of error going to 0. With this, we com-
plete the proof of the achievability of the capacity region for the degraded
broadcast channel. Gallager’s proof [225] of the converse is outlined in
Problem 15.11.
□
So far we have considered sending independent information to each
receiver. But in certain situations, we wish to send common information
to both receivers. Let the rate at which we send common information be
R0. Then we have the following obvious theorem:
Theorem 15.6.3
If the rate pair (R1, R2) is achievable for a broadcast
channel with independent information, the rate triple (R0, R1 −R0, R2 −
R0) with a common rate R0
is achievable, provided that R0 ≤
min(R1, R2).


## PDF page 594

568
NETWORK INFORMATION THEORY
In the case of a degraded broadcast channel, we can do even better.
Since by our coding scheme the better receiver always decodes all the
information that is sent to the worst receiver, one need not reduce the
amount of information sent to the better receiver when we have common
information. Hence, we have the following theorem:
Theorem 15.6.4
If the rate pair (R1, R2) is achievable for a degraded
broadcast channel, the rate triple (R0, R1, R2 −R0) is achievable for the
channel with common information, provided that R0 < R2.
We end this section by considering the example of the binary symmetric
broadcast channel.
Example 15.6.5
Consider a pair of binary symmetric channels with
parameters p1 and p2 that form a broadcast channel as shown in Fig-
ure 15.27. Without loss of generality in the capacity calculation, we can
recast this channel as a physically degraded channel. We assume that
p1 < p2 < 1
2. Then we can express a binary symmetric channel with
parameter p2 as a cascade of a binary symmetric channel with parameter
p1 with another binary symmetric channel. Let the crossover probability
of the new channel be α. Then we must have
p1(1 −α) + (1 −p1)α = p2
(15.229)
X
Y1
Y2
0
0
1
1
0
1
FIGURE 15.27. Binary symmetric broadcast channel.


## PDF page 595

15.6
BROADCAST CHANNEL
569
U
1 −b
1 −b
1 −a
1 −a
1 − p1
1 − p1
X
Y1
Y2
b
b
a
a
p1
p1
FIGURE 15.28. Physically degraded binary symmetric broadcast channel.
or
α = p2 −p1
1 −2p1
.
(15.230)
We now consider the auxiliary random variable in the deﬁnition of the
capacity region. In this case, the cardinality of U is binary from the bound
of the theorem. By symmetry, we connect U to X by another binary
symmetric channel with parameter β, as illustrated in Figure 15.28.
We can now calculate the rates in the capacity region. It is clear by sym-
metry that the distribution on U that maximizes the rates is the uniform
distribution on {0, 1}, so that
I (U; Y2) = H(Y2) −H(Y2|U)
(15.231)
= 1 −H(β ∗p2),
(15.232)
where
β ∗p2 = β(1 −p2) + (1 −β)p2.
(15.233)
Similarly,
I (X; Y1|U) = H(Y1|U) −H(Y1|X, U)
(15.234)
= H(Y1|U) −H(Y1|X)
(15.235)
= H(β ∗p1) −H(p1),
(15.236)
where
β ∗p1 = β(1 −p1) + (1 −β)p1.
(15.237)
Plotting these points as a function of β, we obtain the capacity region
in Figure 15.29. When β = 0, we have maximum information transfer
to Y2 [i.e., R2 = 1 −H(p2) and R1 = 0]. When β = 1
2, we have maxi-
mum information transfer to Y1 [i.e., R1 = 1 −H(p1)] and no information
transfer to Y2. These values of β give us the corner points of the rate
region.


## PDF page 596

570
NETWORK INFORMATION THEORY
R2
R1
I − H(p2)
I − H(p1)
FIGURE 15.29. Capacity region of binary symmetric broadcast channel.
Z1 ~
Y1
Y2
(0,N1)
Z ′2 ~
(0,N2 −N1)
X
FIGURE 15.30. Gaussian broadcast channel.
Example 15.6.6
(Gaussian broadcast channel)
The Gaussian broad-
cast channel is illustrated in Figure 15.30. We have shown it in the case
where one output is a degraded version of the other output. Based on
the results of Problem 15.10, it follows that all scalar Gaussian broadcast
channels are equivalent to this type of degraded channel.
Y1 = X + Z1,
(15.238)
Y2 = X + Z2 = Y1 + Z′
2,
(15.239)
where Z1 ∼N(0, N1) and Z′
2 ∼N(0, N2 −N1).
Extending the results of this section to the Gaussian case, we can show
that the capacity region of this channel is given by
R1 < C
αP
N1

(15.240)
R2 < C
(1 −α)P
αP + N2

,
(15.241)


## PDF page 597

15.7
RELAY CHANNEL
571
where α may be arbitrarily chosen (0 ≤α ≤1). The coding scheme that
achieves this capacity region is outlined in Section 15.1.3.
15.7
RELAY CHANNEL
The relay channel is a channel in which there is one sender and one
receiver with a number of intermediate nodes that act as relays to help
the communication from the sender to the receiver. The simplest relay
channel has only one intermediate or relay node. In this case the channel
consists of four ﬁnite sets X, X1, Y, and Y1 and a collection of probability
mass functions p(y, y1|x, x1) on Y × Y1, one for each (x, x1) ∈X × X1.
The interpretation is that x is the input to the channel and y is the output
of the channel, y1 is the relay’s observation, and x1 is the input symbol
chosen by the relay, as shown in Figure 15.31. The problem is to ﬁnd the
capacity of the channel between the sender X and the receiver Y.
The relay channel combines a broadcast channel (X to Y and Y1) and a
multiple-access channel (X and X1 to Y). The capacity is known for the
special case of the physically degraded relay channel. We ﬁrst prove an
outer bound on the capacity of a general relay channel and later establish
an achievable region for the degraded relay channel.
Deﬁnition
A (2nR, n) code for a relay channel consists of a set of
integers W = {1, 2, . . . , 2nR}, an encoding function
X : {1, 2, . . . , 2nR} →Xn,
(15.242)
a set of relay functions {fi}n
i=1 such that
x1i = fi(Y11, Y12, . . . , Y1i−1),
1 ≤i ≤n,
(15.243)
and a decoding function,
g : Yn →{1, 2, . . . , 2nR}.
(15.244)
X
Y1 : X1
Y
FIGURE 15.31. Relay channel.


## PDF page 598

572
NETWORK INFORMATION THEORY
Note that the deﬁnition of the encoding functions includes the nonan-
ticipatory condition on the relay. The relay channel input is allowed to
depend only on the past observations y11, y12, . . . , y1i−1. The channel is
memoryless in the sense that (Yi, Y1i) depends on the past only through
the current transmitted symbols (Xi, X1i). Thus, for any choice p(w),
w ∈W, and code choice X : {1, 2, . . . , 2nR} →Xn
i and relay functions
{fi}n
i=1, the joint probability mass function on W × Xn × Xn
1 × Yn × Yn
1
is given by
p(w, x, x1, y, y1) = p(w)
n

i=1
p(xi|w)p(x1i|y11, y12, . . . , y1i−1)
× p(yi, y1i|xi, x1i).
(15.245)
If the message w ∈[1, 2nR] is sent, let
λ(w) = Pr{g(Y) ̸= w|w sent}
(15.246)
denote the conditional probability of error. We deﬁne the average proba-
bility of error of the code as
P (n)
e
=
1
2nR

w
λ(w).
(15.247)
The probability of error is calculated under the uniform distribution over
the codewords w ∈{1, . . . , 2nR}. The rate R is said to be achievable
by the relay channel if there exists a sequence of (2nR, n) codes with
P (n)
e
→0. The capacity C of a relay channel is the supremum of the set
of achievable rates.
We ﬁrst give an upper bound on the capacity of the relay channel.
Theorem 15.7.1
For any relay channel (X × X1, p(y, y1|x, x1), Y ×
Y1), the capacity C is bounded above by
C ≤sup
p(x,x1)
min {I (X, X1; Y), I (X; Y, Y1|X1)} .
(15.248)
Proof:
The proof is a direct consequence of a more general max-ﬂow
min-cut theorem given in Section 15.10.
□
This upper bound has a nice max-ﬂow min-cut interpretation. The ﬁrst
term in (15.248) upper bounds the maximum rate of information transfer


## PDF page 599

15.7
RELAY CHANNEL
573
from senders X and X1 to receiver Y. The second terms bound the rate
from X to Y and Y1.
We now consider a family of relay channels in which the relay receiver
is better than the ultimate receiver Y in the sense deﬁned below. Here the
max-ﬂow min-cut upper bound in the (15.248) is achieved.
Deﬁnition
The relay channel (X × X1, p(y, y1|x, x1), Y × Y1) is said
to be physically degraded if p(y, y1|x, x1) can be written in the form
p(y, y1|x, x1) = p(y1|x, x1)p(y|y1, x1).
(15.249)
Thus, Y is a random degradation of the relay signal Y1.
For the physically degraded relay channel, the capacity is given by the
following theorem.
Theorem 15.7.2
The capacity C of a physically degraded relay channel
is given by
C = sup
p(x,x1)
min {I (X, X1; Y), I (X; Y1|X1)} ,
(15.250)
where the supremum is over all joint distributions on X × X1.
Proof:
Converse: The proof follows from Theorem 15.7.1 and by degradedness,
since for the degraded relay channel, I (X; Y, Y1|X1) = I (X; Y1|X1).
Achievability: The proof of achievability involves a combination
of the following basic techniques: (1) random coding, (2) list codes,
(3) Slepian–Wolf partitioning, (4) coding for the cooperative multiple-
access channel, (5) superposition coding, and (6) block Markov encoding
at the relay and transmitter. We provide only an outline of the proof.
Outline of achievability: We consider B blocks of transmission, each of
n symbols. A sequence of B −1 indices, wi ∈{1, . . . , 2nR}, i = 1, 2, . . . ,
B −1, will be sent over the channel in nB transmissions. (Note that as
B →∞for a ﬁxed n, the rate R(B −1)/B is arbitrarily close to R.)
We deﬁne a doubly indexed set of codewords:
C = {x(w|s), x1(s)} : w ∈{1, 2nR}, s ∈{1, 2nR0}, x ∈Xn, x1 ∈Xn
1 .
(15.251)
We will also need a partition
S = {S1, S2, . . . , S2nR0} of W = {1, 2, . . . , 2nR}
(15.252)


## PDF page 600

574
NETWORK INFORMATION THEORY
into 2nR0 cells, with Si ∩Sj = φ, i ̸= j, and ∪Si = W. The partition will
enable us to send side information to the receiver in the manner of Slepian
and Wolf [502].
Generation of random code: Fix p(x1)p(x|x1).
First generate
at random
2nR0
i.i.d.
n-sequences in
Xn
1 , each
drawn according to p(x1) = 
n
i=1 p(x1i). Index them as x1(s), s ∈
{1, 2, . . . , 2nR0}. For each x1(s), generate 2nR conditionally independent
n-sequences x(w|s), w ∈{1, 2, . . . , 2nR}, drawn independently accord-
ing to p(x|x1(s)) = 
n
i=1 p(xi|x1i(s)). This deﬁnes the random code-
book C = {x(w|s), x1(s)}. The random partition S = {S1, S2, . . . , S2nR0} of
{1, 2, . . . , 2nR} is deﬁned as follows. Let each integer w ∈{1, 2, . . . , 2nR}
be assigned independently, according to a uniform distribution over the
indices s = 1, 2, . . . , 2nR0, to cells Ss.
Encoding: Let wi ∈{1, 2, . . . , 2nR} be the new index to be sent in block
i, and let si be deﬁned as the partition corresponding to wi−1 (i.e., wi−1 ∈
Ssi). The encoder sends x(wi|si). The relay has an estimate ˆˆwi−1 of the
previous index wi−1. (This will be made precise in the decoding section.)
Assume that ˆˆwi−1 ∈S ˆˆsi. The relay encoder sends x1( ˆˆsi) in block i.
Decoding: We assume that at the end of block i −1, the receiver
knows (w1, w2, . . . , wi−2) and (s1, s2, . . . , si−1) and the relay knows (w1,
w2, . . . , wi−1) and consequently, (s1, s2, . . . , si). The decoding procedures
at the end of block i are as follows:
1. Knowing si and upon receiving y1(i), the relay receiver estimates
the message of the transmitter ˆˆwi = w if and only if there exists
a unique w such that (x(w|si), x1(si), y1(i)) are jointly ϵ-typical.
Using Theorem 15.2.3, it can be shown that ˆˆwi = wi with an arbi-
trarily small probability of error if
R < I (X; Y1|X1)
(15.253)
and n is sufﬁciently large.
2. The receiver declares that ˆsi = s was sent iff there exists one and
only one s such that (x1(s), y(i)) are jointly ϵ-typical. From Theo-
rem 15.2.1 we know that si can be decoded with arbitrarily small
probability of error if
R0 < I (X1; Y)
(15.254)
and n is sufﬁciently large.


