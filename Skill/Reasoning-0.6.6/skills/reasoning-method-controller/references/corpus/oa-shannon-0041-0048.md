# A Mathematical Theory of Communication

Source ID: C05
Authors: Claude E. Shannon
Source URL: https://www.princeton.edu/~wbialek/rome/refs/shannon_48.pdf
DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x
Identity: Corrected reprint of the two-part Bell System Technical Journal article, 1948. Reprint pagination differs from journal pagination.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 41

density function for the sum is given by the convolution:
r
(x1
;
:
:
:
;xn
)
=
Z



Z
p (y1
;
:
:
:
;yn
)q (x1
y1
;
:
:
:
;xn
yn
)dy1


dyn
:
Physically this corresponds to adding the noises or signals represented by the original ensembles of func-
tions.
The following result is derived in Appendix 6.
Theorem 15: Let the average power of two ensembles be N1 and N2 and let their entropy powers be N1
and N2. Then the entropy power of the sum, N3, is bounded by
N1
+N2
 N3
 N1
+N2
:
White Gaussian noise has the peculiar property that it can absorb any other noise or signal ensemble
which may be added to it with a resultant entropy power approximately equal to the sum of the white noise
power and the signal power (measured from the average signal value, which is normally zero), provided the
signal power is small, in a certain sense, compared to noise.
Consider the function space associated with these ensembles having n dimensions. The white noise
corresponds to the spherical Gaussian distribution in this space. The signal ensemble corresponds to another
probability distribution, not necessarily Gaussian or spherical. Let the second moments of this distribution
about its center of gravity be aij. That is, if p (x1
;
:
:
:
;xn
) is the density distribution function
aij
=
Z



Z
p (xi
i
)(xj
j
)dx1


dxn
where the
i are the coordinates of the center of gravity. Now aij is a positive deﬁnite quadratic form, and
we can rotate our coordinate system to align it with the principal directions of this form. aij is then reduced
to diagonal form bii. We require that each bii be small compared to N, the squared radius of the spherical
distribution.
In this case the convolution of the noise and signal produce approximately a Gaussian distribution whose
corresponding quadratic form is
N
+bii
:
The entropy power of this distribution is
h
∏
(N
+bii
)
i1 =n
or approximately
=
h
(N
)n
+∑bii
(N
)n 1
i1 =n
:
= N
+ 1
n ∑bii
:
The last term is the signal power, while the ﬁrst is the noise power.
PART IV: THE CONTINUOUS CHANNEL
24. THE CAPACITY OF A CONTINUOUS CHANNEL
In a continuous channel the input or transmitted signals will be continuous functions of time f
(t
) belonging
to a certain set, and the output or received signals will be perturbed versions of these. We will consider
only the case where both transmitted and received signals are limited to a certain band W. They can then
be speciﬁed, for a time T, by 2TW numbers, and their statistical structure by ﬁnite dimensional distribution
functions. Thus the statistics of the transmitted signal will be determined by
P(x1
;
:
:
:
;xn
)
= P(x)
41


## PDF page 42

and those of the noise by the conditional probability distribution
Px1
;:::;xn
(y1
;
:
:
:
;yn
)
= Px
(y):
The rate of transmission of information for a continuous channel is deﬁned in a way analogous to that
for a discrete channel, namely
R
= H
(x)
Hy
(x)
where H
(x) is the entropy of the input and Hy
(x) the equivocation. The channel capacity C is deﬁned as the
maximum of R when we vary the input over all possible ensembles. This means that in a ﬁnite dimensional
approximation we must vary P(x)
= P(x1
;
:
:
:
;xn
) and maximize
Z
P(x)logP(x)dx
+
ZZ
P(x;y)log P(x;y)
P(y) dxdy
:
This can be written
Z
Z
P(x;y)log P(x;y)
P(x)P(y) dxdy
using the fact that
Z
Z
P(x;y)logP(x)dxdy
=
Z
P(x)logP(x)dx. The channel capacity is thus expressed as
follows:
C
= Lim
T
!∞Max
P (x)
1
T
Z
Z
P(x;y)log P(x;y)
P(x)P(y) dxdy
:
It is obvious in this form that R and C are independent of the coordinate system since the numerator
and denominator in log P(x;y)
P(x)P(y) will be multiplied by the same factors when x and y are transformed in
any one-to-one way. This integral expression for C is more general than H
(x)
Hy
(x). Properly interpreted
(see Appendix 7) it will always exist while H
(x)
Hy
(x) may assume an indeterminate form ∞
∞in some
cases. This occurs, for example, if x is limited to a surface of fewer dimensions than n in its n dimensional
approximation.
If the logarithmic base used in computing H
(x) and Hy
(x) is two then C is the maximum number of
binary digits that can be sent per second over the channel with arbitrarily small equivocation, just as in
the discrete case. This can be seen physically by dividing the space of signals into a large number of
small cells, sufﬁciently small so that the probability density Px
(y) of signal x being perturbed to point y is
substantially constant over a cell (either of x or y). If the cells are considered as distinct points the situation is
essentially the same as a discrete channel and the proofs used there will apply. But it is clear physically that
this quantizing of the volume into individual points cannot in any practical situation alter the ﬁnal answer
signiﬁcantly, provided the regions are sufﬁciently small. Thus the capacity will be the limit of the capacities
for the discrete subdivisions and this is just the continuous capacity deﬁned above.
On the mathematical side it can be shown ﬁrst (see Appendix 7) that if u is the message, x is the signal,
y is the received signal (perturbed by noise) and v is the recovered message then
H
(x)
Hy
(x)
 H
