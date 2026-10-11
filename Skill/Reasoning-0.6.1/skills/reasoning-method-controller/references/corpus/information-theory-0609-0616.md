# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 609

15.9
RATE DISTORTION WITH SIDE INFORMATION
583
= λ (I (W1, X) −I (W1; Y)) + (1 −λ) (I (W2, X) −I (W2; Y))
= λRY(D1) + (1 −λ)RY(D2),
(15.299)
proving the convexity of RY(D).
□
We are now in a position to prove the converse to the conditional rate
distortion theorem.
Proof:
(Converse to Theorem 15.9.1). Consider any rate distortion code
with side information. Let the encoding function be fn : Xn →{1, 2, . . . ,
2nR}. Let the decoding function be gn : Yn × {1, 2, . . . , 2nR} →
ˆXn, and
let gni : Yn × {1, 2, . . . , 2nR} →ˆX denote the ith symbol produced by the
decoding function. Let T = fn(Xn) denote the encoded version of Xn.
We must show that if Ed(Xn, gn(Y n, fn(Xn))) ≤D, then R ≥RY(D).
We have the following chain of inequalities:
nR
(a)
≥H(T )
(15.300)
(b)
≥H(T |Y n)
(15.301)
≥I (Xn; T |Y n)
(15.302)
(c)
=
n

i=1
I (Xi; T |Y n, Xi−1)
(15.303)
=
n

i=1
H(Xi|Y n, Xi−1) −H(Xi|T, Y n, Xi−1)
(15.304)
(d)
=
n

i=1
H(Xi|Yi) −H(Xi|T, Y i−1, Yi, Y n
i+1, Xi−1)
(15.305)
(e)
≥
n

i=1
H(Xi|Yi) −H(Xi|T, Y i−1, Yi, Y n
i+1)
(15.306)
(f)
=
n

i=1
H(Xi|Yi) −H(Xi|Wi, Yi)
(15.307)
(g)
=
n

i=1
I (Xi; Wi|Yi)
(15.308)


## PDF page 610

584
NETWORK INFORMATION THEORY
=
n

i=1
H(Wi|Yi) −H(Wi|Xi, Yi)
(15.309)
(h)
=
n

i=1
H(Wi|Yi) −H(Wi|Xi)
(15.310)
=
n

i=1
H(Wi) −H(Wi|Xi) −H(Wi) + H(Wi|Yi)
(15.311)
=
n

i=1
I (Wi; Xi) −I (Wi; Yi)
(15.312)
(i)≥
n

i=1
RY(Ed(Xi, g′
ni(Wi, Yi)))
(15.313)
= n1
n
n

i=1
RY(Ed(Xi, g′
ni(Wi, Yi)))
(15.314)
(j)
≥nRY

1
n
n

i=1
Ed(Xi, g′
ni(Wi, Yi))

(15.315)
(k)
≥nRY (D) ,
(15.316)
where
(a) follows from the fact that the range of T is {1, 2, . . . , 2nR}
(b) follows from the fact that conditioning reduces entropy
(c) follows from the chain rule for mutual information
(d) follows from the fact that Xi is independent of the past and future
Y’s and X’s given Yi
(e) follows from the fact that conditioning reduces entropy
(f) follows by deﬁning Wi = (T, Y i−1, Y n
i+1)
(g) follows from the deﬁnition of mutual information
(h) follows from the fact that since Yi depends only on Xi and is condi-
tionally independent of T and the past and future Y’s, Wi →Xi →
Yi forms a Markov chain
(i) follows
from
the deﬁnition
of the (information)
conditional
rate
distortion
function
since
ˆXi = gni(T, Y n)
△= g′
ni(Wi, Yi),
and
hence
I (Wi; Xi) −I (Wi; Yi) ≥minW:Ed(X, ˆX)≤Di I (W; X) −
I (W; Y) = RY(Di)


## PDF page 611

