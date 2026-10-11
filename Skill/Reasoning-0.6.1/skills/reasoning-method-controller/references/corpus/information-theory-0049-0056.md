# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 49

2.5
CHAIN RULES FOR ENTROPY, RELATIVE ENTROPY, MUTUAL INFORMATION
23
= H(X1) + H(X2|X1) + H(X3|X2, X1),
(2.51)
...
H(X1, X2, . . . , Xn) = H(X1) + H(X2|X1) + · · · + H(Xn|Xn−1, . . . , X1)
(2.52)
=
n

i=1
H(Xi|Xi−1, . . . , X1).
□
(2.53)
Alternative Proof:
We write p(x1, . . . , xn) = n
i=1 p(xi|xi−1, . . . , x1)
and evaluate
H(X1, X2, . . . , Xn)
= −

x1,x2,...,xn
p(x1, x2, . . . , xn) log p(x1, x2, . . . , xn)
(2.54)
= −

x1,x2,...,xn
p(x1, x2, . . . , xn) log
n

i=1
p(xi|xi−1, . . . , x1)
(2.55)
= −

x1,x2,...,xn
n

i=1
p(x1, x2, . . . , xn) log p(xi|xi−1, . . . , x1)
(2.56)
= −
n

i=1

x1,x2,...,xn
p(x1, x2, . . . , xn) log p(xi|xi−1, . . . , x1)
(2.57)
= −
n

i=1

x1,x2,...,xi
p(x1, x2, . . . , xi) log p(xi|xi−1, . . . , x1)
(2.58)
=
n

i=1
H(Xi|Xi−1, . . . , X1).
□
(2.59)
We now deﬁne the conditional mutual information as the reduction in
the uncertainty of X due to knowledge of Y when Z is given.
Deﬁnition
The conditional mutual information of random variables X
and Y given Z is deﬁned by
I (X; Y|Z) = H(X|Z) −H(X|Y, Z)
(2.60)
= Ep(x,y,z) log
p(X, Y|Z)
p(X|Z)p(Y|Z).
(2.61)
Mutual information also satisﬁes a chain rule.


## PDF page 50

24
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Theorem 2.5.2
(Chain rule for information)
I (X1, X2, . . . , Xn; Y) =
n

i=1
I (Xi; Y|Xi−1, Xi−2, . . . , X1).
(2.62)
Proof
I (X1, X2, . . . , Xn; Y)
= H(X1, X2, . . . , Xn) −H(X1, X2, . . . , Xn|Y)
(2.63)
=
n

i=1
H(Xi|Xi−1, . . . , X1) −
n

i=1
H(Xi|Xi−1, . . . , X1, Y)
=
n

i=1
I (Xi; Y|X1, X2, . . . , Xi−1).
□
(2.64)
We deﬁne a conditional version of the relative entropy.
Deﬁnition
For joint probability mass functions p(x, y) and q(x, y), the
conditional relative entropy D(p(y|x)||q(y|x)) is the average of the rela-
tive entropies between the conditional probability mass functions p(y|x)
and q(y|x) averaged over the probability mass function p(x). More pre-
cisely,
D(p(y|x)||q(y|x)) =

x
p(x)

y
p(y|x) log p(y|x)
q(y|x)
(2.65)
= Ep(x,y) log p(Y|X)
q(Y|X) .
(2.66)
The notation for conditional relative entropy is not explicit since it omits
mention of the distribution p(x) of the conditioning random variable.
However, it is normally understood from the context.
The relative entropy between two joint distributions on a pair of ran-
dom variables can be expanded as the sum of a relative entropy and a
conditional relative entropy. The chain rule for relative entropy is used in
Section 4.4 to prove a version of the second law of thermodynamics.
Theorem 2.5.3
(Chain rule for relative entropy)
D(p(x, y)||q(x, y)) = D(p(x)||q(x)) + D(p(y|x)||q(y|x)).
(2.67)


## PDF page 51

2.6
JENSEN’S INEQUALITY AND ITS CONSEQUENCES
25
Proof
D(p(x, y)||q(x, y))
=

x

y
p(x, y) log p(x, y)
q(x, y)
(2.68)
=

x

y
p(x, y) log p(x)p(y|x)
q(x)q(y|x)
(2.69)
=

x

y
p(x, y) log p(x)
q(x) +

x

