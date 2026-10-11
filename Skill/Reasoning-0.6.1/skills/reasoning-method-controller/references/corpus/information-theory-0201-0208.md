# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 201

SUMMARY
175
= log 27 + 1
n

xn
p(xn) log b(xn)
(6.46)
= log 27 −1
n

xn
p(xn) log p(xn)
b(xn)
+ 1
n

xn
p(xn) log p(xn)
(6.47)
= log 27 −1
nD(p(xn)||b(xn)) −1
nH(X1, X2, . . . , Xn)
(6.48)
≤log 27 −1
nH(X1, X2, . . . , Xn)
(6.49)
≤log 27 −H(X),
(6.50)
where H(X) is the entropy rate of English. Thus, log 27 −E 1
n log Sn
is an upper bound on the entropy rate of English. The upper bound
estimate, ˆH(X) = log 27 −1
n log Sn, converges to H(X) with prob-
ability 1 if English is ergodic and the gambler uses b(xn) = p(xn).
An experiment [131] with 12 subjects and a sample of 75 letters
from the book Jefferson the Virginian by Dumas Malone (Little,
Brown, Boston, 1948; the source used by Shannon) resulted in an
estimate of 1.34 bits per letter for the entropy of English.
SUMMARY
Doubling rate. W(b, p) = E(log S(X)) = m
k=1 pk log bkok.
Optimal doubling rate. W ∗(p) = maxb W(b, p).
Proportional gambling is log-optimal
W ∗(p) = max
b
W(b, p) =

pi log oi −H(p)
(6.51)
is achieved by b∗= p.
Growth rate. Wealth grows as Sn
.=2nW ∗(p).


## PDF page 202

176
GAMBLING AND DATA COMPRESSION
Conservation law. For uniform fair odds,
H(p) + W ∗(p) = log m.
(6.52)
Side information. In a horse race X, the increase W in doubling
rate due to side information Y is
W = I (X; Y).
(6.53)
PROBLEMS
6.1
Horse race.
Three horses run a race. A gambler offers 3-for-
1 odds on each horse. These are fair odds under the assumption
that all horses are equally likely to win the race. The true win
probabilities are known to be
p = (p1, p2, p3) =
1
2, 1
4, 1
4

.
(6.54)
Let b = (b1, b2, b3), bi ≥0,  bi = 1, be the amount invested on
each of the horses. The expected log wealth is thus
W(b) =
3

i=1
pi log 3bi.
(6.55)
(a) Maximize this over b to ﬁnd b∗and W ∗. Thus, the wealth
achieved in repeated horse races should grow to inﬁnity like
2nW ∗with probability 1.
(b) Show that if instead we put all of our money on horse 1, the
most likely winner, we will eventually go broke with probabil-
ity 1.
6.2
Horse race with subfair odds.
If the odds are bad (due to a track
take), the gambler may wish to keep money in his pocket. Let b(0)
be the amount in his pocket and let b(1), b(2), . . . , b(m) be the
amount bet on horses 1, 2, . . . , m, with odds o(1), o(2), . . . , o(m),
and win probabilities p(1), p(2), . . . , p(m). Thus, the resulting
wealth is S(x) = b(0) + b(x)o(x), with probability p(x), x =
1, 2, . . . , m.
(a) Find b∗maximizing E log S if  1/o(i) < 1.


## PDF page 203

PROBLEMS
177
(b) Discuss b∗if  1/o(i) > 1. (There isn’t an easy closed-form
solution in this case, but a “water-ﬁlling” solution results from
the application of the Kuhn–Tucker conditions.)
6.3
Cards.
An ordinary deck of cards containing 26 red cards and
26 black cards is shufﬂed and dealt out one card at time without
replacement. Let Xi be the color of the ith card.
(a) Determine H(X1).
(b) Determine H(X2).
(c) Does H(Xk | X1, X2, . . . , Xk−1) increase or decrease?
(d) Determine H(X1, X2, . . . , X52).
6.4
Gambling.
Suppose that one gambles sequentially on the card
outcomes in Problem 6.6.3. Even odds of 2-for-1 are paid. Thus,
the wealth Sn at time n is Sn = 2nb(x1, x2, . . . , xn), where
b(x1, x2, . . . , xn) is the proportion of wealth bet on x1, x2, . . . , xn.
Find maxb(·) E log S52.
6.5
Beating the public odds.
Consider a three-horse race with win
probabilities
(p1, p2, p3) =
1
2, 1
4, 1
4

