# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 73

PROBLEMS
47
p(x1, x2, x3) = p(x1)p(x2|x1)p(x3|x2), for all x1 ∈{1, 2, . . . , n},
x2 ∈{1, 2, . . . , k}, x3 ∈{1, 2, . . . , m}.
(a) Show that the dependence of X1 and X3 is limited by the
bottleneck by proving that I (X1; X3) ≤log k.
(b) Evaluate I (X1; X3) for k = 1, and conclude that no depen-
dence can survive such a bottleneck.
2.17
Pure randomness and bent coins.
Let X1, X2, . . . , Xn denote the
outcomes of independent ﬂips of a bent coin. Thus, Pr {Xi =
1} = p, Pr {Xi = 0} = 1 −p, where p is unknown. We wish
to obtain a sequence Z1, Z2, . . . , ZK of fair coin ﬂips from
X1, X2, . . . , Xn. Toward this end, let f : Xn →{0, 1}∗(where
{0, 1}∗= {, 0, 1, 00, 01, . . .} is the set of all ﬁnite-length binary
sequences) be a mapping f (X1, X2, . . . , Xn) = (Z1, Z2, . . . , ZK),
where Zi ∼Bernoulli ( 1
2), and K may depend on (X1, . . . , Xn).
In order that the sequence Z1, Z2, . . . appear to be fair coin ﬂips,
the map f from bent coin ﬂips to fair ﬂips must have the prop-
erty that all 2k sequences (Z1, Z2, . . . , Zk) of a given length k
have equal probability (possibly 0), for k = 1, 2, . . .. For example,
for n = 2, the map f (01) = 0, f (10) = 1, f (00) = f (11) = 
(the null string) has the property that Pr{Z1 = 1|K = 1} = Pr{Z1 =
0|K = 1} = 1
2. Give reasons for the following inequalities:
nH(p)
(a)
= H(X1, . . . , Xn)
(b)
≥H(Z1, Z2, . . . , ZK, K)
(c)
= H(K) + H(Z1, . . . , ZK|K)
(d)
= H(K) + E(K)
(e)
≥EK.
Thus, no more than nH(p) fair coin tosses can be derived from
(X1, . . . , Xn), on the average. Exhibit a good map f on sequences
of length 4.
2.18
World Series.
The World Series is a seven-game series that termi-
nates as soon as either team wins four games. Let X be the random
variable that represents the outcome of a World Series between
teams A and B; possible values of X are AAAA, BABABAB, and
BBBAAAA. Let Y be the number of games played, which ranges
from 4 to 7. Assuming that A and B are equally matched and that


## PDF page 74

48
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
the games are independent, calculate H(X), H(Y), H(Y|X), and
H(X|Y).
2.19
Inﬁnite entropy.
This problem shows that the entropy of a discrete
random variable can be inﬁnite. Let A = ∞
n=2(n log2 n)−1. [It is
easy to show that A is ﬁnite by bounding the inﬁnite sum by the
integral of (x log2 x)−1.] Show that the integer-valued random vari-
able X deﬁned by Pr(X = n) = (An log2 n)−1 for n = 2, 3, . . .,
has H(X) = +∞.
2.20
Run-length coding.
Let X1, X2, . . . , Xn be (possibly dependent)
binary random variables. Suppose that one calculates the run
lengths R = (R1, R2, . . .) of this sequence (in order as they
occur). For example, the sequence X = 0001100100 yields run
lengths R = (3, 2, 2, 1, 2). Compare H(X1, X2, . . . , Xn), H(R),
and H(Xn, R). Show all equalities and inequalities, and bound all
the differences.
2.21
Markov’s inequality for probabilities.
Let p(x) be a probability
mass function. Prove, for all d ≥0, that
Pr {p(X) ≤d} log 1
d ≤H(X).
(2.175)
2.22
Logical order of ideas.
Ideas have been developed in order of
need and then generalized if necessary. Reorder the following ideas,
strongest ﬁrst, implications following:
(a) Chain rule for I (X1, . . . , Xn; Y), chain rule for D(p(x1, . . . ,
xn)||q(x1, x2, . . . , xn)), and chain rule for H(X1, X2, . . . , Xn).
(b) D(f ||g) ≥0, Jensen’s inequality, I (X; Y) ≥0.
2.23
Conditional mutual information.
Consider a sequence of n binary
random variables X1, X2, . . . , Xn. Each sequence with an even
number of 1’s has probability 2−(n−1), and each sequence with an
odd number of 1’s has probability 0. Find the mutual informations
I (X1; X2),
I (X2; X3|X1), . . . , I (Xn−1; Xn|X1, . . . , Xn−2).
2.24
Average entropy.
Let H(p) = −p log2 p −(1 −p) log2(1 −p)
be the binary entropy function.
(a) Evaluate H( 1
4) using the fact that log2 3 ≈1.584. (Hint: You
may wish to consider an experiment with four equally likely
outcomes, one of which is more interesting than the others.)


