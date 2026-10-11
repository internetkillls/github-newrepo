# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 473

13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
447
Proof:
We will prove upper and lower bounds for ELn. The lower bound
follows directly from standard source coding results (i.e., ELn ≥nH for
any preﬁx-free code). To prove the upper bound, we ﬁrst show that
lim1
nE log Rn ≤H
(13.75)
and later bound the other terms in the expression for Ln. To prove the
bound for E log Rn, we expand the expectation by conditioning on the
value of Xn−1
0
and then applying Jensen’s inequality. Thus,
1
nE log Rn = 1
n

xn−1
0
p(xn−1
0
)E[log Rn(Xn−1
0
)|Xn−1
0
= xn−1
0
]
(13.76)
≤1
n

xn−1
0
p(xn−1
0
) log E[Rn(Xn−1
0
)|Xn−1
0
= xn−1
0
]
(13.77)
= 1
n

xn−1
0
p(xn−1
0
) log
1
p(xn−1
0
)
(13.78)
= 1
nH(Xn−1
0
)
(13.79)
↘H(X).
(13.80)
The second term in the expression for Ln is log log Rn, and we wish to
show that
1
nE[log log Rn(Xn−1
0
)] →0.
(13.81)
Again, we use Jensen’s inequality,
1
nE log log Rn ≤1
n log E[log Rn(Xn−1
0
)]
(13.82)
≤1
n log H(Xn−1
0
),
(13.83)
where the last inequality follows from (13.79). For any ϵ > 0, for large
enough
n,
H(Xn−1
0
) < n(H + ϵ),
and
therefore
1
n log log Rn < 1
n
log n + 1
n log(H + ϵ) →0.
This
completes
the
proof
of
the
theorem.
□
Thus, a compression scheme that represents a string by encoding the
last time it was seen in the past is asymptotically optimal. Of course, this
scheme is not practical, since it assumes that both sender and receiver


## PDF page 474

448
UNIVERSAL SOURCE CODING
have access to the inﬁnite past of a sequence. For longer strings, one
would have to look further and further back into the past to ﬁnd a match.
For example, if the entropy rate is 1
2 and the string has length 200 bits,
one would have to look an average of 2100 ≈1030 bits into the past to
ﬁnd a match. Although this is not feasible, the algorithm illustrates the
basic idea that matching the past is asymptotically optimal. The proof of
the optimality of the practical version of LZ77 with a ﬁnite window is
based on similar ideas. We will not present the details here, but refer the
reader to the original proof in [591].
13.5.2
Optimality of Tree-Structured Lempel–Ziv Compression
We now consider the tree-structured version of Lempel–Ziv, where the
input sequence is parsed into phrases, each phrase being the shortest string
that has not been seen so far. The proof of the optimality of this algorithm
has a very different ﬂavor from the proof for LZ77; the essence of the
proof is a counting argument that shows that the number of phrases cannot
be too large if they are all distinct, and the probability of any sequence of
symbols can be bounded by a function of the number of distinct phrases
in the parsing of the sequence.
The algorithm described in Section 13.4.2 requires two passes over the
string—in the ﬁrst pass, we parse the string and calculate c(n), the number
of phrases in the parsed string. We then use that to decide how many bits
[log c(n)] to allot to the pointers in the algorithm. In the second pass, we
calculate the pointers and produce the coded string as indicated above.
The algorithm can be modiﬁed so that it requires only one pass over the
string and also uses fewer bits for the initial pointers. These modiﬁcations
do not affect the asymptotic efﬁciency of the algorithm. Some of the
implementation details are discussed by Welch [554] and Bell et al. [41].
We will show that like the sliding window version of Lempel–Ziv,
this algorithm asymptotically achieves the entropy rate for the unknown
ergodic source. We ﬁrst deﬁne a parsing of the string to be a decomposition
into phrases.
Deﬁnition
A parsing S of a binary string x1x2 · · · xn is a division of the
string into phrases, separated by commas. A distinct parsing is a parsing
such that no two phrases are identical. For example, 0,111,1 is a distinct
parsing of 01111, but 0,11,11 is a parsing that is not distinct.
The LZ78 algorithm described above gives a distinct parsing of the
source sequence. Let c(n) denote the number of phrases in the LZ78
parsing of a sequence of length n. Of course, c(n) depends on the sequence
Xn. The compressed sequence (after applying the Lempel–Ziv algorithm)


## PDF page 475

