# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 105

4.3
EXAMPLE: ENTROPY RATE OF A RANDOM WALK ON A WEIGHTED GRAPH
79
In this case, the stationary distribution has a surprisingly simple form,
which we will guess and verify. The stationary distribution for this Markov
chain assigns probability to node i proportional to the total weight of the
edges emanating from node i. Let
Wi =

j
Wij
(4.29)
be the total weight of edges emanating from node i, and let
W =

i,j:j>i
Wij
(4.30)
be the sum of the weights of all the edges. Then 
i Wi = 2W.
We now guess that the stationary distribution is
µi = Wi
2W .
(4.31)
We verify that this is the stationary distribution by checking that µP = µ.
Here

i
µiPij =

i
Wi
2W
Wij
Wi
(4.32)
=

i
1
2W Wij
(4.33)
= Wj
2W
(4.34)
= µj.
(4.35)
Thus, the stationary probability of state i is proportional to the weight of
edges emanating from node i. This stationary distribution has an inter-
esting property of locality: It depends only on the total weight and the
weight of edges connected to the node and hence does not change if the
weights in some other part of the graph are changed while keeping the
total weight constant. We can now calculate the entropy rate as
H(X) = H(X2|X1)
(4.36)
= −

i
µi

j
Pij log Pij
(4.37)


## PDF page 106

80
ENTROPY RATES OF A STOCHASTIC PROCESS
= −

i
Wi
2W

j
Wij
Wi
log Wij
Wi
(4.38)
= −

i

j
Wij
2W log Wij
Wi
(4.39)
= −

i

j
Wij
2W log Wij
2W +

i

j
Wij
2W log Wi
2W
(4.40)
= H

. . . , Wij
2W , . . .

−H

. . . , Wi
2W , . . .

.
(4.41)
If all the edges have equal weight, the stationary distribution puts
weight Ei/2E on node i, where Ei is the number of edges emanating
from node i and E is the total number of edges in the graph. In this case,
the entropy rate of the random walk is
H(X) = log(2E) −H
 E1
2E , E2
2E , . . . , Em
2E

.
(4.42)
This answer for the entropy rate is so simple that it is almost mislead-
ing. Apparently, the entropy rate, which is the average transition entropy,
depends only on the entropy of the stationary distribution and the total
number of edges.
Example 4.3.1
(Random walk on a chessboard)
Let a king move at
random on an 8 × 8 chessboard. The king has eight moves in the interior,
ﬁve moves at the edges, and three moves at the corners. Using this and
the preceding results, the stationary probabilities are, respectively,
8
420,
5
420, and
3
420, and the entropy rate is 0.92 log 8. The factor of 0.92 is due
to edge effects; we would have an entropy rate of log 8 on an inﬁnite
chessboard.
Similarly, we can ﬁnd the entropy rate of rooks (log 14 bits, since the
rook always has 14 possible moves), bishops, and queens. The queen
combines the moves of a rook and a bishop. Does the queen have more
or less freedom than the pair?
Remark
It is easy to see that a stationary random walk on a graph is
time-reversible; that is, the probability of any sequence of states is the


## PDF page 107

4.4
SECOND LAW OF THERMODYNAMICS
81
same forward or backward:
Pr(X1 = x1, X2 = x2, . . . , Xn = xn)
= Pr(Xn = x1, Xn−1 = x2, . . . , X1 = xn).
(4.43)
Rather surprisingly, the converse is also true; that is, any time-reversible
Markov chain can be represented as a random walk on an undirected
weighted graph.
4.4
SECOND LAW OF THERMODYNAMICS
One of the basic laws of physics, the second law of thermodynamics,
states that the entropy of an isolated system is nondecreasing. We now
explore the relationship between the second law and the entropy function
that we deﬁned earlier in this chapter.
In statistical thermodynamics, entropy is often deﬁned as the log of
the number of microstates in the system. This corresponds exactly to our
notion of entropy if all the states are equally likely. But why does entropy
increase?
We model the isolated system as a Markov chain with transitions obey-
ing the physical laws governing the system. Implicit in this assumption is
the notion of an overall state of the system and the fact that knowing the
present state, the future of the system is independent of the past. In such
a system we can ﬁnd four different interpretations of the second law. It
may come as a shock to ﬁnd that the entropy does not always increase.
However, relative entropy always decreases.
1. Relative entropy D(µn||µ′
n) decreases with n. Let µn and µ′
n be two
probability distributions on the state space of a Markov chain at time
n, and let µn+1 and µ′
n+1 be the corresponding distributions at time
n + 1. Let the corresponding joint mass functions be denoted by
p and q. Thus, p(xn, xn+1) = p(xn)r(xn+1|xn) and q(xn, xn+1) =
q(xn)r(xn+1|xn), where r(·|·) is the probability transition function
for the Markov chain. Then by the chain rule for relative entropy,
we have two expansions:
D(p(xn, xn+1)||q(xn, xn+1)) = D(p(xn)||q(xn))
+ D(p(xn+1|xn)||q(xn+1|xn))


