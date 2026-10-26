# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 217

7.4
PREVIEW OF THE CHANNEL CODING THEOREM
191
The above derivation for symmetric channels carries over to weakly
symmetric channels as well. We have the following theorem for weakly
symmetric channels:
Theorem 7.2.1
For a weakly symmetric channel,
C = log |Y| −H(row of transition matrix),
(7.25)
and this is achieved by a uniform distribution on the input alphabet.
7.3
PROPERTIES OF CHANNEL CAPACITY
1. C ≥0 since I (X; Y) ≥0.
2. C ≤log |X| since C = max I (X; Y) ≤max H(X) = log |X|.
3. C ≤log |Y| for the same reason.
4. I (X; Y) is a continuous function of p(x).
5. I (X; Y) is a concave function of p(x) (Theorem 2.7.4). Since
I (X; Y) is a concave function over a closed convex set, a local
maximum is a global maximum. From properties 2 and 3, the maxi-
mum is ﬁnite, and we are justiﬁed in using the term maximum rather
than supremum in the deﬁnition of capacity. The maximum can then
be found by standard nonlinear optimization techniques such as gra-
dient search. Some of the methods that can be used include the
following:
• Constrained maximization using calculus and the Kuhn–Tucker
conditions.
• The Frank–Wolfe gradient search algorithm.
• An iterative algorithm developed by Arimoto [25] and Blahut
[65]. We describe the algorithm in Section 10.8.
In general, there is no closed-form solution for the capacity. But for
many simple channels it is possible to calculate the capacity using prop-
erties such as symmetry. Some of the examples considered earlier are of
this form.
7.4
PREVIEW OF THE CHANNEL CODING THEOREM
So far, we have deﬁned the information capacity of a discrete memoryless
channel. In the next section we prove Shannon’s second theorem, which


## PDF page 218

192
CHANNEL CAPACITY
Xn
Yn
FIGURE 7.7. Channels after n uses.
gives an operational meaning to the deﬁnition of capacity as the number
of bits we can transmit reliably over the channel. But ﬁrst we will try to
give an intuitive idea as to why we can transmit C bits of information over
a channel. The basic idea is that for large block lengths, every channel
looks like the noisy typewriter channel (Figure 7.4) and the channel has a
subset of inputs that produce essentially disjoint sequences at the output.
For each (typical) input n-sequence, there are approximately 2nH(Y|X)
possible Y sequences, all of them equally likely (Figure 7.7). We wish
to ensure that no two X sequences produce the same Y output sequence.
Otherwise, we will not be able to decide which X sequence was sent.
The total number of possible (typical) Y sequences is ≈2nH(Y). This set
has to be divided into sets of size 2nH(Y|X) corresponding to the different
input X sequences. The total number of disjoint sets is less than or equal
to 2n(H(Y)−H(Y|X)) = 2nI(X;Y). Hence, we can send at most ≈2nI(X;Y)
distinguishable sequences of length n.
Although the above derivation outlines an upper bound on the capacity,
a stronger version of the above argument will be used in the next section
to prove that this rate I is achievable with an arbitrarily low probability
of error.
Before we proceed to the proof of Shannon’s second theorem, we need
a few deﬁnitions.
7.5
DEFINITIONS
We analyze a communication system as shown in Figure 7.8.
A message W, drawn from the index set {1, 2, . . . , M}, results in the
signal Xn(W), which is received by the receiver as a random sequence


## PDF page 219

7.5
DEFINITIONS
193
Encoder
Decoder
Channel
p(y|x)
W
Xn
Yn
Message
W
Estimate
of
Message
^
FIGURE 7.8. Communication channel.
Y n ∼p(yn|xn). The receiver then guesses the index W by an appropriate
decoding rule ˆW = g(Y n). The receiver makes an error if ˆW is not the
same as the index W that was transmitted. We now deﬁne these ideas
formally.
Deﬁnition
A discrete channel, denoted by (X, p(y|x), Y), consists of
two ﬁnite sets X and Y and a collection of probability mass functions
p(y|x), one for each x ∈X, such that for every x and y, p(y|x) ≥0, and
for every x, 
y p(y|x) = 1, with the interpretation that X is the input
and Y is the output of the channel.
Deﬁnition
The nth extension of the discrete memoryless channel (DMC)
is the channel (Xn, p(yn|xn), Yn), where
p(yk|xk, yk−1) = p(yk|xk),
k = 1, 2, . . . , n.
(7.26)
Remark
If the channel is used without feedback [i.e., if the input sym-
bols do not depend on the past output symbols, namely, p(xk|xk−1, yk−1)
= p(xk|xk−1)], the channel transition function for the nth extension of the
discrete memoryless channel reduces to
p(yn|xn) =
n
	