15.9
RATE DISTORTION WITH SIDE INFORMATION
585
(j) follows from Jensen’s inequality and the convexity of the conditional
rate distortion function (Lemma 15.9.1)
(k) follows from the deﬁnition of D = E[ 1
n
n
i=1 d(Xi, ˆXi)]
□
It is easy to see the parallels between this converse and the converse
for rate distortion without side information (Section 10.4). The proof of
achievability is also parallel to the proof of the rate distortion theorem
using strong typicality. However, instead of sending the index of the
codeword that is jointly typical with the source, we divide these codewords
into bins and send the bin index instead. If the number of codewords in
each bin is small enough, the side information can be used to isolate
the particular codeword in the bin at the receiver. Hence again we are
combining random binning with rate distortion encoding to ﬁnd a jointly
typical reproduction codeword. We outline the details of the proof below.
Proof:
(Achievability of Theorem 15.9.1). Fix p(w|x) and the function
f (w, y). Calculate p(w) = 
x p(x)p(w|x).
Generation of codebook: Let R1 = I (X; W) + ϵ. Generate 2nR i.i.d.
codewords W n(s) ∼
n
i=1 p(wi), and index them by s ∈{1, 2, . . . , 2nR1}.
Let R2 = I (X; W) −I (Y; W) + 5ϵ. Randomly assign the indices s ∈
{1, 2, . . . , 2nR1} to one of 2nR2 bins using a uniform distribution over
the bins. Let B(i) denote the indices assigned to bin i. There are approx-
imately 2n(R1−R2) indices in each bin.
Encoding: Given a source sequence Xn, the encoder looks for a code-
word W n(s) such that (Xn, W n(s)) ∈A∗(n)
ϵ
. If there is no such W n, the
encoder sets s = 1. If there is more than one such s, the encoder uses the
lowest s. The encoder sends the index of the bin in which s belongs.
Decoding: The decoder looks for a W n(s) such that s ∈B(i) and
(W n(s), Y n) ∈A∗(n)
ϵ
. If he ﬁnds a unique s, he then calculates ˆXn, where
ˆXi = f (Wi, Yi). If he does not ﬁnd any such s or more than one such s,
he sets ˆXn = ˆxn, where ˆxn is an arbitrary sequence in
ˆXn. It does not
matter which default sequence is used; we will show that the probability
of this event is small.
Analysis of the probability of error: As usual, we have various error
events:
1. The pair (Xn, Y n) /∈A∗(n)
ϵ
. The probability of this event is small for
large enough n by the weak law of large numbers.
2. The sequence Xn is typical, but there does not exist an s such that
(Xn, W n(s)) ∈A∗(n)
ϵ
. As in the proof of the rate distortion theorem,


## PDF page 612

586
NETWORK INFORMATION THEORY
the probability of this event is small if
R1 > I (W; X).
(15.317)
3. The pair of sequences (Xn, W n(s)) ∈A∗(n)
ϵ
but (W n(s), Y n) /∈A∗(n)
ϵ
(i.e., the codeword is not jointly typical with the Y n sequence). By
the Markov lemma (Lemma 15.8.1), the probability of this event is
small if n is large enough.
4. There exists another s′ with the same bin index such that (W n(s′),
Y n) ∈A∗(n)
ϵ
. Since the probability that a randomly chosen W n is
jointly typical with Y n is ≈2−nI(Y;W), the probability that there is
another W n in the same bin that is typical with Y n is bounded by
the number of codewords in the bin times the probability of joint
typicality, that is,
Pr(∃s′ ∈B(i) : (W n(s′), Y n) ∈A∗(n)
ϵ
) ≤2n(R1−R2)2−n(I(W;Y)−3ϵ),
(15.318)
which goes to zero since R1 −R2 < I (Y; W) −3ϵ.
5. If the index s is decoded correctly, (Xn, W n(s)) ∈A∗(n)
ϵ
. By item 1
we can assume that (Xn, Y n) ∈A∗(n)
ϵ
. Thus, by the Markov lemma,
we have (Xn, Y n, W n) ∈A∗(n)
ϵ
and therefore the empirical joint dis-
tribution is close to the original distribution p(x, y)p(w|x) that we
started with, and hence (Xn, ˆXn) will have a joint distribution that
is close to the distribution that achieves distortion D.
Hence with high probability, the decoder will produce ˆXn such that the
distortion between Xn and ˆXn is close to nD. This completes the proof
of the theorem.
□
The reader is referred to Wyner and Ziv [574] for details of the proof.
After the discussion of the various situations of compressing distributed
data, it might be expected that the problem is almost completely solved,
but unfortunately, this is not true. An immediate generalization of all
the above problems is the rate distortion problem for correlated sources,
illustrated in Figure 15.34. This is essentially the Slepian–Wolf problem
with distortion in both X and Y. It is easy to see that the three dis-
tributed source coding problems considered above are all special cases
of this setup. Unlike the earlier problems, though, this problem has not
yet
been
solved
and
the
general
rate
distortion
region
remains
unknown.


