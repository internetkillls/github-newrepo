# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 273

8.3
RELATION OF DIFFERENTIAL ENTROPY TO DISCRETE ENTROPY
247
an interpretation of the differential entropy: It is the logarithm of the
equivalent side length of the smallest set that contains most of the prob-
ability. Hence low entropy implies that the random variable is conﬁned
to a small effective volume and high entropy indicates that the random
variable is widely dispersed.
Note. Just as the entropy is related to the volume of the typical set, there
is a quantity called Fisher information which is related to the surface
area of the typical set. We discuss Fisher information in more detail in
Sections 11.10 and 17.8.
8.3
RELATION OF DIFFERENTIAL ENTROPY TO DISCRETE
ENTROPY
Consider a random variable X with density f (x) illustrated in Figure 8.1.
Suppose that we divide the range of X into bins of length . Let us
assume that the density is continuous within the bins. Then, by the mean
value theorem, there exists a value xi within each bin such that
f (xi) =
 (i+1)
i
f (x) dx.
(8.23)
Consider the quantized random variable X, which is deﬁned by
X = xi
if i ≤X < (i + 1).
(8.24)
∆
f(x)
x
FIGURE 8.1. Quantization of a continuous random variable.


## PDF page 274

248
DIFFERENTIAL ENTROPY
Then the probability that X = xi is
pi =
 (i+1)
i
f (x) dx = f (xi).
(8.25)
The entropy of the quantized version is
H(X) = −
∞

−∞
pi log pi
(8.26)
= −
∞

−∞
f (xi) log(f (xi))
(8.27)
= −

f (xi) log f (xi) −

f (xi) log 
(8.28)
= −

f (xi) log f (xi) −log ,
(8.29)
since  f (xi) =

f (x) = 1. If f (x) log f (x) is Riemann integrable (a
condition to ensure that the limit is well deﬁned [556]), the ﬁrst term in
(8.29) approaches the integral of −f (x) log f (x) as  →0 by deﬁnition
of Riemann integrability. This proves the following.
Theorem 8.3.1
If the density f (x) of the random variable X is Rie-
mann integrable, then
H(X) + log  →h(f ) = h(X),
as  →0.
(8.30)
Thus, the entropy of an n-bit quantization of a continuous random vari-
able X is approximately h(X) + n.
Example 8.3.1
1. If X has a uniform distribution on [0, 1] and we let  = 2−n,
then h = 0, H(X) = n, and n bits sufﬁce to describe X to n
bit accuracy.
2. If X is uniformly distributed on [0, 1
8], the ﬁrst 3 bits to the right
of the decimal point must be 0. To describe X to n-bit accuracy
requires only n −3 bits, which agrees with h(X) = −3.
3. If X ∼N(0, σ 2) with σ 2 = 100, describing X to n bit accuracy
would require on the average n + 1
2 log(2πeσ 2) = n + 5.37 bits.


## PDF page 275

8.4
JOINT AND CONDITIONAL DIFFERENTIAL ENTROPY
249
In general, h(X) + n is the number of bits on the average required to
describe X to n-bit accuracy.
The differential entropy of a discrete random variable can be considered
to be −∞. Note that 2−∞= 0, agreeing with the idea that the volume of
the support set of a discrete random variable is zero.
8.4
JOINT AND CONDITIONAL DIFFERENTIAL ENTROPY
As in the discrete case, we can extend the deﬁnition of differential entropy
of a single random variable to several random variables.
Deﬁnition
The differential entropy of a set X1, X2, . . . , Xn of random
variables with density f (x1, x2, . . . , xn) is deﬁned as
h(X1, X2, . . . , Xn) = −

f (xn) log f (xn) dxn.
(8.31)
Deﬁnition
If X, Y have a joint density function f (x, y), we can deﬁne
the conditional differential entropy h(X|Y) as
h(X|Y) = −

f (x, y) log f (x|y) dx dy.
(8.32)
Since in general f (x|y) = f (x, y)/f (y), we can also write
h(X|Y) = h(X, Y) −h(Y).
(8.33)
But we must be careful if any of the differential entropies are inﬁnite.
The next entropy evaluation is used frequently in the text.
Theorem 8.4.1
(Entropy of a multivariate normal distribution)
Let
X1, X2, . . . , Xn have a multivariate normal distribution with mean µ and
covariance matrix K. Then
h(X1, X2, . . . , Xn) = h(Nn(µ, K)) = 1
2 log(2πe)n|K|
bits,
(8.34)
where |K| denotes the determinant of K.


