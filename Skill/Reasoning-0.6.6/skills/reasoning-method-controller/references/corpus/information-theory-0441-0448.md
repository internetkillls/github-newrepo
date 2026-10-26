# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 441

12.4
SPECTRUM ESTIMATION
415
This example shows that the maximum entropy may only be ϵ-achiev-
able.
12.4
SPECTRUM ESTIMATION
Given a stationary zero-mean stochastic process {Xi}, we deﬁne the auto-
correlation function as
R(k) = EXiXi+k.
(12.33)
The Fourier transform of the autocorrelation function for a zero-mean
process is the power spectral density S(λ):
S(λ) =
∞

m=−∞
R(m)e−imλ,
−π < λ ≤π,
(12.34)
where i =
√
−1. Since the power spectral density is indicative of the
structure of the process, it is useful to form an estimate from a sample of
the process.
There are many methods to estimate the power spectrum. The simplest
way is to estimate the autocorrelation function by taking sample averages
for a sample of length n,
ˆR(k) =
1
n −k
n−k

i=1
XiXi+k.
(12.35)
If we use all the values of the sample correlation function ˆR(·) to cal-
culate the spectrum, the estimate that we obtain from (12.34) does not
converge to the true power spectrum for large n. Hence, this method, the
periodogram method, is rarely used. One of the reasons for the problem
with the periodogram method is that the estimates of the autocorrelation
function from the data have different accuracies. The estimates for low
values of k (called the lags) are based on a large number of samples and
those for high k on very few samples. So the estimates are more accurate
at low k. The method can be modiﬁed so that it depends only on the
autocorrelations at low k by setting the higher lag autocorrelations to 0.
However, this introduces some artifacts because of the sudden transition to
zero autocorrelation. Various windowing schemes have been suggested to
smooth out the transition. However, windowing reduces spectral resolution
and can give rise to negative power spectral estimates.
In the late 1960s, while working on the problem of spectral estimation for
geophysical applications, Burg suggested an alternative method. Instead of


## PDF page 442

416
MAXIMUM ENTROPY
setting the autocorrelations at high lags to zero, he set them to values that
make the fewest assumptions about the data (i.e., values that maximize the
entropy rate of the process). This is consistent with the maximum entropy
principle as articulated by Jaynes [294]. Burg assumed the process to be
stationary and Gaussian and found that the process which maximizes the
entropy subject to the correlation constraints is an autoregressive Gaussian
process of the appropriate order. In some applications where we can assume
an underlying autoregressive model for the data, this method has proved
useful in determining the parameters of the model (e.g., linear predictive
coding for speech). This method (known as the maximum entropy method
or Burg’s method) is a popular method for estimation of spectral densities.
We prove Burg’s theorem in Section 12.6.
12.5
ENTROPY RATES OF A GAUSSIAN PROCESS
In Chapter 8 we deﬁned the differential entropy of a continuous random
variable. We can now extend the deﬁnition of entropy rates to real-valued
stochastic processes.
Deﬁnition
The differential entropy rateofa stochastic process {Xi}, Xi ∈
R, is deﬁned to be
h(X) = lim
n→∞
h(X1, X2, . . . , Xn)
n
(12.36)
if the limit exists.
Just as in the discrete case, we can show that the limit exists for sta-
tionary processes and that the limit is given by the two expressions
h(X) = lim
n→∞
h(X1, X2, . . . , Xn)
n
(12.37)
= lim
n→∞h(Xn|Xn−1, . . . , X1).
(12.38)
For a stationary Gaussian stochastic process, we have
h(X1, X2, . . . , Xn) = 1
2 log(2πe)n|K(n)|,
(12.39)
where the covariance matrix K(n) is Toeplitz with entries R(0), R(1), . . . ,
R(n −1) along the top row. Thus, K(n)
ij
= R(i −j) = E(Xi −EXi)(Xj


## PDF page 443

12.6
BURG’S MAXIMUM ENTROPY THEOREM
417
−EXj). As n →∞, the density of the eigenvalues of the covariance
matrix tends to a limit, which is the spectrum of the stochastic process.
Indeed, Kolmogorov showed that the entropy rate of a stationary Gaussian
stochastic process can be expressed as
h(X) = 1
2 log 2πe + 1
4π
 π
