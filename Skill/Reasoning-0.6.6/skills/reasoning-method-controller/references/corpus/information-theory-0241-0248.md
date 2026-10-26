# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 241

7.11
HAMMING CODES
215
decoding algorithms for these codes. With the advent of integrated circuits,
it has become feasible to implement fairly complex codes in hardware and
realize some of the error-correcting performance promised by Shannon’s
channel capacity theorem. For example, all compact disc players include
error-correction circuitry based on two interleaved (32, 28, 5) and (28, 24,
5) Reed–Solomon codes that allow the decoder to correct bursts of up to
4000 errors.
All the codes described above are block codes —they map a block of
information bits onto a channel codeword and there is no dependence on
past information bits. It is also possible to design codes where each output
block depends not only on the current input block, but also on some of
the past inputs as well. A highly structured form of such a code is called
a convolutional code. The theory of convolutional codes has developed
considerably over the last 40 years. We will not go into the details, but
refer the interested reader to textbooks on coding theory [69, 356].
For many years, none of the known coding algorithms came close
to achieving the promise of Shannon’s channel capacity theorem. For a
binary symmetric channel with crossover probability p, we would need a
code that could correct up to np errors in a block of length n and have
n(1 −H(p)) information bits. For example, the repetition code suggested
earlier corrects up to n/2 errors in a block of length n, but its rate goes
to 0 with n. Until 1972, all known codes that could correct nα errors for
block length n had asymptotic rate 0. In 1972, Justesen [301] described
a class of codes with positive asymptotic rate and positive asymptotic
minimum distance as a fraction of the block length.
In 1993, a paper by Berrou et al. [57] introduced the notion that the
combination of two interleaved convolution codes with a parallel cooper-
ative decoder achieved much better performance than any of the earlier
codes. Each decoder feeds its “opinion” of the value of each bit to the
other decoder and uses the opinion of the other decoder to help it decide
the value of the bit. This iterative process is repeated until both decoders
agree on the value of the bit. The surprising fact is that this iterative
procedure allows for efﬁcient decoding at rates close to capacity for a
variety of channels. There has also been a renewed interest in the theory
of low-density parity check (LDPC) codes that were introduced by Robert
Gallager in his thesis [231, 232]. In 1997, MacKay and Neal [368] showed
that an iterative message-passing algorithm similar to the algorithm used
for decoding turbo codes could achieve rates close to capacity with high
probability for LDPC codes. Both Turbo codes and LDPC codes remain
active areas of research and have been applied to wireless and satellite
communication channels.


## PDF page 242

216
CHANNEL CAPACITY
Encoder
Decoder
Channel
p(y|x)
W
Xi(W,Yi −1)
Yi
Message
W
Estimate
of
Message
^
FIGURE 7.13. Discrete memoryless channel with feedback.
7.12
FEEDBACK CAPACITY
A channel with feedback is illustrated in Figure 7.13. We assume that
all the received symbols are sent back immediately and noiselessly to
the transmitter, which can then use them to decide which symbol to send
next. Can we do better with feedback? The surprising answer is no, which
we shall now prove. We deﬁne a (2nR, n) feedback code as a sequence
of mappings xi(W, Y i−1), where each xi is a function only of the mes-
sage W ∈2nR and the previous received values, Y1, Y2, . . . , Yi−1, and a
sequence of decoding functions g : Yn →{1, 2, . . . , 2nR}. Thus,
P (n)
e
= Pr

g(Y n) ̸= W

,
(7.119)
when W is uniformly distributed over {1, 2, . . . , 2nR}.
Deﬁnition
The capacity with feedback, CFB, of a discrete memoryless
channel is the supremum of all rates achievable by feedback codes.
Theorem 7.12.1
(Feedback capacity)
CFB = C = max
p(x) I (X; Y).
(7.120)
Proof:
Since a nonfeedback code is a special case of a feedback code,
any rate that can be achieved without feedback can be achieved with
feedback, and hence
CFB ≥C.
(7.121)
Proving the inequality the other way is slightly more tricky. We cannot
use the same proof that we used for the converse to the coding theorem
without feedback. Lemma 7.9.2 is no longer true, since Xi depends on
the past received symbols, and it is no longer true that Yi depends only
on Xi and is conditionally independent of the future X’s in (7.93).


