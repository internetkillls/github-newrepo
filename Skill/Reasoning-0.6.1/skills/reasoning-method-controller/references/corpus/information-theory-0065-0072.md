# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 65

2.10
FANO’S INEQUALITY
39
equal to 0. Also, since E is a binary-valued random variable, H(E) =
H(Pe). The remaining term, H(X|E, ˆX), can be bounded as follows:
H(X|E, ˆX) = Pr(E = 0)H(X| ˆX, E = 0) + Pr(E = 1)H(X| ˆX, E = 1)
≤(1 −Pe)0 + Pe log |X|,
(2.136)
since given E = 0, X = ˆX, and given E = 1, we can upper bound the
conditional entropy by the log of the number of possible outcomes. Com-
bining these results, we obtain
H(Pe) + Pe log |X| ≥H(X| ˆX).
(2.137)
By the data-processing inequality, we have I (X; ˆX) ≤I (X; Y) since
X →Y →ˆX is a Markov chain, and therefore H(X| ˆX) ≥H(X|Y). Thus,
we have
H(Pe) + Pe log |X| ≥H(X| ˆX) ≥H(X|Y).
□
(2.138)
Corollary
For any two random variables X and Y, let p = Pr(X ̸= Y).
H(p) + p log |X| ≥H(X|Y).
(2.139)
Proof:
Let ˆX = Y in Fano’s inequality.
□
For any two random variables X and Y, if the estimator g(Y) takes
values in the set X, we can strengthen the inequality slightly by replacing
log |X| with log(|X| −1).
Corollary
Let Pe = Pr(X ̸= ˆX), and let ˆX : Y →X; then
H(Pe) + Pe log(|X| −1) ≥H(X|Y).
(2.140)
Proof:
The proof of the theorem goes through without change, except
that
H(X|E, ˆX) = Pr(E = 0)H(X| ˆX, E = 0) + Pr(E = 1)H(X| ˆX, E = 1)
(2.141)
≤(1 −Pe)0 + Pe log(|X| −1),
(2.142)
since given E = 0, X = ˆX, and given E = 1, the range of possible X
outcomes is |X| −1, we can upper bound the conditional entropy by the
log(|X| −1), the logarithm of the number of possible outcomes. Substi-
tuting this provides us with the stronger inequality.
□


## PDF page 66

40
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Remark
Suppose that there is no knowledge of Y. Thus, X must be
guessed without any information. Let X ∈{1, 2, . . . , m} and p1 ≥p2 ≥
· · · ≥pm. Then the best guess of X is ˆX = 1 and the resulting probability
of error is Pe = 1 −p1. Fano’s inequality becomes
H(Pe) + Pe log(m −1) ≥H(X).
(2.143)
The probability mass function
(p1, p2, . . . , pm) =

1 −Pe,
Pe
m −1, . . . ,
Pe
m −1

(2.144)
achieves this bound with equality. Thus, Fano’s inequality is sharp.
While we are at it, let us introduce a new inequality relating probability
of error and entropy. Let X and X′ by two independent identically dis-
tributed random variables with entropy H(X). The probability at X = X′
is given by
Pr(X = X′) =

x
p2(x).
(2.145)
We have the following inequality:
Lemma 2.10.1
If X and X′ are i.i.d. with entropy H(X),
Pr(X = X′) ≥2−H(X),
(2.146)
with equality if and only if X has a uniform distribution.
Proof:
Suppose that X ∼p(x). By Jensen’s inequality, we have
2E log p(X) ≤E2log p(X),
(2.147)
which implies that
2−H(X) = 2
 p(x) log p(x) ≤

p(x)2log p(x) =

p2(x).
□
(2.148)
Corollary
Let X, X′ be independent with X ∼p(x), X′ ∼r(x), x, x′ ∈
X. Then
Pr(X = X′) ≥2−H(p)−D(p||r),
(2.149)
Pr(X = X′) ≥2−H(r)−D(r||p).
(2.150)


## PDF page 67

SUMMARY
41
Proof:
We have
2−H(p)−D(p||r) = 2
 p(x) log p(x)+ p(x) log r(x)
p(x)
(2.151)
= 2
 p(x) log r(x)
(2.152)
≤

p(x)2log r(x)
(2.153)
=

p(x)r(x)
(2.154)
= Pr(X = X′),
(2.155)
where the inequality follows from Jensen’s inequality and the convexity
of the function f (y) = 2y.
□
The following telegraphic summary omits qualifying conditions.
SUMMARY
Deﬁnition
The entropy H(X) of a discrete random variable X is
deﬁned by
H(X) = −

