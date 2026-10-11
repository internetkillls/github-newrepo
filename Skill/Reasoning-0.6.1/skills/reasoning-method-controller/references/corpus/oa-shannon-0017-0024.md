# A Mathematical Theory of Communication

Source ID: C05
Authors: Claude E. Shannon
Source URL: https://www.princeton.edu/~wbialek/rome/refs/shannon_48.pdf
DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x
Identity: Corrected reprint of the two-part Bell System Technical Journal article, 1948. Reprint pagination differs from journal pagination.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 17

As N increases
,
 and
' approach zero and the rate approaches C
H .
Another method of performing this coding and thereby proving the theorem can be described as follows:
Arrange the messages of length N in order of decreasing probability and suppose their probabilities are
p1
 p2
 p3



 pn. Let Ps
= ∑s1
1
pi; that is Ps is the cumulative probability up to, but not including, ps.
We ﬁrst encode into a binary system. The binary code for message s is obtained by expanding Ps as a binary
number. The expansion is carried out to ms places, where ms is the integer satisfying:
log2
1
ps
 ms
< 1
+log2
1
ps
:
Thus the messages of high probability are represented by short codes and those of low probability by long
codes. From these inequalities we have
1
2ms
 ps
<
1
2ms
1
:
The code for Ps will differ from all succeeding ones in one or more of its ms places, since all the remaining
Pi are at least
1
2ms larger and their binary expansions therefore differ in the ﬁrst ms places. Consequently all
the codes are different and it is possible to recover the message from its code. If the channel sequences are
not already sequences of binary digits, they can be ascribed binary numbers in an arbitrary fashion and the
binary code thus translated into signals suitable for the channel.
The average number H
0 of binary digits used per symbol of original message is easily estimated. We
have
H
0
= 1
N ∑msps
:
But,
1
N ∑

log2
1
ps

ps
 1
N ∑msps
< 1
N ∑

1
+log2
1
ps

ps
and therefore,
GN
 H
0
< GN
+ 1
N
As N increases GN approaches H, the entropy of the source and H
0 approaches H.
We see from this that the inefﬁciency in coding, when only a ﬁnite delay of N symbols is used, need
not be greater than 1
N plus the difference between the true entropy H and the entropy GN calculated for
sequences of length N. The per cent excess time needed over the ideal is therefore less than
GN
H
+ 1
HN
1 :
This method of encoding is substantially the same as one found independently by R. M. Fano.9 His
method is to arrange the messages of length N in order of decreasing probability. Divide this series into two
groups of as nearly equal probability as possible. If the message is in the ﬁrst group its ﬁrst binary digit
will be 0, otherwise 1. The groups are similarly divided into subsets of nearly equal probability and the
particular subset determines the second binary digit. This process is continued until each subset contains
only one message. It is easily seen that apart from minor differences (generally in the last digit) this amounts
to the same thing as the arithmetic process described above.
10. DISCUSSION AND EXAMPLES
In order to obtain the maximum power transfer from a generator to a load, a transformer must in general be
introduced so that the generator as seen from the load has the load resistance. The situation here is roughly
analogous. The transducer which does the encoding should match the source to the channel in a statistical
sense. The source as seen from the channel through the transducer should have the same statistical structure
9Technical Report No. 65, The Research Laboratory of Electronics, M.I.T., March 17, 1949.
17


## PDF page 18

as the source which maximizes the entropy in the channel. The content of Theorem 9 is that, although an
exact match is not in general possible, we can approximate it as closely as desired. The ratio of the actual
rate of transmission to the capacity C may be called the efﬁciency of the coding system. This is of course
equal to the ratio of the actual entropy of the channel symbols to the maximum possible entropy.
In general, ideal or nearly ideal encoding requires a long delay in the transmitter and receiver. In the
noiseless case which we have been considering, the main function of this delay is to allow reasonably good
matching of probabilities to corresponding lengths of sequences. With a good code the logarithm of the
reciprocal probability of a long message must be proportional to the duration of the corresponding signal, in
fact


