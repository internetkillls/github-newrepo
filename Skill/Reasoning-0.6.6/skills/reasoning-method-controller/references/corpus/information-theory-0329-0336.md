# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 329

10.2
DEFINITIONS
303
a point within each region to represent the sample. But it is no longer
immediately obvious what the representation regions and the reconstruc-
tion points should be. We can, however, state two simple properties of
optimal regions and reconstruction points for the quantization of a single
random variable:
• Given a set { ˆX(w)} of reconstruction points, the distortion is mini-
mized by mapping a source random variable X to the representation
ˆX(w) that is closest to it. The set of regions of X deﬁned by this
mapping is called a Voronoi or Dirichlet partition deﬁned by the
reconstruction points.
• The reconstruction points should minimize the conditional expected
distortion over their respective assignment regions.
These two properties enable us to construct a simple algorithm to ﬁnd a
“good” quantizer: We start with a set of reconstruction points, ﬁnd the opti-
mal set of reconstruction regions (which are the nearest-neighbor regions
with respect to the distortion measure), then ﬁnd the optimal reconstruc-
tion points for these regions (the centroids of these regions if the distortion
is squared error), and then repeat the iteration for this new set of recon-
struction points. The expected distortion is decreased at each stage in the
algorithm, so the algorithm will converge to a local minimum of the dis-
tortion. This algorithm is called the Lloyd algorithm [363] (for real-valued
random variables) or the generalized Lloyd algorithm [358] (for vector-
valued random variables) and is frequently used to design quantization
systems.
Instead of quantizing a single random variable, let us assume that we
are given a set of n i.i.d. random variables drawn according to a Gaussian
distribution. These random variables are to be represented using nR bits.
Since the source is i.i.d., the symbols are independent, and it may appear
that the representation of each element is an independent problem to be
treated separately. But this is not true, as the results on rate distortion
theory will show. We will represent the entire sequence by a single index
taking 2nR values. This treatment of entire sequences at once achieves a
lower distortion for the same rate than independent quantization of the
individual samples.
10.2
DEFINITIONS
Assume that we have a source that produces a sequence X1, X2, . . . , Xn
i.i.d. ∼p(x), x ∈X. For the proofs in this chapter, we assume that the


## PDF page 330

304
RATE DISTORTION THEORY
Encoder
Decoder
Xn
Xn
fn(Xn)
{1,2,...,2nR}
∋
^
FIGURE 10.2. Rate distortion encoder and decoder.
alphabet is ﬁnite, but most of the proofs can be extended to continuous
random variables. The encoder describes the source sequence Xn by an
index fn(Xn) ∈{1, 2, . . . , 2nR}. The decoder represents Xn by an estimate
ˆXn ∈ˆX, as illustrated in Figure 10.2.
Deﬁnition
A distortion function or distortion measure is a mapping
d : X × ˆX →R+
(10.2)
from the set of source alphabet-reproduction alphabet pairs into the set of
nonnegative real numbers. The distortion d(x, ˆx) is a measure of the cost
of representing the symbol x by the symbol ˆx.
Deﬁnition
A distortion measure is said to be bounded if the maximum
value of the distortion is ﬁnite:
dmax
def
=
max
x∈X,ˆx∈ˆX
d(x, ˆx) < ∞.
(10.3)
In most cases, the reproduction alphabet ˆX is the same as the source
alphabet X.
Examples of common distortion functions are
• Hamming (probability of error) distortion. The Hamming distortion
is given by
d(x, ˆx) =

0
if x = ˆx
1
if x ̸= ˆx,
(10.4)
which results in a probability of error distortion, since Ed(X, ˆX) =
Pr(X ̸= ˆX).


## PDF page 331

10.2
DEFINITIONS
305
• Squared-error distortion. The squared-error distortion,
d(x, ˆx) = (x −ˆx)2,
(10.5)
is the most popular distortion measure used for continuous alphabets.
Its advantages are its simplicity and its relationship to least-squares
prediction. But in applications such as image and speech coding,
various authors have pointed out that the mean-squared error is not an
appropriate measure of distortion for human observers. For example,
there is a large squared-error distortion between a speech waveform
and another version of the same waveform slightly shifted in time,
even though both would sound the same to a human observer.
Many alternatives have been proposed; a popular measure of distortion
in speech coding is the Itakura–Saito distance, which is the relative entropy
between multivariate normal processes. In image coding, however, there is
at present no real alternative to using the mean-squared error as the distortion
measure.
The distortion measure is deﬁned on a symbol-by-symbol basis. We
extend the deﬁnition to sequences by using the following deﬁnition:
Deﬁnition
The distortion between sequences xn and ˆxn is deﬁned by
d(xn, ˆxn) = 1
n
n

