# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 465

13.3
ARITHMETIC CODING
439
not inﬁnite-precision points for the cumulative distribution function but
intervals in the unit interval. Any ﬁnite-length sequence of symbols can
be said to correspond to a subinterval of the unit interval. The objective
of the arithmetic coding algorithm is to represent a sequence of random
variables by a subinterval in [0, 1]. As the algorithm observes more input
symbols, the length of the subinterval corresponding to the input sequence
decreases. As the top end of the interval and the bottom end of the inter-
val get closer, they begin to agree in the ﬁrst few bits. These will be ﬁrst
few bits of the output sequence. As soon as the two ends of the interval
agree, we can output the corresponding bits. We can therefore shift these
bits out of the calculation and effectively scale the remaining intervals so
that entire calculation can be done with ﬁnite precision. We will not go
into the details here—there is a very good description of the algorithm
and performance considerations in Bell et al. [41]
Example 13.3.2
(Arithmetic coding for a ternary input alphabet)
Con-
sider a random variable X with a ternary alphabet {A, B, C}, which
are assumed to have probabilities 0.4, 0.4, and 0.2, respectively. Let
the sequence to be encoded by ACAA. Thus, Fl(·) = (0, 0.4, 0.8) and
Fh(·) = (0.4, 0.8, 1.0). Initially, the input sequence is empty, and the cor-
responding interval is [0, 1). The cumulative distribution function after
the ﬁrst input symbol is shown in Figure 13.2. It is easy to calculate that
the interval in the algorithm without scaling after the ﬁrst symbol A is
A
1.0
0.8
0.4
B
C
xn
F(xn)
FIGURE 13.2. Cumulative distribution function after the ﬁrst symbol.


## PDF page 466

440
UNIVERSAL SOURCE CODING
AA
AB
AC
BA
BB
BC
CA
CB
CC
xn
F(xn)
0.32
0.4
FIGURE 13.3. Cumulative distribution function after the second symbol.
[0, 0.4); after the second symbol, C, it is [0.32, 0.4) (Figure 13.3); after
the third symbol A, it is [0.32,0.352); and after the fourth symbol A, it
is [0.32, 0.3328). Since the probability of this sequence is 0.0128, we
will use log(1/0.0128) + 2 (i.e., 9 bits) to encode the midpoint of the
interval sequence using Shannon–Fano–Elias coding (0.3264, which is
0.010100111 binary).
In summary, the arithmetic coding procedure, given any length n and
probability mass functionq(x1x2 · · · xn), enables one to encode the sequence
x1x2 · · · xn in a code of length log
1
q(x1x2···xn) + 2 bits. If the source is i.i.d.
and the assumed distribution q is equal to the true distribution p of the data,
this procedure achieves an average length for the block that is within 2 bits
of the entropy. Although this is not necessarily optimal for any ﬁxed block
length (a Huffman code designed for the distribution could have a lower
average codeword length), the procedure is incremental and can be used for
any blocklength.
13.4
LEMPEL–ZIV CODING
In Section 13.3 we discussed the basic ideas of arithmetic coding and
mentioned some results on worst-case redundancy for coding a sequence
from an unknown distribution. We now discuss a popular class of tech-
niques for source coding that are universally optimal (their asymptotic


## PDF page 467

13.4
LEMPEL–ZIV CODING
441
compression rate approaches the entropy rate of the source for any sta-
tionary ergodic source) and simple to implement. This class of algorithms
is termed Lempel–Ziv, named after the authors of two seminal papers
[603, 604] that describe the two basic algorithms that underlie this class.
The algorithms could also be described as adaptive dictionary compression
algorithms.
The notion of using dictionaries for compression dates back to the
invention of the telegraph. At the time, companies were charged by the
number of letters used, and many large companies produced codebooks for
the frequently used phrases and used the codewords for their telegraphic
communication. Another example is the notion of greetings telegrams
that are popular in India—there is a set of standard greetings such as
“25:Merry Christmas” and “26:May Heaven’s choicest blessings be show-
ered on the newly married couple.” A person wishing to send a greeting
only needs to specify the number, which is used to generate the actual
greeting at the destination.
The idea of adaptive dictionary-based schemes was not explored until
Ziv and Lempel wrote their papers in 1977 and 1978. The two papers
describe two distinct versions of the algorithm. We refer to these ver-
sions as LZ77 or sliding window Lempel–Ziv and LZ78 or tree-structured
Lempel–Ziv. (They are sometimes called LZ1 and LZ2, respectively.)
We ﬁrst describe the basic algorithms in the two cases and describe
some simple variations. We later prove their optimality, and end with
some practical issues. The key idea of the Lempel–Ziv algorithm is to
parse the string into phrases and to replace phrases by pointers to where
the same string has occurred in the past. The differences between the
algorithms is based on differences in the set of possible match locations
(and match lengths) the algorithm allows.
13.4.1
Sliding Window Lempel–Ziv Algorithm
The algorithm described in the 1977 paper encodes a string by ﬁnding the
longest match anywhere within a window of past symbols and represents
the string by a pointer to location of the match within the window and the
length of the match. There are many variations of this basic algorithm,
and we describe one due to Storer and Szymanski [507].
We assume that we have a string x1, x2, . . . to be compressed from a
ﬁnite alphabet. A parsing S of a string x1x2 · · · xn is a division of the
string into phrases, separated by commas. Let W be the length of the
window. Then the algorithm can be described as follows: Assume that
we have compressed the string until time i −1. Then to ﬁnd the next
phrase, ﬁnd the largest k such that for some j, i −1 −W ≤j ≤i −1,


