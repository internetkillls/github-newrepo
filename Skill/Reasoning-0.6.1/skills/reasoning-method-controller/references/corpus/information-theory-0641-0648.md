# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 641

16.1
THE STOCK MARKET: SOME DEFINITIONS
615
the sum of i.i.d. versions of the random variable. But in the stock market,
one normally reinvests every day, so that the wealth at the end of n days
is the product of factors, one for each day of the market. The behavior of
the product is determined not by the expected value but by the expected
logarithm. This leads us to deﬁne the growth rate as follows:
Deﬁnition
The growth rate of a stock market portfolio b with respect
to a stock distribution F(x) is deﬁned as
W(b, F) =

log btx dF(x) = E

log btX

.
(16.1)
If the logarithm is to base 2, the growth rate is also called the doubling
rate.
Deﬁnition
The optimal growth rate W ∗(F) is deﬁned as
W ∗(F) = max
b
W(b, F),
(16.2)
where the maximum is over all possible portfolios bi ≥0, 
i bi = 1.
Deﬁnition
A portfolio b∗that achieves the maximum of W(b, F) is
called a log-optimal portfolio or growth optimal portfolio.
The deﬁnition of growth rate is justiﬁed by the following theorem,
which shows that wealth grows as 2nW ∗.
Theorem 16.1.1
Let X1, X2, . . . , Xn be i.i.d. according to F(x). Let
S∗
n =
n

i=1
b∗tXi
(16.3)
be the wealth after n days using the constant rebalanced portfolio b∗. Then
1
n log S∗
n →W ∗
with probability 1.
(16.4)
Proof:
By the strong law of large numbers,
1
n log S∗
n = 1
n
n

i=1
log b∗tXi
(16.5)
→W ∗
with probability 1.
(16.6)
Hence, S∗
n
.= 2nW ∗.
□


## PDF page 642

616
INFORMATION THEORY AND PORTFOLIO THEORY
We now consider some of the properties of the growth rate.
Lemma 16.1.1
W(b, F) is concave in b and linear in F. W ∗(F) is
convex in F.
Proof:
The growth rate is
W(b, F) =

log btx dF(x).
(16.7)
Since the integral is linear in F, so is W(b, F). Since
log(λb1 + (1 −λ)b2)tX ≥λ log bt
1X + (1 −λ) log bt
2X,
(16.8)
by the concavity of the logarithm, it follows, by taking expectations, that
W(b, F) is concave in b. Finally, to prove the convexity of W ∗(F) as a
function of F, let F1 and F2 be two distributions on the stock market and
let the corresponding optimal portfolios be b∗(F1) and b∗(F2), respec-
tively. Let the log-optimal portfolio corresponding to λF1 + (1 −λ)F2 be
b∗(λF1 + (1 −λ)F2). Then by linearity of W(b, F) with respect to F,
we have
W ∗(λF1 + (1 −λ)F2)
= W(b∗(λF1 + (1 −λ)F2), λF1 + (1 −λ)F2)
(16.9)
= λW(b∗(λF1 + (1 −λ)F2), F1)
+ (1 −λ)W(b∗(λF1 + (1 −λ)F2), F2)
≤λW(b∗(F1), F1) + (1 −λ)W ∗(b∗(F2), F2),
(16.10)
since b∗(F1) maximizes W(b, F1) and b∗(F2) maximizes W(b, F2).
□
Lemma 16.1.2
The set of log-optimal portfolios with respect to a given
distribution is convex.
Proof:
Supposethatb1 andb2 arelog-optimal(i.e.,W(b1, F) = W(b2, F)
= W ∗(F)). By the concavity of W(b, F) in b, we have
W(λb1 + (1 −λ)b2, F) ≥λW(b1, F) + (1 −λ)W(b2, F) = W ∗(F).
(16.11)
Thus, λb1 + (1 −λ)b2 is also log-optimal.
□
In the next section we use these properties to characterize the log-
optimal portfolio.


## PDF page 643

16.2
KUHN–TUCKER CHARACTERIZATION OF THE LOG-OPTIMAL PORTFOLIO
617
16.2
KUHN–TUCKER CHARACTERIZATION
OF THE LOG-OPTIMAL PORTFOLIO
Let B = {b ∈Rm : bi ≥0, m
i=1bi = 1} denote the set of allowed port-
folios. The determination of b∗that achieves W ∗(F) is a problem of
maximization of a concave function W(b, F) over a convex set B. The
maximum may lie on the boundary. We can use the standard Kuhn–Tucker
conditions to characterize the maximum. Instead, we derive these condi-
tions from ﬁrst principles.
Theorem 16.2.1
The log-optimal portfolio b∗for a stock market X ∼F
(i.e., the portfolio that maximizes the growth rate W(b, F)) satisﬁes the
following necessary and sufﬁcient conditions:
E
 Xi
b∗tX

= 1
if b∗
i > 0,
≤1
if b∗
i = 0.
(16.12)
Proof:
The growth rate W(b) = E(ln btX) is concave in b, where b
ranges over the simplex of portfolios. It follows that b∗is log-optimum
iff the directional derivative of W(·) in the direction from b∗to any
alternative portfolio b is nonpositive. Thus, letting bλ = (1 −λ)b∗+ λb
for 0 ≤λ ≤1, we have
d
dλW(bλ)
			
