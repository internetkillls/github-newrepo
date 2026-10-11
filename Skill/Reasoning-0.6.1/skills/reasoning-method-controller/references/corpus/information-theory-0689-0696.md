# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 689

17.3
BOUNDS ON ENTROPY AND RELATIVE ENTROPY
663
Theorem 17.2.3
(Theorem 8.6.5)
Let the random vector X ∈Rn have
zero mean and covariance K = EXXt (i.e., Kij = EXiXj, 1 ≤i, j ≤n).
Then
h(X) ≤1
2 log(2πe)n|K|
(17.20)
with equality iff X ∼N(0, K).
17.3
BOUNDS ON ENTROPY AND RELATIVE ENTROPY
In this section we revisit some of the bounds on the entropy function. The
most useful is Fano’s inequality, which is used to bound away from zero
the probability of error of the best decoder for a communication channel
at rates above capacity.
Theorem 17.3.1
(Theorem 2.10.1: Fano’s inequality)
Given two ran-
dom variables X and Y, let ˆX = g(Y) be any estimator of X given Y and
let Pe = Pr(X ̸= ˆX) be the probability of error. Then
H(Pe) + Pe log |X| ≥H(X| ˆX) ≥H(X|Y).
(17.21)
Consequently, if H(X|Y) > 0, then Pe > 0.
A similar result is given in the following lemma.
Lemma 17.3.1
(Lemma 2.10.1)
If X and X′ are i.i.d. with entropy
H(X)
Pr(X = X′) ≥2−H(X)
(17.22)
with equality if and only if X has a uniform distribution.
The continuous analog of Fano’s inequality bounds the mean-squared
error of an estimator.
Theorem 17.3.2
(Theorem 8.6.6)
Let X be a random variable with
differential entropy h(X). Let ˆX be an estimate of X, and let E(X −ˆX)2
be the expected prediction error. Then
E(X −ˆX)2 ≥
1
2πee2h(X).
(17.23)
Given side information Y and estimator ˆX(Y),
E(X −ˆX(Y))2 ≥
1
2πee2h(X|Y).
(17.24)


## PDF page 690

664
INEQUALITIES IN INFORMATION THEORY
Theorem 17.3.3
(L1 bound on entropy)
Let p and q be two proba-
bility mass functions on X such that
||p −q||1 =

x∈X
|p(x) −q(x)| ≤1
2.
(17.25)
Then
|H(p) −H(q)| ≤−||p −q||1 log ||p −q||1
|X|
.
(17.26)
Proof:
Consider the function f (t) = −t log t shown in Figure 17.1. It
can be veriﬁed by differentiation that the function f (·) is concave. Also,
f (0) = f (1) = 0. Hence the function is positive between 0 and 1. Con-
sider the chord of the function from t to t + ν (where ν ≤1
2). The
maximum absolute slope of the chord is at either end (when t = 0 or
1 −ν). Hence for 0 ≤t ≤1 −ν, we have
|f (t) −f (t + ν)| ≤max{f (ν), f (1 −ν)} = −ν log ν.
(17.27)
Let r(x) = |p(x) −q(x)|. Then
|H(p) −H(q)| =


x∈X
(−p(x) log p(x) + q(x) log q(x))

(17.28)
≤

x∈X
|(−p(x) log p(x) + q(x) log q(x))|
(17.29)
0.4
0.35
0.3
0.25
0.2
0.15
0.1
0.05
0 0
0.2
0.4
t
f(t ) = −t In t
−t Int
0.6
0.8
1
FIGURE 17.1. Function f (t) = −t ln t.


## PDF page 691

17.4
INEQUALITIES FOR TYPES
665
≤

x∈X
−r(x) log r(x)
(17.30)
= ||p −q||1

x∈X
−
r(x)
||p −q||1
log
r(x)
||p −q||1
||p −q||1
(17.31)
= −||p −q||1 log ||p −q||1 + ||p −q||1H

r(x)
||p −q||1

(17.32)
≤−||p −q||1 log ||p −q||1 + ||p −q||1 log |X|,
(17.33)
where (17.30) follows from (17.27).
□
Finally, relative entropy is stronger than the L1 norm in the following
sense:
Lemma 17.3.2
(Lemma 11.6.1)
D(p1||p2) ≥
1
2 ln 2||p1 −p2||2
1.
(17.34)
The relative entropy between two probability mass functions P (x) and
Q(x) is zero when P = Q. Around this point, the relative entropy has
a quadratic behavior, and the ﬁrst term in the Taylor series expansion of
the relative entropy D(P ||Q) around the point P = Q is the chi-squared
distance between the distributions P and Q. Let
χ2(P, Q) =

x
(P (x) −Q(x))2
Q(x)
.
(17.35)
Lemma 17.3.3
For P near Q,
D(P ∥Q) = 1
2χ2 + · · · .
(17.36)
Proof:
See Problem 11.2.
□
17.4
INEQUALITIES FOR TYPES
The method of types is a powerful tool for proving results in large devi-
ation theory and error exponents. We repeat the basic theorems.
Theorem 17.4.1
(Theorem 11.1.1)
The number of types with denom-
inator n is bounded by
|Pn| ≤(n + 1)|X|.
(17.37)