## PDF page 108

82
ENTROPY RATES OF A STOCHASTIC PROCESS
= D(p(xn+1)||q(xn+1))
+ D(p(xn|xn+1)||q(xn|xn+1)).
Since both p and q are derived from the Markov chain, the con-
ditional probability mass functions p(xn+1|xn) and q(xn+1|xn) are
both equal to r(xn+1|xn), and hence D(p(xn+1|xn)||q(xn+1|xn)) = 0.
Now using the nonnegativity of D(p(xn|xn+1)||q(xn|xn+1)) (Corol-
lary to Theorem 2.6.3), we have
D(p(xn)||q(xn)) ≥D(p(xn+1)||q(xn+1))
(4.44)
or
D(µn||µ′
n) ≥D(µn+1||µ′
n+1).
(4.45)
Consequently, the distance between the probability mass functions
is decreasing with time n for any Markov chain.
An example of one interpretation of the preceding inequality is
to suppose that the tax system for the redistribution of wealth is
the same in Canada and in England. Then if µn and µ′
n represent
the distributions of wealth among people in the two countries, this
inequality shows that the relative entropy distance between the two
distributions decreases with time. The wealth distributions in Canada
and England become more similar.
2. Relative entropy D(µn||µ) between a distribution µn on the states at
time n and a stationary distribution µ decreases with n. In (4.45),
µ′
n is any distribution on the states at time n. If we let µ′
n be any
stationary distribution µ, the distribution µ′
n+1 at the next time is
also equal to µ. Hence,
D(µn||µ) ≥D(µn+1||µ),
(4.46)
which implies that any state distribution gets closer and closer to
each stationary distribution as time passes. The sequence D(µn||µ)
is a monotonically nonincreasing nonnegative sequence and must
therefore have a limit. The limit is zero if the stationary distribution
is unique, but this is more difﬁcult to prove.
3. Entropy increases if the stationary distribution is uniform. In gen-
eral, the fact that the relative entropy decreases does not imply that
the entropy increases. A simple counterexample is provided by any
Markov chain with a nonuniform stationary distribution. If we start


## PDF page 109

4.4
SECOND LAW OF THERMODYNAMICS
83
this Markov chain from the uniform distribution, which already is
the maximum entropy distribution, the distribution will tend to the
stationary distribution, which has a lower entropy than the uniform.
Here, the entropy decreases with time.
If, however, the stationary distribution is the uniform distribution,
we can express the relative entropy as
D(µn||µ) = log |X| −H(µn) = log |X| −H(Xn).
(4.47)
In this case the monotonic decrease in relative entropy implies a
monotonic increase in entropy. This is the explanation that ties in
most closely with statistical thermodynamics, where all the micro-
states are equally likely. We now characterize processes having a
uniform stationary distribution.
Deﬁnition
A probability transition matrix [Pij], Pij = Pr{Xn+1 =
j|Xn = i}, is called doubly stochastic if

i
Pij = 1,
j = 1, 2, . . .
(4.48)
and

j
Pij = 1,
i = 1, 2, . . . .
(4.49)
Remark
The uniform distribution is a stationary distribution of P if
and only if the probability transition matrix is doubly stochastic (see
Problem 4.1).
4. The conditional entropy H(Xn|X1) increases with n for a station-
ary Markov process. If the Markov process is stationary, H(Xn) is
constant. So the entropy is nonincreasing. However, we will prove
that H(Xn|X1) increases with n. Thus, the conditional uncertainty
of the future increases. We give two alternative proofs of this result.
First, we use the properties of entropy,
H(Xn|X1) ≥H(Xn|X1, X2)
(conditioning reduces entropy)
(4.50)
= H(Xn|X2)
(by Markovity)
(4.51)
= H(Xn−1|X1)
(by stationarity).
(4.52)


## PDF page 110

84
ENTROPY RATES OF A STOCHASTIC PROCESS
Alternatively, by an application of the data-processing inequality to
the Markov chain X1 →Xn−1 →Xn, we have
I (X1; Xn−1) ≥I (X1; Xn).
(4.53)
Expanding the mutual informations in terms of entropies, we have
H(Xn−1) −H(Xn−1|X1) ≥H(Xn) −H(Xn|X1).
(4.54)
By stationarity, H(Xn−1) = H(Xn), and hence we have
H(Xn−1|X1) ≤H(Xn|X1).
(4.55)
[These techniques can also be used to show that H(X0|Xn) is
increasing in n for any Markov chain.]
5. Shufﬂes increase entropy. If T is a shufﬂe (permutation) of a deck
of cards and X is the initial (random) position of the cards in the
deck, and if the choice of the shufﬂe T is independent of X, then
H(T X) ≥H(X),
(4.56)
where T X is the permutation of the deck induced by the shufﬂe T
on the initial permutation X. Problem 4.3 outlines a proof.
4.5
FUNCTIONS OF MARKOV CHAINS
Here is an example that can be very difﬁcult if done the wrong
way. It illustrates the power of the techniques developed so far. Let
X1, X2, . . . , Xn, . . . be a stationary Markov chain, and let Yi = φ(Xi) be
a process each term of which is a function of the corresponding state
in the Markov chain. What is the entropy rate H(Y)? Such functions of
Markov chains occur often in practice. In many situations, one has only
partial information about the state of the system. It would simplify matters
greatly if Y1, Y2, . . . , Yn also formed a Markov chain, but in many cases,
this is not true. Since the Markov chain is stationary, so is Y1, Y2, . . . , Yn,
and the entropy rate is well deﬁned. However, if we wish to compute
H(Y), we might compute H(Yn|Yn−1, . . . , Y1) for each n and ﬁnd the
limit. Since the convergence can be arbitrarily slow, we will never know
how close we are to the limit. (We can’t look at the change between the
values at n and n + 1, since this difference may be small even when we
are far away from the limit—consider, for example,  1
n.)


