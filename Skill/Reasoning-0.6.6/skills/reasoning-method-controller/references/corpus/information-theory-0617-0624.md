# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 617

15.10
GENERAL MULTITERMINAL NETWORKS
591
(h) follows from the fact that Y (Sc)
k
depends only on the current input
symbols X(S)
k
and X(Sc)
k
(i) follows after we introduce a new timesharing random variable Q
distributed uniformly on {1, 2, . . . , n}
(j) follows from the deﬁnition of mutual information
(k) follows from the fact that conditioning reduces entropy
(l) follows from the fact that Y (Sc)
Q
depends only on the inputs X(S)
Q and
X(Sc)
Q
and is conditionally independent of Q
Thus, there exist random variables X(S) and X(Sc) with some arbitrary
joint distribution that satisfy the inequalities of the theorem.
□
The theorem has a simple max-ﬂow min-cut interpretation. The rate of
ﬂow of information across any boundary is less than the mutual informa-
tion between the inputs on one side of the boundary and the outputs on
the other side, conditioned on the inputs on the other side.
The problem of information ﬂow in networks would be solved if the
bounds of the theorem were achievable. But unfortunately, these bounds
are not achievable even for some simple channels. We now apply these
bounds to a few of the channels that we considered earlier.
• Multiple-access channel. The multiple access channel is a network
with many input nodes and one output node. For the case of a two-user
multiple-access channel, the bounds of Theorem 15.10.1 reduce to
R1 ≤I (X1; Y|X2),
(15.339)
R2 ≤I (X2; Y|X1),
(15.340)
R1 + R2 ≤I (X1, X2; Y)
(15.341)
for some joint distribution p(x1, x2)p(y|x1, x2). These bounds coin-
cide with the capacity region if we restrict the input distribution to
be a product distribution and take the convex hull (Theorem 15.3.1).
• Relay channel. For the relay channel, these bounds give the upper
bound of Theorem 15.7.1 with different choices of subsets as shown
in Figure 15.36. Thus,
C ≤sup
p(x,x1)
min {I (X, X1; Y), I (X; Y, Y1|X1)} .
(15.342)
This upper bound is the capacity of a physically degraded relay chan-
nel and for the relay channel with feedback [127].


## PDF page 618

592
NETWORK INFORMATION THEORY
X
Y1 : X1
Y
S1
S2
FIGURE 15.36. Relay channel.
p(y|x1, x2)
X1
X2
U
(U,V )
V
Y
^
^
FIGURE 15.37. Transmission of correlated sources over a multiple-access channel.
To complement our discussion of a general network, we should mention
two features of single-user channels that do not apply to a multiuser
network.
• Source–channel separation theorem. In Section 7.13 we discussed
the source–channel separation theorem, which proves that we can
transmit the source noiselessly over the channel if and only if the
entropy rate is less than the channel capacity. This allows us to char-
acterize a source by a single number (the entropy rate) and the channel
by a single number (the capacity). What about the multiuser case?
We would expect that a distributed source could be transmitted over
a channel if and only if the rate region for the noiseless coding of the
source lay within the capacity region of the channel. To be speciﬁc,
consider the transmission of a distributed source over a multiple-
access channel, as shown in Figure 15.37. Combining the results of
Slepian–Wolf encoding with the capacity results for the multiple-
access channel, we can show that we can transmit the source over
the channel and recover it with a low probability of error if
H(U|V ) ≤I (X1; Y|X2, Q),
(15.343)


## PDF page 619

