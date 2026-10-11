# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 697

17.7
ENTROPY AND FISHER INFORMATION
671
Theorem 17.6.4
Let
f (n)
k
= 1
n
k
	

S:|S|=k
I (X(S); X(Sc))
k
.
(17.65)
Then
f (n)
1
≥f (n)
2
≥· · · ≥f (n)
n .
(17.66)
Proof:
The theorem follows from the identity I (X(S); X(Sc)) =
h(X(S)) −h(X(S)|X(Sc)) and Theorems 17.6.1 and 17.6.3.
□
17.7
ENTROPY AND FISHER INFORMATION
The differential entropy of a random variable is a measure of its descriptive
complexity. The Fisher information is a measure of the minimum error
in estimating a parameter of a distribution. In this section we derive a
relationship between these two fundamental quantities and use this to
derive the entropy power inequality.
Let X be any random variable with density f (x). We introduce a loca-
tion parameter θ and write the density in a parametric form as f (x −θ).
The Fisher information (Section 11.10) with respect to θ is given by
J(θ) =
 ∞
−∞
f (x −θ)
 ∂
∂θ ln f (x −θ)
2
dx.
(17.67)
In this case, differentiation with respect to x is equivalent to differentiation
with respect to θ. So we can write the Fisher information as
J(X) =
 ∞
−∞
f (x −θ)
 ∂
∂x ln f (x −θ)
2
dx
=
 ∞
−∞
f (x)
 ∂
∂x ln f (x)
2
dx,
(17.68)
which we can rewrite as
J(X) =
 ∞
−∞
f (x)
 ∂
∂x f (x)
f (x)
2
dx.
(17.69)
We will call this the Fisher information of the distribution of X. Notice
that like entropy, it is a function of the density.
The importance of Fisher information is illustrated in the following
theorem.


## PDF page 698

672
INEQUALITIES IN INFORMATION THEORY
Theorem 17.7.1
(Theorem 11.10.1: Cram´er–Rao inequality) The
mean-squared error of any unbiased estimator T (X) of the parameter θ is
lower bounded by the reciprocal of the Fisher information:
var(T ) ≥
1
J(θ).
(17.70)
We now prove a fundamental relationship between the differential
entropy and the Fisher information:
Theorem 17.7.2
(de Bruijn’s identity: entropy and Fisher information)
Let X be any random variable with a ﬁnite variance with a density f (x).
Let Z be an independent normally distributed random variable with zero
mean and unit variance. Then
∂
∂t he(X +
√
tZ) = 1
2J(X +
√
tZ),
(17.71)
where he is the differential entropy to base e. In particular, if the limit
exists as t →0,
∂
∂t he(X +
√
tZ)

t=0
= 1
2J(X).
(17.72)
Proof:
Let Yt = X + √tZ. Then the density of Yt is
gt(y) =
 ∞
−∞
f (x)
1
√
2πt
e−(y−x)2
2t
dx.
(17.73)
Then
∂
∂t gt(y) =
 ∞
−∞
f (x) ∂
∂t

1
√
2πt
e−(y−x)2
2t

dx
(17.74)
=
 ∞
−∞
f (x)

−1
2t
1
√
2πt
e−(y−x)2
2t
+(y −x)2
2t2
1
√
2πt
e−(y−x)2
2t

dx.
(17.75)
We also calculate
∂
∂y gt(y) =
 ∞
−∞
f (x)
1
√
2πt
∂
∂y

e−(y−x)2
2t

dx
(17.76)
=
 ∞
−∞
f (x)
1
√
2πt

−y −x
t
e−(y−x)2
2t

dx
(17.77)


## PDF page 699

17.7
ENTROPY AND FISHER INFORMATION
673
and
∂2
∂y2 gt(y) =
 ∞
−∞
f (x)
1
√
2πt
∂
∂y

−y −x
t
e−(y−x)2
2t

dx
(17.78)
=
 ∞
−∞
f (x)
1
√
2πt

−1
t e−(y−x)2
2t
+ (y −x)2
t2
e−(y−x)2
2t

dx.
(17.79)
Thus,
∂
∂t gt(y) = 1
2
∂2
∂y2 gt(y).
(17.80)
We will use this relationship to calculate the derivative of the entropy of
Yt, where the entropy is given by
he(Yt) = −
 ∞
−∞
gt(y) ln gt(y) dy.
(17.81)
Differentiating, we obtain
∂
∂t he(Yt) = −
 ∞
−∞
∂
∂t gt(y) dy −
 ∞
−∞
∂
∂t gt(y) ln gt(y) dy
(17.82)
= −∂
∂t
 ∞
−∞
gt(y) dy −1
2
 ∞
−∞
∂2
∂y2 gt(y) ln gt(y) dy. (17.83)
The ﬁrst term is zero since

gt(y) dy = 1. The second term can be inte-
grated by parts to obtain
∂
∂t he(Yt) = −1
2
∂gt(y)
∂y
ln gt(y)
∞
−∞
+ 1
2
 ∞
−∞
 ∂