## PDF page 75

PROBLEMS
49
(b) Calculate the average entropy H(p) when the probability p is
chosen uniformly in the range 0 ≤p ≤1.
(c) (Optional) Calculate the average entropy H(p1, p2, p3), where
(p1, p2, p3) is a uniformly distributed probability vector. Gen-
eralize to dimension n.
2.25
Venn diagrams.
There isn’t really a notion of mutual information
common to three random variables. Here is one attempt at a deﬁni-
tion: Using Venn diagrams, we can see that the mutual information
common to three random variables X, Y, and Z can be deﬁned by
I (X; Y; Z) = I (X; Y) −I (X; Y|Z) .
This quantity is symmetric in X, Y, and Z, despite the preceding
asymmetric deﬁnition. Unfortunately, I (X; Y; Z) is not necessar-
ily nonnegative. Find X, Y, and Z such that I (X; Y; Z) < 0, and
prove the following two identities:
(a) I (X; Y; Z) = H(X, Y, Z) −H(X) −H(Y) −H(Z) +
I (X; Y) + I (Y; Z) + I (Z; X).
(b) I (X; Y; Z) = H(X, Y, Z) −H(X, Y) −H(Y, Z) −
H(Z, X) + H(X) + H(Y) + H(Z).
The ﬁrst identity can be understood using the Venn diagram analogy
for entropy and mutual information. The second identity follows
easily from the ﬁrst.
2.26
Another proof of nonnegativity of relative entropy.
In view of the
fundamental nature of the result D(p||q) ≥0, we will give another
proof.
(a) Show that ln x ≤x −1 for 0 < x < ∞.
(b) Justify the following steps:
−D(p||q) =

x
p(x) ln q(x)
p(x)
(2.176)
≤

x
p(x)
q(x)
p(x) −1

(2.177)
≤0.
(2.178)
(c) What are the conditions for equality?
2.27
Grouping rule for entropy.
Let p = (p1, p2, . . . , pm) be a prob-
ability distribution on m elements (i.e., pi ≥0 and m
i=1 pi = 1).


## PDF page 76

50
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Deﬁne a new distribution q on m −1 elements as q1 = p1, q2 = p2,
. . . , qm−2 = pm−2, and qm−1 = pm−1 + pm [i.e., the distribution q
is the same as p on {1, 2, . . . , m −2}, and the probability of the
last element in q is the sum of the last two probabilities of p].
Show that
H(p) = H(q) + (pm−1 + pm)H

pm−1
pm−1 + pm
,
pm
pm−1 + pm

.
(2.179)
2.28
Mixing increases entropy.
Show that the entropy of the proba-
bility distribution, (p1, . . . , pi, . . . , pj, . . . , pm), is less than the
entropy
of
the
distribution
(p1, . . . , pi+pj
2
, . . . , pi+pj
2
,
. . . , pm). Show that in general any transfer of probability that
makes the distribution more uniform increases the entropy.
2.29
Inequalities.
Let X, Y, and Z be joint random variables. Prove
the following inequalities and ﬁnd conditions for equality.
(a) H(X, Y|Z) ≥H(X|Z).
(b) I (X, Y; Z) ≥I (X; Z).
(c) H(X, Y, Z) −H(X, Y) ≤H(X, Z) −H(X).
(d) I (X; Z|Y) ≥I (Z; Y|X) −I (Z; Y) + I (X; Z).
2.30
Maximum entropy.
Find the probability mass function p(x) that
maximizes the entropy H(X) of a nonnegative integer-valued ran-
dom variable X subject to the constraint
EX =
∞

