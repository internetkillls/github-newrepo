# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 385

11.3
UNIVERSAL SOURCE CODING
359
By indexing the elements of A, we deﬁne the encoding function fn as
fn(x) =

index of x in A
if x ∈A,
0
otherwise.
(11.83)
The decoding function maps each index onto the corresponding element
of A. Hence all the elements of A are recovered correctly, and all the
remaining sequences result in an error. The set of sequences that are
recovered correctly is illustrated in Figure 11.2.
We now show that this encoding scheme is universal. Assume that the
distribution of X1, X2, . . . , Xn is Q and H(Q) < R. Then the probability
of decoding error is given by
P (n)
e
= 1 −Qn(A)
(11.84)
=

P:H(P)>Rn
Qn(T (P ))
(11.85)
≤(n + 1)|X|
max
P:H(P)>Rn Qn(T (P ))
(11.86)
≤(n + 1)|X|2−n minP :H(P )>Rn D(P||Q).
(11.87)
Since Rn ↑R and H(Q) < R, there exists n0 such that for all n ≥n0,
Rn > H(Q). Then for n ≥n0, minP:H(P)>Rn D(P ||Q) must be greater
than 0, and the probability of error P (n)
e
converges to 0 exponentially fast
as n →∞.
H(P) = R
A
FIGURE 11.2. Universal code and the probability simplex. Each sequence with type that
lies outside the circle is encoded by its index. There are fewer than 2nR such sequences.
Sequences with types within the circle are encoded by 0.


## PDF page 386

360
INFORMATION THEORY AND STATISTICS
Error exponent
H(Q)
Rate of code
FIGURE 11.3. Error exponent for the universal code.
On the other hand, if the distribution Q is such that the entropy H(Q)
is greater than the rate R, then with high probability the sequence will
have a type outside the set A. Hence, in such cases the probability of
error is close to 1.
The exponent in the probability of error is
D∗
R,Q =
min
P:H(P)>R D(P ||Q),
(11.88)
which is illustrated in Figure 11.3.
□
The universal coding scheme described here is only one of many such
schemes. It is universal over the set of i.i.d. distributions. There are other
schemes, such as the Lempel–Ziv algorithm, which is a variable-rate uni-
versal code for all ergodic sources. The Lempel–Ziv algorithm, discussed
in Section 13.4, is often used in practice to compress data that cannot be
modeled simply, such as English text or computer source code.
One may wonder why it is ever necessary to use Huffman codes, which
are speciﬁc to a probability distribution. What do we lose in using a
universal code? Universal codes need a longer block length to obtain
the same performance as a code designed speciﬁcally for the probability
distribution. We pay the penalty for this increase in block length by the
increased complexity of the encoder and decoder. Hence, a distribution
speciﬁc code is best if one knows the distribution of the source.
11.4
LARGE DEVIATION THEORY
The subject of large deviation theory can be illustrated by an example.
What is the probability that 1
n
 Xi is near 1
3 if X1, X2, . . . , Xn are drawn
i.i.d. Bernoulli(1
3)? This is a small deviation (from the expected outcome)


## PDF page 387

11.4
LARGE DEVIATION THEORY
361
and the probability is near 1. Now what is the probability that 1
n
 Xi
is greater than
3
4 given that X1, X2, . . . , Xn are Bernoulli(1
3)? This is
a large deviation, and the probability is exponentially small. We might
estimate the exponent using the central limit theorem, but this is a poor
approximation for more than a few standard deviations. We note that
1
n
 Xi = 3
4 is equivalent to Px = ( 1
4, 3
4). Thus, the probability that Xn is
near 3
4 is the probability that type PX is near (3
4, 1
4). The probability of
this large deviation will turn out to be ≈2−nD(( 3
4, 1
4)||( 1
3, 2
3)). In this section
we estimate the probability of a set of nontypical types.
Let E be a subset of the set of probability mass functions. For example,
E may be the set of probability mass functions with mean µ. With a slight
abuse of notation, we write
Qn(E) = Qn(E ∩Pn) =

x:Px∈E∩Pn
Qn(x).
(11.89)
If E contains a relative entropy neighborhood of Q, then by the weak
law of large numbers (Theorem 11.2.1), Qn(E) →1. On the other hand,
if E does not contain Q or a neighborhood of Q, then by the weak law
of large numbers, Qn(E) →0 exponentially fast. We will use the method
of types to calculate the exponent.
Let us ﬁrst give some examples of the kinds of sets E that we are
considering. For example, assume that by observation we ﬁnd that the
sample average of g(X) is greater than or equal to α [i.e., 1
n

i g(xi) ≥α].
This event is equivalent to the event PX ∈E ∩Pn, where
E =

