# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 289

9.1
GAUSSIAN CHANNEL: DEFINITIONS
263
into a discrete four-input channel. In some practical modulation schemes,
similar ideas are used to convert the continuous channel into a discrete
channel. The main advantage of a discrete channel is ease of processing
of the output signal for error correction, but some information is lost in
the quantization.
9.1
GAUSSIAN CHANNEL: DEFINITIONS
We now deﬁne the (information) capacity of the channel as the maxi-
mum of the mutual information between the input and output over all
distributions on the input that satisfy the power constraint.
Deﬁnition
The information capacity of the Gaussian channel with
power constraint P is
C =
max
f (x):E X2≤P
I (X; Y).
(9.8)
We can calculate the information capacity as follows: Expanding
I (X; Y), we have
I (X; Y) = h(Y) −h(Y|X)
(9.9)
= h(Y) −h(X + Z|X)
(9.10)
= h(Y) −h(Z|X)
(9.11)
= h(Y) −h(Z),
(9.12)
since Z is independent of X. Now, h(Z) = 1
2 log 2πeN. Also,
EY 2 = E(X + Z)2 = EX2 + 2EXEZ + EZ2 = P + N,
(9.13)
since X and Z are independent and EZ = 0. Given EY 2 = P + N, the
entropy of Y is bounded by
1
2 log 2πe(P + N) by Theorem 8.6.5 (the
normal maximizes the entropy for a given variance).
Applying this result to bound the mutual information, we obtain
I (X; Y) = h(Y) −h(Z)
(9.14)
≤1
2 log 2πe(P + N) −1
2 log 2πeN
(9.15)
= 1
2 log

1 + P
N

.
(9.16)


## PDF page 290

264
GAUSSIAN CHANNEL
Hence, the information capacity of the Gaussian channel is
C = max
EX2≤P
I (X; Y) = 1
2 log

1 + P
N

,
(9.17)
and the maximum is attained when X ∼N(0, P ).
We will now show that this capacity is also the supremum of the rates
achievable for the channel. The arguments are similar to the arguments
for a discrete channel. We will begin with the corresponding deﬁnitions.
Deﬁnition
An (M, n) code for the Gaussian channel with power con-
straint P consists of the following:
1. An index set {1, 2, . . . , M}.
2. An encoding function x : {1, 2, . . . , M} →Xn, yielding codewords
xn(1), xn(2), . . . , xn(M), satisfying the power constraint P ; that is,
for every codeword
n

i=1
x2
i (w) ≤nP,
w = 1, 2, . . . , M.
(9.18)
3. A decoding function
g : Yn →{1, 2, . . . , M}.
(9.19)
The rate and probability of error of the code are deﬁned as in Chapter 7
for the discrete case. The arithmetic average of the probability of error is
deﬁned by
P (n)
e
=
1
2nR

λi.
(9.20)
Deﬁnition
A rate R is said to be achievable for a Gaussian channel
with a power constraint P if there exists a sequence of (2nR, n) codes
with codewords satisfying the power constraint such that the maximal
probability of error λ(n) tends to zero. The capacity of the channel is the
supremum of the achievable rates.
Theorem 9.1.1
The capacity of a Gaussian channel with power con-
straint P and noise variance N is
C = 1
2 log

1 + P
N

bits per transmission.
(9.21)


## PDF page 291

9.1
GAUSSIAN CHANNEL: DEFINITIONS
265
Remark
We ﬁrst present a plausibility argument as to why we may be
able to construct (2nC, n) codes with a low probability of error. Consider
any codeword of length n. The received vector is normally distributed with
mean equal to the true codeword and variance equal to the noise variance.
With high probability, the received vector is contained in a sphere of radius
√n(N + ϵ) around the true codeword. If we assign everything within this
sphere to the given codeword, when this codeword is sent there will be
an error only if the received vector falls outside the sphere, which has
low probability.
Similarly, we can choose other codewords and their corresponding
decoding spheres. How many such codewords can we choose? The vol-
ume of an n-dimensional sphere is of the form Cnrn, where r is the
radius of the sphere. In this case, each decoding sphere has radius
√
nN.
These spheres are scattered throughout the space of received vectors. The
received vectors have energy no greater than n(P + N), so they lie in a
sphere of radius √n(P + N). The maximum number of nonintersecting
decoding spheres in this volume is no more than
Cn(n(P + N))
n
2
Cn(nN)
n
2
= 2
n
2 log

1 + P
N

(9.22)
and the rate of the code is 1
2 log(1 + P
N ). This idea is illustrated in Figure 9.2.
FIGURE 9.2. Sphere packing for the Gaussian channel.