(u )
Hv
(u )
regardless of what operations are performed on u to obtain x or on y to obtain v. Thus no matter how we
encode the binary digits to obtain the signal, or how we decode the received signal to recover the message,
the discrete rate for the binary digits does not exceed the channel capacity we have deﬁned. On the other
hand, it is possible under very general conditions to ﬁnd a coding system for transmitting binary digits at the
rate C with as small an equivocation or frequency of errors as desired. This is true, for example, if, when we
take a ﬁnite dimensional approximating space for the signal functions, P(x;y) is continuous in both x and y
except at a set of points of probability zero.
An important special case occurs when the noise is added to the signal and is independent of it (in the
probability sense). Then Px
(y) is a function only of the difference n
=
(y
x),
Px
(y)
= Q(y
x)
42


## PDF page 43

and we can assign a deﬁnite entropy to the noise (independent of the statistics of the signal), namely the
entropy of the distribution Q(n ). This entropy will be denoted by H
(n ).
Theorem 16: If the signal and noise are independent and the received signal is the sum of the transmitted
signal and the noise then the rate of transmission is
R
= H
(y)
H
(n );
i.e., the entropy of the received signal less the entropy of the noise. The channel capacity is
C
= Max
P (x) H
(y)
H
(n ):
We have, since y
= x
+n:
H
(x;y)
= H
(x;n ):
Expanding the left side and using the fact that x and n are independent
H
(y)
+Hy
(x)
= H
(x)
+H
(n ):
Hence
R
= H
(x)
Hy
(x)
= H
(y)
H
(n ):
Since H
(n ) is independent of P(x), maximizing R requires maximizing H
(y), the entropy of the received
signal. If there are certain constraints on the ensemble of transmitted signals, the entropy of the received
signal must be maximized subject to these constraints.
25. CHANNEL CAPACITY WITH AN AVERAGE POWER LIMITATION
A simple application of Theorem 16 is the case when the noise is a white thermal noise and the transmitted
signals are limited to a certain average power P. Then the received signals have an average power P
+ N
where N is the average noise power. The maximum entropy for the received signals occurs when they also
form a white noise ensemble since this is the greatest possible entropy for a power P
+N and can be obtained
by a suitable choice of transmitted signals, namely if they form a white noise ensemble of power P. The
entropy (per second) of the received ensemble is then
H
(y)
= W log2 e(P
+N
);
and the noise entropy is
H
(n )
= W log2 eN
:
The channel capacity is
C
= H
(y)
H
(n )
= W log P
+N
N
:
Summarizing we have the following:
Theorem 17: The capacity of a channel of band W perturbed by white thermal noise power N when the
average transmitter power is limited to P is given by
C
= W log P
+N
N
:
This means that by sufﬁciently involved encoding systems we can transmit binary digits at the rate
W log2
P
+N
N
bits per second, with arbitrarily small frequency of errors. It is not possible to transmit at a
higher rate by any encoding system without a deﬁnite positive frequency of errors.
To approximate this limiting rate of transmission the transmitted signals must approximate, in statistical
properties, a white noise.6 A system which approaches the ideal rate may be described as follows: Let
6This and other properties of the white noise case are discussed from the geometrical point of view in “Communication in the
Presence of Noise,” loc. cit.
43


## PDF page 44

