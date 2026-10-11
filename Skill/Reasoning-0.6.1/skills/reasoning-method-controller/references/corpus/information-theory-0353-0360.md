# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 353

10.6
STRONGLY TYPICAL SEQUENCES AND RATE DISTORTION
327
with a given sequence. Theorem 7.6.1 shows that if we choose Xn and
Y n independently, the probability that they will be weakly jointly typical
is ≈2−nI(X;Y). The following lemma extends the result to strongly typical
sequences. This is stronger than the earlier result in that it gives a lower
bound on the probability that a randomly chosen sequence is jointly typical
with a ﬁxed typical xn.
Lemma 10.6.2
Let Y1, Y2, . . . , Yn be drawn i.i.d. ∼p(y). For xn ∈
A∗(n)
ϵ
(X), the probability that (xn, Y n) ∈A∗(n)
ϵ
is bounded by
2−n(I(X;Y)+ϵ1) ≤Pr((xn, Y n) ∈A∗(n)
ϵ
) ≤2−n(I(X;Y)−ϵ1),
(10.108)
where ϵ1 goes to 0 as ϵ →0 and n →∞.
Proof:
We will not prove this lemma, but instead, outline the proof in
Problem 10.16 at the end of the chapter. In essence, the proof involves
ﬁnding a lower bound on the size of the conditionally typical set.
□
We will proceed directly to the achievability of the rate distortion
function. We will only give an outline to illustrate the main ideas. The
construction of the codebook and the encoding and decoding are similar
to the proof in Section 10.5.
Proof:
Fix p(ˆx|x). Calculate p(ˆx) = 
x p(x)p(ˆx|x). Fix ϵ > 0. Later
we will choose ϵ appropriately to achieve an expected distortion less than
D + δ.
Generation of codebook: Generate a rate distortion codebook C consist-
ing of 2nR sequences ˆXn drawn i.i.d. ∼
i p(ˆxi). Denote the sequences
ˆXn(1), . . . , ˆXn(2nR).
Encoding: Given a sequence Xn, index it by w if there exists a w such
that (Xn, ˆXn(w)) ∈A∗(n)
ϵ
, the strongly jointly typical set. If there is more
than one such w, send the ﬁrst in lexicographic order. If there is no such
w, let w = 1.
Decoding: Let the reproduced sequence be ˆXn(w).
Calculation of distortion: As in the case of the proof in Section 10.5, we
calculate the expected distortion over the random choice of codebook as
D = EXn,Cd(Xn, ˆXn)
(10.109)
= EC

xn
p(xn)d(xn, ˆXn(xn))
(10.110)
=

xn
p(xn)ECd(xn, ˆXn),
(10.111)


## PDF page 354

328
RATE DISTORTION THEORY
Nontypical sequences
Typical
sequences
with
jointly
typical
codeword
Typical
sequences
without
jointly
typical
codeword
FIGURE 10.8. Classes of source sequences in rate distortion theorem.
where the expectation is over the random choice of codebook. For a ﬁxed
codebook C, we divide the sequences xn ∈Xn into three categories, as
shown in Figure 10.8.
• Nontypical sequences xn /∈A∗(n)
ϵ
. The total probability of these
sequences can be made less than ϵ by choosing n large enough. Since
the individual distortion between any two sequences is bounded by
dmax, the nontypical sequences can contribute at most ϵdmax to the
expected distortion.
• Typical sequences xn ∈A∗(n)
ϵ
such that there exists a codeword ˆXn(w)
that is jointly typical with xn. In this case, since the source sequence
and the codeword are strongly jointly typical, the continuity of the
distortion as a function of the joint distribution ensures that they
are also distortion typical. Hence, the distortion between these xn
and their codewords is bounded by D + ϵdmax, and since the total
probability of these sequences is at most 1, these sequences contribute
at most D + ϵdmax to the expected distortion.
• Typical sequences xn ∈A∗(n)
ϵ
such that there does not exist a code-
word ˆXn that is jointly typical with xn. Let Pe be the total probability
of these sequences. Since the distortion for any individual sequence
is bounded by dmax, these sequences contribute at most Pedmax to the
expected distortion.