n=0
np(n) = A
for a ﬁxed value A > 0. Evaluate this maximum H(X).
2.31
Conditional entropy.
Under what conditions does H(X|g(Y)) =
H(X|Y)?
2.32
Fano.
We are given the following joint distribution on (X, Y):


## PDF page 77

PROBLEMS
51
Let
ˆX(Y) be an estimator for X (based on Y) and let Pe =
Pr{ ˆX(Y) ̸= X}.
(a) Find the minimum probability of error estimator ˆX(Y) and the
associated Pe.
(b) Evaluate Fano’s inequality for this problem and compare.
2.33
Fano’s inequality.
Let Pr(X = i) = pi, i = 1, 2, . . . , m, and let
p1 ≥p2 ≥p3 ≥· · · ≥pm. The minimal probability of error pre-
dictor of X is ˆX = 1, with resulting probability of error Pe =
1 −p1. Maximize H(p) subject to the constraint 1 −p1 = Pe to
ﬁnd a bound on Pe in terms of H. This is Fano’s inequality in the
absence of conditioning.
2.34
Entropy of initial conditions.
Prove that H(X0|Xn) is nondecreas-
ing with n for any Markov chain.
2.35
Relative entropy is not symmetric.
Let the random variable X have three possible outcomes {a, b, c}.
Consider two distributions on this random variable:
Symbol
p(x)
q(x)
a
1
2
1
3
b
1
4
1
3
c
1
4
1
3
Calculate H(p), H(q), D(p||q), and D(q||p). Verify that in this
case, D(p||q) ̸= D(q||p).
2.36
Symmetric relative entropy.
Although, as Problem 2.35 shows,
D(p||q) ̸= D(q||p) in general, there could be distributions for
which equality holds. Give an example of two distributions p and
q on a binary alphabet such that D(p||q) = D(q||p) (other than
the trivial case p = q).
2.37
Relative entropy.
Let X, Y, Z be three random variables with a
joint probability mass function p(x, y, z). The relative entropy
between the joint distribution and the product of the marginals is
D(p(x, y, z)||p(x)p(y)p(z)) = E

log
p(x, y, z)
p(x)p(y)p(z)

. (2.180)
Expand this in terms of entropies. When is this quantity zero?


## PDF page 78

52
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
2.38
The value of a question.
Let X ∼p(x), x = 1, 2, . . . , m. We are
given a set S ⊆{1, 2, . . . , m}. We ask whether X ∈S and receive
the answer
Y =

1
if X ∈S
0
if X ̸∈S.
Suppose that Pr{X ∈S} = α. Find the decrease in uncertainty
H(X) −H(X|Y).
Apparently, any set S with a given α is as good as any other.
2.39
Entropy and pairwise independence.
Let X, Y, Z be three binary
Bernoulli(1
2) random variables that are pairwise independent; that
is, I (X; Y) = I (X; Z) = I (Y; Z) = 0.
(a) Under this constraint, what is the minimum value for
H(X, Y, Z)?
(b) Give an example achieving this minimum.
2.40
Discrete entropies.
Let X and Y be two independent integer-
valued random variables. Let X be uniformly distributed over {1, 2,
. . . , 8}, and let Pr{Y = k} = 2−k, k = 1, 2, 3, . . ..
(a) Find H(X).
(b) Find H(Y).
(c) Find H(X + Y, X −Y).
2.41
Random questions.
One wishes to identify a random object X ∼
p(x). A question Q ∼r(q) is asked at random according to r(q).
This results in a deterministic answer A = A(x, q) ∈{a1, a2, . . .}.
Suppose that X and Q are independent. Then I (X; Q, A) is the
uncertainty in X removed by the question–answer (Q, A).
(a) Show that I (X; Q, A) = H(A|Q). Interpret.
(b) Now suppose that two i.i.d. questions Q1, Q2, ∼r(q) are
asked, eliciting answers A1 and A2. Show that two questions
are less valuable than twice a single question in the sense that
I (X; Q1, A1, Q2, A2) ≤2I (X; Q1, A1).
2.42
Inequalities.
Which of the following inequalities are generally
≥, =, ≤? Label each with ≥, =, or ≤.
(a) H(5X) vs. H(X)
(b) I (g(X); Y) vs. I (X; Y)
(c) H(X0|X−1) vs. H(X0|X−1, X1)
(d) H(X, Y)/(H(X) + H(Y)) vs. 1


