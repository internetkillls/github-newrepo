# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 409

11.8
CHERNOFF–STEIN LEMMA
383
Lemma 11.8.1
Let Bn ⊂Xn be any set of sequences x1, x2, . . . , xn such
that P1(Bn) > 1 −ϵ. Let P2 be any other distribution such that D(P1||P2)
< ∞. Then P2(Bn) > (1 −2ϵ)2−n(D(P1||P2)+ϵ).
Proof:
For simplicity, we will denote A(n)
ϵ (P1||P2) by An. Since P1(Bn)
> 1 −ϵ and P (An) > 1 −ϵ (Theorem 11.8.2), we have, by the union of
events bound, P1(Ac
n ∪Bc
n) < 2ϵ, or equivalently, P1(An ∩Bn) > 1 −2ϵ.
Thus,
P2(Bn) ≥P2(An ∩Bn)
(11.218)
=

xn∈An∩Bn
P2(xn)
(11.219)
≥

xn∈An∩Bn
P1(xn)2−n(D(P1||P2)+ϵ)
(11.220)
= 2−n(D(P1||P2)+ϵ)

xn∈An∩Bn
P1(xn)
(11.221)
= 2−n(D(P1||P2)+ϵ)P1(An ∩Bn)
(11.222)
≥2−n(D(P1||P2)+ϵ)(1 −2ϵ),
(11.223)
where the second inequality follows from the properties of the relative
entropy typical sequences (Theorem 11.8.2) and the last inequality follows
from the union bound above.
□
We now consider the problem of testing two hypotheses, P1 vs. P2. We
hold one of the probabilities of error ﬁxed and attempt to minimize the
other probability of error. We show that the relative entropy is the best
exponent in probability of error.
Theorem 11.8.3
(Chernoff–Stein Lemma)
Let X1, X2, . . . , Xn be
i.i.d. ∼Q. Consider the hypothesis test between two alternatives, Q = P1
and Q = P2, where D(P1||P2) < ∞. Let An ⊆Xn be an acceptance
region for hypothesis H1. Let the probabilities of error be
αn = P n
1 (Ac
n),
βn = P n
2 (An).
(11.224)
and for 0 < ϵ < 1
2, deﬁne
βϵ
n =
min
An ⊆Xn
αn < ϵ
βn.
(11.225)


## PDF page 410

384
INFORMATION THEORY AND STATISTICS
Then
lim
n→∞
1
n log βϵ
n = −D(P1||P2).
(11.226)
Proof:
We prove this theorem in two parts. In the ﬁrst part we exhibit
a sequence of sets An for which the probability of error βn goes expo-
nentially to zero as D(P1||P2). In the second part we show that no other
sequence of sets can have a lower exponent in the probability of error.
For the ﬁrst part, we choose as the sets An = A(n)
ϵ (P1||P2). As proved in
Theorem 11.8.2, this sequence of sets has P1(Ac
n) < ϵ for n large enough.
Also,
lim
n→∞
1
n log P2(An) ≤−(D(P1||P2) −ϵ)
(11.227)
from property 3 of Theorem 11.8.2. Thus, the relative entropy typical set
satisﬁes the bounds of the lemma.
To show that no other sequence of sets can to better, consider any
sequence of sets Bn with P1(Bn) > 1 −ϵ. By Lemma 11.8.1, we have
P2(Bn) > (1 −2ϵ)2−n(D(P1||P2)+ϵ), and therefore
lim
n→∞
1
n log P2(Bn) > −(D(P1||P2) + ϵ) + lim
n→∞
1
n log(1 −2ϵ)
= −(D(P1||P2) + ϵ).
(11.228)
Thus, no other sequence of sets has a probability of error exponent better
than D(P1||P2). Thus, the set sequence An = A(n)
ϵ (P1||P2) is asymptoti-
cally optimal in terms of the exponent in the probability.
□
Not that the relative entropy typical set, although asymptotically opti-
mal (i.e., achieving the best asymptotic rate), is not the optimal set for
any ﬁxed hypothesis-testing problem. The optimal set that minimizes the
probabilities of error is that given by the Neyman–Pearson lemma.
11.9
CHERNOFF INFORMATION
We have considered the problem of hypothesis testing in the classical
setting, in which we treat the two probabilities of error separately. In the
derivation of the Chernoff–Stein lemma, we set αn ≤ϵ and achieved
βn
.= 2−nD. But this approach lacks symmetry. Instead, we can fol-
low a Bayesian approach, in which we assign prior probabilities to both


## PDF page 411

