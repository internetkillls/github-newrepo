# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 449

PROBLEMS
423
12.9
Maximum entropy processes
(a) Find the maximum entropy rate binary stochastic process
{Xi}∞
i=−∞, Xi ∈{0, 1},
satisfying
Pr{Xi = Xi+1} = 1
3
for
all i.
(b) What is the resulting entropy rate?
12.10
Maximum entropy of sums.
Let Y = X1 + X2. Find the maxi-
mum entropy density for Y under the constraint EX2
1 = P1, EX2
2
= P2:
(a) If X1 and X2 are independent.
(b) If X1 and X2 are allowed to be dependent.
(c) Prove part (a).
12.11
Maximum entropy Markov chain.
Let {Xi} be a stationary
Markov chain with Xi ∈{1, 2, 3}. Let I (Xn; Xn+2) = 0 for all n.
(a) What is the maximum entropy rate process satisfying this
constraint?
(b) What if I (Xn; Xn+2) = α for all n for some given value of
α, 0 ≤α ≤log 3?
12.12
Entropy bound on prediction error.
Let {Xn} be an arbitrary real
valued stochastic process. Let ˆXn+1 = E{Xn+1|Xn}. Thus the con-
ditional mean ˆXn+1 is a random variable depending on the n-past
Xn. Here ˆXn+1 is the minimum mean squared error prediction of
Xn+1 given the past.
(a) Find a lower bound on the conditional variance E{E{(Xn+1
−ˆXn+1)2|Xn}} in terms of the conditional differential entropy
h(Xn+1|Xn).
(b) Is equality achieved when {Xn} is a Gaussian stochastic pro-
cess?
12.13
Maximum entropy rate.
What is the maximum entropy rate sto-
chastic process {Xi} over the symbol set {0, 1} for which the
probability that 00 occurs in a sequence is zero?
12.14
Maximum entropy
(a) What is the parametric-form maximum entropy density f (x)
satisfying the two conditions
EX8 = a,
EX16 = b?
(b) What is the maximum entropy density satisfying the condition
E(X8 + X16) = a + b?
(c) Which entropy is higher?


## PDF page 450

424
MAXIMUM ENTROPY
12.15
Maximum entropy.
Find the parametric form of the maximum
entropy density f satisfying the Laplace transform condition

f (x)e−x dx = α,
and give the constraints on the parameter.
12.16
Maximum entropy processes.
Consider the set of all stochastic
processes with {Xi}, Xi ∈R, with
R0 = EX2
i = 1,
R1 = EXiXi+1 = 1
2.
Find the maximum entropy rate.
12.17
Binary maximum entropy.
Consider a binary process {Xi}, Xi ∈
{−1, +1}, with R0 = EX2
i = 1 and R1 = EXiXi+1 = 1
2.
(a) Find the maximum entropy process with these constraints.
(b) What is the entropy rate?
(c) Is there a Bernoulli process satisfying these constraints?
12.18
Maximum entropy.
Maximize h(Z, Vx, Vy, Vz) subject to the en-
ergy constraint E( 1
2m∥V ∥2 + mgZ) = E0. Show that the resulting
distribution yields
E 1
2m∥V ∥2 = 3
5E0,
EmgZ = 2
5E0.
Thus, 2
5 of the energy is stored in the potential ﬁeld, regardless of
its strength g.
12.19
Maximum entropy discrete processes
(a) Find the maximum entropy rate binary stochastic process
{Xi}∞
i=−∞,
Xi ∈{0, 1}, satisfying Pr{Xi = Xi+1} = 1
3 for all
i.
(b) What is the resulting entropy rate?
12.20
Maximum entropy of sums.
Let Y = X1 + X2. Find the maxi-
mum entropy of Y under the constraint EX2
1 = P1, EX2
2 = P2:
(a) If X1 and X2 are independent.
(b) If X1 and X2 are allowed to be dependent.


## PDF page 451

