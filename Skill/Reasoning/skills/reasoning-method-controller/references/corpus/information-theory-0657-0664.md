# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 657

16.7
UNIVERSAL PORTFOLIOS
631
the game. Later we describe some horizon-free results that have the same
worst-case asymptotic performance as that of the ﬁnite-horizon game.
16.7.1
Finite-Horizon Universal Portfolios
We begin by analyzing a stock market of n periods, where n is known
in advance, and attempt to ﬁnd a portfolio strategy that does well against
all possible sequences of n stock market vectors. The main result can be
stated in the following theorem.
Theorem 16.7.1
For a stock market sequence xn = x1, . . . , xn, xi ∈
Rm
+ of length n with m assets, let S∗
n(xn) be the wealth achieved by the
optimal constantly rebalanced portfolio on xn, and let ˆSn(xn) be the wealth
achieved by any causal portfolio strategy ˆbi(·) on xn; then
max
ˆbi(·)
min
x1,...,xn
ˆSn(xn)
S∗n(xn) = Vn,
(16.94)
where
Vn =


n1+···+nm=n

n
n1, n2, . . . , nm

2−nH( n1
n ,..., nm
n )
−1
.
(16.95)
Using Stirling’s approximation, we can show that Vn is on the order
of n−m−1
2 , and therefore the growth rate for the universal portfolio on
the worst sequence differs from the growth rate of the best constantly
rebalanced portfolio on that sequence by at most a polynomial factor.
The logarithm of the ratio of growth of wealth of the universal portfolio
ˆb to the growth of wealth of the best constant portfolio behaves like
the redundancy of a universal source code. (See Shtarkov [496], where
log Vn appears as the minimax individual sequence redundancy in data
compression.)
We ﬁrst illustrate the main results by means of an example for n = 1.
Consider the case of two stocks and a single day. Let the stock vector for
the day be x = (x1, x2). If x1 > x2, the best portfolio is one that puts all
its money on stock 1, and if x2 > x1, the best portfolio puts all its money
on stock 2. (If x1 = x2, all portfolios are equivalent.)
Now assume that we must choose a portfolio in advance and our oppo-
nent can choose the stock market sequence after we have chosen our
portfolio to make us do as badly as possible relative to the best portfolio.
Given our portfolio, the opponent can ensure that we do as badly as pos-
sible by making the stock on which we have put more weight equal to 0
and the other stock equal to 1. Our best strategy is therefore to put equal


## PDF page 658

632
INFORMATION THEORY AND PORTFOLIO THEORY
weight on both stocks, and with this, we will achieve a growth factor at
least equal to half the growth factor of the best stock, and hence we will
achieve at least half the gain of the best constantly rebalanced portfolio.
It is not hard to calculate that Vn = 2 when n = 1 and m = 2 in equation
(16.94).
However, this result seems misleading, since it appears to suggest that
for n days, we would use a constant uniform portfolio, putting half our
money on each stock every day. If our opponent then chose the stock
sequence so that only the ﬁrst stock was 1 (and the other was 0) every
day, this uniform strategy would achieve a wealth of 1/2n, and we would
achieve a wealth only within a factor of 2n of the best constant portfolio,
which puts all the money on the ﬁrst stock for all time.
The result of the theorem shows that we can do signiﬁcantly better.
The main part of the argument is to reduce a sequence of stock vectors to
the extreme cases where only one of the stocks is nonzero for each day.
If we can ensure that we do well on such sequences, we can guarantee
that we do well on any sequence of stock vectors, and achieve the bounds
of the theorem.
Before we prove the theorem, we need the following lemma.
Lemma 16.7.1
For p1, p2, . . . , pm ≥0 and q1, q2, . . . , qm ≥0,
m
i=1 pi
m
i=1 qi
≥min
i
pi
qi
.
(16.96)
Proof:
Let I denote the index i that minimizes the right-hand side in
(16.96). Assume that pI > 0 (if pI = 0, the lemma is trivially true). Also,
if qI = 0, both sides of (16.96) are inﬁnite (all the other qi’s must also
be zero), and again the inequality holds. Therefore, we can also assume
that qI > 0. Then
m
i=1 pi
m
i=1 qi
= pI
qI
1 + 
i̸=I(pi/pI)
1 + 
i̸=I(qi/qI) ≥pI
qI
(16.97)
because
pi
qi
≥pI
qI
−→pi
pI
≥qi
qI
(16.98)
for all i.
□
First consider the case when n = 1. The wealth at the end of the ﬁrst
day is
ˆS1(x) = ˆbtx,
(16.99)
S1(x) = btx
(16.100)