15.10
GENERAL MULTITERMINAL NETWORKS
593
H(V |U) ≤I (X2; Y|X1, Q),
(15.344)
H(U, V ) ≤I (X1, X2; Y|Q)
(15.345)
for some distribution p(q)p(x1|q)p(x2|q)p(y|x1, x2). This condition
is equivalent to saying that the Slepian–Wolf rate region of the source
has a nonempty intersection with the capacity region of the multiple-
access channel.
But is this condition also necessary? No, as a simple example illus-
trates. Consider the transmission of the source of Example 15.4.2
over the binary erasure multiple-access channel (Example 15.3.3).
The Slepian–Wolf region does not intersect the capacity region, yet
it is simple to devise a scheme that allows the source to be transmit-
ted over the channel. We just let X1 = U and X2 = V , and the value
of Y will tell us the pair (U, V ) with no error. Thus, the conditions
(15.345) are not necessary.
The reason for the failure of the source–channel separation theorem
lies in the fact that the capacity of the multiple-access channel
increases with the correlation between the inputs of the channel.
Therefore, to maximize the capacity, one should preserve the cor-
relation between the inputs of the channel. Slepian–Wolf encoding,
on the other hand, gets rid of the correlation. Cover et al. [129] pro-
posed an achievable region for transmission of a correlated source
over a multiple access channel based on the idea of preserving the
correlation. Han and Costa [273] have proposed a similar region for
the transmission of a correlated source over a broadcast channel.
• Capacity regions with feedback. Theorem 7.12.1 shows that feedback
does not increase the capacity of a single-user discrete memoryless
channel. For channels with memory, on the other hand, feedback
enables the sender to predict something about the noise and to combat
it more effectively, thus increasing capacity.
What about multiuser channels? Rather surprisingly, feedback does
increase the capacity region of multiuser channels, even when the
channels are memoryless. This was ﬁrst shown by Gaarder and Wolf
[220], who showed how feedback helps increase the capacity of the
binary erasure multiple-access channel. In essence, feedback from the
receiver to the two senders acts as a separate channel between the two
senders. The senders can decode each other’s transmissions before the
receiver does. They then cooperate to resolve the uncertainty at the
receiver, sending information at the higher cooperative capacity rather
than the noncooperative capacity. Using this scheme, Cover and
Leung [133] established an achievable region for a multiple-access


## PDF page 620

594
NETWORK INFORMATION THEORY
channel with feedback. Willems [557] showed that this region was
the capacity for a class of multiple-access channels that included the
binary erasure multiple-access channel. Ozarow [410] established the
capacity region for a two-user Gaussian multiple-access channel. The
problem of ﬁnding the capacity region for a multiple-access channel
with feedback is closely related to the capacity of a two-way channel
with a common output.
There is as yet no uniﬁed theory of network information ﬂow. But there
can be no doubt that a complete theory of communication networks would
have wide implications for the theory of communication and computation.
SUMMARY
Multiple-access channel. The capacity of a multiple-access channel
(X1 × X2, p(y|x1, x2), Y) is the closure of the convex hull of all (R1, R2)
satisfying
R1 < I (X1; Y|X2),
(15.346)
R2 < I (X2; Y|X1),
(15.347)
R1 + R2 < I (X1, X2; Y)
(15.348)
for some distribution p1(x1)p2(x2) on X1 × X2.
The capacity region of the m-user multiple-access channel is the closure
of the convex hull of the rate vectors satisfying
R(S) ≤I (X(S); Y|X(Sc))
for all S ⊆{1, 2, . . . , m}
(15.349)
for some product distribution p1(x1)p2(x2) · · · pm(xm).
Gaussian multiple-access channel. The capacity region of a two-user
Gaussian multiple-access channel is
R1 ≤C
P1
N

,
(15.350)
R2 ≤C
P2
N

,
(15.351)


## PDF page 621

SUMMARY
595
R1 + R2 ≤C
P1 + P2
N

,
(15.352)
where
C(x) = 1
2 log(1 + x).
(15.353)
Slepian–Wolf coding. Correlated sources X and Y can be described
separately at rates R1 and R2 and recovered with arbitrarily low prob-
ability of error by a common decoder if and only if
R1 ≥H(X|Y),
(15.354)
R2 ≥H(Y|X),
(15.355)
R1 + R2 ≥H(X, Y).
(15.356)
Broadcast channels. The capacity region of the degraded broadcast
channel X →Y1 →Y2 is the convex hull of the closure of all (R1, R2)
satisfying
R2 ≤I (U; Y2),
(15.357)
R1 ≤I (X; Y1|U)
(15.358)
for some joint distribution p(u)p(x|u)p(y1, y2|x).
Relay channel. The capacity C of the physically degraded relay chan-
nel p(y, y1|x, x1) is given by
C = sup
p(x,x1)
min {I (X, X1; Y), I (X; Y1|X1)} ,
(15.359)
where the supremum is over all joint distributions on X × X1.
Source coding with side information. Let (X, Y) ∼p(x, y). If Y is
encoded at rate R2 and X is encoded at rate R1, we can recover X with
an arbitrarily small probability of error iff
R1 ≥H(X|U),
(15.360)
R2 ≥I (Y; U)
(15.361)
for some distribution p(y, u) such that X →Y →U.


## PDF page 622

596
NETWORK INFORMATION THEORY
Rate distortion with side information. Let (X, Y) ∼p(x, y). The
rate distortion function with side information is given by
RY(D) = min
p(w|x)
min
f :Y×W→ˆX
I (X; W) −I (Y; W),
(15.362)
where the minimization is over all functions f and conditional distri-
butions p(w|x), |W| ≤|X| + 1, such that