## PDF page 613

15.10
GENERAL MULTITERMINAL NETWORKS
587
Xn
(Xn, Yn)
Encoder 1
i(xn) ∈ 2nR1
j(yn) ∈ 2nR2
Decoder
Yn
Encoder 2
^
^
FIGURE 15.34. Rate distortion for two correlated sources.
15.10
GENERAL MULTITERMINAL NETWORKS
We conclude this chapter by considering a general multiterminal network
of senders and receivers and deriving some bounds on the rates achievable
for communication in such a network. A general multiterminal network
is illustrated in Figure 15.35. In this section, superscripts denote node
indices and subscripts denote time indices. There are m nodes, and node
i has an associated transmitted variable X(i) and a received variable Y (i).
S
Sc
(X(1),Y (1))
(X (m),Y (m))
FIGURE 15.35. General multiterminal network.


## PDF page 614

588
NETWORK INFORMATION THEORY
The node i sends information at rate R(ij) to node j. We assume that all
the messages W (ij) being sent from node i to node j are independent and
uniformly distributed over their respective ranges {1, 2, . . . , 2nR(ij)}.
The
channel
is
represented
by
the
channel
transition
function
p(y(1), . . . , y(m)|x(1), . . . , x(m)), which is the conditional probability mass
function of the outputs given the inputs. This probability transition func-
tion captures the effects of the noise and the interference in the network.
The channel is assumed to be memoryless (i.e., the outputs at any time
instant depend only the current inputs and are conditionally independent
of the past inputs).
Corresponding to each transmitter–receiver node pair is a message
W (ij) ∈{1, 2, . . . , 2nR(ij)}. The input symbol X(i) at node i depends on
W (ij), j ∈{1, . . . , m} and also on the past values of the received symbol
Y (i) at node i. Hence, an encoding scheme of block length n consists of
a set of encoding and decoding functions, one for each node:
• Encoders: X(i)
k (W (i1), W (i2), . . . , W (im), Y (i)
1 , Y (i)
2 , . . . , Y (i)
k−1), k = 1,
. . . , n. The encoder maps the messages and past received symbols
into the symbol X(i)
k
transmitted at time k.
• Decoders: ˆW (ji) 
Y (i)
1 , . . . , Y (i)
n , W (i1), . . . , W (im)
, j = 1, 2, . . . , m.
The decoder j at node i maps the received symbols in each block and
his own transmitted information to form estimates of the messages
intended for him from node j, j = 1, 2, . . . , m.
Associated with every pair of nodes is a rate and a corresponding
probability of error that the message will not be decoded correctly,
P (n)
e
(ij) = Pr
 ˆW (ij) 
Y(j), W (j1), . . . , W (jm)
̸= W (ij)
,
(15.319)
where P (n)
e
(ij) is deﬁned under the assumption that all the messages are
independent and distributed uniformly over their respective ranges.
A set of rates {R(ij)} is said to be achievable if there exist encoders and
decoders with block length n with P (n)
e
(ij) →0 as n →∞for all i, j ∈
{1, 2, . . . , m}. We use this formulation to derive an upper bound on the
ﬂow of information in any multiterminal network. We divide the nodes
into two sets, S and the complement Sc. We now bound the rate of ﬂow
of information from nodes in S to nodes in Sc. See [514]


## PDF page 615

15.10
GENERAL MULTITERMINAL NETWORKS
589
Theorem 15.10.1
If the information rates {R(ij)} are achievable, there
exists some joint probability distribution p(x(1), x(2), . . . , x(m)) such that

