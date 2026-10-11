# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 121

PROBLEMS
95
following recursion:


X1(n)
X2(n)
X3(n)

=


0
1
1
1
0
0
0
1
0




X1(n −1)
X2(n −1)
X3(n −1)

,
(4.101)
with initial conditions X(1) = [1 1 0]t.
(c) Let
A =


0
1
1
1
0
0
0
1
0

.
(4.102)
Then we have by induction
X(n) = AX(n −1) = A2X(n −2) = · · · = An−1X(1).
(4.103)
Using the eigenvalue decomposition of A for the case of distinct
eigenvalues, we can write A = U −1U, where  is the diag-
onal matrix of eigenvalues. Then An−1 = U −1n−1U. Show
that we can write
X(n) = λn−1
1
Y1 + λn−1
2
Y2 + λn−1
3
Y3,
(4.104)
where Y1, Y2, Y3 do not depend on n. For large n, this sum
is dominated by the largest term. Therefore, argue that for i =
1, 2, 3, we have
1
n log Xi(n) →log λ,
(4.105)
where λ is the largest (positive) eigenvalue. Thus, the number
of sequences of length n grows as λn for large n. Calculate λ
for the matrix A above. (The case when the eigenvalues are
not distinct can be handled in a similar manner.)
(d) We now take a different approach. Consider a Markov chain
whose state diagram is the one given in part (a), but with
arbitrary transition probabilities. Therefore, the probability tran-
sition matrix of this Markov chain is
P =


0
1
0
α
0
1 −α
1
0
0

.
(4.106)
Show that the stationary distribution of this Markov chain is
µ =

1
3 −α,
1
3 −α, 1 −α
3 −α

.
(4.107)


## PDF page 122

96
ENTROPY RATES OF A STOCHASTIC PROCESS
(e) Maximize the entropy rate of the Markov chain over choices
of α. What is the maximum entropy rate of the chain?
(f) Compare the maximum entropy rate in part (e) with log λ in
part (c). Why are the two answers the same?
4.17
Recurrence times are insensitive to distributions.
Let X0, X1, X2,
. . . be drawn i.i.d. ∼p(x), x ∈X = {1, 2, . . . , m}, and let N be the
waiting time to the next occurrence of X0. Thus N = minn{Xn =
X0}.
(a) Show that EN = m.
(b) Show that E log N ≤H(X).
(c) (Optional) Prove part (a) for {Xi} stationary and ergodic.
4.18
Stationary but not ergodic process.
A bin has two biased coins,
one with probability of heads p and the other with probability of
heads 1 −p. One of these coins is chosen at random (i.e., with
probability 1
2) and is then tossed n times. Let X denote the identity
of the coin that is picked, and let Y1 and Y2 denote the results of
the ﬁrst two tosses.
(a) Calculate I (Y1; Y2|X).
(b) Calculate I (X; Y1, Y2).
(c) Let H(Y) be the entropy rate of the Y process (the se-
quence of coin tosses). Calculate H(Y). [Hint: Relate this to
lim 1
nH(X, Y1, Y2, . . . , Yn).]
You can check the answer by considering the behavior as p →1
2.
4.19
Random walk on graph.
Consider a random walk on the following
graph:
1
5
4
3
2
(a) Calculate the stationary distribution.


## PDF page 123

PROBLEMS
97
(b) What is the entropy rate?
(c) Find the mutual information I (Xn+1; Xn) assuming that the
process is stationary.
4.20
Random walk on chessboard.
Find the entropy rate of the Markov
chain associated with a random walk of a king on the 3 × 3 chess-
board
1
2
3
4
5
6
7
8
9
What about the entropy rate of rooks, bishops, and queens? There
are two types of bishops.
4.21
Maximal entropy graphs.
Consider a random walk on a connected
graph with four edges.
(a) Which graph has the highest entropy rate?
(b) Which graph has the lowest?
4.22
Three-dimensional maze.
A bird is lost in a 3 × 3 × 3 cubical
maze. The bird ﬂies from room to room going to adjoining rooms
with equal probability through each of the walls. For example, the
corner rooms have three exits.
(a) What is the stationary distribution?
(b) What is the entropy rate of this random walk?
4.23
Entropy rate.
Let {Xi} be a stationary stochastic process with
entropy rate H(X).
(a) Argue that H(X) ≤H(X1).
(b) What are the conditions for equality?
4.24
Entropy rates.
Let {Xi} be a stationary process. Let Yi = (Xi,
Xi+1). Let Zi = (X2i, X2i+1). Let Vi = X2i. Consider the entropy
rates H(X), H(Y), H(Z), and H(V) of the processes {Xi},{Yi},
{Zi}, and {Vi}. What is the inequality relationship ≤, =, or ≥
between each of the pairs listed below?
(a) H(X)⩾<H(Y).
(b) H(X)⩾<H(Z).
(c) H(X)⩾<H(V).
(d) H(Z)⩾<H(X).
4.25
Monotonicity
(a) Show that I (X; Y1, Y2, . . . , Yn) is nondecreasing in n.


## PDF page 124