HISTORICAL NOTES
425
12.21
Entropy rate
(a) Find the maximum entropy rate stochastic process {Xi} with
EX2
i = 1, EXiXi+2 = α, i = 1, 2, . . .. Be careful.
(b) What is the maximum entropy rate?
(c) What is EXiXi+1 for this process?
12.22
Minimum expected value
(a) Find the minimum value of EX over all probability density
functions f (x) satisfying the following three constraints:
(i) f (x) = 0 for x ≤0.
(ii)
 ∞
−∞f (x) dx = 1.
(iii) h(f ) = h.
(b) Solve the same problem if (i) is replaced by
(i′) f (x) = 0 for x ≤a.
HISTORICAL NOTES
The maximum entropy principle arose in statistical mechanics in the
nineteenth century and has been advocated for use in a broader con-
text by Jaynes [294]. It was applied to spectral estimation by Burg [80].
The information-theoretic proof of Burg’s theorem is from Choi and
Cover [98].


## PDF page 452



## PDF page 453

CHAPTER 13
UNIVERSAL SOURCE CODING
Here we develop the basics of universal source coding. Minimax regret
data compression is deﬁned, and the descriptive cost of universality is
shown to be the information radius of the relative entropy ball containing
all the source distributions. The minimax theorem shows this radius to
be the channel capacity for the associated channel given by the source
distribution. Arithmetic coding enables the use of a source distribution
that is learned on the ﬂy. Finally, individual sequence compression is
deﬁned and achieved by a succession of Lempel–Ziv parsing algorithms.
In Chapter 5 we introduced the problem of ﬁnding the shortest rep-
resentation of a source, and showed that the entropy is the fundamental
lower limit on the expected length of any uniquely decodable represen-
tation. We also showed that if we know the probability distribution for
the source, we can use the Huffman algorithm to construct the optimal
(minimal expected length) code for that distribution.
For many practical situations, however, the probability distribution
underlying the source may be unknown, and we cannot apply the methods
of Chapter 5 directly. Instead, all we know is a class of distributions. One
possible approach is to wait until we have seen all the data, estimate the
distribution from the data, use this distribution to construct the best code,
and then go back to the beginning and compress the data using this code.
This two-pass procedure is used in some applications where there is a
fairly small amount of data to be compressed. But there are many situa-
tions in which it is not feasible to make two passes over the data, and it
is desirable to have a one-pass (or online) algorithm to compress the data
that “learns” the probability distribution of the data and uses it to com-
press the incoming symbols. We show the existence of such algorithms
that do well for any distribution within a class of distributions.
In yet other cases, there is no probability distribution underlying the
data—all we are given is an individual sequence of outcomes. Examples
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
427


## PDF page 454

428
UNIVERSAL SOURCE CODING
of such data sources include text and music. We can then ask the question:
How well can we compress the sequence? If we do not put any restric-
tions on the class of algorithms, we get a meaningless answer—there
always exists a function that compresses a particular sequence to one
bit while leaving every other sequence uncompressed. This function is
clearly “overﬁtted” to the data. However, if we compare our performance
to that achievable by optimal word assignments with respect to Bernoulli
distributions or kth-order Markov processes, we obtain more interesting
answers that are in many ways analogous to the results for the probabilis-
tic or average case analysis. The ultimate answer for compressibility for
an individual sequence is the Kolmogorov complexity of the sequence,
which we discuss in Chapter 14.
We begin the chapter by considering the problem of source coding as
a game in which the coder chooses a code that attempts to minimize
the average length of the representation and nature chooses a distribution
on the source sequence. We show that this game has a value that is
related to the capacity of a channel with rows of its transition matrix that
are the possible distributions on the source sequence. We then consider
algorithms for encoding the source sequence given a known or “estimated”
distribution on the sequence. In particular, we describe arithmetic coding,
which is an extension of the Shannon–Fano–Elias code of Section 5.9
that permits incremental encoding and decoding of sequences of source
symbols.
We then describe two basic versions of the class of adaptive dictionary
compression algorithms called Lempel–Ziv, based on the papers by Ziv
and Lempel [603, 604]. We provide a proof of asymptotic optimality for
these algorithms, showing that in the limit they achieve the entropy rate
for any stationary ergodic source. In Chapter 16 we extend the notion of
universality to investment in the stock market and describe online portfolio
selection procedures that are analogous to the universal methods for data
compression.
13.1
UNIVERSAL CODES AND CHANNEL CAPACITY
Assume that we have a random variable X drawn according to a dis-
tribution from the family {pθ}, where the parameter θ ∈{1, 2, . . . , m} is
unknown. We wish to ﬁnd an efﬁcient code for this source.
From the results of Chapter 5, if we know θ, we can construct a code
with codeword lengths l(x) = log
1
pθ(x), achieving an average codeword


