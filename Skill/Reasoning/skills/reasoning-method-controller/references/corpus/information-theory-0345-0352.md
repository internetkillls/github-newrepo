# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 345

10.5
ACHIEVABILITY OF THE RATE DISTORTION FUNCTION
319
Deﬁnition
Let p(x, ˆx) be a joint probability distribution on X × ˆX and
let d(x, ˆx) be a distortion measure on X × ˆX. For any ϵ > 0, a pair of
sequences (xn, ˆxn) is said to be distortion ϵ-typical or simply distortion
typical if
−1
n log p(xn) −H(X)
 < ϵ
(10.72)
−1
n log p(ˆxn) −H( ˆX)
 < ϵ
(10.73)
−1
n log p(xn, ˆxn) −H(X, ˆX)
 < ϵ
(10.74)
|d(xn, ˆxn) −Ed(X, ˆX)| < ϵ.
(10.75)
The set of distortion typical sequences is called the distortion typical set
and is denoted A(n)
d,ϵ.
Note that this is the deﬁnition of the jointly typical set (Section 7.6)
with the additional constraint that the distortion be close to the expected
value. Hence, the distortion typical set is a subset of the jointly typical
set (i.e., A(n)
d,ϵ ⊂A(n)
ϵ ). If (Xi, ˆXi) are drawn i.i.d ∼p(x, ˆx), the distortion
between two random sequences
d(Xn, ˆXn) = 1
n
n

i=1
d(Xi, ˆXi)
(10.76)
is an average of i.i.d. random variables, and the law of large numbers
implies that it is close to its expected value with high probability. Hence
we have the following lemma.
Lemma 10.5.1
Let (Xi, ˆXi) be drawn i.i.d. ∼p(x, ˆx). Then Pr(A(n)
d,ϵ) →
1 as n →∞.
Proof:
The sums in the four conditions in the deﬁnition of A(n)
d,ϵ are
all normalized sums of i.i.d random variables and hence, by the law of
large numbers, tend to their respective expected values with probability 1.
Hence the set of sequences satisfying all four conditions has probability
tending to 1 as n →∞.
□
The following lemma is a direct consequence of the deﬁnition of the
distortion typical set.


## PDF page 346

320
RATE DISTORTION THEORY
Lemma 10.5.2
For all (xn, ˆxn) ∈A(n)
d,ϵ,
p(ˆxn) ≥p(ˆxn|xn)2−n(I(X; ˆX)+3ϵ).
(10.77)
Proof:
Using the deﬁnition of A(n)
d,ϵ, we can bound the probabilities
p(xn), p(ˆxn) and p(xn, ˆxn) for all (xn, ˆxn) ∈A(n)
d,ϵ, and hence
p(ˆxn|xn) = p(xn, ˆxn)
p(xn)
(10.78)
= p(ˆxn) p(xn, ˆxn)
p(xn)p(ˆxn)
(10.79)
≤p(ˆxn)
2−n(H(X, ˆX)−ϵ)
2−n(H(X)+ϵ)2−n(H( ˆX)+ϵ)
(10.80)
= p(ˆxn)2n(I(X; ˆX)+3ϵ),
(10.81)
and the lemma follows immediately.
□
We also need the following interesting inequality.
Lemma 10.5.3
For 0 ≤x, y ≤1, n > 0,
(1 −xy)n ≤1 −x + e−yn.
(10.82)
Proof:
Let f (y) = e−y −1 + y. Then f (0) = 0 and f ′(y) = −e−y +
1 > 0 for y > 0, and hence f (y) > 0 for y > 0. Hence for 0 ≤y ≤1,
we have 1 −y ≤e−y, and raising this to the nth power, we obtain
(1 −y)n ≤e−yn.
(10.83)
Thus, the lemma is satisﬁed for x = 1. By examination, it is clear that
the inequality is also satisﬁed for x = 0. By differentiation, it is easy
to see that gy(x) = (1 −xy)n is a convex function of x, and hence for
0 ≤x ≤1, we have
(1 −xy)n = gy(x)
(10.84)
≤(1 −x)gy(0) + xgy(1)
(10.85)
= (1 −x)1 + x(1 −y)n
(10.86)
≤1 −x + xe−yn
(10.87)
≤1 −x + e−yn.
□
(10.88)
We use the preceding proof to prove the achievability of Theorem 10.2.1.


