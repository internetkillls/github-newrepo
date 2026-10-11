# A Mathematical Theory of Communication

Source ID: C05
Authors: Claude E. Shannon
Source URL: https://www.princeton.edu/~wbialek/rome/refs/shannon_48.pdf
DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x
Identity: Corrected reprint of the two-part Bell System Technical Journal article, 1948. Reprint pagination differs from journal pagination.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 33

3. The ensemble
f
(ai
;t
)
=
+∞
∑
n =∞
an
sin

(2Wt
n )

(2Wt
n )
with the ai normal and independent all with the same standard deviation
p
N. This is a representation
of “white” noise, band limited to the band from 0 to W cycles per second and with average power N.2
4. Let points be distributed on the t axis according to a Poisson distribution. At each selected point the
function f
(t
) is placed and the different functions added, giving the ensemble
∞
∑
k =∞
f
(t
+tk
)
where the tk are the points of the Poisson distribution. This ensemble can be considered as a type of
impulse or shot noise where all the impulses are identical.
5. The set of English speech functions with the probability measure given by the frequency of occurrence
in ordinary use.
An ensemble of functions f

(t
) is stationary if the same ensemble results when all functions are shifted
any ﬁxed amount in time. The ensemble
f

(t
)
= sin (t
+

)
is stationary if
 is distributed uniformly from 0 to 2 . If we shift each function by t1 we obtain
f

