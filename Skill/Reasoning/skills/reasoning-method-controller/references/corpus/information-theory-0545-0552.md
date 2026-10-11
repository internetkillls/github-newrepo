# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 545

15.1
GAUSSIAN MULTIPLE-USER CHANNELS
519
sends it. Now, if the interference a satisﬁes C(a2P/(P + N)) > C(P/N),
the ﬁrst transmitter understands perfectly the index of the second transmit-
ter. He ﬁnds it by the usual technique of looking for the closest codeword
to his received signal. Once he ﬁnds this signal, he subtracts it from
his waveform received. Now there is a clean channel between him and
his sender. He then searches the sender’s codebook to ﬁnd the closest
codeword and declares that codeword to be the one sent.
15.1.6
Gaussian Two-Way Channel
The two-way channel is very similar to the interference channel, with the
additional provision that sender 1 is attached to receiver 2 and sender 2
is attached to receiver 1, as shown in Figure 15.6. Hence, sender 1 can
use information from previous received symbols of receiver 2 to decide
what to send next. This channel introduces another fundamental aspect
of network information theory: namely, feedback. Feedback enables the
senders to use the partial information that each has about the other’s
message to cooperate with each other.
The capacity region of the two-way channel is not known in general.
This channel was ﬁrst considered by Shannon [486], who derived upper
and lower bounds on the region (see Problem 15.15). For Gaussian chan-
nels, these two bounds coincide and the capacity region is known; in
fact, the Gaussian two-way channel decomposes into two independent
channels.
Let P1 and P2 be the powers of transmitters 1 and 2, respectively,
and let N1 and N2 be the noise variances of the two channels. Then
the rates R1 < C(P1/N1) and R2 < C(P2/N2) can be achieved by the
techniques described for the interference channel. In this case, we generate
two codebooks of rates R1 and R2. Sender 1 sends a codeword from the
ﬁrst codebook. Receiver 2 receives the sum of the codewords sent by the
p(y1, y2|x1, x2)
X1
Y1
X2
Y2
FIGURE 15.6. Two-way channel.


## PDF page 546

520
NETWORK INFORMATION THEORY
two senders plus some noise. He simply subtracts out the codeword of
sender 2 and he has a clean channel from sender 1 (with only the noise of
variance N1). Hence, the two-way Gaussian channel decomposes into two
independent Gaussian channels. But this is not the case for the general
two-way channel; in general, there is a trade-off between the two senders
so that both of them cannot send at the optimal rate at the same time.
15.2
JOINTLY TYPICAL SEQUENCES
We have previewed the capacity results for networks by considering mul-
tiuser Gaussian channels. We begin a more detailed analysis in this section,
where we extend the joint AEP proved in Chapter 7 to a form that we
will use to prove the theorems of network information theory. The joint
AEP will enable us to calculate the probability of error for jointly typical
decoding for the various coding schemes considered in this chapter.
Let (X1, X2, . . . , Xk) denote a ﬁnite collection of discrete random vari-
ables with some ﬁxed joint distribution, p(x(1), x(2), . . . , x(k)), (x(1), x(2),
. . . , x(k)) ∈X1 × X2 × · · · × Xk. Let S denote an ordered subset of these
random variables and consider n independent copies of S. Thus,
Pr{S = s} =
n

i=1
Pr{Si = si},
s ∈Sn.
(15.20)
For example, if S = (Xj, Xl), then
Pr{S = s} = Pr

(Xj, Xl) = (xj, xl)

(15.21)
=
n

i=1
p(xij, xil).
(15.22)
To be explicit, we will sometimes use X(S) for S. By the law of large
numbers, for any subset S of random variables,
−1
n log p(S1, S2, . . . , Sn) = −1
n
n

i=1
log p(Si) →H(S),
(15.23)
where the convergence takes place with probability 1 for all 2k subsets,
S ⊆{X(1), X(2), . . . , X(k)}.


## PDF page 547

15.2
JOINTLY TYPICAL SEQUENCES
521
Deﬁnition
The set A(n)
ϵ
of ϵ-typical n-sequences (x1, x2, . . . , xk) is
deﬁned by
A(n)
ϵ (X(1), X(2), . . . , X(k))
= A(n)
ϵ
=

(x1, x2, . . . , xk) :
				−1
n log p(s) −H(S)
				 < ϵ, ∀S ⊆{X(1), X(2), . . . ,
X(k)}

.
(15.24)
Let A(n)
ϵ (S) denote the restriction of A(n)
ϵ
to the coordinates of S. Thus,
if S = (X1, X2), we have
A(n)
ϵ (X1, X2) = {(x1, x2) :
				−1
n log p(x1, x2) −H(X1, X2)
				 < ϵ,
				−1
n log p(x1) −H(X1)
				 < ϵ,
				−1
n log p(x2) −H(X2)
				 < ϵ}.
