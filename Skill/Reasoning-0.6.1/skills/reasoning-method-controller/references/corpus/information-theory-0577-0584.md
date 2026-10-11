# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 577

15.4
ENCODING OF CORRELATED SOURCES
551
Assume that we wish to transmit 100 days of weather information to the
National Weather Service headquarters in Washington. We could send all
the 100 bits of the weather in both places, making 200 bits in all. If we
decided to compress the information independently, we would still need
100H(0.5) = 100 bits of information from each place, for a total of 200
bits. If, instead, we use Slepian–Wolf encoding, we need only H(X) +
H(Y|X) = 100H(0.5) + 100H(0.89) = 100 + 50 = 150 bits total.
Example 15.4.2
Consider the following joint distribution:
p(u, v)
0
1
0
1
3
1
3
1
0
1
3
In this case, the total rate required for the transmission of this
source is H(U) + H(V |U) = log 3 = 1.58 bits rather than the 2 bits that
would be needed if the sources were transmitted independently without
Slepian–Wolf encoding.
15.4.1
Achievability of the Slepian–Wolf Theorem
We now prove the achievability of the rates in the Slepian–Wolf theorem.
Before we proceed to the proof, we introduce a new coding procedure
using random bins. The essential idea of random bins is very similar to
hash functions: We choose a large random index for each source sequence.
If the set of typical source sequences is small enough (or equivalently, the
range of the hash function is large enough), then with high probability,
different source sequences have different indices, and we can recover the
source sequence from the index.
Let us consider the application of this idea to the encoding of a single
source. In Chapter 3 the method that we considered was to index all
elements of the typical set and not bother about elements outside the
typical set. We will now describe the random binning procedure, which
indexes all sequences but rejects untypical sequences at a later stage.
Consider the following procedure: For each sequence Xn, draw an index
at random from {1, 2, . . . , 2nR}. The set of sequences Xn which have the
same index are said to form a bin, since this can be viewed as ﬁrst laying
down a row of bins and then throwing the Xn’s at random into the bins.
For decoding the source from the bin index, we look for a typical Xn
sequence in the bin. If there is one and only one typical Xn sequence
in the bin, we declare it to be the estimate ˆXn of the source sequence;
otherwise, an error is declared.


## PDF page 578

552
NETWORK INFORMATION THEORY
The above procedure deﬁnes a source code. To analyze the probability
of error for this code, we will now divide the Xn sequences into two
types, typical sequences and nontypical sequences. If the source sequence
is typical, the bin corresponding to this source sequence will contain at
least one typical sequence (the source sequence itself). Hence there will
be an error only if there is more than one typical sequence in this bin. If
the source sequence is nontypical, there will always be an error. But if
the number of bins is much larger than the number of typical sequences,
the probability that there is more than one typical sequence in a bin is
very small, and hence the probability that a typical sequence will result
in an error is very small.
Formally, let f (Xn) be the bin index corresponding to Xn. Call the
decoding function g. The probability of error (averaged over the random
choice ofcodes f ) is
P (g(f (X)) ̸= X) ≤P (X /∈A(n)
ϵ ) +

x
P (∃x′ ̸= x : x′ ∈A(n)
ϵ , f (x′)
= f (x))p(x)
≤ϵ +

x

x′ ∈A(n)
ϵ
x′ ̸= x
P (f (x′) = f (x))p(x) (15.161)
≤ϵ +

x

x′∈A(n)
ϵ
2−nRp(x)
(15.162)
= ϵ +

x′∈A(n)
ϵ
2−nR 
x
p(x)
(15.163)
≤ϵ +

x′∈A(n)
ϵ
2−nR
(15.164)
≤ϵ + 2n(H(X)+ϵ)2−nR
(15.165)
≤2ϵ
(15.166)
if R > H(X) + ϵ and n is sufﬁciently large. Hence, if the rate of the code
is greater than the entropy, the probability of error is arbitrarily small and
the code achieves the same results as the code described in Chapter 3.
The above example illustrates the fact that there are many ways to
construct codes with low probabilities of error at rates above the entropy
of the source; the universal source code is another example of such a code.


## PDF page 579