## PDF page 455

13.1
UNIVERSAL CODES AND CHANNEL CAPACITY
429
length equal to the entropy Hθ(x) = −
x pθ(x) log pθ(x), and this is the
best that we can do. For the purposes of this section, we will ignore the
integer constraints on l(x), knowing that applying the integer constraint
will cost at most one bit in expected length. Thus,
min
l(x) Epθ [l(X)] = Epθ

log
1
pθ(X)

= H(pθ).
(13.1)
What happens if we do not know the true distribution pθ, yet wish to
code as efﬁciently as possible? In this case, using a code with codeword
lengths l(x) and implied probability q(x) = 2−l(x), we deﬁne the redun-
dancy of the code as the difference between the expected length of the
code and the lower limit for the expected length:
R(pθ, q) = Epθ [l(X)] −Epθ

log
1
pθ(X)

(13.2)
=

x
pθ(x)

l(x) −log
1
p(x)

(13.3)
=

x
pθ(x)

log
1
q(x) −log
1
p(x)

(13.4)
=

x
pθ(x) log pθ(x)
q(x)
(13.5)
= D(pθ∥q),
(13.6)
where q(x) = 2−l(x) is the distribution that corresponds to the codeword
lengths l(x).
We wish to ﬁnd a code that does well irrespective of the true distribution
pθ, and thus we deﬁne the minimax redundancy as
R∗= min
q max
pθ R(pθ, q) = min
q max
pθ D(pθ∥q).
(13.7)
This minimax redundancy is achieved by a distribution q that is at the
“center” of the information ball containing the distributions pθ, that is,
the distribution q whose maximum distance from any of the distributions
pθ is minimized (Figure 13.1).
To ﬁnd the distribution q that is as close as possible to all the possible
pθ in relative entropy, consider the following channel:


## PDF page 456

430
UNIVERSAL SOURCE CODING
p1
q*
pm
FIGURE 13.1. Minimum radius information ball containing all the pθ’s
θ →


. . . p1 . . .
. . . p2 . . .
...
. . . pθ . . .
...
. . . pm . . .


→X.
(13.8)
This is a channel {θ, pθ(x), X} with the rows of the transition matrix equal
to the different pθ’s, the possible distributions of the source. We will show
that the minimax redundancy R∗is equal to the capacity of this channel,
and the corresponding optimal coding distribution is the output distribution
of this channel induced by the capacity-achieving input distribution. The
capacity of this channel is given by
C = max
π(θ) I (θ; X) = max
π(θ)

θ
π(θ)pθ(x) log pθ(x)
qπ(x),
(13.9)
where
qπ(x) =

θ
π(θ)pθ(x).
(13.10)
The equivalence of R∗and C is expressed in the following theorem:
Theorem 13.1.1
(Gallager [229], Ryabko [450]) The capacity of a
channel p(x|θ) with rows p1, p2, . . . , pm is given by
C = R∗= min
q max
θ
D(pθ∥q).
(13.11)