13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
449
consists of a list of c(n) pairs of numbers, each pair consisting of a pointer
to the previous occurrence of the preﬁx of the phrase and the last bit of
the phrase. Each pointer requires log c(n) bits, and hence the total length
of the compressed sequence is c(n)[log c(n) + 1] bits. We now show that
c(n)(logc(n)+1)
n
→H(X) for a stationary ergodic sequence X1, X2, . . . , Xn.
Our proof is based on the simple proof of asymptotic optimality of LZ78
coding due to Wyner and Ziv [575].
Before we proceed to the details of the proof, we provide an outline
of the main ideas. The ﬁrst lemma shows that the number of phrases in
a distinct parsing of a sequence is less than n/ log n; the main argument
in the proof is based on the fact that there are not enough distinct short
phrases. This bound holds for any distinct parsing of the sequence, not
just the LZ78 parsing.
The second key idea is a bound on the probability of a sequence based
on the number of distinct phrases. To illustrate this, consider an i.i.d.
sequence of random variables X1, X2, X3, X4 that take on four possible
values, {A, B, C, D}, with probabilities pA, pB, pC, and pD, respec-
tively. Now consider the probability of a sequence P (D, A, B, C) =
pDpApBpC. Since pA + pB + pC + pD = 1, the product pDpApBpC is
maximized when the probabilities are equal (i.e., the maximum value of
the probability of a sequence of four distinct symbols is 1/256). On the
other hand, if we consider a sequence A, B, A, B, the probability of this
sequence is maximized if pA = pB = 1
2, pC = pD = 0, and the maximum
probability for A, B, A, B is 1
16. A sequence of the form A, A, A, A could
have a probability of 1. All these examples illustrate a basic point—se-
quences with a large number of distinct symbols (or phrases) cannot have
a large probability. Ziv’s inequality (Lemma 13.5.5) is the extension of
this idea to the Markov case, where the distinct symbols are the phrases
of the distinct parsing of the source sequence.
Since the description length of a sequence after the parsing grows as
c log c, the sequences that have very few distinct phrases can be com-
pressed efﬁciently and correspond to strings that could have a high prob-
ability. On the other hand, strings that have a large number of distinct
phrases do not compress as well; but the probability of these sequences
could not be too large by Ziv’s inequality. Thus, Ziv’s inequality enables
us to connect the logarithm of the probability of the sequence with the
number of phrases in its parsing, and this is ﬁnally used to show that the
tree-structured Lempel–Ziv algorithm is asymptotically optimal.
We ﬁrst prove a few lemmas that we need for the proof of the theorem.
The ﬁrst is a bound on the number of phrases possible in a distinct parsing
of a binary sequence of length n.


## PDF page 476

450
UNIVERSAL SOURCE CODING
Lemma 13.5.3
(Lempel and Ziv [604])
The number of phrases c(n) in
a distinct parsing of a binary sequence X1, X2, . . . , Xn satisﬁes
c(n) ≤
n
(1 −ϵn) log n,
(13.84)
where ϵn = min{1, log(log n)+4
log n
} →0 as n →∞.
Proof:
Let
nk =
k

j=1
j2j = (k −1)2k+1 + 2
(13.85)
be the sum of the lengths of all distinct strings of length less than or equal
to k. The number of phrases c in a distinct parsing of a sequence of length
n is maximized when all the phrases are as short as possible. If n = nk,
this occurs when all the phrases are of length ≤k, and thus
c(nk) ≤
k

j=1
2j = 2k+1 −2 < 2k+1 ≤
nk
k −1.
(13.86)
If nk ≤n < nk+1, we write n = nk + , where  < (k + 1)2k+1. Then
the parsing into shortest phrases has each of the phrases of length ≤k
and /(k + 1) phrases of length k + 1. Thus,
c(n) ≤
nk
k −1 +

k + 1 ≤nk + 
k −1 =
n
k −1.
(13.87)
We now bound the size of k for a given n. Let nk ≤n < nk+1. Then
n ≥nk = (k −1)2k+1 + 2 ≥2k,
(13.88)
and therefore
k ≤log n.
(13.89)
Moreover,
n ≤nk+1 = k2k+2 + 2 ≤(k + 2)2k+2 ≤(log n + 2)2k+2,
(13.90)
by (13.89), and therefore
k + 2 ≥log
n
log n + 2,
(13.91)


## PDF page 477

13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
451
or for all n ≥4,
k −1 ≥log n −log(log n + 2) −3
(13.92)
=

1 −log(log n + 2) + 3
log n

log n
(13.93)
≥

1 −log(2 log n) + 3
log n

log n
(13.94)
=

1 −log(log n) + 4
log n

log n
(13.95)
= (1 −ϵn) log n.
(13.96)
Note that ϵn = min{1, log(log n)+4
log n
}. Combining (13.96) with (13.87), we
obtain the lemma.
□
We will need a simple result on maximum entropy in the proof of the
main theorem.
Lemma 13.5.4
Let Z be a nonnegative integer-valued random variable
with mean µ. Then the entropy H(Z) is bounded by
H(Z) ≤(µ + 1) log(µ + 1) −µ log µ.
(13.97)
Proof:
The lemma follows directly from the results of Theorem 12.1.1,
which show that the geometric distribution maximizes the entropy of a
nonnegative integer-valued random variable subject to a mean constraint.
□
Let {Xi}∞
i=−∞be a binary stationary ergodic process with probabil-
ity mass function P (x1, x2, . . . , xn). (Ergodic processes are discussed in
greater detail in Section 16.8.) For a ﬁxed integer k, deﬁne the kth-order
Markov approximation to P as
Qk(x−(k−1), . . . , x0, x1, . . . , xn)
△= P (x0
−(k−1))
n