log p
1
T
C



must be small for all but a small fraction of the long messages.
If a source can produce only one particular message its entropy is zero, and no channel is required. For
example, a computing machine set up to calculate the successive digits of
 produces a deﬁnite sequence
with no chance element. No channel is required to “transmit” this to another point. One could construct a
second machine to compute the same sequence at the point. However, this may be impractical. In such a case
we can choose to ignore some or all of the statistical knowledge we have of the source. We might consider
the digits of
 to be a random sequence in that we construct a system capable of sending any sequence of
digits. In a similar way we may choose to use some of our statistical knowledge of English in constructing
a code, but not all of it. In such a case we consider the source with the maximum entropy subject to the
statistical conditions we wish to retain. The entropy of this source determines the channel capacity which
is necessary and sufﬁcient. In the
 example the only information retained is that all the digits are chosen
from the set 0;1 ;
:
:
:
;9. In the case of English one might wish to use the statistical saving possible due to
letter frequencies, but nothing else. The maximum entropy source is then the ﬁrst approximation to English
and its entropy determines the required channel capacity.
As a simple example of some of these results consider a source which produces a sequence of letters
chosen from among A, B, C, D with probabilities 1
2, 1
4, 1
8, 1
8, successive symbols being chosen independently.
We have
H
=
1
2 log 1
2
+ 1
4 log 1
4
+ 2
8 log 1
8

= 7
4 bits per symbol
:
Thus we can approximate a coding system to encode messages from this source into binary digits with an
average of 7
4 binary digit per symbol. In this case we can actually achieve the limiting value by the following
code (obtained by the method of the second proof of Theorem 9):
A
0
B
10
C
110
D
111
The average number of binary digits used in encoding a sequence of N symbols will be
N
 1
2
1
+ 1
4
2
+ 2
8
3

= 7
4N
:
It is easily seen that the binary digits 0, 1 have probabilities 1
2, 1
2 so the H for the coded sequences is one
bit per symbol. Since, on the average, we have 7
4 binary symbols per original letter, the entropies on a time
basis are the same. The maximum possible entropy for the original set is log4
= 2, occurring when A, B, C,
D have probabilities 1
4, 1
4, 1
4, 1
4. Hence the relative entropy is 7
8. We can translate the binary sequences into
the original set of symbols on a two-to-one basis by the following table:
00
A
0
01
B
0
10
C
0
11
D
0
18


## PDF page 19

This double process then encodes the original message into the same symbols but with an average compres-
sion ratio 7
8.
As a second example consider a source which produces a sequence of A’s and B’s with probability p for
A and q for B. If p
 q we have
H
=
log pp
(1
 p )1 p
=
plog p (1
 p )
(1 p )=p
:
= plog e
p
:
In such a case one can construct a fairly good coding of the message on a 0, 1 channel by sending a special
sequence, say 0000, for the infrequent symbol A and then a sequence indicating the number of B’s following
it. This could be indicated by the binary representation with all numbers containing the special sequence
deleted. All numbers up to 16 are represented as usual; 16 is represented by the next binary number after 16
which does not contain four zeros, namely 17
= 10001, etc.
It can be shown that as p
! 0 the coding approaches ideal provided the length of the special sequence is
properly adjusted.
PART II: THE DISCRETE CHANNEL WITH NOISE
11. REPRESENTATION OF A NOISY DISCRETE CHANNEL
We now consider the case where the signal is perturbed by noise during transmission or at one or the other
of the terminals. This means that the received signal is not necessarily the same as that sent out by the
transmitter. Two cases may be distinguished. If a particular transmitted signal always produces the same
received signal, i.e., the received signal is a deﬁnite function of the transmitted signal, then the effect may be
called distortion. If this function has an inverse — no two transmitted signals producing the same received
signal — distortion may be corrected, at least in principle, by merely performing the inverse functional
operation on the received signal.
The case of interest here is that in which the signal does not always undergo the same change in trans-
mission. In this case we may assume the received signal E to be a function of the transmitted signal S and a
second variable, the noise N.
E
= f
(S
;N
)
The noise is considered to be a chance variable just as the message was above. In general it may be repre-
sented by a suitable stochastic process. The most general type of noisy discrete channel we shall consider
is a generalization of the ﬁnite state noise-free channel described previously. We assume a ﬁnite number of
states and a set of probabilities
p
;i
(
; j
):
This is the probability, if the channel is in state
 and symbol i is transmitted, that symbol j will be received
