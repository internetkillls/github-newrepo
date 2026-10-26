# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 417

11.9
CHERNOFF INFORMATION
391
results in a gain of a few yards with very high probability, whereas passing
results in huge gains with low probability. Examples of the distributions
are illustrated in Figure 11.12.
At the beginning of the game, the coach uses the strategy that promises
the greatest expected gain. Now assume that we are in the closing min-
utes of the game and one of the teams is leading by a large margin.
(Let us ignore ﬁrst downs and adaptable defenses.) So the trailing team
will win only if it is very lucky. If luck is required to win, we might
as well assume that we will be lucky and play accordingly. What is the
appropriate strategy?
Assume that the team has only n plays left and it must gain l yards,
where l is much larger than n times the expected gain under each play. The
probability that the team succeeds in achieving l yards is exponentially
small; hence, we can use the large deviation results and Sanov’s theorem to
calculate the probability of this event. To be precise, we wish to calculate
the probability that n
i=1 Zi ≥nα, where Zi are independent random
variables and Zi has a distribution corresponding to the strategy chosen.
The situation is illustrated in Figure 11.13. Let E be the set of types
corresponding to the constraint,
E =

P :

a∈X
P (a)a ≥α

.
(11.259)
If P1 is the distribution corresponding to passing all the time, the proba-
bility of winning is the probability that the sample type is in E, which by
Sanov’s theorem is 2−nD(P ∗
1 ||P1), where P ∗
1 is the distribution in E that is
closest to P1. Similarly, if the coach uses the running game all the time,
E
P1
P2
FIGURE 11.13. Probability simplex for a football game.


## PDF page 418

392
INFORMATION THEORY AND STATISTICS
the probability of winning is 2−nD(P ∗
2 ||P2). What if he uses a mixture of
strategies? Is it possible that 2−nD(P ∗
λ ||Pλ), the probability of winning with
a mixed strategy, Pλ = λP1 + (1 −λ)P2, is better than the probability of
winning with either pure passing or pure running? The somewhat surpris-
ing answer is yes, as can be shown by example. This provides a reason
to use a mixed strategy other than the fact that it confuses the defense.
We end this section with another inequality due to Chernoff, which
is a special version of Markov’s inequality. This inequality is called the
Chernoff bound.
Lemma 11.9.1
Let Y be any random variable and let ψ(s) be the
moment generating function of Y,
ψ(s) = EesY.
(11.260)
Then for all s ≥0,
Pr(Y ≥a) ≤e−saψ(s),
(11.261)
and thus
Pr(Y ≥a) ≤min
s≥0 e−saψ(s).
(11.262)
Proof:
Apply Markov’s inequality to the nonnegative random variable
esY.
□
11.10
FISHER INFORMATION AND THE CRAM´ER–RAO
INEQUALITY
A standard problem in statistical estimation is to determine the parameters
of a distribution from a sample of data drawn from that distribution.
For example, let X1, X2, . . . , Xn be drawn i.i.d. ∼N(θ, 1). Suppose that
we wish to estimate θ from a sample of size n. There are a number of
functions of the data that we can use to estimate θ. For example, we can
use the ﬁrst sample X1. Although the expected value of X1 is θ, it is clear
that we can do better by using more of the data. We guess that the best
estimate of θ is the sample mean Xn = 1
n
 Xi. Indeed, it can be shown
that Xn is the minimum mean-squared-error unbiased estimator.
We begin with a few deﬁnitions. Let {f (x; θ)}, θ ∈, denote an
indexed family of densities, f (x; θ) ≥0,

f (x; θ) dx = 1 for all θ ∈.
Here  is called the parameter set.
Deﬁnition
An estimator for θ for sample size n is a function T :
Xn →.


## PDF page 419

