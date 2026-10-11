# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 257

PROBLEMS
231
the symmetry of the random coding argument, this does not
depend on which codeword was sent.
The calculations above show that average probability of error for
a random code with 512 codewords of length 25 over the binary
symmetric channel of crossover probability 0.1 is about 0.34. This
seems quite high, but the reason for this is that the value of ϵ that
we have chosen is too large. By choosing a smaller ϵ and a larger
n in the deﬁnitions of A(n)
ϵ , we can get the probability of error to
be as small as we want as long as the rate of the code is less than
I (X; Y) −3ϵ.
Also note that the decoding procedure described in the problem
is not optimal. The optimal decoding procedure is maximum like-
lihood (i.e., to choose the codeword that is closest to the received
sequence). It is possible to calculate the average probability of
error for a random code for which the decoding is based on an
approximation to maximum likelihood decoding, where we decode
a received sequence to the unique codeword that differs from the
received sequence in ≤4 bits, and declare an error otherwise. The
only difference with the jointly typical decoding described above
is that in the case when the codeword is equal to the received
sequence! The average probability of error for this decoding scheme
can be shown to be about 0.285.
7.16
Encoder and decoder as part of the channel. Consider a binary
symmetric channel with crossover probability 0.1. A possible cod-
ing scheme for this channel with two codewords of length 3 is to
encode message a1 as 000 and a2 as 111. With this coding scheme,
we can consider the combination of encoder, channel, and decoder
as forming a new BSC, with two inputs a1 and a2 and two outputs
a1 and a2.
(a) Calculate the crossover probability of this channel.
(b) What is the capacity of this channel in bits per transmission of
the original channel?
(c) What is the capacity of the original BSC with crossover prob-
ability 0.1?
(d) Prove a general result that for any channel, considering the
encoder, channel, and decoder together as a new channel from
messages to estimated messages will not increase the capacity
in bits per transmission of the original channel.
7.17
Codes of length 3 for a BSC and BEC. In Problem 7.16, the prob-
ability of error was calculated for a code with two codewords of


## PDF page 258

232
CHANNEL CAPACITY
length 3 (000 and 111) sent over a binary symmetric channel with
crossover probability ϵ. For this problem, take ϵ = 0.1.
(a) Find the best code of length 3 with four codewords for this
channel. What is the probability of error for this code? (Note
that all possible received sequences should be mapped onto
possible codewords.)
(b) What is the probability of error if we used all eight possible
sequences of length 3 as codewords?
(c) Now consider a binary erasure channel with erasure probability
0.1. Again, if we used the two-codeword code 000 and 111,
received sequences 00E, 0E0, E00, 0EE, E0E, EE0 would all
be decoded as 0, and similarly, we would decode 11E, 1E1,
E11, 1EE, E1E, EE1 as 1. If we received the sequence EEE,
we would not know if it was a 000 or a 111 that was sent—so
we choose one of these two at random, and are wrong half the
time. What is the probability of error for this code over the
erasure channel?
(d) What is the probability of error for the codes of parts (a) and
(b) when used over the binary erasure channel?
7.18
Channel capacity. Calculate the capacity of the following channels
with probability transition matrices:
(a) X = Y = {0, 1, 2}
p(y|x) =


1
3
1
3
1
3
1
3
1
3
1
3
1
3
1
3
1
3


(7.164)
(b) X = Y = {0, 1, 2}
p(y|x) =


1
2
1
2
0
0
1
2
1
2
1
2
0
1
2


(7.165)
(c) X = Y = {0, 1, 2, 3}
p(y|x) =


p
1 −p
0
0
1 −p
p
0
0
0
0
q
1 −q
0
0
1 −q
q


(7.166)


## PDF page 259

