# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 481

13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
455
and therefore c
nH(U, V ) →0 as n →∞. Therefore,
c(n) log c(n)
n
≤−1
n log Qk(x1, x2, . . . , xn|s1) + ϵk(n),
(13.125)
where ϵk(n) →0 as n →∞. Hence, with probability 1,
lim sup
n→∞
c(n) log c(n)
n
≤lim
n→∞−1
n log Qk(X1, X2, . . . , Xn|X0
−(k−1))
(13.126)
= H(X0|X−1, . . . , X−k)
(13.127)
→H(X)
as k →∞.
□
(13.128)
We now prove that LZ78 coding is asymptotically optimal.
Theorem 13.5.3
Let {Xi}∞
−∞be a binary stationary ergodic stochastic
process. Let l(X1, X2, . . . , Xn) be the LZ78 codeword length associated
with X1, X2, . . . , Xn. Then
lim sup
n→∞
1
nl(X1, X2, . . . , Xn) ≤H(X)
with probability 1,
(13.129)
where H(X) is the entropy rate of the process.
Proof:
We have shown that l(X1, X2, . . . , Xn) = c(n)(log c(n) + 1),
where c(n) is the number of phrases in the LZ78 parsing of the
string X1, X2, . . . , Xn. By Lemma 13.5.3, lim sup c(n)/n = 0, and thus
Theorem 13.5.2 establishes that
lim sup l(X1, X2, . . . , Xn)
n
= lim sup
c(n) log c(n)
n
+ c(n)
n

≤H(X)
with probability 1. □
(13.130)
Thus, the length per source symbol of the LZ78 encoding of an ergodic
source is asymptotically no greater than the entropy rate of the source.
There are some interesting features of the proof of the optimality of LZ78
that are worth noting. The bounds on the number of distinct phrases
and Ziv’s inequality apply to any distinct parsing of the string, not just
the incremental parsing version used in the algorithm. The proof can be
extended in many ways with variations on the parsing algorithm; for
example, it is possible to use multiple trees that are context or state


## PDF page 482

456
UNIVERSAL SOURCE CODING
dependent [218, 426]. Ziv’s inequality (Lemma 13.5.5) remains partic-
ularly intriguing since it relates a probability on one side with a purely
deterministic function of the parsing of a sequence on the other.
The Lempel–Ziv codes are simple examples of a universal code (i.e., a
code that does not depend on the distribution of the source). This code can
be used without knowledge of the source distribution and yet will achieve
an asymptotic compression equal to the entropy rate of the source.
SUMMARY
Ideal word length
l∗(x) = log
1
p(x).
(13.131)
Average description length
Epl∗(x) = H(p).
(13.132)
Estimated probability distribution ˆp(x). If ˆl(x) = log
1
ˆp(x), then
Epˆl(x) = H(p) + D(p|| ˆp).
(13.133)
Average redundancy
Rp = Epl(X) −H(p).
(13.134)
Minimax redundancy. For X ∼pθ(x), θ ∈θ,
D∗= min
l
max
p
Rp = min
q max
θ
D(pθ||q).
(13.135)
Minimax theorem. D∗= C, where C is the capacity of the channel
{θ, pθ(x), X}.
Bernoulli sequences. For Xn ∼Bernoulli(θ), the redundancy is
D∗
n = min
q max
θ
D(pθ(xn)||q(xn)) ≈1
2 log n + o(log n).
(13.136)
Arithmetic coding. nH bits of F(xn) reveal approximately n bits
of xn.


## PDF page 483

PROBLEMS
457
Lempel–Ziv coding (recurrence time coding). Let Rn(Xn) be the
last time in the past that we have seen a block of n symbols Xn. Then
1
n log Rn →H(X), and encoding by describing the recurrence time is
asymptotically optimal.
Lempel–Ziv coding (sequence parsing). If a sequence is parsed into
the shortest phrases not seen before (e.g., 011011101 is parsed to
0,1,10,11,101,...) and l(xn) is the description length of the parsed se-
quence, then
lim sup 1
nl(Xn) ≤H(X)
with probability 1
(13.137)
for every stationary ergodic process {Xi}.
PROBLEMS
13.1
Minimax regret data compression and channel capacity.
First
consider universal data compression with respect to two source
distributions. Let the alphabet V = {1, e, 0} and let p1(v) put mass
1 −α on v = 1 and mass α on v = e. Let p2(v) put mass 1 −α on
0 and mass α on v = e. We assign word lengths to V according to
l(v) = log
1
p(v), the ideal codeword length with respect to a clev-
erly chosen probability mass function p(v). The worst-case excess
description length (above the entropy of the true distribution) is
max
i

Epi log
1
p(V ) −Epi log
1
pi(V )

= max
i
D(pi ∥p).
(13.138)
Thus, the minimax regret is D∗= minp maxi D(pi ∥p).
(a) Find D∗.
(b) Find the p(v) achieving D∗.
(c) Compare D∗to the capacity of the binary erasure channel

1 −α
α
0
0
α
1 −α

and comment.


## PDF page 484