## PDF page 243

7.12
FEEDBACK CAPACITY
217
There is a simple change that will ﬁx the problem with the proof.
Instead of using Xn, we will use the index W and prove a similar series
of inequalities. Let W be uniformly distributed over {1, 2, . . . , 2nR}. Then
Pr(W ̸= ˆW) = P (n)
e
and
nR = H(W) = H(W| ˆW) + I (W; ˆW)
(7.122)
≤1 + P (n)
e
nR + I (W; ˆW)
(7.123)
≤1 + P (n)
e
nR + I (W; Y n),
(7.124)
by Fano’s inequality and the data-processing inequality. Now we can
bound I (W; Y n) as follows:
I (W; Y n) = H(Y n) −H(Y n|W)
(7.125)
= H(Y n) −
n

i=1
H(Yi|Y1, Y2, . . . , Yi−1, W)
(7.126)
= H(Y n) −
n

i=1
H(Yi|Y1, Y2, . . . , Yi−1, W, Xi)
(7.127)
= H(Y n) −
n

i=1
H(Yi|Xi),
(7.128)
since Xi is a function of Y1, . . . , Yi−1 and W; and conditional on Xi, Yi
is independent of W and past samples of Y. Continuing, we have
I (W; Y n) = H(Y n) −
n

i=1
H(Yi|Xi)
(7.129)
≤
n

i=1
H(Yi) −
n

i=1
H(Yi|Xi)
(7.130)
=
n

i=1
I (Xi; Yi)
(7.131)
≤nC
(7.132)
from the deﬁnition of capacity for a discrete memoryless channel. Putting
these together, we obtain
nR ≤P (n)
e
nR + 1 + nC,
(7.133)


## PDF page 244

218
CHANNEL CAPACITY
and dividing by n and letting n →∞, we conclude that
R ≤C.
(7.134)
Thus, we cannot achieve any higher rates with feedback than we can
without feedback, and
CFB = C.
□
(7.135)
As we have seen in the example of the binary erasure channel, feedback
can help enormously in simplifying encoding and decoding. However, it
cannot increase the capacity of the channel.
7.13
SOURCE–CHANNEL SEPARATION THEOREM
It is now time to combine the two main results that we have proved so far:
data compression (R > H: Theorem 5.4.2) and data transmission (R <
C: Theorem 7.7.1). Is the condition H < C necessary and sufﬁcient for
sending a source over a channel? For example, consider sending digitized
speech or music over a discrete memoryless channel. We could design
a code to map the sequence of speech samples directly into the input
of the channel, or we could compress the speech into its most efﬁcient
representation, then use the appropriate channel code to send it over the
channel. It is not immediately clear that we are not losing something
by using the two-stage method, since data compression does not depend
on the channel and the channel coding does not depend on the source
distribution.
We will prove in this section that the two-stage method is as good as
any other method of transmitting information over a noisy channel. This
result has some important practical implications. It implies that we can
consider the design of a communication system as a combination of two
parts, source coding and channel coding. We can design source codes
for the most efﬁcient representation of the data. We can, separately and
independently, design channel codes appropriate for the channel. The com-
bination will be as efﬁcient as anything we could design by considering
both problems together.
The common representation for all kinds of data uses a binary alphabet.
Most modern communication systems are digital, and data are reduced
to a binary representation for transmission over the common channel.
This offers an enormous reduction in complexity. Networks like, ATM
networks and the Internet use the common binary representation to allow
speech, video, and digital data to use the same communication channel.


## PDF page 245

