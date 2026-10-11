# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 585

15.5
SLEPIAN–WOLF ENCODING AND MULTIPLE-ACCESS CHANNELS
559
p(y|x1, x2)
X1
X2
W1
(W1, W2)
W2
Y
^
^
FIGURE 15.23. Multiple-access channels.
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
FIGURE 15.24. Correlated source encoding.
sequences Xn
1 and Xn
2. In the proof for Slepian–Wolf coding, we used a
random map from the set of sequences Xn and Y n to a set of messages.
In the proof of the coding theorem for the multiple-access channel, the
probability of error was bounded by
P (n)
e
≤ϵ +

codewords
Pr(codeword jointly typical with sequence received)
(15.197)
= ϵ +

2nR1 terms
2−nI1 +

2nR2 terms
2−nI2 +

2n(R1+R2) terms
2−nI3,
(15.198)


## PDF page 586

560
NETWORK INFORMATION THEORY
where ϵ is the probability the sequences are not typical, Ri are the rates
corresponding to the number of codewords that can contribute to the
probability of error, and Ii is the corresponding mutual information that
corresponds to the probability that the codeword is jointly typical with
the received sequence.
In the case of Slepian–Wolf encoding, the corresponding expression
for the probability of error is
P (n)
e
≤ϵ +

jointly typical sequences
Pr( have the same codeword)
(15.199)
= ϵ +

2nH1 terms
2−nR1 +

2nH2 terms
2−nR2 +

2nH3 terms
2−n(R1+R2),
(15.200)
where again the probability that the constraints of the AEP are not satisﬁed
is bounded by ϵ, and the other terms refer to the various ways in which
another pair of sequences could be jointly typical and in the same bin as
the given source pair.
The duality of the multiple-access channel and correlated source encod-
ing is now obvious. It is rather surprising that these two systems are duals
of each other; one would have expected a duality between the broadcast
channel and the multiple-access channel.
15.6
BROADCAST CHANNEL
The broadcast channel is a communication channel in which there is one
sender and two or more receivers. It is illustrated in Figure 15.25. The
basic problem is to ﬁnd the set of simultaneously achievable rates for
communication in a broadcast channel. Before we begin the analysis, let
us consider some examples.
Example 15.6.1
(TV station)
The simplest example of the broadcast
channel is a radio or TV station. But this example is slightly degenerate
in the sense that normally the station wants to send the same informa-
tion to everybody who is tuned in; the capacity is essentially maxp(x)
mini I (X; Yi), which may be less than the capacity of the worst receiver.
But we may wish to arrange the information in such a way that the bet-
ter receivers receive extra information, which produces a better picture
or sound, while the worst receivers continue to receive more basic infor-
mation. As TV stations introduce high-deﬁnition TV (HDTV), it may be
necessary to encode the information so that bad receivers will receive the


## PDF page 587

15.6
BROADCAST CHANNEL
561
(W1, W2)
W1
Decoder
p(y1, y2|x)
W2
Y1
Y2
Decoder
Encoder
X
^
^
FIGURE 15.25. Broadcast channel.
regular TV signal, while good receivers will receive the extra informa-
tion for the high-deﬁnition signal. The methods to accomplish this will
be explained in the discussion of the broadcast channel.
Example 15.6.2
(Lecturer in classroom)
A lecturer in a classroom is
communicating information to the students in the class. Due to differences
among the students, they receive various amounts of information. Some of
the students receive most of the information; others receive only a little. In
the ideal situation, the lecturer would be able to tailor his or her lecture in
such a way that the good students receive more information and the poor
students receive at least the minimum amount of information. However, a
poorly prepared lecture proceeds at the pace of the weakest student. This
situation is another example of a broadcast channel.
Example 15.6.3
(Orthogonal broadcast channels)
Thesimplestbroad-
cast channel consists of two independent channels to the two receivers.
Here we can send independent information over both channels, and we
can achieve rate R1 to receiver 1 and rate R2 to receiver 2 if R1 < C1 and
R2 < C2. The capacity region is the rectangle shown in Figure 15.26.
Example 15.6.4
(Spanish and Dutch speaker)
To illustrate the idea of
superposition, we will consider a simpliﬁed example of a speaker who can
speak both Spanish and Dutch. There are two listeners: One understands
only Spanish and the other understands only Dutch. Assume for simplicity
that the vocabulary of each language is 220 words and that the speaker
speaks at the rate of 1 word per second in either language. Then he


## PDF page 588