j=1
P (xj|xj−1
j−k),
(13.98)
where xj
i
△= (xi, xi+1, . . . , xj), i ≤j, and the initial state x0
−(k−1) will be
part of the speciﬁcation of Qk. Since P (Xn|Xn−1
n−k) is itself an ergodic


## PDF page 478

452
UNIVERSAL SOURCE CODING
process, we have
−1
n log Qk(X1, X2, . . . , Xn|X0
−(k−1)) = −1
n
n

j=1
log P (Xj|Xj−1
j−k)
(13.99)
→−E log P (Xj|Xj−1
j−k) (13.100)
= H(Xj|Xj−1
j−k).
(13.101)
We will bound the rate of the LZ78 code by the entropy rate of the kth-
order Markov approximation for all k. The entropy rate of the Markov
approximation H(Xj|Xj−1
j−k) converges to the entropy rate of the process
as k →∞, and this will prove the result.
Suppose that Xn
−(k−1) = xn
−(k−1), and suppose that xn
1 is parsed into c
distinct phrases, y1, y2, . . . , yc. Let νi be the index of the start of the
ith phrase (i.e., yi = xνi+1−1
νi
). For each i = 1, 2, . . . , c, deﬁne si = xνi−1
νi−k.
Thus, si is the k bits of x preceding yi. Of course, s1 = x0
−(k−1).
Let cls be the number of phrases yi with length l and preceding state
si = s for l = 1, 2, . . . and s ∈Xk. We then have

l,s
cls = c
(13.102)
and

l,s
lcls = n.
(13.103)
We now prove a surprising upper bound on the probability of a string
based on the parsing of the string.
Lemma 13.5.5
(Ziv’s inequality)
For any distinct parsing (in particu-
lar, the LZ78 parsing) of the string x1x2 · · · xn, we have
log Qk(x1, x2, . . . , xn|s1) ≤−

l,s
cls log cls.
(13.104)
Note that the right-hand side does not depend on Qk.
Proof:
We write
Qk(x1, x2, . . . , xn|s1) = Qk(y1, y2, . . . , yc|s1)
(13.105)


## PDF page 479

13.5
OPTIMALITY OF LEMPEL–ZIV ALGORITHMS
453
=
c
i=1
P (yi|si)
(13.106)
or
log Qk(x1, x2, . . . , xn|s1) =
c

i=1
log P (yi|si)
(13.107)
=

l,s

i:|yi|=l,si=s
log P (yi|si)
(13.108)
=

l,s
cls

i:|yi|=l,si=s
1
cls
log P (yi|si)
(13.109)
≤

l,s
cls log



i:|yi|=l,si=s
1
cls
P (yi|si)

,
(13.110)
where the inequality follows from Jensen’s inequality and the concavity
of the logarithm.
Now since the yi are distinct, we have 
i:|yi|=l,si=s P (yi|si) ≤1. Thus,
log Qk(x1, x2, . . . , xn|s1) ≤

l,s
cls log 1
cls
,
(13.111)
proving the lemma.
□
We can now prove the main theorem.
Theorem 13.5.2
Let {Xn} be a binary stationary ergodic process with
entropy rate H(X), and let c(n) be the number of phrases in a distinct
parsing of a sample of length n from this process. Then
lim sup
n→∞
c(n) log c(n)
n
≤H(X)
(13.112)
with probability 1.
Proof:
We begin with Ziv’s inequality, which we rewrite as
log Qk(x1, x2, . . . , xn|s1) ≤−

l,s
cls log clsc
c
(13.113)


## PDF page 480

454
UNIVERSAL SOURCE CODING
= −c log c −c

ls
cls
c log cls
c .
(13.114)
Writing πls = cls
c , we have

l,s
πls = 1,

l,s
lπls = n
c ,
(13.115)
from (13.102) and (13.103). We now deﬁne random variables U, V such
that
Pr(U = l, V = s) = πls.
(13.116)
Thus, EU = n
c and
log Qk(x1, x2, . . . , xn|s1) ≤cH(U, V ) −c log c
(13.117)
or
−1
n log Qk(x1, x2, . . . , xn|s1) ≥c
n log c −c
nH(U, V ).
(13.118)
Now
H(U, V ) ≤H(U) + H(V )
(13.119)
and H(V ) ≤log |X|k = k. By Lemma 13.5.4, we have
H(U) ≤(EU + 1) log(EU + 1) −(EU) log(EU)
(13.120)
=
$n
c + 1
%
log
$n
c + 1
%
−n
c log n
c
(13.121)
= log n
c +
$n
c + 1
%
log
$c
n + 1
%
.
(13.122)
Thus,
c
nH(U, V ) ≤c
nk + c
n log n
c + o(1).
(13.123)
For a given n, the maximum of c
n log n
c is attained for the maximum value
of c (for c
n ≤1
e). But from Lemma 13.5.3, c ≤
n
log n(1 + o(1)). Thus,
c
n log n
c ≤O
log log n
log n

,
(13.124)