7.13
SOURCE–CHANNEL SEPARATION THEOREM
219
The result—that a two-stage process is as good as any one-stage pro-
cess—seems so obvious that it may be appropriate to point out that it
is not always true. There are examples of multiuser channels where the
decomposition breaks down. We also consider two simple situations where
the theorem appears to be misleading. A simple example is that of sending
English text over an erasure channel. We can look for the most efﬁcient
binary representation of the text and send it over the channel. But the
errors will be very difﬁcult to decode. If, however, we send the English
text directly over the channel, we can lose up to about half the letters and
yet be able to make sense out of the message. Similarly, the human ear has
some unusual properties that enable it to distinguish speech under very
high noise levels if the noise is white. In such cases, it may be appropriate
to send the uncompressed speech over the noisy channel rather than the
compressed version. Apparently, the redundancy in the source is suited to
the channel.
Let us deﬁne the setup under consideration. We have a source V that
generates symbols from an alphabet V. We will not make any assumptions
about the kind of stochastic process produced by V other than that it is
from a ﬁnite alphabet and satisﬁes the AEP. Examples of such processes
include a sequence of i.i.d. random variables and the sequence of states
of a stationary irreducible Markov chain. Any stationary ergodic source
satisﬁes the AEP, as we show in Section 16.8.
We want to send the sequence of symbols V n = V1, V2, . . . , Vn over
the channel so that the receiver can reconstruct the sequence. To do this,
we map the sequence onto a codeword Xn(V n) and send the codeword
over the channel. The receiver looks at his received sequence Y n and
makes an estimate ˆV n of the sequence V n that was sent. The receiver
makes an error if V n ̸= ˆV n. We deﬁne the probability of error as
Pr(V n ̸= ˆV n) =

yn

vn
p(vn)p(yn|xn(vn))I (g(yn) ̸= vn),
(7.136)
where I is the indicator function and g(yn) is the decoding function. The
system is illustrated in Figure 7.14.
We can now state the joint source–channel coding theorem:
Encoder
Decoder
Channel
p(y|x)
Vn
Xn(Vn)
Yn
Vn
^
FIGURE 7.14. Joint source and channel coding.


## PDF page 246

220
CHANNEL CAPACITY
Theorem 7.13.1
(Source–channel coding theorem)
If V1, V2, . . . V n
is a ﬁnite alphabet stochastic process that satisﬁes the AEP and H(V) <
C, there exists a source–channel code with probability of error Pr( ˆV n ̸=
V n) →0. Conversely, for any stationary stochastic process, if H(V) > C,
the probability of error is bounded away from zero, and it is not possible
to send the process over the channel with arbitrarily low probability of
error.
Proof:
Achievability. The essence of the forward part of the proof is
the two-stage encoding described earlier. Since we have assumed that the
stochastic process satisﬁes the AEP, it implies that there exists a typical
set A(n)
ϵ
of size ≤2n(H(V)+ϵ) which contains most of the probability. We
will encode only the source sequences belonging to the typical set; all
other sequences will result in an error. This will contribute at most ϵ to
the probability of error.
We index all the sequences belonging to A(n)
ϵ . Since there are at most
2n(H+ϵ) such sequences, n(H + ϵ) bits sufﬁce to index them. We can
transmit the desired index to the receiver with probability of error less
than ϵ if
H(V) + ϵ = R < C.
(7.137)
The receiver can reconstruct V n by enumerating the typical set A(n)
ϵ
and choosing the sequence corresponding to the estimated index. This
sequence will agree with the transmitted sequence with high probability.
To be precise,
P (V n ̸= ˆV n) ≤P (V n /∈A(n)
ϵ ) + P (g(Y n) ̸= V n|V n ∈A(n)
ϵ )
(7.138)
≤ϵ + ϵ = 2ϵ
(7.139)
for n sufﬁciently large. Hence, we can reconstruct the sequence with low
probability of error for n sufﬁciently large if
H(V) < C.
(7.140)
Converse: We wish to show that Pr( ˆV n ̸= V n) →0 implies that H(V)
≤C for any sequence of source-channel codes
Xn(V n) : Vn →Xn,
(7.141)
gn(Y n) : Yn →Vn.
(7.142)