## PDF page 355

10.7
CHARACTERIZATION OF THE RATE DISTORTION FUNCTION
329
The sequences in the ﬁrst and third categories are the sequences that
may not be well represented by this rate distortion code. The probability
of the ﬁrst category of sequences is less than ϵ for sufﬁciently large n. The
probability of the last category is Pe, which we will show can be made
small. This will prove the theorem that the total probability of sequences
that are not well represented is small. In turn, we use this to show that
the average distortion is close to D.
Calculation of Pe: We must bound the probability that there is no code-
word that is jointly typical with the given sequence Xn. From the joint
AEP, we know that the probability that Xn and any ˆXn are jointly typical
is
.= 2−nI(X; ˆX). Hence the expected number of jointly typical ˆXn(w) is
2nR2−nI(X; ˆX), which is exponentially large if R > I (X; ˆX).
But this is not sufﬁcient to show that Pe →0. We must show that the
probability that there is no codeword that is jointly typical with Xn goes
to zero. The fact that the expected number of jointly typical codewords is
exponentially large does not ensure that there will at least one with high
probability. Just as in (10.94), we can expand the probability of error as
Pe =

xn∈A∗(n)
ϵ
p(xn)

1 −Pr((xn, ˆXn) ∈A∗(n)
ϵ
)
2nR
.
(10.112)
From Lemma 10.6.2 we have
Pr((xn, ˆXn) ∈A∗(n)
ϵ
) ≥2−n(I(X; ˆX)+ϵ1).
(10.113)
Substituting this in (10.112) and using the inequality (1 −x)n ≤e−nx, we
have
Pe ≤e−(2nR2−n(I (X; ˆX)+ϵ1)),
(10.114)
which goes to 0 as n →∞if R > I (X; ˆX) + ϵ1. Hence for an appropriate
choice of ϵ and n, we can get the total probability of all badly represented
sequences to be as small as we want. Not only is the expected distortion
close to D, but with probability going to 1, we will ﬁnd a codeword whose
distortion with respect to the given sequence is less than D + δ.
□
10.7
CHARACTERIZATION OF THE RATE DISTORTION
FUNCTION
We have deﬁned the information rate distortion function as
R(D) =
min
q(ˆx|x):
(x,ˆx) p(x)q(ˆx|x)d(x,ˆx)≤D I (X; ˆX),
(10.115)


## PDF page 356

330
RATE DISTORTION THEORY
where the minimization is over all conditional distributions q(ˆx|x) for
which the joint distribution p(x)q(ˆx|x) satisﬁes the expected distortion
constraint. This is a standard minimization problem of a convex function
over the convex set of all q(ˆx|x) ≥0 satisfying 
ˆx q(ˆx|x) = 1 for all x
and  q(ˆx|x)p(x)d(x, ˆx) ≤D.
We can use the method of Lagrange multipliers to ﬁnd the solution.
We set up the functional
J(q) =

x

ˆx
p(x)q(ˆx|x) log
q(ˆx|x)

x p(x)q(ˆx|x)
+ λ

x

ˆx
p(x)q(ˆx|x)d(x, ˆx)
(10.116)
+

x
ν(x)

ˆx
q(ˆx|x),
(10.117)
where the last term corresponds to the constraint that q(ˆx|x) is a condi-
tional probability mass function. If we let q(ˆx) = 
x p(x)q(ˆx|x) be the
distribution on ˆX induced by q(ˆx|x), we can rewrite J(q) as
J(q) =

x

ˆx
p(x)q(ˆx|x) log q(ˆx|x)
q(ˆx)
+λ

x

ˆx
p(x)q(ˆx|x)d(x, ˆx)
(10.118)
+

x
ν(x)