## PDF page 79

PROBLEMS
53
2.43
Mutual information of heads and tails
(a) Consider a fair coin ﬂip. What is the mutual information
between the top and bottom sides of the coin?
(b) A six-sided fair die is rolled. What is the mutual information
between the top side and the front face (the side most facing
you)?
2.44
Pure randomness.
We wish to use a three-sided coin to generate
a fair coin toss. Let the coin X have probability mass function
X =



A,
pA
B,
pB
C,
pC,
where pA, pB, pC are unknown.
(a) How would you use two independent ﬂips X1, X2 to generate
(if possible) a Bernoulli(1
2) random variable Z?
(b) What is the resulting maximum expected number of fair bits
generated?
2.45
Finite entropy.
Show that for a discrete random variable X ∈
{1, 2, . . .}, if E log X < ∞, then H(X) < ∞.
2.46
Axiomatic deﬁnition of entropy (Difﬁcult).
If we assume certain
axioms for our measure of information, we will be forced to use a
logarithmic measure such as entropy. Shannon used this to justify
his initial deﬁnition of entropy. In this book we rely more on the
other properties of entropy rather than its axiomatic derivation to
justify its use. The following problem is considerably more difﬁcult
than the other problems in this section.
If a sequence of symmetric functions Hm(p1, p2, . . . , pm) satisﬁes
the following properties:
• Normalization: H2
1
2, 1
2

= 1,
• Continuity: H2(p, 1 −p) is a continuous function of p,
• Grouping: Hm(p1, p2, . . . , pm) = Hm−1(p1 + p2, p3, . . . , pm) +
(p1 + p2)H2

p1
p1+p2,
p2
p1+p2

,
prove that Hm must be of the form
Hm(p1, p2, . . . , pm) = −
m

i=1
pi log pi,
m = 2, 3, . . . .
(2.181)


## PDF page 80

54
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
There are various other axiomatic formulations which result in the
same deﬁnition of entropy. See, for example, the book by Csisz´ar
and K¨orner [149].
2.47
Entropy of a missorted ﬁle.
A deck of n cards in order 1, 2, . . . , n
is provided. One card is removed at random, then replaced at ran-
dom. What is the entropy of the resulting deck?
2.48
Sequence length.
How much information does the length of a
sequence give about the content of a sequence? Suppose that we
consider a Bernoulli (1
2) process {Xi}. Stop the process when the
ﬁrst 1 appears. Let N designate this stopping time. Thus, XN is an
element of the set of all ﬁnite-length binary sequences {0, 1}∗=
{0, 1, 00, 01, 10, 11, 000, . . . }.
(a) Find I (N; XN).
(b) Find H(XN|N).
(c) Find H(XN).
Let’s now consider a different stopping time. For this part, again
assume that Xi ∼Bernoulli( 1
2) but stop at time N = 6, with prob-
ability
1
3 and stop at time N = 12 with probability
2
3. Let this
stopping time be independent of the sequence X1X2 · · · X12.
(d) Find I (N; XN).
(e) Find H(XN|N).
(f) Find H(XN).
HISTORICAL NOTES
The concept of entropy was introduced in thermodynamics, where it
was used to provide a statement of the second law of thermodynam-
ics. Later, statistical mechanics provided a connection between thermo-
dynamic entropy and the logarithm of the number of microstates in a
macrostate of the system. This work was the crowning achievement of
Boltzmann, who had the equation S = k ln W inscribed as the epitaph on
his gravestone [361].
In the 1930s, Hartley introduced a logarithmic measure of informa-
tion for communication. His measure was essentially the logarithm of the
alphabet size. Shannon [472] was the ﬁrst to deﬁne entropy and mutual
information as deﬁned in this chapter. Relative entropy was ﬁrst deﬁned
by Kullback and Leibler [339]. It is known under a variety of names,
including the Kullback–Leibler distance, cross entropy, information diver-
gence, and information for discrimination, and has been studied in detail
by Csisz´ar [138] and Amari [22].