i=1
p(yi|xi).
(7.27)
When we refer to the discrete memoryless channel, we mean the discrete
memoryless channel without feedback unless we state explicitly other-
wise.
Deﬁnition
An (M, n) code for the channel (X, p(y|x), Y) consists of
the following:
1. An index set {1, 2, . . . , M}.
2. An encoding function Xn : {1, 2, . . . , M} →Xn, yielding codewords
xn(1), xn(2), . . ., xn(M). The set of codewords is called the code-
book.


## PDF page 220

194
CHANNEL CAPACITY
3. A decoding function
g: Yn →{1, 2, . . . , M},
(7.28)
which is a deterministic rule that assigns a guess to each possible
received vector.
Deﬁnition
(Conditional probability of error) Let
λi = Pr(g(Y n) ̸= i|Xn = xn(i)) =

yn
p(yn|xn(i))I (g(yn) ̸= i) (7.29)
be the conditional probability of error given that index i was sent, where
I (·) is the indicator function.
Deﬁnition
The maximal probability of error λ(n) for an (M, n) code is
deﬁned as
λ(n) =
max
i∈{1,2,...,M} λi.
(7.30)
Deﬁnition
The (arithmetic) average probability of error P (n)
e
for an
(M, n) code is deﬁned as
P (n)
e
= 1
M
M

i=1
λi.
(7.31)
Note that if the index W is chosen according to a uniform distribution
over the set {1, 2, . . . , M}, and Xn = xn(W), then
P (n)
e
△= Pr(W ̸= g(Y n)),
(7.32)
(i.e., P (n)
e
is the probability of error). Also, obviously,
P (n)
e
≤λ(n).
(7.33)
One would expect the maximal probability of error to behave quite differ-
ently from the average probability. But in the next section we prove that
a small average probability of error implies a small maximal probability
of error at essentially the same rate.


## PDF page 221

7.6
JOINTLY TYPICAL SEQUENCES
195
It is worth noting that P (n)
e
deﬁned in (7.32) is only a mathematical
construct of the conditional probabilities of error λi and is itself a proba-
bility of error only if the message is chosen uniformly over the message
set {1, 2, . . . , 2M}. However, both in the proof of achievability and the
converse, we choose a uniform distribution on W to bound the probability
of error. This allows us to establish the behavior of P (n)
e
and the maximal
probability of error λ(n) and thus characterize the behavior of the channel
regardless of how it is used (i.e., no matter what the distribution of W).
Deﬁnition
The rate R of an (M, n) code is
R = log M
n
bits per transmission.
(7.34)
Deﬁnition
A rate R is said to be achievable if there exists a sequence
of (

2nR
, n) codes such that the maximal probability of error λ(n) tends
to 0 as n →∞.
Later, we write (2nR, n) codes to mean (

2nR
, n) codes. This will
simplify the notation.
Deﬁnition
The capacity of a channel is the supremum of all achievable
rates.
Thus, rates less than capacity yield arbitrarily small probability of error
for sufﬁciently large block lengths.
7.6
JOINTLY TYPICAL SEQUENCES
Roughly speaking, we decode a channel output Y n as the ith index if
the codeword Xn(i) is “jointly typical” with the received signal Y n. We
now deﬁne the important idea of joint typicality and ﬁnd the probabil-
ity of joint typicality when Xn(i) is the true cause of Y n and when it
is not.
Deﬁnition
The set A(n)
ϵ
of jointly typical sequences {(xn, yn)} with
respect to the distribution p(x, y) is the set of n-sequences with empirical
entropies ϵ-close to the true entropies:
A(n)
ϵ
=

(xn, yn) ∈Xn × Yn :
−1
n log p(xn) −H(X)
 < ϵ,
(7.35)


## PDF page 222

196
CHANNEL CAPACITY
−1
n log p(yn) −H(Y)
 < ϵ,
(7.36)
−1
n log p(xn, yn) −H(X, Y)
 < ϵ

,
(7.37)
where
p(xn, yn) =
n
	