98
ENTROPY RATES OF A STOCHASTIC PROCESS
(b) Under what conditions is the mutual information constant for
all n?
4.26
Transitions in Markov chains.
Suppose that {Xi} forms an irre-
ducible Markov chain with transition matrix P and stationary distri-
bution µ. Form the associated “edge process” {Yi} by keeping track
only of the transitions. Thus, the new process {Yi} takes values in
X × X, and Yi = (Xi−1, Xi). For example,
Xn = 3, 2, 8, 5, 7, . . .
becomes
Y n = (∅, 3), (3, 2), (2, 8), (8, 5), (5, 7), . . . .
Find the entropy rate of the edge process {Yi}.
4.27
Entropy rate.
Let {Xi} be a stationary {0, 1}-valued stochastic
process obeying
Xk+1 = Xk ⊕Xk−1 ⊕Zk+1,
where {Zi} is Bernoulli(p)and ⊕denotes mod 2 addition. What is
the entropy rate H(X)?
4.28
Mixture of processes.
Suppose that we observe one of two
stochastic processes but don’t know which. What is the entropy
rate? Speciﬁcally, let X11, X12, X13, . . . be a Bernoulli process with
parameter p1, and let X21, X22, X23, . . . be Bernoulli(p2). Let
θ =

1
with probability 1
2
2
with probability 1
2
and let Yi = Xθi, i = 1, 2, . . . , be the stochastic process observed.
Thus, Y observes the process {X1i} or {X2i}. Eventually, Y will
know which.
(a) Is {Yi} stationary?
(b) Is {Yi} an i.i.d. process?
(c) What is the entropy rate H of {Yi}?
(d) Does
−1
n log p(Y1, Y2, . . . Yn) −→H?
(e) Is there a code that achieves an expected per-symbol description
length 1
nELn −→H?


## PDF page 125

PROBLEMS
99
Now let θi be Bern(1
2). Observe that
Zi = Xθii,
i = 1, 2, . . . .
Thus, θ is not ﬁxed for all time, as it was in the ﬁrst part, but is
chosen i.i.d. each time. Answer parts (a), (b), (c), (d), (e) for the
process {Zi}, labeling the answers (a′), (b′), (c′), (d′), (e′).
4.29
Waiting times.
Let X be the waiting time for the ﬁrst heads to
appear in successive ﬂips of a fair coin. For example, Pr{X = 3} =
( 1
2)3. Let Sn be the waiting time for the nth head to appear. Thus,
S0 = 0
Sn+1 = Sn + Xn+1,
where X1, X2, X3, . . . are i.i.d according to the distribution above.
(a) Is the process {Sn} stationary?
(b) Calculate H(S1, S2, . . . , Sn).
(c) Does the process {Sn} have an entropy rate? If so, what is it?
If not, why not?
(d) What is the expected number of fair coin ﬂips required to
generate a random variable having the same distribution as Sn?
4.30
Markov chain transitions
P = [Pij] =


1
2
1
4
1
4
1
4
1
2
1
4
1
4
1
4
1
2

.
Let X1 be distributed uniformly over the states {0, 1, 2}. Let {Xi}∞
1
be a Markov chain with transition matrix P ; thus, P (Xn+1 =
j|Xn = i) = Pij, i, j ∈{0, 1, 2}.
(a) Is {Xn} stationary?
(b) Find limn→∞1
nH(X1, . . . , Xn).
Now consider the derived process Z1, Z2, . . . , Zn, where
Z1 = X1
Zi = Xi −Xi−1
(mod 3),
i = 2, . . . , n.
Thus, Zn encodes the transitions, not the states.
(c) Find H(Z1, Z2, . . . , Zn).
(d) Find H(Zn) and H(Xn) for n ≥2.


## PDF page 126

100
ENTROPY RATES OF A STOCHASTIC PROCESS
(e) Find H(Zn|Zn−1) for n ≥2.
(f) Are Zn−1 and Zn independent for n ≥2?
4.31
Markov.
Let
{Xi} ∼Bernoulli(p).
Consider
the
associated
Markov chain {Yi}n
i=1, where
Yi = (the number of 1’s in the current run of 1’s). For example, if
Xn = 101110 . . . , we have Y n = 101230 . . . .
(a) Find the entropy rate of Xn.
(b) Find the entropy rate of Y n.
4.32
Time symmetry.
Let {Xn} be a stationary Markov process. We
condition on (X0, X1) and look into the past and future. For what
index k is
H(X−n|X0, X1) = H(Xk|X0, X1)?
Give the argument.
4.33
Chain inequality.
Let X1 →X2 →X3 →X4 form a Markov
chain. Show that
I (X1; X3) + I (X2; X4) ≤I (X1; X4) + I (X2; X3).
(4.108)
4.34
Broadcast channel.
Let X →Y →(Z, W) form a Markov chain
[i.e., p(x, y, z, w) = p(x)p(y|x)p(z, w|y) for all x, y, z, w]. Show
that
I (X; Z) + I (X; W) ≤I (X; Y) + I (Z; W).
(4.109)
4.35
Concavity of second law.
Let {Xn}∞
−∞be a stationary Markov
process. Show that H(Xn|X0) is concave in n. Speciﬁcally, show
that
H(Xn|X0) −H(Xn−1|X0) −(H(Xn−1|X0) −H(Xn−2|X0))
= −I (X1; Xn−1|X0, Xn) ≤0.
(4.110)
Thus, the second difference is negative, establishing that H(Xn|X0)
is a concave function of n.
HISTORICAL NOTES
The entropy rate of a stochastic process was introduced by Shannon [472],
who also explored some of the connections between the entropy rate of the
process and the number of possible sequences generated by the process.
Since Shannon, there have been a number of results extending the basic


## PDF page 127

HISTORICAL NOTES
101
theorems of information theory to general stochastic processes. The AEP
for a general stationary stochastic process is proved in Chapter 16.
Hidden Markov models are used for a number of applications, such
as speech recognition [432]. The calculation of the entropy rate for con-
strained sequences was introduced by Shannon [472]. These sequences
are used for coding for magnetic and optical channels [288].


## PDF page 128