−π
log S(λ) dλ.
(12.40)
The entropy rate is also limn→∞h(Xn|Xn−1). Since the stochastic pro-
cess is Gaussian, the conditional distribution is also Gaussian, and hence
the conditional entropy is 1
2 log 2πeσ 2
∞, where σ 2
∞is the variance of the
error in the best estimate of Xn given the inﬁnite past. Thus,
σ 2
∞=
1
2πe22h(X),
(12.41)
where h(X) is given by (12.40). Hence, the entropy rate corresponds to
the minimum mean-squared error of the best estimator of a sample of the
process given the inﬁnite past.
12.6
BURG’S MAXIMUM ENTROPY THEOREM
Theorem 12.6.1
The maximum entropy rate stochastic process {Xi} sat-
isfying the constraints
EXiXi+k = αk,
k = 0, 1, . . . , p
for all i,
(12.42)
is the pth-order Gauss–Markov process of the form
Xi = −
p

k=1
akXi−k + Zi,
(12.43)
where the Zi are i.i.d. ∼N(0, σ 2) and a1, a2, . . . , ap, σ 2 are chosen to
satisfy (12.42).
Remark
We do not assume that {Xi} is (a) zero mean, (b) Gaussian, or
(c) wide-sense stationary.
Proof:
Let X1, X2, . . . , Xn be any stochastic process that satisﬁes the
constraints (12.42). Let Z1, Z2, . . . , Zn be a Gaussian process with the
same covariance matrix as X1, X2, . . . , Xn. Then since the multivariate
normal distribution maximizes the entropy over all vector-valued random


## PDF page 444

418
MAXIMUM ENTROPY
variables under a covariance constraint, we have
h(X1, X2, . . . , Xn) ≤h(Z1, Z2, . . . , Zn)
(12.44)
= h(Z1, . . . , Zp) +
n

i=p+1
h(Zi|Zi−1, Zi−2, . . . , Z1)
(12.45)
≤h(Z1, . . . , Zp) +
n

i=p+1
h(Zi|Zi−1, Zi−2, . . . , Zi−p)
(12.46)
by the chain rule and the fact that conditioning reduces entropy. Now
deﬁne Z′
1, Z′
2, . . . , Z′
n as a pth-order Gauss–Markov process with the
same distribution as Z1, Z2, . . . , Zn for all orders up to p. (Existence of
such a process will be veriﬁed using the Yule–Walker equations immedi-
ately after the proof.) Then since h(Zi|Zi−1, . . . , Zi−p) depends only on
the pth-order distribution, h(Zi|Zi−1, . . . , Zi−p)= h(Z′
i|Z′
i−1, . . . , Z′
i−p),
and continuing the chain of inequalities, we obtain
h(X1, X2, . . . , Xn) ≤h(Z1, . . . , Zp) +
n

i=p+1
h(Zi|Zi−1, Zi−2, . . . , Zi−p)
(12.47)
= h(Z′
1, . . . , Z′
p) +
n

i=p+1
h(Z′
i|Z′
i−1, Z′
i−2, . . . , Z′
i−p)
(12.48)
= h(Z′
1, Z′
2, . . . , Z′
n),
(12.49)
where the last equality follows from the pth-order Markovity of the {Z′
i}.
Dividing by n and taking the limit, we obtain
lim1
nh(X1, X2, . . . , Xn) ≤lim 1
nh(Z′
1, Z′
2, . . . , Z′
n) = h∗,
(12.50)
where
h∗= 1
2 log 2πeσ 2,
(12.51)
which is the entropy rate of the Gauss–Markov process. Hence, the max-
imum entropy rate stochastic process satisfying the constraints is the
pth-order Gauss–Markov process satisfying the constraints.
□
A bare-bones summary of the proof is that the entropy of a ﬁnite
segment of a stochastic process is bounded above by the entropy of a


