# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 305

9.5
CHANNELS WITH COLORED GAUSSIAN NOISE
279
Now the problem is reduced to maximizing |A + | subject to a trace
constraint tr(A) ≤nP .
Now we apply Hadamard’s inequality, mentioned in Chapter 8. Hada-
mard’s inequality states that the determinant of any positive deﬁnite matrix
K is less than the product of its diagonal elements, that is,
|K| ≤
"
i
Kii
(9.92)
with equality iff the matrix is diagonal. Thus,
|A + | ≤
"
i
(Aii + λi)
(9.93)
with equality iff A is diagonal. Since A is subject to a trace constraint,
1
n

i
Aii ≤P,
(9.94)
and Aii ≥0, the maximum value of #
i(Aii + λi) is attained when
Aii + λi = ν.
(9.95)
However, given the constraints, it may not always be possible to satisfy
this equation with positive Aii. In such cases, we can show by the standard
Kuhn–Tucker conditions that the optimum solution corresponds to setting
Aii = (ν −λi)+,
(9.96)
where the water level ν is chosen so that  Aii = nP . This value of A
maximizes the entropy of Y and hence the mutual information. We can
use Figure 9.4 to see the connection between the methods described above
and water-ﬁlling.
Consider a channel in which the additive Gaussian noise is a stochas-
tic process with ﬁnite-dimensional covariance matrix K(n)
Z . If the process
is stationary, the covariance matrix is Toeplitz and the density of eigen-
values on the real line tends to the power spectrum of the stochastic
process [262]. In this case, the above water-ﬁlling argument translates to
water-ﬁlling in the spectral domain.
Hence, for channels in which the noise forms a stationary stochastic
process, the input signal should be chosen to be a Gaussian process with
a spectrum that is large at frequencies where the noise spectrum is small.


## PDF page 306

280
GAUSSIAN CHANNEL
F(w)
w
FIGURE 9.5. Water-ﬁlling in the spectral domain.
This is illustrated in Figure 9.5. The capacity of an additive Gaussian
noise channel with noise power spectrum N(f ) can be shown to be [233]
C =
 π
−π
1
2 log

1 + (ν −N(f ))+
N(f )

df,
(9.97)
where ν is chosen so that
$
(ν −N(f ))+ df = P .
9.6
GAUSSIAN CHANNELS WITH FEEDBACK
In Chapter 7 we proved that feedback does not increase the capacity for
discrete memoryless channels, although it can help greatly in reducing
the complexity of encoding or decoding. The same is true of an additive
noise channel with white noise. As in the discrete case, feedback does not
increase capacity for memoryless Gaussian channels.
However, for channels with memory, where the noise is correlated
from time instant to time instant, feedback does increase capacity. The
capacity without feedback can be calculated using water-ﬁlling, but we do
not have a simple explicit characterization of the capacity with feedback.
In this section we describe an expression for the capacity in terms of the
covariance matrix of the noise Z. We prove a converse for this expression
for capacity. We then derive a simple bound on the increase in capacity
due to feedback.
The Gaussian channel with feedback is illustrated in Figure 9.6. The
output of the channel Yi is
Yi = Xi + Zi,
Zi ∼N(0, K(n)
Z ).
(9.98)


## PDF page 307

9.6
GAUSSIAN CHANNELS WITH FEEDBACK
281
Zi
Yi
Xi
FIGURE 9.6. Gaussian channel with feedback.
The feedback allows the input of the channel to depend on the past values
of the output.
A (2nR, n) code for the Gaussian channel with feedback consists of
a sequence of mappings xi(W, Y i−1), where W ∈{1, 2, . . . , 2nR} is the
input message and Y i−1 is the sequence of past values of the output. Thus,
x(W, ·) is a code function rather than a codeword. In addition, we require
that the code satisfy a power constraint,
E
%
1
n
n

i=1
x2
i (w, Y i−1)
&
≤P,
w ∈{1, 2, . . . , 2nR},
(9.99)
where the expectation is over all possible noise sequences.
We characterize the capacity of the Gaussian channel is terms of the
covariance matrices of the input X and the noise Z. Because of the feed-
back, Xn and Zn are not independent; Xi depends causally on the past
values of Z. In the next section we prove a converse for the Gaussian
channel with feedback and show that we achieve capacity if we take X
to be Gaussian.
We now state an informal characterization of the capacity of the channel
with and without feedback.
1. With feedback. The capacity Cn,FB in bits per transmission of the
time-varying Gaussian channel with feedback is
Cn,FB =
max
1
ntr(K(n)
X )≤P
1
2n log |K(n)
X+Z|
|K(n)
Z |
,
(9.100)