and fair odds with respect to the (false) distribution
(r1, r2, r3) =
1
4, 1
4, 1
2

.
Thus, the odds are
(o1, o2, o3) = (4, 4, 2).
(a) What is the entropy of the race?
(b) Find the set of bets (b1, b2, b3) such that the compounded
wealth in repeated plays will grow to inﬁnity.
6.6
Horse race.
A three-horse race has win probabilities p =
(p1, p2, p3), and odds o = (1, 1, 1). The gambler places bets b =
(b1, b2, b3), bi ≥0,  bi = 1, where bi denotes the proportion on
wealth bet on horse i. These odds are very bad. The gambler gets
his money back on the winning horse and loses the other bets.
Thus, the wealth Sn at time n resulting from independent gambles
goes exponentially to zero.
(a) Find the exponent.


## PDF page 204

178
GAMBLING AND DATA COMPRESSION
(b) Find the optimal gambling scheme b (i.e., the bet b∗that max-
imizes the exponent).
(c) Assuming that b is chosen as in part (b), what distribution p
causes Sn to go to zero at the fastest rate?
6.7
Horse race.
Consider a horse race with four horses. Assume that
each horse pays 4-for-1 if it wins. Let the probabilities of win-
ning of the horses be {1
2, 1
4, 1
8, 1
8}. If you started with $100 and
bet optimally to maximize your long-term growth rate, what are
your optimal bets on each horse? Approximately how much money
would you have after 20 races with this strategy?
6.8
Lotto.
The following analysis is a crude approximation to the
games of Lotto conducted by various states. Assume that the player
of the game is required to pay $1 to play and is asked to choose
one number from a range 1 to 8. At the end of every day, the state
lottery commission picks a number uniformly over the same range.
The jackpot (i.e., all the money collected that day) is split among
all the people who chose the same number as the one chosen by the
state. For example, if 100 people played today, 10 of them chose
the number 2, and the drawing at the end of the day picked 2, the
$100 collected is split among the 10 people (i.e., each person who
picked 2 will receive $10, and the others will receive nothing).
The
general
population
does
not
choose
numbers
uni-
formly—numbers such as 3 and 7 are supposedly lucky and are
more popular than 4 or 8. Assume that the fraction of people choos-
ing the various numbers 1, 2, . . . , 8 is (f1, f2, . . . , f8), and assume
that n people play every day. Also assume that n is very large, so
that any single person’s choice does not change the proportion of
people betting on any number.
(a) What is the optimal strategy to divide your money among
the various possible tickets so as to maximize your long-term
growth rate? (Ignore the fact that you cannot buy fractional
tickets.)
(b) What is the optimal growth rate that you can achieve in this
game?
(c) If (f1, f2, . . . , f8) = ( 1
8, 1
8, 1
4, 1
16, 1
16, 1
16, 1
4, 1
16), and you start
with $1, how long will it be before you become a millionaire?
6.9
Horse race.
Suppose that one is interested in maximizing the
doubling rate for a horse race. Let p1, p2, . . . , pm denote the win
probabilities of the m horses. When do the odds (o1, o2, . . . , om)
yield a higher doubling rate than the odds (o′
1, o′
2, . . . , o′
m)?


## PDF page 205

