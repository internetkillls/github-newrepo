# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 601

15.8
SOURCE CODING WITH SIDE INFORMATION
575
3. Assuming that si is decoded correctly at the receiver, the receiver
constructs a list Ł(y(i −1)) of indices that the receiver considers to
be jointly typical with y(i −1) in the (i −1)th block. The receiver
then declares ˆwi−1 = w as the index sent in block i −1 if there is
a unique w in Ssi ∩Ł(y(i −1)). If n is sufﬁciently large and if
R < I (X; Y|X1) + R0,
(15.255)
then ˆwi−1 = wi−1 with arbitrarily small probability of error. Com-
bining the two constraints (15.254) and (15.255), R0 drops out,
leaving
R < I (X; Y|X1) + I (X1; Y) = I (X, X1; Y).
(15.256)
For a detailed analysis of the probability of error, the reader is
referred to Cover and El Gamal [127].
□
Theorem 15.7.2 can also shown to be the capacity for the following
classes of relay channels:
1. Reversely degraded relay channel, that is,
p(y, y1|x, x1) = p(y|x, x1)p(y1|y, x1).
(15.257)
2. Relay channel with feedback
3. Deterministic relay channel,
y1 = f (x, x1),
y = g(x, x1).
(15.258)
15.8
SOURCE CODING WITH SIDE INFORMATION
We now consider the distributed source coding problem where two random
variables X and Y are encoded separately but only X is to be recovered.We
now ask how many bits R1 are required to describe X if we are allowed
R2 bits to describe Y. If R2 > H(Y), then Y can be described perfectly,
and by the results of Slepian–Wolf coding, R1 = H(X|Y) bits sufﬁce
to describe X. At the other extreme, if R2 = 0, we must describe X
without any help, and R1 = H(X) bits are then necessary to describe X. In
general, we use R2 = I (Y; ˆY) bits to describe an approximate version of
Y. This will allow us to describe X using H(X| ˆY) bits in the presence of
side information ˆY. The following theorem is consistent with this intuition.


## PDF page 602

576
NETWORK INFORMATION THEORY
Theorem 15.8.1
Let (X, Y) ∼p(x, y). If Y is encoded at rate R2 and
X is encoded at rate R1, we can recover X with an arbitrarily small prob-
ability of error if and only if
R1 ≥H(X|U),
(15.259)
R2 ≥I (Y; U)
(15.260)
for some joint probability mass function p(x, y)p(u|y), where |U| ≤
|Y| + 2.
We prove this theorem in two parts. We begin with the converse, in
which we show that for any encoding scheme that has a small probability
of error, we can ﬁnd a random variable U with a joint probability mass
function as in the theorem.
Proof:
(Converse). Consider any source code for Figure 15.32. The
source code consists of mappings fn(Xn) and gn(Y n) such that the rates of
fn and gn are less than R1 and R2, respectively, and a decoding mapping
hn such that
P (n)
e
= Pr{hn(fn(Xn), gn(Y n)) ̸= Xn} < ϵ.
(15.261)
Deﬁne new random variables S = fn(Xn) and T = gn(Y n). Then since
we can recover Xn from S and T with low probability of error, we have,
by Fano’s inequality,
H(Xn|S, T ) ≤nϵn.
(15.262)
Then
nR2
(a)
≥H(T )
(15.263)
(b)
≥I (Y n; T )
(15.264)
Encoder
Decoder
Encoder
X
X
R1
R2
Y
^
FIGURE 15.32. Encoding with side information.


## PDF page 603

15.8
SOURCE CODING WITH SIDE INFORMATION
577
=
n

i=1
I (Yi; T |Y1, . . . , Yi−1)
(15.265)
(c)
=
n

i=1
I (Yi; T, Y1, . . . , Yi−1)
(15.266)
(d)
=
n