ˆx
q(ˆx|x).
(10.119)
Differentiating with respect to q(ˆx|x), we have
∂J
∂q(ˆx|x) = p(x) log q(ˆx|x)
q(ˆx) + p(x) −

x′
p(x′)q(ˆx|x′) 1
q(ˆx)p(x)
+ λp(x)d(x, ˆx) + ν(x) = 0.
(10.120)
Setting log µ(x) = ν(x)/p(x), we obtain
p(x)

log q(ˆx|x)
q(ˆx) + λd(x, ˆx) + log µ(x)

= 0
(10.121)


## PDF page 357

10.7
CHARACTERIZATION OF THE RATE DISTORTION FUNCTION
331
or
q(ˆx|x) = q(ˆx)e−λd(x,ˆx)
µ(x)
.
(10.122)
Since 
ˆx q(ˆx|x) = 1, we must have
µ(x) =

ˆx
q(ˆx)e−λd(x,ˆx)
(10.123)
or
q(ˆx|x) =
q(ˆx)e−λd(x,ˆx)

ˆx q(ˆx)e−λd(x,ˆx).
(10.124)
Multiplying this by p(x) and summing over all x, we obtain
q(ˆx) = q(ˆx)

x
p(x)e−λd(x,ˆx)

ˆx′ q(ˆx′)e−λd(x,ˆx′) .
(10.125)
If q(ˆx) > 0, we can divide both sides by q(ˆx) and obtain

x
p(x)e−λd(x,ˆx)

ˆx′ q(ˆx′)e−λd(x,ˆx′) = 1
(10.126)
for all ˆx ∈ˆX. We can combine these | ˆX| equations with the equation
deﬁning the distortion and calculate λ and the | ˆX| unknowns q(ˆx). We
can use this and (10.124) to ﬁnd the optimum conditional distribution.
The above analysis is valid if q(ˆx) is unconstrained (i.e., q(ˆx) > 0 for
all ˆx). The inequality condition q(ˆx) > 0 is covered by the Kuhn–Tucker
conditions, which reduce to
∂J
∂q(ˆx|x) = 0 if q(ˆx|x) > 0,
(10.127)
≥0 if q(ˆx|x) = 0.
Substituting the value of the derivative, we obtain the conditions for the
minimum as

x
p(x)e−λd(x,ˆx)

ˆx′ q(ˆx′)e−λd(x,ˆx′) = 1
if q(ˆx) > 0,
(10.128)
≤1
if q(ˆx) = 0.
(10.129)


## PDF page 358

332
RATE DISTORTION THEORY
This characterization will enable us to check if a given q(ˆx) is a solution
to the minimization problem. However, it is not easy to solve for the
optimum output distribution from these equations. In the next section we
provide an iterative algorithm for computing the rate distortion function.
This algorithm is a special case of a general algorithm for ﬁnding the
minimum relative entropy distance between two convex sets of probability
densities.
10.8
COMPUTATION OF CHANNEL CAPACITY AND THE RATE
DISTORTION FUNCTION
Consider the following problem: Given two convex sets A and B in Rn
as shown in Figure 10.9, we would like to ﬁnd the minimum distance
between them:
dmin =
min
a∈A,b∈B d(a, b),
(10.130)
where d(a, b) is the Euclidean distance between a and b. An intuitively
obvious algorithm to do this would be to take any point x ∈A, and ﬁnd
the y ∈B that is closest to it. Then ﬁx this y and ﬁnd the closest point in
A. Repeating this process, it is clear that the distance decreases at each
stage. Does it converge to the minimum distance between the two sets?
Csisz´ar and Tusn´ady [155] have shown that if the sets are convex and
if the distance satisﬁes certain conditions, this alternating minimization
algorithm will indeed converge to the minimum. In particular, if the sets
are sets of probability distributions and the distance measure is the relative
entropy, the algorithm does converge to the minimum relative entropy
between the two sets of distributions.
A
B
FIGURE 10.9. Distance between convex sets.


