# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 57

2.7
LOG SUM INEQUALITY AND ITS APPLICATIONS
31
Theorem 2.7.1
(Log sum inequality)
For nonnegative numbers,
a1, a2, . . . , an and b1, b2, . . . , bn,
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
(2.99)
with equality if and only if ai
bi = const.
We again use the convention that 0 log 0 = 0, a log a
0 = ∞if a > 0 and
0 log 0
0 = 0. These follow easily from continuity.
Proof:
Assume without loss of generality that ai > 0 and bi > 0. The
function f (t) = t log t is strictly convex, since f ′′(t) = 1
t log e > 0 for all
positive t. Hence by Jensen’s inequality, we have

αif (ti) ≥f

αiti

(2.100)
for αi ≥0, 
i αi = 1. Setting αi =
bi
n
j=1 bj and ti = ai
bi , we obtain

ai
 bj
log ai
bi
≥

ai
 bj
log

ai
 bj
,
(2.101)
which is the log sum inequality.
□
We now use the log sum inequality to prove various convexity results.
We begin by reproving Theorem 2.6.3, which states that D(p||q) ≥0 with
equality if and only if p(x) = q(x). By the log sum inequality,
D(p||q) =

p(x) log p(x)
q(x)
(2.102)
≥

p(x)

log

p(x)
 
q(x)
(2.103)
= 1 log 1
1 = 0
(2.104)
with equality if and only if p(x)
q(x) = c. Since both p and q are probability
mass functions, c = 1, and hence we have D(p||q) = 0 if and only if
p(x) = q(x) for all x.


## PDF page 58

32
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Theorem 2.7.2
(Convexity of relative entropy)
D(p||q) is convex in
the pair (p, q); that is, if (p1, q1) and (p2, q2) are two pairs of probability
mass functions, then
D(λp1 + (1 −λ)p2||λq1 + (1 −λ)q2) ≤λD(p1||q1) + (1 −λ)D(p2||q2)
(2.105)
for all 0 ≤λ ≤1.
Proof:
We apply the log sum inequality to a term on the left-hand side
of (2.105):
(λp1(x) + (1 −λ)p2(x)) log λp1(x) + (1 −λ)p2(x)
λq1(x) + (1 −λ)q2(x)
≤λp1(x) log λp1(x)
λq1(x) + (1 −λ)p2(x) log (1 −λ)p2(x)
(1 −λ)q2(x) .
(2.106)
Summing this over all x, we obtain the desired property.
□
Theorem 2.7.3
(Concavity of entropy)
H(p) is a concave function
of p.
Proof
H(p) = log |X| −D(p||u),
(2.107)
where u is the uniform distribution on |X| outcomes. The concavity of H
then follows directly from the convexity of D.
□
Alternative Proof:
Let X1 be a random variable with distribution p1,
taking on values in a set A. Let X2 be another random variable with
distribution p2 on the same set. Let
θ =

1
with probability λ,
2
with probability 1 −λ.
(2.108)
Let Z = Xθ. Then the distribution of Z is λp1 + (1 −λ)p2. Now since
conditioning reduces entropy, we have
H(Z) ≥H(Z|θ),
(2.109)
or equivalently,
H(λp1 + (1 −λ)p2) ≥λH(p1) + (1 −λ)H(p2),
(2.110)
which proves the concavity of the entropy as a function of the distribution.
□


## PDF page 59

2.7
LOG SUM INEQUALITY AND ITS APPLICATIONS
33
One of the consequences of the concavity of entropy is that mixing two
gases of equal entropy results in a gas with higher entropy.
Theorem 2.7.4
Let (X, Y) ∼p(x, y) = p(x)p(y|x). The mutual infor-
mation I (X; Y) is a concave function of p(x) for ﬁxed p(y|x) and a convex
function of p(y|x) for ﬁxed p(x).
Proof:
To prove the ﬁrst part, we expand the mutual information
I (X; Y) = H(Y) −H(Y|X) = H(Y) −

x
p(x)H(Y|X = x). (2.111)
If p(y|x) is ﬁxed, then p(y) is a linear function of p(x). Hence H(Y),
which is a concave function of p(y), is a concave function of p(x). The
second term is a linear function of p(x). Hence, the difference is a concave
function of p(x).
To prove the second part, we ﬁx p(x) and consider two different con-
ditional distributions p1(y|x) and p2(y|x). The corresponding joint dis-
tributions are p1(x, y) = p(x)p1(y|x) and p2(x, y) = p(x)p2(y|x), and
their respective marginals are p(x), p1(y) and p(x), p2(y). Consider a
conditional distribution
pλ(y|x) = λp1(y|x) + (1 −λ)p2(y|x),
(2.112)
which is a mixture of p1(y|x) and p2(y|x) where 0 ≤λ ≤1. The cor-
responding joint distribution is also a mixture of the corresponding joint
distributions,
pλ(x, y) = λp1(x, y) + (1 −λ)p2(x, y),
(2.113)
and the distribution of Y is also a mixture,
pλ(y) = λp1(y) + (1 −λ)p2(y).
(2.114)
Hence if we let qλ(x, y) = p(x)pλ(y) be the product of the marginal
distributions, we have
qλ(x, y) = λq1(x, y) + (1 −λ)q2(x, y).
(2.115)
Since the mutual information is the relative entropy between the joint
distribution and the product of the marginals,
I (X; Y) = D(pλ(x, y)||qλ(x, y)),
(2.116)
and relative entropy D(p||q) is a convex function of (p, q), it follows that
the mutual information is a convex function of the conditional distribution.
□


