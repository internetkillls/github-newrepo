# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 225

7.7
CHANNEL CODING THEOREM
199
any randomly chosen pair is jointly typical is about 2−nI(X;Y). Hence,
we can consider about 2nI(X;Y) such pairs before we are likely to come
across a jointly typical pair. This suggests that there are about 2nI(X;Y)
distinguishable signals Xn.
Another way to look at this is in terms of the set of jointly typical
sequences for a ﬁxed output sequence Y n, presumably the output sequence
resulting from the true input signal Xn. For this sequence Y n, there are
about 2nH(X|Y) conditionally typical input signals. The probability that
some randomly chosen (other) input signal Xn is jointly typical with Y n
is about 2nH(X|Y)/2nH(X) = 2−nI(X;Y). This again suggests that we can
choose about 2nI(X;Y) codewords Xn(W) before one of these codewords
will get confused with the codeword that caused the output Y n.
7.7
CHANNEL CODING THEOREM
We now prove what is perhaps the basic theorem of information theory,
the achievability of channel capacity, ﬁrst stated and essentially proved
by Shannon in his original 1948 paper. The result is rather counterintu-
itive; if the channel introduces errors, how can one correct them all? Any
correction process is also subject to error, ad inﬁnitum.
Shannon used a number of new ideas to prove that information can be
sent reliably over a channel at all rates up to the channel capacity. These
ideas include:
• Allowing an arbitrarily small but nonzero probability of error
• Using the channel many times in succession, so that the law of large
numbers comes into effect
• Calculating the average of the probability of error over a random
choice of codebooks, which symmetrizes the probability, and which
can then be used to show the existence of at least one good code
Shannon’s outline of the proof was based on the idea of typical sequen-
ces, but the proof was not made rigorous until much later. The proof given
below makes use of the properties of typical sequences and is probably
the simplest of the proofs developed so far. As in all the proofs, we
use the same essential ideas—random code selection, calculation of the
average probability of error for a random choice of codewords, and so
on. The main difference is in the decoding rule. In the proof, we decode
by joint typicality; we look for a codeword that is jointly typical with the
received sequence. If we ﬁnd a unique codeword satisfying this property,
we declare that word to be the transmitted codeword. By the properties


## PDF page 226

200
CHANNEL CAPACITY
of joint typicality stated previously, with high probability the transmitted
codeword and the received sequence are jointly typical, since they are
probabilistically related. Also, the probability that any other codeword
looks jointly typical with the received sequence is 2−nI. Hence, if we
have fewer then 2nI codewords, then with high probability there will be
no other codewords that can be confused with the transmitted codeword,
and the probability of error is small.
Although jointly typical decoding is suboptimal, it is simple to analyze
and still achieves all rates below capacity.
We now give the complete statement and proof of Shannon’s second
theorem:
Theorem 7.7.1
(Channel coding theorem)
For a discrete memory-
less channel, all rates below capacity C are achievable. Speciﬁcally, for
every rate R < C, there exists a sequence of (2nR, n) codes with maximum
probability of error λ(n) →0.
Conversely, any sequence of (2nR, n) codes with λ(n) →0 must have
R ≤C.
Proof:
We prove that rates R < C are achievable and postpone proof of
the converse to Section 7.9.
Achievability: Fix p(x). Generate a (2nR, n) code at random according
to the distribution p(x). Speciﬁcally, we generate 2nR codewords inde-
pendently according to the distribution
p(xn) =
n
	
i=1
p(xi).
(7.60)
We exhibit the 2nR codewords as the rows of a matrix:
C =


x1(1)
x2(1)
· · ·
xn(1)
...
...
...
...
x1(2nR)
x2(2nR)
· · ·
xn(2nR)

.
(7.61)
Each entry in this matrix is generated i.i.d. according to p(x). Thus, the
probability that we generate a particular code C is
Pr(C) =
2nR
	
w=1
n
	
i=1
p(xi(w)).
(7.62)


## PDF page 227

