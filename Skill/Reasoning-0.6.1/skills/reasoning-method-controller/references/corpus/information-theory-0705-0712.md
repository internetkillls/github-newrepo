# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 705

17.9
INEQUALITIES FOR DETERMINANTS
679
The general theorem uniﬁes the entropy power inequality and the
Brunn–Minkowski inequality and introduces a continuum of new
inequalities that lie between the entropy power inequality and the
Brunn–Minkowski inequality. This further strengthens the analogy
between entropy power and volume.
17.9
INEQUALITIES FOR DETERMINANTS
Throughout the remainder of this chapter, we assume that K is a nonneg-
ative deﬁnite symmetric n × n matrix. Let |K| denote the determinant of
K.
We ﬁrst give an information-theoretic proof of a result due to Ky Fan
[199].
Theorem 17.9.1
log |K| is concave.
Proof:
Let X1 and X2 be normally distributed n-vectors, Xi ∼N(0, Ki),
i = 1, 2. Let the random variable θ have the distribution
Pr{θ = 1} = λ,
(17.111)
Pr{θ = 2} = 1 −λ
(17.112)
for some 0 ≤λ ≤1. Let θ, X1, and X2 be independent, and let Z =
Xθ. Then Z has covariance KZ = λK1 + (1 −λ)K2. However, Z will
not be multivariate normal. By ﬁrst using Theorem 17.2.3, followed by
Theorem 17.2.1, we have
1
2 log(2πe)n|λK1 + (1 −λ)K2| ≥h(Z)
(17.113)
≥h(Z|θ)
(17.114)
= λ1
2 log(2πe)n|K1|
+ (1 −λ)1
2 log(2πe)n|K2|.
Thus,
|λK1 + (1 −λ)K2| ≥|K1|λ|K2|1−λ,
(17.115)
as desired.
□
We now give Hadamard’s inequality using an information-theoretic
proof [128].


## PDF page 706

680
INEQUALITIES IN INFORMATION THEORY
Theorem 17.9.2
(Hadamard)
|K| ≤Kii, with equality iff Kij =
0, i ̸= j.
Proof:
Let X ∼N(0, K). Then
1
2 log(2πe)n|K| = h(X1, X2, . . . , Xn) ≤

h(Xi) =
n

i=1
1
2 log 2πe|Kii|,
(17.116)
with equality iff X1, X2, . . . , Xn are independent (i.e., Kij = 0, i ̸= j).□
We now prove a generalization of Hadamard’s inequality due to Szasz
[391]. Let K(i1, i2, . . . , ik) be the k × k principal submatrix of K formed
by the rows and columns with indices i1, i2, . . . , ik.
Theorem 17.9.3
(Szasz)
If K is a positive deﬁnite n × n matrix and
Pk denotes the product of the determinants of all the principal k-rowed
minors of K, that is,
Pk =

1≤i1<i2<···<ik≤n
|K(i1, i2, . . . , ik)|,
(17.117)
then
P1 ≥P
1
(n−1
1 )
2
≥P
1
(n−1
2 )
3
≥· · · ≥Pn.
(17.118)
Proof:
Let X ∼N(0, K). Then the theorem follows directly from
Theorem 17.6.1, with the identiﬁcation h(n)
k
=
1
2n(n−1
k−1) log Pk + 1
2 log 2πe.
□
We can also prove a related theorem.
Theorem 17.9.4
Let K be a positive deﬁnite n × n matrix and let
S(n)
k
= 1
n
k
	

1≤i1<i2<···<ik≤n
|K(i1, i2, . . . , ik)|
1
k .
(17.119)
Then
1
ntr(K) = S(n)
1
≥S(n)
2
≥· · · ≥S(n)
n
= |K|
1
n .
(17.120)
Proof:
This follows directly from the corollary to Theorem 17.6.1, with
the identiﬁcation t(n)
k
= (2πe)S(n)
k
and r = 2.
□


## PDF page 707