562
NETWORK INFORMATION THEORY
R2
R1
C2
C1
0
FIGURE 15.26. Capacity region for two orthogonal broadcast channels.
can transmit 20 bits of information per second to receiver 1 by speaking
to her all the time; in this case, he sends no information to receiver 2.
Similarly, he can send 20 bits per second to receiver 2 without sending
any information to receiver 1. Thus, he can achieve any rate pair with
R1 + R2 = 20 by simple time-sharing. But can he do better?
Recall that the Dutch listener, even though he does not understand
Spanish, can recognize when the word is Spanish. Similarly, the Spanish
listener can recognize when Dutch occurs. The speaker can use this to
convey information; for example, if the proportion of time he uses each
language is 50%, then of a sequence of 100 words, about 50 will be
Dutch and about 50 will be Spanish. But there are many ways to order the
Spanish and Dutch words; in fact, there are about
100
50

≈2100H( 1
2) ways
to order the words. Choosing one of these orderings conveys information
to both listeners. This method enables the speaker to send information at
a rate of 10 bits per second to the Dutch receiver, 10 bits per second to
the Spanish receiver, and 1 bit per second of common information to both
receivers, for a total rate of 21 bits per second, which is more than that
achievable by simple timesharing. This is an example of superposition of
information.
The results of the broadcast channel can also be applied to the case
of a single-user channel with an unknown distribution. In this case, the
objective is to get at least the minimum information through when the
channel is bad and to get some extra information through when the channel
is good. We can use the same superposition arguments as in the case of
the broadcast channel to ﬁnd the rates at which we can send information.


## PDF page 589

15.6
BROADCAST CHANNEL
563
15.6.1
Deﬁnitions for a Broadcast Channel
Deﬁnition
A broadcast channel consists of an input alphabet X and
two output alphabets, Y1 and Y2, and a probability transition function
p(y1, y2|x). The broadcast channel will be said to be memoryless if
p(yn
1, yn
2|xn) = 
n
i=1 p(y1i, y2i|xi).
We deﬁne codes, probability of error, achievability, and capacity regions
for the broadcast channel as we did for the multiple-access channel. A
((2nR1, 2nR2), n) code for a broadcast channel with independent informa-
tion consists of an encoder,
X : ({1, 2, . . . , 2nR1} × {1, 2, . . . , 2nR2}) →Xn,
(15.201)
and two decoders,
g1 : Yn
1 →{1, 2, . . . , 2nR1}
(15.202)
and
g2 : Yn
2 →{1, 2, . . . , 2nR2}.
(15.203)
We deﬁne the average probability of error as the probability that the
decoded message is not equal to the transmitted message; that is,
P (n)
e
= P (g1(Y n
1 ) ̸= W1
or
g2(Y n
2 ) ̸= W2),
(15.204)
where (W1, W2) are assumed to be uniformly distributed over 2nR1 × 2nR2.
Deﬁnition
A rate pair (R1, R2) is said to be achievable for the broad-
cast channel if there exists a sequence of ((2nR1, 2nR2), n) codes with
P (n)
e
→0.
We will now deﬁne the rates for the case where we have common
information to be sent to both receivers. A ((2nR0, 2nR1, 2nR2), n) code
for a broadcast channel with common information consists of an encoder,
X : ({1, 2, . . . , 2nR0} × {1, 2, . . . , 2nR1} × {1, 2, . . . , 2nR2}) →Xn,
(15.205)
and two decoders,
g1 : Yn
1 →{1, 2, . . . , 2nR0} × {1, 2, . . . , 2nR1}
(15.206)
and
g2 : Yn
2 →{1, 2, . . . , 2nR0} × {1, 2, . . . , 2nR2}.
(15.207)


## PDF page 590

564
NETWORK INFORMATION THEORY
Assuming that the distribution on (W0, W1, W2) is uniform, we can deﬁne
the probability of error as the probability that the decoded message is not
equal to the transmitted message:
P (n)
e
= P (g1(Y n
1 ) ̸= (W0, W1) or g2(Zn) ̸= (W0, W2)).
(15.208)
Deﬁnition
A rate triple (R0, R1, R2) is said to be achievable for the
broadcast channel with common information if there exists a sequence of
((2nR0, 2nR1, 2nR2), n) codes with P (n)
e
→0.
Deﬁnition
The capacity region of the broadcast channel is the closure
of the set of achievable rates.
We observe that an error for receiver Y n
1 depends only the distribution
p(xn, yn
1) and not on the joint distribution p(xn, yn
1, yn
2). Thus, we have
the following theorem:
Theorem 15.6.1
The capacity region of a broadcast channel depends
only on the conditional marginal distributions p(y1|x) and p(y2|x).
Proof:
See the problems.
□
15.6.2
Degraded Broadcast Channels
Deﬁnition
A broadcast channel is said to be physically degraded if
p(y1, y2|x) = p(y1|x)p(y2|y1).
Deﬁnition
A broadcast channel is said to be stochastically degraded if
its conditional marginal distributions are the same as that of a physically
degraded broadcast channel; that is, if there exists a distribution p′(y2|y1)
such that
p(y2|x) =

