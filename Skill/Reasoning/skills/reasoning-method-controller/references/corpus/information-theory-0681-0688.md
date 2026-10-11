# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 681

HISTORICAL NOTES
655
ˆb2(x1) =
 1
0 bS1(b) db
 1
0 S1(b) db
.
(f) Which of S2(b), S∗
2, ˆS2, ˆb2 are unchanged if we permute the
order of appearance of the stock vector outcomes [i.e., if the
sequence is now (1, 2), (1, 1
2)]?
16.10
Growth optimal.
Let X1, X2 ≥0, be price relatives of two inde-
pendent stocks. Suppose that EX1 > EX2. Do you always want
some of X1 in a growth rate optimal portfolio S(b) = bX1 + bX2?
Prove or provide a counterexample.
16.11
Cost of universality.
In the discussion of ﬁnite-horizon universal
portfolios, it was shown that the loss factor due to universality is
1
Vn
=
n

k=0
n
k
 k
n
k n −k
n
n−k
.
(16.233)
Evaluate Vn for n = 1, 2, 3.
16.12
Convex families.
This problem generalizes Theorem 16.2.2. We
say that S is a convex family of random variables if S1, S2 ∈S
implies that λS1 + (1 −λ)S2 ∈S. Let S be a closed convex family
of random variables. Show that there is a random variable S∗∈S
such that
E ln
 S
S∗

≤0
(16.234)
for all S ∈S if and only if
E
 S
S∗

≤1
(16.235)
for all S ∈S.
HISTORICAL NOTES
There is an extensive literature on the mean–variance approach to invest-
ment in the stock market. A good introduction is the book by Sharpe
[491]. Log-optimal portfolios were introduced by Kelly [308] and Latan´e
[346], and generalized by Breiman [75]. The bound on the increase in the


## PDF page 682

656
INFORMATION THEORY AND PORTFOLIO THEORY
growth rate in terms of the mutual information is due to Barron and Cover
[31]. See Samuelson [453, 454] for a criticism of log-optimal investment.
The proof of the competitive optimality of the log-optimal portfolio
is due to Bell and Cover [39, 40]. Breiman [75] investigated asymptotic
optimality for random market processes.
The AEP was introduced by Shannon. The AEP for the stock mar-
ket and the asymptotic optimality of log-optimal investment are given
in Algoet and Cover [21]. The relatively simple sandwich proof for the
AEP is due to Algoet and Cover [20]. The AEP for real-valued ergodic
processes was proved in full generality by Barron [34] and Orey [402].
The universal portfolio was deﬁned in Cover [110] and the proof of
universality was given in Cover [110] and more exactly in Cover and
Ordentlich [135]. The ﬁxed-horizon exact calculation of the cost of uni-
versality Vn is given in Ordentlich and Cover [401]. The quantity Vn also
appears in data compression in the work of Shtarkov [496].


## PDF page 683

CHAPTER 17
INEQUALITIES IN
INFORMATION THEORY
This chapter summarizes and reorganizes the inequalities found throughout
this book. A number of new inequalities on the entropy rates of subsets
and the relationship of entropy and Lp norms are also developed. The
intimate relationship between Fisher information and entropy is explored,
culminating in a common proof of the entropy power inequality and the
Brunn–Minkowski inequality. We also explore the parallels between the
inequalities in information theory and inequalities in other branches of
mathematics, such as matrix theory and probability theory.
17.1
BASIC INEQUALITIES OF INFORMATION THEORY
Many of the basic inequalities of information theory follow directly from
convexity.
Deﬁnition
A function f is said to be convex if
f (λx1 + (1 −λ)x2) ≤λf (x1) + (1 −λ)f (x2)
(17.1)
for all 0 ≤λ ≤1 and all x1 and x2.
Theorem 17.1.1
(Theorem 2.6.2: Jensen’s inequality)
If f is convex,
then
f (EX) ≤Ef (X).
(17.2)
Lemma 17.1.1
The function log x is concave and x log x is convex, for
0 < x < ∞.
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
657


## PDF page 684

658
INEQUALITIES IN INFORMATION THEORY
Theorem 17.1.2
(Theorem 2.7.1: Log sum inequality)
For positive
numbers a1, a2, . . . , an and b1, b2, . . . , bn,
n

i=1
ai log ai
bi
≥
 n

i=1
ai

log
n
i=1 ai
n
i=1 bi
(17.3)
with equality iff ai
bi = constant.
We recall the following properties of entropy from Section 2.1.
Deﬁnition
The entropy H(X) of a discrete random variable X is de-
ﬁned by
H(X) = −

