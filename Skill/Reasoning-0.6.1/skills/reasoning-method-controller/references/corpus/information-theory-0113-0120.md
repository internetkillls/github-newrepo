# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 113

SUMMARY
87
process X1, X2, . . . , Xn, and deﬁne a new process Y1, Y2, . . . , Yn, where
each Yi is drawn according to p(yi|xi), conditionally independent of all
the other Xj, j ̸= i; that is,
p(xn, yn) = p(x1)
n−1

i=1
p(xi+1|xi)
n

i=1
p(yi|xi).
(4.75)
Such a process, called a hidden Markov model (HMM), is used extensively
in speech recognition, handwriting recognition, and so on. The same argu-
ment as that used above for functions of a Markov chain carry over to
hidden Markov models, and we can lower bound the entropy rate of a
hidden Markov model by conditioning it on the underlying Markov state.
The details of the argument are left to the reader.
SUMMARY
Entropy rate. Two deﬁnitions of entropy rate for a stochastic process
are
H(X) = lim
n→∞
1
nH(X1, X2, . . . , Xn),
(4.76)
H ′(X) = lim
n→∞H(Xn|Xn−1, Xn−2, . . . , X1).
(4.77)
For a stationary stochastic process,
H(X) = H ′(X).
(4.78)
Entropy rate of a stationary Markov chain
H(X) = −

ij
µiPij log Pij.
(4.79)
Second law of thermodynamics. For a Markov chain:
1. Relative entropy D(µn||µ′
n) decreases with time
2. Relative entropy D(µn||µ) between a distribution and the stationary
distribution decreases with time.
3. Entropy H(Xn) increases if the stationary distribution is uniform.


## PDF page 114

88
ENTROPY RATES OF A STOCHASTIC PROCESS
4. The conditional entropy H(Xn|X1) increases with time for a sta-
tionary Markov chain.
5. The conditional entropy H(X0|Xn) of the initial condition X0 in-
creases for any Markov chain.
Functions of a Markov chain. If X1, X2, . . . , Xn form a stationary
Markov chain and Yi = φ(Xi), then
H(Yn|Yn−1, . . . , Y1, X1) ≤H(Y) ≤H(Yn|Yn−1, . . . , Y1)
(4.80)
and
lim
n→∞H(Yn|Yn−1, . . . , Y1, X1) = H(Y) = lim
n→∞H(Yn|Yn−1, . . . , Y1).
(4.81)
PROBLEMS
4.1
Doubly stochastic matrices.
An n × n matrix P = [Pij] is said
to be doubly stochastic if Pij ≥0 and 
j Pij = 1 for all i and

i Pij = 1 for all j. An n × n matrix P is said to be a permu-
tation matrix if it is doubly stochastic and there is precisely one
Pij = 1 in each row and each column. It can be shown that every
doubly stochastic matrix can be written as the convex combination
of permutation matrices.
(a) Let at = (a1, a2, . . . , an), ai ≥0,  ai = 1, be a probability
vector. Let b = aP , where P is doubly stochastic. Show that b
is a probability vector and that H(b1, b2, . . . , bn) ≥H(a1, a2,
. . . , an). Thus, stochastic mixing increases entropy.
(b) Show that a stationary distribution µ for a doubly stochastic
matrix P is the uniform distribution.
(c) Conversely, prove that if the uniform distribution is a stationary
distribution for a Markov transition matrix P , then P is doubly
stochastic.
4.2
Time’s arrow.
Let {Xi}∞
i=−∞be a stationary stochastic process.
Prove that
H(X0|X−1, X−2, . . . , X−n) = H(X0|X1, X2, . . . , Xn).


## PDF page 115

PROBLEMS
89
In other words, the present has a conditional entropy given the past
equal to the conditional entropy given the future. This is true even
though it is quite easy to concoct stationary random processes for
which the ﬂow into the future looks quite different from the ﬂow
into the past. That is, one can determine the direction of time by
looking at a sample function of the process. Nonetheless, given
the present state, the conditional uncertainty of the next symbol in
the future is equal to the conditional uncertainty of the previous
symbol in the past.
4.3
Shufﬂes increase entropy.
Argue that for any distribution on shuf-
ﬂes T and any distribution on card positions X that
H(T X) ≥H(T X|T )
(4.82)
= H(T −1T X|T )
(4.83)
= H(X|T )
(4.84)
= H(X)
(4.85)
if X and T are independent.
4.4
Second law of thermodynamics.
Let X1, X2, X3, . . . be a station-
ary ﬁrst-order Markov chain. In Section 4.4 it was shown that
H(Xn | X1) ≥H(Xn−1 | X1) for n = 2, 3, . . . . Thus, conditional
uncertainty about the future grows with time. This is true although
the unconditional uncertainty H(Xn) remains constant. However,
show by example that H(Xn|X1 = x1) does not necessarily grow
with n for every x1.
4.5
Entropy of a random tree.
Consider the following method of gen-
erating a random tree with n nodes. First expand the root node:
Then expand one of the two terminal nodes at random:
At time k, choose one of the k −1 terminal nodes according to a
uniform distribution and expand it. Continue until n terminal nodes