## PDF page 308

282
GAUSSIAN CHANNEL
where the maximization is taken over all Xn of the form
Xi =
i−1

j=1
bijZj + Vi,
i = 1, 2, . . . , n,
(9.101)
and V n is independent of Zn. To verify that the maximization over
(9.101) involves no loss of generality, note that the distribution on
Xn + Zn achieving the maximum entropy is Gaussian. Since Zn is
also Gaussian, it can be veriﬁed that a jointly Gaussian distribu-
tion on (Xn, Zn, Xn + Zn) achieves the maximization in (9.100).
But since Zn = Y n −Xn, the most general jointly normal causal
dependence of Xn on Y n is of the form (9.101), where V n plays the
role of the innovations process. Recasting (9.100) and (9.101) using
X = BZ + V and Y = X + Z, we can write
Cn,FB = max 1
2n log |(B + I)K(n)
Z (B + I)t + KV |
|K(n)
Z |
,
(9.102)
where the maximum is taken over all nonnegative deﬁnite KV and
strictly lower triangular B such that
tr(BK(n)
Z Bt + KV ) ≤nP.
(9.103)
Note that B is 0 if feedback is not allowed.
2. Without feedback. The capacity Cn of the time-varying Gaussian
channel without feedback is given by
Cn =
max
1
ntr(K(n)
X )≤P
1
2n log |K(n)
X + K(n)
Z |
|K(n)
Z |
.
(9.104)
This reduces to water-ﬁlling on the eigenvalues {λ(n)
i } of K(n)
Z . Thus,
Cn = 1
2n
n

i=1
log

1 + (λ −λ(n)
i )+
λ(n)
i

,
(9.105)
where (y)+ = max{y, 0} and where λ is chosen so that
n

i=1
(λ −λ(n)
i )+ = nP.
(9.106)


## PDF page 309

9.6
GAUSSIAN CHANNELS WITH FEEDBACK
283
We now prove an upper bound for the capacity of the Gaussian channel
with feedback. This bound is actually achievable [136], and is therefore
the capacity, but we do not prove this here.
Theorem 9.6.1
For a Gaussian channel with feedback, the rate Rn for
any sequence of (2nRn, n) codes with P (n)
e
→0 satisﬁes
Rn ≤Cn,FB + ϵn,
(9.107)
with ϵn →0 as n →∞, where Cn,FB is deﬁned in (9.100).
Proof:
Let W be uniform over 2nR, and therefore the probability of error
P (n)
e
is bounded by Fano’s inequality,
H(W| ˆW) ≤1 + nRnP (n)
e
= nϵn,
(9.108)
where ϵn →0 as P (n)
e
→0. We can then bound the rate as follows:
nRn = H(W)
(9.109)
= I (W; ˆW) + H(W| ˆW)
(9.110)
≤I (W; ˆW) + nϵn
(9.111)
≤I (W; Y n) + nϵn
(9.112)
=

I (W; Yi|Y i−1) + nϵn
(9.113)
(a)
=
 
h(Yi|Y i−1) −h(Yi|W, Y i−1, Xi, Xi−1, Zi−1)

+ nϵn
(9.114)
(b)
=
 
h(Yi|Y i−1) −h(Zi|W, Y i−1, Xi, Xi−1, Zi−1)

+ nϵn
(9.115)
(c)
=
 
h(Yi|Y i−1) −h(Zi|Zi−1)

+ nϵn
(9.116)
= h(Y n) −h(Zn) + nϵn,
(9.117)
where (a) follows from the fact that Xi is a function of W and the past
Yi’s, and Zi−1 is Y i−1 −Xi−1, (b) follows from Yi = Xi + Zi and the
fact that h(X + Z|X) = h(Z|X), and (c) follows from the fact Zi and
(W, Y i−1, Xi) are conditionally independent given Zi−1. Continuing the


## PDF page 310

284
GAUSSIAN CHANNEL
chain of inequalities after dividing by n, we have
Rn ≤1
n

h(Y n) −h(Zn)