15.4
ENCODING OF CORRELATED SOURCES
553
Note that the binning scheme does not require an explicit characterization
of the typical set at the encoder; it is needed only at the decoder. It is
this property that enables this code to continue to work in the case of a
distributed source, as illustrated in the proof of the theorem.
We now return to the consideration of the distributed source coding and
prove the achievability of the rate region in the Slepian–Wolf theorem.
Proof:
(Achievability in Theorem 15.4.1). The basic idea of the proof is
to partition the space of Xn into 2nR1 bins and the space of Yn into 2nR2
bins.
Random code generation: Assign every x ∈Xn to one of 2nR1 bins
independently according to a uniform distribution on {1, 2, . . . , 2nR1}.
Similarly, randomly assign every y ∈Yn to one of 2nR2 bins. Reveal
the assignments f1 and f2 to both the encoder and the decoder.
Encoding: Sender 1 sends the index of the bin to which X belongs.
Sender 2 sends the index of the bin to which Y belongs.
Decoding: Given the received index pair (i0, j0), declare (ˆx, ˆy) = (x, y)
if there is one and only one pair of sequences (x, y) such that f1(x) = i0,
f2(y) = j0 and (x, y) ∈A(n)
ϵ . Otherwise, declare an error. The scheme
is illustrated in Figure 15.20. The set of X sequences and the set of Y
sequences are divided into bins in such a way that the pair of indices
speciﬁes a product bin.
2nH(X, Y )
jointly typical pairs
(xn,yn)
2nR1 bins
yn
xn
2nR2 bins
FIGURE 15.20. Slepian–Wolf encoding: the jointly typical pairs are isolated by the product
bins.


## PDF page 580

554
NETWORK INFORMATION THEORY
Probability of error: Let (Xi, Yi) ∼p(x, y). Deﬁne the events
E0 = {(X, Y) /∈A(n)
ϵ },
(15.167)
E1 = {∃x′ ̸= X : f1(x′) = f1(X) and (x′, Y) ∈A(n)
ϵ },
(15.168)
E2 = {∃y′ ̸= Y : f2(y′) = f2(Y) and (X, y′) ∈A(n)
ϵ },
(15.169)
and
E12 = {∃(x′, y′) : x′ ̸= X, y′ ̸= Y, f1(x′)
= f1(X), f2(y′) = f2(Y) and (x′, y′) ∈A(n)
ϵ }.
(15.170)
Here X, Y, f1, and f2 are random. We have an error if (X, Y) is not in
A(n)
ϵ
or if there is another typical pair in the same bin. Hence by the union
of events bound,
P (n)
e
= P (E0 ∪E1 ∪E2 ∪E12)
(15.171)
≤P (E0) + P (E1) + P (E2) + P (E12).
(15.172)
First consider E0. By the AEP, P (E0) →0 and hence for n sufﬁciently
large, P (E0) < ϵ. To bound P (E1), we have
P (E1) = P {∃x′ ̸= X : f1(x′) = f1(X), and (x′, Y) ∈A(n)
ϵ }
(15.173)
=

(x,y)
p(x, y)P {∃x′ ̸= x : f1(x′) = f1(x), (x′, y) ∈A(n)
ϵ }
(15.174)
≤

(x,y)
p(x, y)

x′ ̸= x
(x′, y) ∈A(n)
ϵ
P (f1(x′) = f1(x))
(15.175)
=

(x,y)
p(x, y)2−nR1|Aϵ(X|y)|
(15.176)
≤2−nR12n(H(X|Y)+ϵ)
(by Theorem 15.2.2 ),
(15.177)
which goes to 0 if R1 > H(X|Y). Hence for sufﬁciently large n, P (E1) <
ϵ. Similarly, for sufﬁciently large n, P (E2) < ϵ if R2 > H(Y|X) and
P (E12) < ϵ if R1 + R2 > H(X, Y). Since the average probability of error
is < 4ϵ, there exists at least one code (f ∗
1 , f ∗
2 , g∗) with probability of error
< 4ϵ. Thus, we can construct a sequence of codes with P (n)
e
→0, and
the proof of achievability is complete.
□


## PDF page 581

15.4
ENCODING OF CORRELATED SOURCES
555
15.4.2
Converse for the Slepian–Wolf Theorem
The converse for the Slepian–Wolf theorem follows obviously from the
results for a single source, but we will provide it for completeness.
Proof:
(Converse to Theorem 15.4.1). As usual, we begin with Fano’s
inequality. Let f1, f2, g be ﬁxed. Let I0 = f1(Xn) and J0 = f2(Y n). Then
H(Xn, Y n|I0, J0) ≤P (n)
e
n(log |X| + log |Y|) + 1 = nϵn,
(15.178)
where ϵn →0 as n →∞. Now adding conditioning, we also have
H(Xn|Y n, I0, J0) ≤nϵn,
(15.179)
and
H(Y n|Xn, I0, J0) ≤nϵn.
(15.180)
We can write a chain of inequalities
n(R1 + R2)
(a)
≥H(I0, J0)
(15.181)
= I (Xn, Y n; I0, J0) + H(I0, J0|Xn, Y n)
(15.182)
(b)
= I (Xn, Y n; I0, J0)
(15.183)
= H(Xn, Y n) −H(Xn, Y n|I0, J0)
(15.184)
(c)
≥H(Xn, Y n) −nϵn
(15.185)
(d)
= nH(X, Y) −nϵn,
(15.186)
where
(a) follows
from
the
fact
that
I0 ∈{1, 2, . . . , 2nR1}
and
J0 ∈
{1, 2, . . . , 2nR2}
(b) follows from the fact the I0 is a function of Xn and J0 is a function
of Y n
(c) follows from Fano’s inequality (15.178)
(d) follows from the chain rule and the fact that (Xi, Yi) are i.i.d.


