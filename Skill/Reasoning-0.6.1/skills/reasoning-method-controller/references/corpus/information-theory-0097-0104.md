# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 97

CHAPTER 4
ENTROPY RATES
OF A STOCHASTIC PROCESS
The asymptotic equipartition property in Chapter 3 establishes that
nH(X) bits sufﬁce on the average to describe n independent and iden-
tically distributed random variables. But what if the random variables
are dependent? In particular, what if the random variables form a sta-
tionary process? We will show, just as in the i.i.d. case, that the entropy
H(X1, X2, . . . , Xn) grows (asymptotically) linearly with n at a rate H(X),
which we will call the entropy rate of the process. The interpretation of
H(X) as the best achievable data compression will await the analysis in
Chapter 5.
4.1
MARKOV CHAINS
A stochastic process {Xi} is an indexed sequence of random variables.
In general, there can be an arbitrary dependence among the random vari-
ables. The process is characterized by the joint probability mass functions
Pr{(X1, X2, . . . , Xn) = (x1, x2, . . . , xn)}= p(x1, x2, . . . , xn), (x1, x2, . . . ,
xn) ∈Xn for n = 1, 2, . . . .
Deﬁnition
A stochastic process is said to be stationary if the joint
distribution of any subset of the sequence of random variables is invariant
with respect to shifts in the time index; that is,
Pr{X1 = x1, X2 = x2, . . . , Xn = xn}
= Pr{X1+l = x1, X2+l = x2, . . . , Xn+l = xn}
(4.1)
for every n and every shift l and for all x1, x2, . . . , xn ∈X.
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
71


## PDF page 98

72
ENTROPY RATES OF A STOCHASTIC PROCESS
A simple example of a stochastic process with dependence is one in
which each random variable depends only on the one preceding it and
is conditionally independent of all the other preceding random variables.
Such a process is said to be Markov.
Deﬁnition
A discrete stochastic process X1, X2, . . . is said to be a
Markov chain or a Markov process if for n = 1, 2, . . . ,
Pr(Xn+1 = xn+1|Xn = xn, Xn−1 = xn−1, . . . , X1 = x1)
= Pr (Xn+1 = xn+1|Xn = xn)
(4.2)
for all x1, x2, . . . , xn, xn+1 ∈X.
In this case, the joint probability mass function of the random variables
can be written as
p(x1, x2, . . . , xn) = p(x1)p(x2|x1)p(x3|x2) · · · p(xn|xn−1).
(4.3)
Deﬁnition
The Markov chain is said to be time invariant if the con-
ditional probability p(xn+1|xn) does not depend on n; that is, for n =
1, 2, . . . ,
Pr{Xn+1 = b|Xn = a} = Pr{X2 = b|X1 = a}
for all a, b ∈X.
(4.4)
We will assume that the Markov chain is time invariant unless otherwise
stated.
If {Xi} is a Markov chain, Xn is called the state at time n. A time-
invariant Markov chain is characterized by its initial state and a probability
transition matrix P = [Pij], i, j ∈{1, 2, . . . , m}, where Pij = Pr{Xn+1 =
j|Xn = i}.
If it is possible to go with positive probability from any state of the
Markov chain to any other state in a ﬁnite number of steps, the Markov
chain is said to be irreducible. If the largest common factor of the lengths
of different paths from a state to itself is 1, the Markov chain is said to
aperiodic.
If the probability mass function of the random variable at time n is
p(xn), the probability mass function at time n + 1 is
p(xn+1) =

xn
p(xn)Pxnxn+1.
(4.5)
A distribution on the states such that the distribution at time n + 1 is the
same as the distribution at time n is called a stationary distribution. The


## PDF page 99

4.1
MARKOV CHAINS
73
stationary distribution is so called because if the initial state of a Markov
chain is drawn according to a stationary distribution, the Markov chain
forms a stationary process.
If the ﬁnite-state Markov chain is irreducible and aperiodic, the sta-
tionary distribution is unique, and from any starting distribution, the
distribution of Xn tends to the stationary distribution as n →∞.
Example 4.1.1
Consider a two-state Markov chain with a probability
transition matrix
P =

1 −α
α
β
1 −β

(4.6)
as shown in Figure 4.1.
Let the stationary distribution be represented by a vector µ whose com-
ponents are the stationary probabilities of states 1 and 2, respectively. Then
the stationary probability can be found by solving the equation µP = µ
or, more simply, by balancing probabilities. For the stationary distribution,
the net probability ﬂow across any cut set in the state transition graph is
zero. Applying this to Figure 4.1, we obtain
µ1α = µ2β.
(4.7)
Since µ1 + µ2 = 1, the stationary distribution is
µ1 =
β
α + β ,
µ2 =
α
α + β .
(4.8)
If the Markov chain has an initial state drawn according to the stationary
distribution, the resulting process will be stationary. The entropy of the
State 1
State 2
1 − β
1 − α
β
α
FIGURE 4.1. Two-state Markov chain.