i=1
I (Yi; Ui)
(15.267)
where
(a) follows from the fact that the range of gn is {1, 2, . . . , 2nR2}
(b) follows from the properties of mutual information
(c) follows from the chain rule and the fact that Yi is independent of
Y1, . . . , Yi−1 and hence I (Yi; Y1, . . . , Yi−1) = 0
(d) follows if we deﬁne Ui = (T, Y1, . . . , Yi−1)
We also have another chain for R1,
nR1
(a)
≥H(S)
(15.268)
(b)
≥H(S|T )
(15.269)
= H(S|T ) + H(Xn|S, T ) −H(Xn|S, T )
(15.270)
(c)
≥H(Xn, S|T ) −nϵn
(15.271)
(d)
= H(Xn|T ) −nϵn
(15.272)
(e)
=
n

i=1
H(Xi|T, X1, . . . , Xi−1) −nϵn
(15.273)
(f)
≥
n

i=1
H(Xi|T, Xi−1, Y i−1) −nϵn
(15.274)
(g)
=
n

i=1
H(Xi|T, Y i−1) −nϵn
(15.275)
(h)
=
n

i=1
H(Xi|Ui) −nϵn,
(15.276)


## PDF page 604

578
NETWORK INFORMATION THEORY
where
(a) follows from the fact that the range of S is {1, 2, . . . , 2nR1}
(b) follows from the fact that conditioning reduces entropy
(c) follows from Fano’s inequality
(d) follows from the chain rule and the fact that S is a function of Xn
(e) follows from the chain rule for entropy
(f) follows from the fact that conditioning reduces entropy
(g) follows from the (subtle) fact that Xi →(T, Y i−1) →Xi−1 forms
a Markov chain since Xi does not contain any information about
Xi−1 that is not there in Y i−1 and T
(h) follows from the deﬁnition of U
Also, since Xi contains no more information about Ui than is present
in Yi, it follows that Xi →Yi →Ui forms a Markov chain. Thus we have
the following inequalities:
R1 ≥1
n
n

i=1
H(Xi|Ui),
(15.277)
R2 ≥1
n
n

i=1
I (Yi; Ui).
(15.278)
We now introduce a timesharing random variable Q so that we can rewrite
these equations as
R1 ≥1
n
n

i=1
H(Xi|Ui, Q = i) = H(XQ|UQ, Q),
(15.279)
R2 ≥1
n
n

i=1
I (Yi; Ui|Q = i) = I (YQ; UQ|Q).
(15.280)
Now since Q is independent of YQ (the distribution of Yi does not depend
on i), we have
I (YQ; UQ|Q) = I (YQ; UQ, Q) −I (YQ; Q) = I (YQ; UQ, Q). (15.281)
Now XQ and YQ have the joint distribution p(x, y) in the theorem. Deﬁn-
ing U = (UQ, Q), X = XQ, and Y = YQ, we have shown the existence
of a random variable U such that
R1 ≥H(X|U),
(15.282)
R2 ≥I (Y; U)
(15.283)


## PDF page 605

15.8
SOURCE CODING WITH SIDE INFORMATION
579
for any encoding scheme that has a low probability of error. Thus, the
converse is proved.
□
Before we proceed to the proof of the achievability of this pair of rates,
we will need a new lemma about strong typicality and Markov chains.
Recall the deﬁnition of strong typicality for a triple of random variables
X, Y, and Z. A triplet of sequences xn, yn, zn is said to be ϵ-strongly
typical if
				
1
nN(a, b, c|xn, yn, zn) −p(a, b, c)
				 <
