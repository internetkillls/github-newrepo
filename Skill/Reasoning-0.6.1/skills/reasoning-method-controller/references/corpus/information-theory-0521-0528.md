# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 521

14.11
KOLMOGOROV COMPLEXITY AND UNIVERSAL PROBABILITY
495
≤2−1 	
2⌊log PU (x)⌋+ 2⌊log PU (x)⌋−1 + 2⌊log PU (x)⌋−2 + · · ·

(14.100)
= 2−12⌊log PU (x)⌋

1 + 1
2 + 1
4 + · · ·

(14.101)
= 2−12⌊log PU (x)⌋2
(14.102)
≤PU(x),
(14.103)
where (14.100) is true because there is at most one node at each level
that prints out a particular x. More precisely, the nk’s on the winnowed
list for a particular output string x are all different integers. Hence,

k
2−(nk+1) ≤

x

k:xk=x
2−(nk+1) ≤

x
PU(x) ≤1,
(14.104)
and we can construct a tree with the nodes labeled by the triplets.
If we are given the tree constructed above, it is easy to identify a given
x by the path to the lowest depth node that prints x. Call this node ˜p.
(By construction, l( ˜p) ≤log
1
PU (x) + 2.) To use this tree in a program
to print x, we specify ˜p and ask the computer to execute the foregoing
simulation of all programs. Then the computer will construct the tree as
described above and wait for the particular node ˜p to be assigned. Since
the computer executes the same construction as the sender, eventually the
node ˜p will be assigned. At this point, the computer will halt and print
out the x assigned to that node.
This is an effective (ﬁnite, mechanical) procedure for the computer to
reconstruct x. However, there is no effective procedure to ﬁnd the lowest
depth node corresponding to x. All that we have proved is that there is
an (inﬁnite) tree with a node corresponding to x at level ⌈log
1
PU (x)⌉+ 1.
But this accomplishes our purpose.
With reference to the example, the description of x = 1110 is the path
to the node (p3, x3, n3) (i.e., 01), and the description of x = 1111 is the
path 00001. If we wish to describe the string 1110, we ask the computer
to perform the (simulation) tree construction until node 01 is assigned.
Then we ask the computer to execute the program corresponding to node
01 (i.e., p3). The output of this program is the desired string, x = 1110.
The length of the program to reconstruct x is essentially the length of
the description of the position of the lowest depth node ˜p corresponding


## PDF page 522

496
KOLMOGOROV COMPLEXITY
to x in the tree. The length of this program for x is l( ˜p) + c, where
l( ˜p) ≤

log
1
PU(x)

+ 1,
(14.105)
and hence the complexity of x satisﬁes
K(x) ≤

log
1
PU(x)

+ c.
(14.106)
14.12
KOLMOGOROV SUFFICIENT STATISTIC
Suppose that we are given a sample sequence from a Bernoulli(θ) process.
What are the regularities or deviations from randomness in this sequence?
One way to address the question is to ﬁnd the Kolmogorov complexity
K(xn|n), which we discover to be roughly nH0(θ) + log n + c. Since,
for θ ̸= 1
2, this is much less than n, we conclude that xn has structure
and is not randomly drawn Bernoulli(1
2). But what is the structure? The
ﬁrst attempt to ﬁnd the structure is to investigate the shortest program p∗
for xn. But the shortest description of p∗is about as long as p∗itself;
otherwise, we could further compress the description of xn, contradicting
the minimality of p∗. So this attempt is fruitless.
A hint at a good approach comes from an examination of the way in
which p∗describes xn. The program “The sequence has k 1’s; of such
sequences, it is the ith” is optimal to ﬁrst order for Bernoulli(θ) sequences.
We note that it is a two-stage description, and all of the structure of the
sequence is captured in the ﬁrst stage. Moreover, xn is maximally complex
given the ﬁrst stage of the description. The ﬁrst stage, the description of
k, requires log(n + 1) bits and deﬁnes a set S = {x ∈{0, 1}n :  xi = k}.
The second stage requires log |S| = log
	n
k

≈nH0(xn) ≈nH0(θ) bits and
reveals nothing extraordinary about xn.
We mimic this process for general sequences by looking for a simple
set S that contains xn. We then follow it with a brute-force description of
xn in S using log |S| bits. We begin with a deﬁnition of the smallest set
containing xn that is describable in no more than k bits.
Deﬁnition
The Kolmogorov structure function Kk(xn|n) of a binary
string x ∈{0, 1}n is deﬁned as
Kk(xn|n) =
min
p : l(p) ≤k
U(p, n) = S
xn ∈S ⊆{0, 1}n
log |S|.
(14.107)


## PDF page 523