## PDF page 60

34
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
2.8
DATA-PROCESSING INEQUALITY
The data-processing inequality can be used to show that no clever manip-
ulation of the data can improve the inferences that can be made from
the data.
Deﬁnition
Random variables X, Y, Z are said to form a Markov chain
in that order (denoted by X →Y →Z) if the conditional distribution of
Z depends only on Y and is conditionally independent of X. Speciﬁcally,
X, Y, and Z form a Markov chain X →Y →Z if the joint probability
mass function can be written as
p(x, y, z) = p(x)p(y|x)p(z|y).
(2.117)
Some simple consequences are as follows:
• X →Y →Z if and only if X and Z are conditionally independent
given Y. Markovity implies conditional independence because
p(x, z|y) = p(x, y, z)
p(y)
= p(x, y)p(z|y)
p(y)
= p(x|y)p(z|y). (2.118)
This is the characterization of Markov chains that can be extended
to deﬁne Markov ﬁelds, which are n-dimensional random processes
in which the interior and exterior are independent given the values
on the boundary.
• X →Y →Z implies that Z →Y →X. Thus, the condition is some-
times written X ↔Y ↔Z.
• If Z = f (Y), then X →Y →Z.
We can now prove an important and useful theorem demonstrating that
no processing of Y, deterministic or random, can increase the information
that Y contains about X.
Theorem 2.8.1
(Data-processing inequality)
If X →Y →Z, then
I (X; Y) ≥I (X; Z).
Proof:
By the chain rule, we can expand mutual information in two
different ways:
I (X; Y, Z) = I (X; Z) + I (X; Y|Z)
(2.119)
= I (X; Y) + I (X; Z|Y).
(2.120)


## PDF page 61

2.9
SUFFICIENT STATISTICS
35
Since X and Z are conditionally independent given Y, we have
I (X; Z|Y) = 0. Since I (X; Y|Z) ≥0, we have
I (X; Y) ≥I (X; Z).
(2.121)
We have equality if and only if I (X; Y|Z) = 0 (i.e., X →Z →Y forms
a Markov chain). Similarly, one can prove that I (Y; Z) ≥I (X; Z).
□
Corollary
In particular, if Z = g(Y), we have I (X; Y) ≥I (X; g(Y)).
Proof:
X →Y →g(Y) forms a Markov chain.
□
Thus functions of the data Y cannot increase the information about X.
Corollary
If X →Y →Z, then I (X; Y|Z) ≤I (X; Y).
Proof:
We note in (2.119) and (2.120) that I (X; Z|Y) = 0, by
Markovity, and I (X; Z) ≥0. Thus,
I (X; Y|Z) ≤I (X; Y).
□
(2.122)
Thus, the dependence of X and Y is decreased (or remains unchanged)
by the observation of a “downstream” random variable Z. Note that it is
also possible that I (X; Y|Z) > I (X; Y) when X, Y, and Z do not form a
Markov chain. For example, let X and Y be independent fair binary ran-
dom variables, and let Z = X + Y. Then I (X; Y) = 0, but I (X; Y|Z) =
H(X|Z) −H(X|Y, Z) = H(X|Z) = P (Z = 1)H(X|Z = 1) = 1
2 bit.
2.9
SUFFICIENT STATISTICS
This section is a sidelight showing the power of the data-processing
inequality in clarifying an important idea in statistics. Suppose that we
have a family of probability mass functions {fθ(x)} indexed by θ, and let
X be a sample from a distribution in this family. Let T (X) be any statistic
(function of the sample) like the sample mean or sample variance. Then
θ →X →T (X), and by the data-processing inequality, we have
I (θ; T (X)) ≤I (θ; X)
(2.123)
for any distribution on θ. However, if equality holds, no information
is lost.
A statistic T (X) is called sufﬁcient for θ if it contains all the infor-
mation in X about θ.


## PDF page 62

36
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Deﬁnition
A function T (X) is said to be a sufﬁcient statistic relative to
the family {fθ(x)} if X is independent of θ given T (X) for any distribution
on θ[i.e., θ →T (X) →X forms a Markov chain].
This is the same as the condition for equality in the data-processing
inequality,
I (θ; X) = I (θ; T (X))
(2.124)
for all distributions on θ. Hence sufﬁcient statistics preserve mutual infor-
mation and conversely.
Here are some examples of sufﬁcient statistics:
1. Let X1, X2, . . . , Xn, Xi ∈{0, 1}, be an independent and identically
distributed (i.i.d.) sequence of coin tosses of a coin with unknown
parameter θ = Pr(Xi = 1). Given n, the number of 1’s is a sufﬁcient
statistic for θ. Here T (X1, X2, . . . , Xn) = n
i=1 Xi. In fact, we can
show that given T , all sequences having that many 1’s are equally
likely and independent of the parameter θ. Speciﬁcally,
Pr

