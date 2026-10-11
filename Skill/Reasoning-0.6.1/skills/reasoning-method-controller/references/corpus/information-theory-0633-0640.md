# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 633

PROBLEMS
607
(c) If he is speaking to D and S at the joint rate in part (b), can
he also speak to F at some positive rate? If so, what is it? If
not, why not?
15.30
Parallel Gaussian channels from a mobile telephone.
Assume
that a sender X is sending to two ﬁxed base stations. Assume that
the sender sends a signal X that is constrained to have average
power P . Assume that the two base stations receive signals Y1
and Y2, where
Y1 = α1X + Z1
Y2 = α2X + Z2,
where Zi ∼N(0, N1), Z2 ∼N(0, N2), and Z1 and Z2 are inde-
pendent. We will assume the α’s are constant over a transmitted
block.
(a) Assuming that both signals Y1 and Y2 are available at a com-
mon decoder Y = (Y1, Y2), what is the capacity of the channel
from the sender to the common receiver?
(b) If, instead, the two receivers Y1 and Y2 each decode their sig-
nals independently, this becomes a broadcast channel. Let R1
be the rate to base station 1 and R2 be the rate to base station
2. Find the capacity region of this channel.
15.31
Gaussian multiple access.
A group of m users, each with power
P , is using a Gaussian multiple-access channel at capacity, so that
m

i=1
Ri = C
mP
N

,
(15.395)
where C(x) = 1
2 log(1 + x) and N is the receiver noise power. A
new user of power P0 wishes to join in.
(a) At what rate can he send without disturbing the other users?
(b) What should his power P0 be so that the new users’ rate is
equal to the combined communication rate C(mP/N) of all
the other users?
15.32
Converse for deterministic broadcast channel.
A deterministic
broadcast channel is deﬁned by an input X and two outputs, Y1
and Y2, which are functions of the input X. Thus, Y1 = f1(X) and
Y2 = f2(X). Let R1 and R2 be the rates at which information can
be sent to the two receivers. Prove that
R1 ≤H(Y1)
(15.396)


## PDF page 634

608
NETWORK INFORMATION THEORY
R2 ≤H(Y2)
(15.397)
R1 + R2 ≤H(Y1, Y2).
(15.398)
15.33
Multiple-access channel.
Consider the multiple-access channel
Y = X1
+ X2 (mod 4), where X1 ∈{0, 1, 2, 3}, X2 ∈{0, 1}.
(a) Find the capacity region (R1, R2).
(b) What is the maximum throughput R1 + R2?
15.34
Distributed source compression.
Let
Z1 =

1,
p
0,
q,
Z2 =

1,
p
0,
q,
and let U = Z1Z2, V = Z1 + Z2. Assume that Z1 and Z2 are
independent. This induces a joint distribution on (U, V ). Let
(Ui, Vi) be i.i.d. according to this distribution. Sender 1 describes
U n at rate R1, and sender 2 describes V n at rate R2.
(a) Find the Slepian–Wolf rate region for recovering (U n, V n)
at the receiver.
(b) What is the residual uncertainty (conditional entropy) that
the receiver has about (Xn, Y n).
15.35
Multiple-access channel capacity with costs.
The cost of using
symbol x is r(x). The cost of a codeword xn is r(xn) =
1
n
n
i=1 r(xi). A (2nR, n) codebook satisﬁes cost constraint r if
1
n
n
i=1 r(xi(w)) ≤r for all w ∈2nR.
(a) Find an expression for the capacity C(r) of a discrete mem-
oryless channel with cost constraint r.
(b) Find an expression for the multiple-access channel capacity
region for (X1 × X2, p(y|x1, x2), Y) if sender X1 has cost con-
straint r1 and sender X2 has cost constraint r2.
(c) Prove the converse for part (b).
15.36
Slepian–Wolf .
Three cards from a three-card deck are dealt, one
to sender X1, one to sender X2, and one to sender X3. At what
rates do X1, X2, and X3 need to communicate to some receiver
so that their card information can be recovered?


## PDF page 635