(15.25)
Deﬁnition
We will use the notation an
.= 2n(b±ϵ) to mean that
				
1
n log an −b
				 < ϵ
(15.26)
for n sufﬁciently large.
Theorem 15.2.1
For any ϵ > 0, for sufﬁciently large n,
1. P (A(n)
ϵ (S)) ≥1 −ϵ,
∀S ⊆{X(1), X(2), . . . , X(k)}.
(15.27)
2. s ∈A(n)
ϵ (S) ⇒p(s) .= 2n(H(S)±ϵ).
(15.28)
3. |A(n)
ϵ (S)|
.= 2n(H(S)±2ϵ).
(15.29)


## PDF page 548

522
NETWORK INFORMATION THEORY
4. Let S1, S2 ⊆{X(1), X(2), . . . , X(k)}. If (s1, s2) ∈A(n)
ϵ (S1, S2), then
p(s1|s2)
.= 2−n(H(S1|S2)±2ϵ).
(15.30)
Proof
1. This follows from the law of large numbers for the random variables
in the deﬁnition of A(n)
ϵ (S).
2. This follows directly from the deﬁnition of A(n)
ϵ (S).
3. This follows from
1 ≥

s∈A(n)
ϵ (S)
p(s)
(15.31)
≥

s∈A(n)
ϵ (S)
2−n(H(S)+ϵ)
(15.32)
= |A(n)
ϵ (S)|2−n(H(S)+ϵ).
(15.33)
If n is sufﬁciently large, we can argue that
1 −ϵ ≤

s∈A(n)
ϵ (S)
p(s)
(15.34)
≤

s∈A(n)
ϵ (S)
2−n(H(S)−ϵ)
(15.35)
= |A(n)
ϵ (S)|2−n(H(S)−ϵ).
(15.36)
Combining (15.33) and (15.36), we have |A(n)
ϵ (S)| .= 2n(H(S)±2ϵ) for
sufﬁciently large n.
4. For (s1, s2) ∈A(n)
ϵ (S1, S2), we have p(s1)
.= 2−n(H(S1)±ϵ) and
p(s1, s2)
.= 2−n(H(S1,S2)±ϵ). Hence,
p(s2|s1) = p(s1, s2)
p(s1)
.= 2−n(H(S2|S1)±2ϵ).
□
(15.37)
The next theorem bounds the number of conditionally typical sequences
for a given typical sequence.


## PDF page 549

15.2
JOINTLY TYPICAL SEQUENCES
523
Theorem 15.2.2
Let S1, S2 be two subsets of X(1), X(2), . . . , X(k). For
any ϵ > 0, deﬁne A(n)
ϵ (S1|s2) to be the set of s1 sequences that are jointly ϵ-
typical with a particular s2 sequence. If s2 ∈A(n)
ϵ (S2), then for sufﬁciently
large n, we have
|A(n)
ϵ (S1|s2)| ≤2n(H(S1|S2)+2ϵ)
(15.38)
and
(1 −ϵ)2n(H(S1|S2)−2ϵ) ≤

s2
p(s2)|A(n)
ϵ (S1|s2)|.
(15.39)
Proof:
As in part 3 of Theorem 15.2.1, we have
1 ≥

s1∈A(n)
ϵ (S1|s2)
p(s1|s2)
(15.40)
≥

s1∈A(n)
ϵ (S1|s2)
2−n(H(S1|S2)+2ϵ)
(15.41)
= |A(n)
ϵ (S1|s2)|2−n(H(S1|S2)+2ϵ).
(15.42)
If n is sufﬁciently large, we can argue from (15.27) that
1 −ϵ ≤

s2
p(s2)

s1∈A(n)
ϵ (S1|s2)
p(s1|s2)
(15.43)
≤

s2
p(s2)

s1∈A(n)
ϵ (S1|s2)
2−n(H(S1|S2)−2ϵ)
(15.44)
=

s2
p(s2)|A(n)
ϵ (S1|s2)|2−n(H(S1|S2)−2ϵ).
□
(15.45)
To calculate the probability of decoding error, we need to know the
probability that conditionally independent sequences are jointly typical.
Let S1, S2, and S3 be three subsets of {X(1), X(2), . . . , X(k)}. If S′
1 and
S′
2 are conditionally independent given S′
3 but otherwise share the same
pairwise marginals of (S1, S2, S3), we have the following probability of
joint typicality.


## PDF page 550