## PDF page 468

442
UNIVERSAL SOURCE CODING
the string of length k starting at xj is equal to the string (of length k)
starting at xi (i.e., xj+l = xi+l for all 0 ≤l < k). The next phrase is then
of length k (i.e., xi . . . xi+k−1) and is represented by the pair (P, L), where
P is the location of the beginning of the match and L is the length of
the match. If a match is not found in the window, the next character is
sent uncompressed. To distinguish between these two cases, a ﬂag bit
is needed, and hence the phrases are of two types: (F, P, L) or (F, C),
where C represents an uncompressed character.
Note that the target of a (pointer,length) pair could extend beyond the
window, so that it overlaps with the new phrase. In theory, this match
could be arbitrarily long; in practice, though, the maximum phrase length
is restricted to be less than some parameter.
For example, if W = 4 and the string is ABBABBABBBAABABA
and the initial window is empty, the string will be parsed as follows:
A,B,B,ABBABB,BA,A,BA,BA, which is represented by the sequence of
“pointers”: (0,A),(0,B),(1,1,1),(1,3,6),(1,4,2),(1,1,1),(1,3,2),(1,2,2), where
the ﬂag bit is 0 if there is no match and 1 if there is a match, and the
location of the match is measured backward from the end of the window.
[In the example, we have represented every match within the window
using the (P, L) pair; however, it might be more efﬁcient to represent
short matches as uncompressed characters. See Problem 13.8 for details.]
We can view this algorithm as using a dictionary that consists of all
substrings of the string in the window and of all single characters. The
algorithm ﬁnds the longest match within the dictionary and sends a pointer
to that match. We later show that a simple variation on this version of
LZ77 is asymptotically optimal. Most practical implementations of LZ77,
such as gzip and pkzip, are also based on this version of LZ77.
13.4.2
Tree-Structured Lempel–Ziv Algorithms
In the 1978 paper, Ziv and Lempel described an algorithm that parses a
string into phrases, where each phrase is the shortest phrase not seen ear-
lier. This algorithm can be viewed as building a dictionary in the form of
a tree, where the nodes correspond to phrases seen so far. The algorithm is
particularly simple to implement and has become popular as one of the early
standard algorithms for ﬁle compression on computers because of its speed
and efﬁciency. It is also used for data compression in high-speed modems.
The source sequence is sequentially parsed into strings that have not
appeared so far. For example, if the string is ABBABBABBBAABABAA
. . . , we parse it as A,B,BA,BB,AB,BBA,ABA,BAA. . . . After every com-
ma, we look along the input sequence until we come to the shortest string
that has not been marked off before. Since this is the shortest such string,


## PDF page 469

