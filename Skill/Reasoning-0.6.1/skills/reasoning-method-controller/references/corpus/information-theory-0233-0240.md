# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 233

7.9
FANO’S INEQUALITY AND THE CONVERSE TO THE CODING THEOREM
207
since by the deﬁnition of a discrete memoryless channel, Yi depends only
on Xi and is conditionally independent of everything else. Continuing the
series of inequalities, we have
I (Xn; Y n) = H(Y n) −
n

i=1
H(Yi|Xi)
(7.94)
≤
n

i=1
H(Yi) −
n

i=1
H(Yi|Xi)
(7.95)
=
n

i=1
I (Xi; Yi)
(7.96)
≤nC,
(7.97)
where (7.95) follows from the fact that the entropy of a collection of ran-
dom variables is less than the sum of their individual entropies, and (7.97)
follows from the deﬁnition of capacity. Thus, we have proved that using the
channel many times does not increase the information capacity in bits per
transmission.
□
We are now in a position to prove the converse to the channel coding
theorem.
Proof:
Converse to Theorem 7.7.1 (Channel coding theorem). We have
to show that any sequence of (2nR, n) codes with λ(n) →0 must have R ≤
C. If the maximal probability of error tends to zero, the average probability
of error for the sequence of codes also goes to zero [i.e., λ(n) →0 implies
P (n)
e
→0, where P (n)
e
is deﬁned in (7.32)]. For a ﬁxed encoding rule
Xn(·) and a ﬁxed decoding rule ˆW = g(Y n), we have W →Xn(W) →
Y n →ˆW. For each n, let W be drawn according to a uniform distribution
over {1, 2, . . . , 2nR}. Since W has a uniform distribution, Pr( ˆW ̸= W) =
P (n)
e
=
1
2nR

i λi. Hence,
nR
(a)
= H(W)
(7.98)
(b)
= H(W| ˆW) + I (W; ˆW)
(7.99)
(c)
≤1 + P (n)
e
nR + I (W; ˆW)
(7.100)
(d)
≤1 + P (n)
e
nR + I (Xn; Y n)
(7.101)
(e)
≤1 + P (n)
e
nR + nC,
(7.102)


## PDF page 234

208
CHANNEL CAPACITY
where (a) follows from the assumption that W is uniform over {1, 2, . . . ,
2nR}, (b) is an identity, (c) is Fano’s inequality for W taking on at most 2nR
values, (d) is the data-processing inequality, and (e) is from Lemma 7.9.2.
Dividing by n, we obtain
R ≤P (n)
e
R + 1
n + C.
(7.103)
Now letting n →∞, we see that the ﬁrst two terms on the right-hand
side tend to 0, and hence
R ≤C.
(7.104)
We can rewrite (7.103) as
P (n)
e
≥1 −C
R −1
nR.
(7.105)
This equation shows that if R > C, the probability of error is bounded
away from 0 for sufﬁciently large n (and hence for all n, since if P (n)
e
= 0
for small n, we can construct codes for large n with P (n)
e
= 0 by con-
catenating these codes). Hence, we cannot achieve an arbitrarily low
probability of error at rates above capacity.
□
This converse is sometimes called the weak converse to the channel
coding theorem. It is also possible to prove a strong converse, which states
that for rates above capacity, the probability of error goes exponentially
to 1. Hence, the capacity is a very clear dividing point—at rates below
capacity, P (n)
e
→0 exponentially, and at rates above capacity, P (n)
e
→1
exponentially.
7.10
EQUALITY IN THE CONVERSE TO THE CHANNEL
CODING THEOREM
We have proved the channel coding theorem and its converse. In essence,
these theorems state that when R < C, it is possible to send informa-
tion with an arbitrarily low probability of error, and when R > C, the
probability of error is bounded away from zero.
It is interesting and rewarding to examine the consequences of equality
in the converse; hopefully, it will give some ideas as to the kinds of codes
that achieve capacity. Repeating the steps of the converse in the case when
Pe = 0, we have
nR = H(W)
(7.106)
= H(W| ˆW) + I (W; ˆW)
(7.107)


## PDF page 235

7.10
EQUALITY IN THE CONVERSE TO THE CHANNEL CODING THEOREM
209
= I (W; ˆW))
(7.108)
(a)
≤I (Xn(W); Y n)
(7.109)
= H(Y n) −H(Y n|Xn)
(7.110)
= H(Y n) −
n

i=1
H(Yi|Xi)
(7.111)
(b)
≤
n

i=1
H(Yi) −
n

i=1
H(Yi|Xi)
(7.112)
=
n

i=1
I (Xi; Yi)
(7.113)
(c)
≤nC.
(7.114)
We have equality in (a), the data-processing inequality, only if I (Y n;
Xn(W)|W) = 0 and I (Xn; Y n| ˆW) = 0, which is true if all the codewords
are distinct and if ˆW is a sufﬁcient statistic for decoding. We have equality
in (b) only if the Yi’s are independent, and equality in (c) only if the
distribution of Xi is p∗(x), the distribution on X that achieves capacity.
We have equality in the converse only if these conditions are satisﬁed. This
indicates that a capacity-achieving zero-error code has distinct codewords
and the distribution of the Yi’s must be i.i.d. with
p∗(y) =

