# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 137

5.3
OPTIMAL CODES
111
Substituting this in the constraint to ﬁnd λ, we ﬁnd λ = 1/ loge D, and
hence
pi = D−li,
(5.18)
yielding optimal code lengths,
l∗
i = −logD pi.
(5.19)
This noninteger choice of codeword lengths yields expected codeword
length
L∗=

pil∗
i = −

pi logD pi = HD(X).
(5.20)
But since the li must be integers, we will not always be able to set
the codeword lengths as in (5.19). Instead, we should choose a set of
codeword lengths li “close” to the optimal set. Rather than demonstrate
by calculus that l∗
i = −logD pi is a global minimum, we verify optimality
directly in the proof of the following theorem.
Theorem 5.3.1
The expected length L of any instantaneous D-ary code
for a random variable X is greater than or equal to the entropy HD(X);
that is,
L ≥HD(X),
(5.21)
with equality if and only if D−li = pi.
Proof:
We can write the difference between the expected length and the
entropy as
L −HD(X) =

pili −

pi logD
1
pi
(5.22)
= −

pi logD D−li +

pi logD pi.
(5.23)
Letting ri = D−li/ 
j D−lj and c =  D−li, we obtain
L −H =

pi logD
pi
ri
−logD c
(5.24)
= D(p||r) + logD
1
c
(5.25)
≥0
(5.26)


## PDF page 138

112
DATA COMPRESSION
by the nonnegativity of relative entropy and the fact (Kraft inequality)
that c ≤1. Hence, L ≥H with equality if and only if pi = D−li (i.e., if
and only if −logD pi is an integer for all i).
□
Deﬁnition
A probability distribution is called D-adic if each of the
probabilities is equal to D−n for some n. Thus, we have equality in the
theorem if and only if the distribution of X is D-adic.
The preceding proof also indicates a procedure for ﬁnding an optimal
code: Find the D-adic distribution that is closest (in the relative entropy
sense) to the distribution of X. This distribution provides the set of code-
word lengths. Construct the code by choosing the ﬁrst available node as
in the proof of the Kraft inequality. We then have an optimal code for X.
However, this procedure is not easy, since the search for the closest
D-adic distribution is not obvious. In the next section we give a good
suboptimal procedure (Shannon–Fano coding). In Section 5.6 we describe
a simple procedure (Huffman coding) for actually ﬁnding the optimal
code.
5.4
BOUNDS ON THE OPTIMAL CODE LENGTH
We now demonstrate a code that achieves an expected description length
L within 1 bit of the lower bound; that is,
H(X) ≤L < H(X) + 1.
(5.27)
Recall the setup of Section 5.3: We wish to minimize L =  pili sub-
ject to the constraint that l1, l2, . . . , lm are integers and  D−li ≤1. We
proved that the optimal codeword lengths can be found by ﬁnding the
D-adic probability distribution closest to the distribution of X in relative
entropy, that is, by ﬁnding the D-adic r (ri = D−li/ 
j D−lj ) minimizing
L −HD = D(p||r) −log

D−li

≥0.
(5.28)
The choice of word lengths li = logD
1
pi yields L = H. Since logD
1
pi
may not equal an integer, we round it up to give integer word-length
assignments,
li =

logD
1
pi

,
(5.29)


## PDF page 139

5.4
BOUNDS ON THE OPTIMAL CODE LENGTH
113
where ⌈x⌉is the smallest integer ≥x. These lengths satisfy the Kraft
inequality since

D−⌈log 1
pi ⌉≤

D−log 1
pi =

pi = 1.
(5.30)
This choice of codeword lengths satisﬁes
logD
1
pi
≤li < logD
1
pi
+ 1.
(5.31)
Multiplying by pi and summing over i, we obtain
HD(X) ≤L < HD(X) + 1.
(5.32)
Since an optimal code can only be better than this code, we have the
following theorem.
Theorem 5.4.1
Let l∗
1, l∗
2, . . . , l∗
m be optimal codeword lengths for a
source distribution p and a D-ary alphabet, and let L∗be the associated
expected length of an optimal code (L∗=  pil∗
i ). Then
HD(X) ≤L∗< HD(X) + 1.
(5.33)
Proof:
Let li = ⌈logD
1
pi ⌉. Then li satisﬁes the Kraft inequality and from
(5.32) we have
HD(X) ≤L =

pili < HD(X) + 1.
(5.34)
But since L∗, the expected length of the optimal code, is less than L =
 pili,
and
since
L∗≥HD
from
Theorem 5.3.1,
we
have
the
theorem.
□
In Theorem 5.4.1 there is an overhead that is at most 1 bit, due to the
fact that log 1
pi is not always an integer. We can reduce the overhead per
symbol by spreading it out over many symbols. With this in mind, let us
consider a system in which we send a sequence of n symbols from X.
The symbols are assumed to be drawn i.i.d. according to p(x). We can
consider these n symbols to be a supersymbol from the alphabet Xn.
Deﬁne Ln to be the expected codeword length per input symbol, that
is, if l(x1, x2, . . . , xn) is the length of the binary
codeword associated