+ ϵn
(9.118)
≤1
2n log |K(n)
Y |
|K(n)
Z |
+ ϵn
(9.119)
≤Cn,FB + ϵn,
(9.120)
by the entropy maximizing property of the normal.
□
We have proved an upper bound on the capacity of the Gaussian chan-
nel with feedback in terms of the covariance matrix K(n)
X+Z. We now derive
bounds on the capacity with feedback in terms of K(n)
X
and K(n)
Z , which
will then be used to derive bounds in terms of the capacity without feed-
back. For simplicity of notation, we will drop the superscript n in the
symbols for covariance matrices.
We ﬁrst prove a series of lemmas about matrices and determinants.
Lemma 9.6.1
Let X and Z be n-dimensional random vectors. Then
KX+Z + KX−Z = 2KX + 2KZ.
(9.121)
Proof
KX+Z = E(X + Z)(X + Z)t
(9.122)
= EXXt + EXZt + EZXt + EZZt
(9.123)
= KX + KXZ + KZX + KZ.
(9.124)
Similarly,
KX−Z = KX −KXZ −KZX + KZ.
(9.125)
Adding these two equations completes the proof.
□
Lemma 9.6.2
For two n × n nonnegative deﬁnite matrices A and B, if
A −B is nonnegative deﬁnite, then |A| ≥|B|.
Proof:
Let C = A −B. Since B and C are nonnegative deﬁnite, we
can consider them as covariance matrices. Consider two independent nor-
mal random vectors X1 ∼N(0, B) and X2 ∼N(0, C). Let Y = X1 + X2.


## PDF page 311

9.6
GAUSSIAN CHANNELS WITH FEEDBACK
285
Then
h(Y) ≥h(Y|X2)
(9.126)
= h(X1|X2)
(9.127)
= h(X1),
(9.128)
where the inequality follows from the fact that conditioning reduces dif-
ferential entropy, and the ﬁnal equality from the fact that X1 and X2 are
independent. Substituting the expressions for the differential entropies of
a normal random variable, we obtain
1
2 log(2πe)n|A| > 1
2 log(2πe)n|B|,
(9.129)
which is equivalent to the desired lemma.
□
Lemma 9.6.3
For two n-dimensional random vectors X and Z,
|KX+Z| ≤2n|KX + KZ|.
(9.130)
Proof:
From Lemma 9.6.1,
2(KX + KZ) −KX+Z = KX−Z ⪰0,
(9.131)
where A ⪰0 means that A is nonnegative deﬁnite. Hence, applying
Lemma 9.6.2, we have
|KX+Z| ≤|2(KX + KZ)| = 2n|KX + KZ|,
(9.132)
which is the desired result.
□
Lemma 9.6.4
For A,B nonnegative deﬁnite matrices and 0 ≤λ ≤1,
|λA + (1 −λ)B| ≥|A|λ|B|1−λ.
(9.133)
Proof:
Let X ∼Nn(0, A) and Y ∼Nn(0, B). Let Z be the mixture ran-
dom vector
Z =
!
X
if θ = 1
Y
if θ = 2,
(9.134)


## PDF page 312

286
GAUSSIAN CHANNEL
where
θ =
!
1
with probability λ
2
with probability 1 −λ.
(9.135)
Let X, Y, and θ be independent. Then
KZ = λA + (1 −λ)B.
(9.136)
We observe that
1
2 ln(2πe)n|λA + (1 −λ)B| ≥h(Z)
(9.137)
≥h(Z|θ)
(9.138)
= λh(X) + (1 −λ)h(Y)
(9.139)
= 1
2 ln(2πe)n|A|λ|B|1−λ,
(9.140)
which proves the result. The ﬁrst inequality follows from the entropy
maximizing property of the Gaussian under the covariance constraint. □
Deﬁnition
We say that a random vector Xn is causally related to Zn if
f (xn, zn) = f (zn)
n
"
i=1
f (xi|xi−1, zi−1).
(9.141)
Note that the feedback codes necessarily yield causally related (Xn, Zn).
Lemma 9.6.5
If Xn and Zn are causally related, then
h(Xn −Zn) ≥h(Zn)
(9.142)
and
|KX−Z| ≥|KZ|,
(9.143)
where KX−Z and KZ are the covariance matrices of Xn −Zn and Zn,
respectively.
Proof:
We have
h(Xn −Zn)
(a)
=
n

i=1
h(Xi −Zi|Xi−1 −Zi−1)
(9.144)