7.7
CHANNEL CODING THEOREM
201
Consider the following sequence of events:
1. A random code C is generated as described in (7.62) according to
p(x).
2. The code C is then revealed to both sender and receiver. Both sender
and receiver are also assumed to know the channel transition matrix
p(y|x) for the channel.
3. A message W is chosen according to a uniform distribution
Pr(W = w) = 2−nR,
w = 1, 2, . . . , 2nR.
(7.63)
4. The wth codeword Xn(w), corresponding to the wth row of C, is
sent over the channel.
5. The receiver receives a sequence Y n according to the distribution
P (yn|xn(w)) =
n
	
i=1
p(yi|xi(w)).
(7.64)
6. The receiver guesses which message was sent. (The optimum proce-
dure to minimize probability of error is maximum likelihood decod-
ing (i.e., the receiver should choose the a posteriori most likely
message). But this procedure is difﬁcult to analyze. Instead, we will
use jointly typical decoding, which is described below. Jointly typi-
cal decoding is easier to analyze and is asymptotically optimal.) In
jointly typical decoding, the receiver declares that the index ˆW was
sent if the following conditions are satisﬁed:
• (Xn( ˆW), Y n) is jointly typical.
• There is no other index W ′ ̸= ˆW such that (Xn(W ′), Y n) ∈
A(n)
ϵ .
If no such ˆW exists or if there is more than one such, an error is
declared. (We may assume that the receiver outputs a dummy index
such as 0 in this case.)
7. There is a decoding error if ˆW ̸= W. Let E be the event { ˆW ̸= W}.
Analysis of the probability of error
Outline: We ﬁrst outline the analysis. Instead of calculating the proba-
bility of error for a single code, we calculate the average over all codes
generated at random according to the distribution (7.62). By the symmetry
of the code construction, the average probability of error does not depend


## PDF page 228

202
CHANNEL CAPACITY
on the particular index that was sent. For a typical codeword, there are two
different sources of error when we use jointly typical decoding: Either the
output Y n is not jointly typical with the transmitted codeword or there is
some other codeword that is jointly typical with Y n. The probability that
the transmitted codeword and the received sequence are jointly typical
goes to 1, as shown by the joint AEP. For any rival codeword, the proba-
bility that it is jointly typical with the received sequence is approximately
2−nI, and hence we can use about 2nI codewords and still have a low
probability of error. We will later extend the argument to ﬁnd a code with
a low maximal probability of error.
Detailed calculation of the probability of error: We let W be drawn
according to a uniform distribution over {1, 2, . . . , 2nR} and use jointly
typical decoding
ˆW(yn) as described in step 6. Let E = { ˆW(Y n) ̸= W}
denote the error event. We will calculate the average probability of error,
averaged over all codewords in the codebook, and averaged over all code-
books; that is, we calculate
Pr(E) =

C
Pr(C)P (n)
e
(C)
(7.65)
=

C
Pr(C) 1
2nR
2nR

w=1
λw(C)
(7.66)
=
1
2nR
2nR

w=1

C
Pr(C)λw(C),
(7.67)
where P (n)
e
(C) is deﬁned for jointly typical decoding. By the symmetry
of the code construction, the average probability of error averaged over
all codes does not depend on the particular index that was sent [i.e.,

C Pr(C)λw(C) does not depend on w]. Thus, we can assume without
loss of generality that the message W = 1 was sent, since
Pr(E) =
1
2nR
2nR

w=1

C
Pr(C)λw(C)
(7.68)
=

C
Pr(C)λ1(C)
(7.69)
= Pr(E|W = 1).
(7.70)
Deﬁne the following events:
Ei = { (Xn(i), Y n) is in A(n)
ϵ },
i ∈{1, 2, . . . , 2nR},
(7.71)


## PDF page 229

7.7
CHANNEL CODING THEOREM
203
where Ei is the event that the ith codeword and Y n are jointly typical.
Recall that Y n is the result of sending the ﬁrst codeword Xn(1) over the
channel.
Then an error occurs in the decoding scheme if either Ec
1 occurs (when
the transmitted codeword and the received sequence are not jointly typical)
or E2 ∪E3 ∪· · · ∪E2nR occurs (when a wrong codeword is jointly typical
with the received sequence). Hence, letting P (E) denote Pr(E|W = 1), we
have
Pr(E|W = 1) = P

