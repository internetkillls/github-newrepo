# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 209

CHAPTER 7
CHANNEL CAPACITY
What do we mean when we say that A communicates with B? We mean
that the physical acts of A have induced a desired physical state in B. This
transfer of information is a physical process and therefore is subject to the
uncontrollable ambient noise and imperfections of the physical signaling
process itself. The communication is successful if the receiver B and the
transmitter A agree on what was sent.
In this chapter we ﬁnd the maximum number of distinguishable signals
for n uses of a communication channel. This number grows exponen-
tially with n, and the exponent is known as the channel capacity. The
characterization of the channel capacity (the logarithm of the number of
distinguishable signals) as the maximum mutual information is the central
and most famous success of information theory.
The mathematical analog of a physical signaling system is shown
in Figure 7.1. Source symbols from some ﬁnite alphabet are mapped
into some sequence of channel symbols, which then produces the out-
put sequence of the channel. The output sequence is random but has a
distribution that depends on the input sequence. From the output sequence,
we attempt to recover the transmitted message.
Each of the possible input sequences induces a probability distribution
on the output sequences. Since two different input sequences may give rise
to the same output sequence, the inputs are confusable. In the next few
sections, we show that we can choose a “nonconfusable” subset of input
sequences so that with high probability there is only one highly likely input
that could have caused the particular output. We can then reconstruct the
input sequences at the output with a negligible probability of error. By
mapping the source into the appropriate “widely spaced” input sequences
to the channel, we can transmit a message with very low probability of
error and reconstruct the source message at the output. The maximum rate
at which this can be done is called the capacity of the channel.
Deﬁnition
We deﬁne a discrete channel to be a system consisting of an
input alphabet X and output alphabet Y and a probability transition matrix
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
183


## PDF page 210

184
CHANNEL CAPACITY
Encoder
Decoder
Channel
p(y|x)
W
Xn
Yn
Message
W
Estimate
of
Message
^
FIGURE 7.1. Communication system.
p(y|x) that expresses the probability of observing the output symbol y
given that we send the symbol x. The channel is said to be memoryless
if the probability distribution of the output depends only on the input at
that time and is conditionally independent of previous channel inputs or
outputs.
Deﬁnition
We deﬁne the “information” channel capacity of a discrete
memoryless channel as
C = max
p(x) I (X; Y),
(7.1)
where the maximum is taken over all possible input distributions p(x).
We shall soon give an operational deﬁnition of channel capacity as the
highest rate in bits per channel use at which information can be sent with
arbitrarily low probability of error. Shannon’s second theorem establishes
that the information channel capacity is equal to the operational channel
capacity. Thus, we drop the word information in most discussions of
channel capacity.
There is a duality between the problems of data compression and data
transmission. During compression, we remove all the redundancy in the
data to form the most compressed version possible, whereas during data
transmission, we add redundancy in a controlled fashion to combat errors
in the channel. In Section 7.13 we show that a general communication
system can be broken into two parts and that the problems of data com-
pression and data transmission can be considered separately.
7.1
EXAMPLES OF CHANNEL CAPACITY
7.1.1
Noiseless Binary Channel
Suppose that we have a channel whose the binary input is reproduced
exactly at the output (Figure 7.2).
In this case, any transmitted bit is received without error. Hence, one
error-free bit can be transmitted per use of the channel, and the capacity is


## PDF page 211

7.1
EXAMPLES OF CHANNEL CAPACITY
185
0
0
1
1
X
Y
FIGURE 7.2. Noiseless binary channel. C = 1 bit.
1 bit. We can also calculate the information capacity C = max I (X; Y) =
1 bit, which is achieved by using p(x) = (1
2, 1
2).
7.1.2
Noisy Channel with Nonoverlapping Outputs
This channel has two possible outputs corresponding to each of the two
inputs (Figure 7.3). The channel appears to be noisy, but really is not.
Even though the output of the channel is a random consequence of the
input, the input can be determined from the output, and hence every trans-
mitted bit can be recovered without error. The capacity of this channel is
also 1 bit per transmission. We can also calculate the information capacity
C = max I (X; Y) = 1 bit, which is achieved by using p(x) = ( 1
2, 1
2).
1/2
1/2
0
2
1
X
Y
1/3
2/3
1
4
3
FIGURE 7.3. Noisy channel with nonoverlapping outputs. C = 1 bit.


## PDF page 212

186
CHANNEL CAPACITY
7.1.3
Noisy Typewriter
In this case the channel input is either received unchanged at the
output with probability
1
2 or is transformed into the next letter with
probability
1
2
(Figure 7.4). If the input has 26 symbols and we
use every alternate input symbol, we can transmit one of 13 sym-
bols without error with each transmission. Hence, the capacity of
this channel is log 13 bits per transmission. We can also calculate
the information capacity C = max I (X; Y) = max (H(Y) −H(Y|X)) =
max H(Y) −1 = log 26 −1 = log 13, achieved by using p(x) distributed
uniformly over all the inputs.
Noisy channel
A
B
A
A
B
C
D
C
C
D
E
A
B
C
D
E
Y
Z
Y
Z
Z
Noiseless subset of inputs
FIGURE 7.4. Noisy Typewriter. C = log 13 bits.


## PDF page 213

7.1
EXAMPLES OF CHANNEL CAPACITY
187
7.1.4
Binary Symmetric Channel
Consider the binary symmetric channel (BSC), which is shown in Fig. 7.5.
This is a binary channel in which the input symbols are complemented
with probability p. This is the simplest model of a channel with errors,
yet it captures most of the complexity of the general problem.
When an error occurs, a 0 is received as a 1, and vice versa. The bits
received do not reveal where the errors have occurred. In a sense, all
the bits received are unreliable. Later we show that we can still use such
a communication channel to send information at a nonzero rate with an
arbitrarily small probability of error.
We bound the mutual information by
I (X; Y) = H(Y) −H(Y|X)
(7.2)
= H(Y) −