17.9
INEQUALITIES FOR DETERMINANTS
681
Theorem 17.9.5
Let
Qk =


S:|S|=k
|K|
|K(Sc)|


1
k(n
k)
.
(17.121)
Then
 n

i=1
σ 2
i
 1
n
= Q1 ≤Q2 ≤· · · ≤Qn−1 ≤Qn = |K|
1
n .
(17.122)
Proof:
The theorem follows immediately from Theorem 17.6.3 and the
identiﬁcation
h(X(S)|X(Sc)) = 1
2 log(2πe)k
|K|
|K(Sc)|.
□
(17.123)
The outermost inequality, Q1 ≤Qn, can be rewritten as
|K| ≥
n

i=1
σ 2
i ,
(17.124)
where
σ 2
i =
|K|
|K(1, 2 . . . , i −1, i + 1, . . . , n)|
(17.125)
is the minimum mean-squared error in the linear prediction of Xi from
the remaining X’s. Thus, σ 2
i is the conditional variance of Xi given the
remaining Xj’s if X1, X2, . . . , Xn are jointly normal. Combining this with
Hadamard’s inequality gives upper and lower bounds on the determinant
of a positive deﬁnite matrix.
Corollary

i
Kii ≥|K| ≥

i
σ 2
i .
(17.126)
Hence, the determinant of a covariance matrix lies between the product
of the unconditional variances Kii of the random variables Xi and the
product of the conditional variances σ 2
i .
We now prove a property of Toeplitz matrices, which are important as
the covariance matrices of stationary random processes. A Toeplitz matrix
K is characterized by the property that Kij = Krs if |i −j| = |r −s|.
Let Kk denote the principal minor K(1, 2, . . . , k). For such a matrix, the
following property can be proved easily from the properties of the entropy
function.


## PDF page 708

682
INEQUALITIES IN INFORMATION THEORY
Theorem 17.9.6
If the positive deﬁnite n × n matrix K is Toeplitz, then
|K1| ≥|K2|
1
2 ≥· · · ≥|Kn−1|
1
(n−1) ≥|Kn|
1
n
(17.127)
and |Kk|/|Kk−1| is decreasing in k, and
lim
n→∞|Kn|
1
n = lim
n→∞
|Kn|
|Kn−1|.
(17.128)
Proof:
Let (X1, X2, . . . , Xn) ∼N(0, Kn). We observe that
h(Xk|Xk−1, . . . , X1) = h(Xk) −h(Xk−1)
(17.129)
= 1
2 log(2πe) |Kk|
|Kk−1|.
(17.130)
Thus, the monotonicity of |Kk|/|Kk−1| follows from the monotonocity of
h(Xk|Xk−1, . . . , X1), which follows from
h(Xk|Xk−1, . . . , X1) = h(Xk+1|Xk, . . . , X2)
(17.131)
≥h(Xk+1|Xk, . . . , X2, X1),
(17.132)
where the equality follows from the Toeplitz assumption and the inequality
from the fact that conditioning reduces entropy. Since h(Xk|Xk−1, . . . , X1)
is decreasing, it follows that the running averages
1
kh(X1, . . . , Xk) = 1
k
k

i=1
h(Xi|Xi−1, . . . , X1)
(17.133)
are decreasing in k. Then (17.127) follows from h(X1, X2, . . . , Xk) =
1
2 log(2πe)k|Kk|.
□
Finally, since h(Xn|Xn−1, . . . , X1) is a decreasing sequence, it has a
limit. Hence by the theorem of the Ces´aro mean,
lim
n→∞
h(X1, X2, . . . , Xn)
n
= lim
n→∞
1
n
n

k=1
h(Xk|Xk−1, . . . , X1)
= lim
n→∞h(Xn|Xn−1, . . . , X1).
(17.134)


## PDF page 709