11.9
CHERNOFF INFORMATION
385
hypotheses. In this case we wish to minimize the overall probability of
error given by the weighted sum of the individual probabilities of error.
The resulting error exponent is the Chernoff information.
The setup is as follows: X1, X2, . . . , Xn i.i.d. ∼Q. We have two
hypotheses: Q = P1 with prior probability π1 and Q = P2 with prior
probability π2. The overall probability of error is
P (n)
e
= π1αn + π2βn.
(11.229)
Let
D∗= lim
n→∞−1
n log min
An⊆X n P (n)
e
.
(11.230)
Theorem 11.9.1
(Chernoff )
The best achievable exponent in the
Bayesian probability of error is D∗, where
D∗= D(Pλ∗||P1) = D(Pλ∗||P2),
(11.231)
with
Pλ =
P λ
1 (x)P 1−λ
2
(x)

a∈X P λ
1 (a)P 1−λ
2
(a)
,
(11.232)
and λ∗the value of λ such that
D(Pλ∗||P1) = D(Pλ∗||P2).
(11.233)
Proof:
The basic details of the proof were given in Section 11.8. We
have shown that the optimum test is a likelihood ratio test, which can be
considered to be of the form
D(PXn||P2) −D(PXn||P1) > 1
n log T.
(11.234)
The test divides the probability simplex into regions corresponding to
hypothesis 1 and hypothesis 2, respectively. This is illustrated in Fig-
ure 11.10.
Let A be the set of types associated with hypothesis 1. From the dis-
cussion preceding (11.200), it follows that the closest point in the set Ac
to P1 is on the boundary of A and is of the form given by (11.232). Then
from the discussion in Section 11.8, it is clear that Pλ is the distribution


## PDF page 412

386
INFORMATION THEORY AND STATISTICS
P1
P2
Pl
FIGURE 11.10. Probability simplex and Chernoff information.
in A that is closest to P2; it is also the distribution in Ac that is closest
to P1. By Sanov’s theorem, we can calculate the associated probabilities
of error,
αn = P n
1 (Ac)
.= 2−nD(Pλ∗||P1)
(11.235)
and
βn = P n
2 (A)
.= 2−nD(Pλ∗||P2).
(11.236)
In the Bayesian case, the overall probability of error is the weighted sum
of the two probabilities of error,
Pe
.= π12−nD(Pλ||P1) + π22−nD(Pλ||P2)
.= 2−n min{D(Pλ||P1),D(Pλ||P2)},
(11.237)
since the exponential rate is determined by the worst exponent. Since
D(Pλ||P1) increases with λ and D(Pλ||P2) decreases with λ, the maxi-
mum value of the minimum of {D(Pλ||P1), D(Pλ||P2)} is attained when
they are equal. This is illustrated in Figure 11.11. Hence, we choose λ so
that
D(Pλ||P1) = D(Pλ||P2).
(11.238)
Thus, C(P1, P2) is the highest achievable exponent for the probability of
error and is called the Chernoff information.
□


## PDF page 413

11.9
CHERNOFF INFORMATION
387
2
D(Pl||P1)
D(Pl||P2)
Relative entropy
2.5
1.5
0.5
0
1
0
0.1
0.2
0.3
0.4
l
0.5
0.6
0.7
0.8
0.9
1
FIGURE 11.11. Relative entropy D(Pλ||P1) and D(Pλ||P2) as a function of λ.
The deﬁnition D∗= D(Pλ∗||P1) = D(Pλ∗||P2) is equivalent to the
standard deﬁnition of Chernoff information,
C(P1, P2)
△= −min
0≤λ≤1 log

x
P λ
1 (x)P 1−λ
2
(x)

.
(11.239)
It is left as an exercise to the reader to show the equivalence of (11.231)
and (11.239).
We outline brieﬂy the usual derivation of the Chernoff information
bound. The maximum a posteriori probability decision rule minimizes the
Bayesian probability of error. The decision region A for hypothesis H1
for the maximum a posteriori rule is
A =

x : π1P1(x)
π2P2(x) > 1

,
(11.240)
the set of outcomes where the a posteriori probability of hypothesis H1 is
greater than the a posteriori probability of hypothesis H2. The probability
of error for this rule is
Pe = π1αn + π2βn
(11.241)
=

Ac
π1P1 +

A
π2P2
(11.242)
=

min{π1P1, π2P2}.
(11.243)


## PDF page 414

388
INFORMATION THEORY AND STATISTICS
Now for any two positive numbers a and b, we have
min{a, b} ≤aλb1−λ
for all 0 ≤λ ≤1.
(11.244)
Using this to continue the chain, we have
Pe =

min{π1P1, π2P2}
(11.245)
≤

(π1P1)λ(π2P2)1−λ
(11.246)
≤

P λ
1 P 1−λ
2
.
(11.247)
For a sequence of i.i.d. observations, Pk(x) = n
i=1 Pk(xi), and
P (n)
e
≤

πλ
1 π1−λ
2

