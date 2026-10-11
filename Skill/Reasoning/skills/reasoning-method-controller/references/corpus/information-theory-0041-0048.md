# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 41

2.1
ENTROPY
15
justify the deﬁnition of entropy; instead, we show that it arises as the
answer to a number of natural questions, such as “What is the average
length of the shortest description of the random variable?” First, we derive
some immediate consequences of the deﬁnition.
Lemma 2.1.1
H(X) ≥0.
Proof:
0 ≤p(x) ≤1 implies that log
1
p(x) ≥0.
□
Lemma 2.1.2
Hb(X) = (logb a)Ha(X).
Proof:
logb p = logb a loga p.
□
The second property of entropy enables us to change the base of the
logarithm in the deﬁnition. Entropy can be changed from one base to
another by multiplying by the appropriate factor.
Example 2.1.1
Let
X =

1
with probability p,
0
with probability 1 −p.
(2.4)
Then
H(X) = −p log p −(1 −p) log(1 −p) def
== H(p).
(2.5)
In particular, H(X) = 1 bit when p = 1
2. The graph of the function H(p)
is shown in Figure 2.1. The ﬁgure illustrates some of the basic properties
of entropy: It is a concave function of the distribution and equals 0 when
p = 0 or 1. This makes sense, because when p = 0 or 1, the variable
is not random and there is no uncertainty. Similarly, the uncertainty is
maximum when p = 1
2, which also corresponds to the maximum value of
the entropy.
Example 2.1.2
Let
X =



a
with probability 1
2,
b
with probability 1
4,
c
with probability 1
8,
d
with probability 1
8.
(2.6)
The entropy of X is
H(X) = −1
2 log 1
2 −1
4 log 1
4 −1
8 log 1
8 −1
8 log 1
8 = 7
4 bits.
(2.7)


## PDF page 42

16
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
p
H(p)
FIGURE 2.1. H(p) vs. p.
Suppose that we wish to determine the value of X with the minimum
number of binary questions. An efﬁcient ﬁrst question is “Is X = a?”
This splits the probability in half. If the answer to the ﬁrst question is
no, the second question can be “Is X = b?” The third question can be
“Is X = c?” The resulting expected number of binary questions required
is 1.75. This turns out to be the minimum expected number of binary
questions required to determine the value of X. In Chapter 5 we show that
the minimum expected number of binary questions required to determine
X lies between H(X) and H(X) + 1.
2.2
JOINT ENTROPY AND CONDITIONAL ENTROPY
We deﬁned the entropy of a single random variable in Section 2.1. We
now extend the deﬁnition to a pair of random variables. There is nothing
really new in this deﬁnition because (X, Y) can be considered to be a
single vector-valued random variable.
Deﬁnition
The joint entropy H(X, Y) of a pair of discrete random
variables (X, Y) with a joint distribution p(x, y) is deﬁned as
H(X, Y) = −

x∈X

y∈Y
p(x, y) log p(x, y),
(2.8)


## PDF page 43

2.2
JOINT ENTROPY AND CONDITIONAL ENTROPY
17
which can also be expressed as
H(X, Y) = −E log p(X, Y).
(2.9)
We also deﬁne the conditional entropy of a random variable given
another as the expected value of the entropies of the conditional distribu-
tions, averaged over the conditioning random variable.
Deﬁnition
If (X, Y) ∼p(x, y), the conditional entropy H(Y|X) is
deﬁned as
H(Y|X) =

x∈X
p(x)H(Y|X = x)
(2.10)
= −

x∈X
p(x)

y∈Y
p(y|x) log p(y|x)
(2.11)
= −

x∈X

y∈Y
p(x, y) log p(y|x)
(2.12)
= −E log p(Y|X).
(2.13)
The naturalness of the deﬁnition of joint entropy and conditional entropy
is exhibited by the fact that the entropy of a pair of random variables is
the entropy of one plus the conditional entropy of the other. This is proved
in the following theorem.
Theorem 2.2.1
(Chain rule)
H(X, Y) = H(X) + H(Y|X).
(2.14)
Proof
H(X, Y) = −

x∈X

y∈Y
p(x, y) log p(x, y)
(2.15)
= −

x∈X

y∈Y
p(x, y) log p(x)p(y|x)
(2.16)
= −

