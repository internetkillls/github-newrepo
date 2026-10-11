# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 81

HISTORICAL NOTES
55
Many of the simple properties of these quantities were developed by
Shannon. Fano’s inequality was proved in Fano [201]. The notion of
sufﬁcient statistic was deﬁned by Fisher [209], and the notion of the
minimal sufﬁcient statistic was introduced by Lehmann and Scheff´e [350].
The relationship of mutual information and sufﬁciency is due to Kullback
[335]. The relationship between information theory and thermodynamics
has been discussed extensively by Brillouin [77] and Jaynes [294].
The physics of information is a vast new subject of inquiry spawned
from statistical mechanics, quantum mechanics, and information theory.
The key question is how information is represented physically. Quan-
tum channel capacity (the logarithm of the number of distinguishable
preparations of a physical system) and quantum data compression [299]
are well-deﬁned problems with nice answers involving the von Neumann
entropy. A new element of quantum information arises from the exis-
tence of quantum entanglement and the consequences (exhibited in Bell’s
inequality) that the observed marginal distribution of physical events are
not consistent with any joint distribution (no local realism). The funda-
mental text by Nielsen and Chuang [395] develops the theory of quantum
information and the quantum counterparts to many of the results in this
book. There have also been attempts to determine whether there are
any fundamental physical limits to computation, including work by Ben-
nett [47] and Bennett and Landauer [48].


## PDF page 82



## PDF page 83

CHAPTER 3
ASYMPTOTIC EQUIPARTITION
PROPERTY
In information theory, the analog of the law of large numbers is the
asymptotic equipartition property (AEP). It is a direct consequence
of the weak law of large numbers. The law of large numbers states
that for independent, identically distributed (i.i.d.) random variables,
1
n
n
i=1 Xi is close to its expected value EX for large values of n.
The AEP states that 1
n log
1
p(X1,X2,...,Xn) is close to the entropy H, where
X1, X2, . . . , Xn are i.i.d. random variables and p(X1, X2, . . . , Xn) is the
probability of observing the sequence X1, X2, . . . , Xn. Thus, the proba-
bility p(X1, X2, . . . , Xn) assigned to an observed sequence will be close
to 2−nH.
This enables us to divide the set of all sequences into two sets, the
typical set, where the sample entropy is close to the true entropy, and the
nontypical set, which contains the other sequences. Most of our attention
will be on the typical sequences. Any property that is proved for the typical
sequences will then be true with high probability and will determine the
average behavior of a large sample.
First, an example. Let the random variable X ∈{0, 1} have a probability
mass function deﬁned by p(1) = p and p(0) = q. If X1, X2, . . . , Xn are
i.i.d. according to p(x), the probability of a sequence x1, x2, . . . , xn is
n
i=1 p(xi). For example, the probability of the sequence (1, 0, 1, 1, 0, 1)
is p
 Xiqn− Xi = p4q2. Clearly, it is not true that all 2n sequences of
length n have the same probability.
However, we might be able to predict the probability of the sequence
that we actually observe. We ask for the probability p(X1, X2, . . . , Xn) of
the outcomes X1, X2, . . . , Xn, where X1, X2, . . . are i.i.d. ∼p(x). This is
insidiously self-referential, but well deﬁned nonetheless. Apparently, we
are asking for the probability of an event drawn according to the same
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
57


## PDF page 84

58
ASYMPTOTIC EQUIPARTITION PROPERTY
probability distribution. Here it turns out that p(X1, X2, . . . , Xn) is close
to 2−nH with high probability.
We summarize this by saying, “Almost all events are almost equally
surprising.” This is a way of saying that
Pr

(X1, X2, . . . , Xn) : p(X1, X2, . . . , Xn) = 2−n(H±ϵ)
≈1
(3.1)
if X1, X2, . . . , Xn are i.i.d. ∼p(x).
In the example just given, where p(X1, X2, . . . , Xn) = p
 Xiqn− Xi,