## PDF page 292

266
GAUSSIAN CHANNEL
This sphere-packing argument indicates that we cannot hope to send
at rates greater than C with low probability of error. However, we can
actually do almost as well as this, as is proved next.
Proof:
(Achievability). We will use the same ideas as in the proof of
the channel coding theorem in the case of discrete channels: namely,
random codes and joint typicality decoding. However, we must make
some modiﬁcations to take into account the power constraint and the fact
that the variables are continuous and not discrete.
1. Generation of the codebook. We wish to generate a codebook in
which all the codewords satisfy the power constraint. To ensure
this, we generate the codewords with each element i.i.d. accord-
ing to a normal distribution with variance P −ϵ. Since for large
n, 1
n
 X2
i →P −ϵ, the probability that a codeword does not sat-
isfy the power constraint will be small. Let Xi(w), i = 1, 2, . . . , n,
w = 1, 2, . . . , 2nR be i.i.d. ∼N(0, P −ϵ), forming codewords
Xn(1), Xn(2), . . . , Xn(2nR) ∈Rn.
2. Encoding. After the generation of the codebook, the codebook is
revealed to both the sender and the receiver. To send the message
index w, the transmitter sends the wth codeword Xn(w) in the code-
book.
3. Decoding. The receiver looks down the list of codewords {Xn(w)}
and searches for one that is jointly typical with the received vector.
If there is one and only one such codeword Xn(w), the receiver
declares
ˆW = w to be the transmitted codeword. Otherwise, the
receiver declares an error. The receiver also declares an error if the
chosen codeword does not satisfy the power constraint.
4. Probability of error. Without loss of generality, assume that code-
word 1 was sent. Thus, Y n = Xn(1) + Zn. Deﬁne the following
events:
E0 =



1
n
n

j=1
X2
j(1) > P



(9.23)
and
Ei =

(Xn(i), Y n) is in A(n)
ϵ

.
(9.24)
Then an error occurs if E0 occurs (the power constraint is violated)
or Ec
1 occurs (the transmitted codeword and the received sequence
are not jointly typical) or E2 ∪E3 ∪· · · ∪E2nR occurs (some wrong


## PDF page 293

9.1
GAUSSIAN CHANNEL: DEFINITIONS
267
codeword is jointly typical with the received sequence). Let E denote
the event ˆW ̸= W and let P denote the conditional probability given
that W = 1. Hence,
Pr(E|W = 1) = P (E) = P

E0 ∪Ec
1 ∪E2 ∪E3 ∪· · · ∪E2nR

(9.25)
≤P (E0) + P (Ec
1) +
2nR

i=2
P (Ei),
(9.26)
by the union of events bound for probabilities. By the law of large
numbers, P (E0) →0 as n →∞. Now, by the joint AEP (which
can be proved using the same argument as that used in the discrete
case), P (Ec
1) →0, and hence
P (Ec
1) ≤ϵ
for n sufﬁciently large.
(9.27)
Since by the code generation process, Xn(1) and Xn(i) are indepen-
dent, so are Y n and Xn(i). Hence, the probability that Xn(i) and Y n
will be jointly typical is ≤2−n(I(X;Y)−3ϵ) by the joint AEP.
Now let W be uniformly distributed over {1, 2, . . . , 2nR}, and con-
sequently,
Pr(E) =
1
2nR

λi = P (n)
e
.
(9.28)
Then
P (n)
e
= Pr(E) = Pr(E|W = 1)
(9.29)
≤P (E0) + P (Ec
1) +
2nR

i=2
P (Ei)
(9.30)
≤ϵ + ϵ +
2nR

i=2
2−n(I(X;Y)−3ϵ)
(9.31)
= 2ϵ +

2nR −1

2−n(I(X;Y)−3ϵ)
(9.32)
≤2ϵ + 23nϵ2−n(I(X;Y)−R)
(9.33)
≤3ϵ
(9.34)


## PDF page 294

268
GAUSSIAN CHANNEL
for n sufﬁciently large and R < I (X; Y) −3ϵ. This proves the exis-
tence of a good (2nR, n) code.
Now choosing a good codebook and deleting the worst half of the
codewords, we obtain a code with low maximal probability of error. In
particular, the power constraint is satisﬁed by each of the remaining code-
words (since the codewords that do not satisfy the power constraint have
probability of error 1 and must belong to the worst half of the codewords).
Hence we have constructed a code that achieves a rate arbitrarily close to
capacity. The forward part of the theorem is proved. In the next section
we show that the achievable rate cannot exceed the capacity.
□
9.2
CONVERSE TO THE CODING THEOREM FOR GAUSSIAN
CHANNELS
In this section we complete the proof that the capacity of a Gaussian
channel is C = 1
2 log(1 + P
N ) by proving that rates R > C are not achiev-
able. The proof parallels the proof for the discrete channel. The main new
ingredient is the power constraint.
Proof:
(Converse to Theorem 9.1.1). We must show that if P (n)
e
→0 for
a sequence of (2nR, n) codes for a Gaussian channel with power constraint
P , then
R ≤C = 1
2 log