λ=0+ ≤0,
b ∈B.
(16.13)
These conditions reduce to (16.12) since the one-sided derivative at λ =
0+ of W(bλ) is
d
dλE(ln(bt
λX))
			
λ=0+
= lim
λ↓0
1
λE

ln
(1 −λ)b∗tX + λbtX
b∗tX

(16.14)
= E

lim
λ↓0
1
λ ln

1 + λ
 btX
b∗tX −1

(16.15)
= E
 btX
b∗tX

−1,
(16.16)
where the interchange of limit and expectation can be justiﬁed using the
dominated convergence theorem [39]. Thus, (16.13) reduces to
E
 btX
b∗tX

−1 ≤0
(16.17)


## PDF page 644

618
INFORMATION THEORY AND PORTFOLIO THEORY
for all b ∈B. If the line segment from b to b∗can be extended beyond b∗
in the simplex, the two-sided derivative at λ = 0 of W(bλ) vanishes and
(16.17) holds with equality. If the line segment from b to b∗cannot be
extended because of the inequality constraint on b, we have an inequality
in (16.17).
The Kuhn–Tucker conditions will hold for all portfolios b ∈B if they
hold for all extreme points of the simplex B since E(btX/b∗tX) is linear
in b. Furthermore, the line segment from the jth extreme point (b : bj =
1, bi = 0, i ̸= j) to b∗can be extended beyond b∗in the simplex iff b∗
j >
0. Thus, the Kuhn–Tucker conditions that characterize the log-optimum
b∗are equivalent to the following necessary and sufﬁcient conditions:
E
 Xi
b∗tX

= 1
if b∗
i > 0,
≤1
if b∗
i = 0.
□
(16.18)
This theorem has a few immediate consequences. One useful equiva-
lence is expressed in the following theorem.
Theorem 16.2.2
Let S∗= b∗tX be the random wealth resulting from
the log-optimal portfolio b∗. Let S = btX be the wealth resulting from any
other portfolio b. Then
E ln S
S∗≤0
for all S
⇔
E S
S∗≤1
for all S.
(16.19)
Proof:
From Theorem 16.2.1 it follows that for a log-optimal portfolio
b∗,
E
 Xi
b∗tX

≤1
(16.20)
for all i. Multiplying this equation by bi and summing over i, we have
m

i=1
biE
 Xi
b∗tX

≤
m

i=1
bi = 1,
(16.21)
which is equivalent to
E btX
b∗tX = E S
S∗≤1.
(16.22)
The converse follows from Jensen’s inequality, since
E log S
S∗≤log E S
S∗≤log 1 = 0.
□
(16.23)


## PDF page 645

16.3
ASYMPTOTIC OPTIMALITY OF THE LOG-OPTIMAL PORTFOLIO
619
Maximizing the expected logarithm was motivated by the asymptotic
growth rate. But we have just shown that the log-optimal portfolio, in
addition to maximizing the asymptotic growth rate, also “maximizes” the
expected wealth relative E(S/S∗) for one day. We shall say more about
the short-term optimality of the log-optimal portfolio when we consider
the game-theoretic optimality of this portfolio.
Another consequence of the Kuhn–Tucker characterization of the log-
optimal portfolio is the fact that the expected proportion of wealth in
each stock under the log-optimal portfolio is unchanged from day to day.
Consider the stocks at the end of the ﬁrst day. The initial allocation of
wealth is b∗. The proportion of the wealth in stock i at the end of the day
is
b∗
i Xi
b∗tX, and the expected value of this proportion is
E b∗
i Xi
b∗tX = b∗
i E Xi
b∗tX = b∗
i .
(16.24)
Hence, the proportion of wealth in stock i expected at the end of the
day is the same as the proportion invested in stock i at the beginning of
the day. This is a counterpart to Kelly proportional gambling, where one
invests in proportions that remain unchanged in expected value after the
investment period.
16.3
ASYMPTOTIC OPTIMALITY OF THE LOG-OPTIMAL
PORTFOLIO
In Section 16.2 we introduced the log-optimal portfolio and explained its
motivation in terms of the long-term behavior of a sequence of investments
in a repeated independent versions of the stock market. In this section we
expand on this idea and prove that with probability 1, the conditionally
log-optimal investor will not do any worse than any other investor who
uses a causal investment strategy.
We ﬁrst consider an i.i.d. stock market (i.e., X1, X2, . . . , Xn are i.i.d.
according to F(x)). Let
Sn =
n

i=1
bt
iXi
(16.25)
be the wealth after n days for an investor who uses portfolio bi on day i.
Let
W ∗= max
b
W(b, F) = max
b
E log btX
(16.26)


## PDF page 646