y1
p(y1|x)p′(y2|y1).
(15.209)
Note that since the capacity of a broadcast channel depends only on the
conditional marginals, the capacity region of the stochastically degraded
broadcast channel is the same as that of the corresponding physically
degraded channel. In much of the following, we therefore assume that the
channel is physically degraded.


## PDF page 591

15.6
BROADCAST CHANNEL
565
15.6.3
Capacity Region for the Degraded Broadcast Channel
We now consider sending independent information over a degraded broad-
cast channel at rate R1 to Y1 and rate R2 to Y2.
Theorem 15.6.2
The capacity region for sending independent infor-
mation over the degraded broadcast channel X →Y1 →Y2 is the convex
hull of the closure of all (R1, R2) satisfying
R2 ≤I (U; Y2),
(15.210)
R1 ≤I (X; Y1|U)
(15.211)
for some joint distribution p(u)p(x|u)p(y1, y2|x), where the auxiliary ran-
dom variable U has cardinality bounded by |U| ≤min{|X|, |Y1|, |Y2|}.
Proof:
(The cardinality bounds for the auxiliary random variable U are
derived using standard methods from convex set theory and are not dealt
with here.) We ﬁrst give an outline of the basic idea of superposition
coding for the broadcast channel. The auxiliary random variable U will
serve as a cloud center that can be distinguished by both receivers Y1
and Y2. Each cloud consists of 2nR1 codewords Xn distinguishable by the
receiver Y1. The worst receiver can only see the clouds, while the better
receiver can see the individual codewords within the clouds. The formal
proof of the achievability of this region uses a random coding argument:
Fix p(u) and p(x|u).
Random codebook generation: Generate 2nR2 independent codewords
of length n, U(w2), w2 ∈{1, 2, . . . , 2nR2}, according to 
n
i=1 p(ui). For
each codeword U(w2), generate 2nR1 independent codewords X(w1, w2)
according to 
n
i=1 p(xi|ui(w2)). Here u(i) plays the role of the cloud
center understandable to both Y1 and Y2, while x(i, j) is the jth satellite
codeword in the ith cloud.
Encoding: To send the pair (W1, W2), send the corresponding codeword
X(W1, W2).
Decoding: Receiver 2 determines the unique ˆˆW 2 such that (U( ˆˆW 2),
Y2) ∈A(n)
ϵ . If there are none such or more than one such, an error is
declared.
Receiver 1 looks for the unique ( ˆW1, ˆW2) such that (U( ˆW2), X( ˆW1, ˆW2),
Y1) ∈A(n)
ϵ . If there are none such or more than one such, an error is
declared.
Analysis of the probability of error: By the symmetry of the code gen-
eration, the probability of error does not depend on which codeword was


## PDF page 592

566
NETWORK INFORMATION THEORY
sent. Hence, without loss of generality, we can assume that the mes-
sage pair (W1, W2) = (1, 1) was sent. Let P (·) denote the conditional
probability of an event given that (1,1) was sent.
Since we have essentially a single-user channel from U to Y2, we will
be able to decode the U codewords with a low probability of error if
R2 < I (U; Y2). To prove this, we deﬁne the events
EYi = {(U(i), Y2) ∈A(n)
ϵ }.
(15.212)
Then the probability of error at receiver 2 is
P (n)
e
(2) = P (Ec
Y1
 
i̸=1
EYi)
(15.213)
≤P (Ec
Y1) +

i̸=1
P (EYi)
(15.214)
≤ϵ + 2nR22−n(I(U;Y2)−2ϵ)
(15.215)
≤2ϵ
(15.216)
if n is large enough and R2 < I (U; Y2), where (15.215) follows from the
AEP. Similarly, for decoding for receiver 1, we deﬁne the events
˜EYi = {(U(i), Y1) ∈A(n)
ϵ },
(15.217)
˜EYij = {(U(i), X(i, j), Y1) ∈A(n)
ϵ },
(15.218)
where the tilde refers to events deﬁned at receiver 1. Then we can bound
the probability of error as
P (n)
e
(1) = P

˜Ec
Y1
 ˜Ec
Y11
 
i̸=1
˜EYi
 
j̸=1
˜EY1j


(15.219)
≤P ( ˜Ec
Y1) + P ( ˜Ec
Y11) +

i̸=1
P ( ˜EYi) +

j̸=1
P ( ˜EY1j). (15.220)
By the same arguments as for receiver 2, we can bound P ( ˜EYi) ≤
2−n(I(U;Y1)−3ϵ). Hence, the third term goes to 0 if R2 < I (U; Y1). But
by the data-processing inequality and the degraded nature of the chan-
nel, I (U; Y1) ≥I (U; Y2), and hence the conditions of the theorem imply