## PDF page 140

114
DATA COMPRESSION
with (x1, x2, . . . , xn) (for the rest of this section, we assume that D = 2,
for simplicity), then
Ln = 1
n

p(x1, x2, . . . , xn)l(x1, x2, . . . , xn) = 1
nEl(X1, X2, . . . , Xn).
(5.35)
We can now apply the bounds derived above to the code:
H(X1, X2, . . . , Xn) ≤El(X1, X2, . . . , Xn) < H(X1, X2, . . . , Xn) + 1.
(5.36)
Since
X1, X2, . . . , Xn
are
i.i.d.,
H(X1, X2, . . . , Xn) =  H(Xi) =
nH(X). Dividing (5.36) by n, we obtain
H(X) ≤Ln < H(X) + 1
n.
(5.37)
Hence, by using large block lengths we can achieve an expected code-
length per symbol arbitrarily close to the entropy.
We can use the same argument for a sequence of symbols from a
stochastic process that is not necessarily i.i.d. In this case, we still have
the bound
H(X1, X2, . . . , Xn) ≤El(X1, X2, . . . , Xn) < H(X1, X2, . . . , Xn) + 1.
(5.38)
Dividing by n again and deﬁning Ln to be the expected description length
per symbol, we obtain
H(X1, X2, . . . , Xn)
n
≤Ln < H(X1, X2, . . . , Xn)
n
+ 1
n.
(5.39)
If the stochastic process is stationary, then H(X1, X2, . . . , Xn)/n →
H(X), and the expected description length tends to the entropy rate as
n →∞. Thus, we have the following theorem:
Theorem 5.4.2
The minimum expected codeword length per symbol sat-
isﬁes
H(X1, X2, . . . , Xn)
n
≤L∗
n < H(X1, X2, . . . , Xn)
n
+ 1
n.
(5.40)
Moreover, if X1, X2, . . . , Xn is a stationary stochastic process,
L∗
n →H(X),
(5.41)
where H(X) is the entropy rate of the process.


## PDF page 141

5.5
KRAFT INEQUALITY FOR UNIQUELY DECODABLE CODES
115
This theorem provides another justiﬁcation for the deﬁnition of entropy
rate—it is the expected number of bits per symbol required to describe
the process.
Finally, we ask what happens to the expected description length if the
code is designed for the wrong distribution. For example, the wrong dis-
tribution may be the best estimate that we can make of the unknown true
distribution. We consider the Shannon code assignment l(x) =
	
log
1
q(x)

designed for the probability mass function q(x). Suppose that the true
probability mass function is p(x). Thus, we will not achieve expected
length L ≈H(p) = − p(x) log p(x). We now show that the increase
in expected description length due to the incorrect distribution is the rel-
ative entropy D(p||q). Thus, D(p||q) has a concrete interpretation as the
increase in descriptive complexity due to incorrect information.
Theorem 5.4.3
(Wrong code)
The expected length under p(x) of the
code assignment l(x) =
	
log
1
q(x)

satisﬁes
H(p) + D(p||q) ≤Epl(X) < H(p) + D(p||q) + 1.
(5.42)
Proof:
The expected codelength is
El(X) =

x
p(x)

log
1
q(x)

(5.43)
<

x
p(x)

log
1
q(x) + 1

(5.44)
=

x
p(x) log p(x)
q(x)
1
p(x) + 1
(5.45)
=

x
p(x) log p(x)
q(x) +

x
p(x) log
1
p(x) + 1
(5.46)
= D(p||q) + H(p) + 1.
(5.47)
The lower bound can be derived similarly.
□
Thus, believing that the distribution is q(x) when the true distribution
is p(x) incurs a penalty of D(p||q) in the average description length.
5.5
KRAFT INEQUALITY FOR UNIQUELY DECODABLE CODES
We have proved that any instantaneous code must satisfy the Kraft inequal-
ity. The class of uniquely decodable codes is larger than the class of


## PDF page 142

116
DATA COMPRESSION
instantaneous codes, so one expects to achieve a lower expected codeword
length if L is minimized over all uniquely decodable codes. In this section
we prove that the class of uniquely decodable codes does not offer any
further possibilities for the set of codeword lengths than do instantaneous
codes. We now give Karush’s elegant proof of the following theorem.
Theorem 5.5.1
(McMillan)
The codeword lengths of any uniquely
decodable D-ary code must satisfy the Kraft inequality

