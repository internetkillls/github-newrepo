# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 161

5.11
GENERATION OF DISCRETE DISTRIBUTIONS FROM FAIR COINS
135
a
b
c
FIGURE 5.7. Tree for generation of the distribution ( 1
2, 1
4, 1
4).
p = (p1, p2, . . . , pm). Let the random variable T denote the number of
coin ﬂips used in the algorithm.
We can describe the algorithm mapping strings of bits Z1, Z2, . . . , to
possible outcomes X by a binary tree. The leaves of the tree are marked
by output symbols X, and the path to the leaves is given by the sequence
of bits produced by the fair coin. For example, the tree for the distribution
( 1
2, 1
4, 1
4) is shown in Figure 5.7.
The tree representing the algorithm must satisfy certain properties:
1. The tree should be complete (i.e., every node is either a leaf or has
two descendants in the tree). The tree may be inﬁnite, as we will
see in some examples.
2. The probability of a leaf at depth k is 2−k. Many leaves may be
labeled with the same output symbol—the total probability of all
these leaves should equal the desired probability of the output sym-
bol.
3. The expected number of fair bits ET required to generate X is equal
to the expected depth of this tree.
There are many possible algorithms that generate the same output dis-
tribution. For example, the mapping 00 →a, 01 →b, 10 →c, 11 →a
also yields the distribution ( 1
2, 1
4, 1
4). However, this algorithm uses two
fair bits to generate each sample and is therefore not as efﬁcient as the
mapping given earlier, which used only 1.5 bits per sample. This brings
up the question: What is the most efﬁcient algorithm to generate a given
distribution, and how is this related to the entropy of the distribution?
We expect that we need at least as much randomness in the fair bits as
we produce in the output samples. Since entropy is a measure of random-
ness, and each fair bit has an entropy of 1 bit, we expect that the number
of fair bits used will be at least equal to the entropy of the output. This
is proved in the following theorem. We will need a simple lemma about
trees in the proof of the theorem. Let Y denote the set of leaves of a com-
plete tree. Consider a distribution on the leaves such that the probability


## PDF page 162

136
DATA COMPRESSION
of a leaf at depth k on the tree is 2−k. Let Y be a random variable with
this distribution. Then we have the following lemma.
Lemma 5.11.1
For any complete tree, consider a probability distribu-
tion on the leaves such that the probability of a leaf at depth k is 2−k. Then
the expected depth of the tree is equal to the entropy of this distribution.
Proof:
The expected depth of the tree
ET =

y∈Y
k(y)2−k(y)
(5.99)
and the entropy of the distribution of Y is
H(Y) = −
y∈Y
1
2k(y) log
1
2k(y)
(5.100)
= 
y∈Y k(y)2−k(y),
(5.101)
where k(y) denotes the depth of leaf y. Thus,
H(Y) = ET.
□
(5.102)
Theorem 5.11.1
For any algorithm generating X, the expected number
of fair bits used is greater than the entropy H(X), that is,
ET ≥H(X).
(5.103)
Proof:
Any algorithm generating X from fair bits can be represented by
a complete binary tree. Label all the leaves of this tree by distinct symbols
y ∈Y = {1, 2, . . .}. If the tree is inﬁnite, the alphabet Y is also inﬁnite.
Now consider the random variable Y deﬁned on the leaves of the tree,
such that for any leaf y at depth k, the probability that Y = y is 2−k.
By Lemma 5.11.1, the expected depth of this tree is equal to the entropy
of Y:
ET = H(Y).
(5.104)
Now the random variable X is a function of Y (one or more leaves
map onto an output symbol), and hence by the result of Problem 2.4, we
have
H(X) ≤H(Y).
(5.105)


## PDF page 163

