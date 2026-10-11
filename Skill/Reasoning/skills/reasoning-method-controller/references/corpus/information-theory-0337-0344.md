# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 337

10.3
CALCULATION OF THE RATE DISTORTION FUNCTION
311
where (10.28) follows from the fact that conditioning reduces entropy and
(10.29) follows from the fact that the normal distribution maximizes the
entropy for a given second moment (Theorem 8.6.5). Hence,
R(D) ≥1
2 log σ 2
D .
(10.33)
To ﬁnd the conditional density f (ˆx|x) that achieves this lower bound,
it is usually more convenient to look at the conditional density f (x|ˆx),
which is sometimes called the test channel (thus emphasizing the duality of
rate distortion with channel capacity). As in the binary case, we construct
f (x|ˆx) to achieve equality in the bound. We choose the joint distribution
as shown in Figure 10.5. If D ≤σ 2, we choose
X = ˆX + Z,
ˆX ∼N(0, σ 2 −D),
Z ∼N(0, D),
(10.34)
where ˆX and Z are independent. For this joint distribution, we calculate
I (X; ˆX) = 1
2 log σ 2
D ,
(10.35)
and E(X −ˆX)2 = D, thus achieving the bound in (10.33). If D > σ 2, we
choose ˆX = 0 with probability 1, achieving R(D) = 0. Hence, the rate
distortion function for the Gaussian source with squared-error distortion is
R(D) =



1
2 log σ 2
D ,
0 ≤D ≤σ 2,
0,
D > σ 2,
(10.36)
as illustrated in Figure 10.6.
□
We can rewrite (10.36) to express the distortion in terms of the rate,
D(R) = σ 22−2R.
(10.37)
Z ~
(0,D)
X ~
(0, s2 −D)
^
X ~
(0,s2)
FIGURE 10.5. Joint distribution for Gaussian source.


## PDF page 338

312
RATE DISTORTION THEORY
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1.8
2
D
R(D)
FIGURE 10.6. Rate distortion function for a Gaussian source.
Each bit of description reduces the expected distortion by a factor of 4.
With a 1-bit description, the best expected square error is σ 2/4. We can
compare this with the result of simple 1-bit quantization of a N(0, σ 2)
random variable as described in Section 10.1. In this case, using the two
regions corresponding to the positive and negative real lines and repro-
duction points as the centroids of the respective regions, the expected dis-
tortion is (π−2)
π
σ 2 = 0.3633σ 2 (see Problem 10.1). As we prove later, the
rate distortion limit R(D) is achieved by considering long block lengths.
This example shows that we can achieve a lower distortion by consider-
ing several distortion problems in succession (long block lengths) than can
be achieved by considering each problem separately. This is somewhat
surprising because we are quantizing independent random variables.
10.3.3
Simultaneous Description of Independent Gaussian
Random Variables
Consider the case of representing m independent (but not identically dis-
tributed) normal random sources X1, . . . , Xm, where Xi are ∼N(0, σ 2
i ),
with squared-error distortion. Assume that we are given R bits with which
to represent this random vector. The question naturally arises as to how
we should allot these bits to the various components to minimize the
total distortion. Extending the deﬁnition of the information rate distortion


## PDF page 339

10.3
CALCULATION OF THE RATE DISTORTION FUNCTION
313
function to the vector case, we have
R(D) =
min
f (ˆxm|xm):Ed(Xm, ˆXm)≤D
I (Xm; ˆXm),
(10.38)
where d(xm, ˆxm) = m
i=1(xi −ˆxi)2. Now using the arguments in the pre-
ceding example, we have
I (Xm; ˆXm) = h(Xm) −h(Xm| ˆXm)
(10.39)
=
m

i=1
h(Xi) −
m

i=1
h(Xi|Xi−1, ˆXm)
(10.40)
≥
m

i=1
h(Xi) −
m

i=1
h(Xi| ˆXi)
(10.41)
=
m

i=1
I (Xi; ˆXi)
(10.42)
≥
m

i=1
R(Di)
(10.43)
=
m

i=1
	
1
2 log σ 2
i
Di

+
,
(10.44)
where Di = E(Xi −ˆXi)2 and (10.41) follows from the fact that condi-
tioning reduces entropy. We can achieve equality in (10.41) by choosing
f (xm|ˆxm) = m
i=1 f (xi|ˆxi) and in (10.43) by choosing the distribution of
each ˆXi ∼N(0, σ 2
i −Di), as in the preceding example. Hence, the prob-
lem of ﬁnding the rate distortion function can be reduced to the following
optimization (using nats for convenience):
R(D) =
min
 Di=D
m

i=1
max

1
2 ln σ 2
i
Di
, 0