## PDF page 347

10.5
ACHIEVABILITY OF THE RATE DISTORTION FUNCTION
321
Proof:
(Achievability in Theorem 10.2.1). Let X1, X2, . . . , Xn be drawn
i.i.d. ∼p(x) and let d(x, ˆx) be a bounded distortion measure for this
source. Let the rate distortion function for this source be R(D). Then for
any D, and any R > R(D), we will show that the rate distortion pair
(R, D) is achievable by proving the existence of a sequence of rate dis-
tortion codes with rate R and asymptotic distortion D. Fix p(ˆx|x), where
p(ˆx|x) achieves equality in (10.53). Thus, I (X; ˆX) = R(D). Calculate
p(ˆx) = 
x p(x)p(ˆx|x). Choose δ > 0. We will prove the existence of a
rate distortion code with rate R and distortion less than or equal to D + δ.
Generation of codebook: Randomly generate a rate distortion codebook
C consisting of 2nR sequences ˆXn drawn i.i.d. ∼n
i=1 p(ˆxi). Index these
codewords by w ∈{1, 2, . . . , 2nR}. Reveal this codebook to the encoder
and decoder.
Encoding: Encode Xn by w if there exists a w such that (Xn, ˆXn(w)) ∈
A(n)
d,ϵ, the distortion typical set. If there is more than one such w, send the
least. If there is no such w, let w = 1. Thus, nR bits sufﬁce to describe
the index w of the jointly typical codeword.
Decoding: The reproduced sequence is ˆXn(w).
Calculation of distortion: As in the case of the channel coding theorem,
we calculate the expected distortion over the random choice of codebooks
C as
D = EXn,Cd(Xn, ˆXn),
(10.89)
where the expectation is over the random choice of codebooks and over
Xn.
For a ﬁxed codebook C and choice of ϵ > 0, we divide the sequences
xn ∈Xn into two categories:
• Sequences xn such that there exists a codeword ˆXn(w) that is dis-
tortion typical with xn [i.e., d(xn, ˆxn(w)) < D + ϵ]. Since the total
probability of these sequences is at most 1, these sequences contribute
at most D + ϵ to the expected distortion.
• Sequences xn such that there does not exist a codeword
ˆXn(w)
that is distortion typical with xn. Let Pe be the total probability of
these sequences. Since the distortion for any individual sequence is
bounded by dmax, these sequences contribute at most Pedmax to the
expected distortion.
Hence, we can bound the total distortion by
Ed(Xn, ˆXn(Xn)) ≤D + ϵ + Pedmax,
(10.90)


## PDF page 348

322
RATE DISTORTION THEORY
which can be made less than D + δ for an appropriate choice of ϵ if Pe is
small enough. Hence, if we show that Pe is small, the expected distortion
is close to D and the theorem is proved.
Calculation of Pe: We must bound the probability that for a random
choice of codebook C and a randomly chosen source sequence, there is
no codeword that is distortion typical with the source sequence. Let J(C)
denote the set of source sequences xn such that at least one codeword in
C is distortion typical with xn. Then
Pe =

C
P (C)

xn:xn /∈J(C)
p(xn).
(10.91)
This is the probability of all sequences not well represented by a code,
averaged over the randomly chosen code. By changing the order of sum-
mation, we can also interpret this as the probability of choosing a code-
book that does not well represent sequence xn, averaged with respect to
p(xn). Thus,
Pe =

xn
p(xn)

C:xn /∈J(C)
p(C).
(10.92)
Let us deﬁne
K(xn, ˆxn) =

1
if (xn, ˆxn) ∈A(n)
d,ϵ,
0
if (xn, ˆxn) /∈A(n)
d,ϵ.
(10.93)
The probability that a single randomly chosen codeword ˆXn does not well
represent a ﬁxed xn is
Pr((xn, ˆXn) /∈A(n)
d,ϵ) = Pr(K(xn, ˆXn) = 0) = 1 −

ˆxn
p(ˆxn)K(xn, ˆxn),
(10.94)
and therefore the probability that 2nR independently chosen codewords do
not represent xn, averaged over p(xn), is
Pe =

xn
p(xn)

C:xn /∈J(C)
p(C)
(10.95)
=

xn
p(xn)

1 −

ˆxn
p(ˆxn)K(xn, ˆxn)
2nR
.
(10.96)