5.11
GENERATION OF DISCRETE DISTRIBUTIONS FROM FAIR COINS
137
Thus, for any algorithm generating the random variable X, we have
H(X) ≤ET.
□
(5.106)
The same argument answers the question of optimality for a dyadic dis-
tribution.
Theorem 5.11.2
Let the random variable X have a dyadic distribu-
tion. The optimal algorithm to generate X from fair coin ﬂips requires an
expected number of coin tosses precisely equal to the entropy:
ET = H(X).
(5.107)
Proof:
Theorem 5.11.1 shows that we need at least H(X) bits to generate
X. For the constructive part, we use the Huffman code tree for X as
the tree to generate the random variable. For a dyadic distribution, the
Huffman code is the same as the Shannon code and achieves the entropy
bound. For any x ∈X, the depth of the leaf in the code tree corresponding
to x is the length of the corresponding codeword, which is log
1
p(x). Hence,
when this code tree is used to generate X, the leaf will have a probability
2−log
1
p(x) = p(x). The expected number of coin ﬂips is the expected depth
of the tree, which is equal to the entropy (because the distribution is
dyadic). Hence, for a dyadic distribution, the optimal generating algorithm
achieves
ET = H(X).
□
(5.108)
What if the distribution is not dyadic? In this case we cannot use the
same idea, since the code tree for the Huffman code will generate a dyadic
distribution on the leaves, not the distribution with which we started. Since
all the leaves of the tree have probabilities of the form 2−k, it follows that
we should split any probability pi that is not of this form into atoms of this
form. We can then allot these atoms to leaves on the tree. For example, if
one of the outcomes x has probability p(x) = 1
4, we need only one atom
(leaf of the tree at level 2), but if p(x) = 7
8 = 1
2 + 1
4 + 1
8, we need three
atoms, one each at levels 1, 2, and 3 of the tree.
To minimize the expected depth of the tree, we should use atoms with
as large a probability as possible. So given a probability pi, we ﬁnd the
largest atom of the form 2−k that is less than pi, and allot this atom to
the tree. Then we calculate the remainder and ﬁnd that largest atom that
will ﬁt in the remainder. Continuing this process, we can split all the


## PDF page 164

138
DATA COMPRESSION
probabilities into dyadic atoms. This process is equivalent to ﬁnding the
binary expansions of the probabilities. Let the binary expansion of the
probability pi be
pi =

j≥1
p(j)
i ,
(5.109)
where p(j)
i
= 2−j or 0. Then the atoms of the expansion are the {p(j)
i
:
i = 1, 2, . . . , m, j ≥1}.
Since 
i pi = 1, the sum of the probabilities of these atoms is 1.
We will allot an atom of probability 2−j to a leaf at depth j on the
tree. The depths of the atoms satisfy the Kraft inequality, and hence by
Theorem 5.2.1, we can always construct such a tree with all the atoms at
the right depths. We illustrate this procedure with an example.
Example 5.11.2
Let X have the distribution
X =
 a
with probability 2
3,
b
with probability 1
3.
(5.110)
We ﬁnd the binary expansions of these probabilities:
2
3 = 0.10101010 . . .2
(5.111)
1
3 = 0.01010101 . . .2 .
(5.112)
Hence, the atoms for the expansion are
2
3 →
1
2, 1
8, 1
32, . . .

(5.113)
1
3 →
1
4, 1
16, 1
64, . . .

.
(5.114)
These can be allotted to a tree as shown in Figure 5.8.
This procedure yields a tree that generates the random variable X.
We have argued that this procedure is optimal (gives a tree of minimum
expected depth), but we will not give a formal proof. Instead, we bound
the expected depth of the tree generated by this procedure.


## PDF page 165

5.11
GENERATION OF DISCRETE DISTRIBUTIONS FROM FAIR COINS
139
a
b
a
b
FIGURE 5.8. Tree to generate a ( 2
3, 1
3) distribution.
Theorem 5.11.3
The expected number of fair bits required by the opti-
mal algorithm to generate a random variable X lies between H(X) and
H(X) + 2:
H(X) ≤ET < H(X) + 2.
(5.115)
Proof:
The lower bound on the expected number of coin tosses is proved
in Theorem 5.11.1. For the upper bound, we write down an explicit
expression for the expected number of coin tosses required for the proce-
dure described above. We split all the probabilities (p1, p2, . . . , pm) into
dyadic atoms, for example,
p1 →

p(1)
1 , p(2)
1 , . . .

,
(5.116)
and so on. Using these atoms (which form a dyadic distribution), we
construct a tree with leaves corresponding to each of these atoms. The
number of coin tosses required to generate each atom is its depth in the
tree, and therefore the expected number of coin tosses is the expected
depth of the tree, which is equal to the entropy of the dyadic distribution
of the atoms. Hence,
ET = H(Y),
(5.117)
where Y has the distribution, (p(1)
1 , p(2)
1 , . . . , p(1)
2 , p(2)
2 , . . . , p(1)
m , p(2)
m , . . .).
Now since X is a function of Y, we have
H(Y) = H(Y, X) = H(X) + H(Y|X),
(5.118)