## PDF page 582

556
NETWORK INFORMATION THEORY
Similarly, using (15.179), we have
nR1
(a)
≥H(I0)
(15.187)
≥H(I0|Y n)
(15.188)
= I (Xn; I0|Y n) + H(I0|Xn, Y n)
(15.189)
(b)
= I (Xn; I0|Y n)
(15.190)
= H(Xn|Y n) −H(Xn|I0, J0, Y n)
(15.191)
(c)
≥H(Xn|Y n) −nϵn
(15.192)
(d)
= nH(X|Y) −nϵn,
(15.193)
where the reasons are the same as for the equations above. Similarly, we
can show that
nR2 ≥nH(Y|X) −nϵn.
(15.194)
Dividing these inequalities by n and taking the limit as n →∞, we have
the desired converse.
□
The region described in the Slepian–Wolf theorem is illustrated in
Figure 15.21.
15.4.3
Slepian–Wolf Theorem for Many Sources
The results of Section 15.4.2 can easily be generalized to many sources.
The proof follows exactly the same lines.
Theorem 15.4.2
Let (X1i, X2i, . . . , Xmi) be i.i.d. ∼p(x1, x2, . . . , xm).
Then the set of rate vectors achievable for distributed source coding with
separate encoders and a common decoder is deﬁned by
R(S) > H(X(S)|X(Sc))
(15.195)
for all S ⊆{1, 2, . . . , m}, where
R(S) =

i∈S
Ri
(15.196)
and X(S) = {Xj : j ∈S}.


## PDF page 583

15.4
ENCODING OF CORRELATED SOURCES
557
R2
R1
H(Y )
H(Y|X)
H(X|Y)
H(X)
0
FIGURE 15.21. Rate region for Slepian–Wolf encoding.
Proof:
The proof is identical to the case of two variables and is
omitted.
□
The achievability of Slepian–Wolf encoding has been proved for an
i.i.d. correlated source, but the proof can easily be extended to the case
of an arbitrary joint source that satisﬁes the AEP; in particular, it can
be extended to the case of any jointly ergodic source [122]. In these
cases the entropies in the deﬁnition of the rate region are replaced by the
corresponding entropy rates.
15.4.4
Interpretation of Slepian–Wolf Coding
We consider an interpretation of the corner points of the rate region in
Slepian–Wolf encoding in terms of graph coloring. Consider the point
with rate R1 = H(X), R2 = H(Y|X). Using nH(X) bits, we can encode
Xn efﬁciently, so that the decoder can reconstruct Xn with arbitrarily low
probability of error. But how do we code Y n with nH(Y|X) bits? Looking
at the picture in terms of typical sets, we see that associated with every
Xn is a typical “fan” of Y n sequences that are jointly typical with the
given Xn as shown in Figure 15.22.
If the Y encoder knows Xn, the encoder can send the index of the Y n
within this typical fan. The decoder, also knowing Xn, can then construct
this typical fan and hence reconstruct Y n. But the Y encoder does not
know Xn. So instead of trying to determine the typical fan, he randomly


## PDF page 584

558
NETWORK INFORMATION THEORY
xn
yn
FIGURE 15.22. Jointly typical fans.
colors all Y n sequences with 2nR2 colors. If the number of colors is high
enough, then with high probability all the colors in a particular fan will
be different and the color of the Y n sequence will uniquely deﬁne the
Y n sequence within the Xn fan. If the rate R2 > H(Y|X), the number of
colors is exponentially larger than the number of elements in the fan and
we can show that the scheme will have an exponentially small probability
of error.
15.5
DUALITY BETWEEN SLEPIAN–WOLF ENCODING
AND MULTIPLE-ACCESS CHANNELS
With multiple-access channels, we considered the problem of sending
independent messages over a channel with two inputs and only one output.
With Slepian–Wolf encoding, we considered the problem of sending a
correlated source over a noiseless channel, with a common decoder for
recovery of both sources. In this section we explore the duality between
the two systems.
In Figure 15.23, two independent messages are to be sent over the
channel as Xn
1 and Xn
2 sequences. The receiver estimates the messages
from the received sequence. In Figure 15.24 the correlated sources are
encoded as “independent” messages i and j. The receiver tries to estimate
the source sequences from knowledge of i and j.
In the proof of the achievability of the capacity region for the multiple-
access channel, we used a random map from the set of messages to the