## PDF page 100

74
ENTROPY RATES OF A STOCHASTIC PROCESS
state Xn at time n is
H(Xn) = H

β
α + β ,
α
α + β

.
(4.9)
However, this is not the rate at which entropy grows for H(X1, X2, . . . ,
Xn). The dependence among the Xi’s will take a steady toll.
4.2
ENTROPY RATE
If we have a sequence of n random variables, a natural question to ask
is: How does the entropy of the sequence grow with n? We deﬁne the
entropy rate as this rate of growth as follows.
Deﬁnition
The entropy of a stochastic process {Xi} is deﬁned by
H(X) = lim
n→∞
1
nH(X1, X2, . . . , Xn)
(4.10)
when the limit exists.
We now consider some simple examples of stochastic processes and
their corresponding entropy rates.
1. Typewriter.
Consider the case of a typewriter that has m equally likely output
letters. The typewriter can produce mn sequences of length n, all
of them equally likely. Hence H(X1, X2, . . . , Xn) = log mn and the
entropy rate is H(X) = log m bits per symbol.
2. X1, X2, . . . are i.i.d. random variables. Then
H(X) = lim H(X1, X2, . . . , Xn)
n
= lim nH(X1)
n
= H(X1),
(4.11)
which is what one would expect for the entropy rate per symbol.
3. Sequence of independent but not identically distributed random vari-
ables. In this case,
H(X1, X2, . . . , Xn) =
n

i=1
H(Xi),
(4.12)
but the H(Xi)’s are all not equal. We can choose a sequence of dis-
tributions on X1, X2, . . . such that the limit of 1
n
 H(Xi) does not
exist. An example of such a sequence is a random binary sequence


## PDF page 101

4.2
ENTROPY RATE
75
where pi = P (Xi = 1) is not constant but a function of i, chosen
carefully so that the limit in (4.10) does not exist. For example, let
pi =
 0.5
if 2k < log log i ≤2k + 1,
0
if 2k + 1 < log log i ≤2k + 2
(4.13)
for k = 0, 1, 2, . . . .
Then there are arbitrarily long stretches where H(Xi) = 1, followed
by exponentially longer segments where H(Xi) = 0. Hence, the run-
ning average of the H(Xi) will oscillate between 0 and 1 and will
not have a limit. Thus, H(X) is not deﬁned for this process.
We can also deﬁne a related quantity for entropy rate:
H ′(X) = lim
n→∞H(Xn|Xn−1, Xn−2, . . . , X1)
(4.14)
when the limit exists.
The two quantities H(X) and H ′(X) correspond to two different notions
of entropy rate. The ﬁrst is the per symbol entropy of the n random vari-
ables, and the second is the conditional entropy of the last random variable
given the past. We now prove the important result that for stationary pro-
cesses both limits exist and are equal.
Theorem 4.2.1
For a stationary stochastic process, the limits in (4.10)
and (4.14) exist and are equal:
H(X) = H ′(X).
(4.15)
We ﬁrst prove that lim H(Xn|Xn−1, . . . , X1) exists.
Theorem 4.2.2
For a stationary stochastic process, H(Xn|Xn−1, . . . ,
X1) is nonincreasing in n and has a limit H ′(X).
Proof
H(Xn+1|X1, X2, . . . , Xn) ≤H(Xn+1|Xn, . . . , X2)
(4.16)
= H(Xn|Xn−1, . . . , X1),
(4.17)
where the inequality follows from the fact that conditioning reduces en-
tropy and the equality follows from the stationarity of the process. Since
H(Xn|Xn−1, . . . , X1) is a decreasing sequence of nonnegative numbers,
it has a limit, H ′(X).
□


## PDF page 102

76
ENTROPY RATES OF A STOCHASTIC PROCESS
We now use the following simple result from analysis.
Theorem 4.2.3
(Ces´aro mean)
If an →a and bn = 1
n
n
i=1 ai, then
bn →a.
Proof:
(Informal outline). Since most of the terms in the sequence {ak}
are eventually close to a, then bn, which is the average of the ﬁrst n terms,
is also eventually close to a.
Formal Proof:
Let ϵ > 0. Since an →a, there exists a number N(ϵ)
such that |an −a| ≤ϵ for all n ≥N(ϵ). Hence,
|bn −a| =