14.12
KOLMOGOROV SUFFICIENT STATISTIC
497
The set S is the smallest set that can be described with no more than
k bits and which includes xn. By U(p, n) = S, we mean that running the
program p with data n on the universal computer U will print out the
indicator function of the set S.
Deﬁnition
For a given small constant c, let k∗be the least k such that
Kk(xn|n) + k ≤K(xn|n) + c.
(14.108)
Let S∗∗be the corresponding set and let p∗∗be the program that prints out
the indicator function of S∗∗. Then we shall say that p∗∗is a Kolmogorov
minimal sufﬁcient statistic for xn.
Consider the programs p∗describing sets S∗such that
Kk(xn|n) + k = K(xn|n).
(14.109)
All the programs p∗are “sufﬁcient statistics” in that the complexity of
xn given S∗is maximal. But the minimal sufﬁcient statistic is the shortest
“sufﬁcient statistic.”
The equality in the deﬁnition above is up to a large constant depending
on the computer U. Then k∗corresponds to the least k for which the two-
stage description of xn is as good as the best single-stage description of
xn. The second stage of the description merely provides the index of xn
within the set S∗∗; this takes Kk(xn|n) bits if xn is conditionally maximally
complex given the set S∗∗. Hence the set S∗∗captures all the structure
within xn. The remaining description of xn within S∗∗is essentially the
description of the randomness within the string. Hence S∗∗or p∗∗is called
the Kolmogorov sufﬁcient statistic for xn.
This is parallel to the deﬁnition of a sufﬁcient statistic in mathematical
statistics. A statistic T is said to be sufﬁcient for a parameter θ if the
distribution of the sample given the sufﬁcient statistic is independent of
the parameter; that is,
θ →T (X) →X
(14.110)
forms a Markov chain in that order. For the Kolmogorov sufﬁcient statistic,
the program p∗∗is sufﬁcient for the “structure” of the string xn; the
remainder of the description of xn is essentially independent of the “struc-
ture” of xn. In particular, xn is maximally complex given S∗∗.
A typical graph of the structure function is illustrated in Figure 14.4.
When k = 0, the only set that can be described is the entire set {0, 1}n,


## PDF page 524

498
KOLMOGOROV COMPLEXITY
Slope = −1
k*
K(x)
k
n
Kk(x)
FIGURE 14.4. Kolmogorov sufﬁcient statistic.
so that the corresponding log set size is n. As we increase k, the size of
the set drops rapidly until
k + Kk(xn|n) ≈K(xn|n).
(14.111)
After this, each additional bit of k reduces the set by half, and we pro-
ceed along the line of slope −1 until k = K(xn|n). For k ≥K(xn|n), the
smallest set that can be described that includes xn is the singleton {xn},
and hence Kk(xn|n) = 0.
We will now illustrate the concept with a few examples.
1. Bernoulli(θ) sequence. Consider a sample of length n from a
Bernoulli sequence with an unknown parameter θ. As discussed in
Example 14.2, we can describle this sequence with nH
	 k
n

+ 1
2 log n
bits using a two stage description where we describe k in the ﬁrst
stage (using log n bits) and then describe the sequence within all
sequences with k ones (using log
	n
k

bits). However, we can use an
even shorter ﬁrst stage description. Instead of describing k exactly,
we divide the range of k into bins and describe k only to an accu-
racy of

k
n
n−k
n
√n using 1
2 log n bits. Then we describe the actual


## PDF page 525

14.12
KOLMOGOROV SUFFICIENT STATISTIC
499
Slope = −1
log n
1
2
nH0(p) +    log n
k
n
Kk(x)
1
2
FIGURE 14.5. Kolmogorov sufﬁcient statistic for a Bernoulli sequence.
sequence among all sequences whose type is in the same bin as k.
The size of the set of all sequences with l ones, l ∈k ±

k
n
n−k
n
√n is
nH
	k
n

+ o(n) by Stirling’s formula, so the total description length
is still nH
	k
n

+ 1
2 log n + o(n), but the description length of the
Kolmogorov sufﬁcient statistics is k∗≈1
n log n.
2. Sample from a Markov chain. In the same vein as the preceding
example, consider a sample from a ﬁrst-order binary Markov chain.
In this case again, p∗∗will correspond to describing the Markov type
of the sequence (the number of occurrences of 00’s, 01’s, 10’s, and
11’s in the sequence); this conveys all the structure in the sequence.
The remainder of the description will be the index of the sequence
in the set of all sequences of this Markov type. Hence, in this case,
k∗≈2( 1
2 log n) = log n, corresponding to describing two elements
of the conditional joint type to appropriate accuracy. (The other
elements of the conditional joint type can be determined from these
two.)
3. Mona Lisa.
Consider an image that consists of a gray circle on a
white background. The circle is not uniformly gray but Bernoulli
with parameter θ. This is illustrated in Figure 14.6. In this case, the
best two-stage description is ﬁrst to describe the size and position of


## PDF page 526