## PDF page 359

10.8
COMPUTATION OF CHANNEL CAPACITY AND RATE DISTORTION FUNCTION
333
To apply this algorithm to rate distortion, we have to rewrite the rate
distortion function as a minimum of the relative entropy between two sets.
We begin with a simple lemma. A form of this lemma comes up again
in theorem 13.1.1, establishing the duality of channel capacity universal
data compression.
Lemma 10.8.1
Let p(x)p(y|x) be a given joint distribution. Then the
distribution r(y) that minimizes the relative entropy D(p(x)p(y|x)||p(x)
r(y)) is the marginal distribution r∗(y) corresponding to p(y|x):
D(p(x)p(y|x)||p(x)r∗(y)) = min
r(y) D(p(x)p(y|x)||p(x)r(y)), (10.131)
where r∗(y) = 
x p(x)p(y|x). Also,
max
r(x|y)

x,y
p(x)p(y|x) log r(x|y)
p(x) =

x,y
p(x)p(y|x) log r∗(x|y)
p(x) ,
(10.132)
where
r∗(x|y) =
p(x)p(y|x)

x p(x)p(y|x).
(10.133)
Proof
D(p(x)p(y|x)||p(x)r(y)) −D(p(x)p(y|x)||p(x)r∗(y))
=

x,y
p(x)p(y|x) log p(x)p(y|x)
p(x)r(y)
(10.134)
−

x,y
p(x)p(y|x) log p(x)p(y|x)
p(x)r∗(y)
(10.135)
=

x,y
p(x)p(y|x) log r∗(y)
r(y)
(10.136)
=

y
r∗(y) log r∗(y)
r(y)
(10.137)
= D(r∗||r)
(10.138)
≥0.
(10.139)


## PDF page 360

334
RATE DISTORTION THEORY
The proof of the second part of the lemma is left as an exercise.
□
We can use this lemma to rewrite the minimization in the deﬁnition of
the rate distortion function as a double minimization,
R(D) = min
r(ˆx)
min
q(ˆx|x): p(x)q(ˆx|x)d(x,ˆx)≤D

x

ˆx
p(x)q(ˆx|x) log q(ˆx|x)
r(ˆx) .
(10.140)
If A is the set of all joint distributions with marginal p(x) that satisfy the
distortion constraints and if B the set of product distributions p(x)r(ˆx)
with arbitrary r(ˆx), we can write
R(D) = min
q∈B min
p∈A D(p||q).
(10.141)
We now apply the process of alternating minimization, which is called the
Blahut–Arimoto algorithm in this case. We begin with a choice of λ and
an initial output distribution r(ˆx) and calculate the q(ˆx|x) that minimizes
the mutual information subject to the distortion constraint. We can use the
method of Lagrange multipliers for this minimization to obtain
q(ˆx|x) =
r(ˆx)e−λd(x,ˆx)

ˆx r(ˆx)e−λd(x,ˆx) .
(10.142)
For this conditional distribution q(ˆx|x), we calculate the output distribu-
tion r(ˆx) that minimizes the mutual information, which by Lemma 10.8.1
is
r(ˆx) =

x
p(x)q(ˆx|x).
(10.143)
We use this output distribution as the starting point of the next iteration.
Each step in the iteration, minimizing over q(·|·) and then minimizing over
r(·), reduces the right-hand side of (10.140). Thus, there is a limit, and
the limit has been shown to be R(D) by Csisz´ar [139], where the value
of D and R(D) depends on λ. Thus, choosing λ appropriately sweeps out
the R(D) curve.
A similar procedure can be applied to the calculation of channel capac-
ity. Again we rewrite the deﬁnition of channel capacity,
C = max
r(x) I (X; Y) = max
r(x)

x

y
r(x)p(y|x) log
r(x)p(y|x)
r(x) 
x′ r(x′)p(y|x′)
(10.144)