17.10
INEQUALITIES FOR RATIOS OF DETERMINANTS
683
Translating this to determinants, one obtains
lim
n→∞|Kn|
1
n = lim
n→∞
|Kn|
|Kn−1|.
(17.135)
Theorem 17.9.7
(Minkowski inequality [390])
|K1 + K2|1/n ≥|K1|1/n + |K2|1/n.
(17.136)
Proof:
Let X1, X2 be independent with Xi ∼N(0, Ki). Noting that X1 +
X2 ∼N(0, K1 + K2) and using the entropy power inequality (Theorem
17.7.3) yields
(2πe)|K1 + K2|1/n = 2
2
nh(X1 + X2)
(17.137)
≥2
2
nh(X1) + 2
2
nh(X2)
(17.138)
= (2πe)|K1|1/n + (2πe)|K2|1/n.
□(17.139)
17.10
INEQUALITIES FOR RATIOS OF DETERMINANTS
We now prove similar inequalities for ratios of determinants. Before devel-
oping the next theorem, we make an observation about minimum mean-
squared-error linear prediction. If (X1, X2, . . . , Xn) ∼N(0, Kn), we know
that the conditional density of Xn given (X1, X2, . . . , Xn−1) is univariate
normal with mean linear in X1, X2, . . . , Xn−1 and conditional variance
σ 2
n. Here σ 2
n is the minimum mean squared error E(Xn −ˆXn)2 over all
linear estimators ˆXn based on X1, X2, . . . , Xn−1.
Lemma 17.10.1
σ 2
n = |Kn|/|Kn−1|.
Proof:
Using the conditional normality of Xn, we have
1
2 log 2πeσ 2
n = h(Xn|X1, X2, . . . , Xn−1)
(17.140)
= h(X1, X2, . . . , Xn) −h(X1, X2, . . . , Xn−1) (17.141)
= 1
2 log(2πe)n|Kn| −1
2 log(2πe)n−1|Kn−1|
(17.142)
= 1
2 log 2πe|Kn|/|Kn−1|.
□
(17.143)


## PDF page 710

684
INEQUALITIES IN INFORMATION THEORY
Minimization of σ 2
n over a set of allowed covariance matrices {Kn} is
aided by the following theorem. Such problems arise in maximum entropy
spectral density estimation.
Theorem 17.10.1
(Bergstrøm
[42])
log(|Kn|/|Kn−p|)
is
concave
in Kn.
Proof:
We remark that Theorem 17.9.1 cannot be used because
log(|Kn|/|Kn−p|) is the difference of two concave functions. Let Z = Xθ,
where X1 ∼N(0, Sn), X2 ∼N(0, Tn), Pr{θ = 1} = λ = 1 −Pr{θ = 2},
and let X1, X2, θ be independent. The covariance matrix Kn of Z is
given by
Kn = λSn + (1 −λ)Tn.
(17.144)
The following chain of inequalities proves the theorem:
λ1
2 log(2πe)p|Sn|/|Sn−p| + (1 −λ)1
2 log(2πe)p|Tn|/|Tn−p|
(a)
= λh(X1,n, X1,n−1, . . . , X1,n−p+1|X1,1, . . . , X1,n−p)
+ (1 −λ)h(X2,n, X2,n−1, . . . , X2,n−p+1|X2,1, . . . , X2,n−p)
(17.145)
= h(Zn, Zn−1, . . . , Zn−p+1|Z1, . . . , Zn−p, θ)
(17.146)
(b)
≤h(Zn, Zn−1, . . . , Zn−p+1|Z1, . . . , Zn−p)
(17.147)
(c)
≤1
2 log(2πe)p |Kn|
|Kn−p|,
(17.148)
where
(a) follows
from
h(Xn, Xn−1, . . . , Xn−p+1|X1, . . . , Xn−p) =
h(X1, . . . , Xn) −h(X1, . . . , Xn−p), (b) follows from the conditioning
lemma, and (c) follows from a conditional version of Theorem 17.2.3. □
Theorem 17.10.2
(Bergstrøm [42])
|Kn|/|Kn−1| is concave in Kn.
Proof:
Again we use the properties of Gaussian random variables. Let
us assume that we have two independent Gaussian random n-vectors,
X ∼N(0, An) and Y ∼N(0, Bn). Let Z = X + Y. Then
1
2 log 2πe
|An + Bn|
|An−1 + Bn−1|
(a)
= h(Zn|Zn−1, Zn−2, . . . , Z1)
(17.149)