500
KOLMOGOROV COMPLEXITY
FIGURE 14.6. Mona Lisa.
the circle and its average gray level and then to describe the index of
the circle among all the circles with the same gray level. Assuming
an n-pixel image (of size √n by √n), there are about n + 1 possible
gray levels, and there are about (√n)3 distinguishable circles. Hence,
k∗≈5
2 log n in this case.
14.13
MINIMUM DESCRIPTION LENGTH PRINCIPLE
A natural extension of Occam’s razor occurs when we need to describe
data drawn from an unknown distribution. Let X1, X2, . . . , Xn be drawn
i.i.d. according to probability mass function p(x). We assume that we
do not know p(x), but know that p(x) ∈P, a class of probability mass
functions. Given the data, we can estimate the probability mass function in
P that best ﬁts the data. For simple classes P (e.g., if P has only ﬁnitely
many distributions), the problem is straightforward, and the maximum
likelihood procedure [i.e., ﬁnd ˆp ∈P that maximizes ˆp(X1, X2, . . . , Xn)]
works well. However, if the class P is rich enough, there is a problem
of overﬁtting the data. For example, if X1, X2, . . . , Xn are continuous
random variables, and if P is the set of all probability distributions, the
maximum likelihood estimator given X1, X2, . . . , Xn is a distribution that
places a single mass point of weight 1
n at each observed value. Clearly, this
estimate is too closely tied to actual observed data and does not capture
any of the structure of the underlying distribution.
To get around this problem, various methods have been applied. In the
simplest case, the data are assumed to come from some parametric distri-
bution (e.g., the normal distribution), and the parameters of the distribution
are estimated from the data. To validate this method, the data should be
tested to check whether the distribution “looks” normal, and if the data
pass the test, we could use this description of the data. A more general
procedure is to take the maximum likelihood estimate and smooth it out
to obtain a smooth density. With enough data, and appropriate smoothness


## PDF page 527

SUMMARY
501
conditions, it is possible to make good estimates of the original density.
This process is called kernel density estimation.
However, the theory of Kolmogorov complexity (or the Kolmogorov
sufﬁcient statistic) suggests a different procedure: Find the p ∈P that
minimizes
Lp(X1, X2, . . . , Xn) = K(p) + log
1
p(X1, X2, . . . , Xn).
(14.112)
This is the length of a two-stage description of the data, where we ﬁrst
describe the distribution p and then, given the distribution, construct the
Shannon code and describe the data using log
1
p(X1,X2,...,Xn) bits. This pro-
cedure is a special case of what is termed the minimum description length
(MDL) principle: Given data and a choice of models, choose the model
such that the description of the model plus the conditional description of
the data is as short as possible.
SUMMARY
Deﬁnition.
The Kolmogorov complexity K(x) of a string x is
K(x) =
min
p: U(p)=x l(p)
(14.113)
K(x|l(x)) =
min
p: U(p,l(x))=x l(p).
(14.114)
Universality of Kolmogorov complexity. There exists a universal
computer U such that for any other computer A,
KU(x) ≤KA(x) + cA
(14.115)
for any string x, where the constant cA does not depend on x. If U and
A are universal, |KU(x) −KA(x)| ≤c for all x.
Upper bound on Kolmogorov complexity
K(x|l(x)) ≤l(x) + c
(14.116)
K(x) ≤K(x|l(x)) + 2 log l(x) + c.
(14.117)


## PDF page 528

502
KOLMOGOROV COMPLEXITY
Kolmogorov complexity and entropy. If X1, X2, . . . are i.i.d. integer-
valued random variables with entropy H, there exists a constant c such
that for all n,
H ≤1
nEK(Xn|n) ≤H + |X|log n
n
+ c
n.
(14.118)
Lower bound on Kolmogorov complexity. There are no more than
2k strings x with complexity K(x) < k. If X1, X2, . . . , Xn are drawn
according to a Bernoulli(1
2) process,
Pr (K(X1X2 . . . Xn|n) ≤n −k) ≤2−k.
(14.119)
Deﬁnition
A sequence x is said to be incompressible if
K(x1x2 . . . xn|n)/n →1.
Strong law of large numbers for incompressible sequences
K(x1, x2, . . . , xn)
n
→1 ⇒1
n
n

i=1
xi →1
2.
(14.120)
Deﬁnition
The universal probability of a string x is
PU(x) =

p: U(p)=x
2−l(p) = Pr(U(p) = x).
(14.121)
Universality of PU(x). For every computer A,
PU(x) ≥cAPA(x)
(14.122)
for every string x ∈{0, 1}∗, where the constant cA depends only on U
and A.
Deﬁnition
 = 
p: U(p) halts 2−l(p) = Pr(U(p) halts) is the proba-
bility that the computer halts when the input p to the computer is a
binary string drawn according to a Bernoulli(1
2) process.
Properties of 
1.  is not computable.
2.  is a “philosopher’s stone”.
3.  is algorithmically random (incompressible).


