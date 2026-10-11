# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 169

PROBLEMS
143
5.2
How many ﬁngers has a Martian? Let
S =
S1, . . . , Sm
p1, . . . , pm

.
The Si’s are encoded into strings from a D-symbol output alphabet
in a uniquely decodable manner. If m = 6 and the codeword lengths
are (l1, l2, . . . , l6) = (1, 1, 2, 3, 2, 3), ﬁnd a good lower bound on
D. You may wish to explain the title of the problem.
5.3
Slackness in the Kraft inequality.
An instantaneous code has word
lengths l1, l2, . . . , lm, which satisfy the strict inequality
m

i=1
D−li < 1.
The code alphabet is D = {0, 1, 2, . . . , D −1}. Show that there
exist arbitrarily long sequences of code symbols in D∗which cannot
be decoded into sequences of codewords.
5.4
Huffman coding.
Consider the random variable
X =

x1
x2
x3
x4
x5
x6
x7
0.49
0.26
0.12
0.04
0.04
0.03
0.02

.
(a) Find a binary Huffman code for X.
(b) Find the expected code length for this encoding.
(c) Find a ternary Huffman code for X.
5.5
More Huffman codes.
Find the binary Huffman code for the
source with probabilities ( 1
3, 1
5, 1
5, 2
15, 2
15). Argue that this code is
also optimal for the source with probabilities ( 1
5, 1
5, 1
5, 1
5, 1
5).
5.6
Bad codes.
Which of these codes cannot be Huffman codes for
any probability assignment?
(a) {0, 10, 11}
(b) {00, 01, 10, 110}
(c) {01, 10}
5.7
Huffman 20 questions.
Consider a set of n objects. Let Xi =
1 or 0 accordingly as the ith object is good or defective. Let
X1, X2, . . . , Xn be independent with Pr{Xi = 1} = pi; and p1 >
p2 > · · · > pn > 1
2. We are asked to determine the set of all defec-
tive objects. Any yes–no question you can think of is admissible.


## PDF page 170