Ec
1 ∪E2 ∪E3 ∪· · · ∪E2nR|W = 1

(7.72)
≤P (Ec
1|W = 1) +
2nR

i=2
P (Ei|W = 1),
(7.73)
by the union of events bound for probabilities. Now, by the joint AEP,
P (Ec
1|W = 1)→0, and hence
P (Ec
1|W = 1) ≤ϵ
for n sufﬁciently large.
(7.74)
Since by the code generation process, Xn(1) and Xn(i) are independent
for i ̸= 1, so are Y n and Xn(i). Hence, the probability that Xn(i) and Y n
are jointly typical is ≤2−n(I(X;Y)−3ϵ) by the joint AEP. Consequently,
Pr(E) = Pr(E|W = 1) ≤P (Ec
1|W = 1) +
2nR

i=2
P (Ei|W = 1) (7.75)
≤ϵ +
2nR

i=2
2−n(I(X;Y)−3ϵ)
(7.76)
= ϵ +

2nR −1

2−n(I(X;Y)−3ϵ)
(7.77)
≤ϵ + 23nϵ2−n(I(X;Y)−R)
(7.78)
≤2ϵ
(7.79)
if n is sufﬁciently large and R < I (X; Y) −3ϵ. Hence, if R < I (X; Y),
we can choose ϵ and n so that the average probability of error, averaged
over codebooks and codewords, is less than 2ϵ.
To ﬁnish the proof, we will strengthen this conclusion by a series of
code selections.
1. Choose p(x) in the proof to be p∗(x), the distribution on X that
achieves capacity. Then the condition R < I (X; Y) can be replaced
by the achievability condition R < C.


## PDF page 230

204
CHANNEL CAPACITY
2. Get rid of the average over codebooks. Since the average proba-
bility of error over codebooks is small (≤2ϵ), there exists at least
one codebook C∗with a small average probability of error. Thus,
Pr(E|C∗) ≤2ϵ. Determination of C∗can be achieved by an exhaus-
tive search over all (2nR, n) codes. Note that
Pr(E|C∗) =
1
2nR
2nR

i=1
λi(C∗),
(7.80)
since we have chosen
ˆW according to a uniform distribution as
speciﬁed in (7.63).
3. Throw away the worst half of the codewords in the best codebook
C∗. Since the arithmetic average probability of error P (n)
e
(C∗) for
this code is less then 2ϵ, we have
Pr(E|C∗) ≤
1
2nR

λi(C∗) ≤2ϵ,
(7.81)
which implies that at least half the indices i and their associated
codewords Xn(i) must have conditional probability of error λi less
than 4ϵ (otherwise, these codewords themselves would contribute
more than 2ϵ to the sum). Hence the best half of the codewords
have a maximal probability of error less than 4ϵ. If we reindex these
codewords, we have 2nR−1 codewords. Throwing out half the code-
words has changed the rate from R to R −1
n, which is negligible
for large n.
Combining all these improvements, we have constructed a code of rate
R′ = R −1
n, with maximal probability of error λ(n) ≤4ϵ. This proves the
achievability of any rate below capacity.
□
Random coding is the method of proof for Theorem 7.7.1, not the
method of signaling. Codes are selected at random in the proof merely to
symmetrize the mathematics and to show the existence of a good deter-
ministic code. We proved that the average over all codes of block length
n has a small probability of error. We can ﬁnd the best code within this
set by an exhaustive search. Incidentally, this shows that the Kolmogorov
complexity (Chapter 14) of the best code is a small constant. This means
that the revelation (in step 2) to the sender and receiver of the best code
C∗requires no channel. The sender and receiver merely agree to use the
best (2nR, n) code for the channel.
Although the theorem shows that there exist good codes with arbitrar-
ily small probability of error for long block lengths, it does not provide
a way of constructing the best codes. If we used the scheme suggested