ϵ
|X||Y||Z|.
(15.284)
In particular, this implies that (xn, yn) are jointly strongly typical and
that (yn, zn) are also jointly strongly typical. But the converse is not true:
The fact that (xn, yn) ∈A∗(n)
ϵ
(X, Y) and (yn, zn) ∈A∗(n)
ϵ
(Y, Z) does not
in general imply that (xn, yn, zn) ∈A∗(n)
ϵ
(X, Y, Z). But if X →Y →Z
forms a Markov chain, this implication is true. We state this as a lemma
without proof [53, 149].
Lemma 15.8.1
Let (X, Y, Z) form a Markov chain X →Y →Z [i.e.,
p(x, y, z) = p(x, y)p(z|y)]. If for a given (yn, zn) ∈A∗(n)
ϵ
(Y, Z), Xn is
drawn ∼
n
i=1 p(xi|yi), then Pr{(Xn, yn, zn) ∈A∗(n)
ϵ
(X, Y, Z)} > 1 −ϵ
for n sufﬁciently large.
Remark
The theorem is true from the strong law of large numbers if
Xn ∼
n
i=1 p(xi|yi, zi). The Markovity of X →Y →Z is used to show
that Xn ∼p(xi|yi) is sufﬁcient for the same conclusion.
We now outline the proof of achievability in Theorem 15.8.1.
Proof:
(Achievability in Theorem 15.8.1). Fix p(u|y). Calculate p(u) =

y p(y)p(u|y).
Generation of codebooks: Generate 2nR2 independent codewords of
length n, U(w2), w2 ∈{1, 2, . . . , 2nR2} according to 
n
i=1 p(ui). Ran-
domly bin all the Xn sequences into 2nR1 bins by independently generating
an index b distributed uniformly on {1, 2, . . . , 2nR1} for each Xn. Let B(i)
denote the set of Xn sequences allotted to bin i.
Encoding: The X sender sends the index i of the bin in which Xn falls.
The Y sender looks for an index s such that (Y n, U n(s)) ∈A∗(n)
ϵ
(Y, U).
If there is more than one such s, it sends the least. If there is no such
U n(s) in the codebook, it sends s = 1.
Decoding: The receiver looks for a unique Xn ∈B(i) such that (Xn,
U n(s)) ∈A∗(n)
ϵ
(X, U). If there is none or more than one, it declares an
error.


## PDF page 606

580
NETWORK INFORMATION THEORY
Analysis of the probability of error: The various sources of error are as
follows:
1. The pair (Xn, Y n) generated by the source is not typical. The proba-
bility of this is small if n is large. Hence, without loss of generality,
we can condition on the event that the source produces a particular
typical sequence (xn, yn) ∈A∗(n)
ϵ
.
2. The sequence Y n is typical, but there does not exist a U n(s) in the
codebook that is jointly typical with it. The probability of this is
small from the arguments of Section 10.6, where we showed that if
there are enough codewords; that is, if
R2 > I (Y; U),
(15.285)
we are very likely to ﬁnd a codeword that is jointly strongly typical
with the given source sequence.
3. The codeword U n(s) is jointly typical with yn but not with xn. But
by Lemma 15.8.1, the probability of this is small since X →Y →U
forms a Markov chain.
4. We also have an error if there exists another typical Xn ∈B(i) which
is jointly typical with U n(s). The probability that any other Xn is
jointly typical with U n(s) is less than 2−n(I(U;X)−3ϵ), and therefore
the probability of this kind of error is bounded above by
|B(i) ∩A∗(n)
ϵ
(X)|2−n(I(X;U)−3ϵ) ≤2n(H(X)+ϵ)2−nR12−n(I(X;U)−3ϵ),
(15.286)
which goes to 0 if R1 > H(X|U).
Hence, it is likely that the actual source sequence Xn is jointly typical
with U n(s) and that no other typical source sequence in the same bin is
also jointly typical with U n(s). We can achieve an arbitrarily low proba-
bility of error with an appropriate choice of n and ϵ, and this completes
the proof of achievability.
□
15.9
RATE DISTORTION WITH SIDE INFORMATION
We know that R(D) bits are sufﬁcient to describe X within distortion D.
We now ask how many bits are required given side information Y.
We begin with a few deﬁnitions. Let (Xi, Yi) be i.i.d. ∼p(x, y) and
encoded as shown in Figure 15.33.


## PDF page 607