x
p∗(x)p(y|x),
(7.115)
the distribution on Y induced by the optimum distribution on X. The
distribution referred to in the converse is the empirical distribution on X
and Y induced by a uniform distribution over codewords, that is,
p(xi, yi) =
1
2nR
2nR

w=1
I (Xi(w) = xi)p(yi|xi).
(7.116)
We can check this result in examples of codes that achieve capacity:
1. Noisy typewriter. In this case we have an input alphabet of 26 let-
ters, and each letter is either printed out correctly or changed to the
next letter with probability 1
2. A simple code that achieves capacity
(log 13) for this channel is to use every alternate input letter so that


## PDF page 236

210
CHANNEL CAPACITY
no two letters can be confused. In this case, there are 13 codewords
of block length 1. If we choose the codewords i.i.d. according to a
uniform distribution on {1, 3, 5, 7, . . . , 25}, the output of the channel
is also i.i.d. and uniformly distributed on {1, 2, . . . , 26}, as expected.
2. Binary symmetric channel. Since given any input sequence, every
possible output sequence has some positive probability, it will not
be possible to distinguish even two codewords with zero probability
of error. Hence the zero-error capacity of the BSC is zero. How-
ever, even in this case, we can draw some useful conclusions. The
efﬁcient codes will still induce a distribution on Y that looks i.i.d.
∼Bernoulli(1
2). Also, from the arguments that lead up to the con-
verse, we can see that at rates close to capacity, we have almost
entirely covered the set of possible output sequences with decoding
sets corresponding to the codewords. At rates above capacity, the
decoding sets begin to overlap, and the probability of error can no
longer be made arbitrarily small.
7.11
HAMMING CODES
The channel coding theorem promises the existence of block codes that
will allow us to transmit information at rates below capacity with an
arbitrarily small probability of error if the block length is large enough.
Ever since the appearance of Shannon’s original paper [471], people have
searched for such codes. In addition to achieving low probabilities of
error, useful codes should be “simple,” so that they can be encoded and
decoded efﬁciently.
The search for simple good codes has come a long way since the pub-
lication of Shannon’s original paper in 1948. The entire ﬁeld of coding
theory has been developed during this search. We will not be able to
describe the many elegant and intricate coding schemes that have been
developed since 1948. We will only describe the simplest such scheme
developed by Hamming [266]. It illustrates some of the basic ideas under-
lying most codes.
The object of coding is to introduce redundancy so that even if some
of the information is lost or corrupted, it will still be possible to recover
the message at the receiver. The most obvious coding scheme is to repeat
information. For example, to send a 1, we send 11111, and to send a 0, we
send 00000. This scheme uses ﬁve symbols to send 1 bit, and therefore
has a rate of 1
5 bit per symbol. If this code is used on a binary symmetric
channel, the optimum decoding scheme is to take the majority vote of
each block of ﬁve received bits. If three or more bits are 1, we decode


## PDF page 237

7.11
HAMMING CODES
211
the block as a 1; otherwise, we decode it as 0. An error occurs if and
only if more than three of the bits are changed. By using longer repetition
codes, we can achieve an arbitrarily low probability of error. But the rate
of the code also goes to zero with block length, so even though the code
is “simple,” it is really not a very useful code.
Instead of simply repeating the bits, we can combine the bits in some
intelligent fashion so that each extra bit checks whether there is an error in
some subset of the information bits. A simple example of this is a parity
check code. Starting with a block of n −1 information bits, we choose
the nth bit so that the parity of the entire block is 0 (the number of 1’s
in the block is even). Then if there is an odd number of errors during
the transmission, the receiver will notice that the parity has changed and
detect the error. This is the simplest example of an error-detecting code.
The code does not detect an even number of errors and does not give any
information about how to correct the errors that occur.
We can extend the idea of parity checks to allow for more than one
parity check bit and to allow the parity checks to depend on various subsets
of the information bits. The Hamming code that we describe below is an
example of a parity check code. We describe it using some simple ideas
from linear algebra.
To illustrate the principles of Hamming codes, we consider a binary
code of block length 7. All operations will be done modulo 2. Consider
the set of all nonzero binary vectors of length 3. Arrange them in columns
to form a matrix:
H =


0
0
0
1
1
1
1
0
1
1
0
0
1
1
1
0
1
0
1
0
1

.
(7.117)
Consider the set of vectors of length 7 in the null space of H (the vectors
which when multiplied by H give 000). From the theory of linear spaces,
since H has rank 3, we expect the null space of H to have dimension 4.
These 24 codewords are
0000000
0100101
1000011
1100110
0001111
0101010
1001100
1101001
0010110
0110011
1010101
1110000
0011001
0111100
1011010
1111111
Since the set of codewords is the null space of a matrix, it is linear in the
sense that the sum of any two codewords is also a codeword. The set of
codewords therefore forms a linear subspace of dimension 4 in the vector
space of dimension 7.