i=1
d(xi, ˆxi).
(10.6)
So the distortion for a sequence is the average of the per symbol dis-
tortion of the elements of the sequence. This is not the only reasonable
deﬁnition. For example, one may want to measure the distortion between
two sequences by the maximum of the per symbol distortions. The the-
ory derived below does not apply directly to this more general distortion
measure.
Deﬁnition
A (2nR, n)-rate distortion code consists of an encoding func-
tion,
fn : Xn →{1, 2, . . . , 2nR},
(10.7)
and a decoding (reproduction) function,
gn : {1, 2, . . . , 2nR} →
ˆXn.
(10.8)


## PDF page 332

306
RATE DISTORTION THEORY
The distortion associated with the (2nR, n) code is deﬁned as
D = Ed(Xn, gn(fn(Xn))),
(10.9)
where the expectation is with respect to the probability distribution on X:
D =

xn
p(xn)d(xn, gn(fn(xn))).
(10.10)
The set of n-tuples gn(1), gn(2), . . . , gn(2nR), denoted by
ˆXn(1), . . . ,
ˆXn(2nR), constitutes the codebook, and f −1
n (1), . . . , f −1
n (2nR) are the
associated assignment regions.
Many terms are used to describe the replacement of Xn by its quantized
version ˆXn(w). It is common to refer to ˆXn as the vector quantiza-
tion, reproduction, reconstruction, representation, source code, or estimate
of Xn.
Deﬁnition
A rate distortion pair (R, D) is said to be achievable if
there exists a sequence of (2nR, n)-rate distortion codes (fn, gn) with
limn→∞Ed(Xn, gn(fn(Xn))) ≤D.
Deﬁnition
The rate distortion region for a source is the closure of the
set of achievable rate distortion pairs (R, D).
Deﬁnition
The rate distortion function R(D) is the inﬁmum of rates R
such that (R, D) is in the rate distortion region of the source for a given
distortion D.
Deﬁnition
The distortion rate function D(R) is the inﬁmum of all dis-
tortions D such that (R, D) is in the rate distortion region of the source
for a given rate R.
The distortion rate function deﬁnes another way of looking at the
boundary of the rate distortion region. We will in general use the rate
distortion function rather than the distortion rate function to describe this
boundary, although the two approaches are equivalent.
We now deﬁne a mathematical function of the source, which we call
the information rate distortion function. The main result of this chapter
is the proof that the information rate distortion function is equal to the
rate distortion function deﬁned above (i.e., it is the inﬁmum of rates that
achieve a particular distortion).


## PDF page 333

10.3
CALCULATION OF THE RATE DISTORTION FUNCTION
307
Deﬁnition
The information rate distortion function R(I)(D) for a source
X with distortion measure d(x, ˆx) is deﬁned as
R(I)(D) =
min
p(ˆx|x):
(x,ˆx) p(x)p(ˆx|x)d(x,ˆx)≤D I (X; ˆX),
(10.11)
where the minimization is over all conditional distributions p(ˆx|x) for
which the joint distribution p(x, ˆx) = p(x)p(ˆx|x) satisﬁes the expected
distortion constraint.
Paralleling the discussion of channel capacity in Chapter 7, we initially
consider the properties of the information rate distortion function and
calculate it for some simple sources and distortion measures. Later we
prove that we can actually achieve this function (i.e., there exist codes with
rate R(I)(D) with distortion D). We also prove a converse establishing
that R ≥R(I)(D) for any code that achieves distortion D.
The main theorem of rate distortion theory can now be stated as follows:
Theorem 10.2.1
The rate distortion function for an i.i.d. source X
with distribution p(x) and bounded distortion function d(x, ˆx) is equal to
the associated information rate distortion function. Thus,
R(D) = R(I)(D) =
min
p(ˆx|x):
(x,ˆx) p(x)p(ˆx|x)d(x,ˆx)≤D I (X; ˆX)
(10.12)
is the minimum achievable rate at distortion D.
This theorem shows that the operational deﬁnition of the rate distortion
function is equal to the information deﬁnition. Hence we will use R(D)
from now on to denote both deﬁnitions of the rate distortion function.
Before coming to the proof of the theorem, we calculate the information
rate distortion function for some simple sources and distortions.
10.3
CALCULATION OF THE RATE DISTORTION FUNCTION
10.3.1
Binary Source
We now ﬁnd the description rate R(D) required to describe a Bernoulli(p)
source with an expected proportion of errors less than or equal to D.
Theorem 10.3.1
The rate distortion function for a Bernoulli(p) source
with Hamming distortion is given by
R(D) =

H(p) −H(D),
0 ≤D ≤min{p, 1 −p},
0,
D > min{p, 1 −p}.
(10.13)


## PDF page 334

