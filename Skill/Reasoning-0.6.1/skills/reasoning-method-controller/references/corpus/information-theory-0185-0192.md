# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 185

CHAPTER 6
GAMBLING AND DATA
COMPRESSION
At ﬁrst sight, information theory and gambling seem to be unrelated.
But as we shall see, there is strong duality between the growth rate of
investment in a horse race and the entropy rate of the horse race. Indeed,
the sum of the growth rate and the entropy rate is a constant. In the process
of proving this, we shall argue that the ﬁnancial value of side information
is equal to the mutual information between the horse race and the side
information. The horse race is a special case of investment in the stock
market, studied in Chapter 16.
We also show how to use a pair of identical gamblers to compress a
sequence of random variables by an amount equal to the growth rate of
wealth on that sequence. Finally, we use these gambling techniques to
estimate the entropy rate of English.
6.1
THE HORSE RACE
Assume that m horses run in a race. Let the ith horse win with probability
pi. If horse i wins, the payoff is oi for 1 (i.e., an investment of 1 dollar
on horse i results in oi dollars if horse i wins and 0 dollars if horse i
loses).
There are two ways of describing odds: a-for-1 and b-to-1. The ﬁrst
refers to an exchange that takes place before the race—the gambler puts
down 1 dollar before the race and at a-for-1 odds will receive a dollars
after the race if his horse wins, and will receive nothing otherwise. The
second refers to an exchange after the race—at b-to-1 odds, the gambler
will pay 1 dollar after the race if his horse loses and will pick up b dollars
after the race if his horse wins. Thus, a bet at b-to-1 odds is equivalent to
a bet at a-for-1 odds if b = a −1. For example, fair odds on a coin ﬂip
would be 2-for-1 or 1-to-1, otherwise known as even odds.
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
159


## PDF page 186

160
GAMBLING AND DATA COMPRESSION
We assume that the gambler distributes all of his wealth across the
horses. Let bi be the fraction of the gambler’s wealth invested in horse i,
where bi ≥0 and  bi = 1. Then if horse i wins the race, the gambler
will receive oi times the amount of wealth bet on horse i. All the other
bets are lost. Thus, at the end of the race, the gambler will have multiplied
his wealth by a factor bioi if horse i wins, and this will happen with prob-
ability pi. For notational convenience, we use b(i) and bi interchangeably
throughout this chapter.
The wealth at the end of the race is a random variable, and the gambler
wishes to “maximize” the value of this random variable. It is tempting to
bet everything on the horse that has the maximum expected return (i.e.,
the one with the maximum pioi). But this is clearly risky, since all the
money could be lost.
Some clarity results from considering repeated gambles on this race.
Now since the gambler can reinvest his money, his wealth is the product
of the gains for each race. Let Sn be the gambler’s wealth after n races.
Then
Sn =
n

i=1
S(Xi),
(6.1)
where S(X) = b(X)o(X) is the factor by which the gambler’s wealth is
multiplied when horse X wins.
Deﬁnition
The wealth relative S(X) = b(X)o(X) is the factor by which
the gambler’s wealth grows if horse X wins the race.
Deﬁnition
The doubling rate of a horse race is
W(b, p) = E(log S(X)) =
m

k=1
pk log bkok.
(6.2)
The deﬁnition of doubling rate is justiﬁed by the following theorem.
Theorem 6.1.1
Let the race outcomes X1, X2, . . . be i.i.d. ∼p(x).
Then the wealth of the gambler using betting strategy b grows exponen-
tially at rate W(b, p); that is,
Sn
.= 2nW(b,p).
(6.3)


## PDF page 187

6.1
THE HORSE RACE
161
Proof:
Functions of independent random variables are also independent,
and hence log S(X1), log S(X2), . . . are i.i.d. Then, by the weak law of
large numbers,
1
n log Sn = 1
n
n

i=1
log S(Xi) →E(log S(X))
in probability.
(6.4)
Thus,
Sn
.= 2nW(b,p).
□
(6.5)
Now since the gambler’s wealth grows as 2nW(b,p), we seek to maximize
the exponent W(b, p) over all choices of the portfolio b.
Deﬁnition
The optimum doubling rate W ∗(p) is the maximum doubling
rate over all choices of the portfolio b:
W ∗(p) = max
b
W(b, p) =
max
b:bi≥0, 
i bi=1
m

i=1
pi log bioi.
(6.6)
We maximize W(b, p) as a function of b subject to the constraint
 bi = 1. Writing the functional with a Lagrange multiplier and changing
the base of the logarithm (which does not affect the maximizing b), we
have
J(b) =

pi ln bioi + λ

