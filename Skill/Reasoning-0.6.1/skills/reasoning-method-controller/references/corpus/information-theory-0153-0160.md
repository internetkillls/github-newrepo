# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 153

5.9
SHANNON–FANO–ELIAS CODING
127
Now examine the two terms in (5.71). By assumption, since L∗(p′) is the
optimal length for p′, we have L(p′) −L∗(p′) ≥0. Similarly, the length
of the extension of the optimal code for p′ has to have an average length
at least as large as the optimal code for p [i.e., L(p) −L∗(p) ≥0]. But
the sum of two nonnegative terms can only be 0 if both of them are 0,
which implies that L(p) = L∗(p) (i.e., the extension of the optimal code
for p′ is optimal for p).
Consequently, if we start with an optimal code for p′ with m −1 sym-
bols and construct a code for m symbols by extending the codeword
corresponding to pm−1 + pm, the new code is also optimal. Starting with
a code for two elements, in which case the optimal code is obvious, we
can by induction extend this result to prove the following theorem.
Theorem 5.8.1
Huffman coding is optimal; that is, if C∗is a Huffman
code and C′ is any other uniquely decodable code, L(C∗) ≤L(C′).
Although we have proved the theorem for a binary alphabet, the proof
can be extended to establishing optimality of the Huffman coding algo-
rithm for a D-ary alphabet as well. Incidentally, we should remark that
Huffman coding is a “greedy” algorithm in that it coalesces the two least
likely symbols at each stage. The proof above shows that this local opti-
mality ensures global optimality of the ﬁnal code.
5.9
SHANNON–FANO–ELIAS CODING
In Section 5.4 we showed that the codeword lengths l(x) =
	
log
1
p(x)

sat-
isfy the Kraft inequality and can therefore be used to construct a uniquely
decodable code for the source. In this section we describe a simple con-
structive procedure that uses the cumulative distribution function to allot
codewords.
Without loss of generality, we can take X = {1, 2, . . . , m}. Assume that
p(x) > 0 for all x. The cumulative distribution function F(x) is deﬁned
as
F(x) =

a≤x
p(a).
(5.72)
This function is illustrated in Figure 5.5. Consider the modiﬁed cumulative
distribution function
F(x) =

a<x
p(a) + 1
2p(x),
(5.73)


## PDF page 154

128
DATA COMPRESSION
F(x)
F(x)
F(x)
F(x − 1)
1
2
x
x
p(x)
FIGURE 5.5. Cumulative distribution function and Shannon–Fano–Elias coding.
where F(x) denotes the sum of the probabilities of all symbols less than
x plus half the probability of the symbol x. Since the random variable is
discrete, the cumulative distribution function consists of steps of size p(x).
The value of the function F(x) is the midpoint of the step corresponding
to x.
Since all the probabilities are positive, F(a) ̸= F(b) if a ̸= b, and hence
we can determine x if we know F(x). Merely look at the graph of the
cumulative distribution function and ﬁnd the corresponding x. Thus, the
value of F(x) can be used as a code for x.
But, in general, F(x) is a real number expressible only by an inﬁnite
number of bits. So it is not efﬁcient to use the exact value of F(x) as a
code for x. If we use an approximate value, what is the required accuracy?
Assume that we truncate F(x) to l(x) bits (denoted by ⌊F(x)⌋l(x)).
Thus, we use the ﬁrst l(x) bits of F(x) as a code for x. By deﬁnition of
rounding off, we have
F(x) −⌊F(x)⌋l(x) <
1
2l(x).
(5.74)
If l(x) =
	
log
1
p(x)

+ 1, then
1
2l(x) < p(x)
2
= F(x) −F(x −1),
(5.75)
and therefore ⌊F(x)⌋l(x) lies within the step corresponding to x. Thus,
l(x) bits sufﬁce to describe x.


## PDF page 155

5.9
SHANNON–FANO–ELIAS CODING
129
In addition to requiring that the codeword identify the corresponding
symbol, we also require the set of codewords to be preﬁx-free. To check
whether the code is preﬁx-free, we consider each codeword z1z2 · · · zl to
represent not a point but the interval

0.z1z2 · · · zl, 0.z1z2 · · · zl + 1
2l

. The
code is preﬁx-free if and only if the intervals corresponding to codewords
are disjoint.
We now verify that the code above is preﬁx-free. The interval corre-
sponding to any codeword has length 2−l(x), which is less than half the
height of the step corresponding to x by (5.75). The lower end of the
interval is in the lower half of the step. Thus, the upper end of the inter-
val lies below the top of the step, and the interval corresponding to any
codeword lies entirely within the step corresponding to that symbol in the
cumulative distribution function. Therefore, the intervals corresponding to
different codewords are disjoint and the code is preﬁx-free. Note that this
procedure does not require the symbols to be ordered in terms of proba-
bility. Another procedure that uses the ordered probabilities is described
in Problem 5.5.28.
Since we use l(x) =
	
log
1
p(x)

+ 1 bits to represent x, the expected
length of this code is
L =