.
(10.45)
Using Lagrange multipliers, we construct the functional
J(D) =
m

i=1
1
2 ln σ 2
i
Di
+ λ
m

i=1
Di,
(10.46)


## PDF page 340

314
RATE DISTORTION THEORY
and differentiating with respect to Di and setting equal to 0, we have
∂J
∂Di
= −1
2
1
Di
+ λ = 0
(10.47)
or
Di = λ′.
(10.48)
Hence, the optimum allotment of the bits to the various descriptions
results in an equal distortion for each random variable. This is possible if
the constant λ′ in (10.48) is less than σ 2
i for all i. As the total allowable
distortion D is increased, the constant λ′ increases until it exceeds σ 2
i
for some i. At this point the solution (10.48) is on the boundary of the
allowable region of distortions. If we increase the total distortion, we must
use the Kuhn–Tucker conditions to ﬁnd the minimum in (10.46). In this
case the Kuhn–Tucker conditions yield
∂J
∂Di
= −1
2
1
Di
+ λ,
(10.49)
where λ is chosen so that
∂J
∂Di

= 0
if Di < σ 2
i
≤0
if Di ≥σ 2
i .
(10.50)
It is easy to check that the solution to the Kuhn–Tucker equations is given
by the following theorem:
Theorem 10.3.3
(Rate distortion for a parallel Gaussian source) Let
Xi ∼N(0, σ 2
i ), i = 1, 2, . . . , m, be independent Gaussian random vari-
ables, and let the distortion measure be d(xm, ˆxm) = m
i=1(xi −ˆxi)2 .
Then the rate distortion function is given by
R(D) =
m

i=1
1
2 log σ 2
i
Di
,
(10.51)
where
Di =

λ
if λ < σ 2
i ,
σ 2
i
if λ ≥σ 2
i ,
(10.52)
where λ is chosen so that m
i=1 Di = D.


## PDF page 341

10.4
CONVERSE TO THE RATE DISTORTION THEOREM
315
s2
i
l
s2
1
s2
1
s2
2
s2
3
^
s2
4
s2
5
s2
4
^
s2
6
s2
6
^
D1
D2
D3
D4
D5
D6
X1
X2
X3
X4
X5
X6
FIGURE 10.7. Reverse water-ﬁlling for independent Gaussian random variables.
This gives rise to a kind of reverse water-ﬁlling, as illustrated in
Figure 10.7. We choose a constant λ and only describe those random vari-
ables with variances greater than λ. No bits are used to describe random
variables with variance less than λ. Summarizing, if
X ∼N(0,


σ 2
1
· · ·
0
...
...
...
0
· · ·
σ 2
m

), then ˆX ∼N(0,


ˆσ 2
1
· · ·
0
...
...
...
0
· · ·
ˆσ 2
m

),
and E(Xi −ˆXi)2 = Di, where Di = min{λ, σ 2
i }. More generally, the rate
distortion function for a multivariate normal vector can be obtained by
reverse water-ﬁlling on the eigenvalues. We can also apply the same argu-
ments to a Gaussian stochastic process. By the spectral representation
theorem, a Gaussian stochastic process can be represented as an inte-
gral of independent Gaussian processes in the various frequency bands.
Reverse water-ﬁlling on the spectrum yields the rate distortion function.
10.4
CONVERSE TO THE RATE DISTORTION THEOREM
In this section we prove the converse to Theorem 10.2.1 by showing that
we cannot achieve a distortion of less than D if we describe X at a rate
less than R(D), where
R(D) =
min
p(ˆx|x):
(x,ˆx) p(x)p(ˆx|x)d(x,ˆx)≤D I (X; ˆX).
(10.53)


## PDF page 342