D−li ≤1.
(5.48)
Conversely, given a set of codeword lengths that satisfy this inequality, it
is possible to construct a uniquely decodable code with these codeword
lengths.
Proof:
Consider Ck, the kth extension of the code (i.e., the code formed
by the concatenation of k repetitions of the given uniquely decodable code
C). By the deﬁnition of unique decodability, the kth extension of the code
is nonsingular. Since there are only Dn different D-ary strings of length n,
unique decodability implies that the number of code sequences of length
n in the kth extension of the code must be no greater than Dn. We now
use this observation to prove the Kraft inequality.
Let the codeword lengths of the symbols x ∈X be denoted by l(x).
For the extension code, the length of the code sequence is
l(x1, x2, . . . , xk) =
k

i=1
l(xi).
(5.49)
The inequality that we wish to prove is

x∈X
D−l(x) ≤1.
(5.50)
The trick is to consider the kth power of this quantity. Thus,

x∈X
D−l(x)
k
=

x1∈X

x2∈X
· · ·

xk∈X
D−l(x1)D−l(x2) · · · D−l(xk)
(5.51)
=

x1,x2,...,xk∈X k
D−l(x1)D−l(x2) · · · D−l(xk)
(5.52)
=

xk∈X k
D−l(xk),
(5.53)


## PDF page 143

5.5
KRAFT INEQUALITY FOR UNIQUELY DECODABLE CODES
117
by (5.49). We now gather the terms by word lengths to obtain

xk∈X k
D−l(xk) =
klmax

m=1
a(m)D−m,
(5.54)
where lmax is the maximum codeword length and a(m) is the number
of source sequences xk mapping into codewords of length m. But the
code is uniquely decodable, so there is at most one sequence mapping
into each code m-sequence and there are at most Dm code m-sequences.
Thus, a(m) ≤Dm, and we have

x∈X
D−l(x)
k
=
klmax

m=1
a(m)D−m
(5.55)
≤
klmax

m=1
DmD−m
(5.56)
= klmax
(5.57)
and hence

j
D−lj ≤(klmax)1/k .
(5.58)
Since this inequality is true for all k, it is true in the limit as k →∞.
Since (klmax)1/k →1, we have

j
D−lj ≤1,
(5.59)
which is the Kraft inequality.
Conversely, given any set of l1, l2, . . . , lm satisfying the Kraft inequal-
ity, we can construct an instantaneous code as proved in Section 5.2. Since
every instantaneous code is uniquely decodable, we have also constructed
a uniquely decodable code.
□
Corollary
A uniquely decodable code for an inﬁnite source alphabet X
also satisﬁes the Kraft inequality.
Proof:
The point at which the preceding proof breaks down for inﬁnite
|X| is at (5.58), since for an inﬁnite code lmax is inﬁnite. But there is a


## PDF page 144

118
DATA COMPRESSION
simple ﬁx to the proof. Any subset of a uniquely decodable code is also
uniquely decodable; thus, any ﬁnite subset of the inﬁnite set of codewords
satisﬁes the Kraft inequality. Hence,
∞

i=1
D−li = lim
N→∞
N

i=1
D−li ≤1.
(5.60)
Given a set of word lengths l1, l2, . . . that satisfy the Kraft inequality, we
can construct an instantaneous code as in Section 5.4. Since instantaneous
codes are uniquely decodable, we have constructed a uniquely decodable
code with an inﬁnite number of codewords. So the McMillan theorem
also applies to inﬁnite alphabets.
□
The theorem implies a rather surprising result—that the class of
uniquely decodable codes does not offer any further choices for the set
of codeword lengths than the class of preﬁx codes. The set of achievable
codeword lengths is the same for uniquely decodable and instantaneous
codes. Hence, the bounds derived on the optimal codeword lengths con-
tinue to hold even when we expand the class of allowed codes to the class
of all uniquely decodable codes.
5.6
HUFFMAN CODES
An optimal (shortest expected length) preﬁx code for a given distribution
can be constructed by a simple algorithm discovered by Huffman [283].
We will prove that any other code for the same alphabet cannot have a
lower expected length than the code constructed by the algorithm. Before
we give any formal proofs, let us introduce Huffman codes with some
examples.
Example 5.6.1
Consider a random variable X taking values in the set
X = {1, 2, 3, 4, 5} with probabilities 0.25, 0.25, 0.2, 0.15, 0.15, respec-
tively. We expect the optimal binary code for X to have the longest
codewords assigned to the symbols 4 and 5. These two lengths must be
equal, since otherwise we can delete a bit from the longer codeword and
still have a preﬁx code, but with a shorter expected length. In general,
we can construct a code in which the two longest codewords differ only
in the last bit. For this code, we can combine the symbols 4 and 5 into
a single source symbol, with a probability assignment 0.30. Proceeding
this way, combining the two least likely symbols into one symbol until
we are ﬁnally left with only one symbol, and then assigning codewords
to the symbols, we obtain the following table:


