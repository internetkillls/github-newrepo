# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 129

CHAPTER 5
DATA COMPRESSION
We now put content in the deﬁnition of entropy by establishing the funda-
mental limit for the compression of information. Data compression can be
achieved by assigning short descriptions to the most frequent outcomes
of the data source, and necessarily longer descriptions to the less fre-
quent outcomes. For example, in Morse code, the most frequent symbol
is represented by a single dot. In this chapter we ﬁnd the shortest average
description length of a random variable.
We ﬁrst deﬁne the notion of an instantaneous code and then prove the
important Kraft inequality, which asserts that the exponentiated codeword
length assignments must look like a probability mass function. Elemen-
tary calculus then shows that the expected description length must be
greater than or equal to the entropy, the ﬁrst main result. Then Shan-
non’s simple construction shows that the expected description length can
achieve this bound asymptotically for repeated descriptions. This estab-
lishes the entropy as a natural measure of efﬁcient description length.
The famous Huffman coding procedure for ﬁnding minimum expected
description length assignments is provided. Finally, we show that Huff-
man codes are competitively optimal and that it requires roughly H fair
coin ﬂips to generate a sample of a random variable having entropy H.
Thus, the entropy is the data compression limit as well as the number of
bits needed in random number generation, and codes achieving H turn
out to be optimal from many points of view.
5.1
EXAMPLES OF CODES
Deﬁnition
A source code C for a random variable X is a mapping from
X, the range of X, to D∗, the set of ﬁnite-length strings of symbols from
a D-ary alphabet. Let C(x) denote the codeword corresponding to x and
let l(x) denote the length of C(x).
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
103


## PDF page 130

104
DATA COMPRESSION
For example, C(red) = 00, C(blue) = 11 is a source code for X = {red,
blue} with alphabet D = {0, 1}.
Deﬁnition
The expected length L(C) of a source code C(x) for a ran-
dom variable X with probability mass function p(x) is given by
L(C) =

x∈X
p(x)l(x),
(5.1)
where l(x) is the length of the codeword associated with x.
Without loss of generality, we can assume that the D-ary alphabet is
D = {0, 1, . . . , D −1}.
Some examples of codes follow.
Example 5.1.1
Let X be a random variable with the following distri-
bution and codeword assignment:
Pr(X = 1) = 1
2,
codeword C(1) = 0
Pr(X = 2) = 1
4,
codeword C(2) = 10
Pr(X = 3) = 1
8,
codeword C(3) = 110
Pr(X = 4) = 1
8,
codeword C(4) = 111.
(5.2)
The entropy H(X) of X is 1.75 bits, and the expected length L(C) =
El(X) of this code is also 1.75 bits. Here we have a code that has the
same average length as the entropy. We note that any sequence of bits
can be uniquely decoded into a sequence of symbols of X. For example,
the bit string 0110111100110 is decoded as 134213.
Example 5.1.2
Consider another simple example of a code for a random
variable:
Pr(X = 1) = 1
3,
codeword C(1) = 0
Pr(X = 2) = 1
3,
codeword C(2) = 10
Pr(X = 3) = 1
3,
codeword C(3) = 11.
(5.3)
Just as in Example 5.1.1, the code is uniquely decodable. However, in
this case the entropy is log 3 = 1.58 bits and the average length of the
encoding is 1.66 bits. Here El(X) > H(X).
Example 5.1.3
(Morse code) The Morse code is a reasonably efﬁcient
code for the English alphabet using an alphabet of four symbols: a dot,


## PDF page 131

5.1
EXAMPLES OF CODES
105
a dash, a letter space, and a word space. Short sequences represent fre-
quent letters (e.g., a single dot represents E) and long sequences represent
infrequent letters (e.g., Q is represented by “dash,dash,dot,dash”). This is
not the optimal representation for the alphabet in four symbols—in fact,
many possible codewords are not utilized because the codewords for let-
ters do not contain spaces except for a letter space at the end of every
codeword, and no space can follow another space. It is an interesting prob-
lem to calculate the number of sequences that can be constructed under
these constraints. The problem was solved by Shannon in his original
1948 paper. The problem is also related to coding for magnetic recording,
where long strings of 0’s are prohibited [5], [370].
We now deﬁne increasingly more stringent conditions on codes. Let xn
denote (x1, x2, . . . , xn).
Deﬁnition
A code is said to be nonsingular if every element of the
range of X maps into a different string in D∗; that is,
x ̸= x′ ⇒C(x) ̸= C(x′).
(5.4)
Nonsingularity sufﬁces for an unambiguous description of a single
value of X. But we usually wish to send a sequence of values of X.
In such cases we can ensure decodability by adding a special symbol
(a “comma”) between any two codewords. But this is an inefﬁcient use
of the special symbol; we can do better by developing the idea of self-
punctuating or instantaneous codes. Motivated by the necessity to send
sequences of symbols X, we deﬁne the extension of a code as follows:
Deﬁnition
The extension C∗of a code C is the mapping from ﬁnite-
length strings of X to ﬁnite-length strings of D, deﬁned by
C(x1x2 · · · xn) = C(x1)C(x2) · · · C(xn),
(5.5)
where C(x1)C(x2) · · · C(xn) indicates concatenation of the corresponding
codewords.
Example 5.1.4
If C(x1) = 00 and C(x2) = 11, then C(x1x2) = 0011.
Deﬁnition
A code is called uniquely decodable if its extension is non-
singular.
In other words, any encoded string in a uniquely decodable code has
only one possible source string producing it. However, one may have
to look at the entire string to determine even the ﬁrst symbol in the
corresponding source string.


## PDF page 132

106
DATA COMPRESSION
Deﬁnition
A code is called a preﬁx code or an instantaneous code if
no codeword is a preﬁx of any other codeword.
An instantaneous code can be decoded without reference to future code-
words since the end of a codeword is immediately recognizable. Hence,
for an instantaneous code, the symbol xi can be decoded as soon as we
come to the end of the codeword corresponding to it. We need not wait
to see the codewords that come later. An instantaneous code is a self-
punctuating code; we can look down the sequence of code symbols and
add the commas to separate the codewords without looking at later sym-
bols. For example, the binary string 01011111010 produced by the code
of Example 5.1.1 is parsed as 0,10,111,110,10.
The nesting of these deﬁnitions is shown in Figure 5.1. To illustrate the
differences between the various kinds of codes, consider the examples of
codeword assignments C(x) to x ∈X in Table 5.1. For the nonsingular
code, the code string 010 has three possible source sequences: 2 or 14 or
31, and hence the code is not uniquely decodable. The uniquely decodable
code is not preﬁx-free and hence is not instantaneous. To see that it is
uniquely decodable, take any code string and start from the beginning.
If the ﬁrst two bits are 00 or 10, they can be decoded immediately. If
All
codes
Nonsingular
codes
Uniquely
decodable
codes
Instantaneous
codes
FIGURE 5.1. Classes of codes.


## PDF page 133

5.2
KRAFT INEQUALITY
107
TABLE 5.1
Classes of Codes
Nonsingular, But Not
Uniquely Decodable,
X
Singular
Uniquely Decodable
But Not Instantaneous
Instantaneous
1
0
0
10
0
2
0
010
00
10
3
0
01
11
110
4
0
10
110
111
the ﬁrst two bits are 11, we must look at the following bits. If the next
bit is a 1, the ﬁrst source symbol is a 3. If the length of the string of
0’s immediately following the 11 is odd, the ﬁrst codeword must be 110
and the ﬁrst source symbol must be 4; if the length of the string of 0’s is
even, the ﬁrst source symbol is a 3. By repeating this argument, we can see
that this code is uniquely decodable. Sardinas and Patterson [455] have
devised a ﬁnite test for unique decodability, which involves forming sets
of possible sufﬁxes to the codewords and eliminating them systematically.
The test is described more fully in Problem 5.5.27. The fact that the last
code in Table 5.1 is instantaneous is obvious since no codeword is a preﬁx
of any other.
5.2
KRAFT INEQUALITY
We wish to construct instantaneous codes of minimum expected length to
describe a given source. It is clear that we cannot assign short codewords
to all source symbols and still be preﬁx-free. The set of codeword lengths
possible for instantaneous codes is limited by the following inequality.
Theorem 5.2.1
(Kraft inequality)
For any instantaneous code (preﬁx
code) over an alphabet of size D, the codeword lengths l1, l2, . . . , lm must
satisfy the inequality

i
D−li ≤1.
(5.6)
Conversely, given a set of codeword lengths that satisfy this inequality,
there exists an instantaneous code with these word lengths.
Proof:
Consider a D-ary tree in which each node has D children. Let the
branches of the tree represent the symbols of the codeword. For example,
the D branches arising from the root node represent the D possible values
of the ﬁrst symbol of the codeword. Then each codeword is represented


## PDF page 134