## PDF page 231

7.8
ZERO-ERROR CODES
205
by the proof and generate a code at random with the appropriate distri-
bution, the code constructed is likely to be good for long block lengths.
However, without some structure in the code, it is very difﬁcult to decode
(the simple scheme of table lookup requires an exponentially large table).
Hence the theorem does not provide a practical coding scheme. Ever
since Shannon’s original paper on information theory, researchers have
tried to develop structured codes that are easy to encode and decode.
In Section 7.11, we discuss Hamming codes, the simplest of a class of
algebraic error correcting codes that can correct one error in a block of
bits. Since Shannon’s paper, a variety of techniques have been used to
construct error correcting codes, and with turbo codes have come close
to achieving capacity for Gaussian channels.
7.8
ZERO-ERROR CODES
The outline of the proof of the converse is most clearly motivated by
going through the argument when absolutely no errors are allowed. We
will now prove that P (n)
e
= 0 implies that R ≤C. Assume that we have a
(2nR, n) code with zero probability of error [i.e., the decoder output g(Y n)
is equal to the input index W with probability 1]. Then the input index W
is determined by the output sequence [i.e., H(W|Y n) = 0]. Now, to obtain
a strong bound, we arbitrarily assume that W is uniformly distributed
over {1, 2, . . . , 2nR}. Thus, H(W) = nR. We can now write the string of
inequalities:
nR = H(W) = H(W|Y n)



=0
+I (W; Y n)
(7.82)
= I (W; Y n)
(7.83)
(a)
≤I (Xn; Y n)
(7.84)
(b)
≤
n

i=1
I (Xi; Yi)
(7.85)
(c)
≤nC,
(7.86)
where (a) follows from the data-processing inequality (since W →Xn(W)
→Y n forms a Markov chain), (b) will be proved in Lemma 7.9.2 using
the discrete memoryless assumption, and (c) follows from the deﬁnition
of (information) capacity. Hence, for any zero-error (2nR, n) code, for
all n,
R ≤C.
(7.87)


## PDF page 232

206
CHANNEL CAPACITY
7.9
FANO’S INEQUALITY AND THE CONVERSE
TO THE CODING THEOREM
We now extend the proof that was derived for zero-error codes to the case
of codes with very small probabilities of error. The new ingredient will be
Fano’s inequality, which gives a lower bound on the probability of error
in terms of the conditional entropy. Recall the proof of Fano’s inequality,
which is repeated here in a new context for reference.
Let us deﬁne the setup under consideration. The index W is uniformly
distributed on the set W = {1, 2, . . . , 2nR}, and the sequence Y n is related
probabilistically to W. From Y n, we estimate the index W that was sent.
Let the estimate be ˆW = g(Y n). Thus, W →Xn(W) →Y n →ˆW forms
a Markov chain. Note that the probability of error is
Pr
 ˆW ̸= W

=
1
2nR

i
λi = P (n)
e
.
(7.88)
We begin with the following lemma, which has been proved in
Section 2.10:
Lemma 7.9.1
(Fano’s inequality)
For a discrete memoryless channel
with a codebook C and the input message W uniformly distributed over
2nR, we have
H(W| ˆW) ≤1 + P (n)
e
nR.
(7.89)
Proof:
Since W is uniformly distributed, we have P (n)
e
= Pr(W ̸= ˆW).
We apply Fano’s inequality (Theorem 2.10.1) for W in an alphabet of
size 2nR.
□
We will now prove a lemma which shows that the capacity per trans-
mission is not increased if we use a discrete memoryless channel many
times.
Lemma 7.9.2
Let Y n be the result of passing Xn through a discrete
memoryless channel of capacity C. Then
I (Xn; Y n) ≤nC
for all p(xn).
(7.90)
Proof
I (Xn; Y n) = H(Y n) −H(Y n|Xn)
(7.91)
= H(Y n) −
n

i=1
H(Yi|Y1, . . . , Yi−1, Xn)
(7.92)
= H(Y n) −
n

i=1
H(Yi|Xi),
(7.93)


