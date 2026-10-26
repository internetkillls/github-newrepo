# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 249

PROBLEMS
223
−1
n log p(yn) −H(Y)
 < ϵ,
(7.153)
−1
n log p(xn, yn) −H(X, Y)
 < ϵ

,
(7.154)
where p(xn, yn) = n
i=1 p(xi, yi).
Joint AEP. Let (Xn, Y n) be sequences of length n drawn i.i.d. accord-
ing to p(xn, yn) = n
i=1 p(xi, yi). Then:
1. Pr((Xn, Y n) ∈A(n)
ϵ ) →1 as n →∞.
2. |A(n)
ϵ | ≤2n(H(X,Y)+ϵ).
3. If ( ˜Xn, ˜Y n) ∼p(xn)p(yn), then Pr

( ˜Xn, ˜Y n) ∈A(n)
ϵ

≤2−n(I(X;Y)−3ϵ).
Channel coding theorem. All rates below capacity C are achievable,
and all rates above capacity are not; that is, for all rates R < C, there
exists a sequence of (2nR, n) codes with probability of error λ(n) →0.
Conversely, for rates R > C,
λ(n) is bounded away from 0.
Feedback capacity. Feedback does not increase capacity for discrete
memoryless channels (i.e., CFB = C).
Source–channel theorem. A stochastic process with entropy rate H
cannot be sent reliably over a discrete memoryless channel if H >
C. Conversely, if the process satisﬁes the AEP, the source can be
transmitted reliably if H < C.
PROBLEMS
7.1
Preprocessing the output. One is given a communication chan-
nel with transition probabilities p(y|x) and channel capacity C =
maxp(x) I (X; Y). A helpful statistician preprocesses the output by
forming ˜Y = g(Y). He claims that this will strictly improve the
capacity.
(a) Show that he is wrong.
(b) Under what conditions does he not strictly decrease the
capacity?


## PDF page 250

224
CHANNEL CAPACITY
7.2
Additive noise channel. Find the channel capacity of the following
discrete memoryless channel:
Z
Y
X
where Pr{Z = 0} = Pr{Z = a} = 1
2. The alphabet for x is X =
{0, 1}. Assume that Z is independent of X. Observe that the channel
capacity depends on the value of a.
7.3
Channels with memory have higher capacity. Consider a binary
symmetric channel with Yi = Xi ⊕Zi, where ⊕is mod 2 addi-
tion, and Xi, Yi ∈{0, 1}. Suppose that {Zi} has constant marginal
probabilities Pr{Zi = 1} = p = 1 −Pr{Zi = 0}, but that Z1, Z2,
. . ., Zn are not necessarily independent. Assume that Zn is inde-
pendent of the input Xn. Let C = 1 −H(p, 1 −p). Show that
maxp(x1,x2,...,xn) I (X1, X2, . . . , Xn; Y1, Y2, . . . ,
Yn) ≥nC.
7.4
Channel capacity. Consider the discrete memoryless channel Y =
X + Z (mod 11), where
Z =
 1,
2,
3
1
3,
1
3,
1
3

and X ∈{0, 1, . . . , 10}. Assume that Z is independent of X.
(a) Find the capacity.
(b) What is the maximizing p∗(x)?
7.5
Using two channels at once. Consider two discrete memoryless
channels (X1, p(y1 | x1), Y1) and (X2, p(y2 | x2), Y2) with capac-
ities C1 and C2, respectively. A new channel (X1 × X2, p(y1 |
x1) × p(y2 | x2), Y1 × Y2) is formed in which x1 ∈X1 and x2 ∈X2
are sent simultaneously, resulting in y1, y2. Find the capacity of this
channel.
7.6
Noisy typewriter. Consider a 26-key typewriter.
(a) If pushing a key results in printing the associated letter, what
is the capacity C in bits?


## PDF page 251

PROBLEMS
225
(b) Now suppose that pushing a key results in printing that letter or
the next (with equal probability). Thus, A →A or B, . . . , Z →
Z or A. What is the capacity?
(c) What is the highest rate code with block length one that you
can ﬁnd that achieves zero probability of error for the channel
in part (b)?
7.7
Cascade of binary symmetric channels. Show that a cascade of n
identical independent binary symmetric channels,
X0 →BSC →X1 →· · · →Xn−1 →BSC →Xn,
each with raw error probability p, is equivalent to a single BSC with
error probability 1
2

1 −(1 −2p)n
and hence that lim
n→∞I (X0; Xn)
= 0 if p ̸= 0, 1. No encoding or decoding takes place at the inter-
mediate terminals X1, . . . , Xn−1. Thus, the capacity of the cascade
tends to zero.
7.8
Z-channel. The Z-channel has binary input and output alphabets
and transition probabilities p(y|x) given by the following matrix:
Q =