## PDF page 111

4.5
FUNCTIONS OF MARKOV CHAINS
85
It would be useful computationally to have upper and lower bounds con-
verging to the limit from above and below. We can halt the computation
when the difference between upper and lower bounds is small, and we
will then have a good estimate of the limit.
We already know that H(Yn|Yn−1, . . . , Y1) converges monoton-
ically
to
H(Y)
from
above.
For
a
lower
bound,
we
will
use
H(Yn|Yn−1, . . . , Y1, X1). This is a neat trick based on the idea that X1
contains as much information about Yn as Y1, Y0, Y−1, . . . .
Lemma 4.5.1
H(Yn|Yn−1, . . . , Y2, X1) ≤H(Y).
(4.57)
Proof:
We have for k = 1, 2, . . . ,
H(Yn|Yn−1, . . . , Y2, X1)
(a)
= H(Yn|Yn−1, . . . , Y2, Y1, X1)
(4.58)
(b)
= H(Yn|Yn−1, . . . , Y1, X1, X0, X−1, . . . , X−k)
(4.59)
(c)
= H(Yn|Yn−1, . . . , Y1, X1, X0, X−1, . . . ,
X−k, Y0, . . . , Y−k)
(4.60)
(d)
≤H(Yn|Yn−1, . . . , Y1, Y0, . . . , Y−k)
(4.61)
(e)
= H(Yn+k+1|Yn+k, . . . , Y1),
(4.62)
where (a) follows from that fact that Y1 is a function of X1, and (b) follows
from the Markovity of X, (c) follows from the fact that Yi is a function
of Xi, (d) follows from the fact that conditioning reduces entropy, and (e)
follows by stationarity. Since the inequality is true for all k, it is true in
the limit. Thus,
H(Yn|Yn−1, . . . , Y1, X1) ≤lim
k H(Yn+k+1|Yn+k, . . . , Y1)
(4.63)
= H(Y).
□
(4.64)
The next lemma shows that the interval between the upper and the
lower bounds decreases in length.
Lemma 4.5.2
H(Yn|Yn−1, . . . , Y1) −H(Yn|Yn−1, . . . , Y1, X1) →0.
(4.65)


## PDF page 112

86
ENTROPY RATES OF A STOCHASTIC PROCESS
Proof:
The interval length can be rewritten as
H(Yn|Yn−1, . . . , Y1) −H(Yn|Yn−1, . . . , Y1, X1)
= I (X1; Yn|Yn−1, . . . , Y1).
(4.66)
By the properties of mutual information,
I (X1; Y1, Y2, . . . , Yn) ≤H(X1),
(4.67)
and I (X1; Y1, Y2, . . . , Yn) increases with n. Thus, lim I (X1; Y1, Y2, . . . ,
Yn) exists and
lim
n→∞I (X1; Y1, Y2, . . . , Yn) ≤H(X1).
(4.68)
By the chain rule,
H(X) ≥lim
n→∞I (X1; Y1, Y2, . . . , Yn)
(4.69)
= lim
n→∞
n

i=1
I (X1; Yi|Yi−1, . . . , Y1)
(4.70)
=
∞

i=1
I (X1; Yi|Yi−1, . . . , Y1).
(4.71)
Since this inﬁnite sum is ﬁnite and the terms are nonnegative, the terms
must tend to 0; that is,
lim I (X1; Yn|Yn−1, . . . , Y1) = 0,
(4.72)
which proves the lemma.
□
Combining Lemmas 4.5.1 and 4.5.2, we have the following theorem.
Theorem 4.5.1
If X1, X2, . . . , Xn form a stationary Markov chain, and
Yi = φ(Xi), then
H(Yn|Yn−1, . . . , Y1, X1) ≤H(Y) ≤H(Yn|Yn−1, . . . , Y1)
(4.73)
and
lim H(Yn|Yn−1, . . . , Y1, X1) = H(Y) = lim H(Yn|Yn−1, . . . , Y1). (4.74)
In general, we could also consider the case where Yi is a stochastic
function (as opposed to a deterministic function) of Xi. Consider a Markov