## PDF page 166

140
DATA COMPRESSION
and our objective is to show that H(Y|X) < 2. We now give an algebraic
proof of this result. Expanding the entropy of Y, we have
H(Y) = −m
i=1

j≥1 p(j)
i
log p(j)
i
(5.119)
= m
i=1

j:p(j)
i
>0 j2−j,
(5.120)
since each of the atoms is either 0 or 2−k for some k. Now consider the
term in the expansion corresponding to each i, which we shall call Ti:
Ti =

j:p(j)
i
>0
j2−j.
(5.121)
We can ﬁnd an n such that 2−(n−1) > pi ≥2−n, or
n −1 < −log pi ≤n.
(5.122)
Then it follows that p(j)
i
> 0 only if j ≥n, so that we can rewrite (5.121)
as
Ti =

j:j≥n,p(j)
i
>0
j2−j.
(5.123)
We use the deﬁnition of the atom to write pi as
pi =

j:j≥n,p(j)
i
>0
2−j.
(5.124)
To prove the upper bound, we ﬁrst show that Ti < −pi log pi + 2pi.
Consider the difference
Ti + pi log pi −2pi
(a)
< Ti −pi(n −1) −2pi
(5.125)
= Ti −(n −1 + 2)pi
(5.126)
=

j:j≥n,p(j)
i
>0
j2−j −(n + 1)

j:j≥n,p(j)
i
>0
2−j
(5.127)
=

j:j≥n,p(j)
i
>0
(j −n −1)2−j
(5.128)


## PDF page 167

SUMMARY
141
= −2−n + 0 +

j:j≥n+2,p(j)
i
>0
(j −n −1)2−j
(5.129)
(b)
= −2−n +

k:k≥1,p(k+n+1)
i
>0
k2−(k+n+1)
(5.130)
(c)
≤−2−n +

k:k≥1
k2−(k+n+1)
(5.131)
= −2−n + 2−(n+1)2
(5.132)
= 0,
(5.133)
where (a) follows from (5.122), (b) follows from a change of variables
for the summation, and (c) follows from increasing the range of the sum-
mation. Hence, we have shown that
Ti < −pi log pi + 2pi.
(5.134)
Since ET = 
i Ti, it follows immediately that
ET < −

i
pi log pi + 2

i
pi = H(X) + 2,
(5.135)
completing the proof of the theorem.
□
Thus, an average of H(X) + 2 coin ﬂips sufﬁce to simulate a random
variable X.
SUMMARY
Kraft inequality. Instantaneous codes ⇔ D−li ≤1.
McMillan inequality. Uniquely decodable codes ⇔ D−li ≤1.
Entropy bound on data compression
L
△=

pili ≥HD(X).
(5.136)


## PDF page 168

142
DATA COMPRESSION
Shannon code
li =

logD
1
pi

(5.137)
HD(X) ≤L < HD(X) + 1.
(5.138)
Huffman code
L∗=
min
 D−li ≤1

pili
(5.139)
HD(X) ≤L∗< HD(X) + 1.
(5.140)
Wrong code. X ∼p(x), l(x) =
	
log
1
q(x)

, L =  p(x)l(x):
H(p) + D(p||q) ≤L < H(p) + D(p||q) + 1.
(5.141)
Stochastic processes
H(X1, X2, . . . , Xn)
n
≤Ln < H(X1, X2, . . . , Xn)
n
+ 1
n.
(5.142)
Stationary processes
Ln →H(X).
(5.143)
Competitive optimality. Shannon code l(x) =
	
log
1
p(x)

versus any
other code l′(x):
Pr

l(X) ≥l′(X) + c

≤
1
2c−1.
(5.144)
PROBLEMS
5.1
Uniquely
decodable
and
instantaneous
codes.
Let
L = m
i=1 pil100
i
be the expected value of the 100th power
of the word lengths associated with an encoding of the random
variable X. Let L1 = min L over all instantaneous codes; and let
L2 = min L over all uniquely decodable codes. What inequality
relationship exists between L1 and L2?