620
INFORMATION THEORY AND PORTFOLIO THEORY
be the maximal growth rate, and let b∗be a portfolio that achieves the
maximum growth rate. We only allow alternative portfolios bi that depend
causally on the past and are independent of the future values of the stock
market.
Deﬁnition
A nonanticipating or causal portfolio strategy is a sequence
of mappings bi : Rm(i−1) →B, with the interpretation that portfolio bi(x1,
. . . , xi−1) is used on day i.
From the deﬁnition of W ∗, it follows immediately that the log-optimal
portfolio maximizes the expected log of the ﬁnal wealth. This is stated in
the following lemma.
Lemma 16.3.1
Let S∗
n be the wealth after n days using the log-optimal
strategy b∗on i.i.d. stocks, and let Sn be the wealth using a causal portfolio
strategy bi. Then
E log S∗
n = nW ∗≥E log Sn.
(16.27)
Proof
max
b1,b2,...,bn E log Sn =
max
b1,b2,...,bn E
n

i=1
log bt
iXi
(16.28)
=
n

i=1
max
bi(X1,X2,...,Xi−1) E log bt
i(X1, X2, . . . , Xi−1)Xi
(16.29)
=
n

i=1
E log b∗tXi
(16.30)
= nW ∗,
(16.31)
and the maximum is achieved by a constant portfolio strategy b∗.
□
So far, we have proved two simple consequences of the deﬁnition of
log-optimal portfolios: that b∗(satisfying (16.12)) maximizes the expected
log wealth, and that the resulting wealth S∗
n is equal to 2nW ∗to ﬁrst order
in the exponent, with high probability.
Now we prove a much stronger result, which shows that S∗
n exceeds
the wealth (to ﬁrst order in the exponent) of any other investor for almost
every sequence of outcomes from the stock market.
Theorem 16.3.1
(Asymptotic optimality of the log-optimal portfolio)
Let X1, X2, . . . , Xn be a sequence of i.i.d. stock vectors drawn according


## PDF page 647

16.4
SIDE INFORMATION AND THE GROWTH RATE
621
to F(x). Let S∗
n = 
n
i=1 b∗tXi, where b∗is the log-optimal portfolio, and
let Sn = 
n
i=1 bt
iXi be the wealth resulting from any other causal portfolio.
Then
lim sup
n→∞
1
n log Sn
S∗n
≤0
with probability 1.
(16.32)
Proof:
From the Kuhn–Tucker conditions and the log optimality of S∗
n,
we have
E Sn
S∗n
≤1.
(16.33)
Hence by Markov’s inequality, we have
Pr

Sn > tnS∗
n

= Pr
Sn
S∗n
> tn

< 1
tn
.
(16.34)
Hence,
Pr
1
n log Sn
S∗n
> 1
n log tn

≤1
tn
.
(16.35)
Setting tn = n2 and summing over n, we have
∞

n=1
Pr
1
n log Sn
S∗n
> 2 log n
n

≤
∞

n=1
1
n2 = π2
6 .
(16.36)
Then, by the Borel–Cantelli lemma,
Pr
1
n log Sn
S∗n
> 2 log n
n
, inﬁnitely often

= 0.
(16.37)
This implies that for almost every sequence from the stock market, there
exists an N such that for all n > N, 1
n log Sn
S∗n < 2 log n
n
. Thus,
lim sup 1
n log Sn
S∗n
≤0
with probability 1.
□
(16.38)
The theorem proves that the log-optimal portfolio will perform as well
as or better than any other portfolio to ﬁrst order in the exponent.
16.4
SIDE INFORMATION AND THE GROWTH RATE
We showed in Chapter 6 that side information Y for the horse race X can
be used to increase the growth rate by the mutual information I (X; Y).


## PDF page 648

622
INFORMATION THEORY AND PORTFOLIO THEORY
We now extend this result to the stock market. Here, I (X; Y) is an upper
bound on the increase in the growth rate, with equality if X is a horse
race. We ﬁrst consider the decrease in growth rate incurred by believing
in the wrong distribution.
Theorem 16.4.1
Let X ∼f (x). Let bf be a log-optimal portfolio cor-
responding to f (x), and let bg be a log-optimal portfolio corresponding
to some other density g(x). Then the increase in growth rate W by using
bf instead of bg is bounded by
W = W(bf , F) −W(bg, F) ≤D(f ||g).
(16.39)
Proof:
We have
W =

f (x) log bt
f x −

f (x) log bt
gx
(16.40)
=

f (x) log
bt
f x
btgx
(16.41)
=

f (x) log
bt
f x
btgx
g(x)
f (x)
f (x)
g(x)
(16.42)
=

f (x) log
bt
f x
btgx
g(x)
f (x) + D(f ||g)
(16.43)
(a)
≤log

f (x)
bt
f x
btgx
g(x)
f (x) + D(f ||g)
(16.44)
= log

g(x)
bt
f x
btgx + D(f ||g)
(16.45)
(b)
≤log 1 + D(f ||g)
(16.46)
= D(f ||g),
(16.47)
where (a) follows from Jensen’s inequality and (b) follows from the
Kuhn–Tucker conditions and the fact that bg is log-optimal for g.
□
Theorem 16.4.2
The increase W in growth rate due to side informa-
tion Y is bounded by
W ≤I (X; Y).
(16.48)


