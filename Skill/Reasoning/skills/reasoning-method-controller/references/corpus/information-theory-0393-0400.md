# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 393

11.6
CONDITIONAL LIMIT THEOREM
367
E
Q
P
P*
FIGURE 11.5. Pythagorean theorem for relative entropy.
number of terms. Since the number of terms is polynomial in the length
of the sequences, the sum is equal to the largest term to ﬁrst order in the
exponent.
We now strengthen the argument to show that not only is the proba-
bility of the set E essentially the same as the probability of the closest
type P ∗but also that the total probability of other types that are far
away from P ∗is negligible. This implies that with very high probabil-
ity, the type observed is close to P ∗. We call this a conditional limit
theorem.
Before we prove this result, we prove a “Pythagorean” theorem, which
gives some insight into the geometry of D(P ||Q). Since D(P ||Q) is not
a metric, many of the intuitive properties of distance are not valid for
D(P ||Q). The next theorem shows a sense in which D(P ||Q) behaves
like the square of the Euclidean metric (Figure 11.5).
Theorem 11.6.1
For a closed convex set E ⊂P and distribution Q /∈
E, let P ∗∈E be the distribution that achieves the minimum distance to
Q; that is,
D(P ∗||Q) = min
P∈E D(P ||Q).
(11.121)
Then
D(P ||Q) ≥D(P ||P ∗) + D(P ∗||Q)
(11.122)
for all P ∈E.


## PDF page 394

368
INFORMATION THEORY AND STATISTICS
Note. The main use of this theorem is as follows: Suppose that we have
a sequence Pn ∈E that yields D(Pn||Q) →D(P ∗||Q). Then from the
Pythagorean theorem, D(Pn||P ∗) →0 as well.
Proof:
Consider any P ∈E. Let
Pλ = λP + (1 −λ)P ∗.
(11.123)
Then Pλ →P ∗as λ →0. Also, since E is convex, Pλ ∈E for 0 ≤λ ≤1.
Since D(P ∗||Q) is the minimum of D(Pλ||Q) along the path P ∗→P ,
the derivative of D(Pλ||Q) as a function of λ is nonnegative at λ = 0.
Now
Dλ = D(Pλ||Q) =

Pλ(x) log Pλ(x)
Q(x)
(11.124)
and
dDλ
dλ =
 
(P (x) −P ∗(x)) log Pλ(x)
Q(x) + (P (x) −P ∗(x))

. (11.125)
Setting λ = 0, so that Pλ = P ∗and using the fact that  P (x) =  P ∗
(x) = 1, we have
0 ≤
dDλ
dλ

λ=0
(11.126)
=

(P (x) −P ∗(x)) log P ∗(x)
Q(x)
(11.127)
=

P (x) log P ∗(x)
Q(x) −

P ∗(x) log P ∗(x)
Q(x)
(11.128)
=

P (x) log P (x)
Q(x)
P ∗(x)
P (x) −

P ∗(x) log P ∗(x)
Q(x)
(11.129)
= D(P ||Q) −D(P ||P ∗) −D(P ∗||Q),
(11.130)
which proves the theorem.
□
Note that the relative entropy D(P ||Q) behaves like the square of the
Euclidean distance. Suppose that we have a convex set E in Rn. Let A
be a point outside the set, B the point in the set closest to A, and C any


## PDF page 395

11.6
CONDITIONAL LIMIT THEOREM
369
A
B
C
FIGURE 11.6. Triangle inequality for distance squared.
other point in the set. Then the angle between the lines BA and BC must
be obtuse, which implies that l2
AC ≥l2
AB + l2
BC, which is of the same form
as Theorem 11.6.1. This is illustrated in Figure 11.6.
We now prove a useful lemma which shows that convergence in relative
entropy implies convergence in the L1 norm.
Deﬁnition
The L1 distance between any two distributions is deﬁned as
||P1 −P2||1 =

a∈X
|P1(a) −P2(a)|.
(11.131)
Let A be the set on which P1(x) > P2(x). Then
||P1 −P2||1 =

x∈X
|P1(x) −P2(x)|
(11.132)
=

x∈A
(P1(x) −P2(x)) +