we are simply saying that the number of 1’s in the sequence is close
to np (with high probability), and all such sequences have (roughly) the
same probability 2−nH(p). We use the idea of convergence in probability,
deﬁned as follows:
Deﬁnition
(Convergence of random variables). Given a sequence of
random variables, X1, X2, . . . , we say that the sequence X1, X2, . . . con-
verges to a random variable X:
1. In probability if for every ϵ > 0, Pr{|Xn −X| > ϵ} →0
2. In mean square if E(Xn −X)2 →0
3. With probability 1 (also called almost surely) if Pr{limn→∞Xn =
X} = 1
3.1
ASYMPTOTIC EQUIPARTITION PROPERTY THEOREM
The asymptotic equipartition property is formalized in the following
theorem.
Theorem 3.1.1
(AEP)
If X1, X2, . . . are i.i.d. ∼p(x), then
−1
n log p(X1, X2, . . . , Xn) →H(X)
in probability.
(3.2)
Proof:
Functions of independent random variables are also independent
random variables. Thus, since the Xi are i.i.d., so are log p(Xi). Hence,
by the weak law of large numbers,
−1
n log p(X1, X2, . . . , Xn) = −1
n

i
log p(Xi)
(3.3)
→−E log p(X)
in probability
(3.4)
= H(X),
(3.5)
which proves the theorem.
□


## PDF page 85

3.1
ASYMPTOTIC EQUIPARTITION PROPERTY THEOREM
59
Deﬁnition
The typical set A(n)
ϵ
with respect to p(x) is the set of se-
quences (x1, x2, . . . , xn) ∈Xn with the property
2−n(H(X)+ϵ) ≤p(x1, x2, . . . , xn) ≤2−n(H(X)−ϵ).
(3.6)
As a consequence of the AEP, we can show that the set A(n)
ϵ
has the
following properties:
Theorem 3.1.2
1. If (x1, x2, . . . , xn) ∈A(n)
ϵ , then H(X) −ϵ ≤−1
n log p(x1, x2, . . . ,
xn) ≤H(X) + ϵ.
2. Pr

A(n)
ϵ

> 1 −ϵ for n sufﬁciently large.
3.
A(n)
ϵ
 ≤2n(H(X)+ϵ), where |A| denotes the number of elements in the
set A.
4. |A(n)
ϵ | ≥(1 −ϵ)2n(H(X)−ϵ) for n sufﬁciently large.
Thus, the typical set has probability nearly 1, all elements of the typical
set are nearly equiprobable, and the number of elements in the typical set
is nearly 2nH.
Proof:
The proof of property (1) is immediate from the deﬁnition of
A(n)
ϵ . The second property follows directly from Theorem 3.1.1, since the
probability of the event (X1, X2, . . . , Xn) ∈A(n)
ϵ
tends to 1 as n →∞.
Thus, for any δ > 0, there exists an n0 such that for all n ≥n0, we have
Pr
−1
n log p(X1, X2, . . . , Xn) −H(X)
 < ϵ

> 1 −δ.
(3.7)
Setting δ = ϵ, we obtain the second part of the theorem. The identiﬁcation
of δ = ϵ will conveniently simplify notation later.
To prove property (3), we write
1 =

x∈X n
p(x)
(3.8)
≥

x∈A(n)
ϵ
p(x)
(3.9)
≥

x∈A(n)
ϵ
2−n(H(X)+ϵ)
(3.10)
= 2−n(H(X)+ϵ)|A(n)
ϵ |,
(3.11)


## PDF page 86

60
ASYMPTOTIC EQUIPARTITION PROPERTY
where the second inequality follows from (3.6). Hence
|A(n)
ϵ | ≤2n(H(X)+ϵ).
(3.12)
Finally, for sufﬁciently large n, Pr{A(n)
ϵ } > 1 −ϵ, so that
1 −ϵ < Pr{A(n)
ϵ }
(3.13)
≤

x∈A(n)
ϵ
2−n(H(X)−ϵ)
(3.14)
= 2−n(H(X)−ϵ)|A(n)
ϵ |,
(3.15)
where the second inequality follows from (3.6). Hence,
|A(n)
ϵ | ≥(1 −ϵ)2n(H(X)−ϵ),
(3.16)
which completes the proof of the properties of A(n)
ϵ .
□
3.2
CONSEQUENCES OF THE AEP: DATA COMPRESSION
Let X1, X2, . . . , Xn be independent, identically distributed random vari-
ables drawn from the probability mass function p(x). We wish to ﬁnd
short descriptions for such sequences of random variables. We divide all
sequences in Xn into two sets: the typical set A(n)
ϵ
and its complement,
as shown in Figure 3.1.
Non-typical set
Typical set
∋
∋
A(n): 2n(H +   ) elements
n:|    |n elements
FIGURE 3.1. Typical sets and source coding.