1
0
1/2
1/2

x, y ∈{0, 1}
Find the capacity of the Z-channel and the maximizing input prob-
ability distribution.
7.9
Suboptimal codes. For the Z-channel of Problem 7.8, assume that
we choose a (2nR, n) code at random, where each codeword is a
sequence of fair coin tosses. This will not achieve capacity. Find the
maximum rate R such that the probability of error P (n)
e
, averaged
over the randomly generated codes, tends to zero as the block length
n tends to inﬁnity.
7.10
Zero-error capacity. A channel with alphabet {0, 1, 2, 3, 4} has tran-
sition probabilities of the form
p(y|x) =

1/2
if y = x ± 1 mod 5
0
otherwise.
(a) Compute the capacity of this channel in bits.


## PDF page 252

226
CHANNEL CAPACITY
(b) The zero-error capacity of a channel is the number of bits per
channel use that can be transmitted with zero probability of
error. Clearly, the zero-error capacity of this pentagonal chan-
nel is at least 1 bit (transmit 0 or 1 with probability 1/2). Find
a block code that shows that the zero-error capacity is greater
than 1 bit. Can you estimate the exact value of the zero-error
capacity? (Hint: Consider codes of length 2 for this channel.)
The zero-error capacity of this channel was ﬁnally found by
Lovasz [365].
7.11
Time-varying channels. Consider a time-varying discrete memory-
less channel.
Let Y1, Y2, . . . , Yn be conditionally independent given X1, X2,
. . . , Xn, with conditional distribution given by p(y | x) = n
i=1
pi(yi | xi). Let X = (X1, X2, . . . , Xn), Y = (Y1, Y2, . . . , Yn). Find
maxp(x) I (X; Y).
1 −pi
1 −pi
0
1
0
1
pi
pi
7.12
Unused symbols. Show that the capacity of the channel with prob-
ability transition matrix
Py|x =


2
3
1
3
0
1
3
1
3
1
3
0
1
3
2
3


(7.155)
is achieved by a distribution that places zero probability on one
of input symbols. What is the capacity of this channel? Give an
intuitive reason why that letter is not used.
7.13
Erasures and errors in a binary channel. Consider a channel with
binary inputs that has both erasures and errors. Let the probability


## PDF page 253

PROBLEMS
227
of error be ϵ and the probability of erasure be α, so the channel is
follows:
0
1 −a −
0
1
1
e
∋
1 −a −
∋
∋
∋
a
a
(a) Find the capacity of this channel.
(b) Specialize to the case of the binary symmetric channel (α = 0).
(c) Specialize to the case of the binary erasure channel (ϵ = 0).
7.14
Channels with dependence between the letters. Consider the fol-
lowing channel over a binary alphabet that takes in 2-bit symbols
and produces a 2-bit output, as determined by the following map-
ping: 00 →01, 01 →10, 10 →11, and 11 →00. Thus, if the
2-bit sequence 01 is the input to the channel, the output is 10 with
probability 1. Let X1, X2 denote the two input symbols and Y1, Y2
denote the corresponding output symbols.
(a) Calculate the mutual information I (X1, X2; Y1, Y2) as a func-
tion of the input distribution on the four possible pairs of inputs.
(b) Show that the capacity of a pair of transmissions on this chan-
nel is 2 bits.
(c) Show that under the maximizing input distribution, I (X1; Y1)
= 0. Thus, the distribution on the input sequences that achieves
capacity does not necessarily maximize the mutual information
between individual symbols and their corresponding outputs.
7.15
Jointly typical sequences. As we did in Problem 3.13 for the typical
set for a single random variable, we will calculate the jointly typical
set for a pair of random variables connected by a binary symmetric


## PDF page 254

228
CHANNEL CAPACITY
channel, and the probability of error for jointly typical decoding
for such a channel.
0.9
0.9
0
1
0
1
0.1
0.1
We consider a binary symmetric channel with crossover probability
0.1. The input distribution that achieves capacity is the uniform
distribution [i.e., p(x) = ( 1
2, 1
2)], which yields the joint distribution
p(x, y) for this channel is given by
X Y
0
1
0
0.45
0.05
1
0.05
0.45
The marginal distribution of Y is also ( 1
2, 1
2).
(a) Calculate H(X), H(Y), H(X, Y), and I (X; Y) for the joint
distribution above.
(b) Let X1, X2, . . . , Xn be drawn i.i.d. according the Bernoulli(1
2)
distribution. Of the 2n possible input sequences of length n,
which of them are typical [i.e., member of A(n)
ϵ (X) for ϵ =
0.2]? Which are the typical sequences in A(n)
ϵ (Y)?
(c) The jointly typical set A(n)
ϵ (X, Y) is deﬁned as the set of
sequences that satisfy equations (7.35-7.37). The ﬁrst two
equations correspond to the conditions that xn and yn are in
A(n)
ϵ (X) and A(n)
ϵ (Y), respectively. Consider the last condi-
tion, which can be rewritten to state that −1
n log p(xn, yn) ∈
(H(X, Y) −ϵ, H(X, Y) + ϵ). Let k be the number of places
in which the sequence xn differs from yn (k is a function of
the two sequences). Then we can write
p(xn, yn) =
n
	