x
p(x)l(x) =

x
p(x)

log
1
p(x)

+ 1

< H(X) + 2. (5.76)
Thus, this coding scheme achieves an average codeword length that is
within 2 bits of the entropy.
Example 5.9.1
We ﬁrst consider an example where all the probabilities
are dyadic. We construct the code in the following table:
x
p(x)
F(x)
F(x)
F(x) in Binary
l(x) =

log
1
p(x)

+ 1
Codeword
1
0.25
0.25
0.125
0.001
3
001
2
0.5
0.75
0.5
0.10
2
10
3
0.125
0.875
0.8125
0.1101
4
1101
4
0.125
1.0
0.9375
0.1111
4
1111
In this case, the average codeword length is 2.75 bits and the entropy
is 1.75 bits. The Huffman code for this case achieves the entropy
bound. Looking at the codewords, it is obvious that there is some inef-
ﬁciency—for example, the last bit of the last two codewords can be
omitted. But if we remove the last bit from all the codewords, the code
is no longer preﬁx-free.


## PDF page 156

130
DATA COMPRESSION
Example 5.9.2
We now give another example for construction of the
Shannon–Fano–Elias code. In this case, since the distribution is not
dyadic, the representation of F(x) in binary may have an inﬁnite number
of bits. We denote 0.01010101 . . . by 0.01. We construct the code in the
following table:
x
p(x)
F(x)
F(x)
F(x) in Binary
l(x) =

log
1
p(x)

+ 1
Codeword
1
0.25
0.25
0.125
0.001
3
001
2
0.25
0.5
0.375
0.011
3
011
3
0.2
0.7
0.6
0.10011
4
1001
4
0.15
0.85
0.775
0.1100011
4
1100
5
0.15
1.0
0.925
0.1110110
4
1110
The above code is 1.2 bits longer on the average than the Huffman
code for this source (Example 5.6.1).
The Shannon–Fano–Elias coding procedure can also be applied to
sequences of random variables. The key idea is to use the cumulative
distribution function of the sequence, expressed to the appropriate accu-
racy, as a code for the sequence. Direct application of the method to blocks
of length n would require calculation of the probabilities and cumulative
distribution function for all sequences of length n, a calculation that would
grow exponentially with the block length. But a simple trick ensures that
we can calculate both the probability and the cumulative density func-
tion sequentially as we see each symbol in the block, ensuring that the
calculation grows only linearly with the block length. Direct application
of Shannon–Fano–Elias coding would also need arithmetic whose preci-
sion grows with the block size, which is not practical when we deal with
long blocks. In Chapter 13 we describe arithmetic coding, which is an
extension of the Shannon–Fano–Elias method to sequences of random
variables that encodes using ﬁxed-precision arithmetic with a complexity
that is linear in the length of the sequence. This method is the basis of
many practical compression schemes such as those used in the JPEG and
FAX compression standards.
5.10
COMPETITIVE OPTIMALITY OF THE SHANNON CODE
We have shown that Huffman coding is optimal in that it has minimum
expected length. But what does that say about its performance on any
particular sequence? For example, is it always better than any other code
for all sequences? Obviously not, since there are codes that assign short


## PDF page 157

5.10
COMPETITIVE OPTIMALITY OF THE SHANNON CODE
131
codewords to infrequent source symbols. Such codes will be better than
the Huffman code on those source symbols.
To formalize the question of competitive optimality, consider the fol-
lowing two-person zero-sum game: Two people are given a probability
distribution and are asked to design an instantaneous code for the dis-
tribution. Then a source symbol is drawn from this distribution, and the
payoff to player A is 1 or −1, depending on whether the codeword of
player A is shorter or longer than the codeword of player B. The payoff
is 0 for ties.
Dealing with Huffman code lengths is difﬁcult, since there is no explicit
expression for the codeword lengths. Instead, we consider the Shannon
code with codeword lengths l(x) =
	
log
1
p(x)

. In this case, we have the
following theorem.
Theorem 5.10.1
Let l(x) be the codeword lengths associated with the
Shannon code, and let l′(x) be the codeword lengths associated with any
other uniquely decodable code. Then
Pr

l(X) ≥l′(X) + c

≤
1
2c−1 .
(5.77)
For example, the probability that l′(X) is 5 or more bits shorter than
l(X) is less than
1
16.
Proof
Pr

l(X) ≥l′(X) + c

= Pr

log
1
p(X)

≥l′(X) + c

(5.78)
≤Pr

log
1
p(X) ≥l′(X) + c −1

(5.79)
= Pr

p(X) ≤2−l′(X)−c+1
(5.80)
=

x: p(x)≤2−l′(x)−c+1
p(x)
(5.81)
≤

x: p(x)≤2−l′(x)−c+1
2−l′(x)−(c−1)
(5.82)
≤

x
2−l′(x)2−(c−1)
(5.83)
≤2−(c−1)
(5.84)
since  2−l′(x) ≤1 by the Kraft inequality.
□


## PDF page 158

