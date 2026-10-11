# A Mathematical Theory of Communication

Source ID: C05
Authors: Claude E. Shannon
Source URL: https://www.princeton.edu/~wbialek/rome/refs/shannon_48.pdf
DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x
Identity: Corrected reprint of the two-part Bell System Technical Journal article, 1948. Reprint pagination differs from journal pagination.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 49

1. R.M.S. criterion.
v
=
x(t
)
y(t
)
2
:
In this very commonly used measure of ﬁdelity the distance function
(x;y) is (apart from a constant
factor) the square of the ordinary Euclidean distance between the points x and y in the associated
function space.
(x;y)
= 1
T
Z T
0

x(t
)
y(t
)
2 dt
:
2. Frequency weighted R.M.S. criterion. More generally one can apply different weights to the different
frequency components before using an R.M.S. measure of ﬁdelity. This is equivalent to passing the
difference x(t
)
 y(t
) through a shaping ﬁlter and then determining the average power in the output.
Thus let
e(t
)
= x(t
)
y(t
)
and
f
(t
)
=
Z ∞
∞e(
)k
(t

)d

then
(x;y)
= 1
T
Z T
0
f
(t
)2 dt
:
3. Absolute error criterion.
(x;y)
= 1
T
Z T
0

x(t
)
y(t
)

dt
:
4. The structure of the ear and brain determine implicitly an evaluation, or rather a number of evaluations,
appropriate in the case of speech or music transmission. There is, for example, an “intelligibility”
criterion in which
(x;y) is equal to the relative frequency of incorrectly interpreted words when
message x(t
) is received as y(t
). Although we cannot give an explicit representation of
(x;y) in these
cases it could, in principle, be determined by sufﬁcient experimentation. Some of its properties follow
from well-known experimental results in hearing, e.g., the ear is relatively insensitive to phase and the
sensitivity to amplitude and frequency is roughly logarithmic.
5. The discrete case can be considered as a specialization in which we have tacitly assumed an evaluation
based on the frequency of errors. The function
(x;y) is then deﬁned as the number of symbols in the
sequence y differing from the corresponding symbols in x divided by the total number of symbols in
x.
28. THE RATE FOR A SOURCE RELATIVE TO A FIDELITY EVALUATION
We are now in a position to deﬁne a rate of generating information for a continuous source. We are given
P(x) for the source and an evaluation v determined by a distance function
(x;y) which will be assumed
continuous in both x and y. With a particular system P(x;y) the quality is measured by
v
=
Z
Z
(x;y)P(x;y)dxdy
:
Furthermore the rate of ﬂow of binary digits corresponding to P(x;y) is
R
=
Z
Z
P(x;y)log P(x;y)
P(x)P(y) dxdy
:
We deﬁne the rate R1 of generating information for a given quality v1 of reproduction to be the minimum of
R when we keep v ﬁxed at v1 and vary Px
(y). That is:
R1
= Min
Px
(y)
Z
Z
P(x;y)log P(x;y)
P(x)P(y) dxdy
49


## PDF page 50

subject to the constraint:
v1
=
Z
Z
P(x;y)(x;y)dxdy
:
This means that we consider, in effect, all the communication systems that might be used and that
transmit with the required ﬁdelity. The rate of transmission in bits per second is calculated for each one
and we choose that having the least rate. This latter rate is the rate we assign the source for the ﬁdelity in
question.
The justiﬁcation of this deﬁnition lies in the following result:
Theorem 21: If a source has a rate R1 for a valuation v1 it is possible to encode the output of the source
and transmit it over a channel of capacity C with ﬁdelity as near v1 as desired provided R1
 C. This is not
possible if R1
> C.
The last statement in the theorem follows immediately from the deﬁnition of R1 and previous results. If
it were not true we could transmit more than C bits per second over a channel of capacity C. The ﬁrst part
of the theorem is proved by a method analogous to that used for Theorem 11. We may, in the ﬁrst place,
divide the
(x;y) space into a large number of small cells and represent the situation as a discrete case. This
will not change the evaluation function by more than an arbitrarily small amount (when the cells are very
small) because of the continuity assumed for
(x;y). Suppose that P1
(x;y) is the particular system which
minimizes the rate and gives R1. We choose from the high probability y’s a set at random containing
2
(R1
+)T
members where

