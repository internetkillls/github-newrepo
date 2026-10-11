# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 433

PROBLEMS
407
11.24
Fisher information for mixtures.
Let f1(x) and f0(x) be two
given probability densities. Let Z be Bernoulli(θ), where θ is
unknown. Let X ∼f1(x) if Z = 1 and X ∼f0(x) if Z = 0.
(a) Find the density fθ(x) of the observed X.
(b) Find the Fisher information J(θ).
(c) What is the Cram´er–Rao lower bound on the mean-squared
error of an unbiased estimate of θ?
(d) Can you exhibit an unbiased estimator of θ?
11.25
Bent coins.
Let {Xi} be iid ∼Q, where
Q(k) = Pr(Xi = k) =
m
k

qk(1 −q)m−k for k = 0, 1, 2, . . . , m.
Thus, the Xi’s are iid ∼Binomial(m, q). Show that as n →∞,
Pr

X1 = k

1
n
n

i=1
Xi ≥α

→P ∗(k),
where P ∗is Binomial(m, λ) (i.e., P ∗(k) =
m
k

λk(1 −λ)m−k for
some λ ∈[0, 1]). Find λ.
11.26
Conditional limiting distribution
(a) Find the exact value of
Pr

X1 = 1

1
n
n

i=1
Xi = 1
4

(11.332)
if X1, X2, . . . , are Bernoulli(2
3) and n is a multiple of 4.
(b) Now let Xiϵ{−1, 0, 1} and let X1, X2 . . . be i.i.d. uniform
over {−1, 0, +1}. Find the limit of
Pr

X1 = +1

1
n
n

i=1
X2
i = 1
2

(11.333)
for n = 2k, k →∞.


## PDF page 434

408
INFORMATION THEORY AND STATISTICS
11.27
Variational inequality.
Verify for positive random variables X
that
log EP (X) = sup
Q
!
EQ(log X) −D(Q||P )
"
,
(11.334)
where EP (X) = 
x xP (x) and D(Q||P ) = 
x Q(x) log Q(x)
P(x)
and
the
supremum
is
over
all
Q(x) ≥0,
 Q(x) = 1.
It
is
enough
to
extremize
J(Q) = EQ ln X −D(Q||P ) +
λ( Q(x) −1).
11.28
Type constraints
(a) Find constraints on the type PXn such that the sample variance
X2n −(Xn)2 ≤α,
where
X2n = 1
n
n
i=1 X2
i
and
Xn = 1
n
n
i=1 Xi.
(b) Find the exponent in the probability Qn(X2n −(Xn)2 ≤α).
You can leave the answer in parametric form.
11.29
Uniform distribution on the simplex.
Which of these methods
will generate a sample from the uniform distribution on the sim-
plex {x ∈Rn : xi ≥0,
n
i=1 xi = 1}?
(a) Let Yi be i.i.d. uniform [0, 1] with Xi = Yi/ n
j=1 Yj.
(b) Let Yi be i.i.d. exponentially distributed ∼λe−λy, y ≥0, with
Xi = Yi/ n
j=1 Yj.
(c) (Break stick into n parts) Let Y1, Y2, . . . , Yn−1 be i.i.d. uni-
form [0, 1], and let Xi be the length of the ith interval.
HISTORICAL NOTES
The method of types evolved from notions of strong typicality; some
of the ideas were used by Wolfowitz [566] to prove channel capacity
theorems. The method was fully developed by Csisz´ar and K¨orner [149],
who derived the main theorems of information theory from this viewpoint.
The method of types described in Section 11.1 follows the development
in Csisz´ar and K¨orner. The L1 lower bound on relative entropy is due to
Csisz´ar [138], Kullback [336], and Kemperman [309]. Sanov’s theorem
[455] was generalized by Csisz´ar [141] using the method of types.


## PDF page 435

CHAPTER 12
MAXIMUM ENTROPY
The temperature of a gas corresponds to the average kinetic energy of the
molecules in the gas. What can we say about the distribution of veloci-
ties in the gas at a given temperature? We know from physics that this
distribution is the maximum entropy distribution under the temperature
constraint, otherwise known as the Maxwell–Boltzmann distribution. The
maximum entropy distribution corresponds to the macrostate (as indexed
by the empirical distribution) that has the most microstates (the individual
gas velocities). Implicit in the use of maximum entropy methods in physics
is a sort of AEP which says that all microstates are equally probable.
12.1
MAXIMUM ENTROPY DISTRIBUTIONS
Consider the following problem: Maximize the entropy h(f ) over all
probability densities f satisfying
1.
f (x) ≥0, with equality outside the support set S
2.

S f (x) dx = 1
3.

S f (x)ri(x) dx = αi
for 1 ≤i ≤m.
(12.1)
Thus, f is a density on support set S meeting certain moment con-
straints α1, α2, . . . , αm.
Approach 1
( Calculus)
The differential entropy h(f ) is a concave
function over a convex set. We form the functional
J(f ) = −

f ln f + λ0

f +
m