y
p(x, y) log p(y|x)
q(y|x)
(2.70)
= D(p(x)||q(x)) + D(p(y|x)||q(y|x)).
□
(2.71)
2.6
JENSEN’S INEQUALITY AND ITS CONSEQUENCES
In this section we prove some simple properties of the quantities deﬁned
earlier. We begin with the properties of convex functions.
Deﬁnition
A function f (x) is said to be convex over an interval (a, b)
if for every x1, x2 ∈(a, b) and 0 ≤λ ≤1,
f (λx1 + (1 −λ)x2) ≤λf (x1) + (1 −λ)f (x2).
(2.72)
A function f is said to be strictly convex if equality holds only if λ = 0
or λ = 1.
Deﬁnition
A function f is concave if −f is convex. A function is
convex if it always lies below any chord. A function is concave if it
always lies above any chord.
Examples of convex functions include x2, |x|, ex, x log x (for x ≥
0), and so on. Examples of concave functions include log x and √x for
x ≥0. Figure 2.3 shows some examples of convex and concave functions.
Note that linear functions ax + b are both convex and concave. Convexity
underlies many of the basic properties of information-theoretic quantities
such as entropy and mutual information. Before we prove some of these
properties, we derive some simple results for convex functions.
Theorem 2.6.1
If the function f has a second derivative that is non-
negative (positive) over an interval, the function is convex (strictly convex)
over that interval.


## PDF page 52

26
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
(a)
(b)
FIGURE 2.3. Examples of (a) convex and (b) concave functions.
Proof:
We use the Taylor series expansion of the function around x0:
f (x) = f (x0) + f ′(x0)(x −x0) + f ′′(x∗)
2
(x −x0)2,
(2.73)
where x∗lies between x0 and x. By hypothesis, f ′′(x∗) ≥0, and thus
the last term is nonnegative for all x.
We let x0 = λx1 + (1 −λ)x2 and take x = x1, to obtain
f (x1) ≥f (x0) + f ′(x0)((1 −λ)(x1 −x2)).
(2.74)
Similarly, taking x = x2, we obtain
f (x2) ≥f (x0) + f ′(x0)(λ(x2 −x1)).
(2.75)
Multiplying (2.74) by λ and (2.75) by 1 −λ and adding, we obtain (2.72).
The proof for strict convexity proceeds along the same lines.
□
Theorem 2.6.1 allows us immediately to verify the strict convexity of
x2, ex, and x log x for x ≥0, and the strict concavity of log x and √x for
x ≥0.
Let E denote expectation. Thus, EX = 
x∈X p(x)x in the discrete
case and EX =

xf (x) dx in the continuous case.


## PDF page 53

2.6
JENSEN’S INEQUALITY AND ITS CONSEQUENCES
27
The next inequality is one of the most widely used in mathematics and
one that underlies many of the basic results in information theory.
Theorem 2.6.2
(Jensen’s inequality)
If f is a convex function and
X is a random variable,
Ef (X) ≥f (EX).
(2.76)
Moreover, if f is strictly convex, the equality in (2.76) implies that
X = EX with probability 1 (i.e., X is a constant).
Proof:
We prove this for discrete distributions by induction on the num-
ber of mass points. The proof of conditions for equality when f is strictly
convex is left to the reader.
For a two-mass-point distribution, the inequality becomes
p1f (x1) + p2f (x2) ≥f (p1x1 + p2x2),
(2.77)
which follows directly from the deﬁnition of convex functions. Suppose
that the theorem is true for distributions with k −1 mass points. Then
writing p′
i = pi/(1 −pk) for i = 1, 2, . . . , k −1, we have
k

i=1
pif (xi) = pkf (xk) + (1 −pk)
k−1

i=1
p′
if (xi)
(2.78)
≥pkf (xk) + (1 −pk)f
	k−1

i=1
p′
ixi

(2.79)
≥f
	
pkxk + (1 −pk)
k−1

i=1
p′
ixi

(2.80)
= f
	 k

i=1
pixi

,
(2.81)
where the ﬁrst inequality follows from the induction hypothesis and the
second follows from the deﬁnition of convexity.
The proof can be extended to continuous distributions by continuity
arguments.
□
We now use these results to prove some of the properties of entropy and
relative entropy. The following theorem is of fundamental importance.


## PDF page 54

28
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Theorem 2.6.3
(Information inequality)
Let p(x), q(x), x ∈X, be
two probability mass functions. Then
D(p||q) ≥0
(2.82)
with equality if and only if p(x) = q(x) for all x.
Proof:
Let A = {x : p(x) > 0} be the support set of p(x). Then
−D(p||q) = −