i=1
p(xi, yi)
(7.156)


## PDF page 255

PROBLEMS
229
= (0.45)n−k(0.05)k
(7.157)
=
1
2
n
(1 −p)n−kpk.
(7.158)
An alternative way at looking at this probability is to look at the
binary symmetric channel as in additive channel Y = X ⊕Z,
where Z is a binary random variable that is equal to 1 with
probability p, and is independent of X. In this case,
p(xn, yn) = p(xn)p(yn|xn)
(7.159)
= p(xn)p(zn|xn)
(7.160)
= p(xn)p(zn)
(7.161)
=
1
2
n
(1 −p)n−kpk.
(7.162)
Show that the condition that (xn, yn) being jointly typical is
equivalent to the condition that xn is typical and zn = yn −xn
is typical.
(d) We now calculate the size of A(n)
ϵ (Z) for n = 25 and ϵ = 0.2.
As in Problem 3.13, here is a table of the probabilities and
numbers of sequences with k ones:
k
n
k

n
k

pk(1 −p)n−k
−1
n log p(xn)
0
1
0.071790
0.152003
1
25
0.199416
0.278800
2
300
0.265888
0.405597
3
2300
0.226497
0.532394
4
12650
0.138415
0.659191
5
53130
0.064594
0.785988
6
177100
0.023924
0.912785
7
480700
0.007215
1.039582
8
1081575
0.001804
1.166379
9
2042975
0.000379
1.293176
10
3268760
0.000067
1.419973
11
4457400
0.000010
1.546770
12
5200300
0.000001
1.673567
[Sequences with more than 12 ones are omitted since their total
probability is negligible (and they are not in the typical set).]
What is the size of the set A(n)
ϵ (Z)?


## PDF page 256

230
CHANNEL CAPACITY
(e) Now consider random coding for the channel, as in the proof
of the channel coding theorem. Assume that 2nR codewords
Xn(1), Xn(2),. . ., Xn(2nR) are chosen uniformly over the 2n
possible binary sequences of length n. One of these codewords
is chosen and sent over the channel. The receiver looks at
the received sequence and tries to ﬁnd a codeword in the
code that is jointly typical with the received sequence. As
argued above, this corresponds to ﬁnding a codeword Xn(i)
such that Y n −Xn(i) ∈A(n)
ϵ (Z). For a ﬁxed codeword xn(i),
what is the probability that the received sequence Y n is such
that (xn(i), Y n) is jointly typical?
(f) Now
consider
a
particular
received
sequence
yn =
000000 . . . 0,
say.
Assume
that
we
choose
a
sequence
Xn at random, uniformly distributed among all the 2n possible
binary n-sequences. What is the probability that the chosen
sequence is jointly typical with this yn? [Hint: This is the
probability of all sequences xn such that yn −xn ∈A(n)
ϵ (Z).]
(g) Now consider a code with 29 = 512 codewords of length 12
chosen at random, uniformly distributed among all the 2n
sequences of length n = 25. One of these codewords, say
the one corresponding to i = 1, is chosen and sent over the
channel. As calculated in part (e), the received sequence, with
high probability, is jointly typical with the codeword that was
sent. What is the probability that one or more of the other
codewords (which were chosen at random, independent of the
sent codeword) is jointly typical with the received sequence?
[Hint: You could use the union bound, but you could also
calculate this probability exactly, using the result of part (f)
and the independence of the codewords.]
(h) Given that a particular codeword was sent, the probability of
error (averaged over the probability distribution of the chan-
nel and over the random choice of other codewords) can be
written as
Pr(Error|xn(1) sent) = 
yn:yncauses error p(yn|xn(1)). (7.163)
There are two kinds of error: the ﬁrst occurs if the received
sequence yn is not jointly typical with the transmitted code-
word, and the second occurs if there is another codeword
jointly typical with the received sequence. Using the result
of the preceding parts, calculate this probability of error. By