HISTORICAL NOTES
609
Decoder
(Xn
1, Xn
2, Xn
3)
i(Xn
1)
k(Xn
3)
j(Xn
2)
Xn
1
Xn
3
Xn
2
^
^
^
Assume that (X1i, X2i, X3i) are drawn i.i.d. from a uniform dis-
tribution over the permutations of {1, 2, 3}.
HISTORICAL NOTES
This chapter is based on the review in El Gamal and Cover [186]. The
two-way channel was studied by Shannon [486] in 1961. He derived inner
and outer bounds on the capacity region. Dueck [175] and Schalkwijk
[464, 465] suggested coding schemes for two-way channels that achieve
rates exceeding Shannon’s inner bound; outer bounds for this channel
were derived by Zhang et al. [596] and Willems and Hekstra [558].
The multiple-access channel capacity region was found by Ahlswede
[7] and Liao [355] and was extended to the case of the multiple-access
channel with common information by Slepian and Wolf [501]. Gaarder
and Wolf [220] were the ﬁrst to show that feedback increases the capac-
ity of a discrete memoryless multiple-access channel. Cover and Leung
[133] proposed an achievable region for the multiple-access channel with
feedback, which was shown to be optimal for a class of multiple-access
channels by Willems [557]. Ozarow [410] has determined the capacity
region for a two-user Gaussian multiple-access channel with feedback.
Cover et al. [129] and Ahlswede and Han [12] have considered the prob-
lem of transmission of a correlated source over a multiple-access channel.
The Slepian–Wolf theorem was proved by Slepian and Wolf [502] and was
extended to jointly ergodic sources by a binning argument in Cover [122].
Superposition coding for broadcast channels was suggested by Cover
in 1972 [119]. The capacity region for the degraded broadcast channel
was determined by Bergmans [55] and Gallager [225]. The superposi-
tion codes for the degraded broadcast channel are also optimal for the
less noisy broadcast channel (K¨orner and Marton [324]), the more capa-
ble broadcast channel (El Gamal [185]), and the broadcast channel with
degraded message sets (K¨orner and Marton [325]). Van der Meulen [526]
and Cover [121] proposed achievable regions for the general broadcast
channel. The capacity of a deterministic broadcast channel was found by
Gelfand and Pinsker [242, 243, 423] and Marton [377]. The best known


## PDF page 636

610
NETWORK INFORMATION THEORY
achievable region for the broadcast channel is due to Marton [377]; a sim-
pler proof of Marton’s region was given by El Gamal and Van der Meulen
[188]. El Gamal [184] showed that feedback does not increase the capac-
ity of a physically degraded broadcast channel. Dueck [176] introduced
an example to illustrate that feedback can increase the capacity of a mem-
oryless broadcast channel; Ozarow and Leung [411] described a coding
procedure for the Gaussian broadcast channel with feedback that increased
the capacity region.
The relay channel was introduced by Van der Meulen [528]; the capac-
ity region for the degraded relay channel was determined by Cover and
El Gamal [127]. Carleial [85] introduced the Gaussian interference chan-
nel with power constraints and showed that very strong interference is
equivalent to no interference at all. Sato and Tanabe [459] extended the
work of Carleial to discrete interference channels with strong interference.
Sato [457] and Benzel [51] dealt with degraded interference channels. The
best known achievable region for the general interference channel is due
to Han and Kobayashi [274]. This region gives the capacity for Gaussian
interference channels with interference parameters greater than 1, as was
shown in Han and Kobayashi [274] and Sato [458]. Carleial [84] proved
new bounds on the capacity region for interference channels.
The problem of coding with side information was introduced by Wyner
and Ziv [573] and Wyner [570]; the achievable region for this problem
was described in Ahlswede and K¨orner [13], Gray and Wyner [261], and
Wyner [571],[572]. The problem of ﬁnding the rate distortion function
with side information was solved by Wyner and Ziv [574]. The channel
capacity counterpart of rate distortion with side information was solved by
Gelfand and Pinsker [243]; the duality between the two results is explored
in Cover and Chiang [113]. The problem of multiple descriptions is treated
in El Gamal and Cover [187].
The special problem of encoding a function of two random variables
was discussed by K¨orner and Marton [326], who described a simple
method to encode the modulo 2 sum of two binary random variables.
A general framework for the description of source networks may be
found in Csisz´ar and K¨orner [148],[149]. A common model that includes
Slepian–Wolf encoding, coding with side information, and rate distor-
tion with side information as special cases was described by Berger and
Yeung [54].
In 1989, Ahlswede and Dueck [17] introduced the problem of identi-
ﬁcation via communication channels, which can be viewed as a problem
where the sender sends information to the receivers but each receiver only
needs to know whether or not a single message was sent. In this case, the
set of possible messages that can be sent reliably is doubly exponential in


## PDF page 637