144
DATA COMPRESSION
(a) Give a good lower bound on the minimum average number of
questions required.
(b) If the longest sequence of questions is required by nature’s
answers to our questions, what (in words) is the last ques-
tion we should ask? What two sets are we distinguishing with
this question? Assume a compact (minimum average length)
sequence of questions.
(c) Give an upper bound (within one question) on the minimum
average number of questions required.
5.8
Simple optimum compression of a Markov source.
Consider the
three-state Markov process U1, U2, . . . having transition matrix
Un
Un−1
S1
S2
S3
S1
1
2
1
4
1
4
S2
1
4
1
2
1
4
S3
0
1
2
1
2
Thus, the probability that S1 follows S3 is equal to zero. Design
three codes C1, C2, C3 (one for each state 1, 2 and 3, each code
mapping elements of the set of Si’s into sequences of 0’s and 1’s,
such that this Markov process can be sent with maximal compres-
sion by the following scheme:
(a) Note the present symbol Xn = i.
(b) Select code Ci.
(c) Note the next symbol Xn+1 = j and send the codeword in Ci
corresponding to j.
(d) Repeat for the next symbol. What is the average message length
of the next symbol conditioned on the previous state Xn = i
using this coding scheme? What is the unconditional average
number of bits per source symbol? Relate this to the entropy
rate H(U) of the Markov chain.
5.9
Optimal code lengths that require one bit above entropy.
The
source coding theorem shows that the optimal code for a random
variable X has an expected length less than H(X) + 1. Give an
example of a random variable for which the expected length of the
optimal code is close to H(X) + 1 [i.e., for any ϵ > 0, construct a
distribution for which the optimal code has L > H(X) + 1 −ϵ].


## PDF page 171

PROBLEMS
145
5.10
Ternary codes that achieve the entropy bound.
A random variable
X takes on m values and has entropy H(X). An instantaneous
ternary code is found for this source, with average length
L = H(X)
log2 3 = H3(X).
(5.145)
(a) Show that each symbol of X has a probability of the form 3−i
for some i.
(b) Show that m is odd.
5.11
Sufﬁx condition.
Consider codes that satisfy the sufﬁx condition,
which says that no codeword is a sufﬁx of any other codeword.
Show that a sufﬁx condition code is uniquely decodable, and show
that the minimum average length over all codes satisfying the sufﬁx
condition is the same as the average length of the Huffman code
for that random variable.
5.12
Shannon codes and Huffman codes.
Consider a random variable
X that takes on four values with probabilities ( 1
3, 1
3, 1
4, 1
12).
(a) Construct a Huffman code for this random variable.
(b) Show that there exist two different sets of optimal lengths
for the codewords; namely, show that codeword length assign-
ments (1, 2, 3, 3) and (2, 2, 2, 2) are both optimal.
(c) Conclude that there are optimal codes with codeword lengths
for some symbols that exceed the Shannon code length
	
log
1
p(x)

.
5.13
Twenty questions.
Player A chooses some object in the universe,
and player B attempts to identify the object with a series of yes–no
questions. Suppose that player B is clever enough to use the code
achieving the minimal expected length with respect to player A’s
distribution. We observe that player B requires an average of 38.5
questions to determine the object. Find a rough lower bound to the
number of objects in the universe.
5.14
Huffman code.
Find the (a) binary and (b) ternary Huffman codes
for the random variable X with probabilities
p =
 1
21, 2
21, 3
21, 4
21, 5
21, 6
21

.
(c) Calculate L =  pili in each case.


## PDF page 172

146
DATA COMPRESSION
5.15
Huffman codes
(a) Construct a binary Huffman code for the following distribu-
tion on ﬁve symbols: p = (0.3, 0.3, 0.2, 0.1, 0.1). What is the
average length of this code?
(b) Construct a probability distribution p′ on ﬁve symbols for
which the code that you constructed in part (a) has an average
length (under p′) equal to its entropy H(p′).
5.16
Huffman codes.
Consider a random variable X that takes six val-
ues {A, B, C, D, E, F} with probabilities 0.5, 0.25, 0.1, 0.05, 0.05,
and 0.05, respectively.
(a) Construct a binary Huffman code for this random variable.
What is its average length?
(b) Construct a quaternary Huffman code for this random variable
[i.e., a code over an alphabet of four symbols (call them a, b, c
and d)]. What is the average length of this code?
(c) One way to construct a binary code for the random variable
is to start with a quaternary code and convert the symbols into
binary using the mapping a →00, b →01, c →10, and d →
11. What is the average length of the binary code for the random
variable above constructed by this process?
(d) For any random variable X, let LH be the average length of
the binary Huffman code for the random variable, and let LQB
be the average length code constructed by ﬁrst building a qua-
ternary Huffman code and converting it to binary. Show that
LH ≤LQB < LH + 2.
(5.146)
(e) The lower bound in the example is tight. Give an example
where the code constructed by converting an optimal quaternary
code is also the optimal binary code.
(f) The upper bound (i.e., LQB < LH + 2) is not tight. In fact, a
better bound is LQB ≤LH + 1. Prove this bound, and provide
an example where this bound is tight.
5.17
Data compression.
Find an optimal set of binary codeword
lengths l1, l2, . . . (minimizing  pili) for an instantaneous code
for each of the following probability mass functions:
(a) p = ( 10
41, 9
41, 8
41, 7
41, 7
41)
(b) p = ( 9
10, ( 9
10)( 1
10), ( 9
10)( 1
10)2, ( 9
10)( 1
10)3, . . .)


## PDF page 173

PROBLEMS
147
5.18
Classes of codes.
Consider the code {0, 01}.
(a) Is it instantaneous?
(b) Is it uniquely decodable?
(c) Is it nonsingular?
5.19
The game of Hi-Lo
(a) A computer generates a number X according to a known proba-
bility mass function p(x), x ∈{1, 2, . . . , 100}. The player asks
a question, “Is X = i?” and is told “Yes,” “You’re too high,”
or “You’re too low.” He continues for a total of six questions.
If he is right (i.e., he receives the answer “Yes”) during this
sequence, he receives a prize of value v(X). How should the
player proceed to maximize his expected winnings?
(b) Part (a) doesn’t have much to do with information theory. Con-
sider the following variation: X ∼p(x), prize = v(x), p(x)
known, as before. But arbitrary yes–no questions are asked
sequentially until X is determined. (“Determined” doesn’t mean
that a “Yes” answer is received.) Questions cost 1 unit each.
How should the player proceed? What is the expected payoff?
(c) Continuing part (b), what if v(x) is ﬁxed but p(x) can be
chosen by the computer (and then announced to the player)?
The computer wishes to minimize the player’s expected return.
What should p(x) be? What is the expected return to the
player?
5.20
Huffman codes with costs.
Words such as “Run!”, “Help!”, and
“Fire!” are short, not because they are used frequently, but perhaps
because time is precious in the situations in which these words are
required. Suppose that X = i with probability pi, i = 1, 2, . . . , m.
Let li be the number of binary symbols in the codeword associated
with X = i, and let ci denote the cost per letter of the codeword
when X = i. Thus, the average cost C of the description of X is
C = m
i=1 picili.
(a) Minimize C over all l1, l2, . . . , lm such that  2−li ≤1. Ignore
any implied integer constraints on li. Exhibit the minimizing
l∗
1, l∗
2, . . . , l∗
m and the associated minimum value C∗.
(b) How would you use the Huffman code procedure to minimize
C over all uniquely decodable codes? Let CHuffman denote this
minimum.


## PDF page 174

148
DATA COMPRESSION
(c) Can you show that
C∗≤CHuffman ≤C∗+
m

i=1
pici?
5.21
Conditions for unique decodability.
Prove that a code C is
uniquely decodable if (and only if) the extension
Ck(x1, x2, . . . , xk) = C(x1)C(x2) · · · C(xk)
is a one-to-one mapping from Xk to D∗for every k ≥1. (The “only
if” part is obvious.)
5.22
Average length of an optimal code.
Prove that L(p1, . . . , pm),
the average codeword length for an optimal D-ary preﬁx code for
probabilities {p1, . . . , pm}, is a continuous function of p1, . . . , pm.
This is true even though the optimal code changes discontinuously
as the probabilities vary.
5.23
Unused code sequences.
Let C be a variable-length code that
satisﬁes the Kraft inequality with an equality but does not satisfy
the preﬁx condition.
(a) Prove that some ﬁnite sequence of code alphabet symbols is
not the preﬁx of any sequence of codewords.
(b) (Optional) Prove or disprove: C has inﬁnite decoding delay.
5.24
Optimal codes for uniform distributions.
Consider a random vari-
able with m equiprobable outcomes. The entropy of this informa-
tion source is obviously log2 m bits.
(a) Describe the optimal instantaneous binary code for this source
and compute the average codeword length Lm.
(b) For what values of m does the average codeword length Lm
equal the entropy H = log2 m?
(c) We know that L < H + 1 for any probability distribution. The
redundancy of a variable-length code is deﬁned to be ρ =
L −H. For what value(s) of m, where 2k ≤m ≤2k+1, is the
redundancy of the code maximized? What is the limiting value
of this worst-case redundancy as m →∞?
5.25
Optimal codeword lengths.
Although the codeword lengths of an
optimal variable-length code are complicated functions of the mes-
sage probabilities {p1, p2, . . . , pm}, it can be said that less probable


## PDF page 175

PROBLEMS
149
symbols are encoded into longer codewords. Suppose that the mes-
sage probabilities are given in decreasing order, p1 > p2 ≥· · · ≥
pm.
(a) Prove that for any binary Huffman code, if the most probable
message symbol has probability p1 > 2
5, that symbol must be
assigned a codeword of length 1.
(b) Prove that for any binary Huffman code, if the most probable
message symbol has probability p1 < 1
3, that symbol must be
assigned a codeword of length ≥2.
5.26
Merges.
Companies with values W1, W2, . . . , Wm are merged as
follows. The two least valuable companies are merged, thus form-
ing a list of m −1 companies. The value of the merge is the
sum of the values of the two merged companies. This contin-
ues until one supercompany remains. Let V equal the sum of
the values of the merges. Thus, V represents the total reported
dollar volume of the merges. For example, if W = (3, 3, 2, 2),
the merges yield (3, 3, 2, 2) →(4, 3, 3) →(6, 4) →(10) and V =
4 + 6 + 10 = 20.
(a) Argue that V is the minimum volume achievable by sequences
of pairwise merges terminating in one supercompany. (Hint:
Compare to Huffman coding.)
(b) Let W =  Wi,
˜Wi = Wi/W, and show that the minimum
merge volume V satisﬁes
WH( ˜W) ≤V ≤WH( ˜W) + W.
(5.147)
5.27
Sardinas–Patterson test for unique decodability.
A code is not
uniquely decodable if and only if there exists a ﬁnite sequence of
code symbols which can be resolved into sequences of codewords
in two different ways. That is, a situation such as
B1
A1
A2
A3
Am
B2
B3
Bn
...
...
must occur where each Ai and each Bi is a codeword. Note that
B1 must be a preﬁx of A1 with some resulting “dangling sufﬁx.”
Each dangling sufﬁx must in turn be either a preﬁx of a codeword
or have another codeword as its preﬁx, resulting in another dan-
gling sufﬁx. Finally, the last dangling sufﬁx in the sequence must
also be a codeword. Thus, one can set up a test for unique decod-
ability (which is essentially the Sardinas–Patterson test [456]) in


## PDF page 176

150
DATA COMPRESSION
the following way: Construct a set S of all possible dangling suf-
ﬁxes. The code is uniquely decodable if and only if S contains no
codeword.
(a) State the precise rules for building the set S.
(b) Suppose that the codeword lengths are li, i = 1, 2, . . . , m. Find
a good upper bound on the number of elements in the set S.
(c) Determine which of the following codes is uniquely decodable:
(i) {0, 10, 11}
(ii) {0, 01, 11}
(iii) {0, 01, 10}
(iv) {0, 01}
(v) {00, 01, 10, 11}
(vi) {110, 11, 10}
(vii) {110, 11, 100, 00, 10}
(d) For each uniquely decodable code in part (c), construct, if pos-
sible, an inﬁnite encoded sequence with a known starting point
such that it can be resolved into codewords in two different
ways. (This illustrates that unique decodability does not imply
ﬁnite decodability.) Prove that such a sequence cannot arise in
a preﬁx code.
5.28
Shannon code.
Consider the following method for generating a
code for a random variable X that takes on m values {1, 2, . . . , m}
with probabilities p1, p2, . . . , pm. Assume that the probabilities are
ordered so that p1 ≥p2 ≥· · · ≥pm. Deﬁne
Fi =
i−1

k=1
pk,
(5.148)
the sum of the probabilities of all symbols less than i. Then the
codeword for i is the number Fi ∈[0, 1] rounded off to li bits,
where li = ⌈log 1
pi ⌉.
(a) Show that the code constructed by this process is preﬁx-free
and that the average length satisﬁes
H(X) ≤L < H(X) + 1.
(5.149)
(b) Construct the code for the probability distribution (0.5, 0.25,
0.125, 0.125).