bi.
(6.7)
Differentiating this with respect to bi yields
∂J
∂bi
= pi
bi
+ λ,
i = 1, 2, . . . , m.
(6.8)
Setting the partial derivative equal to 0 for a maximum, we have
bi = −pi
λ .
(6.9)
Substituting this in the constraint  bi = 1 yields λ = −1 and bi = pi.
Hence, we can conclude that b = p is a stationary point of the function
J(b). To prove that this is actually a maximum is tedious if we take


## PDF page 188

162
GAMBLING AND DATA COMPRESSION
second derivatives. Instead, we use a method that works for many such
problems: Guess and verify. We verify that proportional gambling b = p
is optimal in the following theorem. Proportional gambling is known as
Kelly gambling [308].
Theorem 6.1.2
(Proportional gambling is log-optimal)
The optimum
doubling rate is given by
W ∗(p) =

pi log oi −H(p)
(6.10)
and is achieved by the proportional gambling scheme b∗= p.
Proof:
We rewrite the function W(b, p) in a form in which the maximum
is obvious:
W(b, p) =

pi log bioi
(6.11)
=

pi log
 bi
pi
pioi

(6.12)
=

pi log oi −H(p) −D(p||b)
(6.13)
≤

pi log oi −H(p),
(6.14)
with equality iff p = b (i.e., the gambler bets on each horse in proportion
to its probability of winning).
□
Example 6.1.1
Consider a case with two horses, where horse 1 wins
with probability p1 and horse 2 wins with probability p2. Assume even
odds (2-for-1 on both horses). Then the optimal bet is proportional bet-
ting (i.e., b1 = p1, b2 = p2). The optimal doubling rate is W ∗(p) =
 pi log oi −H(p) = 1 −H(p), and the resulting wealth grows to inﬁn-
ity at this rate:
Sn
.= 2n(1−H(p)).
(6.15)
Thus, we have shown that proportional betting is growth rate optimal
for a sequence of i.i.d. horse races if the gambler can reinvest his wealth
and if there is no alternative of keeping some of the wealth in cash.
We now consider a special case when the odds are fair with respect to
some distribution (i.e., there is no track take and  1
oi = 1). In this case,
we write ri = 1
oi , where ri can be interpreted as a probability mass function


## PDF page 189

6.1
THE HORSE RACE
163
over the horses. (This is the bookie’s estimate of the win probabilities.)
With this deﬁnition, we can write the doubling rate as
W(b, p) =

pi log bioi
(6.16)
=

pi log
 bi
pi
pi
ri

(6.17)
= D(p||r) −D(p||b).
(6.18)
This equation gives another interpretation for the relative entropy dis-
tance: The doubling rate is the difference between the distance of the
bookie’s estimate from the true distribution and the distance of the gam-
bler’s estimate from the true distribution. Hence, the gambler can make
money only if his estimate (as expressed by b) is better than the bookie’s.
An even more special case is when the odds are m-for-1 on each horse.
In this case, the odds are fair with respect to the uniform distribution and
the optimum doubling rate is
W ∗(p) = D

p|| 1
m

= log m −H(p).
(6.19)
In this case we can clearly see the duality between data compression and
the doubling rate.
Theorem 6.1.3
(Conservation theorem)
For uniform fair odds,
W ∗(p) + H(p) = log m.
(6.20)
Thus, the sum of the doubling rate and the entropy rate is a constant.
Every bit of entropy decrease doubles the gambler’s wealth. Low entropy
races are the most proﬁtable.
In the analysis above, we assumed that the gambler was fully invested.
In general, we should allow the gambler the option of retaining some of
his wealth as cash. Let b(0) be the proportion of wealth held out as cash,
and b(1), b(2), . . . , b(m) be the proportions bet on the various horses.
Then at the end of a race, the ratio of ﬁnal wealth to initial wealth (the
wealth relative) is
S(X) = b(0) + b(X)o(X).
(6.21)
Now the optimum strategy may depend on the odds and will not necessar-
ily have the simple form of proportional gambling. We distinguish three
subcases:


## PDF page 190