x∈Xp(x) log p(x).
(17.4)
Theorem 17.1.3
(Lemma 2.1.1, Theorem 2.6.4: Entropy bound)
0 ≤H(X) ≤log |X|.
(17.5)
Theorem 17.1.4
(Theorem 2.6.5: Conditioning reduces entropy)
For
any two random variables X and Y,
H(X|Y) ≤H(X),
(17.6)
with equality iff X and Y are independent.
Theorem 17.1.5
(Theorem 2.5.1 with Theorem 2.6.6: Chain rule)
H(X1, X2, . . . , Xn) =
n

i=1
H(Xi|Xi−1, . . . , X1) ≤
n

i=1
H(Xi),
(17.7)
with equality iff X1, X2, . . . , Xn are independent.
Theorem 17.1.6
(Theorem 2.7.3)
H(p) is a concave function of p.
We now state some properties of relative entropy and mutual informa-
tion (Section 2.3).
Deﬁnition
The relative entropy or Kullback–Leibler distance between
two probability mass functions p(x) and q(x) is deﬁned by
D(p||q) =

x∈X
p(x) log p(x)
q(x) .
(17.8)


## PDF page 685

17.1
BASIC INEQUALITIES OF INFORMATION THEORY
659
Deﬁnition
The mutual information between two random variables X
and Y is deﬁned by
I (X; Y) =

x∈X

y∈Y
p(x, y) log p(x, y)
p(x)p(y) = D(p(x, y)||p(x)p(y)).
(17.9)
The following basic information inequality can be used to prove many
of the other inequalities in this chapter.
Theorem 17.1.7
(Theorem 2.6.3: Information inequality)
For any
two probability mass functions p and q,
D(p||q) ≥0
(17.10)
with equality iff p(x) = q(x) for all x ∈X.
Corollary
For any two random variables X and Y,
I (X; Y) = D(p(x, y)||p(x)p(y)) ≥0
(17.11)
with equality iff p(x, y) = p(x)p(y) (i.e., X and Y are independent).
Theorem 17.1.8
(Theorem 2.7.2:
Convexity
of
relative
entropy)
D(p||q) is convex in the pair (p, q).
Theorem 17.1.9
(Theorem 2.4.1)
I (X; Y) = H(X) −H(X|Y).
(17.12)
I (X; Y) = H(Y) −H(Y|X).
(17.13)
I (X; Y) = H(X) + H(Y) −H(X, Y).
(17.14)
I (X; X) = H(X).
(17.15)
Theorem 17.1.10
(Section 4.4)
For a Markov chain:
1. Relative entropy D(µn||µ′
n) decreases with time.
2. Relative entropy D(µn||µ) between a distribution and the stationary
distribution decreases with time.
3. Entropy H(Xn) increases if the stationary distribution is uniform.
4. The conditional entropy H(Xn|X1) increases with time for a station-
ary Markov chain.


## PDF page 686

660
INEQUALITIES IN INFORMATION THEORY
Theorem 17.1.11
Let X1, X2, . . . , Xn be i.i.d. ∼p(x). Let ˆpn be the
empirical probability mass function of X1, X2, . . . , Xn. Then
ED( ˆpn||p) ≤ED( ˆpn−1||p).
(17.16)
17.2
DIFFERENTIAL ENTROPY
We now review some of the basic properties of differential entropy
(Section 8.1).
Deﬁnition
The differential entropy h(X1, X2, . . . , Xn), sometimes writ-
ten h(f ), is deﬁned by
h(X1, X2, . . . , Xn) = −

f (x) log f (x) dx.
(17.17)
The differential entropy for many common densities is given in
Table 17.1.
Deﬁnition
The relative entropy between probability densities f and
g is
D(f ||g) =

f (x) log (f (x)/g(x)) dx.
(17.18)
The properties of the continuous version of relative entropy are iden-
tical to the discrete version. Differential entropy, on the other hand, has
some properties that differ from those of discrete entropy. For example,
differential entropy may be negative.
We now restate some of the theorems that continue to hold for differ-
ential entropy.
Theorem 17.2.1
(Theorem 8.6.1:
Conditioning
reduces
entropy)
h(X|Y) ≤h(X), with equality iff X and Y are independent.
Theorem 17.2.2
(Theorem 8.6.2: Chain rule)
h(X1, X2, . . . , Xn) =
n

i=1
h(Xi|Xi−1, Xi−2, . . . , X1) ≤
n