## PDF page 276

250
DIFFERENTIAL ENTROPY
Proof:
The probability density function of X1, X2, . . . , Xn is
f (x) =
1
√
2π
n
|K|
1
2
e−1
2(x−µ)T K−1(x−µ).
(8.35)
Then
h(f ) = −

f (x)

−1
2(x −µ)T K−1(x −µ) −ln
√
2π
n
|K|
1
2

dx
(8.36)
= 1
2E


i,j
(Xi −µi)

K−1
ij (Xj −µj)

+ 1
2 ln(2π)n|K| (8.37)
= 1
2E


i,j
(Xi −µi)(Xj −µj)

K−1
ij

+ 1
2 ln(2π)n|K| (8.38)
= 1
2

i,j
E[(Xj −µj)(Xi −µi)]

K−1
ij + 1
2 ln(2π)n|K|
(8.39)
= 1
2

j

i
Kji

K−1
ij + 1
2 ln(2π)n|K|
(8.40)
= 1
2

j
(KK−1)jj + 1
2 ln(2π)n|K|
(8.41)
= 1
2

j
Ijj + 1
2 ln(2π)n|K|
(8.42)
= n
2 + 1
2 ln(2π)n|K|
(8.43)
= 1
2 ln(2πe)n|K|
nats
(8.44)
= 1
2 log(2πe)n|K|
bits.
□
(8.45)
8.5
RELATIVE ENTROPY AND MUTUAL INFORMATION
We now extend the deﬁnition of two familiar quantities, D(f ||g) and
I (X; Y), to probability densities.


## PDF page 277

8.5
RELATIVE ENTROPY AND MUTUAL INFORMATION
251
Deﬁnition
The relative entropy (or Kullback–Leibler distance) D(f ||g)
between two densities f and g is deﬁned by
D(f ||g) =

f log f
g .
(8.46)
Note that D(f ||g) is ﬁnite only if the support set of f is contained in
the support set of g. [Motivated by continuity, we set 0 log 0
0 = 0.]
Deﬁnition
The mutual information I (X; Y) between two random vari-
ables with joint density f (x, y) is deﬁned as
I (X; Y) =

f (x, y) log f (x, y)
f (x)f (y) dx dy.
(8.47)
From the deﬁnition it is clear that
I (X; Y) = h(X) −h(X|Y) = h(Y) −h(Y|X) = h(X) + h(Y) −h(X, Y)
(8.48)
and
I (X; Y) = D(f (x, y)||f (x)f (y)).
(8.49)
The properties of D(f ||g) and I (X; Y) are the same as in the dis-
crete case. In particular, the mutual information between two random
variables is the limit of the mutual information between their quantized
versions, since
I (X; Y ) = H(X) −H(X|Y )
(8.50)
≈h(X) −log  −(h(X|Y) −log )
(8.51)
= I (X; Y).
(8.52)
More generally, we can deﬁne mutual information in terms of ﬁnite
partitions of the range of the random variable. Let X be the range of a
random variable X. A partition P of X is a ﬁnite collection of disjoint
sets Pi such that ∪iPi = X. The quantization of X by P (denoted [X]P)
is the discrete random variable deﬁned by
Pr([X]P = i) = Pr(X ∈Pi) =

Pi
dF(x).
(8.53)
For two random variables X and Y with partitions P and Q, we can
calculate the mutual information between the quantized versions of X
and Y using (2.28). Mutual information can now be deﬁned for arbitrary
pairs of random variables as follows:


## PDF page 278

252
DIFFERENTIAL ENTROPY
Deﬁnition
The mutual information between two random variables X
and Y is given by
I (X; Y) = sup
P,Q
I ([X]P; [Y]Q),
(8.54)
where the supremum is over all ﬁnite partitions P and Q.
This is the master deﬁnition of mutual information that always applies,
even to joint distributions with atoms, densities, and singular parts. More-
over, by continuing to reﬁne the partitions P and Q, one ﬁnds a mono-
tonically increasing sequence I ([X]P ; [Y]Q) ↗I.
By arguments similar to (8.52), we can show that this deﬁnition of
mutual information is equivalent to (8.47) for random variables that have
a density. For discrete random variables, this deﬁnition is equivalent to
the deﬁnition of mutual information in (2.28).
Example 8.5.1
(Mutual information between correlated Gaussian ran-
dom variables with correlation ρ)
Let (X, Y) ∼N(0, K), where
K =