(X1, X2, . . . , Xn) = (x1, x2, . . . , xn)

n

i=1
Xi = k

=

1
(n
k)
if  xi = k,
0
otherwise.
(2.125)
Thus, θ → Xi →(X1, X2, . . . , Xn) forms a Markov chain, and
T is a sufﬁcient statistic for θ.
The next two examples involve probability densities instead of
probability mass functions, but the theory still applies. We deﬁne
entropy and mutual information for continuous random variables in
Chapter 8.
2. If X is normally distributed with mean θ and variance 1; that is, if
fθ(x) =
1
√
2π
e−(x−θ)2/2 = N(θ, 1),
(2.126)
and X1, X2, . . . , Xn are drawn independently according to this distri-
bution, a sufﬁcient statistic for θ is the sample mean Xn = 1
n
n
i=1 Xi.
It can be veriﬁed that the conditional distribution of X1, X2, . . . , Xn,
conditioned on Xn and n does not depend on θ.


## PDF page 63

2.10
FANO’S INEQUALITY
37
3. If fθ = Uniform(θ, θ + 1), a sufﬁcient statistic for θ is
T (X1, X2, . . . , Xn)
= (max{X1, X2, . . . , Xn}, min{X1, X2, . . . , Xn}).
(2.127)
The proof of this is slightly more complicated, but again one can
show that the distribution of the data is independent of the parameter
given the statistic T .
The minimal sufﬁcient statistic is a sufﬁcient statistic that is a function
of all other sufﬁcient statistics.
Deﬁnition
A statistic T (X) is a minimal sufﬁcient statistic relative to
{fθ(x)} if it is a function of every other sufﬁcient statistic U. Interpreting
this in terms of the data-processing inequality, this implies that
θ →T (X) →U(X) →X.
(2.128)
Hence, a minimal sufﬁcient statistic maximally compresses the infor-
mation about θ in the sample. Other sufﬁcient statistics may contain
additional irrelevant information. For example, for a normal distribution
with mean θ, the pair of functions giving the mean of all odd samples and
the mean of all even samples is a sufﬁcient statistic, but not a minimal
sufﬁcient statistic. In the preceding examples, the sufﬁcient statistics are
also minimal.
2.10
FANO’S INEQUALITY
Suppose that we know a random variable Y and we wish to guess the value
of a correlated random variable X. Fano’s inequality relates the probabil-
ity of error in guessing the random variable X to its conditional entropy
H(X|Y). It will be crucial in proving the converse to Shannon’s channel
capacity theorem in Chapter 7. From Problem 2.5 we know that the con-
ditional entropy of a random variable X given another random variable
Y is zero if and only if X is a function of Y. Hence we can estimate X
from Y with zero probability of error if and only if H(X|Y) = 0.
Extending this argument, we expect to be able to estimate X with a
low probability of error only if the conditional entropy H(X|Y) is small.
Fano’s inequality quantiﬁes this idea. Suppose that we wish to estimate a
random variable X with a distribution p(x). We observe a random variable
Y that is related to X by the conditional distribution p(y|x). From Y, we


## PDF page 64

38
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
calculate a function g(Y) = ˆX, where ˆX is an estimate of X and takes on
values in ˆX. We will not restrict the alphabet ˆX to be equal to X, and we
will also allow the function g(Y) to be random. We wish to bound the
probability that ˆX ̸= X. We observe that X →Y →ˆX forms a Markov
chain. Deﬁne the probability of error
Pe = Pr
 ˆX ̸= X

.
(2.129)
Theorem 2.10.1
(Fano’s Inequality)
For any estimator ˆX such that
X →Y →ˆX, with Pe = Pr(X ̸= ˆX), we have
H(Pe) + Pe log |X| ≥H(X| ˆX) ≥H(X|Y).
(2.130)
This inequality can be weakened to
1 + Pe log |X| ≥H(X|Y)
(2.131)
or
Pe ≥H(X|Y) −1
log |X|
.
(2.132)
Remark
Note from (2.130) that Pe = 0 implies that H(X|Y) = 0, as
intuition suggests.
Proof:
We ﬁrst ignore the role of Y and prove the ﬁrst inequality in
(2.130). We will then use the data-processing inequality to prove the more
traditional form of Fano’s inequality, given by the second inequality in
(2.130). Deﬁne an error random variable,
E =

1
if ˆX ̸= X,
0
if ˆX = X.
(2.133)
Then, using the chain rule for entropies to expand H(E, X| ˆX) in two
different ways, we have
H(E, X| ˆX) = H(X| ˆX) + H(E|X, ˆX)



=0
(2.134)
= H(E| ˆX)



≤H(Pe)
+ H(X|E, ˆX)



≤Pe log |X|
.
(2.135)
Since conditioning reduces entropy, H(E| ˆX) ≤H(E) = H(Pe). Now
since E is a function of X and ˆX, the conditional entropy H(E|X, ˆX) is


