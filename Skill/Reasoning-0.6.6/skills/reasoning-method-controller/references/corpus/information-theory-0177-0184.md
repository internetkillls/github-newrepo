# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 177

PROBLEMS
151
5.29
Optimal codes for dyadic distributions.
For a Huffman code tree,
deﬁne the probability of a node as the sum of the probabilities of
all the leaves under that node. Let the random variable X be drawn
from a dyadic distribution [i.e., p(x) = 2−i, for some i, for all
x ∈X]. Now consider a binary Huffman code for this distribution.
(a) Argue that for any node in the tree, the probability of the left
child is equal to the probability of the right child.
(b) Let X1, X2, . . . , Xn be drawn i.i.d. ∼p(x). Using the Huff-
man code for p(x), we map X1, X2, . . . , Xn to a sequence
of bits Y1, Y2, . . . , Yk(X1,X2,...,Xn). (The length of this sequence
will depend on the outcome X1, X2, . . . , Xn.) Use part (a) to
argue that the sequence Y1, Y2, . . . forms a sequence of fair coin
ﬂips [i.e., that Pr{Yi = 0} = Pr{Yi = 1} = 1
2, independent of
Y1, Y2, . . . , Yi−1]. Thus, the entropy rate of the coded sequence
is 1 bit per symbol.
(c) Give a heuristic argument why the encoded sequence of bits
for any code that achieves the entropy bound cannot be com-
pressible and therefore should have an entropy rate of 1 bit per
symbol.
5.30
Relative entropy is cost of miscoding.
Let the random variable X
have ﬁve possible outcomes {1, 2, 3, 4, 5}. Consider two distribu-
tions p(x) and q(x) on this random variable.
Symbol
p(x)
q(x)
C1(x)
C2(x)
1
1
2
1
2
0
0
2
1
4
1
8
10
100
3
1
8
1
8
110
101
4
1
16
1
8
1110
110
5
1
16
1
8
1111
111
(a) Calculate H(p), H(q), D(p||q), and D(q||p).
(b) The last two columns represent codes for the random variable.
Verify that the average length of C1 under p is equal to the
entropy H(p). Thus, C1 is optimal for p. Verify that C2 is
optimal for q.
(c) Now assume that we use code C2 when the distribution is p.
What is the average length of the codewords. By how much
does it exceed the entropy p?
(d) What is the loss if we use code C1 when the distribution is q?


## PDF page 178

152
DATA COMPRESSION
5.31
Nonsingular codes.
The discussion in the text focused on instan-
taneous codes, with extensions to uniquely decodable codes. Both
these are required in cases when the code is to be used repeatedly
to encode a sequence of outcomes of a random variable. But if
we need to encode only one outcome and we know when we have
reached the end of a codeword, we do not need unique decod-
ability—the fact that the code is nonsingular would sufﬁce. For
example, if a random variable X takes on three values, a, b, and c,
we could encode them by 0, 1, and 00. Such a code is nonsingular
but not uniquely decodable.
In the following, assume that we have a random variable X which
takes on m values with probabilities p1, p2, . . . , pm and that the
probabilities are ordered so that p1 ≥p2 ≥· · · ≥pm.
(a) By viewing the nonsingular binary code as a ternary code with
three symbols, 0, 1, and “STOP,” show that the expected length
of a nonsingular code L1:1 for a random variable X satisﬁes the
following inequality:
L1:1 ≥H2(X)
log2 3 −1,
(5.150)
where H2(X) is the entropy of X in bits. Thus, the average
length of a nonsingular code is at least a constant fraction of
the average length of an instantaneous code.
(b) Let LINST be the expected length of the best instantaneous code
and L∗
1:1 be the expected length of the best nonsingular code
for X. Argue that L∗
1:1 ≤L∗
INST ≤H(X) + 1.
(c) Give a simple example where the average length of the non-
singular code is less than the entropy.
(d) The set of codewords available for a nonsingular code is {0, 1,
00, 01, 10, 11, 000, . . .}. Since L1:1 = m
i=1 pili, show that this
is minimized if we allot the shortest codewords to the most
probable symbols. Thus, l1 = l2 = 1, l3 = l4 = l5 = l6 = 2, etc.
Show that in general li =

log
 i
2 + 1

, and therefore L∗
1:1 =
m
i=1 pi

log
 i
2 + 1

.
(e) Part (d) shows that it is easy to ﬁnd the optimal nonsin-
gular code for a distribution. However, it is a little more
tricky to deal with the average length of this code. We now
bound this average length. It follows from part (d) that L∗
1:1 ≥


## PDF page 179

PROBLEMS
153
˜L
△= m
i=1 pi log
 i
2 + 1

. Consider the difference
F(p) = H(X) −˜L = −
m

i=1
pi log pi −
m

i=1
pi log
 i
2 + 1

.
(5.151)
Prove by the method of Lagrange multipliers that the maximum
of F(p) occurs when pi = c/(i + 2), where c = 1/(Hm+2 −
H2) and Hk is the sum of the harmonic series:
Hk
△=
k