x∈X

y∈Y
p(x, y) log p(x) −

x∈X

y∈Y
p(x, y) log p(y|x)
(2.17)
= −

x∈X
p(x) log p(x) −

x∈X

y∈Y
p(x, y) log p(y|x)
(2.18)
= H(X) + H(Y|X).
(2.19)


## PDF page 44

18
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
Equivalently, we can write
log p(X, Y) = log p(X) + log p(Y|X)
(2.20)
and take the expectation of both sides of the equation to obtain the
theorem.
□
Corollary
H(X, Y|Z) = H(X|Z) + H(Y|X, Z).
(2.21)
Proof:
The proof follows along the same lines as the theorem.
□
Example 2.2.1
Let (X, Y) have the following joint distribution:
The marginal distribution of X is ( 1
2, 1
4, 1
8, 1
8) and the marginal distribution
of Y is ( 1
4, 1
4, 1
4, 1
4), and hence H(X) = 7
4 bits and H(Y) = 2 bits. Also,
H(X|Y) =
4

i=1
p(Y = i)H(X|Y = i)
(2.22)
= 1
4H
1
2, 1
4, 1
8, 1
8

+ 1
4H
1
4, 1
2, 1
8, 1
8

+ 1
4H
1
4, 1
4, 1
4, 1
4

+ 1
4H(1, 0, 0, 0)
(2.23)
= 1
4 × 7
4 + 1
4 × 7
4 + 1
4 × 2 + 1
4 × 0
(2.24)
= 11
8 bits.
(2.25)
Similarly, H(Y|X) = 13
8 bits and H(X, Y) = 27
8 bits.
Remark
Note that H(Y|X) ̸= H(X|Y). However, H(X) −H(X|Y) =
H(Y)−H(Y|X), a property that we exploit later.


## PDF page 45

2.3
RELATIVE ENTROPY AND MUTUAL INFORMATION
19
2.3
RELATIVE ENTROPY AND MUTUAL INFORMATION
The entropy of a random variable is a measure of the uncertainty of the
random variable; it is a measure of the amount of information required on
the average to describe the random variable. In this section we introduce
two related concepts: relative entropy and mutual information.
The relative entropy is a measure of the distance between two distribu-
tions. In statistics, it arises as an expected logarithm of the likelihood ratio.
The relative entropy D(p||q) is a measure of the inefﬁciency of assuming
that the distribution is q when the true distribution is p. For example, if
we knew the true distribution p of the random variable, we could con-
struct a code with average description length H(p). If, instead, we used
the code for a distribution q, we would need H(p) + D(p||q) bits on the
average to describe the random variable.
Deﬁnition
The relative entropy or Kullback–Leibler distance between
two probability mass functions p(x) and q(x) is deﬁned as
D(p||q) =

x∈X
p(x) log p(x)
q(x)
(2.26)
= Ep log p(X)
q(X).
(2.27)
In the above deﬁnition, we use the convention that 0 log 0
0 = 0 and the
convention (based on continuity arguments) that 0 log 0
q = 0 and p log p
0 =
∞. Thus, if there is any symbol x ∈X such that p(x) > 0 and q(x) = 0,
then D(p||q) = ∞.
We will soon show that relative entropy is always nonnegative and is
zero if and only if p = q. However, it is not a true distance between
distributions since it is not symmetric and does not satisfy the triangle
inequality. Nonetheless, it is often useful to think of relative entropy as a
“distance” between distributions.
We now introduce mutual information, which is a measure of the
amount of information that one random variable contains about another
random variable. It is the reduction in the uncertainty of one random
variable due to the knowledge of the other.
Deﬁnition
Consider two random variables X and Y with a joint proba-
bility mass function p(x, y) and marginal probability mass functions p(x)
and p(y). The mutual information I (X; Y) is the relative entropy between


## PDF page 46

20
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
the joint distribution and the product distribution p(x)p(y):
I (X; Y) =

x∈X