132
DATA COMPRESSION
Hence, no other code can do much better than the Shannon code most
of the time. We now strengthen this result. In a game-theoretic setting,
one would like to ensure that l(x) < l′(x) more often than l(x) > l′(x).
The fact that l(x) ≤l′(x) + 1 with probability ≥1
2 does not ensure this.
We now show that even under this stricter criterion, Shannon coding is
optimal. Recall that the probability mass function p(x) is dyadic if log
1
p(x)
is an integer for all x.
Theorem 5.10.2
For a dyadic probability mass function p(x), let
l(x) = log
1
p(x) be the word lengths of the binary Shannon code for the
source, and let l′(x) be the lengths of any other uniquely decodable binary
code for the source. Then
Pr(l(X) < l′(X)) ≥Pr(l(X) > l′(X)),
(5.85)
with equality if and only if l′(x) = l(x) for all x. Thus, the code length
assignment l(x) = log
1
p(x) is uniquely competitively optimal.
Proof:
Deﬁne the function sgn(t) as follows:
sgn(t) =



1
if t > 0
0
if t = 0
−1
if t < 0
(5.86)
Then it is easy to see from Figure 5.6 that
sgn(t) ≤2t −1
for t = 0, ±1, ±2, . . . .
(5.87)
sgn(x)
−1
1
1
2t − 1
x
FIGURE 5.6. Sgn function and a bound.


## PDF page 159

5.10
COMPETITIVE OPTIMALITY OF THE SHANNON CODE
133
Note that though this inequality is not satisﬁed for all t, it is satisﬁed
at all integer values of t. We can now write
Pr(l′(X) < l(X)) −Pr(l′(X) > l(X)) =

x:l′(x)<l(x)
p(x) −

x:l′(x)>l(x)
p(x)
(5.88)
=

x
p(x)sgn(l(x) −l′(x))
(5.89)
= E sgn

l(X) −l′(X)

(5.90)
(a)
≤

x
p(x)

2l(x)−l′(x) −1

(5.91)
=

x
2−l(x) 
2l(x)−l′(x) −1

(5.92)
=

x
2−l′(x) −

x
2−l(x)
(5.93)
=

x
2−l′(x) −1
(5.94)
(b)
≤1 −1
(5.95)
= 0,
(5.96)
where (a) follows from the bound on sgn(x) and (b) follows from the fact
that l′(x) satisﬁes the Kraft inequality.
We have equality in the above chain only if we have equality in (a)
and (b). We have equality in the bound for sgn(t) only if t is 0 or 1 [i.e.,
l(x) = l′(x) or l(x) = l′(x) + 1]. Equality in (b) implies that l′(x) satisﬁes
the Kraft inequality with equality. Combining these two facts implies that
l′(x) = l(x) for all x.
□
Corollary
For nondyadic probability mass functions,
E sgn(l(X) −l′(X) −1) ≤0,
(5.97)
where l(x) =
	
log
1
p(x)

and l′(x) is any other code for the source.


## PDF page 160

134
DATA COMPRESSION
Proof:
Along the same lines as the preceding proof.
□
Hence we have shown that Shannon coding l(x) =
	
log
1
p(x)

is opti-
mal under a variety of criteria; it is robust with respect to the payoff
function. In particular, for dyadic p, E(l −l′) ≤0, E sgn(l −l′) ≤0, and
by use of inequality (5.87), Ef (l −l′) ≤0 for any function f satisfying
f (t) ≤2t −1, t = 0, ±1, ±2, . . ..
5.11
GENERATION OF DISCRETE DISTRIBUTIONS FROM FAIR
COINS
In the early sections of this chapter we considered the problem of repre-
senting a random variable by a sequence of bits such that the expected
length of the representation was minimized. It can be argued (Prob-
lem 5.5.29) that the encoded sequence is essentially incompressible and
therefore has an entropy rate close to 1 bit per symbol. Therefore, the bits
of the encoded sequence are essentially fair coin ﬂips.
In this section we take a slight detour from our discussion of source
coding and consider the dual question. How many fair coin ﬂips does
it take to generate a random variable X drawn according to a speciﬁed
probability mass function p? We ﬁrst consider a simple example.
Example 5.11.1
Given a sequence of fair coin tosses (fair bits), suppose
that we wish to generate a random variable X with distribution
X =



a
with probability 1
2,
b
with probability 1
4,
c
with probability 1
4.
(5.98)
It is easy to guess the answer. If the ﬁrst bit is 0, we let X = a. If the
ﬁrst two bits are 10, we let X = b. If we see 11, we let X = c. It is clear
that X has the desired distribution.
We calculate the average number of fair bits required for generating
the random variable, in this case as 1
2(1) + 1
4(2) + 1
4(2) = 1.5 bits. This
is also the entropy of the distribution. Is this unusual? No, as the results
of this section indicate.
The general problem can now be formulated as follows. We are given a
sequence of fair coin tosses Z1, Z2, . . . , and we wish to generate a discrete
random variable X ∈X = {1, 2, . . . , m} with probability mass function