PROBLEMS
233
7.19
Capacity of the carrier pigeon channel. Consider a commander of
an army besieged in a fort for whom the only means of commu-
nication to his allies is a set of carrier pigeons. Assume that each
carrier pigeon can carry one letter (8 bits), that pigeons are released
once every 5 minutes, and that each pigeon takes exactly 3 minutes
to reach its destination.
(a) Assuming that all the pigeons reach safely, what is the capacity
of this link in bits/hour?
(b) Now assume that the enemies try to shoot down the pigeons
and that they manage to hit a fraction α of them. Since the
pigeons are sent at a constant rate, the receiver knows when
the pigeons are missing. What is the capacity of this link?
(c) Now assume that the enemy is more cunning and that every
time they shoot down a pigeon, they send out a dummy pigeon
carrying a random letter (chosen uniformly from all 8-bit let-
ters). What is the capacity of this link in bits/hour?
Set up an appropriate model for the channel in each of the above
cases, and indicate how to go about ﬁnding the capacity.
7.20
Channel with two independent looks at Y. Let Y1 and Y2 be condi-
tionally independent and conditionally identically distributed given
X.
(a) Show that I (X; Y1, Y2) = 2I (X; Y1) −I (Y1, Y2).
(b) Conclude that the capacity of the channel
X
(Y1, Y2)
is less than twice the capacity of the channel
X
Y1
7.21
Tall, fat people. Suppose that the average height of people in a
room is 5 feet. Suppose that the average weight is 100 lb.
(a) Argue that no more than one-third of the population is 15 feet
tall.
(b) Find an upper bound on the fraction of 300-lb 10-footers in
the room.


## PDF page 260

234
CHANNEL CAPACITY
7.22
Can signal alternatives lower capacity? Show that adding a row to
a channel transition matrix does not decrease capacity.
7.23
Binary multiplier channel
(a) Consider the channel Y = XZ, where X and Z are independent
binary random variables that take on values 0 and 1. Z is
Bernoulli(α) [i.e., P (Z = 1) = α]. Find the capacity of this
channel and the maximizing distribution on X.
(b) Now suppose that the receiver can observe Z as well as Y.
What is the capacity?
7.24
Noise alphabets. Consider the channel
Z
Y
X
∑
X = {0, 1, 2, 3}, where Y = X + Z, and Z is uniformly distributed
over three distinct integer values Z = {z1, z2, z3}.
(a) What is the maximum capacity over all choices of the Z alpha-
bet? Give distinct integer values z1, z2, z3 and a distribution on
X achieving this.
(b) What is the minimum capacity over all choices for the Z alpha-
bet? Give distinct integer values z1, z2, z3 and a distribution on
X achieving this.
7.25
Bottleneck channel. Suppose that a signal X ∈X = {1, 2, . . . , m}
goes through an intervening transition X −→V −→Y:
X
V
Y
p(v |x)
p(y |v )
where x = {1, 2, . . . , m}, y = {1, 2, . . . , m}, and v = {1, 2, . . . , k}.
Here p(v|x) and p(y|v) are arbitrary and the channel has transition
probability p(y|x) = 
v p(v|x)p(y|v). Show that C ≤log k.


## PDF page 261

PROBLEMS
235
7.26
Noisy typewriter. Consider the channel with x, y ∈{0, 1, 2, 3} and
transition probabilities p(y|x) given by the following matrix:


1
2
1
2
0
0
0
1
2
1
2
0
0
0
1
2
1
2
1
2
0
0
1
2


(a) Find the capacity of this channel.
(b) Deﬁne the random variable z = g(y), where
g(y) =

A
if y ∈{0, 1}
B
if y ∈{2, 3}.
For the following two PMFs for x, compute I (X; Z):
(i)
p(x) =
 1
2
if x ∈{1, 3}
0
if x ∈{0, 2}.
(ii)
p(x) =
 0
if x ∈{1, 3}
1
2
if x ∈{0, 2}.
(c) Find the capacity of the channel between x and z, speciﬁcally
where x ∈{0, 1, 2, 3}, z ∈{A, B}, and the transition probabil-
ities P (z|x) are given by
p(Z = z|X = x) =

g(y0)=z
P (Y = y0|X = x).
(d) For the X distribution of part (i) of (b), does X →Z →Y
form a Markov chain?
7.27
Erasure channel. Let {X, p(y|x), Y} be a discrete memoryless chan-
nel with capacity C. Suppose that this channel is cascaded imme-
diately with an erasure channel {Y, p(s|y), S} that erases α of its
symbols.
X
p (y | x)
Y
e
S