x

w

y
p(x, y)p(w|x)d(x, f (y, w)) ≤D.
(15.363)
PROBLEMS
15.1
Cooperative capacity of a multiple-access channel
p(y|x1, x2)
X1
X2
(W1,W2)
(W1,W2)
Y
^
^
(a) Suppose that X1 and X2 have access to both indices W1 ∈
{1, 2nR}, W2 ∈{1, 2nR2}.
Thus,
the
codewords
X1(W1,
W2), X2(W1, W2) depend on both indices. Find the capacity
region.
(b) Evaluate this region for the binary erasure multiple access
channel Y = X1 + X2, Xi ∈{0, 1}. Compare to the noncoop-
erative region.
15.2
Capacity of multiple-access channels.
Find the capacity region
for each of the following multiple-access channels:
(a) Additive modulo 2 multiple-access channel. X1 ∈{0, 1},
X2 ∈{0, 1}, Y = X1 ⊕X2.
(b) Multiplicative
multiple-access
channel.
X1 ∈{−1, 1},
X2 ∈{−1, 1}, Y = X1 · X2.


## PDF page 623

PROBLEMS
597
15.3
Cut-set interpretation of capacity region of multiple-access chan-
nel.
For the multiple-access channel we know that (R1, R2) is
achievable if
R1 < I (X1; Y | X2),
(15.364)
R2 < I (X2; Y | X1),
(15.365)
R1 + R2 < I (X1, X2; Y)
(15.366)
for X1, X2 independent. Show, for X1, X2 independent that
I (X1; Y | X2) = I (X1; Y, X2).
X1
Y
X2
S1
S2
S3
Interpret the information bounds as bounds on the rate of ﬂow
across cut sets S1, S2, and S3.
15.4
Gaussian multiple-access channel capacity.
For the AWGN
multiple-access channel, prove, using typical sequences, the
achievability of any rate pairs (R1, R2) satisfying
R1 < 1
2 log

1 + P1
N

,
(15.367)
R2 < 1
2 log

1 + P2
N

,
(15.368)
R1 + R2 < 1
2 log

1 + P1 + P2
N

.
(15.369)


## PDF page 624

598
NETWORK INFORMATION THEORY
The proof extends the proof for the discrete multiple-access chan-
nel in the same way as the proof for the single-user Gaussian
channel extends the proof for the discrete single-user channel.
15.5
Converse for the Gaussian multiple-access channel.
Prove the
converse for the Gaussian multiple-access channel by extending
the converse in the discrete case to take into account the power
constraint on the codewords.
15.6
Unusual
multiple-access
channel.
Consider
the
following
multiple-access channel: X1 = X2 = Y = {0, 1}. If (X1, X2) =
(0, 0), then Y = 0. If (X1, X2) = (0, 1), then Y = 1. If (X1, X2) =
(1, 0), then Y = 1. If (X1, X2) = (1, 1), then Y = 0 with proba-
bility 1
2 and Y = 1 with probability 1
2.
(a) Show that the rate pairs (1,0) and (0,1) are achievable.
(b) Show that for any nondegenerate distribution p(x1)p(x2), we
have I (X1, X2; Y) < 1.
(c) Argue that there are points in the capacity region of this
multiple-access channel that can only be achieved by time-
sharing; that is, there exist achievable rate pairs (R1, R2) that
lie in the capacity region for the channel but not in the region
deﬁned by
R1 ≤I (X1; Y|X2),
(15.370)
R2 ≤I (X2; Y|X1),
(15.371)
R1 + R2 ≤I (X1, X2; Y)
(15.372)
for any product distribution p(x1)p(x2). Hence the operation
of convexiﬁcation strictly enlarges the capacity region. This
channel was introduced independently by Csisz´ar and K¨orner
[149] and Bierbaum and Wallmeier [59].
15.7
Convexity of capacity region of broadcast channel.
Let C ⊆R2
be the capacity region of all achievable rate pairs R = (R1, R2)
for the broadcast channel. Show that C is a convex set by using
a time-sharing argument. Speciﬁcally, show that if R(1) and R(2)
are achievable, λR(1) + (1 −λ)R(2) is achievable for 0 ≤λ ≤1.
15.8
Slepian–Wolf for deterministically related sources.
Find and
sketch the Slepian–Wolf rate region for the simultaneous data
compression of (X, Y), where y = f (x) is some deterministic
function of x.