458
UNIVERSAL SOURCE CODING
13.2
Universal data compression.
Consider three possible source dis-
tributions on X,
Pa = (0.7, 0.2, 0.1),
Pb = (0.1, 0.7, 0.2),
Pc = (0.2, 0.1, 0.7).
(a) Find the minimum incremental cost of compression
D∗= min
P max
θ
D(Pθ∥P ),
the associated mass function P = (p1, p2, p3), and ideal code-
word lengths li = log(1/pi).
(b) What is the channel capacity of a channel matrix with rows
Pa, Pb, Pc?
13.3
Arithmetic coding.
Let {Xi}∞
i=0 be a stationary binary Markov
chain with transition matrix
pij =
& 3
4
1
4
1
4
3
4
'
.
(13.139)
Calculate the ﬁrst 3 bits of F(X∞) = 0.F1F2 . . . when X∞=
1010111 . . . . How many bits of X∞does this specify?
13.4
Arithmetic coding.
Let Xi be binary stationary Markov with
transition matrix
& 1
3
2
3
2
3
1
3
'
.
(a) Find F(01110) = Pr{.X1X2X3X4X5 < .01110}.
(b) How many bits .F1F2 . . . can be known for sure if it is not
known how X = 01110 continues?
13.5
Lempel–Ziv.
Give
the
LZ78
parsing
and
encoding
of
00000011010100000110101.
13.6
Compression of constant sequence.
We are given the constant
sequence xn = 11111 . . . .
(a) Give the LZ78 parsing for this sequence.
(b) Argue that the number of encoding bits per symbol for this
sequence goes to zero as n →∞.
13.7
Another idealized version of Lempel–Ziv coding.
An idealized
version of LZ was shown to be optimal: The encoder and decoder
both have available to them the “inﬁnite past” generated by the
process, . . . , X−1, X0, and the encoder describes the string (X1,
X2, . . . , Xn) by telling the decoder the position Rn in the past


## PDF page 485

PROBLEMS
459
of the ﬁrst recurrence of that string. This takes roughly log Rn +
2 log log Rn bits. Now consider the following variant: Instead of
describing Rn, the encoder describes Rn−1 plus the last sym-
bol, Xn. From these two the decoder can reconstruct the string
(X1, X2, . . . , Xn).
(a) What is the number of bits per symbol used in this case to
encode (X1, X2, . . . , Xn)?
(b) Modify the proof given in the text to show that this version is
also asymptotically optimal: namely, that the expected number
of bits per symbol converges to the entropy rate.
13.8
Length of pointers in LZ77.
In the version of LZ77 due to Storer
and Szymanski [507] described in Section 13.4.1, a short match
can be represented by either (F, P, L) (ﬂag, pointer, length) or
by (F, C) (ﬂag, character). Assume that the window length is W,
and assume that the maximum match length is M.
(a) How many bits are required to represent P ? To represent L?
(b) Assume that C, the representation of a character, is 8 bits
long. If the representation of P plus L is longer than 8 bits,
it would be better to represent a single character match as
an uncompressed character rather than as a match within the
dictionary. As a function of W and M, what is the shortest
match that one should represent as a match rather than as
uncompressed characters?
(c) Let W = 4096 and M = 256. What is the shortest match that
one would represent as a match rather than uncompressed
characters?
13.9
Lempel–Ziv 78.
(a) Continue
the
Lempel–Ziv
parsing
of
the
sequence
0,00,001,00000011010111.
(b) Give a sequence for which the number of phrases in the LZ
parsing grows as fast as possible.
(c) Give a sequence for which the number of phrases in the LZ
parsing grows as slowly as possible.
13.10
Two versions of ﬁxed-database Lempel–Ziv.
Consider a source
(A, P ). For simplicity assume that the alphabet is ﬁnite |A| =
A < ∞and the symbols are i.i.d. ∼P . A ﬁxed database D is
given and is revealed to the decoder. The encoder parses the tar-
get sequence xn
1 into blocks of length l, and subsequently encodes
them by giving the binary description of their last appearance


## PDF page 486

460
UNIVERSAL SOURCE CODING
in the database. If a match is not found, the entire block is
sent uncompressed, requiring l log A bits. A ﬂag is used to tell
the decoder whether a match location is being described or the
sequence itself. Parts (a) and (b) give some preliminaries you will
need in showing the optimality of ﬁxed-database LZ in part (c).
(a) Let xl be a δ-typical sequence of length l starting at 0, and let
Rl(xl) be the corresponding recurrence index in the inﬁnite
past . . . , X−2, X−1. Show that
E
(
Rl(Xl)|Xl = xl)
≤2l(H+δ),
where H is the entropy rate of the source.
(b) Prove that for any ϵ > 0, Pr