11.10
FISHER INFORMATION AND THE CRAM´ER–RAO INEQUALITY
393
An estimator is meant to approximate the value of the parameter. It
is therefore desirable to have some idea of the goodness of the approxi-
mation. We will call the difference T −θ the error of the estimator. The
error is a random variable.
Deﬁnition
The bias of an estimator T (X1, X2, . . . , Xn) for the param-
eter θ is the expected value of the error of the estimator [i.e., the bias is
EθT (x1, x2, . . . , xn) −θ]. The subscript θ means that the expectation is
with respect to the density f (·; θ). The estimator is said to be unbiased
if the bias is zero for all θ ∈ (i.e., the expected value of the estimator
is equal to the parameter).
Example 11.10.1
Let X1, X2, . . . , Xn drawn i.i.d. ∼f (x) = (1/λ)
e−x/λ, x ≥0 be a sequence of exponentially distributed random variables.
Estimators of λ include X1 and Xn. Both estimators are unbiased.
The bias is the expected value of the error, and the fact that it is
zero does not guarantee that the error is low with high probability. We
need to look at some loss function of the error; the most commonly
chosen loss function is the expected square of the error. A good estima-
tor should have a low expected squared error and should have an error
that approaches 0 as the sample size goes to inﬁnity. This motivates the
following deﬁnition:
Deﬁnition
An estimator T (X1, X2, . . . , Xn) for θ is said to be consis-
tent in probability if
T (X1, X2, . . . , Xn) →θ in probability as n →∞.
Consistency is a desirable asymptotic property, but we are interested in
the behavior for small sample sizes as well. We can then rank estimators
on the basis of their mean-squared error.
Deﬁnition
An estimator T1(X1, X2, . . . , Xn) is said to dominate
another estimator T2(X1, X2, . . . , Xn) if, for all θ,
E (T1(X1, X2, . . . , Xn) −θ)2 ≤E (T2(X1, X2, . . . , Xn) −θ)2 .
(11.263)
This raises a natural question: Is there a best estimator of θ that dom-
inates every other estimator? To answer this question, we derive the
Cram´er–Rao lower bound on the mean-squared error of any estimator.
We ﬁrst deﬁne the score function of the distribution f (x; θ). We then use
the Cauchy–Schwarz inequality to prove the Cram´er–Rao lower bound
on the variance of all unbiased estimators.


## PDF page 420

394
INFORMATION THEORY AND STATISTICS
Deﬁnition
The score V is a random variable deﬁned by
V = ∂
∂θ ln f (X; θ) =
∂
∂θ f (X; θ)
f (X; θ) ,
(11.264)
where X ∼f (x; θ).
The mean value of the score is
EV =

∂
∂θ f (x; θ)
f (x; θ) f (x; θ) dx
(11.265)
=

∂
∂θ f (x; θ) dx
(11.266)
= ∂
∂θ

f (x; θ) dx
(11.267)
= ∂
∂θ 1
(11.268)
= 0,
(11.269)
and therefore EV 2 = var(V ). The variance of the score has a special
signiﬁcance.
Deﬁnition
The Fisher information J(θ) is the variance of the score:
J(θ) = Eθ
 ∂
∂θ ln f (X; θ)
2
.
(11.270)
If we consider a sample of n random variables X1, X2, . . . , Xn drawn
i.i.d. ∼f (x; θ), we have
f (x1, x2, . . . , xn; θ) =
n

i=1
f (xi; θ),
(11.271)
and the score function is the sum of the individual score functions,
V (X1, X2, . . . , Xn) = ∂
∂θ ln f (X1, X2, . . . , Xn; θ)
(11.272)
=
n

i=1
∂
∂θ ln f (Xi; θ)
(11.273)
=
n

i=1
V (Xi),
(11.274)


## PDF page 421

11.10
FISHER INFORMATION AND THE CRAM´ER–RAO INEQUALITY
395
where the V (Xi) are independent, identically distributed with zero mean.
Hence, the n-sample Fisher information is
Jn(θ) = Eθ
 ∂
∂θ ln f (X1, X2, . . . , Xn; θ)
2
(11.275)
= EθV 2(X1, X2, . . . , Xn)
(11.276)
= Eθ
 n

i=1
V (Xi)
2
(11.277)
=
n

i=1
EθV 2(Xi)
(11.278)
= nJ(θ).
(11.279)
Consequently, the Fisher information for n i.i.d. samples is n times the
individual Fisher information. The signiﬁcance of the Fisher information
is shown in the following theorem.
Theorem 11.10.1
(Cram´er–Rao inequality)
The mean-squared error
of any unbiased estimator T (X) of the parameter θ is lower bounded by
the reciprocal of the Fisher information:
var(T ) ≥
1
J(θ).
(11.280)
Proof:
Let V be the score function and T be the estimator. By the
Cauchy–Schwarz inequality, we have
(Eθ[(V −EθV )(T −EθT )])2 ≤Eθ(V −EθV )2Eθ(T −EθT )2.
(11.281)
Since T is unbiased, EθT = θ for all θ. By (11.269), EθV = 0 and hence
Eθ(V −EθV )(T −EθT ) = Eθ(V T ). Also, by deﬁnition, var(V ) = J(θ).
Substituting these conditions in (11.281), we have
[Eθ(V T )]2 ≤J(θ)var(T ).
(11.282)
Now,
Eθ(V T ) =

∂
∂θ f (x; θ)
f (x; θ) T (x)f (x; θ) dx
(11.283)


## PDF page 422

396
INFORMATION THEORY AND STATISTICS
=

∂
∂θ f (x; θ)T (x) dx
(11.284)
= ∂
∂θ