x∈A
p(x) log p(x)
q(x)
(2.83)
=

x∈A
p(x) log q(x)
p(x)
(2.84)
≤log

x∈A
p(x)q(x)
p(x)
(2.85)
= log

x∈A
q(x)
(2.86)
≤log

x∈X
q(x)
(2.87)
= log 1
(2.88)
= 0,
(2.89)
where (2.85) follows from Jensen’s inequality. Since log t is a strictly
concave function of t, we have equality in (2.85) if and only if q(x)/p(x)
is constant everywhere [i.e., q(x) = cp(x) for all x]. Thus, 
x∈A q(x) =
c 
x∈A p(x) = c. We have equality in (2.87) only if 
x∈A q(x) = 
x∈X
q(x) = 1, which implies that c = 1. Hence, we have D(p||q) = 0 if and
only if p(x) = q(x) for all x.
□
Corollary
(Nonnegativity of mutual information)
For any two random
variables, X, Y,
I (X; Y) ≥0,
(2.90)
with equality if and only if X and Y are independent.
Proof:
I (X; Y) = D(p(x, y)||p(x)p(y)) ≥0, with equality if and only
if p(x, y) = p(x)p(y) (i.e., X and Y are independent).
□


## PDF page 55

2.6
JENSEN’S INEQUALITY AND ITS CONSEQUENCES
29
Corollary
D(p(y|x)||q(y|x)) ≥0,
(2.91)
with equality if and only if p(y|x) = q(y|x) for all y and x such that
p(x) > 0.
Corollary
I (X; Y|Z) ≥0,
(2.92)
with equality if and only if X and Y are conditionally independent given Z.
We now show that the uniform distribution over the range X is the
maximum entropy distribution over this range. It follows that any random
variable with this range has an entropy no greater than log |X|.
Theorem 2.6.4
H(X) ≤log |X|, where |X| denotes the number of ele-
ments in the range of X, with equality if and only X has a uniform distri-
bution over X.
Proof:
Let u(x) =
1
|X| be the uniform probability mass function over X,
and let p(x) be the probability mass function for X. Then
D(p ∥u) =

p(x) log p(x)
u(x) = log |X| −H(X).
(2.93)
Hence by the nonnegativity of relative entropy,
0 ≤D(p ∥u) = log |X| −H(X).
□
(2.94)
Theorem 2.6.5
(Conditioning reduces entropy)(Information can’t hurt)
H(X|Y) ≤H(X)
(2.95)
with equality if and only if X and Y are independent.
Proof:
0 ≤I (X; Y) = H(X) −H(X|Y).
□
Intuitively, the theorem says that knowing another random variable Y
can only reduce the uncertainty in X. Note that this is true only on the
average. Speciﬁcally, H(X|Y = y) may be greater than or less than or
equal to H(X), but on the average H(X|Y) = 
y p(y)H(X|Y = y) ≤
H(X). For example, in a court case, speciﬁc new evidence might increase
uncertainty, but on the average evidence decreases uncertainty.


## PDF page 56

30
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Example 2.6.1
Let (X, Y) have the following joint distribution:
Then
H(X) = H(1
8, 7
8) = 0.544
bit,
H(X|Y = 1) = 0
bits,
and
H(X|Y = 2) = 1
bit.
We
calculate
H(X|Y) = 3
4H(X|Y = 1) + 1
4
H(X|Y = 2) = 0.25 bit. Thus, the uncertainty in X is increased if Y = 2
is observed and decreased if Y = 1 is observed, but uncertainty decreases
on the average.
Theorem 2.6.6
(Independence
bound
on
entropy)
Let
X1, X2, . . . , Xn be drawn according to p(x1, x2, . . . , xn). Then
H(X1, X2, . . . , Xn) ≤
n

i=1
H(Xi)
(2.96)
with equality if and only if the Xi are independent.
Proof:
By the chain rule for entropies,
H(X1, X2, . . . , Xn) =
n

i=1
H(Xi|Xi−1, . . . , X1)
(2.97)
≤
n

i=1
H(Xi),
(2.98)
where the inequality follows directly from Theorem 2.6.5. We have equal-
ity if and only if Xi is independent of Xi−1, . . . , X1 for all i (i.e., if and
only if the Xi’s are independent).
□
2.7
LOG SUM INEQUALITY AND ITS APPLICATIONS
We now prove a simple consequence of the concavity of the logarithm,
which will be used to prove some concavity results for the entropy.