1
n
n

i=1
(ai −a)

(4.18)
≤1
n
n

i=1
|(ai −a)|
(4.19)
≤1
n
N(ϵ)

i=1
|ai −a| + n −N(ϵ)
n
ϵ
(4.20)
≤1
n
N(ϵ)

i=1
|ai −a| + ϵ
(4.21)
for all n ≥N(ϵ). Since the ﬁrst term goes to 0 as n →∞, we can make
|bn −a| ≤2ϵ by taking n large enough. Hence, bn →a as n →∞.
□
Proof of Theorem 4.2.1:
By the chain rule,
H(X1, X2, . . . , Xn)
n
= 1
n
n

i=1
H(Xi|Xi−1, . . . , X1),
(4.22)
that is, the entropy rate is the time average of the conditional entropies.
But we know that the conditional entropies tend to a limit H ′. Hence, by
Theorem 4.2.3, their running average has a limit, which is equal to the
limit H ′ of the terms. Thus, by Theorem 4.2.2,
H(X) = lim H(X1, X2, . . . , Xn)
n
= lim H(Xn|Xn−1, . . . , X1)
= H ′(X).
□
(4.23)


## PDF page 103

4.2
ENTROPY RATE
77
The signiﬁcance of the entropy rate of a stochastic process arises from
the AEP for a stationary ergodic process. We prove the general AEP in
Section 16.8, where we show that for any stationary ergodic process,
−1
n log p(X1, X2, . . . , Xn) →H(X)
(4.24)
with probability 1. Using this, the theorems of Chapter 3 can easily be
extended to a general stationary ergodic process. We can deﬁne a typical
set in the same way as we did for the i.i.d. case in Chapter 3. By the
same arguments, we can show that the typical set has a probability close
to 1 and that there are about 2nH(X) typical sequences of length n, each
with probability about 2−nH(X). We can therefore represent the typical
sequences of length n using approximately nH(X) bits. This shows the
signiﬁcance of the entropy rate as the average description length for a
stationary ergodic process.
The entropy rate is well deﬁned for all stationary processes. The entropy
rate is particularly easy to calculate for Markov chains.
Markov Chains.
For a stationary Markov chain, the entropy rate is
given by
H(X) = H ′(X) = lim H(Xn|Xn−1, . . . , X1) = lim H(Xn|Xn−1)
= H(X2|X1),
(4.25)
where the conditional entropy is calculated using the given stationary
distribution. Recall that the stationary distribution µ is the solution of the
equations
µj =

i
µiPij
for all j.
(4.26)
We express the conditional entropy explicitly in the following theorem.
Theorem 4.2.4
Let {Xi} be a stationary Markov chain with station-
ary distribution µ and transition matrix P . Let X1 ∼µ. Then the entropy
rate is
H(X) = −

ij
µiPij log Pij.
(4.27)
Proof:
H(X) = H(X2|X1) = 
i µi
	
j −Pij log Pij

.
□


## PDF page 104

78
ENTROPY RATES OF A STOCHASTIC PROCESS
Example 4.2.1
(Two-state Markov chain)
The entropy rate of the two-
state Markov chain in Figure 4.1 is
H(X) = H(X2|X1) =
β
α + β H(α) +
α
α + β H(β).
(4.28)
Remark
If the Markov chain is irreducible and aperiodic, it has a unique
stationary distribution on the states, and any initial distribution tends to
the stationary distribution as n →∞. In this case, even though the initial
distribution is not the stationary distribution, the entropy rate, which is
deﬁned in terms of long-term behavior, is H(X), as deﬁned in (4.25) and
(4.27).
4.3
EXAMPLE: ENTROPY RATE OF A RANDOM WALK
ON A WEIGHTED GRAPH
As an example of a stochastic process, let us consider a random walk on
a connected graph (Figure 4.2). Consider a graph with m nodes labeled
{1, 2, . . . , m}, with weight Wij ≥0 on the edge joining node i to node
j. (The graph is assumed to be undirected, so that Wij = Wji. We set
Wij = 0 if there is no edge joining nodes i and j.)
A particle walks randomly from node to node in this graph. The ran-
dom walk {Xn}, Xn ∈{1, 2, . . . , m}, is a sequence of vertices of the
graph. Given Xn = i, the next vertex j is chosen from among the nodes
connected to node i with a probability proportional to the weight of the
edge connecting i to j. Thus, Pij = Wij/ 
k Wik.
1
2
5
3
4
FIGURE 4.2. Random walk on a graph.