1 + P
N

.
(9.35)
Consider any (2nR, n) code that satisﬁes the power constraint, that is,
1
n
n

i=1
x2
i (w) ≤P,
(9.36)
for w = 1, 2, . . . , 2nR. Proceeding as in the converse for the discrete case,
let W be distributed uniformly over {1, 2, . . . , 2nR}. The uniform distri-
bution over the index set W ∈{1, 2, . . . , 2nR} induces a distribution on
the input codewords, which in turn induces a distribution over the input
alphabet. This speciﬁes a joint distribution on W →Xn(W) →Y n →ˆW.
To relate probability of error and mutual information, we can apply Fano’s
inequality to obtain
H(W| ˆW) ≤1 + nRP (n)
e
= nϵn,
(9.37)


## PDF page 295

9.2
CONVERSE TO THE CODING THEOREM FOR GAUSSIAN CHANNELS
269
where ϵn →0 as P (n)
e
→0. Hence,
nR = H(W) = I (W; ˆW) + H(W| ˆW)
(9.38)
≤I (W; ˆW) + nϵn
(9.39)
≤I (Xn; Y n) + nϵn
(9.40)
= h(Y n) −h(Y n|Xn) + nϵn
(9.41)
= h(Y n) −h(Zn) + nϵn
(9.42)
≤
n

i=1
h(Yi) −h(Zn) + nϵn
(9.43)
=
n

i=1
h(Yi) −
n

i=1
h(Zi) + nϵn
(9.44)
=
n

i=1
I (Xi; Yi) + nϵn.
(9.45)
Here Xi = xi(W), where W is drawn according to the uniform distribution
on {1, 2, . . . , 2nR}. Now let Pi be the average power of the ith column of
the codebook, that is,
Pi =
1
2nR

w
x2
i (w).
(9.46)
Then, since Yi = Xi + Zi and since Xi and Zi are independent, the aver-
age power EYi2 of Yi is Pi + N. Hence, since entropy is maximized by
the normal distribution,
h(Yi) ≤1
2 log 2πe(Pi + N).
(9.47)
Continuing with the inequalities of the converse, we obtain
nR ≤

(h(Yi) −h(Zi)) + nϵn
(9.48)
≤
 1
2 log(2πe(Pi + N)) −1
2 log 2πeN

+ nϵn
(9.49)
=
 1
2 log

1 + Pi
N

+ nϵn.
(9.50)


## PDF page 296

270
GAUSSIAN CHANNEL
Since each of the codewords satisﬁes the power constraint, so does their
average, and hence
1
n

i
Pi ≤P.
(9.51)
Since f (x) = 1
2 log(1 + x) is a concave function of x, we can apply
Jensen’s inequality to obtain
1
n
n

i=1
1
2 log

1 + Pi
N

≤1
2 log

1 + 1
n
n

i=1
Pi
N

(9.52)
≤1
2 log

1 + P
N

.
(9.53)
Thus R ≤1
2 log(1 + P
N ) + ϵn, ϵn →0, and we have the required converse.
Note that the power constraint enters the standard proof in (9.46).
9.3
BANDLIMITED CHANNELS
A common model for communication over a radio network or a telephone
line is a bandlimited channel with white noise. This is a continuous-
time channel. The output of such a channel can be described as the
convolution
Y(t) = (X(t) + Z(t)) ∗h(t),
(9.54)
where X(t) is the signal waveform, Z(t) is the waveform of the white
Gaussian noise, and h(t) is the impulse response of an ideal bandpass
ﬁlter, which cuts out all frequencies greater than W. In this section we
give simpliﬁed arguments to calculate the capacity of such a channel.
We begin with a representation theorem due to Nyquist [396] and Shan-
non [480], which shows that sampling a bandlimited signal at a sampling
rate
1
2W is sufﬁcient to reconstruct the signal from the samples. Intuitively,
this is due to the fact that if a signal is bandlimited to W, it cannot change
by a substantial amount in a time less than half a cycle of the maximum
frequency in the signal, that is, the signal cannot change very much in
time intervals less than
1
2W seconds.