524
NETWORK INFORMATION THEORY
Theorem 15.2.3
Let A(n)
ϵ
denote the typical set for the probability mass
function p(s1, s2, s3), and let
P (S′
1 = s1, S′
2 = s2, S′
3 = s3) =
n

i=1
p(s1i|s3i)p(s2i|s3i)p(s3i).
(15.46)
Then
P {(S′
1, S′
2, S′
3) ∈A(n)
ϵ }
.= 2n(I(S1;S2|S3)±6ϵ).
(15.47)
Proof:
We use the
.= notation from (15.26) to avoid calculating the
upper and lower bounds separately. We have
P {(S′
1, S′
2, S′
3) ∈A(n)
ϵ }
=

(s1, s2, s3)∈A(n)
ϵ
p(s3)p(s1|s3)p(s2|s3)
(15.48)
.= |A(n)
ϵ (S1, S2, S3)|2−n(H(S3)±ϵ)2−n(H(S1|S3)±2ϵ)2−n(H(S2|S3)±2ϵ)
(15.49)
.= 2n(H(S1,S2,S3)±ϵ)2−n(H(S3)±ϵ)2−n(H(S1|S3)±2ϵ)2−n(H(S2|S3)±2ϵ)
(15.50)
.= 2−n(I(S1;S2|S3)±6ϵ).
□
(15.51)
We will specialize this theorem to particular choices of S1, S2, and S3
for the various achievability proofs in this chapter.
15.3
MULTIPLE-ACCESS CHANNEL
The ﬁrst channel that we examine in detail is the multiple-access channel,
in which two (or more) senders send information to a common receiver.
The channel is illustrated in Figure 15.7. A common example of this
channel is a satellite receiver with many independent ground stations, or
a set of cell phones communicating with a base station. We see that the
senders must contend not only with the receiver noise but with interference
from each other as well.
Deﬁnition
A discrete memoryless multiple-access channel consists of
three alphabets, X1, X2, and Y, and a probability transition matrix
p(y|x1, x2).


## PDF page 551

15.3
MULTIPLE-ACCESS CHANNEL
525
p(y |x1, x2)
X1
Y1
W1
(W1, W2)
W2
Y
^
^
FIGURE 15.7. Multiple-access channel.
Deﬁnition
A ((2nR1, 2nR2), n) code for the multiple-access channel con-
sists of two sets of integers W1 = {1, 2, . . . , 2nR1} and W2 = {1, 2, . . . ,
2nR2}, called the message sets, two encoding functions,
X1 : W1 →Xn
1
(15.52)
and
X2 : W2 →Xn
2,
(15.53)
and a decoding function,
g : Yn →W1 × W2.
(15.54)
There are two senders and one receiver for this channel. Sender 1
chooses an index W1 uniformly from the set {1, 2, . . . , 2nR1} and sends
the corresponding codeword over the channel. Sender 2 does likewise.
Assuming that the distribution of messages over the product set W1 × W2
is uniform (i.e., the messages are independent and equally likely), we
deﬁne the average probability of error for the ((2nR1, 2nR2), n) code as
follows:
P (n)
e
=
1
2n(R1+R2)

(w1,w2)∈W1×W2
Pr

g(Y n) ̸= (w1, w2)|(w1, w2) sent

.
(15.55)
Deﬁnition
A rate pair (R1, R2) is said to be achievable for the multiple-
access channel if there exists a sequence of ((2nR1, 2nR2), n) codes with
P (n)
e
→0.


## PDF page 552

526
NETWORK INFORMATION THEORY
Deﬁnition
The capacity region of the multiple-access channel is the
closure of the set of achievable (R1, R2) rate pairs.
An example of the capacity region for a multiple-access channel is
illustrated in Figure 15.8. We ﬁrst state the capacity region in the form of
a theorem.
Theorem 15.3.1
(Multiple-access channel capacity)
The capacity of
a multiple-access channel (X1 × X2, p(y|x1, x2), Y) is the closure of the
convex hull of all (R1, R2) satisfying
R1 < I (X1; Y|X2),
(15.56)
R2 < I (X2; Y|X1),
(15.57)
R1 + R2 < I (X1, X2; Y)
(15.58)
for some product distribution p1(x1)p2(x2) on X1 × X2.
Before we prove that this is the capacity region of the multiple-access
channel, let us consider a few examples of multiple-access channels:
Example 15.3.1
(Independent binary symmetric channels)
Assume
that we have two independent binary symmetric channels, one from sender
1 and the other from sender 2, as shown in Figure 15.9. In this case, it is
obvious from the results of Chapter 7 that we can send at rate 1 −H(p1)
over the ﬁrst channel and at rate 1 −H(p2) over the second channel.
R1
R2
0
C2
C1
FIGURE 15.8. Capacity region for a multiple-access channel.