## PDF page 692

666
INEQUALITIES IN INFORMATION THEORY
Theorem 17.4.2
(Theorem 11.1.2)
If X1, X2, . . . , Xn are drawn i.i.d.
according to Q(x), the probability of xn depends only on its type and is
given by
Qn(xn) = 2−n(H(Pxn)+D(Pxn||Q)).
(17.38)
Theorem 17.4.3
(Theorem 11.1.3: Size of a type class T (P ))
For any
type P ∈Pn,
1
(n + 1)|X| 2nH(P) ≤|T (P )| ≤2nH(P).
(17.39)
Theorem 17.4.4
(Theorem 11.1.4)
For any P ∈Pn and any distribu-
tion Q, the probability of the type class T (P ) under Qn is 2−nD(P||Q) to
ﬁrst order in the exponent. More precisely,
1
(n + 1)|X| 2−nD(P||Q) ≤Qn(T (P )) ≤2−nD(P||Q).
(17.40)
17.5
COMBINATORIAL BOUNDS ON ENTROPY
We give tight bounds on the size of
n
k
	
when k is not 0 or n using the
result of Wozencraft and Reiffen [568]:
Lemma 17.5.1
For 0 < p < 1, q = 1 −p, such that np is an integer,
1
√8npq ≤

 n
np

2−nH(p) ≤
1
√πnpq .
(17.41)
Proof:
We begin with a strong form of Stirling’s approximation [208],
which states that
√
2πn
n
e
n
≤n! ≤
√
2πn
n
e
n
e
1
12n .
(17.42)
Applying this to ﬁnd an upper bound, we obtain

 n
np

≤
√
2πn(n
e)ne
1
12n
√2πnp( np
e )np√2πnq(nq
e )nq
(17.43)
=
1
√2πnpq
1
pnpqnq e
1
12n
(17.44)


## PDF page 693

17.6
ENTROPY RATES OF SUBSETS
667
<
1
√πnpq 2nH(p),
(17.45)
since e
1
12n < e
1
12 = 1.087 <
√
2, hence proving the upper bound.
The lower bound is obtained similarly. Using Stirling’s formula, we
obtain

 n
np

≥
√
2πn(n
e)ne
−

1
12np +
1
12nq

√2πnp( np
e )np√2πnq(nq
e )nq
(17.46)
=
1
√2πnpq
1
pnpqnq e
−

1
12np +
1
12nq

(17.47)
=
1
√2πnpq 2nH(p) e
−

1
12np +
1
12nq

.
(17.48)
If np ≥1, and nq ≥3, then
e
−

1
12np +
1
12nq

≥e−1
9 = 0.8948 >
√π
2
= 0.8862,
(17.49)
and the lower bound follows directly from substituting this into the equa-
tion. The exceptions to this condition are the cases where np = 1, nq = 1
or 2, and np = 2, nq = 2 (the case when np ≥3, nq = 1 or 2 can be
handled by ﬂipping the roles of p and q). In each of these cases
np = 1, nq = 1 →n = 2, p = 1
2,
 n
np
	
= 2, bound = 2
np = 1, nq = 2 →n = 3, p = 1
3,
 n
np
	
= 3, bound = 2.92
np = 2, nq = 2 →n = 4, p = 1
2,
 n
np
	
= 6, bound = 5.66.
Thus, even in these special cases, the bound is valid, and hence the lower
bound is valid for all p ̸= 0, 1. Note that the lower bound blows up when
p = 0 or p = 1, and is therefore not valid.
□
17.6
ENTROPY RATES OF SUBSETS
We now generalize the chain rule for differential entropy. The chain rule
provides a bound on the entropy rate of a collection of random variables
in terms of the entropy of each random variable:
h(X1, X2, . . . , Xn) ≤
n

i=1
h(Xi).
(17.50)


## PDF page 694

668
INEQUALITIES IN INFORMATION THEORY
We extend this to show that the entropy per element of a subset of a set of
random variables decreases as the size of the subset increases. This is not
true for each subset but is true on the average over subsets, as expressed
in Theorem 17.6.1.
Deﬁnition
Let (X1, X2, . . . , Xn) have a density, and for every S ⊆
{1, 2, . . . , n}, denote by X(S) the subset {Xi : i ∈S).
Let
h(n)
k
= 1
n
k
	