i=1
λi

f ri
(12.2)
and “differentiate” with respect to f (x), the xth component of f , to obtain
∂J
∂f (x) = −ln f (x) −1 + λ0 +
m

i=1
λiri(x).
(12.3)
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
409


## PDF page 436

410
MAXIMUM ENTROPY
Setting this equal to zero, we obtain the form of the maximizing density
f (x) = eλ0−1+m
i=1 λiri(x),
x ∈S,
(12.4)
where λ0, λ1, . . . , λm are chosen so that f satisﬁes the constraints.
The approach using calculus only suggests the form of the density that
maximizes the entropy. To prove that this is indeed the maximum, we can
take the second variation. It is simpler to use the information inequality
D(g||f ) ≥0.
Approach 2
(Information inequality)
If g satisﬁes (12.1) and if f ∗is
of the form (12.4), then 0 ≤D(g||f ∗) = −h(g) + h(f ∗). Thus h(g) ≤
h(f ∗) for all g satisfying the constraints. We prove this in the following
theorem.
Theorem 12.1.1
(Maximum entropy distribution)
Let f ∗(x) = fλ(x)
= eλ0+m
i=1 λiri(x), x ∈S, where λ0, . . . , λm are chosen so that f ∗satisﬁes
(12.1). Then f ∗uniquely maximizes h(f ) over all probability densities f
satisfying constraints (12.1).
Proof:
Let g satisfy the constraints (12.1). Then
h(g) = −

S
g ln g
(12.5)
= −

S
g ln g
f ∗f ∗
(12.6)
= −D(g||f ∗) −

S
g ln f ∗
(12.7)
(a)
≤−

S
g ln f ∗
(12.8)
(b)
= −

S
g

λ0 +

λiri

(12.9)
(c)
= −

S
f ∗
λ0 +

λiri

(12.10)
= −

S
f ∗ln f ∗
(12.11)
= h(f ∗),
(12.12)
where (a) follows from the nonnegativity of relative entropy, (b) follows
from the deﬁnition of f ∗, and (c) follows from the fact that both f ∗
and g satisfy the constraints. Note that equality holds in (a) if and only


## PDF page 437

12.2
EXAMPLES
411
if g(x) = f ∗(x) for all x, except for a set of measure 0, thus proving
uniqueness.
□
The same approach holds for discrete entropies and for multivariate
distributions.
12.2
EXAMPLES
Example 12.2.1
(One-dimensional gas with a temperature constraint)
Let the constraints be EX = 0 and EX2 = σ 2. Then the form of the
maximizing distribution is
f (x) = eλ0+λ1x+λ2x2.
(12.13)
To ﬁnd the appropriate constants, we ﬁrst recognize that this distribution
has the same form as a normal distribution. Hence, the density that satisﬁes
the constraints and also maximizes the entropy is the N(0, σ 2) distribution:
f (x) =
1
√
2πσ 2 e−x2
2σ2 .
(12.14)
Example 12.2.2
(Dice, no constraints)
Let S = {1, 2, 3, 4, 5, 6}. The
distribution that maximizes the entropy is the uniform distribution, p(x) =
1
6 for x ∈S.
Example 12.2.3
(Dice, with EX =  ipi = α)
This important exam-
ple was used by Boltzmann. Suppose that n dice are thrown on the table
and we are told that the total number of spots showing is nα. What
proportion of the dice are showing face i, i = 1, 2, . . . , 6?
One way of going about this is to count the number of ways that
n dice can fall so that ni dice show face i. There are

n
n1, n2, . . . , n6

such ways. This is a macrostate indexed by (n1, n2, . . . , n6) corresponding
to

n
n1, n2, . . . , n6

microstates, each having probability
1
6n. To ﬁnd the
most probable macrostate, we wish to maximize

n
n1, n2, . . . , n6

under
the constraint observed on the total number of spots,
6

i=1
ini = nα.
(12.15)
Using a crude Stirling’s approximation, n! ≈( n
e)n, we ﬁnd that

n
n1, n2, . . . , n6

≈
( n
e)n
	6
i=1 ( ni
e )ni
(12.16)


## PDF page 438

412
MAXIMUM ENTROPY
=
6

i=1
 n
ni
ni
(12.17)
= e
nH
 n1
n , n2
n ,..., n6
n

.
(12.18)
Thus, maximizing

n
n1, n2, . . . , n6

under the constraint (12.15) is almost
equivalent to maximizing H(p1, p2, . . . , p6) under the constraint  ipi =
α. Using Theorem 12.1.1 under this constraint, we ﬁnd the maximum
entropy probability mass function to be
p∗
i =
eλi
6
i=1 eλi ,
(12.19)
where λ is chosen so that  ip∗
i = α. Thus, the most probable macrostate
is (np∗
1, np∗
2. . . . , np∗
6), and we expect to ﬁnd n∗
i = np∗
i dice showing
face i.
In Chapter 11 we show that the reasoning and the approximations are
essentially correct. In fact, we show that not only is the maximum entropy
macrostate the most likely, but it also contains almost all of the probability.
Speciﬁcally, for rational α,
Pr