HISTORICAL NOTES
611
the block length, and the key result of this paper was to show that 22nC
messages could be identiﬁed for any noisy channel with capacity C. This
problem spawned a set of papers [16, 18, 269, 434], including extensions
to channels with feedback and multiuser channels.
Another active area of work has been the analysis of MIMO (multiple-
input multiple-output) systems or space-time coding, which use multiple
antennas at the transmitter and receiver to take advantage of the diversity
gains from multipath for wireless systems. The analysis of these multiple
antenna systems by Foschini [217], Teletar [512], and Rayleigh and Ciofﬁ
[246] show that the capacity gains from the diversity obtained using mul-
tiple antennas in fading environments can be substantial relative to the
single-user capacity achieved by traditional equalization and interleav-
ing techniques. A special issue of the IEEE Transactions in Information
Theory [70] has a number of papers covering different aspects of this
technology.
Comprehensive surveys of network information theory may be found
in El Gamal and Cover [186], Van der Meulen [526–528], Berger [53],
Csisz´ar and K¨orner [149], Verdu [538], Cover [111], and Ephremides and
Hajek [197].


## PDF page 638



## PDF page 639

CHAPTER 16
INFORMATION THEORY
AND PORTFOLIO THEORY
The duality between the growth rate of wealth in the stock market and
the entropy rate of the market is striking. In particular, we shall ﬁnd the
competitively optimal and growth rate optimal portfolio strategies. They
are the same, just as the Shannon code is optimal both competitively and
in the expected description rate. We also ﬁnd the asymptotic growth rate
of wealth for an ergodic stock market process. We end with a discussion
of universal portfolios that enable one to achieve the same asymptotic
growth rate as the best constant rebalanced portfolio in hindsight.
In Section 16.8 we provide a “sandwich” proof of the asymptotic
equipartition property for general ergodic processes that is motivated by
the notion of optimal portfolios for stationary ergodic stock markets.
16.1
THE STOCK MARKET: SOME DEFINITIONS
A stock market is represented as a vector of stocks X = (X1, X2, . . . , Xm),
Xi ≥0, i = 1, 2, . . . , m, where m is the number of stocks and the price
relative Xi is the ratio of the price at the end of the day to the price at the
beginning of the day. So typically, Xi is near 1. For example, Xi = 1.03
means that the ith stock went up 3 percent that day.
Let X ∼F(x), where F(x) is the joint distribution of the vector of
price relatives. A portfolio b = (b1, b2, . . . , bm), bi ≥0,  bi = 1, is an
allocation of wealth across the stocks. Here bi is the fraction of one’s
wealth invested in stock i. If one uses a portfolio b and the stock vector
is X, the wealth relative (ratio of the wealth at the end of the day to the
wealth at the beginning of the day) is S = btX = m
i=1 biXi.
We wish to maximize S in some sense. But S is a random variable,
the distribution of which depends on portfolio b, so there is controversy
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
613


## PDF page 640

614
INFORMATION THEORY AND PORTFOLIO THEORY
Variance
Mean
Risk-free asset
Efficient
frontier
FIGURE 16.1. Sharpe–Markowitz theory: set of achievable mean–variance pairs.
over the choice of the best distribution for S. The standard theory of
stock market investment is based on consideration of the ﬁrst and second
moments of S. The objective is to maximize the expected value of S
subject to a constraint on the variance. Since it is easy to calculate these
moments, the theory is simpler than the theory that deals with the entire
distribution of S.
The mean–variance approach is the basis of the Sharpe–Markowitz
theory of investment in the stock market and is used by business ana-
lysts and others. It is illustrated in Figure 16.1. The ﬁgure illustrates the
set of achievable mean–variance pairs using various portfolios. The set
of portfolios on the boundary of this region corresponds to the undomi-
nated portfolios: These are the portfolios that have the highest mean for
a given variance. This boundary is called the efﬁcient frontier, and if one
is interested only in mean and variance, one should operate along this
boundary.
Normally, the theory is simpliﬁed with the introduction of a risk-free
asset (e.g., cash or Treasury bonds, which provide a ﬁxed interest rate
with zero variance). This stock corresponds to a point on the Y axis
in the ﬁgure. By combining the risk-free asset with various stocks, one
obtains all points below the tangent from the risk-free asset to the efﬁcient
frontier. This line now becomes part of the efﬁcient frontier.
The concept of the efﬁcient frontier also implies that there is a true
price for a stock corresponding to its risk. This theory of stock prices,
called the capital asset pricing model (CAPM), is used to decide whether
the market price for a stock is too high or too low. Looking at the mean
of a random variable gives information about the long-term behavior of