i=1
1
i .
(5.152)
(This can also be done using the nonnegativity of relative
entropy.)
(f) Complete the arguments for
H(X) −L∗
1:1 ≤H(X) −˜L
(5.153)
≤log(2(Hm+2 −H2)).
(5.154)
Now it is well known (see, e.g., Knuth [315]) that Hk ≈ln k
(more precisely, Hk = ln k + γ + 1
2k −
1
12k2 +
1
120k4 −ϵ, where
0 < ϵ < 1/252n6, and γ = Euler’s constant = 0.577 . . .).
Using either this or a simple approximation that Hk ≤ln k + 1,
which can be proved by integration of 1
x, it can be shown that
H(X) −L∗
1:1 < log log m + 2. Thus, we have
H(X) −log log |X| −2 ≤L∗
1:1 ≤H(X) + 1.
(5.155)
A nonsingular code cannot do much better than an instantaneous
code!
5.32
Bad wine.
One is given six bottles of wine. It is known that
precisely one bottle has gone bad (tastes terrible). From inspection
of the bottles it is determined that the probability pi that the ith
bottle is bad is given by (p1, p2, . . . , p6) = ( 8
23, 6
23, 4
23, 2
23, 2
23, 1
23).
Tasting will determine the bad wine. Suppose that you taste the
wines one at a time. Choose the order of tasting to minimize the


## PDF page 180

154
DATA COMPRESSION
expected number of tastings required to determine the bad bottle.
Remember, if the ﬁrst ﬁve wines pass the test, you don’t have to
taste the last.
(a) What is the expected number of tastings required?
(b) Which bottle should be tasted ﬁrst?
Now you get smart. For the ﬁrst sample, you mix some of the wines
in a fresh glass and sample the mixture. You proceed, mixing and
tasting, stopping when the bad bottle has been determined.
(a) What is the minimum expected number of tastings required to
determine the bad wine?
(b) What mixture should be tasted ﬁrst?
5.33
Huffman vs. Shannon.
A random variable X takes on three values
with probabilities 0.6, 0.3, and 0.1.
(a) What are the lengths of the binary Huffman codewords for
X? What are the lengths of the binary Shannon codewords

l(x) =
	
log

1
p(x)


for X?
(b) What is the smallest integer D such that the expected Shannon
codeword length with a D-ary alphabet equals the expected
Huffman codeword length with a D-ary alphabet?
5.34
Huffman algorithm for tree construction.
Consider the following
problem: m binary signals S1, S2, . . . , Sm are available at times
T1 ≤T2 ≤· · · ≤Tm, and we would like to ﬁnd their sum S1 ⊕S2 ⊕
· · · ⊕Sm using two-input gates, each gate with one time unit delay,
so that the ﬁnal result is available as quickly as possible. A simple
greedy algorithm is to combine the earliest two results, forming
the partial result at time max(T1, T2) + 1. We now have a new
problem with S1 ⊕S2, S3, . . . , Sm, available at times max(T1, T2) +
1, T3, . . . , Tm. We can now sort this list of T ’s and apply the same
merging step again, repeating this until we have the ﬁnal result.
(a) Argue that the foregoing procedure is optimal, in that it con-
structs a circuit for which the ﬁnal result is available as quickly
as possible.
(b) Show that this procedure ﬁnds the tree that minimizes
C(T ) = max
i (Ti + li),
(5.156)
where Ti is the time at which the result allotted to the ith leaf
is available and li is the length of the path from the ith leaf to
the root.


## PDF page 181

PROBLEMS
155
(c) Show that
C(T ) ≥log2

i
2Ti

(5.157)
for any tree T .
(d) Show that there exists a tree such that
C(T ) ≤log2

i
2Ti

+ 1.
(5.158)
Thus, log2

i 2Ti
is the analog of entropy for this problem.
5.35
Generating random variables.
One wishes to generate a random
variable X
X =

1
with probability p
0
with probability 1 −p.
(5.159)
You are given fair coin ﬂips Z1, Z2, . . . . Let N be the (random)
number of ﬂips needed to generate X. Find a good way to use
Z1, Z2, . . . to generate X. Show that EN ≤2.
5.36
Optimal word lengths.
(a) Can l = (1, 2, 2) be the word lengths of a binary Huffman
code. What about (2,2,3,3)?
(b) What word lengths l = (l1, l2, . . .) can arise from binary Huff-
man codes?
5.37
Codes.
Which of the following codes are
(a) Uniquely decodable?
(b) Instantaneous?
C1 = {00, 01, 0}
C2 = {00, 01, 100, 101, 11}
C3 = {0, 10, 110, 1110, . . .}
C4 = {0, 00, 000, 0000}
5.38
Huffman.
Find the Huffman D-ary code for (p1, p2, p3, p4, p5,
p6) = ( 6
25, 6
25, 4
25, 4
25, 3
25, 2
25) and the expected word length
(a) For D = 2.
(b) For D = 4.