164
GAMBLING AND DATA COMPRESSION
1. Fair odds with respect to some distribution:  1
oi = 1. For fair odds,
the option of withholding cash does not change the analysis. This is
because we can get the effect of withholding cash by betting bi = 1
oi
on the ith horse, i = 1, 2, . . . , m. Then S(X) = 1 irrespective of
which horse wins. Thus, whatever money the gambler keeps aside
as cash can equally well be distributed over the horses, and the
assumption that the gambler must invest all his money does not
change the analysis. Proportional betting is optimal.
2. Superfair odds:  1
oi < 1. In this case, the odds are even better than
fair odds, so one would always want to put all one’s wealth into the
race rather than leave it as cash. In this race, too, the optimum
strategy is proportional betting. However, it is possible to choose
b so as to form a Dutch book by choosing bi = c 1
oi , where c =
1/  1
ci , to get oibi = c, irrespective of which horse wins. With
this allotment, one has wealth S(X) = 1/  1
oi > 1 with probability
1 (i.e., no risk). Needless to say, one seldom ﬁnds such odds in
real life. Incidentally, a Dutch book, although risk-free, does not
optimize the doubling rate.
3. Subfair odds:  1
oi > 1. This is more representative of real life. The
organizers of the race track take a cut of all the bets. In this case it
is optimal to bet only some of the money and leave the rest aside
as cash. Proportional gambling is no longer log-optimal. A paramet-
ric form for the optimal strategy can be found using Kuhn–Tucker
conditions (Problem 6.6.2); it has a simple “water-ﬁlling” interpre-
tation.
6.2
GAMBLING AND SIDE INFORMATION
Suppose the gambler has some information that is relevant to the outcome
of the gamble. For example, the gambler may have some information
about the performance of the horses in previous races. What is the value
of this side information?
One deﬁnition of the ﬁnancial value of such information is the increase
in wealth that results from that information. In the setting described in
Section 6.1 the measure of the value of information is the increase in the
doubling rate due to that information. We will now derive a connection
between mutual information and the increase in the doubling rate.
To formalize the notion, let horse X ∈{1, 2, . . . , m} win the race with
probability p(x) and pay odds of o(x) for 1. Let (X, Y) have joint
probability mass function p(x, y). Let b(x|y) ≥0, 
x b(x|y) = 1 be an
arbitrary conditional betting strategy depending on the side information


## PDF page 191

6.2
GAMBLING AND SIDE INFORMATION
165
Y, where b(x|y) is the proportion of wealth bet on horse x when y is
observed. As before, let b(x) ≥0,  b(x) = 1 denote the unconditional
betting scheme.
Let the unconditional and the conditional doubling rates be
W ∗(X) = max
b(x)

x
p(x) log b(x)o(x),
(6.22)
W ∗(X|Y) = max
b(x|y)

x,y
p(x, y) log b(x|y)o(x)
(6.23)
and let
W = W ∗(X|Y) −W ∗(X).
(6.24)
We observe that for (Xi, Yi) i.i.d. horse races, wealth grows like 2nW ∗(X|Y)
with side information and like 2nW ∗(X) without side information.
Theorem 6.2.1
The increase W in doubling rate due to side infor-
mation Y for a horse race X is
W = I (X; Y).
(6.25)
Proof:
With side information, the maximum value of W ∗(X|Y) with
side information Y is achieved by conditionally proportional gambling
[i.e., b∗(x|y) = p(x|y)]. Thus,
W ∗(X|Y) = max
b(x|y) E

log S

= max
b(x|y)

p(x, y) log o(x)b(x|y)
(6.26)
=

p(x, y) log o(x)p(x|y)
(6.27)
=

p(x) log o(x) −H(X|Y).
(6.28)
Without side information, the optimal doubling rate is
W ∗(X) =

p(x) log o(x) −H(X).
(6.29)
Thus, the increase in doubling rate due to the presence of side information
Y is
W = W ∗(X|Y) −W ∗(X) = H(X) −H(X|Y) = I (X; Y).
□(6.30)


## PDF page 192

166
GAMBLING AND DATA COMPRESSION
Hence, the increase in doubling rate is equal to the mutual informa-
tion between the side information and the horse race. Not surprisingly,
independent side information does not increase the doubling rate.
This relationship can also be extended to the general stock market
(Chapter 16). In this case, however, one can only show the inequality
W ≤I, with equality if and only if the market is a horse race.
6.3
DEPENDENT HORSE RACES AND ENTROPY RATE
The most common example of side information for a horse race is the
past performance of the horses. If the horse races are independent, this
information will be useless. If we assume that there is dependence among
the races, we can calculate the effective doubling rate if we are allowed
to use the results of previous races to determine the strategy for the next
race.
Suppose that the sequence {Xk} of horse race outcomes forms a stochas-
tic process. Let the strategy for each race depend on the results of previous
races. In this case, the optimal doubling rate for uniform fair odds is
W ∗(Xk|Xk−1, Xk−2, . . . , X1)
= E

max
b(·|Xk−1,Xk−2,...,X1) E[log S(Xk)|Xk−1, Xk−2, . . . , X1]
	
= log m −H(Xk|Xk−1, Xk−2, . . . , X1),
(6.31)
which is achieved by b∗(xk|xk−1, . . . , x1) = p(xk|xk−1, . . . , x1).
At the end of n races, the gambler’s wealth is
Sn =
n

i=1
S(Xi),
(6.32)
and the exponent in the growth rate (assuming m for 1 odds) is
1
nE log Sn = 1
n

E log S(Xi)
(6.33)
= 1
n

(log m −H(Xi|Xi−1, Xi−2, . . . , X1))
(6.34)
= log m −H(X1, X2, . . . , Xn)
n
.
(6.35)