x∈X
p(x) log p(x).
(2.156)
Properties of H
1. H(X) ≥0.
2. Hb(X) = (logb a)Ha(X).
3. (Conditioning reduces entropy) For any two random variables, X
and Y, we have
H(X|Y) ≤H(X)
(2.157)
with equality if and only if X and Y are independent.
4. H(X1, X2, . . . , Xn) ≤n
i=1 H(Xi), with equality if and only if the
Xi are independent.
5. H(X) ≤log | X |, with equality if and only if X is distributed uni-
formly over X.
6. H(p) is concave in p.


## PDF page 68

42
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Deﬁnition
The relative entropy D(p ∥q) of the probability mass
function p with respect to the probability mass function q is deﬁned by
D(p ∥q) =

xp(x) log p(x)
q(x) .
(2.158)
Deﬁnition
The mutual information between two random variables X
and Y is deﬁned as
I (X; Y) =

x∈X

y∈Y
p(x, y) log p(x, y)
p(x)p(y).
(2.159)
Alternative expressions
H(X) = Ep log
1
p(X),
(2.160)
H(X, Y) = Ep log
1
p(X, Y),
(2.161)
H(X|Y) = Ep log
1
p(X|Y),
(2.162)
I (X; Y) = Ep log p(X, Y)
p(X)p(Y),
(2.163)
D(p||q) = Ep log p(X)
q(X).
(2.164)
Properties of D and I
1. I (X; Y) = H(X) −H(X|Y) = H(Y) −H(Y|X) = H(X) +
H(Y) −H(X, Y).
2. D(p ∥q) ≥0 with equality if and only if p(x) = q(x), for all x ∈
X.
3. I (X; Y) = D(p(x, y)||p(x)p(y)) ≥0, with equality if and only if
p(x, y) = p(x)p(y) (i.e., X and Y are independent).
4. If | X |= m, and u is the uniform distribution over X, then D(p ∥
u) = log m −H(p).
5. D(p||q) is convex in the pair (p, q).
Chain rules
Entropy: H(X1, X2, . . . , Xn) = n
i=1 H(Xi|Xi−1, . . . , X1).
Mutual information:
I (X1, X2, . . . , Xn; Y) = n
i=1 I (Xi; Y|X1, X2, . . . , Xi−1).


## PDF page 69

PROBLEMS
43
Relative entropy:
D(p(x, y)||q(x, y)) = D(p(x)||q(x)) + D(p(y|x)||q(y|x)).
Jensen’s inequality. If f is a convex function, then Ef (X) ≥f (EX).
Log sum inequality. For n positive numbers, a1, a2, . . . , an and
b1, b2, . . . , bn,
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
(2.165)
with equality if and only if ai
bi = constant.
Data-processing inequality. If X →Y →Z forms a Markov chain,
I (X; Y) ≥I (X; Z).
Sufﬁcient statistic. T (X) is sufﬁcient relative to {fθ(x)} if and only
if I (θ; X) = I (θ; T (X)) for all distributions on θ.
Fano’s inequality. Let Pe = Pr{ ˆX(Y) ̸= X}. Then
H(Pe) + Pe log |X| ≥H(X|Y).
(2.166)
Inequality. If X and X′ are independent and identically distributed,
then
Pr(X = X′) ≥2−H(X),
(2.167)
PROBLEMS
2.1
Coin ﬂips.
A fair coin is ﬂipped until the ﬁrst head occurs. Let
X denote the number of ﬂips required.
(a) Find the entropy H(X) in bits. The following expressions may
be useful:
∞

n=0
rn =
1
1 −r ,
∞

n=0
nrn =
r
(1 −r)2.
(b) A random variable X is drawn according to this distribution.
Find an “efﬁcient” sequence of yes–no questions of the form,


## PDF page 70