M
= 2s samples of white noise be constructed each of duration T. These are assigned binary numbers from
0 to M
 1. At the transmitter the message sequences are broken up into groups of s and for each group
the corresponding noise sample is transmitted as the signal. At the receiver the M samples are known and
the actual received signal (perturbed by noise) is compared with each of them. The sample which has the
least R.M.S. discrepancy from the received signal is chosen as the transmitted signal and the corresponding
binary number reconstructed. This process amounts to choosing the most probable (a posteriori) signal.
The number M of noise samples used will depend on the tolerable frequency
 of errors, but for almost all
selections of samples we have
Lim
!0 Lim
T
!∞
logM
(;T
)
T
= W log P
+N
N
;
so that no matter how small
 is chosen, we can, by taking T sufﬁciently large, transmit as near as we wish
to TW log P
+N
N
binary digits in the time T.
Formulas similar to C
= W log P
+N
N
for the white noise case have been developed independently
by several other writers, although with somewhat different interpretations. We may mention the work of
N. Wiener,7 W. G. Tuller,8 and H. Sullivan in this connection.
In the case of an arbitrary perturbing noise (not necessarily white thermal noise) it does not appear that
the maximizing problem involved in determining the channel capacity C can be solved explicitly. However,
upper and lower bounds can be set for C in terms of the average noise power N the noise entropy power N1.
These bounds are sufﬁciently close together in most practical cases to furnish a satisfactory solution to the
problem.
Theorem 18: The capacity of a channel of band W perturbed by an arbitrary noise is bounded by the
inequalities
W log P
+N1
N1
 C
 W log P
+N
N1
where
P
= average transmitter power
N
= average noise power
N1
= entropy power of the noise.
Here again the average power of the perturbed signals will be P
+ N. The maximum entropy for this
power would occur if the received signal were white noise and would be W log2 e(P
+ N
). It may not
be possible to achieve this; i.e., there may not be any ensemble of transmitted signals which, added to the
perturbing noise, produce a white thermal noise at the receiver, but at least this sets an upper bound to H
(y).
We have, therefore
C
= MaxH
(y)
H
(n )
 W log2 e(P
+N
)
W log2 eN1
:
This is the upper limit given in the theorem. The lower limit can be obtained by considering the rate if we
make the transmitted signal a white noise, of power P. In this case the entropy power of the received signal
must be at least as great as that of a white noise of power P
+ N1 since we have shown in in a previous
theorem that the entropy power of the sum of two ensembles is greater than or equal to the sum of the
individual entropy powers. Hence
MaxH
(y)
 W log2 e(P
+N1
)
7Cybernetics, loc. cit.
8“Theoretical Limitations on the Rate of Transmission of Information,” Proceedings of the Institute of Radio Engineers, v. 37,
No. 5, May, 1949, pp. 468–78.
44


## PDF page 45

and
C
 W log2 e(P
+N1
)
W log2 eN1
= W log P
+N1
N1
:
As P increases, the upper and lower bounds approach each other, so we have as an asymptotic rate
W log P
+N
N1
:
If the noise is itself white, N
= N1 and the result reduces to the formula proved previously:
C
= W log

1
+ P
N

:
If the noise is Gaussian but with a spectrum which is not necessarily ﬂat, N1 is the geometric mean of
the noise power over the various frequencies in the band W. Thus
N1
= exp 1
W
Z
W logN
(f
)d f
where N
(f
) is the noise power at frequency f.
Theorem 19: If we set the capacity for a given transmitter power P equal to
C
= W log P
+N

N1
then
 is monotonic decreasing as P increases and approaches 0 as a limit.
Suppose that for a given power P1 the channel capacity is
W log P1
+N
1
N1
:
This means that the best signal distribution, say p (x), when added to the noise distribution q (x), gives a
received distribution r
(y) whose entropy power is
(P1
+ N
1
). Let us increase the power to P1
+
P by
adding a white noise of power
P to the signal. The entropy of the received signal is now at least
H
(y)
= W log2 e(P1
+N
1
+
P)
by application of the theorem on the minimum entropy power of a sum. Hence, since we can attain the
H indicated, the entropy of the maximizing distribution must be at least as great and
 must be monotonic
decreasing. To show that