i=1
p(xi, yi).
(7.38)
Theorem 7.6.1
(Joint AEP)
Let (Xn, Y n) be sequences of length n
drawn i.i.d. according to p(xn, yn) = n
i=1 p(xi, yi). Then:
1. Pr((Xn, Y n) ∈A(n)
ϵ ) →1 as n →∞.
2. |A(n)
ϵ | ≤2n(H(X,Y)+ϵ).
3. If ( ˜Xn, ˜Y n) ∼p(xn)p(yn) [i.e., ˜Xn and ˜Y n are independent with the
same marginals as p(xn, yn)], then
Pr

( ˜Xn, ˜Y n) ∈A(n)
ϵ

≤2−n(I(X;Y)−3ϵ).
(7.39)
Also, for sufﬁciently large n,
Pr

( ˜Xn, ˜Y n) ∈A(n)
ϵ

≥(1 −ϵ)2−n(I(X;Y)+3ϵ).
(7.40)
Proof
1. We begin by showing that with high probability, the sequence is in
the typical set. By the weak law of large numbers,
−1
n log p(Xn) →−E[log p(X)] = H(X)
in probability.
(7.41)
Hence, given ϵ > 0, there exists n1, such that for all n > n1,
Pr
−1
n log p(Xn) −H(X)
 ≥ϵ

< ϵ
3.
(7.42)
Similarly, by the weak law,
−1
n log p(Y n) →−E[log p(Y)] = H(Y)
in probability
(7.43)


## PDF page 223

7.6
JOINTLY TYPICAL SEQUENCES
197
and
−1
n log p(Xn, Y n) →−E[log p(X, Y)] = H(X, Y) in probability,
(7.44)
and there exist n2 and n3, such that for all n ≥n2,
Pr
−1
n log p(Y n) −H(Y)
 ≥ϵ

< ϵ
3
(7.45)
and for all n ≥n3,
Pr
−1
n log p(Xn, Y n) −H(X, Y)
 ≥ϵ

< ϵ
3.
(7.46)
Choosing n > max{n1, n2, n3}, the probability of the union of the
sets in (7.42), (7.45), and (7.46) must be less than ϵ. Hence for n
sufﬁciently large, the probability of the set A(n)
ϵ
is greater than 1 −ϵ,
establishing the ﬁrst part of the theorem.
2. To prove the second part of the theorem, we have
1 =

p(xn, yn)
(7.47)
≥

A(n)
ϵ
p(xn, yn)
(7.48)
≥|A(n)
ϵ |2−n(H(X,Y)+ϵ),
(7.49)
and hence
|A(n)
ϵ | ≤2n(H(X,Y)+ϵ).
(7.50)
3. Now if ˜Xn and ˜Y n are independent but have the same marginals as
Xn and Y n, then
Pr(( ˜Xn, ˜Y n) ∈A(n)
ϵ ) =

(xn,yn)∈A(n)
ϵ
p(xn)p(yn)
(7.51)
≤2n(H(X,Y)+ϵ)2−n(H(X)−ϵ)2−n(H(Y)−ϵ)
(7.52)
= 2−n(I(X;Y)−3ϵ).
(7.53)


## PDF page 224

198
CHANNEL CAPACITY
For sufﬁciently large n, Pr(A(n)
ϵ ) ≥1 −ϵ, and therefore
1 −ϵ ≤

(xn,yn)∈A(n)
ϵ
p(xn, yn)
(7.54)
≤|A(n)
ϵ |2−n(H(X,Y)−ϵ)
(7.55)
and
|A(n)
ϵ | ≥(1 −ϵ)2n(H(X,Y)−ϵ).
(7.56)
By similar arguments to the upper bound above, we can also show
that for n sufﬁciently large,
Pr(( ˜Xn, ˜Y n) ∈A(n)
ϵ ) =

A(n)
ϵ
p(xn)p(yn)
(7.57)
≥(1 −ϵ)2n(H(X,Y)−ϵ)2−n(H(X)+ϵ)2−n(H(Y)+ϵ)
(7.58)
= (1 −ϵ)2−n(I(X;Y)+3ϵ).
□
(7.59)
The jointly typical set is illustrated in Figure 7.9. There are about
2nH(X) typical X sequences and about 2nH(Y) typical Y sequences. How-
ever, since there are only 2nH(X,Y) jointly typical sequences, not all pairs
of typical Xn and typical Y n are also jointly typical. The probability that
.
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
..
.
.
.
.
.
.
.
..
.
.
..
..
.
.
..
..
.
.
.
..
.
.
.
.
.
.
.
..
..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
xn
yn
FIGURE 7.9. Jointly typical sequences.