44
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
“Is X contained in the set S?” Compare H(X) to the expected
number of questions required to determine X.
2.2
Entropy of functions.
Let X be a random variable taking on a
ﬁnite number of values. What is the (general) inequality relation-
ship of H(X) and H(Y) if
(a) Y = 2X?
(b) Y = cos X?
2.3
Minimum
entropy.
What
is
the
minimum
value
of
H(p1, . . . , pn) = H(p) as p ranges over the set of n-dimensional
probability vectors?
Find all p’s that achieve this minimum.
2.4
Entropy of functions of a random variable.
Let X be a discrete
random variable. Show that the entropy of a function of X is less
than or equal to the entropy of X by justifying the following steps:
H(X, g(X))
(a)
= H(X) + H(g(X) | X)
(2.168)
(b)
= H(X),
(2.169)
H(X, g(X))
(c)
= H(g(X)) + H(X | g(X))
(2.170)
(d)
≥H(g(X)).
(2.171)
Thus, H(g(X)) ≤H(X).
2.5
Zero conditional entropy.
Show that if H(Y|X) = 0, then Y is
a function of X [i.e., for all x with p(x) > 0, there is only one
possible value of y with p(x, y) > 0].
2.6
Conditional mutual information vs. unconditional mutual informa-
tion.
Give examples of joint random variables X, Y, and Z
such that
(a) I (X; Y | Z) < I (X; Y).
(b) I (X; Y | Z) > I (X; Y).
2.7
Coin weighing.
Suppose that one has n coins, among which there
may or may not be one counterfeit coin. If there is a counterfeit
coin, it may be either heavier or lighter than the other coins. The
coins are to be weighed by a balance.
(a) Find an upper bound on the number of coins n so that k
weighings will ﬁnd the counterfeit coin (if any) and correctly
declare it to be heavier or lighter.


## PDF page 71

PROBLEMS
45
(b) (Difﬁcult) What is the coin- weighing strategy for k = 3 weigh-
ings and 12 coins?
2.8
Drawing with and without replacement.
An urn contains r red, w
white, and b black balls. Which has higher entropy, drawing k ≥2
balls from the urn with replacement or without replacement? Set it
up and show why. (There is both a difﬁcult way and a relatively
simple way to do this.)
2.9
Metric.
A function ρ(x, y) is a metric if for all x, y,
• ρ(x, y) ≥0.
• ρ(x, y) = ρ(y, x).
• ρ(x, y) = 0 if and only if x = y.
• ρ(x, y) + ρ(y, z) ≥ρ(x, z).
(a) Show that ρ(X, Y) = H(X|Y) + H(Y|X) satisﬁes the ﬁrst,
second, and fourth properties above. If we say that X = Y if
there is a one-to-one function mapping from X to Y, the third
property is also satisﬁed, and ρ(X, Y) is a metric.
(b) Verify that ρ(X, Y) can also be expressed as
ρ(X, Y) = H(X) + H(Y) −2I (X; Y)
(2.172)
= H(X, Y) −I (X; Y)
(2.173)
= 2H(X, Y) −H(X) −H(Y).
(2.174)
2.10
Entropy of a disjoint mixture.
Let X1 and X2 be discrete random
variables drawn according to probability mass functions p1(·) and
p2(·) over the respective alphabets X1 = {1, 2, . . . , m} and X2 =
{m + 1, . . . , n}. Let
X =

X1
with probability α,
X2
with probability 1 −α.
(a) Find H(X) in terms of H(X1), H(X2), and α.
(b) Maximize over α to show that 2H(X) ≤2H(X1) + 2H(X2) and
interpret using the notion that 2H(X) is the effective alpha-
bet size.
2.11
Measure of correlation.
Let X1 and X2 be identically distributed
but not necessarily independent. Let
ρ = 1 −H(X2 | X1)
H(X1)
.


## PDF page 72

46
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
(a) Show that ρ = I(X1;X2)
H(X1) .
(b) Show that 0 ≤ρ ≤1.
(c) When is ρ = 0?
(d) When is ρ = 1?
2.12
Example of joint entropy.
Let p(x, y) be given by
Find:
(a) H(X), H(Y).
(b) H(X | Y), H(Y | X).
(c) H(X, Y).
(d) H(Y) −H(Y | X).
(e) I (X; Y).
(f) Draw a Venn diagram for the quantities in parts (a) through (e).
2.13
Inequality.
Show that ln x ≥1 −1
x for x > 0.
2.14
Entropy of a sum.
Let X and Y be random variables that take
on values x1, x2, . . . , xr and y1, y2, . . . , ys, respectively. Let Z =
X + Y.
(a) Show that H(Z|X) = H(Y|X). Argue that if X, Y are inde-
pendent, then H(Y) ≤H(Z) and H(X) ≤H(Z). Thus, the
addition of independent random variables adds uncertainty.
(b) Give an example of (necessarily dependent) random variables
in which H(X) > H(Z) and H(Y) > H(Z).
(c) Under what conditions does H(Z) = H(X) + H(Y)?
2.15
Data processing.
Let
X1 →X2 →X3 →· · · →Xn
form
a
Markov chain in this order; that is, let
p(x1, x2, . . . , xn) = p(x1)p(x2|x1) · · · p(xn|xn−1).
Reduce I (X1; X2, . . . , Xn) to its simplest form.
2.16
Bottleneck.
Suppose that a (nonstationary) Markov chain starts
in one of n states, necks down to k < n states, and then
fans back to m > k states. Thus, X1 →X2 →X3, that is,