! 0 as P
! ∞consider a signal which is white noise with a large P. Whatever
the perturbing noise, the received signal will be approximately a white noise, if P is sufﬁciently large, in the
sense of having an entropy power approaching P
+N.
26. THE CHANNEL CAPACITY WITH A PEAK POWER LIMITATION
In some applications the transmitter is limited not by the average power output but by the peak instantaneous
power. The problem of calculating the channel capacity is then that of maximizing (by variation of the
ensemble of transmitted symbols)
H
(y)
H
(n )
subject to the constraint that all the functions f
(t
) in the ensemble be less than or equal to
p
S, say, for all
t. A constraint of this type does not work out as well mathematically as the average power limitation. The
most we have obtained for this case is a lower bound valid for all S
N , an “asymptotic” upper bound (valid
for large S
N ) and an asymptotic value of C for S
N small.
45


## PDF page 46

Theorem 20: The channel capacity C for a band W perturbed by white thermal noise of power N is
bounded by
C
 W log 2
e3
S
N
;
where S is the peak allowed transmitter power. For sufﬁciently large S
N
C
 W log
2
eS
+N
N
(1
+
)
where
 is arbitrarily small. As S
N
! 0 (and provided the band W starts at 0)
C
.
W log

1
+ S
N

! 1 :
We wish to maximize the entropy of the received signal. If S
N is large this will occur very nearly when
we maximize the entropy of the transmitted ensemble.
The asymptotic upper bound is obtained by relaxing the conditions on the ensemble. Let us suppose that
the power is limited to S not at every instant of time, but only at the sample points. The maximum entropy of
the transmitted ensemble under these weakened conditions is certainly greater than or equal to that under the
original conditions. This altered problem can be solved easily. The maximum entropy occurs if the different
samples are independent and have a distribution function which is constant from
p
S to
+
p
S. The entropy
can be calculated as
W log4S
:
The received signal will then have an entropy less than
W log(4S
+2 eN
)(1
+
)
with

! 0 as S
N
! ∞and the channel capacity is obtained by subtracting the entropy of the white noise,
W log2 eN:
W log(4S
+2 eN
)(1
+
)
W log(2 eN
)
= W log
2
eS
+N
N
(1
+
):
This is the desired upper bound to the channel capacity.
To obtain a lower bound consider the same ensemble of functions. Let these functions be passed through
an ideal ﬁlter with a triangular transfer characteristic. The gain is to be unity at frequency 0 and decline
linearly down to gain 0 at frequency W. We ﬁrst show that the output functions of the ﬁlter have a peak
power limitation S at all times (not just the sample points). First we note that a pulse sin2 Wt
2 Wt
going into
the ﬁlter produces
1
2
sin2
Wt
(Wt
)2
in the output. This function is never negative. The input function (in the general case) can be thought of as
the sum of a series of shifted functions
asin2 Wt
2 Wt
where a, the amplitude of the sample, is not greater than
p
S. Hence the output is the sum of shifted functions
of the non-negative form above with the same coefﬁcients. These functions being non-negative, the greatest
positive value for any t is obtained when all the coefﬁcients a have their maximum positive values, i.e.,
p
S.
In this case the input function was a constant of amplitude
p
S and since the ﬁlter has unit gain for D.C., the
output is the same. Hence the output ensemble has a peak power S.
46


## PDF page 47

The entropy of the output ensemble can be calculated from that of the input ensemble by using the
theorem dealing with such a situation. The output entropy is equal to the input entropy plus the geometrical
mean gain of the ﬁlter:
Z W
0
logG2 d f
=
Z W
0
log
W
 f
W
2
d f
=
2W
:
Hence the output entropy is
W log4S
2W
= W log 4S
e2
and the channel capacity is greater than
W log 2
e3
S
N
:
We now wish to show that, for small S
N (peak signal power over average white noise power), the channel
capacity is approximately
C
= W log

1
+ S
N

:
More precisely C
.
W log

1
+ S
N

! 1 as S
N
! 0. Since the average signal power P is less than or equal
to the peak S, it follows that for all S
N
C
 W log

1
+ P
N

 W log

1
+ S
N

:
Therefore, if we can ﬁnd an ensemble of functions such that they correspond to a rate nearly W log

1
+ S
N

and are limited to band W and peak S the result will be proved. Consider the ensemble of functions of the
following type. A series of t samples have the same value, either
+
p
S or
p
S, then the next t samples have
the same value, etc. The value for a series is chosen at random, probability 1
2 for
+
p
S and 1
2 for
p
S. If
this ensemble be passed through a ﬁlter with triangular gain characteristic (unit gain at D.C.), the output is
peak limited to
S. Furthermore the average power is nearly S and can be made to approach this by taking t
sufﬁciently large. The entropy of the sum of this and the thermal noise can be found by applying the theorem
on the sum of a noise and a small signal. This theorem will apply if
p
t S
N
is sufﬁciently small. This can be ensured by taking S
N small enough (after t is chosen). The entropy power
will be S
+N to as close an approximation as desired, and hence the rate of transmission as near as we wish
to
W log
S
+N
N