and the channel left in state
. Thus
 and
 range over the possible states, i over the possible transmitted
signals and j over the possible received signals. In the case where successive symbols are independently per-
turbed by the noise there is only one state, and the channel is described by the set of transition probabilities
pi
(j
), the probability of transmitted symbol i being received as j.
If a noisy channel is fed by a source there are two statistical processes at work: the source and the noise.
Thus there are a number of entropies that can be calculated. First there is the entropy H
(x) of the source
or of the input to the channel (these will be equal if the transmitter is non-singular). The entropy of the
output of the channel, i.e., the received signal, will be denoted by H
(y). In the noiseless case H
(y)
= H
(x).
The joint entropy of input and output will be H
(xy). Finally there are two conditional entropies Hx
(y) and
Hy
(x), the entropy of the output when the input is known and conversely. Among these quantities we have
the relations
H
(x;y)
= H
(x)
+Hx
(y)
= H
(y)
+Hy
(x):
All of these entropies can be measured on a per-second or a per-symbol basis.
19


## PDF page 20

12. EQUIVOCATION AND CHANNEL CAPACITY
If the channel is noisy it is not in general possible to reconstruct the original message or the transmitted
signal with certainty by any operation on the received signal E. There are, however, ways of transmitting
the information which are optimal in combating noise. This is the problem which we now consider.
Suppose there are two possible symbols 0 and 1, and we are transmitting at a rate of 1000 symbols per
second with probabilities p0
= p1
= 1
2. Thus our source is producing information at the rate of 1000 bits
per second. During transmission the noise introduces errors so that, on the average, 1 in 100 is received
incorrectly (a 0 as 1, or 1 as 0). What is the rate of transmission of information? Certainly less than 1000
bits per second since about 1% of the received symbols are incorrect. Our ﬁrst impulse might be to say
the rate is 990 bits per second, merely subtracting the expected number of errors. This is not satisfactory
since it fails to take into account the recipient’s lack of knowledge of where the errors occur. We may carry
it to an extreme case and suppose the noise so great that the received symbols are entirely independent of
the transmitted symbols. The probability of receiving 1 is 1
2 whatever was transmitted and similarly for 0.
Then about half of the received symbols are correct due to chance alone, and we would be giving the system
credit for transmitting 500 bits per second while actually no information is being transmitted at all. Equally
“good” transmission would be obtained by dispensing with the channel entirely and ﬂipping a coin at the
receiving point.
Evidently the proper correction to apply to the amount of information transmitted is the amount of this
information which is missing in the received signal, or alternatively the uncertainty when we have received
a signal of what was actually sent. From our previous discussion of entropy as a measure of uncertainty it
seems reasonable to use the conditional entropy of the message, knowing the received signal, as a measure
of this missing information. This is indeed the proper deﬁnition, as we shall see later. Following this idea
the rate of actual transmission, R, would be obtained by subtracting from the rate of production (i.e., the
entropy of the source) the average rate of conditional entropy.
R
= H
(x)
Hy
(x)
The conditional entropy Hy
(x) will, for convenience, be called the equivocation. It measures the average
ambiguity of the received signal.
In the example considered above, if a 0 is received the a posteriori probability that a 0 was transmitted
is .99, and that a 1 was transmitted is .01. These ﬁgures are reversed if a 1 is received. Hence
Hy
(x)
=
[:99log
:99
+0 :01log0 :01 ]
=
:081 bits/symbol
or 81 bits per second. We may say that the system is transmitting at a rate 1000
81
= 919 bits per second.
In the extreme case where a 0 is equally likely to be received as a 0 or 1 and similarly for 1, the a posteriori
probabilities are 1
2, 1
2 and
Hy
(x)
=
1
2 log 1
2
+ 1
2 log 1
2