∂y gt(y)
2
1
gt(y) dy.
(17.84)
The second term in (17.84) is 1
2J(Yt). So the proof will be complete if
we show that the ﬁrst term in (17.84) is zero. We can rewrite the ﬁrst
term as
∂gt(y)
∂y
ln gt(y) =

∂gt(y)
∂y
√gt(y)

2

gt(y) ln

gt(y)

.
(17.85)
The square of the ﬁrst factor integrates to the Fisher information and
hence must be bounded as y →±∞. The second factor goes to zero since
x ln x →0 as x →0 and gt(y) →0 as y →±∞. Hence, the ﬁrst term in


## PDF page 700

674
INEQUALITIES IN INFORMATION THEORY
(17.84) goes to 0 at both limits and the theorem is proved. In the proof, we
have exchanged integration and differentiation in (17.74), (17.76), (17.78),
and (17.82). Strict justiﬁcation of these exchanges requires the application
of the bounded convergence and mean value theorems; the details may
be found in Barron [30].
□
This theorem can be used to prove the entropy power inequality, which
gives a lower bound on the entropy of a sum of independent random
variables.
Theorem 17.7.3
(Entropy power inequality) If X and Y are indepen-
dent random n-vectors with densities, then
2
2
nh(X + Y) ≥2
2
nh(X) + 2
2
nh(Y) .
(17.86)
We outline the basic steps in the proof due to Stam [505] and Blachman
[61]. A different proof is given in Section 17.8.
Stam’s proof of the entropy power inequality is based on a perturbation
argument. Let n = 1. Let Xt = X + √f (t)Z1, Yt = Y + √g(t)Z2, where
Z1 and Z2 are independent N(0, 1) random variables. Then the entropy
power inequality for n = 1 reduces to showing that s(0) ≤1, where we
deﬁne
s(t) = 22h(Xt) + 22h(Yt)
22h(Xt+Yt)
.
(17.87)
If f (t) →∞and g(t) →∞as t →∞, it is easy to show that s(∞) = 1.
If, in addition, s′(t) ≥0 for t ≥0, this implies that s(0) ≤1. The proof
of the fact that s′(t) ≥0 involves a clever choice of the functions f (t)
and g(t), an application of Theorem 17.7.2 and the use of a convolution
inequality for Fisher information,
1
J(X + Y) ≥
1
J(X) +
1
J(Y).
(17.88)
The entropy power inequality can be extended to the vector case by
induction. The details may be found in the papers by Stam [505] and
Blachman [61].
17.8
ENTROPY POWER INEQUALITY AND
BRUNN–MINKOWSKI INEQUALITY
The entropy power inequality provides a lower bound on the differential
entropy of a sum of two independent random vectors in terms of their
individual differential entropies. In this section we restate and outline an


## PDF page 701

17.8
ENTROPY POWER INEQUALITY AND BRUNN–MINKOWSKI INEQUALITY
675
alternative proof of the entropy power inequality. We also show how the
entropy power inequality and the Brunn–Minkowski inequality are related
by means of a common proof.
We can rewrite the entropy power inequality for dimension n = 1 in
a form that emphasizes its relationship to the normal distribution. Let
X and Y be two independent random variables with densities, and let
X′ and Y ′ be independent normals with the same entropy as X and
Y, respectively. Then 22h(X) = 22h(X′) = (2πe)σ 2
X′ and similarly, 22h(Y) =
(2πe)σ 2
Y ′. Hence the entropy power inequality can be rewritten as
22h(X+Y) ≥(2πe)(σ 2
X′ + σ 2
Y ′) = 22h(X′+Y ′),
(17.89)
since X′ and Y ′ are independent. Thus, we have a new statement of the
entropy power inequality.
Theorem 17.8.1
(Restatement of the entropy power inequality)
For
two independent random variables X and Y,
h(X + Y) ≥h(X′ + Y ′),
(17.90)
where X′ and Y ′ are independent normal random variables with h(X′) =
h(X) and h(Y ′) = h(Y).
This form of the entropy power inequality bears a striking resemblance
to the Brunn–Minkowski inequality, which bounds the volume of set
sums.
Deﬁnition
The set sum A + B of two sets A, B ⊂Rn is deﬁned as the
set {x + y : x ∈A, y ∈B}.
Example 17.8.1
The set sum of two spheres of radius 1 is a sphere of
radius 2.
Theorem 17.8.2
(Brunn–Minkowski inequality)
The volume of the set
sum of two sets A and B is greater than the volume of the set sum of two
spheres A′ and B′ with the same volume as A and B, respectively:
V (A + B) ≥V (A′ + B′),
(17.91)
where A′ and B′ are spheres with V (A′) = V (A) and V (B′) = V (B).
The similarity between the two theorems was pointed out in [104].
A common proof was found by Dembo [162] and Lieb, starting from a


## PDF page 702

676
INEQUALITIES IN INFORMATION THEORY
strengthened version of Young’s inequality. The same proof can be used to
prove a range of inequalities which includes the entropy power inequality
and the Brunn–Minkowski inequality as special cases. We begin with a
few deﬁnitions.
Deﬁnition
Let f and g be two densities over Rn and let f ∗g denote
the convolution of the two densities. Let the Lr norm of the density be
deﬁned by
||f ||r =