108
DATA COMPRESSION
Root
0
10
110
111
FIGURE 5.2. Code tree for the Kraft inequality.
by a leaf on the tree. The path from the root traces out the symbols of the
codeword. A binary example of such a tree is shown in Figure 5.2. The
preﬁx condition on the codewords implies that no codeword is an ancestor
of any other codeword on the tree. Hence, each codeword eliminates its
descendants as possible codewords.
Let lmax be the length of the longest codeword of the set of codewords.
Consider all nodes of the tree at level lmax. Some of them are codewords,
some are descendants of codewords, and some are neither. A codeword
at level li has Dlmax−li descendants at level lmax. Each of these descendant
sets must be disjoint. Also, the total number of nodes in these sets must
be less than or equal to Dlmax. Hence, summing over all the codewords,
we have

Dlmax−li ≤Dlmax
(5.7)
or

D−li ≤1,
(5.8)
which is the Kraft inequality.
Conversely, given any set of codeword lengths l1, l2, . . . , lm that sat-
isfy the Kraft inequality, we can always construct a tree like the one in


## PDF page 135

5.2
KRAFT INEQUALITY
109
Figure 5.2. Label the ﬁrst node (lexicographically) of depth l1 as code-
word 1, and remove its descendants from the tree. Then label the ﬁrst
remaining node of depth l2 as codeword 2, and so on. Proceeding this
way, we construct a preﬁx code with the speciﬁed l1, l2, . . . , lm.
□
We now show that an inﬁnite preﬁx code also satisﬁes the Kraft inequal-
ity.
Theorem 5.2.2
(Extended Kraft Inequality)
For any countably inﬁ-
nite set of codewords that form a preﬁx code, the codeword lengths satisfy
the extended Kraft inequality,
∞

i=1
D−li ≤1.
(5.9)
Conversely, given any l1, l2, . . . satisfying the extended Kraft inequality,
we can construct a preﬁx code with these codeword lengths.
Proof:
Let the D-ary alphabet be {0, 1, . . . , D −1}. Consider the ith
codeword y1y2 · · · yli. Let 0.y1y2 · · · yli be the real number given by the
D-ary expansion
0.y1y2 · · · yli =
li

j=1
yjD−j.
(5.10)
This codeword corresponds to the interval

0.y1y2 · · · yli, 0.y1y2 · · · yli + 1
Dli

,
(5.11)
the set of all real numbers whose D-ary expansion begins with
0.y1y2 · · · yli. This is a subinterval of the unit interval [0, 1]. By the preﬁx
condition, these intervals are disjoint. Hence, the sum of their lengths has
to be less than or equal to 1. This proves that
∞

i=1
D−li ≤1.
(5.12)
Just as in the ﬁnite case, we can reverse the proof to construct the
code for a given l1, l2, . . . that satisﬁes the Kraft inequality. First, reorder
the indexing so that l1 ≤l2 ≤. . . . Then simply assign the intervals in


## PDF page 136

110
DATA COMPRESSION
order from the low end of the unit interval. For example, if we wish to
construct a binary code with l1 = 1, l2 = 2, . . . , we assign the intervals
[0, 1
2), [1
2, 1
4), . . . to the symbols, with corresponding codewords 0, 10,
. . . .
□
In Section 5.5 we show that the lengths of codewords for a uniquely
decodable code also satisfy the Kraft inequality. Before we do that, we
consider the problem of ﬁnding the shortest instantaneous code.
5.3
OPTIMAL CODES
In Section 5.2 we proved that any codeword set that satisﬁes the preﬁx
condition has to satisfy the Kraft inequality and that the Kraft inequality
is a sufﬁcient condition for the existence of a codeword set with the
speciﬁed set of codeword lengths. We now consider the problem of ﬁnding
the preﬁx code with the minimum expected length. From the results of
Section 5.2, this is equivalent to ﬁnding the set of lengths l1, l2, . . . , lm
satisfying the Kraft inequality and whose expected length L =  pili is
less than the expected length of any other preﬁx code. This is a standard
optimization problem: Minimize
L =

pili
(5.13)
over all integers l1, l2, . . . , lm satisfying

D−li ≤1.
(5.14)
A simple analysis by calculus suggests the form of the minimizing l∗
i .
We neglect the integer constraint on li and assume equality in the con-
straint. Hence, we can write the constrained minimization using Lagrange
multipliers as the minimization of
J =

pili + λ

D−li

.
(5.15)
Differentiating with respect to li, we obtain
∂J
∂li
= pi −λD−li loge D.
(5.16)
Setting the derivative to 0, we obtain
D−li =
pi
λ loge D.
(5.17)


