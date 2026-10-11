# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 377

11.1
METHOD OF TYPES
351
nP (a|X|) objects in a sequence, which is
|T (P )| =

n
nP (a1), nP (a2), . . . , nP (a|X|)

.
(11.17)
This value is hard to manipulate, so we derive simple exponential bounds
on its value.
We suggest two alternative proofs for the exponential bounds. The ﬁrst
proof uses Stirling’s formula [208] to bound the factorial function, and
after some algebra, we can obtain the bounds of the theorem. We give an
alternative proof. We ﬁrst prove the upper bound. Since a type class must
have probability ≤1, we have
1 ≥P n(T (P ))
(11.18)
=

x∈T (P)
P n(x)
(11.19)
=

x∈T (P)
2−nH(P)
(11.20)
= |T (P )|2−nH(P),
(11.21)
using Theorem 11.1.2. Thus,
|T (P )| ≤2nH(P).
(11.22)
Now for the lower bound. We ﬁrst prove that the type class T (P )
has the highest probability among all type classes under the probability
distribution P :
P n(T (P )) ≥P n(T ( ˆP ))
for all ˆP ∈Pn.
(11.23)
We lower bound the ratio of probabilities,
P n(T (P ))
P n(T ( ˆP ))
= |T (P )| 
a∈X P (a)nP(a)
|T ( ˆP )| 
a∈X P (a)n ˆP(a)
(11.24)
=
	
n
nP(a1), nP(a2),...,nP(a|X|)

 
a∈X P (a)nP(a)
	
n
n ˆP(a1), n ˆP(a2),...,n ˆP(a|X|)

 
a∈X P (a)n ˆP (a)
(11.25)
=

a∈X
(n ˆP (a))!
(nP (a))!P (a)n(P(a)−ˆP(a)).
(11.26)


## PDF page 378

352
INFORMATION THEORY AND STATISTICS
Now using the simple bound (easy to prove by separately considering the
cases m ≥n and m < n)
m!
n! ≥nm−n,
(11.27)
we obtain
P n(T (P ))
P n(T ( ˆP ))
≥

a∈X
(nP (a))n ˆP(a)−nP(a)P (a)n(P(a)−ˆP(a))
(11.28)
=

a∈X
nn( ˆP(a)−P(a))
(11.29)
= nn(

a∈X ˆP (a)−
a∈X P(a))
(11.30)
= nn(1−1)
(11.31)
= 1.
(11.32)
Hence, P n(T (P )) ≥P n(T ( ˆP )). The lower bound now follows easily
from this result, since
1 =

Q∈Pn
P n(T (Q))
(11.33)
≤

Q∈Pn
max
Q P n(T (Q))
(11.34)
=

Q∈Pn
P n(T (P ))
(11.35)
≤(n + 1)|X|P n(T (P ))
(11.36)
= (n + 1)|X| 
x∈T (P)
P n(x)
(11.37)
= (n + 1)|X| 
x∈T (P)
2−nH(P)
(11.38)
= (n + 1)|X||T (P )|2−nH(P),
(11.39)
where (11.36) follows from Theorem 11.1.1 and (11.38) follows from
Theorem 11.1.2.
□
We give a slightly better approximation for the binary case.


## PDF page 379

11.1
METHOD OF TYPES
353
Example 11.1.3
(Binary alphabet)
In this case, the type is deﬁned
by the number of 1’s in the sequence, and the size of the type class is
therefore
	n
k

. We show that
1
n + 12
nH
 k
n

≤
n
k

≤2
nH
 k
n

.
(11.40)
These bounds can be proved using Stirling’s approximation for the fac-
torial function (Lemma 17.5.1). But we provide a more intuitive proof
below.
We ﬁrst prove the upper bound. From the binomial formula, for any p,
n

k=0
n
k

pk(1 −p)n−k = 1.
(11.41)
Since all the terms of the sum are positive for 0 ≤p ≤1, each of the
terms is less than 1. Setting p = k/n and taking the kth term, we get
1 ≥
n
k
 k
n
k 
1 −k
n
n−k
(11.42)
=
n
k

2k log k
n+(n−k) log n−k
n
(11.43)
=
n
k

2
n

k
n log k
n+ n−k
n
log n−k
n

(11.44)
=
n
k

2
−nH

k
n

.
(11.45)
Hence,
n
k

≤2
nH

k
n