:
PART V: THE RATE FOR A CONTINUOUS SOURCE
27. FIDELITY EVALUATION FUNCTIONS
In the case of a discrete source of information we were able to determine a deﬁnite rate of generating
information, namely the entropy of the underlying stochastic process. With a continuous source the situation
is considerably more involved. In the ﬁrst place a continuously variable quantity can assume an inﬁnite
number of values and requires, therefore, an inﬁnite number of binary digits for exact speciﬁcation. This
means that to transmit the output of a continuous source with exact recovery at the receiving point requires,
47


## PDF page 48

in general, a channel of inﬁnite capacity (in bits per second). Since, ordinarily, channels have a certain
amount of noise, and therefore a ﬁnite capacity, exact transmission is impossible.
This, however, evades the real issue. Practically, we are not interested in exact transmission when we
have a continuous source, but only in transmission to within a certain tolerance. The question is, can we
assign a deﬁnite rate to a continuous source when we require only a certain ﬁdelity of recovery, measured in
a suitable way. Of course, as the ﬁdelity requirements are increased the rate will increase. It will be shown
that we can, in very general cases, deﬁne such a rate, having the property that it is possible, by properly
encoding the information, to transmit it over a channel whose capacity is equal to the rate in question, and
satisfy the ﬁdelity requirements. A channel of smaller capacity is insufﬁcient.
It is ﬁrst necessary to give a general mathematical formulation of the idea of ﬁdelity of transmission.
Consider the set of messages of a long duration, say T seconds. The source is described by giving the
probability density, in the associated space, that the source will select the message in question P(x). A given
communication system is described (from the external point of view) by giving the conditional probability
Px
(y) that if message x is produced by the source the recovered message at the receiving point will be y. The
system as a whole (including source and transmission system) is described by the probability function P(x;y)
of having message x and ﬁnal output y. If this function is known, the complete characteristics of the system
from the point of view of ﬁdelity are known. Any evaluation of ﬁdelity must correspond mathematically
to an operation applied to P(x;y). This operation must at least have the properties of a simple ordering of
systems; i.e., it must be possible to say of two systems represented by P1
(x;y) and P2
(x;y) that, according to
our ﬁdelity criterion, either (1) the ﬁrst has higher ﬁdelity, (2) the second has higher ﬁdelity, or (3) they have
equal ﬁdelity. This means that a criterion of ﬁdelity can be represented by a numerically valued function:
v
P(x;y)

whose argument ranges over possible probability functions P(x;y).
We will now show that under very general and reasonable assumptions the function v
P(x;y)

can be
written in a seemingly much more specialized form, namely as an average of a function
(x;y) over the set
of possible values of x and y:
v
P(x;y)

=
Z
Z
P(x;y)(x;y)dxdy
:
To obtain this we need only assume (1) that the source and system are ergodic so that a very long sample
will be, with probability nearly 1, typical of the ensemble, and (2) that the evaluation is “reasonable” in the
sense that it is possible, by observing a typical input and output x1 and y1, to form a tentative evaluation
on the basis of these samples; and if these samples are increased in duration the tentative evaluation will,
with probability 1, approach the exact evaluation based on a full knowledge of P(x;y). Let the tentative
evaluation be
(x;y). Then the function
(x;y) approaches (as T
! ∞) a constant for almost all
(x;y) which
are in the high probability region corresponding to the system:
(x;y)
! v
P(x;y)

and we may also write
(x;y)
!
Z
Z
P(x;y)(x;y)dxdy
since
Z
Z
P(x;y)dxdy
= 1 :
This establishes the desired result.
The function
(x;y) has the general nature of a “distance” between x and y.9 It measures how undesirable
it is (according to our ﬁdelity criterion) to receive y when x is transmitted. The general result given above
can be restated as follows: Any reasonable evaluation can be represented as an average of a distance function
over the set of messages and recovered messages x and y weighted according to the probability P(x;y) of
getting the pair in question, provided the duration T of the messages be taken sufﬁciently large.
The following are simple examples of evaluation functions:
9It is not a “metric” in the strict sense, however, since in general it does not satisfy either
(x;y)
=
(y
;x) or
(x;y)
+
(y
;z)

(x;z).
48