f r(x) dx
 1
r
.
(17.92)
Lemma 17.8.1
(Strengthened Young’s inequality)
For any two densi-
ties f and g over Rn,
||f ∗g||r ≤

CpCq
Cr
n
2
||f ||p||g||q,
(17.93)
where
1
r = 1
p + 1
q −1
(17.94)
and
Cp = p
1
p
p′
1
p′
,
1
p + 1
p′ = 1.
(17.95)
Proof:
The proof of this inequality may be found in [38] and [73].
□
We deﬁne a generalization of the entropy.
Deﬁnition
The Renyi entropy hr(X) of order r is deﬁned as
hr(X) =
1
1 −r log

f r(x) dx

(17.96)
for 0 < r < ∞, r ̸= 1. If we take the limit as r →1, we obtain the Shan-
non entropy function,
h(X) = h1(X) = −

f (x) log f (x) dx.
(17.97)
If we take the limit as r →0, we obtain the logarithm of the volume of
the support set,
h0(X) = log (µ{x : f (x) > 0}) .
(17.98)


## PDF page 703

17.8
ENTROPY POWER INEQUALITY AND BRUNN–MINKOWSKI INEQUALITY
677
Thus, the zeroth-order Renyi entropy gives the logarithm of the measure
of the support set of the density f , and the Shannon entropy h1 gives the
logarithm of the size of the “effective” support set (Theorem 8.2.2). We
now deﬁne the equivalent of the entropy power for Renyi entropies.
Deﬁnition
The Renyi entropy power Vr(X) of order r is deﬁned as
Vr(X) =




f r(x) dx
−2
n
r′
r ,
0 < r ≤∞, r ̸= 1 , 1
r + 1
r′ = 1
exp [ 2
nh(X)],
r = 1
µ({x : f (x) > 0})
2
n ,
r = 0
(17.99)
Theorem 17.8.3
For two independent random variables X and Y and
any 0 ≤r < ∞and any 0 ≤λ ≤1, we have
log Vr(X + Y) ≥λ log Vp(X) + (1 −λ) log Vq(Y) + H(λ)
+1+r
1−r

H

r+λ(1−r)
1+r

−H
 r
1+r
	
,
(17.100)
where p =
r
(r+λ(1−r)), q =
r
(r+(1−λ)(1−r)) and H(λ) = −λ log λ −(1 −λ)
log(1 −λ).
Proof:
If we take the logarithm of Young’s inequality (17.93), we obtain
1
r′ log Vr(X + Y) ≥1
p′ log Vp(X) + 1
q′ log Vq(Y) + log Cr
−log Cp −log Cq.
(17.101)
Setting λ = r′/p′ and using (17.94), we have 1 −λ = r′/q′, p =
r
r+λ(1−r)
and q =
r
r+(1−λ)(1−r). Thus, (17.101) becomes
log Vr(X + Y) ≥λ log Vp(X) + (1 −λ) log Vq(Y) + r′
r log r −log r′
−r′
p log p + r′
p′ log p′ −r′
q log q + r′
q′ log q′
(17.102)
= λ log Vp(X) + (1 −λ) log Vq(Y)
+ r′
r log r −(λ + 1 −λ) log r′
−r′
p log p + λ log p′ −r′
q log q + (1 −λ) log q′
(17.103)


## PDF page 704

678
INEQUALITIES IN INFORMATION THEORY
= λ log Vp(X) + (1 −λ) log Vq(Y) +
1
r −1 log r + H(λ)
−r + λ(1 −r)
r −1
log
r
r + λ(1 −r)
−r + (1 −λ)(1 −r)
r −1
log
r
r + (1 −λ)(1 −r)
(17.104)
= λ log Vp(X) + (1 −λ) log Vq(Y) + H(λ)
+ 1 + r
1 −r

H

r + λ(1 −r)
1 + r

−H

r
1 + r

,
(17.105)
where the details of the algebra for the last step are omitted.
□
The Brunn–Minkowski inequality and the entropy power inequality
can then be obtained as special cases of this theorem.
• The entropy power inequality. Taking the limit of (17.100) as r →1
and setting
λ =
V1(X)
V1(X) + V1(Y),
(17.106)
we obtain
V1(X + Y) ≥V1(X) + V1(Y),
(17.107)
which is the entropy power inequality.
• The Brunn–Minkowski inequality. Similarly, letting r →0 and choos-
ing
λ =
√V0(X)
√V0(X) + √V0(Y),
(17.108)
we obtain

V0(X + Y) ≥

V0(X) +

V0(Y).
(17.109)
Now let A be the support set of X and B be the support set of Y.
Then A + B is the support set of X + Y, and (17.109) reduces to
[µ(A + B)]
1
n ≥[µ(A)]
1
n + [µ(B)]
1
n ,
(17.110)
which is the Brunn–Minkowski inequality.