308
RATE DISTORTION THEORY
Proof:
Consider a binary source X ∼Bernoulli(p) with a Hamming
distortion measure. Without loss of generality, we may assume that p < 1
2.
We wish to calculate the rate distortion function,
R(D) =
min
p(ˆx|x):
(x,ˆx) p(x)p(ˆx|x)d(x,ˆx)≤D I (X; ˆX).
(10.14)
Let ⊕denote modulo 2 addition. Thus, X ⊕ˆX = 1 is equivalent to X ̸=
ˆX. We do not minimize I (X; ˆX) directly; instead, we ﬁnd a lower bound
and then show that this lower bound is achievable. For any joint distribu-
tion satisfying the distortion constraint, we have
I (X; ˆX) = H(X) −H(X| ˆX)
(10.15)
= H(p) −H(X ⊕ˆX| ˆX)
(10.16)
≥H(p) −H(X ⊕ˆX)
(10.17)
≥H(p) −H(D),
(10.18)
since Pr(X ̸= ˆX) ≤D and H(D) increases with D for D ≤1
2. Thus,
R(D) ≥H(p) −H(D).
(10.19)
We now show that the lower bound is actually the rate distortion function
by ﬁnding a joint distribution that meets the distortion constraint and
has I (X; ˆX) = R(D). For 0 ≤D ≤p, we can achieve the value of the
rate distortion function in (10.19) by choosing (X, ˆX) to have the joint
distribution given by the binary symmetric channel shown in Figure 10.3.
1 −D
1 −p −D
1 − 2D
1 −D
D
D
X
0
1
0
1 −p
p
1
p −D
1 − 2D
X
^
FIGURE 10.3. Joint distribution for binary source.


## PDF page 335

10.3
CALCULATION OF THE RATE DISTORTION FUNCTION
309
We choose the distribution of ˆX at the input of the channel so that the
output distribution of X is the speciﬁed distribution. Let r = Pr( ˆX = 1).
Then choose r so that
r(1 −D) + (1 −r)D = p,
(10.20)
or
r = p −D
1 −2D .
(10.21)
If D ≤p ≤1
2, then Pr( ˆX = 1) ≥0 and Pr( ˆX = 0) ≥0. We then have
I (X; ˆX) = H(X) −H(X| ˆX) = H(p) −H(D),
(10.22)
and the expected distortion is Pr(X ̸= ˆX) = D.
If D ≥p, we can achieve R(D) = 0 by letting ˆX = 0 with probability
1. In this case, I (X; ˆX) = 0 and D = p. Similarly, if D ≥1 −p, we can
achieve R(D) = 0 by setting ˆX = 1 with probability 1. Hence, the rate
distortion function for a binary source is
R(D) =

H(p) −H(D),
0 ≤D ≤min{p, 1 −p},
0,
D > min{p, 1 −p}.
(10.23)
This function is illustrated in Figure 10.4.
□
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
D
R(D)
FIGURE 10.4. Rate distortion function for a Bernoulli ( 1
2) source.


## PDF page 336

310
RATE DISTORTION THEORY
The above calculations may seem entirely unmotivated. Why should
minimizing mutual information have anything to do with quantization?
The answer to this question must wait until we prove Theorem 10.2.1.
10.3.2
Gaussian Source
Although Theorem 10.2.1 is proved only for discrete sources with a
bounded distortion measure, it can also be proved for well-behaved contin-
uous sources and unbounded distortion measures. Assuming this general
theorem, we calculate the rate distortion function for a Gaussian source
with squared-error distortion.
Theorem 10.3.2
The rate distortion function for a N(0, σ 2) source with
squared-error distortion is
R(D) =



1
2 log σ 2
D ,
0 ≤D ≤σ 2,
0,
D > σ 2.
(10.24)
Proof:
Let X be ∼N(0, σ 2). By the rate distortion theorem extended
to continuous alphabets, we have
R(D) =
min
f (ˆx|x):E( ˆX−X)2≤D
I (X; ˆX).
(10.25)
As in the preceding example, we ﬁrst ﬁnd a lower bound for the rate
distortion function and then prove that this is achievable. Since E(X −
ˆX)2 ≤D, we observe that
I (X; ˆX) = h(X) −h(X| ˆX)
(10.26)
= 1
2 log(2πe)σ 2 −h(X −ˆX| ˆX)
(10.27)
≥1
2 log(2πe)σ 2 −h(X −ˆX)
(10.28)
≥1
2 log(2πe)σ 2 −h(N(0, E(X −ˆX)2))
(10.29)
= 1
2 log(2πe)σ 2 −1
2 log(2πe)E(X −ˆX)2
(10.30)
≥1
2 log(2πe)σ 2 −1
2 log(2πe)D
(10.31)
= 1
2 log σ 2
D ,
(10.32)