## PDF page 238

212
CHANNEL CAPACITY
Looking at the codewords, we notice that other than the all-0 codeword,
the minimum number of 1’s in any codeword is 3. This is called the
minimum weight of the code. We can see that the minimum weight of
a code has to be at least 3 since all the columns of H are different, so
no two columns can add to 000. The fact that the minimum distance is
exactly 3 can be seen from the fact that the sum of any two columns must
be one of the columns of the matrix.
Since the code is linear, the difference between any two codewords is
also a codeword, and hence any two codewords differ in at least three
places. The minimum number of places in which two codewords differ is
called the minimum distance of the code. The minimum distance of the
code is a measure of how far apart the codewords are and will determine
how distinguishable the codewords will be at the output of the channel.
The minimum distance is equal to the minimum weight for a linear code.
We aim to develop codes that have a large minimum distance.
For the code described above, the minimum distance is 3. Hence if a
codeword c is corrupted in only one place, it will differ from any other
codeword in at least two places and therefore be closer to c than to
any other codeword. But can we discover which is the closest codeword
without searching over all the codewords?
The answer is yes. We can use the structure of the matrix H for decod-
ing. The matrix H, called the parity check matrix, has the property that
for every codeword c, Hc = 0. Let ei be a vector with a 1 in the ith
position and 0’s elsewhere. If the codeword is corrupted at position i, the
received vector r = c + ei. If we multiply this vector by the matrix H,
we obtain
Hr = H(c + ei) = Hc + Hei = Hei,
(7.118)
which is the vector corresponding to the ith column of H. Hence looking
at Hr, we can ﬁnd which position of the vector was corrupted. Revers-
ing this bit will give us a codeword. This yields a simple procedure for
correcting one error in the received sequence. We have constructed a code-
book with 16 codewords of block length 7, which can correct up to one
error. This code is called a Hamming code.
We have not yet identiﬁed a simple encoding procedure; we could use
any mapping from a set of 16 messages into the codewords. But if we
examine the ﬁrst 4 bits of the codewords in the table, we observe that
they cycle through all 24 combinations of 4 bits. Thus, we could use
these 4 bits to be the 4 bits of the message we want to send; the other
3 bits are then determined by the code. In general, it is possible to modify
a linear code so that the mapping is explicit, so that the ﬁrst k bits in each


## PDF page 239

7.11
HAMMING CODES
213
codeword represent the message, and the last n −k bits are parity check
bits. Such a code is called a systematic code. The code is often identiﬁed
by its block length n, the number of information bits k and the minimum
distance d. For example, the above code is called a (7,4,3) Hamming code
(i.e., n = 7, k = 4, and d = 3).
An easy way to see how Hamming codes work is by means of a Venn
diagram. Consider the following Venn diagram with three circles and with
four intersection regions as shown in Figure 7.10. To send the information
sequence 1101, we place the 4 information bits in the four intersection
regions as shown in the ﬁgure. We then place a parity bit in each of the
three remaining regions so that the parity of each circle is even (i.e., there
are an even number of 1’s in each circle). Thus, the parity bits are as
shown in Figure 7.11.
Now assume that one of the bits is changed; for example one of the
information bits is changed from 1 to 0 as shown in Figure 7.12. Then
the parity constraints are violated for two of the circles (highlighted in the
ﬁgure), and it is not hard to see that given these violations, the only single
bit error that could have caused it is at the intersection of the two circles
(i.e., the bit that was changed). Similarly working through the other error
cases, it is not hard to see that this code can detect and correct any single
bit error in the received codeword.
We can easily generalize this procedure to construct larger matrices
H. In general, if we use l rows in H, the code that we obtain will have
block length n = 2l −1, k = 2l −l −1 and minimum distance 3. All
these codes are called Hamming codes and can correct one error.
1
1
0
1
FIGURE 7.10. Venn diagram with information bits.


## PDF page 240

214
CHANNEL CAPACITY
0
1
1
0
1
0
1
FIGURE 7.11. Venn diagram with information bits and parity bits with even parity for each
circle.
0
1
1
0
0
1
0
FIGURE 7.12. Venn diagram with one of the information bits changed.
Hamming codes are the simplest examples of linear parity check codes.
They demonstrate the principle that underlies the construction of other
linear codes. But with large block lengths it is likely that there will be
more than one error in the block. In the early 1950s, Reed and Solomon
found a class of multiple error-correcting codes for nonbinary channels.
In the late 1950s, Bose and Ray-Chaudhuri [72] and Hocquenghem [278]
generalized the ideas of Hamming codes using Galois ﬁeld theory to con-
struct t-error correcting codes (called BCH codes) for any t. Since then,
various authors have developed other codes and also developed efﬁcient