## PDF page 711

17.10
INEQUALITIES FOR RATIOS OF DETERMINANTS
685
(b)
≥h(Zn|Zn−1, Zn−2, . . . , Z1, Xn−1, Xn−2, . . . , X1, Yn−1, Yn−2, . . . , Y1)
(17.150)
(c)
= h(Xn + Yn|Xn−1, Xn−2, . . . , X1, Yn−1, Yn−2, . . . , Y1)
(17.151)
(d)
= E 1
2 log

2πe Var(Xn + Yn|Xn−1, Xn−2, . . . , X1, Yn−1,
Yn−2, . . . , Y1)

(17.152)
(e)
= E 1
2 log

2πe(Var(Xn|Xn−1, Xn−2, . . . , X1)
+ Var(Yn|Yn−1, Yn−2, . . . , Y1))

(17.153)
(f)= E 1
2 log

2πe

 |An|
|An−1| + |Bn|
|Bn−1|

(17.154)
= 1
2 log

2πe

 |An|
|An−1| + |Bn|
|Bn−1|

,
(17.155)
where
(a) follows from Lemma 17.10.1
(b) follows from the fact that the conditioning decreases entropy
(c) follows from the fact that Z is a function of X and Y
(d) follows since Xn + Yn is Gaussian conditioned on X1, X2, . . . ,
Xn−1, Y1, Y2, . . . , Yn−1, and hence we can express its entropy in
terms of its variance
(e) follows from the independence of Xn and Yn conditioned on the
past X1, X2, . . . , Xn−1, Y1, Y2, . . . , Yn−1
(f) follows from the fact that for a set of jointly Gaussian random
variables, the conditional variance is constant, independent of the
conditioning variables (Lemma 17.10.1)
Setting A = λS and B = λT , we obtain
|λSn + λTn|
|λSn−1 + λTn−1| ≥λ |Sn|
|Sn−1| + λ |Tn|
|Tn−1|
(17.156)
(i.e., |Kn|/|Kn−1| is concave). Simple examples show that |Kn|/
|Kn−p| is not necessarily concave for p ≥2.
□
A number of other determinant inequalities can be proved by these
techniques. A few of them are given as problems.


## PDF page 712

686
INEQUALITIES IN INFORMATION THEORY
OVERALL SUMMARY
Entropy. H(X) = − p(x) log p(x).
Relative entropy. D(p||q) =  p(x) log p(x)
q(x).
Mutual information. I (X; Y) =  p(x, y) log
p(x,y)
p(x)p(y).
Information inequality. D(p||q) ≥0.
Asymptotic
equipartition
property. −1
n log p(X1, X2, . . . , Xn) →
H(X).
Data compression. H(X) ≤L∗< H(X) + 1.
Kolmogorov complexity. K(x) = minU(p)=x l(p).
Universal probability. log
1
PU (x) ≈K(x).
Channel capacity. C = maxp(x) I (X; Y).
Data transmission
• R < C: Asymptotically error-free communication possible
• R > C: Asymptotically error-free communication not possible
Gaussian channel capacity. C = 1
2 log(1 + P
N ).
Rate distortion. R(D) = min I (X; ˆX) over all p(ˆx|x) such that
Ep(x)p(ˆx|x)d(X, ˆX) ≤D.
Growth rate for investment. W ∗= maxb∗E log btX.
PROBLEMS
17.1
Sum of positive deﬁnite matrices.
For any two positive deﬁnite
matrices, K1 and K2, show that |K1 + K2| ≥|K1|.