p(x)H(Y|X = x)
(7.3)
= H(Y) −

p(x)H(p)
(7.4)
= H(Y) −H(p)
(7.5)
≤1 −H(p),
(7.6)
where the last inequality follows because Y is a binary random variable.
Equality is achieved when the input distribution is uniform. Hence, the
information capacity of a binary symmetric channel with parameter p is
C = 1 −H(p)
bits.
(7.7)
1 −p
1 −p
p
p
0
1
0
1
FIGURE 7.5. Binary symmetric channel. C = 1 −H(p) bits.


## PDF page 214

188
CHANNEL CAPACITY
7.1.5
Binary Erasure Channel
The analog of the binary symmetric channel in which some bits are lost
(rather than corrupted) is the binary erasure channel. In this channel, a
fraction α of the bits are erased. The receiver knows which bits have
been erased. The binary erasure channel has two inputs and three outputs
(Figure 7.6).
We calculate the capacity of the binary erasure channel as follows:
C = max
p(x) I (X; Y)
(7.8)
= max
p(x) (H(Y) −H(Y|X))
(7.9)
= max
p(x) H(Y) −H(α).
(7.10)
The ﬁrst guess for the maximum of H(Y) would be log 3, but we cannot
achieve this by any choice of input distribution p(x). Letting E be the
event {Y = e}, using the expansion
H(Y) = H(Y, E) = H(E) + H(Y|E),
(7.11)
and letting Pr(X = 1) = π, we have
H(Y) = H((1 −π)(1 −α), α, π(1 −α)) = H(α) + (1 −α)H(π).
(7.12)
1 −a
1 −a
0
e
a
a
0
1
1
FIGURE 7.6. Binary erasure channel.


## PDF page 215

7.2
SYMMETRIC CHANNELS
189
Hence
C = max
p(x) H(Y) −H(α)
(7.13)
= max
π (1 −α)H(π) + H(α) −H(α)
(7.14)
= max
π (1 −α)H(π)
(7.15)
= 1 −α,
(7.16)
where capacity is achieved by π = 1
2.
The expression for the capacity has some intuitive meaning: Since a
proportion α of the bits are lost in the channel, we can recover (at most)
a proportion 1 −α of the bits. Hence the capacity is at most 1 −α. It is
not immediately obvious that it is possible to achieve this rate. This will
follow from Shannon’s second theorem.
In many practical channels, the sender receives some feedback from
the receiver. If feedback is available for the binary erasure channel, it is
very clear what to do: If a bit is lost, retransmit it until it gets through.
Since the bits get through with probability 1 −α, the effective rate of
transmission is 1 −α. In this way we are easily able to achieve a capacity
of 1 −α with feedback.
Later in the chapter we prove that the rate 1 −α is the best that can be
achieved both with and without feedback. This is one of the consequences
of the surprising fact that feedback does not increase the capacity of
discrete memoryless channels.
7.2
SYMMETRIC CHANNELS
The capacity of the binary symmetric channel is C = 1 −H(p) bits per
transmission, and the capacity of the binary erasure channel is C = 1 −
α bits per transmission. Now consider the channel with transition matrix:
p(y|x) =


0.3
0.2
0.5
0.5
0.3
0.2
0.2
0.5
0.3

.
(7.17)
Here the entry in the xth row and the yth column denotes the conditional
probability p(y|x) that y is received when x is sent. In this channel, all
the rows of the probability transition matrix are permutations of each other
and so are the columns. Such a channel is said to be symmetric. Another
example of a symmetric channel is one of the form
Y = X + Z
(mod c),
(7.18)


## PDF page 216

190
CHANNEL CAPACITY
where Z has some distribution on the integers {0, 1, 2, . . . , c −1}, X has
the same alphabet as Z, and Z is independent of X.
In both these cases, we can easily ﬁnd an explicit expression for the
capacity of the channel. Letting r be a row of the transition matrix, we
have
I (X; Y) = H(Y) −H(Y|X)
(7.19)
= H(Y) −H(r)
(7.20)
≤log |Y| −H(r)
(7.21)
with equality if the output distribution is uniform. But p(x) = 1/|X|
achieves a uniform distribution on Y, as seen from
p(y) =

x∈X
p(y|x)p(x) = 1
|X|

p(y|x) = c 1
|X| = 1
|Y|,
(7.22)
where c is the sum of the entries in one column of the probability transition
matrix.
Thus, the channel in (7.17) has the capacity
C = max
p(x) I (X; Y) = log 3 −H(0.5, 0.3, 0.2),
(7.23)
and C is achieved by a uniform distribution on the input.
The transition matrix of the symmetric channel deﬁned above is doubly
stochastic. In the computation of the capacity, we used the facts that the
rows were permutations of one another and that all the column sums were
equal.
Considering these properties, we can deﬁne a generalization of the
concept of a symmetric channel as follows:
Deﬁnition
A channel is said to be symmetric if the rows of the channel
transition matrix p(y|x) are permutations of each other and the columns
are permutations of each other. A channel is said to be weakly symmetric
if every row of the transition matrix p(·|x) is a permutation of every other
row and all the column sums 
x p(y|x) are equal.
For example, the channel with transition matrix
p(y|x) =
 1
3
1
6
1
2
1
3
1
2
1
6

(7.24)
is weakly symmetric but not symmetric.