! 0 as T
! ∞. With large T each chosen point will be connected by a high probability
line (as in Fig. 10) to a set of x’s. A calculation similar to that used in proving Theorem 11 shows that with
large T almost all x’s are covered by the fans from the chosen y points for almost all choices of the y’s. The
communication system to be used operates as follows: The selected points are assigned binary numbers.
When a message x is originated it will (with probability approaching 1 as T
! ∞) lie within at least one
of the fans. The corresponding binary number is transmitted (or one of them chosen arbitrarily if there are
several) over the channel by suitable coding means to give a small probability of error. Since R1
 C this is
possible. At the receiving point the corresponding y is reconstructed and used as the recovered message.
The evaluation v
0
1 for this system can be made arbitrarily close to v1 by taking T sufﬁciently large.
This is due to the fact that for each long sample of message x(t
) and recovered message y(t
) the evaluation
approaches v1 (with probability 1).
It is interesting to note that, in this system, the noise in the recovered message is actually produced by a
kind of general quantizing at the transmitter and not produced by the noise in the channel. It is more or less
analogous to the quantizing noise in PCM.
29. THE CALCULATION OF RATES
The deﬁnition of the rate is similar in many respects to the deﬁnition of channel capacity. In the former
R
= Min
Px
(y)
Z
Z
P(x;y)log P(x;y)
P(x)P(y) dxdy
with P(x) and v1
=
Z
Z
P(x;y)(x;y)dxdy ﬁxed. In the latter
C
= Max
P (x)
Z
Z
P(x;y)log P(x;y)
P(x)P(y) dxdy
with Px
(y) ﬁxed and possibly one or more other constraints (e.g., an average power limitation) of the form
K
=
R
R P(x;y)(x;y)dxdy.
A partial solution of the general maximizing problem for determining the rate of a source can be given.
Using Lagrange’s method we consider
Z
Z

P(x;y)log P(x;y)
P(x)P(y)
+
P(x;y)(x;y)
+

(x)P(x;y)

dxdy
:
50


## PDF page 51

The variational equation (when we take the ﬁrst variation on P(x;y)) leads to
Py
(x)
= B(x)e
(x;y)
where
 is determined to give the required ﬁdelity and B(x) is chosen to satisfy
Z
B(x)e
(x;y) dx
= 1 :
This shows that, with best encoding, the conditional probability of a certain cause for various received
y, Py
(x) will decline exponentially with the distance function
(x;y) between the x and y in question.
In the special case where the distance function
(x;y) depends only on the (vector) difference between x
and y,
(x;y)
=
(x
y)
we have
Z
B(x)e
(xy) dx
= 1 :
Hence B(x) is constant, say
, and
Py
(x)
=
e
(xy)
:
Unfortunately these formal solutions are difﬁcult to evaluate in particular cases and seem to be of little value.
In fact, the actual calculation of rates has been carried out in only a few very simple cases.
If the distance function
(x;y) is the mean square discrepancy between x and y and the message ensemble
is white noise, the rate can be determined. In that case we have
R
= Min

H
(x)
Hy
(x)

= H
(x)
MaxHy
(x)
with N
=
(x
y)2. But the MaxHy
(x) occurs when y
x is a white noise, and is equal to W1 log2 eN where
W1 is the bandwidth of the message ensemble. Therefore
R
= W1 log2 eQ
W1log2 eN
= W1 log Q
N
where Q is the average message power. This proves the following:
Theorem 22: The rate for a white noise source of power Q and band W1 relative to an R.M.S. measure
of ﬁdelity is
R
= W1 log Q
N
where N is the allowed mean square error between original and recovered messages.
More generally with any message source we can obtain inequalities bounding the rate relative to a mean
square error criterion.
Theorem 23: The rate for any source of band W1 is bounded by
W1 log Q1
N
 R
 W1 log Q
N
where Q is the average power of the source, Q1 its entropy power and N the allowed mean square error.
The lower bound follows from the fact that the MaxHy
(x) for a given
(x
y)2
= N occurs in the white
noise case. The upper bound results if we place points (used in the proof of Theorem 21) not in the best way
but at random in a sphere of radius
pQ
N.
51