= 1 bit per symbol
or 1000 bits per second. The rate of transmission is then 0 as it should be.
The following theorem gives a direct intuitive interpretation of the equivocation and also serves to justify
it as the unique appropriate measure. We consider a communication system and an observer (or auxiliary
device) who can see both what is sent and what is recovered (with errors due to noise). This observer notes
the errors in the recovered message and transmits data to the receiving point over a “correction channel” to
enable the receiver to correct the errors. The situation is indicated schematically in Fig. 8.
Theorem 10: If the correction channel has a capacity equal to Hy
(x) it is possible to so encode the
correction data as to send it over this channel and correct all but an arbitrarily small fraction
 of the errors.
This is not possible if the channel capacity is less than Hy
(x).
20


## PDF page 21

SOURCE
M
TRANSMITTER
RECEIVER
CORRECTING
DEVICE
OBSERVER
M
0
M
CORRECTION DATA
Fig. 8—Schematic diagram of a correction system.
Roughly then, Hy
(x) is the amount of additional information that must be supplied per second at the
receiving point to correct the received message.
To prove the ﬁrst part, consider long sequences of received message M
0 and corresponding original
message M. There will be logarithmically THy
(x) of the M’s which could reasonably have produced each
M
0. Thus we have THy
(x) binary digits to send each T seconds. This can be done with
 frequency of errors
on a channel of capacity Hy
(x).
The second part can be proved by noting, ﬁrst, that for any discrete chance variables x, y, z
Hy
(x;z)
 Hy
(x):
The left-hand side can be expanded to give
Hy
(z)
+Hyz
(x)
 Hy
(x)
Hyz
(x)
 Hy
(x)
Hy
(z)
 Hy
(x)
H
(z):
If we identify x as the output of the source, y as the received signal and z as the signal sent over the correction
channel, then the right-hand side is the equivocation less the rate of transmission over the correction channel.
If the capacity of this channel is less than the equivocation the right-hand side will be greater than zero and
Hyz
(x)
> 0. But this is the uncertainty of what was sent, knowing both the received signal and the correction
signal. If this is greater than zero the frequency of errors cannot be arbitrarily small.
Example:
Suppose the errors occur at random in a sequence of binary digits: probability p that a digit is wrong
and q
= 1
 p that it is right. These errors can be corrected if their position is known. Thus the
correction channel need only send information as to these positions. This amounts to transmitting
from a source which produces binary digits with probability p for 1 (incorrect) and q for 0 (correct).
This requires a channel of capacity
[plog p
+qlogq ]
which is the equivocation of the original system.
The rate of transmission R can be written in two other forms due to the identities noted above. We have
R
= H
(x)
Hy
(x)
= H
(y)
Hx
(y)
= H
(x)
+H
(y)
H
(x;y):
21


## PDF page 22

The ﬁrst deﬁning expression has already been interpreted as the amount of information sent less the uncer-
tainty of what was sent. The second measures the amount received less the part of this which is due to noise.
The third is the sum of the two amounts less the joint entropy and therefore in a sense is the number of bits
per second common to the two. Thus all three expressions have a certain intuitive signiﬁcance.
The capacity C of a noisy channel should be the maximum possible rate of transmission, i.e., the rate
when the source is properly matched to the channel. We therefore deﬁne the channel capacity by
C
= Max
H
(x)
Hy
(x)