i∈S,j∈Sc
R(ij) ≤I (X(S); Y (Sc)|X(Sc))
(15.320)
for all S ⊂{1, 2, . . . , m}. Thus, the total rate of ﬂow of information across
cut sets is bounded by the conditional mutual information.
Proof:
The proof follows the same lines as the proof of the converse
for the multiple access channel. Let T = {(i, j) : i ∈S, j ∈Sc} be the set
of links that cross from S to Sc, and let T c be all the other links in the
network. Then
n

i∈S,j∈Sc
R(ij)
(15.321)
(a)
=

i∈S,j∈Sc
H

W (ij)
(15.322)
(b)
= H

W (T )
(15.323)
(c)
= H

W (T )|W (T c)
(15.324)
= I

W (T ); Y (Sc)
1
, . . . , Y (Sc)
n
|W (T c)
(15.325)
+ H

W (T )|Y (Sc)
1
, . . . , Y (Sc)
n
, W (T c)
(15.326)
(d)
≤I

W (T ); Y (Sc)
1
, . . . , Y (Sc)
n
|W (T c)
+ nϵn
(15.327)
(e)
=
n

k=1
I

W (T ); Y (Sc)
k
|Y (Sc)
1
, . . . , Y (Sc)
k−1 , W (T c)
+ nϵn
(15.328)
(f)
=
n

k=1
H

Y (Sc)
k
|Y (Sc)
1
, . . . , Y (Sc)
k−1 , W (T c)
−H

Y (Sc)
k
|Y (Sc)
1
, . . . , Y (Sc)
k−1 , W (T c), W (T )
+ nϵn
(15.329)


## PDF page 616

590
NETWORK INFORMATION THEORY
(g)
≤
n

k=1
H

Y (Sc)
k
|Y (Sc)
1
, . . . , Y (Sc)
k−1 , W (T c), X(Sc)
k

−H

Y (Sc)
k
|Y (Sc)
1
, . . . , Y (Sc)
k−1 , W (T c), W (T ), X(S)
k , X(Sc)
k

+ nϵn
(15.330)
(h)
≤
n

k=1
H

Y (Sc)
k
|X(Sc)
k

−H

Y (Sc)
k
|X(Sc)
k
, X(S)
k

+ nϵn
(15.331)
=
n

k=1
I

X(S)
k ; Y (Sc)
k
|X(Sc)
k

+ nϵn
(15.332)
(i)= n1
n
n

k=1
I

X(S)
Q ; Y (Sc)
Q
|X(Sc)
Q , Q = k

+ nϵn
(15.333)
(j)= nI

X(S)
Q ; Y (Sc)
Q
|X(Sc)
Q , Q

+ nϵn
(15.334)
= n

H

Y (Sc)
Q
|X(Sc)
Q , Q

−H

Y (Sc)
Q
|X(S)
Q , X(Sc)
Q , Q

+ nϵn (15.335)
(k)
≤n

H

Y (Sc)
Q
|X(Sc)
Q

−H

Y (Sc)
Q
|X(S)
Q , X(Sc)
Q , Q

+ nϵn
(15.336)
(l)= n

H

Y (Sc)
Q
|X(Sc)
Q

−H

Y (Sc)
Q
|X(S)
Q , X(Sc)
Q

+ nϵn
(15.337)
= nI

X(S)
Q ; Y (Sc)
Q
|X(Sc)
Q

+ nϵn,
(15.338)
where
(a) follows from the fact that the messages W (ij) are uniformly dis-
tributed over their respective ranges {1, 2, . . . , 2nR(ij)}
(b) follows from the deﬁnition of W (T ) = {W (ij) : i ∈S, j ∈Sc} and
the fact that the messages are independent
(c) follows from the independence of the messages for T and T c
(d) follows from Fano’s inequality since the messages W (T ) can be
decoded from Y (S) and W (T c)
(e) is the chain rule for mutual information
(f) follows from the deﬁnition of mutual information
(g) follows from the fact that X(Sc)
k
is a function of the past received
symbols Y (Sc) and the messages W (T c) and the fact that adding
conditioning reduces the second term