PROBLEMS
179
6.10
Horse race with probability estimates.
(a) Three horses race. Their probabilities of winning are ( 1
2, 1
4, 1
4).
The odds are 4-for-1, 3-for-1, and 3-for-1. Let W ∗be the opti-
mal doubling rate. Suppose you believe that the probabilities
are (1
4, 1
2, 1
4). If you try to maximize the doubling rate, what
doubling rate W will you achieve? By how much has your dou-
bling rate decrease due to your poor estimate of the probabilities
(i.e., what is W = W ∗−W)?
(b) Now let the horse race be among m horses, with probabil-
ities p = (p1, p2, . . . , pm) and odds o = (o1, o2, . . . , om). If
you believe the true probabilities to be q = (q1, q2, . . . , qm),
and try to maximize the doubling rate W, what is W ∗−W?
6.11
Two-envelope problem.
One envelope contains b dollars, the other
2b dollars. The amount b is unknown. An envelope is selected at
random. Let X be the amount observed in this envelope, and let Y
be the amount in the other envelope. Adopt the strategy of switch-
ing to the other envelope with probability p(x), where p(x) =
e−x
(e−x+ex). Let Z be the amount that the player receives. Thus,
(X, Y) =

(b, 2b)
with probability 1
2
(2b, b)
with probability 1
2
(6.56)
Z =
 X
with probability 1 −p(x)
Y
with probability p(x).
(6.57)
(a) Show that E(X) = E(Y) = 3b
2 .
(b) Show that E(Y/X) = 5
4. Since the expected ratio of the
amount in the other envelope is 5
4, it seems that one should
always switch. (This is the origin of the switching paradox.)
However, observe that E(Y) ̸= E(X)E(Y/X). Thus, although
E(Y/X) > 1, it does not follow that E(Y) > E(X).
(c) Let J be the index of the envelope containing the maximum
amount of money, and let J ′ be the index of the envelope
chosen by the algorithm. Show that for any b, I (J; J ′) > 0.
Thus, the amount in the ﬁrst envelope always contains some
information about which envelope to choose.
(d) Show that E(Z) > E(X). Thus, you can do better than always
staying or always switching. In fact, this is true for any mono-
tonic decreasing switching function p(x). By randomly switch-
ing according to p(x), you are more likely to trade up than to
trade down.


## PDF page 206

180
GAMBLING AND DATA COMPRESSION
6.12
Gambling.
Find the horse win probabilities p1, p2, . . . , pm:
(a) Maximizing the doubling rate W ∗for given ﬁxed known odds
o1, o2, . . . , om.
(b) Minimizing the doubling rate for given ﬁxed odds o1, o2, . . . ,
om.
6.13
Dutch book.
Consider a horse race with m = 2 horses,
X = 1, 2
p = 1
2,
1
2
odds (for one) = 10, 30
bets = b, 1 −b.
The odds are superfair.
(a) There is a bet b that guarantees the same payoff regardless of
which horse wins. Such a bet is called a Dutch book. Find this
b and the associated wealth factor S(X).
(b) What is the maximum growth rate of the wealth for the optimal
choice of b? Compare it to the growth rate for the Dutch book.
6.14
Horse race.
Suppose that one is interested in maximizing the
doubling rate for a horse race. Let p1, p2, . . . , pm denote the win
probabilities of the m horses. When do the odds (o1, o2, . . . , om)
yield a higher doubling rate than the odds (o′
1, o′
2, . . . , o′
m)?
6.15
Entropy of a fair horse race.
Let X ∼p(x), x = 1, 2, . . . , m,
denote the winner of a horse race. Suppose that the odds o(x)
are fair with respect to p(x) [i.e., o(x) =
1
p(x)]. Let b(x) be the
amount bet on horse x, b(x) ≥0, m
1 b(x) = 1. Then the resulting
wealth factor is S(x) = b(x)o(x), with probability p(x).
(a) Find the expected wealth ES(X).
(b) Find W ∗, the optimal growth rate of wealth.
(c) Suppose that
Y =

1,
X = 1 or 2
0,
otherwise.
If this side information is available before the bet, how much
does it increase the growth rate W ∗?
(d) Find I (X; Y).