## PDF page 116

90
ENTROPY RATES OF A STOCHASTIC PROCESS
have been generated. Thus, a sequence leading to a ﬁve-node tree
might look like this:
Surprisingly, the following method of generating random trees
yields the same probability distribution on trees with n termi-
nal nodes. First choose an integer N1 uniformly distributed on
{1, 2, . . . , n −1}. We then have the picture
N1
n − N1
Then
choose
an
integer
N2
uniformly
distributed
over
{1, 2, . . . , N1 −1}, and independently choose another integer N3
uniformly over {1, 2, . . . , (n −N1) −1}. The picture is now
N2
N3
n − N1 − N3
N1 − N2
Continue the process until no further subdivision can be made.
(The equivalence of these two tree generation schemes follows, for
example, from Polya’s urn model.)
Now let Tn denote a random n-node tree generated as described. The
probability distribution on such trees seems difﬁcult to describe, but
we can ﬁnd the entropy of this distribution in recursive form.
First some examples. For n = 2, we have only one tree. Thus,
H(T2) = 0. For n = 3, we have two equally probable trees:


## PDF page 117

PROBLEMS
91
Thus, H(T3) = log 2. For n = 4, we have ﬁve possible trees, with
probabilities 1
3, 1
6, 1
6, 1
6, 1
6.
Now for the recurrence relation. Let N1(Tn) denote the number of
terminal nodes of Tn in the right half of the tree. Justify each of
the steps in the following:
H(Tn)
(a)
= H(N1, Tn)
(4.86)
(b)
= H(N1) + H(Tn|N1)
(4.87)
(c)
= log(n −1) + H(Tn|N1)
(4.88)
(d)
= log(n −1) +
1
n −1
n−1

k=1
(H(Tk) + H(Tn−k))
(4.89)
(e)
= log(n −1) +
2
n −1
n−1

k=1
H(Tk)
(4.90)
= log(n −1) +
2
n −1
n−1

k=1
Hk.
(4.91)
(f) Use this to show that
(n −1)Hn = nHn−1 + (n −1) log(n −1) −(n −2) log(n −2)
(4.92)
or
Hn
n = Hn−1
n −1 + cn
(4.93)
for appropriately deﬁned cn. Since  cn = c < ∞, you have proved
that 1
nH(Tn) converges to a constant. Thus, the expected number of
bits necessary to describe the random tree Tn grows linearly with n.
4.6
Monotonicity of entropy per element.
For a stationary stochastic
process X1, X2, . . . , Xn, show that
(a)
H(X1, X2, . . . , Xn)
n
≤H(X1, X2, . . . , Xn−1)
n −1
.
(4.94)
(b)
H(X1, X2, . . . , Xn)
n
≥H(Xn|Xn−1, . . . , X1).
(4.95)


## PDF page 118

92
ENTROPY RATES OF A STOCHASTIC PROCESS
4.7
Entropy rates of Markov chains
(a) Find the entropy rate of the two-state Markov chain with tran-
sition matrix
P =

1 −p01
p01
p10
1 −p10

.
(b) What values of p01, p10 maximize the entropy rate?
(c) Find the entropy rate of the two-state Markov chain with tran-
sition matrix
P =

1 −p
p
1
0