15.9
RATE DISTORTION WITH SIDE INFORMATION
581
Encoder
Decoder
X
X
Ed (X,X ) = D
R
Y
^
^
FIGURE 15.33. Rate distortion with side information.
Deﬁnition
The rate distortion function with side information RY(D)
is deﬁned as the minimum rate required to achieve distortion D if the
side information Y is available to the decoder. Precisely, RY(D) is the
inﬁmum of rates R such that there exist maps in : Xn →{1, . . . , 2nR},
gn : Yn × {1, . . . , 2nR} →
ˆXn such that
lim sup
n→∞
Ed(Xn, gn(Y n, in(Xn))) ≤D.
(15.287)
Clearly, since the side information can only help, we have RY(D) ≤
R(D). For the case of zero distortion, this is the Slepian–Wolf problem
and we will need H(X|Y) bits. Hence, RY(0) = H(X|Y). We wish to
determine the entire curve RY(D). The result can be expressed in the
following theorem.
Theorem 15.9.1
(Rate distortion with side information (Wyner and Ziv))
Let
(X, Y)
be
drawn
i.i.d.
∼p(x, y)
and
let
d(xn, ˆxn)
= 1
n
n
i=1 d(xi, ˆxi) be given. The rate distortion function with side infor-
mation is
RY(D) = min
p(w|x) min
f
(I (X; W) −I (Y; W))
(15.288)
where the minimization is over all functions f : Y × W →ˆX and condi-
tional probability mass functions p(w|x), |W| ≤|X| + 1, such that

x

w

y
p(x, y)p(w|x)d(x, f (y, w)) ≤D.
(15.289)
The function f in the theorem corresponds to the decoding map that
maps the encoded version of the X symbols and the side information Y to
the output alphabet. We minimize over all conditional distributions on W
and functions f such that the expected distortion for the joint distribution
is less than D.
We ﬁrst prove the converse after considering some of the properties of
the function RY(D) deﬁned in (15.288).


## PDF page 608

582
NETWORK INFORMATION THEORY
Lemma 15.9.1
The rate distortion function with side information
RY(D) deﬁned in (15.288) is a nonincreasing convex function of D.
Proof:
The monotonicity of RY(D) follows immediately from the fact
that the domain of minimization in the deﬁnition of RY(D) increases with
D. As in the case of rate distortion without side information, we expect
RY(D) to be convex. However, the proof of convexity is more involved
because of the double rather than single minimization in the deﬁnition of
RY(D) in (15.288). We outline the proof here.
Let D1 and D2 be two values of the distortion and let W1, f1 and
W2, f2 be the corresponding random variables and functions that achieve
the minima in the deﬁnitions of RY(D1) and RY(D2), respectively. Let
Q be a random variable independent of X, Y, W1, and W2 which takes on
the value 1 with probability λ and the value 2 with probability 1 −λ.
Deﬁne W = (Q, WQ) and let f (W, Y) = fQ(WQ, Y). Speciﬁcally,
f (W, Y) = f1(W1, Y) with probability λ and f (W, Y) = f2(W2, Y) with
probability 1 −λ. Then the distortion becomes
D = Ed(X, ˆX)
(15.290)
= λEd(X, f1(W1, Y)) + (1 −λ)Ed(X, f2(W2, Y))
(15.291)
= λD1 + (1 −λ)D2,
(15.292)
and (15.288) becomes
I (W; X) −I (W; Y) = H(X) −H(X|W) −H(Y) + H(Y|W)
(15.293)
= H(X) −H(X|WQ, Q) −H(Y) + H(Y|WQ, Q)
(15.294)
= H(X) −λH(X|W1) −(1 −λ)H(X|W2)
−H(Y) + λH(Y|W1) + (1 −λ)H(Y|W2)
(15.295)
= λ (I (W1, X) −I (W1; Y))
+ (1 −λ) (I (W2, X) −I (W2; Y)) , (15.296)
and hence
RY(D) =
min
U:Ed≤D (I (U; X) −I (U; Y))
(15.297)
≤I (W; X) −I (W; Y)
(15.298)