i
P λ
1 (xi)P 1−λ
2
(xi)
(11.248)
= πλ
1 π1−λ
2

i

P λ
1 (xi)P 1−λ
2
(xi)
(11.249)
≤

xi

P λ
1 P 1−λ
2
(11.250)
=

x
P λ
1 P 1−λ
2
n
,
(11.251)
where (11.250) follows since π1 ≤1, π2 ≤1. Hence, we have
1
n log P (n)
e
≤log

P λ
1 (x)P 1−λ
2
(x).
(11.252)
Since this is true for all λ, we can take the minimum over 0 ≤λ ≤1,
resulting in the Chernoff information bound. This proves that the exponent
is no better than C(P1, P2). Achievability follows from Theorem 11.9.1.
Note that the Bayesian error exponent does not depend on the actual
value of π1 and π2, as long as they are nonzero. Essentially, the effect of
the prior is washed out for large sample sizes. The optimum decision rule
is to choose the hypothesis with the maximum a posteriori probability,
which corresponds to the test
π1P1(X1, X2, . . . , Xn)
π2P2(X1, X2, . . . , Xn)
>< 1.
(11.253)


## PDF page 415

11.9
CHERNOFF INFORMATION
389
Taking the log and dividing by n, this test can be rewritten as
1
n log π1
π2
+ 1
n

i
log P1(Xi)
P2(Xi)
<> 0,
(11.254)
where the second term tends to D(P1||P2) or −D(P2||P1) accordingly as
P1 or P2 is the true distribution. The ﬁrst term tends to 0, and the effect
of the prior distribution washes out.
Finally, to round off our discussion of large deviation theory and hypoth-
esis testing, we consider an example of the conditional limit theorem.
Example 11.9.1
Suppose that major league baseball players have a bat-
ting average of 260 with a standard deviation of 15 and suppose that
minor league ballplayers have a batting average of 240 with a standard
deviation of 15. A group of 100 ballplayers from one of the leagues (the
league is chosen at random) are found to have a group batting average
greater than 250 and are therefore judged to be major leaguers. We are
now told that we are mistaken; these players are minor leaguers. What
can we say about the distribution of batting averages among these 100
players? The conditional limit theorem can be used to show that the dis-
tribution of batting averages among these players will have a mean of 250
and a standard deviation of 15. To see this, we abstract the problem as
follows.
Let us consider an example of testing between two Gaussian distribu-
tions, f1 = N(1, σ 2) and f2 = N(−1, σ 2), with different means and the
same variance. As discussed in Section 11.8, the likelihood ratio test in
this case is equivalent to comparing the sample mean with a threshold.
The Bayes test is “Accept the hypothesis f = f1 if 1
n
n
i=1 Xi > 0.” Now
assume that we make an error of the ﬁrst kind (we say that f = f1 when
indeed f = f2) in this test. What is the conditional distribution of the
samples given that we have made an error?
We might guess at various possibilities:
• The sample will look like a ( 1
2, 1
2) mix of the two normal distributions.
Plausible as this is, it is incorrect.
• Xi ≈0 for all i. This is quite clearly very unlikely, although it is
conditionally likely that Xn is close to 0.
• The correct answer is given by the conditional limit theorem. If the
true distribution is f2 and the sample type is in the set A, the condi-
tional distribution is close to f ∗, the distribution in A that is closest to
f2. By symmetry, this corresponds to λ = 1
2 in (11.232). Calculating


## PDF page 416

390
INFORMATION THEORY AND STATISTICS
the distribution, we get
f ∗(x) =

1
√
2πσ 2 e−(x−1)2
2σ2
 1
2 
1
√
2πσ 2 e−(x+1)2
2σ2
 1
2
 
1
√
2πσ 2 e−(x−1)2
2σ2
 1
2 
1
√
2πσ 2 e−(x+1)2
2σ2
 1
2
dx
(11.255)
=
1
√
2πσ 2 e−(x2+1)
2σ2

1
√
2πσ 2 e−(x2+1)
2σ2
dx
(11.256)
=
1
√
2πσ 2 e−x2
2σ2
(11.257)
= N(0, σ 2).
(11.258)
It is interesting to note that the conditional distribution is normal with
mean 0 and with the same variance as the original distributions. This
is strange but true; if we mistake a normal population for another, the
“shape” of this population still looks normal with the same variance
and a different mean. Apparently, this rare event does not result from
bizarre-looking data.
Example 11.9.2
(Large deviation theory and football)
Consider a very
simple version of football in which the score is directly related to the
number of yards gained. Assume that the coach has a choice between two
strategies: running or passing. Associated with each strategy is a distri-
bution on the number of yards gained. For example, in general, running
Yards gained in pass
Probability density
Yards gained in run
Probability density
FIGURE 11.12. Distribution of yards gained in a run or a pass play.