13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
443
all its preﬁxes must have occurred earlier. (Thus, we can build up a tree
of these phrases.) In particular, the string consisting of all but the last bit
of this string must have occurred earlier. We code this phrase by giving
the location of the preﬁx and the value of the last symbol. Thus, the string
above would be represented as (0,A),(0,B),(2,A),(2,B),(1,B),(4,A),(5,A),
(3,A), . . . .
Sending an uncompressed character in each phrase results in a loss of
efﬁciency. It is possible to get around this by considering the extension
character (the last character of the current phrase) as part of the next
phrase. This variation, due to Welch [554], is the basis of most practical
implementations of LZ78, such as compress on Unix, in compression in
modems, and in the image ﬁles in the GIF format.
13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
13.5.1
Sliding Window Lempel–Ziv Algorithms
In the original paper of Ziv and Lempel [603], the authors described the
basic LZ77 algorithm and proved that it compressed any string as well
as any ﬁnite-state compressor acting on that string. However, they did
not prove that this algorithm achieved asymptotic optimality (i.e., that the
compression ratio converged to the entropy for an ergodic source). This
result was proved by Wyner and Ziv [591].
The proof relies on a simple lemma due to Kac: the average length of
time that you need to wait to see a particular symbol is the reciprocal of
the probability of a symbol. Thus, we are likely to see the high-probability
strings within the window and encode these strings efﬁciently. The strings
that we do not ﬁnd within the window have low probability, so that
asymptotically, they do not inﬂuence the compression achieved.
Instead of proving the optimality of the practical version of LZ77, we
will present a simpler proof for a different version of the algorithm, which,
though not practical, captures some of the basic ideas. This algorithm
assumes that both the sender and receiver have access to the inﬁnite past
of the string, and represents a string of length n by pointing to the last
time it occurred in the past.
We assume that we have a stationary and ergodic process deﬁned
for time from −∞to ∞, and that both the encoder and decoder have
access to . . . , X−2, X−1, the inﬁnite past of the sequence. Then to encode
X0, X1, . . . , Xn−1 (a block of length n), we ﬁnd the last time we have
seen these n symbols in the past. Let
Rn(X0, X1, . . . , Xn−1) =
max{j < 0 : (X−j, X−j+1 . . . X−j+n−1) = (X0, . . . , Xn−1)}. (13.60)


## PDF page 470

444
UNIVERSAL SOURCE CODING
Then to represent X0, . . . , Xn−1, we need only to send Rn to the receiver,
who can then look back Rn bits into the past and recover X0, . . . , Xn−1.
Thus, the cost of the encoding is the cost of representing Rn. We will show
that this cost is approximately log Rn and that asymptotically 1
nE log Rn
→H(X), thus proving the asymptotic optimality of this algorithm.
We will need the following lemmas.
Lemma 13.5.1
There exists a preﬁx-free code for the integers such that
the length of the codeword for integer k is log k + 2 log log k + O(1).
Proof:
If we knew that k ≤m, we could encode k with log m bits. How-
ever, since we don’t have an upper limit for k, we need to tell the receiver
the length of the encoding of k (i.e., we need to specify log k). Consider
the following encoding for the integer k: We ﬁrst represent ⌈log k⌉in
unary, followed by the binary representation of k:
C1(k) = 00 · · · 0
  
⌈log k⌉0’s
1
xx · · · x
  
k in binary
.
(13.61)
It is easy to see that the length of this representation is 2⌈log k⌉+ 1 ≤
2 log k + 3. This is more than the length we are looking for since we are
using the very inefﬁcient unary code to send log k. However, if we use C1
to represent log k, it is now easy to see that this representation has a length
less than log k + 2 log log k + 4, which proves the lemma. A similar method
is presented in the discussion following Theorem 14.2.3.
□
The key result that underlies the proof of the optimality of LZ77 is
Kac’s lemma, which relates the average recurrence time to the proba-
bility of a symbol for any stationary ergodic process. For example, if
X1, X2, . . . , Xn is an i.i.d. process, we ask what is the expected waiting
time to see the symbol a again, conditioned on the fact that X1 = a. In
this case, the waiting time has a geometric distribution with parameter
p = p(X0 = a), and thus the expected waiting time is 1/p(X0 = a). The
somewhat surprising result is that the same is true even if the process is
not i.i.d., but stationary and ergodic. A simple intuitive reason for this
is that in a long sample of length n, we would expect to see a about
np(a) times, and the average distance between these occurrences of a is
n/(np(a)) (i.e., 1/p(a)).
Lemma 13.5.2
(Kac)
Let . . . , U2, U1, U0, U1, . . . be a stationary
ergodic process on a countable alphabet. For any u such that p(u) > 0