## PDF page 52

ACKNOWLEDGMENTS
The writer is indebted to his colleagues at the Laboratories, particularly to Dr. H. W. Bode, Dr. J. R. Pierce,
Dr. B. McMillan, and Dr. B. M. Oliver for many helpful suggestions and criticisms during the course of this
work. Credit should also be given to Professor N. Wiener, whose elegant solution of the problems of ﬁltering
and prediction of stationary ensembles has considerably inﬂuenced the writer’s thinking in this ﬁeld.
APPENDIX 5
Let S1 be any measurable subset of the g ensemble, and S2 the subset of the f ensemble which gives S1
under the operation T. Then
S1
= TS2
:
Let H
 be the operator which shifts all functions in a set by the time
. Then
H
S1
= H
TS2
= TH
S2
since T is invariant and therefore commutes with H
. Hence if m[S
] is the probability measure of the set S
m[H
S1
]
= m[TH
S2
]
= m[H
S2
]
= m[S2
]
= m[S1
]
where the second equality is by deﬁnition of measure in the g space, the third since the f ensemble is
stationary, and the last by deﬁnition of g measure again.
To prove that the ergodic property is preserved under invariant operations, let S1 be a subset of the g
ensemble which is invariant under H
, and let S2 be the set of all functions f which transform into S1. Then
H
S1
= H
TS2
= TH
S2
= S1
so that H
S2 is included in S2 for all
. Now, since
m[H
S2
]
= m[S1
]
this implies
H
S2
= S2
for all
 with m[S2
]
= 0 ;1. This contradiction shows that S1 does not exist.
APPENDIX 6
The upper bound, N3
 N1
+N2, is due to the fact that the maximum possible entropy for a power N1
+N2
occurs when we have a white noise of this power. In this case the entropy power is N1
+N2.
To obtain the lower bound, suppose we have two distributions in n dimensions p (xi
) and q (xi
) with
entropy powers N1 and N2. What form should p and q have to minimize the entropy power N3 of their
convolution r
(xi
):
r
(xi
)
=
Z
p (yi
)q (xi
yi
)dyi
:
The entropy H3 of r is given by
H3
=
Z
r
(xi
)logr
(xi
)dxi
:
We wish to minimize this subject to the constraints
H1
=
Z
p (xi
)log p (xi
)dxi
H2
=
Z
q (xi
)logq (xi
)dxi
:
52


## PDF page 53

We consider then
U
=
Z

r
(x)logr
(x)
+
p (x)log p (x)
+
q (x)logq (x)

dx
U
=
Z

[1
+logr
(x)]r
(x)
+
[1
+log p (x)]p (x)
+
[1
+logq (x)]q (x)

dx:
If p (x) is varied at a particular argument xi
= si, the variation in r
(x) is
r
(x)
= q (xi
si
)
and
U
=
Z
q (xi
si
)logr
(xi
)dxi
log p (si
)
= 0
and similarly when q is varied. Hence the conditions for a minimum are
Z
q (xi
si
)logr
(xi
)dxi
=
log p (si
)
Z
p (xi
si
)logr
(xi
)dxi
=
logq (si
):
If we multiply the ﬁrst by p (si
) and the second by q (si
) and integrate with respect to si we obtain
H3
=
H1
H3
=
H2
or solving for
 and
 and replacing in the equations
H1
Z
q (xi
si
)logr
(xi
)dxi
=
H3 log p (si
)
H2
Z
p (xi
si
)logr
(xi
)dxi
=
H3 logq (si
):
Now suppose p (xi
) and q (xi
) are normal
p (xi
)
=
jAij
jn =2
(2 
)n =2 exp
 1
2 ∑Aijxixj
q (xi
)
=
jBij
jn =2
(2 
)n =2 exp
 1
2 ∑Bijxixj
:
Then r
(xi
) will also be normal with quadratic form Cij. If the inverses of these forms are aij, bij, cij then
cij
= aij
+bij
:
We wish to show that these functions satisfy the minimizing conditions if and only if aij
= Kbij and thus
give the minimum H3 under the constraints. First we have
logr
(xi
)
= n
2 log 1
2 
jCij
j
 1