.
(d) Find the maximum value of the entropy rate of the Markov
chain of part (c). We expect that the maximizing value of p
should be less than 1
2, since the 0 state permits more informa-
tion to be generated than the 1 state.
(e) Let N(t) be the number of allowable state sequences of length t
for the Markov chain of part (c). Find N(t) and calculate
H0 = lim
t→∞
1
t log N(t).
[Hint: Find a linear recurrence that expresses N(t) in terms
of N(t −1) and N(t −2). Why is H0 an upper bound on the
entropy rate of the Markov chain? Compare H0 with the max-
imum entropy found in part (d).]
4.8
Maximum entropy process.
A discrete memoryless source has the
alphabet {1, 2}, where the symbol 1 has duration 1 and the sym-
bol 2 has duration 2. The probabilities of 1 and 2 are p1 and p2,
respectively. Find the value of p1 that maximizes the source entropy
per unit time H(X) = H(X)
ET . What is the maximum value H(X)?
4.9
Initial conditions.
Show, for a Markov chain, that
H(X0|Xn) ≥H(X0|Xn−1).
Thus, initial conditions X0 become more difﬁcult to recover as the
future Xn unfolds.
4.10
Pairwise independence.
Let X1, X2, . . . , Xn−1 be i.i.d. random
variables taking values in {0, 1}, with Pr{Xi = 1} = 1
2 . Let Xn = 1
if n−1
i=1 Xi is odd and Xn = 0 otherwise. Let n ≥3.


## PDF page 119

PROBLEMS
93
(a) Show that Xi and Xj are independent for i ̸= j, i, j ∈{1, 2,
. . . , n}.
(b) Find H(Xi, Xj) for i ̸= j.
(c) Find H(X1, X2, . . . , Xn). Is this equal to nH(X1)?
4.11
Stationary processes.
Let . . . , X−1, X0, X1, . . . be a stationary
(not necessarily Markov) stochastic process. Which of the follow-
ing statements are true? Prove or provide a counterexample.
(a) H(Xn|X0) = H(X−n|X0) .
(b) H(Xn|X0) ≥H(Xn−1|X0) .
(c) H(Xn|X1, X2, . . . , Xn−1, Xn+1) is nonincreasing in n.
(d) H(Xn|X1, . . . , Xn−1, Xn+1, . . . , X2n) is nonincreasing in n.
4.12
Entropy rate of a dog looking for a bone.
A dog walks on the
integers, possibly reversing direction at each step with probability
p = 0.1. Let X0 = 0. The ﬁrst step is equally likely to be positive
or negative. A typical walk might look like this:
(X0, X1, . . .) = (0, −1, −2, −3, −4, −3, −2, −1, 0, 1, . . .).
(a) Find H(X1, X2, . . . , Xn).
(b) Find the entropy rate of the dog.
(c) What is the expected number of steps that the dog takes before
reversing direction?
4.13
The past has little to say about the future.
For a stationary stochas-
tic process X1, X2, . . . , Xn, . . . , show that
lim
n→∞
1
2nI (X1, X2, . . . , Xn; Xn+1, Xn+2, . . . , X2n) = 0.
(4.96)
Thus, the dependence between adjacent n-blocks of a stationary
process does not grow linearly with n.
4.14
Functions of a stochastic process
(a) Consider a stationary stochastic process X1, X2, . . . , Xn, and
let Y1, Y2, . . . , Yn be deﬁned by
Yi = φ(Xi),
i = 1, 2, . . .
(4.97)
for some function φ. Prove that
H(Y) ≤H(X).
(4.98)


## PDF page 120

94
ENTROPY RATES OF A STOCHASTIC PROCESS
(b) What is the relationship between the entropy rates H(Z) and
H(X) if
Zi = ψ(Xi, Xi+1),
i = 1, 2, . . .
(4.99)
for some function ψ?
4.15
Entropy rate.
Let {Xi} be a discrete stationary stochastic process
with entropy rate H(X). Show that
1
nH(Xn, . . . , X1 | X0, X−1, . . . , X−k) →H(X)
(4.100)
for k = 1, 2, . . ..
4.16
Entropy rate of constrained sequences.
In magnetic recording, the
mechanism of recording and reading the bits imposes constraints
on the sequences of bits that can be recorded. For example, to
ensure proper synchronization, it is often necessary to limit the
length of runs of 0’s between two 1’s. Also, to reduce intersymbol
interference, it may be necessary to require at least one 0 between
any two 1’s. We consider a simple example of such a constraint.
Suppose that we are required to have at least one 0 and at most
two 0’s between any pair of 1’s in a sequences. Thus, sequences
like 101001 and 0101001 are valid sequences, but 0110010 and
0000101 are not. We wish to calculate the number of valid se-
quences of length n.
(a) Show that the set of constrained sequences is the same as the
set of allowed paths on the following state diagram:
(b) Let Xi(n) be the number of valid paths of length n ending at
state i. Argue that X(n) = [X1(n) X2(n) X3(n)]t satisﬁes the