## PDF page 471

13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
445
and for i = 1, 2, . . . , let
Qu(i) = Pr

U−i = u; Uj ̸= u for −i < j < 0|U0 = u

(13.62)
[i.e., Qu(i) is the conditional probability that the most recent previous
occurrence of the symbol u is i, given that U0 = u]. Then
E(R1(U)|X0 = u) =

i
iQu(i) =
1
p(u).
(13.63)
Thus, the conditional expected waiting time to see the symbol u again,
looking backward from zero, is 1/p(u).
Note the amusing fact that the expected recurrence time
ER1(U) =

p(u)
1
p(u) = m,
(13.64)
where m is the alphabet size.
Proof:
LetU0 = u.Deﬁnetheeventsforj = 1, 2, . . .andk = 0, 1, 2, . . . :
Ajk =

U−j = u, Ul ̸= u, −j < l < k, Uk = u

.
(13.65)
Event Ajk corresponds to the event where the last time before zero at
which the process is equal to u is at −j, the ﬁrst time after zero at which
the process equals u is k. These events are disjoint, and by ergodicity, the
probability Pr{∪j,kAjk} = 1. Thus,
1 = Pr

∪j,kAjk

(13.66)
(a)
=
∞

j=1
∞

k=0
Pr{Ajk}
(13.67)
=
∞

j=1
∞

k=0
Pr(Uk = u) Pr

U−j = u, Ul ̸= u, −j < l < k|Uk = u

(13.68)
(b)
=
∞

j=1
∞

k=0
Pr(Uk = u)Qu(j + k)
(13.69)


## PDF page 472

446
UNIVERSAL SOURCE CODING
(c)
=
∞

j=1
∞

k=0
Pr(U0 = u)Qu(j + k)
(13.70)
= Pr(U0 = u)
∞

j=1
∞

k=0
Qu(j + k)
(13.71)
(d)
= Pr(U0 = u)
∞

i=1
iQu(i),
(13.72)
where (a) follows from the fact that the Ajk are disjoint, (b) follows from
the deﬁnition of Qu(·), (c) follows from stationarity, and (d) follows from
the fact that there are i pairs (j, k) such that j + k = i in the sum. Kac’s
lemma follows directly from this equation.
□
Corollary
Let . . . , X−1, X0, X1, . . . be a stationary ergodic process and
let Rn(X0, . . . , Xn−1) be the recurrence time looking backward as deﬁned
in (13.60). Then
E

Rn(X0, . . . , Xn−1)|(X0, . . . , Xn−1) = xn−1
0

=
1
p(xn−1
0
)
.
(13.73)
Proof:
Deﬁne a new process with Ui = (Xi, Xi+1, . . . , Xi+n−1). The U
process is also stationary and ergodic, and thus by Kac’s lemma the aver-
age recurrence time for U conditioned on U0 = u is 1/p(u). Translating
this to the X process proves the corollary.
□
We are now in a position to prove the main result, which shows that
the compression ratio for the simple version of Lempel–Ziv using recur-
rence time approaches the entropy. The algorithm describes Xn−1
0
by
describing Rn(Xn−1
0
), which by Lemma 13.5.1 can be done with log Rn +
2 log log Rn + 4 bits. We now prove the following theorem.
Theorem 13.5.1
Let Ln(Xn−1
0
) = log Rn + 2 log log Rn + O(1) be the
description length for Xn−1
0
in the simple algorithm described above. Then
1
nELn(Xn−1
0
) →H(X)
(13.74)
as n →∞, where H(X) is the entropy rate of the process {Xi}.