Ni
n −p∗
i
 < ϵ, i = 1, 2, . . . , 6

n

i=1
Xi = nα

→1,
(12.20)
as n →∞along the subsequence such that nα is an integer.
Example 12.2.4
Let S = [a, b], with no other constraints. Then the
maximum entropy distribution is the uniform distribution over this range.
Example 12.2.5
S = [0, ∞) and EX = µ. Then the entropy-maxi-
mizing distribution is
f (x) = 1
µe−x
µ ,
x ≥0.
(12.21)
This problem has a physical interpretation. Consider the distribution of the
height X of molecules in the atmosphere. The average potential energy of
the molecules is ﬁxed, and the gas tends to the distribution that has the
maximum entropy subject to the constraint that E(mgX) is ﬁxed. This
is the exponential distribution with density f (x) = λe−λx, x ≥0. The
density of the atmosphere does indeed have this distribution.


## PDF page 439

12.3
ANOMALOUS MAXIMUM ENTROPY PROBLEM
413
Example 12.2.6
S = (−∞, ∞), and EX = µ. Here the maximum en-
tropy is inﬁnite, and there is no maximum entropy distribution. (Consider
normal distributions with larger and larger variances.)
Example 12.2.7
S = (−∞, ∞), EX = α1, and EX2 = α2. The maxi-
mum entropy distribution is N(α1, α2 −α2
1).
Example 12.2.8
S = Rn, EXiXj = Kij, 1 ≤i, j ≤n. This is a mul-
tivariate example, but the same analysis holds and the maximum entropy
density is of the form
f (x) = eλ0+
i,j λijxixj.
(12.22)
Since the exponent is a quadratic form, it is clear by inspection that the
density is a multivariate normal with zero mean. Since we have to satisfy
the second moment constraints, we must have a multivariate normal with
covariance Kij, and hence the density is
f (x) =
1
√
2π
n
|K|1/2
e−1
2xT K−1x,
(12.23)
which has an entropy
h(Nn(0, K)) = 1
2 log(2πe)n|K|,
(12.24)
as derived in Chapter 8.
Example 12.2.9
Suppose that we have the same constraints as in Ex-
ample 12.2.8, but EXiXj = Kij only for some restricted set of (i, j) ∈A.
For example, we might know only Kij for i = j ± 2. Then by comparing
(12.22) and (12.23), we can conclude that (K−1)ij = 0 for (i, j) ∈Ac
(i.e., the entries in the inverse of the covariance matrix are 0 when (i, j)
is outside the constraint set).
12.3
ANOMALOUS MAXIMUM ENTROPY PROBLEM
We have proved that the maximum entropy distribution subject to the
constraints

S
hi(x)f (x) dx = αi
(12.25)
is of the form
f (x) = eλ0+ λihi(x)
(12.26)
if λ0, λ1, . . . , λp satisfying the constraints (12.25) exist.


## PDF page 440

414
MAXIMUM ENTROPY
We now consider a tricky problem in which the λi cannot be chosen
to satisfy the constraints. Nonetheless, the “maximum” entropy can be
found. We consider the following problem: Maximize the entropy subject
to the constraints
 ∞
−∞
f (x) dx = 1,
(12.27)
 ∞
−∞
xf (x) dx = α1,
(12.28)
 ∞
−∞
x2f (x) dx = α2,
(12.29)
 ∞
−∞
x3f (x) dx = α3.
(12.30)
Here, the maximum entropy distribution, if it exists, must be of the form
f (x) = eλ0+λ1x+λ2x2+λ3x3.
(12.31)
But if λ3 is nonzero,
 ∞
−∞f = ∞and the density cannot be normalized.
So λ3 must be 0. But then we have four equations and only three variables,
so that in general it is not possible to choose the appropriate constants.
The method seems to have failed in this case.
The reason for the apparent failure is simple: The entropy has a least
upper bound under these constraints, but it is not possible to attain it. Con-
sider the corresponding problem with only ﬁrst and second moment con-
straints. In this case, the results of Example 12.2.1 show that the entropy-
maximizing distribution is the normal with the appropriate moments. With
the additional third moment constraint, the maximum entropy cannot be
higher. Is it possible to achieve this value?
We cannot achieve it, but we can come arbitrarily close. Consider a
normal distribution with a small “wiggle” at a very high value of x. The
moments of the new distribution are almost the same as those of the old
one, the biggest change being in the third moment. We can bring the
ﬁrst and second moments back to their original values by adding new
wiggles to balance out the changes caused by the ﬁrst. By choosing the
position of the wiggles, we can get any value of the third moment without
reducing the entropy signiﬁcantly below that of the associated normal.
Using this method, we can come arbitrarily close to the upper bound for
the maximum entropy distribution. We conclude that
sup h(f ) = h(N(0, α2 −α2
1)) = 1
2 ln 2πe(α2 −α2
1).
(12.32)