x∈Ac
(P2(x) −P1(x)) (11.133)
= P1(A) −P2(A) + P2(Ac) −P1(Ac)
(11.134)
= P1(A) −P2(A) + 1 −P2(A) −1 + P1(A)
(11.135)
= 2(P1(A) −P2(A)).
(11.136)


## PDF page 396

370
INFORMATION THEORY AND STATISTICS
Also note that
max
B⊆X (P1(B) −P2(B)) = P1(A) −P2(A) = ||P1 −P2||1
2
.
(11.137)
The left-hand side of (11.137) is called the variational distance between
P1 and P2.
Lemma 11.6.1
D(P1||P2) ≥
1
2 ln 2||P1 −P2||2
1.
(11.138)
Proof:
We ﬁrst prove it for the binary case. Consider two binary distri-
butions with parameters p and q with p ≥q. We will show that
p log p
q + (1 −p) log 1 −p
1 −q ≥
4
2 ln 2(p −q)2.
(11.139)
The difference g(p, q) between the two sides is
g(p, q) = p log p
q + (1 −p) log 1 −p
1 −q −
4
2 ln 2(p −q)2.
(11.140)
Then
dg(p, q)
dq
= −
p
q ln 2 +
1 −p
(1 −q) ln 2 −
4
2 ln 22(q −p) (11.141)
=
q −p
q(1 −q) ln 2 −4
ln 2(q −p)
(11.142)
≤0
(11.143)
since q(1 −q) ≤1
4 and q ≤p. For q = p, g(p, q) = 0, and hence
g(p, q) ≥0 for q ≤p, which proves the lemma for the binary case.
For the general case, for any two distributions P1 and P2, let
A = {x : P1(x) > P2(x)}.
(11.144)
Deﬁne a new binary random variable Y = φ(X), the indicator of the set A,
and let ˆP1 and ˆP2 be the distributions of Y. Thus, ˆP1 and ˆP2 correspond
to the quantized versions of P1 and P2. Then by the data-processing


## PDF page 397

11.6
CONDITIONAL LIMIT THEOREM
371
inequality applied to relative entropies (which is proved in the same way
as the data-processing inequality for mutual information), we have
D(P1||P2) ≥D( ˆP1|| ˆP2)
(11.145)
≥
4
2 ln 2(P1(A) −P2(A))2
(11.146)
=
1
2 ln 2||P1 −P2||2
1,
(11.147)
by (11.137), and the lemma is proved.
□
We can now begin the proof of the conditional limit theorem. We ﬁrst
outline the method used. As stated at the beginning of the chapter, the
essential idea is that the probability of a type under Q depends exponen-
tially on the distance of the type from Q, and hence types that are farther
away are exponentially less likely to occur. We divide the set of types in
E into two categories: those at about the same distance from Q as P ∗and
those a distance 2δ farther away. The second set has exponentially less
probability than the ﬁrst, and hence the ﬁrst set has a conditional proba-
bility tending to 1. We then use the Pythagorean theorem to establish that
all the elements in the ﬁrst set are close to P ∗, which will establish the
theorem.
The following theorem is an important strengthening of the maximum
entropy principle.
Theorem 11.6.2
(Conditional limit theorem)
Let E be a closed con-
vex subset of P and let Q be a distribution not in E. Let X1, X2, . . . , Xn
be discrete random variables drawn i.i.d. ∼Q. Let P ∗achieve minP∈E
D(P ||Q). Then
Pr(X1 = a|PXn ∈E) →P ∗(a)
(11.148)
in probability as n →∞, i.e., the conditional distribution of X1, given that
the type of the sequence is in E, is close to P ∗for large n.
Example 11.6.1
If Xi i.i.d. ∼Q, then
Pr

X1 = a

1
n

X2
i ≥α

→P ∗(a),
(11.149)


## PDF page 398

372
INFORMATION THEORY AND STATISTICS
where P ∗(a) minimizes D(P ||Q) over P satisfying  P (a)a2 ≥α. This
minimization results in
P ∗(a) = Q(a)
eλa2