σ 2
ρσ 2
ρσ 2
σ 2

.
(8.55)
Then h(X) = h(Y) = 1
2 log(2πe)σ 2 and h(X, Y) = 1
2 log(2πe)2|K| =
1
2 log(2πe)2σ 4(1 −ρ2), and therefore
I (X; Y) = h(X) + h(Y) −h(X, Y) = −1
2 log(1 −ρ2).
(8.56)
If ρ = 0, X and Y are independent and the mutual information is 0.
If ρ = ±1, X and Y are perfectly correlated and the mutual information
is inﬁnite.
8.6
PROPERTIES OF DIFFERENTIAL ENTROPY, RELATIVE
ENTROPY, AND MUTUAL INFORMATION
Theorem 8.6.1
D(f ||g) ≥0
(8.57)
with equality iff f = g almost everywhere (a.e.).
Proof:
Let S be the support set of f . Then
−D(f ||g) =

S
f log g
f
(8.58)
≤log

S
f g
f
(by Jensen’s inequality)
(8.59)


## PDF page 279

8.6
DIFFERENTIAL ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
253
= log

S
g
(8.60)
≤log 1 = 0.
(8.61)
We have equality iff we have equality in Jensen’s inequality, which
occurs iff f = g a.e.
□
Corollary
I (X; Y) ≥0 with equality iff X and Y are independent.
Corollary
h(X|Y) ≤h(X) with equality iff X and Y are independent.
Theorem 8.6.2
(Chain rule for differential entropy)
h(X1, X2, . . . , Xn) =
n

i=1
h(Xi|X1, X2, . . . , Xi−1).
(8.62)
Proof:
Follows directly from the deﬁnitions.
□
Corollary
h(X1, X2, . . . , Xn) ≤

h(Xi),
(8.63)
with equality iff X1, X2, . . . , Xn are independent.
Proof:
Follows directly from Theorem 8.6.2 and the corollary to Theo-
rem 8.6.1.
□
Application
(Hadamard’s inequality)
If we let X ∼N(0, K) be a mul-
tivariate normal random variable, calculating the entropy in the above
inequality gives us
|K| ≤
n

i=1
Kii,
(8.64)
which is Hadamard’s inequality. A number of determinant inequalities
can be derived in this fashion from information-theoretic inequalities
(Chapter 17).
Theorem 8.6.3
h(X + c) = h(X).
(8.65)
Translation does not change the differential entropy.
Proof:
Follows directly from the deﬁnition of differential entropy.
□


## PDF page 280

254
DIFFERENTIAL ENTROPY
Theorem 8.6.4
h(aX) = h(X) + log |a|.
(8.66)
Proof:
Let Y = aX. Then fY(y) =
1
|a|fX( y
a), and
h(aX) = −

fY(y) log fY(y) dy
(8.67)
= −

1
|a|fX
y
a

log
 1
|a|fX
y
a

dy
(8.68)
= −

fX(x) log fX(x) dx + log |a|
(8.69)
= h(X) + log |a|,
(8.70)
after a change of variables in the integral.
□
Similarly, we can prove the following corollary for vector-valued ran-
dom variables.
Corollary
h(AX) = h(X) + log |det(A)|.
(8.71)
We now show that the multivariate normal distribution maximizes the
entropy over all distributions with the same covariance.
Theorem 8.6.5
Let the random vector X ∈Rn have zero mean and
covariance K = EXXt (i.e., Kij = EXiXj, 1 ≤i, j ≤n). Then h(X) ≤
1
2 log(2πe)n|K|, with equality iff X ∼N(0, K).
Proof:
Let g(x) be any density satisfying

g(x)xixjdx = Kij for all
i, j. Let φK be the density of a N(0, K) vector as given in (8.35), where we
set µ = 0. Note that log φK(x) is a quadratic form and

xixjφK(x) dx =
Kij. Then
0 ≤D(g||φK)
(8.72)
=

g log(g/φK)
(8.73)
= −h(g) −

g log φK
(8.74)