## PDF page 445

12.6
BURG’S MAXIMUM ENTROPY THEOREM
419
segment of a Gaussian random process with the same covariance structure.
This entropy is in turn bounded above by the entropy of the minimal order
Gauss–Markov process satisfying the given covariance constraints. Such
a process exists and has a convenient characterization by means of the
Yule–Walker equations given below.
Note on the choice of a1, . . . , ap and σ 2: Given a sequence of covariances
R(0), R(1), . . . , R(p), does there exist a pth-order Gauss–Markov pro-
cess with these covariances? Given a process of the form (12.43), can we
choose the ak’s to satisfy the constraints? Multiplying (12.43) by Xi−l
and taking expectations, noting that R(k) = R(−k), we get
R(0) = −
p

k=1
akR(−k) + σ 2
(12.52)
and
R(l) = −
p

k=1
akR(l −k),
l = 1, 2, . . . .
(12.53)
These equations are called the Yule–Walker equations. There are p + 1
equations in the p + 1 unknowns a1, a2, . . . , ap, σ 2. Therefore, we can
solve for the parameters of the process from the covariances.
Fast algorithms such as the Levinson algorithm and the Durbin algo-
rithm [433] have been devised to use the special structure of these
equations to calculate the coefﬁcients a1, a2, . . . , ap efﬁciently from the
covariances. (We set a0 = 1 for a consistent notation.) Not only do the
Yule–Walker equations provide a convenient set of linear equations for
calculating the ak’s and σ 2 from the R(k)’s, they also indicate how the
autocorrelations behave for lags greater than p. The autocorrelations for
high lags are an extension of the values for lags less than p. These val-
ues are called the Yule–Walker extension of the autocorrelations. The
spectrum of the maximum entropy process is seen to be
S(λ) =
∞

m=−∞
R(m)e−imλ
(12.54)
=
σ 2
1 + p
k=1 ake−ikλ2 ,
−π ≤λ ≤π.
(12.55)
This is the maximum entropy spectral density subject to the constraints
R(0), R(1), . . . , R(p).
However, for the pth-order Gauss–Markov process, it is possible to
calculate the entropy rate directly without calculating the ai’s. Let Kp be


## PDF page 446

420
MAXIMUM ENTROPY
the autocorrelation matrix corresponding to this process—the matrix with
R0, R1, . . . , Rp along the top row. For this process, the entropy rate is
equal to
h∗= h(Xp|Xp−1, . . . , X0) = h(X0, . . . , Xp) −h(X0, . . . , Xp−1)
(12.56)
= 1
2 log(2πe)p+1|Kp| −1
2 log(2πe)p|Kp−1|
(12.57)
= 1
2 log(2πe) |Kp|
|Kp−1|.
(12.58)
In a practical problem, we are generally given a sample sequence
X1, X2, . . . , Xn, from which we calculate the autocorrelations. An impor-
tant question is: How many autocorrelation lags should we consider (i.e.,
what is the optimum value of p)? A logically sound method is to choose
the value of p that minimizes the total description length in a two-stage
description of the data. This method has been proposed by Rissanen
[442, 447] and Barron [33] and is closely related to the idea of Kol-
mogorov complexity.
SUMMARY
Maximum entropy distribution. Let f be a probability density satis-
fying the constraints

S
f (x)ri(x) = αi
for 1 ≤i ≤m.
(12.59)
Let f ∗(x) = fλ(x) = eλ0+m
i=1 λiri(x), x ∈S, and let λ0, . . . , λm be cho-
sen so that f ∗satisﬁes (12.59). Then f ∗uniquely maximizes h(f ) over
all f satisfying these constraints.
Maximum entropy spectral density estimation. The entropy rate of a
stochastic process subject to autocorrelation constraints R0, R1, . . . , Rp
is maximized by the pth order zero-mean Gauss-Markov process satis-
fying these constraints. The maximum entropy rate is
h∗= 1
2 log(2πe) |Kp|
|Kp−1|,
(12.60)