where the maximum is with respect to all possible information sources used as input to the channel. If the
channel is noiseless, Hy
(x)
= 0. The deﬁnition is then equivalent to that already given for a noiseless channel
since the maximum entropy for the channel is its capacity.
13. THE FUNDAMENTAL THEOREM FOR A DISCRETE CHANNEL WITH NOISE
It may seem surprising that we should deﬁne a deﬁnite capacity C for a noisy channel since we can never
send certain information in such a case. It is clear, however, that by sending the information in a redundant
form the probability of errors can be reduced. For example, by repeating the message many times and by a
statistical study of the different received versions of the message the probability of errors could be made very
small. One would expect, however, that to make this probability of errors approach zero, the redundancy
of the encoding must increase indeﬁnitely, and the rate of transmission therefore approach zero. This is by
no means true. If it were, there would not be a very well deﬁned capacity, but only a capacity for a given
frequency of errors, or a given equivocation; the capacity going down as the error requirements are made
more stringent. Actually the capacity C deﬁned above has a very deﬁnite signiﬁcance. It is possible to send
information at the rate C through the channel with as small a frequency of errors or equivocation as desired
by proper encoding. This statement is not true for any rate greater than C. If an attempt is made to transmit
at a higher rate than C, say C
+R1, then there will necessarily be an equivocation equal to or greater than the
excess R1. Nature takes payment by requiring just that much uncertainty, so that we are not actually getting
any more than C through correctly.
The situation is indicated in Fig. 9. The rate of information into the channel is plotted horizontally and
the equivocation vertically. Any point above the heavy line in the shaded region can be attained and those
below cannot. The points on the line cannot in general be attained, but there will usually be two points on
the line that can.
These results are the main justiﬁcation for the deﬁnition of C and will now be proved.
Theorem 11: Let a discrete channel have the capacity C and a discrete source the entropy per second H.
If H
 C there exists a coding system such that the output of the source can be transmitted over the channel
with an arbitrarily small frequency of errors (or an arbitrarily small equivocation). If H
> C it is possible
to encode the source so that the equivocation is less than H
C
+
 where
 is arbitrarily small. There is no
method of encoding which gives an equivocation less than H
C.
The method of proving the ﬁrst part of this theorem is not by exhibiting a coding method having the
desired properties, but by showing that such a code must exist in a certain group of codes. In fact we will
ATTAINABLE
REGION
C
H
(x)
Hy
(x)
SLOPE = 1.0
Fig. 9—The equivocation possible for a given input entropy to a channel.
22


## PDF page 23

average the frequency of errors over this group and show that this average can be made less than
. If the
average of a set of numbers is less than
 there must exist at least one in the set which is less than
. This
will establish the desired result.
The capacity C of a noisy channel has been deﬁned as
C
= Max
H
(x)
Hy
(x)

where x is the input and y the output. The maximization is over all sources which might be used as input to
the channel.
Let S0 be a source which achieves the maximum capacity C. If this maximum is not actually achieved
by any source let S0 be a source which approximates to giving the maximum rate. Suppose S0 is used as
input to the channel. We consider the possible transmitted and received sequences of a long duration T. The
following will be true:
1. The transmitted sequences fall into two classes, a high probability group with about 2TH
(x) members
and the remaining sequences of small total probability.
2. Similarly the received sequences have a high probability set of about 2TH
(y) members and a low
probability set of remaining sequences.
3. Each high probability output could be produced by about 2THy
(x) inputs. The probability of all other
cases has a small total probability.
All the
’s and
’s implied by the words “small” and “about” in these statements approach zero as we
allow T to increase and S0 to approach the maximizing source.
The situation is summarized in Fig. 10 where the input sequences are points on the left and output
sequences points on the right. The fan of cross lines represents the range of possible causes for a typical
output.
M
E
2H
(x)T
HIGH PROBABILITY
MESSAGES
2H
(y)T
HIGH PROBABILITY
RECEIVED SIGNALS
2Hy
(x)T
REASONABLE CAUSES
FOR EACH E
2Hx
(y)T
REASONABLE EFFECTS
FOR EACH M
Fig. 10—Schematic representation of the relations between inputs and outputs in a channel.
Now suppose we have another source producing information at rate R with R
< C. In the period T this
source will have 2TR high probability messages. We wish to associate these with a selection of the possible
channel inputs in such a way as to get a small frequency of errors. We will set up this association in all
23