a Q(a)eλa2 ,
(11.150)
where λ is chosen to satisfy  P ∗(a)a2 = α. Thus, the conditional dis-
tribution on X1 given a constraint on the sum of the squares is a (normal-
ized) product of the original probability mass function and the maximum
entropy probability mass function (which in this case is Gaussian).
Proof of Theorem:
Deﬁne the sets
St = {P ∈P : D(P ||Q) ≤t}.
(11.151)
The set St is convex since D(P ||Q) is a convex function of P . Let
D∗= D(P ∗||Q) = min
P∈E D(P ||Q).
(11.152)
Then P ∗is unique, since D(P ||Q) is strictly convex in P . Now deﬁne
the set
A = SD∗+2δ ∩E
(11.153)
and
B = E −SD∗+2δ ∩E.
(11.154)
Thus, A ∪B = E. These sets are illustrated in Figure 11.7. Then
Qn(B) =

P∈E∩Pn:D(P||Q)>D∗+2δ
Qn(T (P ))
(11.155)
≤

P∈E∩Pn:D(P||Q)>D∗+2δ
2−nD(P||Q)
(11.156)
≤

P∈E∩Pn:D(P||Q)>D∗+2δ
2−n(D∗+2δ)
(11.157)
≤(n + 1)|X|2−n(D∗+2δ)
(11.158)


## PDF page 399

11.6
CONDITIONAL LIMIT THEOREM
373
E
B
A
P*
SD* + 2d
SD* + d
Q
FIGURE 11.7. Conditional limit theorem.
since there are only a polynomial number of types. On the other hand,
Qn(A) ≥Qn(SD∗+δ ∩E)
(11.159)
=

P∈E∩Pn:D(P||Q)≤D∗+δ
Qn(T (P ))
(11.160)
≥

P∈E∩Pn:D(P||Q)≤D∗+δ
1
(n + 1)|X| 2−nD(P||Q)
(11.161)
≥
1
(n + 1)|X| 2−n(D∗+δ)
for n sufﬁciently large,
(11.162)
since the sum is greater than one of the terms, and for sufﬁciently large n,
there exists at least one type in SD∗+δ ∩E ∩Pn. Then, for n sufﬁciently
large,
Pr(PXn ∈B|PXn ∈E) = Qn(B ∩E)
Qn(E)
(11.163)
≤Qn(B)
Qn(A)
(11.164)
≤(n + 1)|X|2−n(D∗+2δ)
1
(n+1)|X|2−n(D∗+δ)
(11.165)
= (n + 1)2|X|2−nδ,
(11.166)


## PDF page 400

374
INFORMATION THEORY AND STATISTICS
which goes to 0 as n →∞. Hence the conditional probability of B goes
to 0 as n →∞, which implies that the conditional probability of A goes
to 1.
We now show that all the members of A are close to P ∗in relative
entropy. For all members of A,
D(P ||Q) ≤D∗+ 2δ.
(11.167)
Hence by the “Pythagorean” theorem (Theorem 11.6.1),
D(P ||P ∗) + D(P ∗||Q) ≤D(P ||Q) ≤D∗+ 2δ,
(11.168)
which in turn implies that
D(P ||P ∗) ≤2δ,
(11.169)
since D(P ∗||Q) = D∗. Thus, Px ∈A implies that D(Px||Q) ≤D∗+ 2δ,
and therefore that D(Px||P ∗) ≤2δ. Consequently, since Pr{PXn ∈A|PXn
∈E} →1, it follows that
Pr(D(PXn||P ∗) ≤2δ|PXn ∈E) →1
(11.170)
as n →∞. By Lemma 11.6.1, the fact that the relative entropy is small
implies that the L1 distance is small, which in turn implies that maxa∈X
|PXn(a) −P ∗(a)| is small. Thus, Pr(|PXn(a) −P ∗(a)| ≥ϵ|PXn ∈E) →
0 as n →∞. Alternatively, this can be written as
Pr(X1 = a|PXn ∈E) →P ∗(a)
in probability, a ∈X.
(11.171)
In this theorem we have only proved that the marginal distribution goes
to P ∗as n →∞. Using a similar argument, we can prove a stronger
version of this theorem:
Pr(X1 = a1, X2 = a2, . . . , Xm
= am|PXn ∈E) →
m

i=1
P ∗(ai)
in probability.
(11.172)
This holds for ﬁxed m as n →∞. The result is not true for m = n, since
there are end effects; given that the type of the sequence is in E, the
last elements of the sequence can be determined from the remaining ele-
ments, and the elements are no longer independent. The conditional limit