P :

a∈X
g(a)P (a) ≥α

,
(11.90)
because
1
n
n

i=1
g(xi) ≥α ⇔

a∈X
PX(a)g(a) ≥α
(11.91)
⇔PX ∈E ∩Pn.
(11.92)
Thus,
Pr

1
n
n

i=1
g(Xi) ≥α

= Qn(E ∩Pn) = Qn(E).
(11.93)


## PDF page 388

362
INFORMATION THEORY AND STATISTICS
P*
Q
E
FIGURE 11.4. Probability simplex and Sanov’s theorem.
Here E is a half space in the space of probability vectors, as illustrated
in Figure 11.4.
Theorem 11.4.1
(Sanov’s
theorem)
Let
X1, X2, . . . , Xn
be
i.i.d.
∼Q(x). Let E ⊆P be a set of probability distributions. Then
Qn(E) = Qn(E ∩Pn) ≤(n + 1)|X|2−nD(P ∗||Q),
(11.94)
where
P ∗= arg min
P∈E D(P ||Q)
(11.95)
is the distribution in E that is closest to Q in relative entropy.
If, in addition, the set E is the closure of its interior, then
1
n log Qn(E) →−D(P ∗||Q).
(11.96)
Proof:
We ﬁrst prove the upper bound:
Qn(E) =

P∈E∩Pn
Qn(T (P ))
(11.97)
≤

P∈E∩Pn
2−nD(P||Q)
(11.98)


## PDF page 389

11.4
LARGE DEVIATION THEORY
363
≤

P∈E∩Pn
max
P∈E∩Pn 2−nD(P||Q)
(11.99)
=

P∈E∩Pn
2−n minP ∈E∩Pn D(P||Q)
(11.100)
≤

P∈E∩Pn
2−n minP ∈E D(P||Q)
(11.101)
=

P∈E∩Pn
2−nD(P ∗||Q)
(11.102)
≤(n + 1)|X|2−nD(P ∗||Q),
(11.103)
where the last inequality follows from Theorem 11.1.1. Note that P ∗need
not be a member of Pn. We now come to the lower bound, for which we
need a “nice” set E, so that for all large n, we can ﬁnd a distribution in
E ∩Pn that is close to P ∗. If we now assume that E is the closure of its
interior (thus, the interior must be nonempty), then since ∪nPn is dense
in the set of all distributions, it follows that E ∩Pn is nonempty for all
n ≥n0 for some n0. We can then ﬁnd a sequence of distributions Pn such
that Pn ∈E ∩Pn and D(Pn||Q) →D(P ∗||Q). For each n ≥n0,
Qn(E) =

P∈E∩Pn
Qn(T (P ))
(11.104)
≥Qn(T (Pn))
(11.105)
≥
1
(n + 1)|X| 2−nD(Pn||Q).
(11.106)
Consequently,
lim inf 1
n log Qn(E) ≥lim inf

−|X| log(n + 1)
n
−D(Pn||Q)

= −D(P ∗||Q).
(11.107)
Combining this with the upper bound establishes the theorem.
□
This argument can be extended to continuous distributions using quan-
tization.


## PDF page 390

364
INFORMATION THEORY AND STATISTICS
11.5
EXAMPLES OF SANOV’S THEOREM
Suppose that we wish to ﬁnd Pr{ 1
n
n
i=1 gj(Xi) ≥αj, j = 1, 2, . . . , k}.
Then the set E is deﬁned as
E =

P :

a
P (a)gj(a) ≥αj, j = 1, 2, . . . , k

.
(11.108)
To ﬁnd the closest distribution in E to Q, we minimize D(P ||Q) subject
to the constraints in (11.108). Using Lagrange multipliers, we construct
the functional
J(P ) =

x
P (x) log P (x)
Q(x) +

i
λi

x
P (x)gi(x) + ν

x
P (x).
(11.109)
We then differentiate and calculate the closest distribution to Q to be of
the form
P ∗(x) =
Q(x)e

i λigi(x)

a∈X Q(a)e