## PDF page 247

7.13
SOURCE–CHANNEL SEPARATION THEOREM
221
Thus Xn(·) is an arbitrary (perhaps random) assignment of codewords
to data sequences V n, and gn(·) is any decoding function (assignment of
estimates ˆV n to output sequences Y n. By Fano’s inequality, we must have
H(V n| ˆV n) ≤1 + Pr( ˆV n ̸= V n) log |Vn| = 1 + Pr( ˆV n ̸= V n)n log |V|.
(7.143)
Hence for the code,
H(V)
(a)
≤H(V1, V2, . . . , Vn)
n
(7.144)
= H(V n)
n
(7.145)
= 1
nH(V n| ˆV n) + 1
nI (V n; ˆV n)
(7.146)
(b)
≤1
n(1 + Pr( ˆV n ̸= V n)n log |V|) + 1
nI (V n; ˆV n)
(7.147)
(c)
≤1
n(1 + Pr( ˆV n ̸= V n)n log |V|) + 1
nI (Xn; Y n)
(7.148)
(d)
≤1
n + Pr( ˆV n ̸= V n) log |V| + C,
(7.149)
where (a) follows from the deﬁnition of entropy rate of a stationary
process, (b) follows from Fano’s inequality, (c) follows from the data-
processing inequality (since V n →Xn →Y n →ˆV n forms a Markov
chain) and (d) follows from the memorylessness of the channel. Now
letting n →∞, we have Pr( ˆV n ̸= V n) →0 and hence
H(V) ≤C.
(7.150)
□
Hence, we can transmit a stationary ergodic source over a channel if and
only if its entropy rate is less than the capacity of the channel. The joint
source–channel separation theorem enables us to consider the problem of
source coding separately from the problem of channel coding. The source
coder tries to ﬁnd the most efﬁcient representation of the source, and
the channel coder encodes the message to combat the noise and errors
introduced by the channel. The separation theorem says that the separate
encoders (Figure 7.15) can achieve the same rates as the joint encoder
(Figure 7.14).
With this result, we have tied together the two basic theorems of
information theory: data compression and data transmission. We will try
to summarize the proofs of the two results in a few words. The data


## PDF page 248

222
CHANNEL CAPACITY
Source
Encoder
Source
Decoder
Channel
Encoder
Channel
Decoder
Channel
p(y|x)
Vn
Xn(Vn)
Yn
V n
^
FIGURE 7.15. Separate source and channel coding.
compression theorem is a consequence of the AEP, which shows that
there exists a “small” subset (of size 2nH) of all possible source sequences
that contain most of the probability and that we can therefore represent
the source with a small probability of error using H bits per symbol.
The data transmission theorem is based on the joint AEP; it uses the
fact that for long block lengths, the output sequence of the channel is
very likely to be jointly typical with the input codeword, while any other
codeword is jointly typical with probability ≈2−nI. Hence, we can use
about 2nI codewords and still have negligible probability of error. The
source–channel separation theorem shows that we can design the source
code and the channel code separately and combine the results to achieve
optimal performance.
SUMMARY
Channel capacity. The logarithm of the number of distinguishable
inputs is given by
C = max
p(x) I (X; Y).
Examples
• Binary symmetric channel: C = 1 −H(p).
• Binary erasure channel: C = 1 −α.
• Symmetric channel: C = log |Y| −H(row of transition matrix).
Properties of C
1. 0 ≤C ≤min{log |X|, log |Y|}.
2. I (X; Y) is a continuous concave function of p(x).
Joint typicality. The set A(n)
ϵ
of jointly typical sequences {(xn, yn)}
with respect to the distribution p(x, y) is given by
A(n)
ϵ
=

(xn, yn) ∈Xn × Yn :
(7.151)
−1
n log p(xn) −H(X)
 < ϵ,
(7.152)