Rl(Xl) > 2l(H+ϵ)
→0 as l →
∞. (Hint: Expand the probability by conditioning on strings
xl, and break things up into typical and nontypical. Markov’s
inequality and the AEP should prove handy as well.)
(c) Consider the following two ﬁxed databases: (i) D1 is formed
by taking all δ-typical l-vectors; and (ii) D2 formed by taking
the most recent ˜L = 2l(H+δ) symbols in the inﬁnite past (i.e.,
X−˜L, . . . , X−1). Argue that the algorithm described above is
asymptotically optimal: namely, that the expected number of
bits per symbol converges to the entropy rate when used in
conjunction with either database D1 or D2.
13.11
Tunstall coding.
The normal setting for source coding maps a
symbol(orablockofsymbols)fromaﬁnitealphabetontoavariable-
length string. An example of such a code is the Huffman code, which
is the optimal (minimal expected length) mapping from a set of
symbols to a preﬁx-free set of codewords. Now consider the dual
problem of variable-to-ﬁxed length codes, where we map a variable-
length sequence of source symbols into a ﬁxed-length binary (or
D-ary) representation. A variable-to-ﬁxed length code for an i.i.d.
sequence of random variables X1, X2, . . . , Xn, Xi ∼p(x), x ∈X
= {0, 1, . . . , m −1}, is deﬁned by a preﬁx-free set of phrases AD ⊂
X∗, where X∗is the set of ﬁnite-length strings of symbols of X, and
|AD| = D. Given any sequence X1, X2, . . . , Xn, the string is parsed
into phrases from AD (unique because of the preﬁx-free property of
AD) and represented by a sequence of symbols from a D-ary alpha-
bet. Deﬁne the efﬁciency of this coding scheme by
R(AD) =
log D
EL(AD),
(13.140)


## PDF page 487

HISTORICAL NOTES
461
where EL(AD) is the expected length of a phrase from AD.
(a) Prove that R(AD) ≥H(X).
(b) The process of constructing AD can be considered as a process
of constructing an m-ary tree whose leaves are the phrases in
AD. Assume that D = 1 + k(m −1) for some integer k ≥1.
Consider the following algorithm due to Tunstall:
(i) Start with A = {0, 1, . . . , m −1} with probabilities p0,
p1, . . . , pm−1. This corresponds to a complete m-ary tree
of depth 1.
(ii) Expand the node with the highest probability. For ex-
ample, if p0 is the node with the highest probability, the
new set is A = {00, 01, . . . , 0(m −1), 1, . . . , (m −1)}.
(iii) Repeat step 2 until the number of leaves (number of
phrases) reaches the required value.
Show that the Tunstall algorithm is optimal in the sense that
it constructs a variable to a ﬁxed code with the best R(AD)
for a given D [i.e., the largest value of EL(AD) for a given
D].
(c) Show that there exists a D such that R(A∗
D) < H(X) + 1.
HISTORICAL NOTES
The problem of encoding a source with an unknown distribution was
analyzed by Fitingof [211] and Davisson [159], who showed that there
were classes of sources for which the universal coding procedure was
asymptotically optimal. The result relating the average redundancy of a
universal code and channel capacity is due to Gallager [229] and Ryabko
[450]. Our proof follows that of Csisz´ar. This result was extended to
show that the channel capacity was the lower bound for the redundancy
for “most” sources in the class by Merhav and Feder [387], extending the
results obtained by Rissanen [444, 448] for the parametric case.
The arithmetic coding procedure has its roots in the Shannon–Fano
code developed by Elias (unpublished), which was analyzed by Jelinek
[297]. The procedure for the construction of a preﬁx-free code described
in the text is due to Gilbert and Moore [249]. Arithmetic coding itself was
developed by Rissanen [441] and Pasco [414]; it was generalized by Lang-
don and Rissanen [343]. See also the enumerative methods in Cover [120].
Tutorial introductions to arithmetic coding can be found in Langdon [342]
and Witten et al. [564]. Arithmetic coding combined with the context-tree
weighting algorithm due to Willems et al. [560, 561] achieve the Rissanen


## PDF page 488

462
UNIVERSAL SOURCE CODING
lower bound [444] and therefore have the optimal rate of convergence to
the entropy for tree sources with unknown parameters.
The class of Lempel–Ziv algorithms was ﬁrst described in the seminal
papers of Lempel and Ziv [603, 604]. The original results were theoreti-
cally interesting, but people implementing compression algorithms did not
take notice until the publication of a simple efﬁcient version of the algo-
rithm due to Welch [554]. Since then, multiple versions of the algorithms
have been described, many of them patented. Versions of this algorithm
are now used in many compression products, including GIF ﬁles for image
compression and the CCITT standard for compression in modems. The
optimality of the sliding window version of Lempel–Ziv (LZ77) is due to
Wyner and Ziv [575]. An extension of the proof of the optimality of LZ78
[426] shows that the redundancy of LZ78 is on the order of 1/ log(n),
as opposed to the lower bounds of log(n)/n. Thus even though LZ78
is asymptotically optimal for all stationary ergodic sources, it converges
to the entropy rate very slowly compared to the lower bounds for ﬁnite-
state Markov sources. However, for the class of all ergodic sources, lower
bounds on the redundancy of a universal code do not exist, as shown by
examples due to Shields [492] and Shields and Weiss [494]. A lossless
block compression algorithm based on sorting the blocks and using simple
run-length encoding due to Burrows and Wheeler [81] has been analyzed
by Effros et al. [181]. Universal methods for prediction are discussed in
Feder, Merhav and Gutman [204, 386, 388].