## PDF page 262

236
CHANNEL CAPACITY
Speciﬁcally, S = {y1, y2, . . . , ym, e}, and
Pr{S = y|X = x} = αp(y|x),
y ∈Y,
Pr{S = e|X = x} = α.
Determine the capacity of this channel.
7.28
Choice of channels. Find the capacity C of the union of two chan-
nels (X1, p1(y1|x1), Y1) and (X2, p2(y2|x2), Y2), where at each
time, one can send a symbol over channel 1 or channel 2 but
not both. Assume that the output alphabets are distinct and do not
intersect.
(a) Show that 2C = 2C1 + 2C2. Thus, 2C is the effective alphabet
size of a channel with capacity C.
(b) Compare with Problem 2.10 where 2H = 2H1 + 2H2, and inter-
pret part (a) in terms of the effective number of noise-free
symbols.
(c) Use the above result to calculate the capacity of the following
channel.
1 −p
1 −p
0
1
0
1
2
2
1
p
p
7.29
Binary multiplier channel
(a) Consider the discrete memoryless channel Y = XZ, where X
and Z are independent binary random variables that take on
values 0 and 1. Let P (Z = 1) = α. Find the capacity of this
channel and the maximizing distribution on X.
(b) Now suppose that the receiver can observe Z as well as Y.
What is the capacity?


## PDF page 263

PROBLEMS
237
7.30
Noise alphabets. Consider the channel
Z
Y
X
∑
X = {0, 1, 2, 3}, where Y = X + Z, and Z is uniformly distributed
over three distinct integer values Z = {z1, z2, z3}.
(a) What is the maximum capacity over all choices of the Z alpha-
bet? Give distinct integer values z1, z2, z3 and a distribution on
X achieving this.
(b) What is the minimum capacity over all choices for the Z alpha-
bet? Give distinct integer values z1, z2, z3 and a distribution on
X achieving this.
7.31
Source and channel. We wish to encode a Bernoulli(α) process
V1, V2, . . . for transmission over a binary symmetric channel with
crossover probability p.
1 −p
Xn (Vn)
Vn
Vn
Y n
1 −p
p
p
^
Find conditions on α and p so that the probability of error P ( ˆV n ̸=
V n) can be made to go to zero as n −→∞.
7.32
Random 20 questions. Let X be uniformly distributed over {1, 2,
. . . , m}. Assume that m = 2n. We ask random questions: Is X ∈S1?
Is X ∈S2? . . . until only one integer remains. All 2m subsets S of
{1, 2, . . . , m} are equally likely.
(a) How many deterministic questions are needed to determine X?
(b) Without loss of generality, suppose that X = 1 is the random
object. What is the probability that object 2 yields the same
answers as object 1 for k questions?
(c) What is the expected number of objects in {2, 3, . . . , m} that
have the same answers to the questions as those of the correct
object 1?


## PDF page 264

238
CHANNEL CAPACITY
(d) Suppose that we ask n + √n random questions. What is the
expected number of wrong objects agreeing with the answers?
(e) Use Markov’s inequality Pr{X ≥tµ} ≤1
t , to show that the
probability of error (one or more wrong object remaining) goes
to zero as n −→∞.
7.33
BSC with feedback. Suppose that feedback is used on a binary
symmetric channel with parameter p. Each time a Y is received,
it becomes the next transmission. Thus, X1 is Bern(1
2), X2 = Y1,
X3 = Y2, . . ., Xn = Yn−1.
(a) Find limn→∞1
nI (Xn; Y n).
(b) Show that for some values of p, this can be higher than capac-
ity.
(c) Using this feedback transmission scheme, Xn(W, Y n) = (X1
(W), Y1, Y2, . . . , Ym−1), what is the asymptotic communication
rate achieved; that is, what is limn→∞1
nI (W; Y n)?
7.34
Capacity. Find the capacity of
(a) Two parallel BSCs:
p
p
1
2
1
2
p
p
3
X
Y
4
3
4
(b) BSC and a single symbol:
p
p
1
2
1
2
3
X
Y
3