f (x; θ)T (x) dx
(11.285)
= ∂
∂θ EθT
(11.286)
= ∂
∂θ θ
(11.287)
= 1,
(11.288)
where the interchange of differentiation and integration in (11.285) can be
justiﬁed using the bounded convergence theorem for appropriately well
behaved f (x; θ), and (11.287) follows from the fact that the estimator T
is unbiased. Substituting this in (11.282), we obtain
var(T ) ≥
1
J(θ),
(11.289)
which is the Cram´er–Rao inequality for unbiased estimators.
□
By essentially the same arguments, we can show that for any estimator
E(T −θ)2 ≥(1 + b′
T (θ))2
J(θ)
+ b2
T (θ),
(11.290)
where bT (θ) = EθT −θ and b′
T (θ) is the derivative of bT (θ) with respect
to θ. The proof of this is left as a problem at the end of the chapter.
Example 11.10.2
Let X1, X2, . . . , Xn be i.i.d. ∼N(θ, σ 2), σ 2 known.
Here
J(θ) = n/σ 2.
Let
T (X1, X2, . . . , Xn) = Xn = 1
n
 Xi.
Then
Eθ(Xn −θ)2 = σ 2/n = 1/J(θ). Thus, Xn is the minimum variance unbi-
ased estimator of θ, since it achieves the Cram´er–Rao lower bound.
The Cram´er–Rao inequality gives us a lower bound on the variance
for all unbiased estimators. When this bound is achieved, we call the
estimator efﬁcient.
Deﬁnition
An unbiased estimator T is said to be efﬁcient if it meets
the Cram´er–Rao bound with equality [i.e., if var(T ) =
1
J(θ)].


## PDF page 423

SUMMARY
397
The Fisher information is therefore a measure of the amount of “infor-
mation” about θ that is present in the data. It gives a lower bound on the
error in estimating θ from the data. However, it is possible that there does
not exist an estimator meeting this lower bound.
We can generalize the concept of Fisher information to the multipa-
rameter case, in which case we deﬁne the Fisher information matrix J(θ)
with elements
Jij(θ) =

f (x; θ) ∂
∂θi
ln f (x; θ) ∂
∂θj
ln f (x; θ) dx.
(11.291)
The Cram´er–Rao inequality becomes the matrix inequality
 ≥J −1(θ),
(11.292)
where  is the covariance matrix of a set of unbiased estimators for the
parameters θ and  ≥J −1(θ) in the sense that the difference  −J −1 is
a nonnegative deﬁnite matrix. We will not go into the details of the proof
for multiple parameters; the basic ideas are similar.
Is there a relationship between the Fisher information J(θ) and quanti-
ties such as entropy deﬁned earlier? Note that Fisher information is deﬁned
with respect to a family of parametric distributions, unlike entropy, which
is deﬁned for all distributions. But we can parametrize any distribution
f (x) by a location parameter θ and deﬁne Fisher information with respect
to the family of densities f (x −θ) under translation. We explore the
relationship in greater detail in Section 17.8, where we show that while
entropy is related to the volume of the typical set, the Fisher information
is related to the surface area of the typical set. Further relationships of
Fisher information to relative entropy are developed in the problems.
SUMMARY
Basic identities
Qn(x) = 2−n(D(Px||Q)+H(Px)),
(11.293)
|Pn| ≤(n + 1)|X|,
(11.294)
|T (P )| .= 2nH(P),
(11.295)
Qn(T (P )) .= 2−nD(P||Q).
(11.296)


## PDF page 424

398
INFORMATION THEORY AND STATISTICS
Universal data compression
P (n)
e
≤2−nD(P ∗
R||Q)
for all Q,
(11.297)
where
D(P ∗
R||Q) =
min
P:H(P)≥R D(P ||Q).
(11.298)
Large deviations (Sanov’s theorem)
Qn(E) = Qn(E ∩Pn) ≤(n + 1)|X|2−nD(P ∗||Q),
(11.299)
D(P ∗||Q) = min
P∈E D(P ||Q).
(11.300)
If E is the closure of its interior, then
Qn(E) .= 2−nD(P ∗||Q).
(11.301)
L1 bound on relative entropy
D(P1||P2) ≥
1
2 ln 2||P1 −P2||2
1.
(11.302)
Pythagorean theorem. If E is a convex set of types, distribution Q /∈
E, and P ∗achieves D(P ∗||Q) = minP∈E D(P ||Q), we have
D(P ||Q) ≥D(P ||P ∗) + D(P ∗||Q)
(11.303)
for all P ∈E.
Conditional limit theorem. If X1, X2, . . . , Xn i.i.d. ∼Q, then
Pr(X1 = a|PXn ∈E) →P ∗(a)
in probability,
(11.304)
where P ∗minimizes D(P ||Q) over P ∈E. In particular,
Pr

X1 = a

1
n
n

i=1
Xi ≥α

→
Q(a)eλa

x Q(x)eλx .
(11.305)
Neyman–Pearson lemma. The optimum test between two densities
P1 and P2 has a decision region of the form “accept P = P1 if
P1(x1,x2,...,xn)
P2(x1,x2,...,xn) > T.”