## PDF page 87

3.2
CONSEQUENCES OF THE AEP: DATA COMPRESSION
61
Non-typical set
Typical set
Description: n log |    | + 2 bits
Description: n(H +   ) + 2 bits
∋
FIGURE 3.2. Source code using the typical set.
We order all elements in each set according to some order (e.g., lexi-
cographic order). Then we can represent each sequence of A(n)
ϵ
by giving
the index of the sequence in the set. Since there are ≤2n(H+ϵ) sequences
in A(n)
ϵ , the indexing requires no more than n(H + ϵ) + 1 bits. [The extra
bit may be necessary because n(H + ϵ) may not be an integer.] We pre-
ﬁx all these sequences by a 0, giving a total length of ≤n(H + ϵ) + 2
bits to represent each sequence in A(n)
ϵ
(see Figure 3.2). Similarly, we can
index each sequence not in A(n)
ϵ
by using not more than n log |X| + 1 bits.
Preﬁxing these indices by 1, we have a code for all the sequences in Xn.
Note the following features of the above coding scheme:
• The code is one-to-one and easily decodable. The initial bit acts as
a ﬂag bit to indicate the length of the codeword that follows.
• We have used a brute-force enumeration of the atypical set A(n)
ϵ
c
without taking into account the fact that the number of elements in
A(n)
ϵ
c is less than the number of elements in Xn. Surprisingly, this is
good enough to yield an efﬁcient description.
• The typical sequences have short descriptions of length ≈nH.
We use the notation xn to denote a sequence x1, x2, . . . , xn. Let l(xn)
be the length of the codeword corresponding to xn. If n is sufﬁciently
large so that Pr{A(n)
ϵ } ≥1 −ϵ, the expected length of the codeword is
E(l(Xn)) =

xn
p(xn)l(xn)
(3.17)


## PDF page 88

62
ASYMPTOTIC EQUIPARTITION PROPERTY
=

xn∈A(n)
ϵ
p(xn)l(xn) +

xn∈A(n)
ϵ
c
p(xn)l(xn)
(3.18)
≤

xn∈A(n)
ϵ
p(xn)(n(H + ϵ) + 2)
+

xn∈A(n)
ϵ
c
p(xn)(n log |X| + 2)
(3.19)
= Pr

A(n)
ϵ

(n(H + ϵ) + 2) + Pr
	
A(n)
ϵ
c
(n log |X| + 2)
(3.20)
≤n(H + ϵ) + ϵn(log |X|) + 2
(3.21)
= n(H + ϵ′),
(3.22)
where ϵ′ = ϵ + ϵ log |X| + 2
n can be made arbitrarily small by an appro-
priate choice of ϵ followed by an appropriate choice of n. Hence we have
proved the following theorem.
Theorem 3.2.1
Let Xn be i.i.d. ∼p(x). Let ϵ > 0. Then there exists a
code that maps sequences xn of length n into binary strings such that the
mapping is one-to-one (and therefore invertible) and
E
1
nl(Xn)

≤H(X) + ϵ
(3.23)
for n sufﬁciently large.
Thus, we can represent sequences Xn using nH(X) bits on the average.
3.3
HIGH-PROBABILITY SETS AND THE TYPICAL SET
From the deﬁnition of A(n)
ϵ , it is clear that A(n)
ϵ
is a fairly small set that
contains most of the probability. But from the deﬁnition, it is not clear
whether it is the smallest such set. We will prove that the typical set has
essentially the same number of elements as the smallest set, to ﬁrst order
in the exponent.
Deﬁnition
For each n = 1, 2, . . . , let B(n)
δ
⊂Xn be the smallest set
with
Pr{B(n)
δ } ≥1 −δ.
(3.24)