.
(11.46)
For the lower bound, let S be a random variable with a binomial
distribution with parameters n and p. The most likely value of S is
S = ⟨np⟩. This can easily be veriﬁed from the fact that
P (S = i + 1)
P (S = i)
= n −i
i + 1
p
1 −p
(11.47)
and considering the cases when i < np and when i > np. Then, since
there are n + 1 terms in the binomial sum,


## PDF page 380

354
INFORMATION THEORY AND STATISTICS
1 =
n

k=0
n
k

pk(1 −p)n−k ≤(n + 1) max
k
n
k

pk(1 −p)n−k (11.48)
= (n + 1)
 n
⟨np⟩

p⟨np⟩(1 −p)n−⟨np⟩.
(11.49)
Now let p = k/n. Then we have
1 ≤(n + 1)
n
k
 k
n
k 
1 −k
n
n−k
,
(11.50)
which by the arguments in (11.45) is equivalent to
1
n + 1 ≤
n
k

2
−nH

k
n

,
(11.51)
or
n
k

≥2
nH

k
n

n + 1 .
(11.52)
Combining the two results, we see that
n
k

.= 2
nH

k
n

.
(11.53)
A more precise bound can be found in theorem 17.5.1 when k ̸= 0 or n.
Theorem 11.1.4
(Probability of type class)
for any P ∈Pn and any
distribution Q, the probability of the type class T (P ) under Qn is 2−nD(P||Q)
to ﬁrst order in the exponent. More precisely,
1
(n + 1)|X| 2−nD(P||Q) ≤Qn(T (P )) ≤2−nD(P||Q).
(11.54)
Proof:
We have
Qn(T (P )) =

x∈T (P)
Qn(x)
(11.55)
=

x∈T (P)
2−n(D(P||Q)+H(P))
(11.56)
= |T (P )|2−n(D(P||Q)+H(P)),
(11.57)


## PDF page 381

11.2
LAW OF LARGE NUMBERS
355
by Theorem 11.1.2. Using the bounds on |T (P )| derived in Theorem
11.1.3, we have
1
(n + 1)|X| 2−nD(P||Q) ≤Qn(T (P )) ≤2−nD(P||Q).
□
(11.58)
We can summarize the basic theorems concerning types in four equa-
tions:
|Pn| ≤(n + 1)|X|,
(11.59)
Qn(x) = 2−n(D(Px||Q)+H(Px)),
(11.60)
|T (P )| .= 2nH(P),
(11.61)
Qn(T (P )) .= 2−nD(P||Q).
(11.62)
These equations state that there are only a polynomial number of types
and that there are an exponential number of sequences of each type. We
also have an exact formula for the probability of any sequence of type P
under distribution Q and an approximate formula for the probability of a
type class.
These equations allow us to calculate the behavior of long sequences
based on the properties of the type of the sequence. For example, for
long sequences drawn i.i.d. according to some distribution, the type of
the sequence is close to the distribution generating the sequence, and we
can use the properties of this distribution to estimate the properties of the
sequence. Some of the applications that will be dealt with in the next few
sections are as follows:
• The law of large numbers
• Universal source coding
• Sanov’s theorem
• The Chernoff–Stein lemma and hypothesis testing
• Conditional probability and limit theorems
11.2
LAW OF LARGE NUMBERS
The concept of type and type classes enables us to give an alternative
statement of the law of large numbers. In fact, it can be used as a proof
of a version of the weak law in the discrete case. The most important
property of types is that there are only a polynomial number of types, and


## PDF page 382

356
INFORMATION THEORY AND STATISTICS
an exponential number of sequences of each type. Since the probability
of each type class depends exponentially on the relative entropy distance
between the type P and the distribution Q, type classes that are far from
the true distribution have exponentially smaller probability.
Given an ϵ > 0, we can deﬁne a typical set T ϵ
Q of sequences for the
distribution Qn as
T ϵ
Q = {xn : D(Pxn||Q) ≤ϵ}.
(11.63)
Then the probability that xn is not typical is
1 −Qn(T ϵ
Q) =

P:D(P||Q)>ϵ
Qn(T (P ))
(11.64)
≤

P:D(P||Q)>ϵ
2−nD(P||Q)
(Theorem 11.1.4)
(11.65)
≤

P:D(P||Q)>ϵ
2−nϵ
(11.66)
≤(n + 1)|X|2−nϵ
(Theorem 11.1.1)
(11.67)
= 2
−n

ϵ−|X| log(n+1)
n