## PDF page 349

10.5
ACHIEVABILITY OF THE RATE DISTORTION FUNCTION
323
We now use Lemma 10.5.2 to bound the sum within the brackets. From
Lemma 10.5.2, it follows that

ˆxn
p(ˆxn)K(xn, ˆxn) ≥

ˆxn
p(ˆxn|xn)2−n(I(X; ˆX)+3ϵ)K(xn, ˆxn),
(10.97)
and hence
Pe ≤

xn
p(xn)
	
1 −2−n(I(X; ˆX)+3ϵ) 
ˆxn
p(ˆxn|xn)K(xn, ˆxn)

2nR
.
(10.98)
We now use Lemma 10.5.3 to bound the term on the right-hand side
of (10.98) and obtain
	
1 −2−n(I(X; ˆX)+3ϵ) 
ˆxn
p(ˆxn|xn)K(xn, ˆxn)

2nR
≤1 −
ˆxn p(ˆxn|xn)K(xn, ˆxn) + e−(2−n(I (X; ˆX)+3ϵ)2nR). (10.99)
Substituting this inequality in (10.98), we obtain
Pe ≤1 −

xn

ˆxn
p(xn)p(ˆxn|xn)K(xn, ˆxn) + e−2−n(I (X; ˆX)+3ϵ)2nR.
(10.100)
The last term in the bound is equal to
e−2n(R−I (X; ˆX)−3ϵ),
(10.101)
which goes to zero exponentially fast with n if R > I (X; ˆX) + 3ϵ. Hence
if we choose p(ˆx|x) to be the conditional distribution that achieves the
minimum in the rate distortion function, then R > R(D) implies that
R > I (X; ˆX) and we can choose ϵ small enough so that the last term in
(10.100) goes to 0.
The ﬁrst two terms in (10.100) give the probability under the joint
distribution p(xn, ˆxn) that the pair of sequences is not distortion typical.
Hence, using Lemma 10.5.1, we obtain
1 −

xn

ˆxn
p(xn, ˆxn)K(xn, ˆxn) = Pr((Xn, ˆXn) /∈A(n)
d,ϵ) < ϵ
(10.102)


## PDF page 350

324
RATE DISTORTION THEORY
for n sufﬁciently large. Therefore, by an appropriate choice of ϵ and n,
we can make Pe as small as we like.
So, for any choice of δ > 0, there exists an ϵ and n such that over all
randomly chosen rate R codes of block length n, the expected distortion
is less than D + δ. Hence, there must exist at least one code C∗with this
rate and block length with average distortion less than D + δ. Since δ was
arbitrary, we have shown that (R, D) is achievable if R > R(D).
□
We have proved the existence of a rate distortion code with an expected
distortion close to D and a rate close to R(D). The similarities between
the random coding proof of the rate distortion theorem and the random
coding proof of the channel coding theorem are now evident. We will
explore the parallels further by considering the Gaussian example, which
provides some geometric insight into the problem. It turns out that channel
coding is sphere packing and rate distortion coding is sphere covering.
Channel coding for the Gaussian channel. Consider a Gaussian channel,
Yi = Xi + Zi, where the Zi are i.i.d. ∼N(0, N) and there is a power
constraint P on the power per symbol of the transmitted codeword. Con-
sider a sequence of n transmissions. The power constraint implies that
the transmitted sequence lies within a sphere of radius
√
nP in Rn. The
coding problem is equivalent to ﬁnding a set of 2nR sequences within
this sphere such that the probability of any of them being mistaken for
any other is small—the spheres of radius
√
nN around each of them are
almost disjoint. This corresponds to ﬁlling a sphere of radius √n(P + N)
with spheres of radius
√
nN. One would expect that the largest number
of spheres that could be ﬁt would be the ratio of their volumes, or, equiv-
alently, the nth power of the ratio of their radii. Thus, if M is the number
of codewords that can be transmitted efﬁciently, we have
M ≤(√n(P + N))n
(
√
nN)n
=
P + N
N
 n
2
.
(10.103)
The results of the channel coding theorem show that it is possible to do
this efﬁciently for large n; it is possible to ﬁnd approximately
2nC =
P + N
N
 n
2
(10.104)
codewords such that the noise spheres around them are almost disjoint
(the total volume of their intersection is arbitrarily small).


## PDF page 351