y∈Y
p(x, y) log p(x, y)
p(x)p(y)
(2.28)
= D(p(x, y)||p(x)p(y))
(2.29)
= Ep(x,y) log p(X, Y)
p(X)p(Y).
(2.30)
In Chapter 8 we generalize this deﬁnition to continuous random vari-
ables, and in (8.54) to general random variables that could be a mixture
of discrete and continuous random variables.
Example 2.3.1
Let X = {0, 1} and consider two distributions p and q
on X. Let p(0) = 1 −r, p(1) = r, and let q(0) = 1 −s, q(1) = s. Then
D(p||q) = (1 −r) log 1 −r
1 −s + r log r
s
(2.31)
and
D(q||p) = (1 −s) log 1 −s
1 −r + s log s
r .
(2.32)
If r = s, then D(p||q) = D(q||p) = 0. If r = 1
2, s = 1
4, we can calculate
D(p||q) = 1
2 log
1
2
3
4
+ 1
2 log
1
2
1
4
= 1 −1
2 log 3 = 0.2075 bit,
(2.33)
whereas
D(q||p) = 3
4 log
3
4
1
2
+ 1
4 log
1
4
1
2
= 3
4 log 3 −1 = 0.1887 bit.
(2.34)
Note that D(p||q) ̸= D(q||p) in general.
2.4
RELATIONSHIP BETWEEN ENTROPY AND MUTUAL
INFORMATION
We can rewrite the deﬁnition of mutual information I (X; Y) as
I (X; Y) =

x,y
p(x, y) log p(x, y)
p(x)p(y)
(2.35)


## PDF page 47

2.4
RELATIONSHIP BETWEEN ENTROPY AND MUTUAL INFORMATION
21
=

x,y
p(x, y) log p(x|y)
p(x)
(2.36)
= −

x,y
p(x, y) log p(x) +

x,y
p(x, y) log p(x|y)
(2.37)
= −

x
p(x) log p(x) −
	
−

x,y
p(x, y) log p(x|y)

(2.38)
= H(X) −H(X|Y).
(2.39)
Thus, the mutual information I (X; Y) is the reduction in the uncertainty
of X due to the knowledge of Y.
By symmetry, it also follows that
I (X; Y) = H(Y) −H(Y|X).
(2.40)
Thus, X says as much about Y as Y says about X.
Since H(X, Y) = H(X) + H(Y|X), as shown in Section 2.2, we have
I (X; Y) = H(X) + H(Y) −H(X, Y).
(2.41)
Finally, we note that
I (X; X) = H(X) −H(X|X) = H(X).
(2.42)
Thus, the mutual information of a random variable with itself is the
entropy of the random variable. This is the reason that entropy is some-
times referred to as self-information.
Collecting these results, we have the following theorem.
Theorem 2.4.1
(Mutual information and entropy)
I (X; Y) = H(X) −H(X|Y)
(2.43)
I (X; Y) = H(Y) −H(Y|X)
(2.44)
I (X; Y) = H(X) + H(Y) −H(X, Y)
(2.45)
I (X; Y) = I (Y; X)
(2.46)
I (X; X) = H(X).
(2.47)


## PDF page 48

22
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
H(X,Y)
H(Y |X)
H(X|Y )
H(Y)
I(X;Y)
H(X )
FIGURE 2.2. Relationship between entropy and mutual information.
The relationship between H(X), H(Y), H(X, Y), H(X|Y), H(Y|X),
and I (X; Y) is expressed in a Venn diagram (Figure 2.2). Notice that
the mutual information I (X; Y) corresponds to the intersection of the
information in X with the information in Y.
Example 2.4.1
For the joint distribution of Example 2.2.1, it is easy to
calculate the mutual information I (X; Y) = H(X) −H(X|Y) = H(Y) −
H(Y|X) = 0.375 bit.
2.5
CHAIN RULES FOR ENTROPY, RELATIVE ENTROPY,
AND MUTUAL INFORMATION
We now show that the entropy of a collection of random variables is the
sum of the conditional entropies.
Theorem 2.5.1
(Chain rule for entropy)
Let X1, X2, . . . , Xn be drawn
according to p(x1, x2, . . . , xn). Then
H(X1, X2, . . . , Xn) =
n

i=1
H(Xi|Xi−1, . . . , X1).
(2.48)
Proof:
By repeated application of the two-variable expansion rule for
entropies, we have
H(X1, X2) = H(X1) + H(X2|X1),
(2.49)
H(X1, X2, X3) = H(X1) + H(X2, X3|X1)
(2.50)