## PDF page 207

PROBLEMS
181
6.16
Negative horse race.
Consider a horse race with m horses with
win probabilities p1, p2, . . . , pm. Here the gambler hopes that a
given horse will lose. He places bets (b1, b2, . . . , bm), m
i=1 bi = 1,
on the horses, loses his bet bi if horse i wins, and retains the rest of
his bets. (No odds.) Thus, S = 
j̸=i bj, with probability pi, and
one wishes to maximize  pi ln(1 −bi) subject to the constraint
 bi = 1.
(a) Find the growth rate optimal investment strategy b∗. Do not
constrain the bets to be positive, but do constrain the bets to
sum to 1. (This effectively allows short selling and margin.)
(b) What is the optimal growth rate?
6.17
St. Petersburg paradox.
Many years ago in ancient St. Petersburg
the following gambling proposition caused great consternation. For
an entry fee of c units, a gambler receives a payoff of 2k units with
probability 2−k, k = 1, 2, . . . .
(a) Show that the expected payoff for this game is inﬁnite. For this
reason, it was argued that c = ∞was a “fair” price to pay to
play this game. Most people ﬁnd this answer absurd.
(b) Suppose that the gambler can buy a share of the game. For
example, if he invests c/2 units in the game, he receives 1
2 a
share and a return X/2, where Pr(X = 2k) = 2−k, k = 1, 2, . . . .
Suppose that X1, X2, . . . are i.i.d. according to this distribution
and that the gambler reinvests all his wealth each time. Thus,
his wealth Sn at time n is given by
Sn =
n

i=1
Xi
c .
(6.58)
Show that this limit is ∞or 0, with probability 1, accordingly
as c < c∗or c > c∗. Identify the “fair” entry fee c∗.
More realistically, the gambler should be allowed to keep a pro-
portion b = 1 −b of his money in his pocket and invest the rest
in the St. Petersburg game. His wealth at time n is then
Sn =
n

i=1

b + bXi
c

.
(6.59)
Let
W(b, c) =
∞

k=1
2−k log

1 −b + b2k
c

.
(6.60)


## PDF page 208

182
GAMBLING AND DATA COMPRESSION
We have
Sn
.= 2nW(b,c).
(6.61)
Let
W ∗(c) = max
0≤b≤1 W(b, c).
(6.62)
Here are some questions about W ∗(c).
(a) For what value of the entry fee c does the optimizing value b∗
drop below 1?
(b) How does b∗vary with c?
(c) How does W ∗(c) fall off with c?
Note that since W ∗(c) > 0, for all c, we can conclude that any
entry fee c is fair.
6.18
Super St. Petersburg.
Finally, we have the super St. Peters-
burg paradox, where Pr(X = 22k) = 2−k, k = 1, 2, . . . . Here the
expected log wealth is inﬁnite for all b > 0, for all c, and the
gambler’s wealth grows to inﬁnity faster than exponentially for
any b > 0. But that doesn’t mean that all investment ratios b are
equally good. To see this, we wish to maximize the relative growth
rate with respect to some other portfolio, say, b = ( 1
2, 1
2). Show
that there exists a unique b maximizing
E ln b + bX/c
1
2 + 1
2X/c
and interpret the answer.
HISTORICAL NOTES
The original treatment of gambling on a horse race is due to Kelly [308],
who found that W = I. Log-optimal portfolios go back to the work
of Bernoulli, Kelly [308], Latan´e [346], and Latan´e and Tuttle [347].
Proportional gambling is sometimes referred to as the Kelly gambling
scheme. The improvement in the probability of winning by switching
envelopes in Problem 6.11 is based on Cover [130].
Shannon studied stochastic models for English in his original paper
[472]. His guessing game for estimating the entropy rate of English is
described in [482]. Cover and King [131] provide a gambling estimate
for the entropy of English. The analysis of the St. Petersburg paradox
is from Bell and Cover [39]. An alternative analysis can be found in
Feller [208].