## PDF page 659

16.7
UNIVERSAL PORTFOLIOS
633
and
ˆS1(x)
S1(x) =
 ˆbixi
 bixi
≥min
 ˆbi
bi

.
(16.101)
We wish to ﬁnd maxˆb minb,x
ˆbtx
btx. Nature should choose x = ei, where ei is
the ith basis vector with 1 in the component i that minimizes
ˆbi
b∗
i , and the
investor should choose ˆb to maximize this minimum. This is achieved by
choosing ˆb = ( 1
m, 1
m, . . . , 1
m).
The important point to realize is that
ˆSn(xn)
Sn(xn) =

n
i=1 ˆbt
ixi

n
i=1 bt
ixi
(16.102)
can also be rewritten in the form of a ratio of terms
ˆSn(xn)
Sn(xn) =
ˆbtx′
btx′ ,
(16.103)
where ˆb, b, x′ ∈Rmn
+ . Here the mn components of the constantly rebal-
anced portfolios b are all of the product form bn1
1 bn2
2 · · · bnm
m . One wishes
to ﬁnd a universal ˆb that is uniformly close to the b’s corresponding to
constantly rebalanced portfolios.
We can now prove the main theorem (Theorem 16.7.1).
Proof of Theorem 16.7.1:
We will prove the theorem for m = 2. The
proof extends in a straightforward fashion to the case m > 2. Denote the
stocks by 1 and 2. The key idea is to express the wealth at time n,
Sn(xn) =
n

i=1
bt
ixi,
(16.104)
which is a product of sums, into a sum of products. Each term in the sum
corresponds to a sequence of stock price relatives for stock 1 or stock
2 times the proportion bi1 or bi2 that the strategy places on stock 1 or
stock 2 at time i. We can therefore view the wealth Sn as a sum over
all 2n possible n-sequences of 1’s and 2’s of the product of the portfolio
proportions times the stock price relatives:
Sn(xn) =

jn∈{1,2}n
n

i=1
bijixiji =

jn∈{1,2}n
n

i=1
biji
n

i=1
xiji.
(16.105)


## PDF page 660

634
INFORMATION THEORY AND PORTFOLIO THEORY
If we let w(j n) denote the product 
n
i=1 biji, the total fraction of wealth
invested in the sequence j n, and let
x(j n) =
n

i=1
xiji
(16.106)
be the corresponding return for this sequence, we can write
Sn(xn) =

jn∈{1,2}n
w(j n)x(j n).
(16.107)
Similar expressions apply to both the best constantly rebalanced portfolio
and the universal portfolio strategy. Thus, we have
ˆSn(xn)
S∗n(xn) =

jn∈{1,2}n ˆw(j n)x(j n)

jn∈{1,2}n w∗(j n)x(j n),
(16.108)
where ˆwn is the amount of wealth placed on the sequence j n by the
universal nonanticipating strategy, and w∗(j n) is the amount placed by the
best constant rebalanced portfolio strategy. Now applying Lemma 16.7.1,
we have
ˆSn(xn)
S∗n(xn) ≥min
jn
ˆw(j n)x(j n)
w∗(j n)x(j n) = min
jn
ˆw(j n)
w∗(j n).
(16.109)
Thus, the problem of maximizing the performance ratio ˆSn/S∗
n is reduced
to ensuring that the proportion of money bet on a sequence of stocks by
the universal portfolio is uniformly close to the proportion bet by b∗. As
might be obvious by now, this formulation of Sn reduces the n-period
stock market to a special case of a single-period stock market—there are
2n stocks, one invests w(j n) in stock j n and receives a return x(j n) for
stock j n, and the total wealth Sn is 
jn w(j n)x(j n).
We ﬁrst calculate the weight w∗(j n) associated with the best constant
rebalanced portfolio b∗. We observe that a constantly rebalanced portfolio
b results in
w(j n) =
n