(t
+t1
)
= sin (t
+t1
+

)
= sin (t
+
')
with
' distributed uniformly from 0 to 2
. Each function has changed but the ensemble as a whole is
invariant under the translation. The other examples given above are also stationary.
An ensemble is ergodic if it is stationary, and there is no subset of the functions in the set with a
probability different from 0 and 1 which is stationary. The ensemble
sin (t
+

)
is ergodic. No subset of these functions of probability
= 0 ;1 is transformed into itself under all time trans-
lations. On the other hand the ensemble
asin (t
+

)
with a distributed normally and
 uniform is stationary but not ergodic. The subset of these functions with
a between 0 and 1 for example is stationary.
Of the examples given, 3 and 4 are ergodic, and 5 may perhaps be considered so. If an ensemble is
ergodic we may say roughly that each function in the set is typical of the ensemble. More precisely it is
known that with an ergodic ensemble an average of any statistic over the ensemble is equal (with probability
1) to an average over the time translations of a particular function of the set.3 Roughly speaking, each
function can be expected, as time progresses, to go through, with the proper frequency, all the convolutions
of any of the functions in the set.
2This representation can be used as a deﬁnition of band limited white noise. It has certain advantages in that it involves fewer
limiting operations than do deﬁnitions that have been used in the past. The name “white noise,” already ﬁrmly entrenched in the
literature, is perhaps somewhat unfortunate. In optics white light means either any continuous spectrum as contrasted with a point
spectrum, or a spectrum which is ﬂat with wavelength (which is not the same as a spectrum ﬂat with frequency).
3This is the famous ergodic theorem or rather one aspect of this theorem which was proved in somewhat different formulations
by Birkoff, von Neumann, and Koopman, and subsequently generalized by Wiener, Hopf, Hurewicz and others. The literature on
ergodic theory is quite extensive and the reader is referred to the papers of these writers for precise and general formulations; e.g.,
E. Hopf, “Ergodentheorie,” Ergebnisse der Mathematik und ihrer Grenzgebiete, v. 5; “On Causality Statistics and Probability,” Journal
of Mathematics and Physics, v. XIII, No. 1, 1934; N. Wiener, “The Ergodic Theorem,” Duke Mathematical Journal, v. 5, 1939.
33


## PDF page 34

Just as we may perform various operations on numbers or functions to obtain new numbers or functions,
we can perform operations on ensembles to obtain new ensembles. Suppose, for example, we have an
ensemble of functions f

(t
) and an operator T which gives for each function f

(t
) a resulting function
g

(t
):
g

(t
)
= T f

(t
):
Probability measure is deﬁned for the set g

(t
) by means of that for the set f

(t
). The probability of a certain
subset of the g

(t
) functions is equal to that of the subset of the f

(t
) functions which produce members of
the given subset of g functions under the operation T. Physically this corresponds to passing the ensemble
through some device, for example, a ﬁlter, a rectiﬁer or a modulator. The output functions of the device
form the ensemble g

(t
).
A device or operator T will be called invariant if shifting the input merely shifts the output, i.e., if
g

(t
)
= T f

(t
)
implies
g

(t
+t1
)
= T f

(t
+t1
)
for all f

(t
) and all t1. It is easily shown (see Appendix 5 that if T is invariant and the input ensemble is
stationary then the output ensemble is stationary. Likewise if the input is ergodic the output will also be
ergodic.
A ﬁlter or a rectiﬁer is invariant under all time translations. The operation of modulation is not since the
carrier phase gives a certain time structure. However, modulation is invariant under all translations which
are multiples of the period of the carrier.
Wiener has pointed out the intimate relation between the invariance of physical devices under time
translations and Fourier theory.4 He has shown, in fact, that if a device is linear as well as invariant Fourier
analysis is then the appropriate mathematical tool for dealing with the problem.
An ensemble of functions is the appropriate mathematical representation of the messages produced by
a continuous source (for example, speech), of the signals produced by a transmitter, and of the perturbing
noise. Communication theory is properly concerned, as has been emphasized by Wiener, not with operations
on particular functions, but with operations on ensembles of functions. A communication system is designed
not for a particular speech function and still less for a sine wave, but for the ensemble of speech functions.
19. BAND LIMITED ENSEMBLES OF FUNCTIONS
If a function of time f
(t
) is limited to the band from 0 to W cycles per second it is completely determined
by giving its ordinates at a series of discrete points spaced
1
2W seconds apart in the manner indicated by the
following result.5
Theorem 13: Let f
(t
) contain no frequencies over W. Then
f
(t
)
=
∞
∑
∞
Xn
sin

(2Wt
n )

(2Wt
n )
where
Xn
= f
 n
2W

:
4Communication theory is heavily indebted to Wiener for much of its basic philosophy and theory. His classic NDRC report,
The Interpolation, Extrapolation and Smoothing of Stationary Time Series (Wiley, 1949), contains the ﬁrst clear-cut formulation of
communication theory as a statistical problem, the study of operations on time series. This work, although chieﬂy concerned with the
linear prediction and ﬁltering problem, is an important collateral reference in connection with the present paper. We may also refer
here to Wiener’s Cybernetics (Wiley, 1948), dealing with the general problems of communication and control.
5For a proof of this theorem and further discussion see the author’s paper “Communication in the Presence of Noise” published in
the Proceedings of the Institute of Radio Engineers, v. 37, No. 1, Jan., 1949, pp. 10–21.
34


## PDF page 35

In this expansion f
(t
) is represented as a sum of orthogonal functions. The coefﬁcients Xn of the various
terms can be considered as coordinates in an inﬁnite dimensional “function space.” In this space each
function corresponds to precisely one point and each point to one function.
A function can be considered to be substantially limited to a time T if all the ordinates Xn outside this
interval of time are zero. In this case all but 2TW of the coordinates will be zero. Thus functions limited to
a band W and duration T correspond to points in a space of 2TW dimensions.
A subset of the functions of band W and duration T corresponds to a region in this space. For example,
the functions whose total energy is less than or equal to E correspond to points in a 2TW dimensional sphere
with radius r
=
p
2WE.
An ensemble of functions of limited duration and band will be represented by a probability distribution
p (x1
;
:
:
:
;xn
) in the correspondingn dimensional space. If the ensemble is not limited in time we can consider
the 2TW coordinates in a given interval T to represent substantially the part of the function in the interval T
and the probability distribution p (x1
;
:
:
:
;xn
) to give the statistical structure of the ensemble for intervals of
that duration.
20. ENTROPY OF A CONTINUOUS DISTRIBUTION
The entropy of a discrete set of probabilities p1
;
:
:
:
; pn has been deﬁned as:
H
=
∑pi log pi
:
In an analogous manner we deﬁne the entropy of a continuous distribution with the density distribution
function p (x) by:
H
=
Z ∞
∞p (x)log p (x)dx:
With an n dimensional distribution p (x1
;
:
:
:
;xn
) we have
H
=
Z



Z
p (x1
;
:
:
:
;xn
)log p (x1
;
:
:
:
;xn
)dx1


dxn
:
If we have two arguments x and y (which may themselves be multidimensional) the joint and conditional
entropies of p (x;y) are given by
H
(x;y)
=
Z
Z
p (x;y)log p (x;y)dxdy
and
Hx
(y)
=
Z
Z
p (x;y)log p (x;y)
p (x) dxdy
Hy
(x)
=
Z
Z
p (x;y)log p (x;y)
p (y) dxdy
where
p (x)
=
Z
p (x;y)dy
p (y)
=
Z
p (x;y)dx:
The entropies of continuous distributions have most (but not all) of the properties of the discrete case.
In particular we have the following:
1. If x is limited to a certain volume v in its space, then H
(x) is a maximum and equal to logv when p (x)
is constant (1 =v) in the volume.
35


## PDF page 36

2. With any two variables x, y we have
H
(x;y)
 H
(x)
+H
(y)
with equality if (and only if) x and y are independent, i.e., p (x;y)
= p (x)p (y) (apart possibly from a
set of points of probability zero).
3. Consider a generalized averaging operation of the following type:
p
0
(y)
=
Z
a (x;y)p (x)dx
with
Z
a (x;y)dx
=
Z
a (x;y)dy
= 1 ;
a (x;y)
 0 :
Then the entropy of the averaged distribution p
0
(y) is equal to or greater than that of the original
distribution p (x).
4. We have
H
(x;y)
= H
(x)
+Hx
(y)
= H
(y)
+Hy
(x)
and
Hx
(y)
 H
(y):
5. Let p (x) be a one-dimensional distribution. The form of p (x) giving a maximum entropy subject to the
condition that the standard deviation of x be ﬁxed at
 is Gaussian. To show this we must maximize
H
(x)
=
Z
p (x)log p (x)dx
with
2
=
Z
p (x)x2 dx
and
1
=
Z
p (x)dx
as constraints. This requires, by the calculus of variations, maximizing
Z

p (x)log p (x)
+
p (x)x2
+
p (x)

dx:
The condition for this is
1
logp (x)
+
x2
+

= 0
and consequently (adjusting the constants to satisfy the constraints)
p (x)
=
1
p
2 

e
(x2
=2 2
)
:
Similarly in n dimensions, suppose the second order moments of p (x1
;
:
:
:
;xn
) are ﬁxed at Aij:
Aij
=
Z



Z
xixjp (x1
;
:
:
:
;xn
)dx1


 dxn
:
Then the maximum entropy occurs (by a similar calculation) when p (x1
;
:
:
:
;xn
) is the n dimensional
Gaussian distribution with the second order moments Aij.
36


## PDF page 37

6. The entropy of a one-dimensional Gaussian distribution whose standard deviation is
 is given by
H
(x)
= log
p
2 e
:
This is calculated as follows:
p (x)
=
1
p
2 

e
(x2
=2 2
)
log p (x)
= log
p
2 

+ x2
2 2
H
(x)
=
Z
p (x)log p (x)dx
=
Z
p (x)log
p
2 
dx
+
Z
p (x) x2
2 2 dx
= log
p
2 

+
2
2 2
= log
p
2 

+log
pe
= log
p
2 e

:
Similarly the n dimensional Gaussian distribution with associated quadratic form aij is given by
p (x1
;
:
:
:
;xn
)
=
jaij
j
1
2
(2 
)n =2 exp

 1
2 ∑aijxixj

and the entropy can be calculated as
H
= log(2 e)n =2
jaij
j
 1
2
where
jaij
j is the determinant whose elements are aij.
7. If x is limited to a half line (p (x)
= 0 for x
 0) and the ﬁrst moment of x is ﬁxed at a:
a
=
Z ∞
0 p (x)xdx;
then the maximum entropy occurs when
p (x)
= 1
ae
(x=a )
and is equal to logea.
8. There is one important difference between the continuous and discrete entropies. In the discrete case
the entropy measures in an absolute way the randomness of the chance variable. In the continuous
case the measurement is relative to the coordinate system. If we change coordinates the entropy will
in general change. In fact if we change to coordinates y1


yn the new entropy is given by
H
(y)
=
Z



Z
p (x1
;
:
:
:
;xn
)J
x
y

log p (x1
;
:
:
:
;xn
)J
x
y

dy1


dyn
where J
 x
y

is the Jacobian of the coordinate transformation. On expanding the logarithm and chang-
ing the variables to x1


xn, we obtain:
H
(y)
= H
(x)
Z



Z
p (x1
;
:
:
:
;xn
)logJ
x
y

dx1
:
:
:dxn
:
37


## PDF page 38

Thus the new entropy is the old entropy less the expected logarithm of the Jacobian. In the continuous
case the entropy can be considered a measure of randomnessrelative to an assumed standard, namely
the coordinate system chosen with each small volume element dx1


dxn given equal weight. When
we change the coordinate system the entropy in the new system measures the randomness when equal
volume elements dy1


dyn in the new system are given equal weight.
In spite of this dependence on the coordinate system the entropy concept is as important in the con-
tinuous case as the discrete case. This is due to the fact that the derived concepts of information rate
and channel capacity depend on the difference of two entropies and this difference does not depend
on the coordinate frame, each of the two terms being changed by the same amount.
The entropy of a continuous distribution can be negative. The scale of measurements sets an arbitrary
zero correspondingto a uniform distribution over a unit volume. A distribution which is more conﬁned
than this has less entropy and will be negative. The rates and capacities will, however, always be non-
negative.
9. A particular case of changing coordinates is the linear transformation
yj
= ∑
i
aijxi
:
In this case the Jacobian is simply the determinant
jaij
j
1 and
H
(y)
= H
(x)
+log
jaij
j:
In the case of a rotation of coordinates (or any measure preserving transformation) J
= 1 and H
(y)
=
H
(x).
21. ENTROPY OF AN ENSEMBLE OF FUNCTIONS
Consider an ergodic ensemble of functions limited to a certain band of width W cycles per second. Let
p (x1
;
:
:
:
;xn
)
be the density distribution function for amplitudes x1
;
:
:
:
;xn at n successive sample points. We deﬁne the
entropy of the ensemble per degree of freedom by
H
0
=
Lim
n !∞
1
n
Z



Z
p (x1
;
:
:
:
;xn
)log p (x1
;
:
:
:
;xn
)dx1
:
:
:dxn
:
We may also deﬁne an entropy H per second by dividing, not by n, but by the time T in seconds for n
samples. Since n
= 2TW, H
= 2WH
0.
With white thermal noise p is Gaussian and we have
H
0
= log
p
2 eN
;
H
= W log2 eN
:
For a given average power N, white noise has the maximum possible entropy. This follows from the
maximizing properties of the Gaussian distribution noted above.
The entropy for a continuous stochastic process has many properties analogous to that for discrete pro-
cesses. In the discrete case the entropy was related to the logarithm of the probability of long sequences,
and to the number of reasonably probable sequences of long length. In the continuous case it is related in
a similar fashion to the logarithm of the probability density for a long series of samples, and the volume of
reasonably high probability in the function space.
More precisely, if we assume p (x1
;
:
:
:
;xn
) continuous in all the xi for all n, then for sufﬁciently large n


log p
n
H
0



<

38


## PDF page 39

for all choices of
(x1
;
:
:
:
;xn
) apart from a set whose total probability is less than
, with
 and
 arbitrarily
small. This follows form the ergodic property if we divide the space into a large number of small cells.
The relation of H to volume can be stated as follows: Under the same assumptions consider the n
dimensional space corresponding to p (x1
;
:
:
:
;xn
). Let Vn
(q ) be the smallest volume in this space which
includes in its interior a total probability q. Then
Lim
n !∞
logVn
(q )
n
= H
0
provided q does not equal 0 or 1.
These results show that for large n there is a rather well-deﬁned volume (at least in the logarithmic sense)
of high probability, and that within this volume the probability density is relatively uniform (again in the
logarithmic sense).
In the white noise case the distribution function is given by
p (x1
;
:
:
:
;xn
)
=
1
(2 N
)n =2 exp
 1
2N ∑x2
i
:
Since this depends only on ∑x2
i the surfaces of equal probability density are spheres and the entire distri-
bution has spherical symmetry. The region of high probability is a sphere of radius
p
nN. As n
! ∞the
probability of being outside a sphere of radius
p
n (N
+
) approaches zero and 1
n times the logarithm of the
volume of the sphere approaches log
p
2 eN.
In the continuous case it is convenient to work not with the entropy H of an ensemble but with a derived
quantity which we will call the entropy power. This is deﬁned as the power in a white noise limited to the
same band as the original ensemble and having the same entropy. In other words if H
0 is the entropy of an
ensemble its entropy power is
N1
=
1
2 e exp2H
0
:
In the geometrical picture this amounts to measuring the high probability volume by the squared radius of a
sphere having the same volume. Since white noise has the maximum entropy for a given power, the entropy
power of any noise is less than or equal to its actual power.
22. ENTROPY LOSS IN LINEAR FILTERS
Theorem 14: If an ensemble having an entropy H1 per degree of freedom in band W is passed through a
ﬁlter with characteristic Y
(f
) the output ensemble has an entropy
H2
= H1
+ 1
W
Z
W log
jY
(f
)j2 d f
:
The operation of the ﬁlter is essentially a linear transformation of coordinates. If we think of the different
frequency components as the original coordinate system, the new frequency components are merely the old
ones multiplied by factors. The coordinate transformation matrix is thus essentially diagonalized in terms
of these coordinates. The Jacobian of the transformation is (for n sine and n cosine components)
J
=
n
∏
i=1
jY
(fi
)j2
where the fi are equally spaced through the band W. This becomes in the limit
exp 1
W
Z
W log
jY
(f
)j2 d f
:
Since J is constant its average value is the same quantity and applying the theorem on the change of entropy
with a change of coordinates, the result follows. We may also phrase it in terms of the entropy power. Thus
if the entropy power of the ﬁrst ensemble is N1 that of the second is
N1 exp 1
W
Z
W log
jY
(f
)j2 d f
:
39


## PDF page 40

TABLE I
ENTROPY
ENTROPY
GAIN
POWER
POWER GAIN
IMPULSE RESPONSE
FACTOR
IN DECIBELS
0

!

1
!
1
e2
8:69
sin2
(t
=2)
t2
=2
0

!

1
!2
 2
e
4
5:33
2
 sint
t3
 cost
t2

0

!

1
!3
0:411
3:87
6
 cost
1
t4
 cost
2t2
+ sint
t3

0

!

p
1
!2
 2
e
2
2:67

2
J1
(t
)
t
0

!


1
e2
8:69
1
t2

cos(1
)t
cost

The ﬁnal entropy power is the initial entropy power multiplied by the geometric mean gain of the ﬁlter. If
the gain is measured in db, then the output entropy power will be increased by the arithmetic mean db gain
over W.
In Table I the entropy power loss has been calculated (and also expressed in db) for a number of ideal
gain characteristics. The impulsive responses of these ﬁlters are also given for W
= 2 , with phase assumed
to be 0.
The entropy loss for many other cases can be obtained from these results. For example the entropy
power factor 1 =e2 for the ﬁrst case also applies to any gain characteristic obtain from 1
! by a measure
preserving transformation of the
! axis. In particular a linearly increasing gain G(!
)
=
!, or a “saw tooth”
characteristic between 0 and 1 have the same entropy loss. The reciprocal gain has the reciprocal factor.
Thus 1 =! has the factor e2. Raising the gain to any power raises the factor to this power.
23. ENTROPY OF A SUM OF TWO ENSEMBLES
If we have two ensembles of functions f

(t
) and g

(t
) we can form a new ensemble by “addition.” Suppose
the ﬁrst ensemble has the probability density function p (x1
;
:
:
:
;xn
) and the second q (x1
;
:
:
:
;xn
). Then the
40