,
(11.68)
which goes to 0 as n →∞. Hence, the probability of the typical set T ϵ
Q
goes to 1 as n →∞. This is similar to the AEP proved in Chapter 3,
which is a form of the weak law of large numbers. We now prove that
the empirical distribution PXn converges to P .
Theorem 11.2.1
Let X1, X2, . . . , Xn be i.i.d. ∼P (x). Then
Pr {D(Pxn||P ) > ϵ} ≤2−n(ϵ−|X| log(n+1)
n
),
(11.69)
and consequently, D(Pxn||P ) →0 with probability 1.
Proof:
The inequality (11.69) was proved in (11.68). Summing over n,
we ﬁnd that
∞

n=1
Pr{D(Pxn||P ) > ϵ} < ∞.
(11.70)


## PDF page 383

11.3
UNIVERSAL SOURCE CODING
357
Thus, the expected number of occurrences of the event {D(Pxn||P ) > ϵ}
for all n is ﬁnite, which implies that the actual number of such occur-
rences is also ﬁnite with probability 1 (Borel–Cantelli lemma). Hence
D(Pxn||P ) →0 with probability 1.
□
We now deﬁne a stronger version of typicality than in Chapter 3.
Deﬁnition
We deﬁne the strongly typical set A∗(n)
ϵ
to be the set of
sequences in Xn for which the sample frequencies are close to the true
values:
A∗(n)
ϵ
=



x ∈Xn :

1
nN(a|x) −P (a)
 <
ϵ
|X |,
if P (a) > 0
N(a|x) = 0
if P (a) = 0



.
(11.71)
Hence, the typical set consists of sequences whose type does not differ
from the true probabilities by more than ϵ/|X| in any component. By the
strong law of large numbers, it follows that the probability of the strongly
typical set goes to 1 as n →∞. The additional power afforded by strong
typicality is useful in proving stronger results, particularly in universal
coding, rate distortion theory, and large deviation theory.
11.3
UNIVERSAL SOURCE CODING
Huffman coding compresses an i.i.d. source with a known distribution
p(x) to its entropy limit H(X). However, if the code is designed for
some incorrect distribution q(x), a penalty of D(p||q) is incurred. Thus,
Huffman coding is sensitive to the assumed distribution.
What compression can be achieved if the true distribution p(x) is
unknown? Is there a universal code of rate R, say, that sufﬁces to describe
every i.i.d. source with entropy H(X) < R? The surprising answer is yes.
The idea is based on the method of types. There are 2nH(P) sequences of
type P . Since there are only a polynomial number of types with denom-
inator n, an enumeration of all sequences xn with type Pxn such that
H(Pxn) < R will require roughly nR bits. Thus, by describing all such
sequences, we are prepared to describe any sequence that is likely to arise
from any distribution Q having entropy H(Q) < R. We begin with a
deﬁnition.
Deﬁnition
A ﬁxed-rate block code of rate R for a source X1, X2, . . . ,
Xn which has an unknown distribution Q consists of two mappings: the
encoder,
fn : Xn →{1, 2, . . . , 2nR},
(11.72)


## PDF page 384

358
INFORMATION THEORY AND STATISTICS
and the decoder,
φn : {1, 2, . . . , 2nR} →Xn.
(11.73)
Here R is called the rate of the code. The probability of error for the
code with respect to the distribution Q is
P (n)
e
= Qn(Xn : φn(fn(Xn)) ̸= Xn)
(11.74)
Deﬁnition
A rate R block code for a source will be called universal
if the functions fn and φn do not depend on the distribution Q and if
P (n)
e
→0 as n →∞if R > H(Q).
We now describe one such universal encoding scheme, due to Csisz´ar
and K¨orner [149], that is based on the fact that the number of sequences
of type P increases exponentially with the entropy and the fact that there
are only a polynomial number of types.
Theorem 11.3.1
There exists a sequence of (2nR, n) universal source
codes such that P (n)
e
→0 for every source Q such that H(Q) < R.
Proof:
Fix the rate R for the code. Let
Rn = R −|X|log(n + 1)
n
.
(11.75)
Consider the set of sequences
A = {x ∈Xn : H(Px) ≤Rn}.
(11.76)
Then
|A| =

P∈Pn:H(P)≤Rn
|T (P )|
(11.77)
≤

P∈Pn:H(P)≤Rn
2nH(P)
(11.78)
≤

P∈Pn:H(P)≤Rn
2nRn
(11.79)
≤(n + 1)|X|2nRn
(11.80)
= 2n(Rn+|X| log(n+1)
n
)
(11.81)
= 2nR.
(11.82)