i=1
biji = bk(1 −b)n−k,
(16.110)
where k is the number of times 1 appears in the sequence j n. Thus, w(j n)
depends only on k, the number of 1’s in j n. Fixing attention on j n, we


## PDF page 661

16.7
UNIVERSAL PORTFOLIOS
635
ﬁnd by differentiating with respect to b that the maximum value
w∗(j n) = max
0≤b≤1 bk(1 −b)n−k
(16.111)
=
k
n
k n −k
n
n−k
,
(16.112)
which is achieved by
b∗=
k
n, n −k
n

.
(16.113)
Note that  w∗(j n) > 1, reﬂecting the fact that the amount “bet” on
j n is chosen in hindsight, thus relieving the hindsight investor of the
responsibility of allocating his investments w∗(j n) to sum to 1. The causal
investor has no such luxury. How can the causal investor choose initial
investments ˆw(j n),  ˆw(j n) = 1, to protect himself from all possible j n
and hindsight-determined w∗(j n)? The answer will be to choose ˆw(j n)
proportional to w∗(j n). Then the worst-case ratio of ˆw(j n)/w∗(j n) will
be maximized. To proceed, we deﬁne Vn by
1
Vn
=

jn
k(j n)
n
k(jn) n −k(j n)
n
n−k(jn)
(16.114)
=
n

k=0
n
k
 k
n
k n −k
n
n−k
(16.115)
and let
ˆw(j n) = Vn
k(j n)
n
k(jn) n −k(j n)
n
n−k(jn)
.
(16.116)
It is clear that ˆw(j n) is a legitimate distribution of wealth over the 2n
stock sequences (i.e., ˆw(j n) ≥0 and 
jn ˆw(j n) = 1). Here Vn is the
normalization factor that makes ˆw(j n) a probability mass function. Also,
from (16.109) and (16.113), for all sequences xn,
ˆSn(xn)
S∗n(xn) ≥min
jn
ˆw(j n)
w∗(j n)
(16.117)
= min
k
Vn( k
n)k( n−k
n )n−k
b∗k(1 −b∗)n−k
(16.118)
≥Vn,
(16.119)


## PDF page 662

636
INFORMATION THEORY AND PORTFOLIO THEORY
where (16.117) follows from (16.109) and (16.119) follows from (16.112).
Consequently, we have
max
ˆb
min
xn
ˆSn(xn)
S∗n(xn) ≥Vn.
(16.120)
We have thus demonstrated a portfolio on the 2n possible sequences of
length n that achieves wealth ˆSn(xn) within a factor Vn of the wealth
S∗
n(xn) achieved by the best constant rebalanced portfolio in hindsight. To
complete the proof of the theorem, we show that this is the best possible,
that is, that any nonanticipating portfolio bi(xi−1) cannot do better than
a factor Vn in the worst case (i.e., for the worst choice of xn). To prove
this, we construct a set of extremal stock market sequences and show that
the performance of any nonanticipating portfolio strategy is bounded by
Vn for at least one of these sequences, proving the worst-case bound.
For each j n ∈{1, 2}n, we deﬁne the corresponding extremal stock mar-
ket vector xn(j n) as
xi(ji) =

(1, 0)t
if ji = 1,
(0, 1)t
if ji = 2,
(16.121)
Let e1 = (1, 0)t, e2 = (0, 1)t be standard basis vectors. Let
K = {x(j n) : j n ∈{1, 2}n, xiji = eji}
(16.122)
be the set of extremal sequences. There are 2n such extremal sequences,
and for each sequence at each time, there is only one stock that yields
a nonzero return. The wealth invested in the other stock is lost. There-
fore, the wealth at the end of n periods for extremal sequence xn(j n)
is the product of the amounts invested in the stocks j1, j2, . . . , jn, [i.e.,
Sn(xn(j n)) = 
i bji = w(j n)]. Again, we can view this as an investment
on sequences of length n, and given the 0–1 nature of the return, it is
easy to see for xn ∈K that