i λigi(a),
(11.110)
where the constants λi are chosen to satisfy the constraints. Note that if
Q is uniform, P ∗is the maximum entropy distribution. Veriﬁcation that
P ∗is indeed the minimum follows from the same kinds of arguments as
given in Chapter 12.
Let us consider some speciﬁc examples:
Example 11.5.1
(Dice)
Suppose that we toss a fair die n times; what
is the probability that the average of the throws is greater than or equal
to 4? From Sanov’s theorem, it follows that
Qn(E) .= 2−nD(P ∗||Q),
(11.111)
where P ∗minimizes D(P ||Q) over all distributions P that satisfy
6

i=1
iP (i) ≥4.
(11.112)


## PDF page 391

11.5
EXAMPLES OF SANOV’S THEOREM
365
From (11.110), it follows that P ∗has the form
P ∗(x) =
2λx
6
i=1 2λi ,
(11.113)
with λ chosen so that  iP ∗(i) = 4. Solving numerically, we obtain
λ = 0.2519, P ∗= (0.1031, 0.1227, 0.1461, 0.1740, 0.2072, 0.2468), and
therefore D(P ∗||Q) = 0.0624 bit. Thus, the probability that the average
of 10000 throws is greater than or equal to 4 is ≈2−624.
Example 11.5.2
(Coins)
Suppose that we have a fair coin and want
to estimate the probability of observing more than 700 heads in a series
of 1000 tosses. The problem is like Example 11.5.1. The probability is
P (Xn ≥0.7) .= 2−nD(P ∗||Q),
(11.114)
where P ∗is the (0.7, 0.3) distribution and Q is the (0.5, 0.5) distribution.
In this case, D(P ∗||Q) = 1 −H(P ∗) = 1 −H(0.7) = 0.119. Thus, the
probability of 700 or more heads in 1000 trials is approximately 2−119.
Example 11.5.3
(Mutual dependence)
Let Q(x, y) be a given joint
distribution and let Q0(x, y) = Q(x)Q(y) be the associated product dis-
tribution formed from the marginals of Q. We wish to know the likelihood
that a sample drawn according to Q0 will “appear” to be jointly dis-
tributed according to Q. Accordingly, let (Xi, Yi) be i.i.d. ∼Q0(x, y) =
Q(x)Q(y). We deﬁne joint typicality as we did in Section 7.6; that is,
(xn, yn) is jointly typical with respect to a joint distribution Q(x, y) iff
the sample entropies are close to their true values:
−1
n log Q(xn) −H(X)
 ≤ϵ,
(11.115)
−1
n log Q(yn) −H(Y)
 ≤ϵ,
(11.116)
and
−1
n log Q(xn, yn) −H(X, Y)
 ≤ϵ.
(11.117)
We wish to calculate the probability (under the product distribution) of
seeing a pair (xn, yn) that looks jointly typical
of Q [i.e., (xn, yn)


## PDF page 392

366
INFORMATION THEORY AND STATISTICS
satisﬁes (11.115)–(11.117)]. Thus, (xn, yn) are jointly typical with respect
to Q(x, y) if Pxn,yn ∈E ∩Pn(X, Y), where
E = {P (x, y) :
−

x,y
P (x, y) log Q(x) −H(X)
 ≤ϵ,
−

x,y
P (x, y) log Q(y) −H(Y)
 ≤ϵ,
−

x,y
P (x, y) log Q(x, y) −H(X, Y)
 ≤ϵ}.
(11.118)
Using Sanov’s theorem, the probability is
Qn
0(E)
.= 2−nD(P ∗||Q0),
(11.119)
where P ∗is the distribution satisfying the constraints that is closest to
Q0 in relative entropy. In this case, as ϵ →0, it can be veriﬁed (Prob-
lem 11.10) that P ∗is the joint distribution Q, and Q0 is the product
distribution, so that the probability is 2−nD(Q(x,y)||Q(x)Q(y)) = 2−nI(X;Y),
which is the same as the result derived in Chapter 7 for the joint AEP.
In the next section we consider the empirical distribution of the sequence
of outcomes given that the type is in a particular set of distributions E. We
will show that not only is the probability of the set E essentially determined
by D(P ∗||Q), the distance of the closest element of E to Q, but also that
the conditional type is essentially P ∗, so that given that we are in set E, the
type is very likely to be close to P ∗.
11.6
CONDITIONAL LIMIT THEOREM
It has been shown that the probability of a set of types under a distribution
Q is determined essentially by the probability of the closest element of
the set to Q; the probability is 2−nD∗to ﬁrst order in the exponent, where
D∗= min
P∈E D(P ||Q).
(11.120)
This follows because the probability of the set of types is the sum of the
probabilities of each type, which is bounded by the largest term times the