## PDF page 182

156
DATA COMPRESSION
5.39
Entropy of encoded bits.
Let C : X −→{0, 1}∗be a nonsingular
but nonuniquely decodable code. Let X have entropy H(X).
(a) Compare H(C(X)) to H(X).
(b) Compare H(C(Xn)) to H(Xn).
5.40
Code rate.
Let X be a random variable with alphabet {1, 2, 3}
and distribution
X =



1
with probability 1
2
2
with probability 1
4
3
with probability 1
4.
The data compression code for X assigns codewords
C(x) =



0
if x = 1
10
if x = 2
11
if x = 3.
Let X1, X2, . . . be independent, identically distributed according
to this distribution and let Z1Z2Z3 · · · = C(X1)C(X2) · · · be the
string of binary symbols resulting from concatenating the corre-
sponding codewords. For example, 122 becomes 01010.
(a) Find the entropy rate H(X) and the entropy rate H(Z) in bits
per symbol. Note that Z is not compressible further.
(b) Now let the code be
C(x) =



00
if x = 1
10
if x = 2
01
if x = 3
and ﬁnd the entropy rate H(Z).
(c) Finally, let the code be
C(x) =



00
if x = 1
1
if x = 2
01
if x = 3
and ﬁnd the entropy rate H(Z).
5.41
Optimal codes.
Let l1, l2, . . . , l10 be the binary Huffman code-
word lengths for the probabilities p1 ≥p2 ≥· · · ≥p10. Suppose
that we get a new distribution by splitting the last probability


## PDF page 183

HISTORICAL NOTES
157
mass. What can you say about the optimal binary codeword lengths
˜l1, ˜l2, . . . , ˜l11 for the probabilities p1, p2, . . . , p9, αp10, (1 −α)p10,
where 0 ≤α ≤1.
5.42
Ternary codes.
Which of the following codeword lengths can be
the word lengths of a 3-ary Huffman code, and which cannot?
(a) (1, 2, 2, 2, 2)
(b) (2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3)
5.43
Piecewise Huffman.
Suppose the codeword that we use to
describe a random variable X ∼p(x) always starts with a symbol
chosen from the set {A, B, C}, followed by binary digits {0, 1}.
Thus, we have a ternary code for the ﬁrst symbol and binary
thereafter. Give the optimal uniquely decodable code (minimum
expected number of symbols) for the probability distribution
p =
16
69, 15
69, 12
69, 10
69, 8
69, 8
69

.
(5.160)
5.44
Huffman.
Find the word lengths of the optimal binary encoding
of p =
 1
100,
1
100, . . . ,
1
100

.
5.45
Random 20 questions.
Let X be uniformly distributed over {1, 2,
. . . , m}. Assume that m = 2n. We ask random questions: Is X ∈S1?
Is X ∈S2?... until only one integer remains. All 2m subsets S of
{1, 2, . . . , m} are equally likely to be asked.
(a) Without loss of generality, suppose that X = 1 is the random
object. What is the probability that object 2 yields the same
answers for k questions as does object 1?
(b) What is the expected number of objects in {2, 3, . . . , m} that
have the same answers to the questions as does the correct
object 1?
(c) Suppose that we ask n + √n
random questions. What is the
expected number of wrong objects agreeing with the answers?
(d) Use Markov’s inequality Pr{X ≥tµ} ≤1
t , to show that the
probability of error (one or more wrong object remaining) goes
to zero as n −→∞.
HISTORICAL NOTES
The foundations for the material in this chapter can be found in Shan-
non’s original paper [469], in which Shannon stated the source coding


## PDF page 184

158
DATA COMPRESSION
theorem and gave simple examples of codes. He described a simple code
construction procedure (described in Problem 5.5.28), which he attributed
to Fano. This method is now called the Shannon–Fano code construction
procedure.
The Kraft inequality for uniquely decodable codes was ﬁrst proved
by McMillan [385]; the proof given here is due to Karush [306]. The
Huffman coding procedure was ﬁrst exhibited and proved to be optimal
by Huffman [283].
In recent years, there has been considerable interest in designing source
codes that are matched to particular applications, such as magnetic record-
ing. In these cases, the objective is to design codes so that the output
sequences satisfy certain properties. Some of the results for this problem
are described by Franaszek [219], Adler et al. [5] and Marcus [370].
The arithmetic coding procedure has its roots in the Shannon–Fano
code developed by Elias (unpublished), which was analyzed by Jelinek
[297]. The procedure for the construction of a preﬁx-free code described
in the text is due to Gilbert and Moore [249]. The extension of the
Shannon–Fano–Elias method to sequences is based on the enumerative
methods in Cover [120] and was described with ﬁnite-precision arithmetic
by Pasco [414] and Rissanen [441]. The competitive optimality of Shan-
non codes was proved in Cover [125] and extended to Huffman codes by
Feder [203]. Section 5.11 on the generation of discrete distributions from
fair coin ﬂips follows the work of Knuth and Yao[317].