jn
Sn(xn(j n)) = 1.
(16.123)
For any extremal sequence xn(j n) ∈K, the best constant rebalanced port-
folio is
b∗(xn(j n)) =
n1(j n)
n
,
n2(j n)
n
t
,
(16.124)


## PDF page 663

16.7
UNIVERSAL PORTFOLIOS
637
where n1(j n) is the number of occurrences of 1 in the sequence j n. The
corresponding wealth at the end of n periods is
S∗
n(xn(j n)) =
n1(j n)
n
n1(jn) n2(j n)
n
n2(jn)
= ˆw(j n)
Vn
,
(16.125)
from (16.116) and it therefore follows that

xn∈K
S∗
n(xn) = 1
Vn

jn
ˆw(j n) = 1
Vn
.
(16.126)
We then have the following inequality for any portfolio sequence {bi}n
i=1,
with Sn(xn) deﬁned as in (16.104):
min
xn∈K
Sn(xn)
S∗n(xn) ≤

˜xn∈K
S∗
n(˜xn)

xn∈K S∗n(xn)
Sn(˜xn)
S∗n(˜xn)
(16.127)
=

˜xn∈K
Sn(˜xn)

xn∈K S∗n(xn)
(16.128)
=
1

xn∈K S∗n(xn)
(16.129)
= Vn,
(16.130)
where the inequality follows from the fact that the minimum is less than
the average. Thus,
max
b
min
xn∈K
Sn(xn)
S∗n(xn) ≤Vn.
□
(16.131)
The strategy described in the theorem puts mass on all sequences of
length n and is clearly dependent on n. We can recast the strategy in
incremental terms (i.e., in terms of the amount bet on stock 1 and stock
2 at time 1), then, conditional on the outcome at time 1, the amount bet
on each of the two stocks at time 2, and so on. Consider the weight
ˆbi,1 assigned by the algorithm to stock 1 at time i given the previous
sequence of stock vectors xi−1. We can calculate this by summing over
all sequences j n that have a 1 in position i, giving
ˆbi,1(xi−1) =

ji−1∈Mi−1 ˆw(j i−11)x(j i−1)

ji∈Mi ˆw(j i)x(j i−1)
,
(16.132)


## PDF page 664

638
INFORMATION THEORY AND PORTFOLIO THEORY
where
ˆw(j i) =

jn:ji⊆jn
w(j n)
(16.133)
is the weight put on all sequences j n that start with j i, and
x(j i−1) =
i−1

k=1
xkjk
(16.134)
is the return on those sequences as deﬁned in (16.106).
Investigation of the asymptotics of Vn reveals [401, 496] that
Vn ∼

2
n
m−1
(m/2)/√π
(16.135)
for m assets. In particular, for m = 2 assets,
Vn ∼

2
πn
(16.136)
and
1
2
√
n + 1
≤Vn ≤
2
√
n + 1
(16.137)
for all n [400]. Consequently, for m = 2 stocks, the causal portfolio strat-
egy ˆbi(xi−1) given in (16.132) achieves wealth ˆSn(xn) such that
ˆSn(xn)
S∗n(xn) ≥Vn ≥
1
2
√
n + 1
(16.138)
for all market sequences xn.
16.7.2
Horizon-Free Universal Portfolios
We describe the horizon-free strategy in terms of a weighting of different
portfolio strategies. As described earlier, each constantly rebalanced port-
folio b can be viewed as corresponding to a mutual fund that rebalances
the m assets according to b. Initially, we distribute the wealth among
these funds according to a distribution µ(b), where dµ(b) is the amount
of wealth invested in portfolios in the neighborhood db of the constantly
rebalanced portfolio b.