## PDF page 447

PROBLEMS
421
and the maximum entropy spectral density is
S(λ) =
σ 2
1 + p
k=1 ake−ikλ2 .
(12.61)
PROBLEMS
12.1
Maximum entropy.
Find the maximum entropy density f ,
deﬁned for x ≥0, satisfying EX = α1, E ln X = α2. That is, max-
imize −

f ln f subject to

xf (x) dx = α1,

(ln x)f (x) dx =
α2, where the integral is over 0 ≤x < ∞. What family of densi-
ties is this?
12.2
Min D(P ∥Q) under constraints on P .
We wish to ﬁnd the
(parametric form) of the probability mass function P (x), x ∈{1, 2,
. . .} that minimizes the relative entropy D(P ∥Q) over all P such
that  P (x)gi(x) = αi, i = 1, 2, . . . .
(a) Use Lagrange multipliers to guess that
P ∗(x) = Q(x)e
∞
i=1 λigi(x)+λ0
(12.62)
achieves this minimum if there exist λi’s satisfying the αi
constraints. This generalizes the theorem on maximum en-
tropy distributions subject to constraints.
(b) Verify that P ∗minimizes D(P ∥Q).
12.3
Maximum entropy processes.
Find the maximum entropy rate
stochastic process {Xi}∞
−∞subject to the constraints:
(a) EX2
i = 1,
i = 1, 2, . . . .
(b) EX2
i = 1, EXiXi+1 = 1
2,
i = 1, 2, . . . .
(c) Find the maximum entropy spectrum for the processes in parts
(a) and (b).
12.4
Maximum entropy with marginals.
What is the maximum en-
tropy distribution p(x, y) that has the following marginals?


## PDF page 448

422
MAXIMUM ENTROPY
(Hint: You may wish to guess and verify a more general result.)
12.5
Processes with ﬁxed marginals.
Consider the set of all densities
with ﬁxed pairwise marginals fX1,X2(x1, x2), fX2,X3(x2, x3), . . . ,
fXn−1,Xn(xn−1, xn). Show that the maximum entropy process with
these marginals is the ﬁrst-order (possibly time-varying) Markov
process with these marginals. Identify the maximizing f ∗(x1, x2,
. . . , xn).
12.6
Every density is a maximum entropy density.
Let f0(x) be a
given density. Given r(x), let gα(x) be the density maximizing
h(X) over all f satisfying

f (x)r(x) dx = α. Now let r(x) =
ln f0(x). Show that gα(x) = f0(x) for an appropriate choice α =
α0. Thus, f0(x) is a maximum entropy density under the constraint

f ln f0 = α0.
12.7
Mean-squared error.
Let {Xi}n
i=1 satisfy EXiXi+k = Rk, k =
0, 1, . . . , p. Consider linear predictors for Xn; that is,
ˆXn =
n−1

i=1
biXn−i.
Assume that n > p. Find
max
f (xn) min
b E(Xn −ˆXn)2,
where the minimum is over all linear predictors b and the maxi-
mum is over all densities f satisfying R0, . . . , Rp.
12.8
Maximum entropy characteristic functions.
We ask for the max-
imum entropy density f (x), 0 ≤x ≤a, satisfying a constraint on
the characteristic function (u) =
 a
0 eiuxf (x) dx. The answers
need be given only in parametric form.
(a) Find the maximum entropy f satisfying
 a
0 f (x) cos(u0x) dx
= α, at a speciﬁed point u0.
(b) Find the maximum entropy f satisfying
 a
0 f (x) sin(u0x) dx
= β.
(c) Find the maximum entropy density f (x), 0 ≤x ≤a, having a
given value of the characteristic function (u0) at a speciﬁed
point u0.
(d) What problem is encountered if a = ∞?