S: |S|=k
h(X(S))
k
.
(17.51)
Here h(n)
k
is the average entropy in bits per symbol of a randomly drawn
k-element subset of {X1, X2, . . . , Xn}.
The following theorem by Han [270] says that the average entropy
decreases monotonically in the size of the subset.
Theorem 17.6.1
h(n)
1
≥h(n)
2
≥· · · ≥h(n)
n .
(17.52)
Proof:
We ﬁrst prove the last inequality, h(n)
n
≤h(n)
n−1. We write
h(X1, X2, . . . , Xn) = h(X1, X2, . . . , Xn−1)+h(Xn|X1, X2, . . . , Xn−1),
h(X1, X2, . . . , Xn) = h(X1, X2, . . . , Xn−2, Xn)
+ h(Xn−1|X1, X2, . . . , Xn−2, Xn),
≤h(X1, X2, . . . , Xn−2, Xn)
+ h(Xn−1|X1, X2, . . . , Xn−2),
...
h(X1, X2, . . . , Xn) ≤h(X2, X3, . . . , Xn) + h(X1).
Adding these n inequalities and using the chain rule, we obtain
n h(X1, X2, . . . , Xn) ≤
n

i=1
h(X1, X2, . . . , Xi−1, Xi+1, . . . , Xn)
+ h(X1, X2, . . . , Xn)
(17.53)
or
1
nh(X1, X2, . . . , Xn) ≤1
n
n

i=1
h(X1, X2, . . . , Xi−1, Xi+1, . . . , Xn)
n −1
,
(17.54)


## PDF page 695

17.6
ENTROPY RATES OF SUBSETS
669
which is the desired result h(n)
n
≤h(n)
n−1. We now prove that h(n)
k
≤h(n)
k−1
for all k ≤n by ﬁrst conditioning on a k-element subset, and then taking
a uniform choice over its (k −1)-element subsets. For each k-element
subset, h(k)
k
≤h(k)
k−1, and hence the inequality remains true after taking
the expectation over all k-element subsets chosen uniformly from the n
elements.
□
Theorem 17.6.2
Let r > 0, and deﬁne
t(n)
k
= 1
n
k
	

S: |S|=k
e
r h(X(S))
k
.
(17.55)
Then
t(n)
1
≥t(n)
2
≥· · · ≥t(n)
n .
(17.56)
Proof:
Starting from (17.54), we multiply both sides by r, exponentiate,
and then apply the arithmetic mean geometric mean inequality, to obtain
e
1
nrh(X1, X2, . . . , Xn)
≤e
1
n
n
i=1
rh(X1,X2,...,Xi−1,Xi+1,...,Xn)
(n−1)
(17.57)
≤1
n
n

i=1
e
rh(X1,X2,...,Xi−1,Xi+1,...,Xn)
(n−1)
for all r ≥0,
(17.58)
which is equivalent to t(n)
n
≤t(n)
n−1. Now we use the same arguments as
in Theorem 17.6.1, taking an average over all subsets to prove the result
that for all k ≤n, t(n)
k
≤t(n)
k−1.
□
Deﬁnition
The average conditional entropy rate per element for all
subsets of size k is the average of the above quantities for k-element
subsets of {1, 2, . . . , n}:
g(n)
k
= 1
n
k
	

S:|S|=k
h(X(S)|X(Sc))
k
.
(17.59)
Here gk(S) is the entropy per element of the set S conditional on the
elements of the set Sc. When the size of the set S increases, one can
expect a greater dependence among the elements of the set S, which
explains Theorem 17.6.1.


## PDF page 696

670
INEQUALITIES IN INFORMATION THEORY
In the case of the conditional entropy per element, as k increases, the
size of the conditioning set Sc decreases and the entropy of the set S
increases. The increase in entropy per element due to the decrease in
conditioning dominates the decrease due to additional dependence among
the elements, as can be seen from the following theorem due to Han [270].
Note that the conditional entropy ordering in the following theorem is the
reverse of the unconditional entropy ordering in Theorem 17.6.1.
Theorem 17.6.3
g(n)
1
≤g(n)
2
≤· · · ≤g(n)
n .
(17.60)
Proof:
The proof proceeds on lines very similar to the proof of the
theorem for the unconditional entropy per element for a random subset.
We ﬁrst prove that g(n)
n
≥g(n)
n−1 and then use this to prove the rest of
the inequalities. By the chain rule, the entropy of a collection of random
variables is less than the sum of the entropies:
h(X1, X2, . . . , Xn) ≤
n

i=1
h(Xi).
(17.61)
Subtracting both sides of this inequality from nh(X1, X2, . . . , Xn), we
have
(n −1)h(X1, X2, . . . , Xn) ≥
n

i=1
(h(X1, X2, . . . , Xn) −h(Xi)) (17.62)
=
n

i=1
h(X1, . . . , Xi−1, Xi+1, . . . , Xn|Xi).
(17.63)
Dividing this by n(n −1), we obtain
h(X1, X2, . . . , Xn)
n
≥1
n
n

i=1
h(X1, X2, . . . , Xi−1, Xi+1, . . . , Xn|Xi)
n −1
,
(17.64)
which is equivalent to g(n)
n
≥g(n)
n−1. We now prove that g(n)
k
≥g(n)
k−1 for
all k ≤n by ﬁrst conditioning on a k-element subset and then taking
a uniform choice over its (k −1)-element subsets. For each k-element
subset, g(k)
k
≥g(k)
k−1, and hence the inequality remains true after taking
the expectation over all k-element subsets chosen uniformly from the n
elements.
□