## PDF page 24

possible ways (using, however, only the high probability group of inputs as determined by the source S0)
and average the frequency of errors for this large class of possible coding systems. This is the same as
calculating the frequency of errors for a random association of the messages and channel inputs of duration
T. Suppose a particular output y1 is observed. What is the probability of more than one message in the set
of possible causes of y1? There are 2TR messages distributed at random in 2TH
(x) points. The probability of
a particular point being a message is thus
2T
(R H
(x))
:
The probability that none of the points in the fan is a message (apart from the actual originating message) is
P
=

1
2T
(R H
(x))
2THy
(x)
:
Now R
< H
(x)
Hy
(x) so R
H
(x)
=
Hy
(x)
 with
 positive. Consequently
P
=

1
2
THy
(x)T

2THy
(x)
approaches (as T
! ∞)
1
2
T

:
Hence the probability of an error approaches zero and the ﬁrst part of the theorem is proved.
The second part of the theorem is easily shown by noting that we could merely send C bits per second
from the source, completely neglecting the remainder of the information generated. At the receiver the
neglected part gives an equivocation H
(x)
C and the part transmitted need only add
. This limit can also
be attained in many other ways, as will be shown when we consider the continuous case.
The last statement of the theorem is a simple consequence of our deﬁnition of C. Suppose we can encode
a source with H
(x)
= C
+a in such a way as to obtain an equivocation Hy
(x)
= a
 with
 positive. Then
R
= H
(x)
= C
+a and
H
(x)
Hy
(x)
= C
+

with
 positive. This contradicts the deﬁnition of C as the maximum of H
(x)
Hy
(x).
Actually more has been proved than was stated in the theorem. If the average of a set of numbers is
within
 of of their maximum, a fraction of at most
p
 can be more than
p
 below the maximum. Since
 is
arbitrarily small we can say that almost all the systems are arbitrarily close to the ideal.
14. DISCUSSION
The demonstration of Theorem 11, while not a pure existence proof, has some of the deﬁciencies of such
proofs. An attempt to obtain a good approximation to ideal coding by following the method of the proof is
generally impractical. In fact, apart from some rather trivial cases and certain limiting situations, no explicit
description of a series of approximation to the ideal has been found. Probably this is no accident but is
related to the difﬁculty of giving an explicit construction for a good approximation to a random sequence.
An approximation to the ideal would have the property that if the signal is altered in a reasonable way
by the noise, the original can still be recovered. In other words the alteration will not in general bring it
closer to another reasonable signal than the original. This is accomplished at the cost of a certain amount of
redundancy in the coding. The redundancy must be introduced in the proper way to combat the particular
noise structure involved. However, any redundancy in the source will usually help if it is utilized at the
receiving point. In particular, if the source already has a certain redundancy and no attempt is made to
eliminate it in matching to the channel, this redundancy will help combat noise. For example, in a noiseless
telegraph channel one could save about 50% in time by proper encoding of the messages. This is not done
and most of the redundancy of English remains in the channel symbols. This has the advantage, however,
of allowing considerable noise in the channel. A sizable fraction of the letters can be received incorrectly
and still reconstructed by the context. In fact this is probably not a bad approximation to the ideal in many
cases, since the statistical structure of English is rather involved and the reasonable English sequences are
not too far (in the sense required for the theorem) from a random selection.
24