i=1
h(Xi)
(17.19)
with equality iff X1, X2, . . . , Xn are independent.
Lemma 17.2.1
If X and Y are independent, then h(X + Y) ≥h(X).
Proof:
h(X + Y) ≥h(X + Y|Y) = h(X|Y) = h(X).
□


## PDF page 687

17.2
DIFFERENTIAL ENTROPY
661
TABLE 17.1
Differential Entropiesa
Distribution
Name
Density
Entropy (nats)
f (x) = xp−1(1 −x)q−1
B(p, q)
,
ln B(p, q) −(p −1)
Beta
×[ψ(p) −ψ(p + q)]
0 ≤x ≤1, p, q > 0
−(q −1)[ψ(q) −ψ(p + q)]
f (x) = λ
π
1
λ2 + x2 ,
Cauchy
ln(4πλ)
−∞< x < ∞, λ > 0
f (x) =
2
2n/2σ n(n/2)xn−1e
−x2
2σ2 ,
Chi
ln σ(n/2)
√
2
−n −1
2
ψ
n
2

+ n
2
x > 0, n > 0
f (x) =
1
2n/2σ n(n/2)x
n
2 −1e
−x
2σ2 ,
ln 2σ 2
n
2

Chi-squared
x > 0, n > 0
−

1 −n
2

ψ
n
2

+ n
2
f (x) =
βn
(n −1)!xn−1e−βx,
Erlang
(1 −n)ψ(n) + ln (n)
β
+ n
x, β > 0, n > 0
Exponential f (x) = 1
λe−x
λ , x, λ > 0
1 + ln λ
f (x) = n
n1
2
1 n
n2
2
2
B( n1
2 , n2
2 )
×
x( n1
2 ) −1
(n2 + n1x)
n1+n2
2
,
ln n1
n2
B
n1
2 , n2
2

x > 0, n1, n2 > 0
F
+

1 −n1
2
	
ψ
n1
2

−

1 −n2
2

ψ
n2
2

+n1 + n2
2
ψ

n1 + n2
2

Gamma
f (x) = xα−1e−x
β
βα(α) ,
x, α, β > 0
ln(β(α)) + (1 −α)ψ(α) + α
f (x) = 1
2λe−|x−θ|
λ
,
Laplace
1 + ln 2λ
−∞< x, θ < ∞, λ > 0
f (x) =
e−x
(1+e−x)2 ,
Logistic
2
−∞< x < ∞


## PDF page 688

662
INEQUALITIES IN INFORMATION THEORY
TABLE 17.1
(continued)
Distribution
Name
Density
Entropy (nats)
f (x) =
1
σx
√
2π e
−ln(x−m)2
2σ2
,
Lognormal
m + 1
2 ln(2πeσ 2)
x > 0, −∞< m < ∞, σ > 0
Maxwell–
f (x) = 4π−1
2 β
3
2 x2e−βx2,
Boltzmann
1
2 ln π
β + γ −1
2
x, β > 0
f (x) =
1
√
2πσ 2 e
−(x−µ)2
2σ2
,
Normal
1
2 ln(2πeσ 2)
−∞< x, µ < ∞, σ > 0
Generalized
f (x) = 2β
α
2
( α
2 )xα−1e−βx2,
normal
ln ( α
2 )
2β
1
2
−α −1
2
ψ
α
2

+ α
2
x, α, β > 0
Pareto
f (x) = aka
xa+1 , x ≥k > 0, a > 0
ln k
a + 1 + 1
a
Rayleigh
f (x) = x
b2 e
−x2
2b2 ,
x, b > 0
1 + ln β
√
2
+ γ
2
f (x) = (1 + x2/n)−(n+1)/2
√nB( 1
2, n
2 )
,
n + 1
2
ψ

n + 1
2

−ψ
n
2

Student’s t
−∞< x < ∞, n > 0
+ ln √nB

1
2, n
2

Triangular
f (x) =



2x
a ,
0 ≤x ≤a
2(1 −x)
1 −a
,
a ≤x ≤1
1
2 −ln 2
Uniform
f (x) =
1
β −α , α ≤x ≤β
ln(β −α)
Weibull
f (x) = c
α xc−1e−xc
α ,
x, c, α > 0
(c −1)γ
c
+ ln α
1
c
c + 1
a All entropies are in nats; (z) =
 ∞
0 e−ttz−1 dt; ψ(z) = d
dz ln (z); γ = Euler’s constant =
0.57721566 . . . .
Source: Lazo and Rathie [543].