316
RATE DISTORTION THEORY
The minimization is over all conditional distributions p(ˆx|x) for which
the joint distribution p(x, ˆx) = p(x)p(ˆx|x) satisﬁes the expected distor-
tion constraint. Before proving the converse, we establish some simple
properties of the information rate distortion function.
Lemma 10.4.1
(Convexity of R(D)) The rate distortion function R(D)
given in (10.53) is a nonincreasing convex function of D.
Proof:
R(D) is the minimum of the mutual information over increas-
ingly larger sets as D increases. Thus, R(D) is nonincreasing in D. To
prove that R(D) is convex, consider two rate distortion pairs, (R1, D1)
and (R2, D2), which lie on the rate distortion curve. Let the joint distribu-
tions that achieve these pairs be p1(x, ˆx) = p(x)p1(ˆx|x) and p2(x, ˆx) =
p(x)p2(ˆx|x). Consider the distribution pλ = λp1 + (1 −λ)p2. Since the
distortion is a linear function of the distribution, we have D(pλ) = λD1 +
(1 −λ)D2. Mutual information, on the other hand, is a convex function
of the conditional distribution (Theorem 2.7.4), and hence
Ipλ(X; ˆX) ≤λIp1(X; ˆX) + (1 −λ)Ip2(X; ˆX).
(10.54)
Hence, by the deﬁnition of the rate distortion function,
R(Dλ) ≤Ipλ(X; ˆX)
(10.55)
≤λIp1(X; ˆX) + (1 −λ)Ip2(X; ˆX)
(10.56)
= λR(D1) + (1 −λ)R(D2),
(10.57)
which proves that R(D) is a convex function of D.
□
The converse can now be proved.
Proof:
(Converse in Theorem 10.2.1). We must show for any source X
drawn i.i.d. ∼p(x) with distortion measure d(x, ˆx) and any (2nR, n) rate
distortion code with distortion ≤D, that the rate R of the code satis-
ﬁes R ≥R(D). In fact, we prove that R ≥R(D) even for randomized
mappings fn and gn, as long as fn takes on at most 2nR values.
Consider any (2nR, n) rate distortion code deﬁned by functions fn and
gn as given in (10.7) and (10.8). Let ˆXn = ˆXn(Xn) = gn(fn(Xn)) be the
reproduced sequence corresponding to Xn. Assume that Ed(Xn, ˆXn) ≥D


## PDF page 343

10.4
CONVERSE TO THE RATE DISTORTION THEOREM
317
for this code. Then we have the following chain of inequalities:
nR
(a)
≥H(fn(Xn))
(10.58)
(b)
≥H(fn(Xn)) −H(fn(Xn)|Xn)
(10.59)
= I (Xn; fn(Xn))
(10.60)
(c)
≥I (Xn; ˆXn)
(10.61)
= H(Xn) −H(Xn| ˆXn)
(10.62)
(d)
=
n

i=1
H(Xi) −H(Xn| ˆXn)
(10.63)
(e)
=
n

i=1
H(Xi) −
n

i=1
H(Xi| ˆXn, Xi−1, . . . , X1)
(10.64)
(f)≥
n

i=1
H(Xi) −
n

i=1
H(Xi| ˆXi)
(10.65)
=
n

i=1
I (Xi; ˆXi)
(10.66)
(g)
≥
n

i=1
R(Ed(Xi, ˆXi))
(10.67)
= n
	
1
n
n

i=1
R(Ed(Xi, ˆXi))

(10.68)
(h)
≥nR
	
1
n
n

i=1
Ed(Xi, ˆXi)

(10.69)
(i)= nR(Ed(Xn, ˆXn))
(10.70)
(j)= nR(D),
(10.71)
where
(a) follows from the fact that the range of fn is at most 2nR
(b) follows from the fact that H(fn(Xn)|Xn) ≥0


## PDF page 344

318
RATE DISTORTION THEORY
(c) follows from the data-processing inequality
(d) follows from the fact that the Xi are independent
(e) follows from the chain rule for entropy
(f) follows from the fact that conditioning reduces entropy
(g) follows from the deﬁnition of the rate distortion function
(h) follows from the convexity of the rate distortion function (Lemma
10.4.1) and Jensen’s inequality
(i) follows from the deﬁnition of distortion for blocks of length n
(j) follows from the fact that R(D) is a nonincreasing function of D and
Ed(Xn, ˆXn) ≤D
This shows that the rate R of any rate distortion code exceeds the rate
distortion function R(D) evaluated at the distortion level D = Ed(Xn, ˆXn)
achieved by that code.
□
A similar argument can be applied when the encoded source is passed
through a noisy channel and hence we have the equivalent of the source
channel separation theorem with distortion:
Theorem 10.4.1
(Source–channel separation theorem with distortion)
Let V1, V2, . . . , Vn be a ﬁnite alphabet i.i.d. source which is encoded as
a sequence of n input symbols Xn of a discrete memoryless channel with
capacity C. The output of the channel Y n is mapped onto the reconstruction
alphabet ˆV n = g(Y n). Let D = Ed(V n, ˆV n) = 1
n
n
i=1 Ed(Vi, ˆVi) be the
average distortion achieved by this combined source and channel coding
scheme. Then distortion D is achievable if and only if C > R(D).
Channel Capacity C
Vn
Vn
Yn
Xn(Vn)
^
Proof:
See Problem 10.17.
□
10.5
ACHIEVABILITY OF THE RATE DISTORTION FUNCTION
We now prove the achievability of the rate distortion function. We begin
with a modiﬁed version of the joint AEP in which we add the condition
that the pair of sequences be typical with respect to the distortion measure.