2 ∑Cijxixj
Z
q (xi
si
)logr
(xi
)dxi
= n
2 log 1
2 
jCij
j
 1
2 ∑Cijsisj
 1
2 ∑Cijbij
:
This should equal
H3
H1
n
2 log 1
2 
jAij
j
 1
2 ∑Aijsisj

which requires Aij
= H1
H3
Cij. In this case Aij
= H1
H2
Bij and both equations reduce to identities.
53


## PDF page 54

APPENDIX 7
The following will indicate a more general and more rigorous approach to the central deﬁnitions of commu-
nication theory. Consider a probability measure space whose elements are ordered pairs
(x;y). The variables
x, y are to be identiﬁed as the possible transmitted and received signals of some long duration T. Let us call
the set of all points whose x belongs to a subset S1 of x points the strip over S1, and similarly the set whose
y belong to S2 the strip over S2. We divide x and y into a collection of non-overlapping measurable subsets
Xi and Yi approximate to the rate of transmission R by
R1
= 1
T ∑
i
P(Xi
;Yi
)log P(Xi
;Yi
)
P(Xi
)P(Yi
)
where
P(Xi
)
is the probability measure of the strip over Xi
P(Yi
)
is the probability measure of the strip over Yi
P(Xi
;Yi
)
is the probability measure of the intersection of the strips
:
A further subdivision can never decrease R1. For let X1 be divided into X1
= X
0
1
+X
0
0
1 and let
P(Y1
)
= a
P(X1
)
= b
+c
P(X
0
1
)
= b
P(X
0
1
;Y1
)
= d
P(X
0
0
1
)
= c
P(X
0
0
1
;Y1
)
= e
P(X1
;Y1
)
= d
+e
:
Then in the sum we have replaced (for the X1, Y1 intersection)
(d
+e)log
d
+e
a (b
+c)
by
d log d
ab
+elog e
ac
:
It is easily shown that with the limitation we have on b, c, d, e,
d
+e
b
+c
d
+e
 ddee
bdce
and consequently the sum is increased. Thus the various possible subdivisions form a directed set, with
R monotonic increasing with reﬁnement of the subdivision. We may deﬁne R unambiguously as the least
upper bound for R1 and write it
R
= 1
T
Z
Z
P(x;y)log P(x;y)
P(x)P(y) dxdy
:
This integral, understood in the above sense, includes both the continuous and discrete cases and of course
many others which cannot be represented in either form. It is trivial in this formulation that if x and u are
in one-to-one correspondence, the rate from u to y is equal to that from x to y. If v is any function of y (not
necessarily with an inverse) then the rate from x to y is greater than or equal to that from x to v since, in
the calculation of the approximations, the subdivisions of y are essentially a ﬁner subdivision of those for
v. More generally if y and v are related not functionally but statistically, i.e., we have a probability measure
space
(y
;v), then R(x;v)
 R(x;y). This means that any operation applied to the received signal, even though
it involves statistical elements, does not increase R.
Another notion which should be deﬁned precisely in an abstract formulation of the theory is that of
“dimension rate,” that is the average number of dimensions required per second to specify a member of
an ensemble. In the band limited case 2W numbers per second are sufﬁcient. A general deﬁnition can be
framed as follows. Let f

(t
) be an ensemble of functions and let
T
[f

(t
); f

(t
)] be a metric measuring
54


## PDF page 55

the “distance” from f
 to f
 over the time T (for example the R.M.S. discrepancy over this interval.) Let
N
(;

;T
) be the least number of elements f which can be chosen such that all elements of the ensemble
apart from a set of measure
 are within the distance
 of at least one of those chosen. Thus we are covering
the space to within
 apart from a set of small measure
. We deﬁne the dimension rate
 for the ensemble
by the triple limit

= Lim

!0 Lim
!0 Lim
T
!∞
logN
(;

;T
)
T log

:
This is a generalization of the measure type deﬁnitions of dimension in topology, and agrees with the intu-
itive dimension rate for simple ensembles where the desired result is obvious.
55