10.6
STRONGLY TYPICAL SEQUENCES AND RATE DISTORTION
325
Rate distortion for the Gaussian source. Consider a Gaussian source of
variance σ 2. A (2nR, n) rate distortion code for this source with distortion
D is a set of 2nR sequences in Rn such that most source sequences of
length n (all those that lie within a sphere of radius
√
nσ 2) are within a
distance
√
nD of some codeword. Again, by the sphere-packing argument,
it is clear that the minimum number of codewords required is
2nR(D) =
σ 2
D
 n
2
.
(10.105)
The rate distortion theorem shows that this minimum rate is asymptotically
achievable (i.e., that there exists a collection of spheres of radius
√
nD
that cover the space except for a set of arbitrarily small probability).
The above geometric arguments also enable us to transform a good
code for channel transmission into a good code for rate distortion. In both
cases, the essential idea is to ﬁll the space of source sequences: In channel
transmission, we want to ﬁnd the largest set of codewords that have a large
minimum distance between codewords, whereas in rate distortion, we wish
to ﬁnd the smallest set of codewords that covers the entire space. If we
have any set that meets the sphere packing bound for one, it will meet the
sphere packing bound for the other. In the Gaussian case, choosing the
codewords to be Gaussian with the appropriate variance is asymptotically
optimal for both rate distortion and channel coding.
10.6
STRONGLY TYPICAL SEQUENCES AND RATE
DISTORTION
In Section 10.5 we proved the existence of a rate distortion code of
rate R(D) with average distortion close to D. In fact, not only is the
average distortion close to D, but the total probability that the distor-
tion is greater than D + δ is close to 0. The proof of this is similar
to the proof in Section 10.5; the main difference is that we will use
strongly typical sequences rather than weakly typical sequences. This
will enable us to give an upper bound to the probability that a typical
source sequence is not well represented by a randomly chosen codeword
in (10.94). We now outline an alternative proof based on strong typical-
ity that will provide a stronger and more intuitive approach to the rate
distortion theorem.
We begin by deﬁning strong typicality and quoting a basic theorem
bounding the probability that two sequences are jointly typical. The
properties of strong typicality were introduced by Berger [53] and were


## PDF page 352

326
RATE DISTORTION THEORY
explored in detail in the book by Csisz´ar and K¨orner [149]. We will
deﬁne strong typicality (as in Chapter 11) and state a fundamental lemma
(Lemma 10.6.2).
Deﬁnition
A sequence xn ∈Xn is said to be ϵ-strongly typical with
respect to a distribution p(x) on X if:
1. For all a ∈X with p(a) > 0, we have

1
nN(a|xn) −p(a)
 < ϵ
|X|.
(10.106)
2. For all a ∈X with p(a) = 0, N(a|xn) = 0.
N(a|xn) is the number of occurrences of the symbol a in the sequence
xn.
The set of sequences xn ∈Xn such that xn is strongly typical is called
the strongly typical set and is denoted A∗(n)
ϵ
(X) or A∗(n)
ϵ
when the random
variable is understood from the context.
Deﬁnition
A pair of sequences (xn, yn) ∈Xn × Yn is said to be ϵ-
strongly typical with respect to a distribution p(x, y) on X × Y if:
1. For all (a, b) ∈X × Y with p(a, b) > 0, we have

1
nN(a, b|xn, yn) −p(a, b)
 <
ϵ
|X||Y|.
(10.107)
2. For all (a, b) ∈X × Y with p(a, b) = 0, N(a, b|xn, yn) = 0.
N(a, b|xn, yn) is the number of occurrences of the pair (a, b) in the pair
of sequences (xn, yn).
The set of sequences (xn, yn) ∈Xn × Yn such that (xn, yn) is strongly
typical is called the strongly typical set and is denoted A∗(n)
ϵ
(X, Y) or
A∗(n)
ϵ
. From the deﬁnition, it follows that if (xn, yn) ∈A∗(n)
ϵ
(X, Y), then
xn ∈A∗(n)
ϵ
(X). From the strong law of large numbers, the following
lemma is immediate.
Lemma 10.6.1
Let (Xi, Yi) be drawn i.i.d. ∼p(x, y). Then Pr(A∗(n)
ϵ
)
→1 as n →∞.
We will use one basic result, which bounds the probability that an
independently drawn sequence will be seen as jointly strongly typical


