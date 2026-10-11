# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 25

ACKNOWLEDGMENTS
FOR THE FIRST EDITION
We wish to thank everyone who helped make this book what it is. In
particular, Aaron Wyner, Toby Berger, Masoud Salehi, Alon Orlitsky,
Jim Mazo and Andrew Barron have made detailed comments on various
drafts of the book which guided us in our ﬁnal choice of content. We
would like to thank Bob Gallager for an initial reading of the manuscript
and his encouragement to publish it. Aaron Wyner donated his new proof
with Ziv on the convergence of the Lempel-Ziv algorithm. We would
also like to thank Normam Abramson, Ed van der Meulen, Jack Salz and
Raymond Yeung for their suggested revisions.
Certain key visitors and research associates contributed as well, includ-
ing Amir Dembo, Paul Algoet, Hirosuke Yamamoto, Ben Kawabata, M.
Shimizu and Yoichiro Watanabe. We beneﬁted from the advice of John
Gill when he used this text in his class. Abbas El Gamal made invaluable
contributions, and helped begin this book years ago when we planned
to write a research monograph on multiple user information theory. We
would also like to thank the Ph.D. students in information theory as this
book was being written: Laura Ekroot, Will Equitz, Don Kimber, Mitchell
Trott, Andrew Nobel, Jim Roche, Erik Ordentlich, Elza Erkip and Vitto-
rio Castelli. Also Mitchell Oslick, Chien-Wen Tseng and Michael Morrell
were among the most active students in contributing questions and sug-
gestions to the text. Marc Goldberg and Anil Kaul helped us produce
some of the ﬁgures. Finally we would like to thank Kirsten Goodell and
Kathy Adams for their support and help in some of the aspects of the
preparation of the manuscript.
Joy Thomas would also like to thank Peter Franaszek, Steve Lavenberg,
Fred Jelinek, David Nahamoo and Lalit Bahl for their encouragment and
support during the ﬁnal stages of production of this book.
xxiii


## PDF page 26



## PDF page 27

CHAPTER 1
INTRODUCTION AND PREVIEW
Information theory answers two fundamental questions in communication
theory: What is the ultimate data compression (answer: the entropy H),
and what is the ultimate transmission rate of communication (answer: the
channel capacity C). For this reason some consider information theory
to be a subset of communication theory. We argue that it is much more.
Indeed, it has fundamental contributions to make in statistical physics
(thermodynamics), computer science (Kolmogorov complexity or algo-
rithmic complexity), statistical inference (Occam’s Razor: “The simplest
explanation is best”), and to probability and statistics (error exponents for
optimal hypothesis testing and estimation).
This “ﬁrst lecture” chapter goes backward and forward through infor-
mation theory and its naturally related ideas. The full deﬁnitions and study
of the subject begin in Chapter 2. Figure 1.1 illustrates the relationship
of information theory to other ﬁelds. As the ﬁgure suggests, information
theory intersects physics (statistical mechanics), mathematics (probability
theory), electrical engineering (communication theory), and computer sci-
ence (algorithmic complexity). We now describe the areas of intersection
in greater detail.
Electrical Engineering (Communication Theory).
In the early 1940s
it was thought to be impossible to send information at a positive rate
with negligible probability of error. Shannon surprised the communica-
tion theory community by proving that the probability of error could be
made nearly zero for all communication rates below channel capacity.
The capacity can be computed simply from the noise characteristics of
the channel. Shannon further argued that random processes such as music
and speech have an irreducible complexity below which the signal cannot
be compressed. This he named the entropy, in deference to the parallel
use of this word in thermodynamics, and argued that if the entropy of the
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
1


## PDF page 28

2
INTRODUCTION AND PREVIEW
Physics
AEP
Thermodynamics
Quantum
Information
Theory
Mathematics
Inequalities
Statistics
Hypothesis
Testing
Fisher
Information
Computer
Science
Kolmogorov
Complexity
Probability
Theory
Limit
Theorems
Large
Deviations
Communication
Theory
Limits of
Communication
Theory
Portfolio Theory
Kelly Gambling
Economics
Information
Theory
FIGURE 1.1. Relationship of information theory to other ﬁelds.
Data compression
limit
Data transmission
limit
min l(X; X )
^
max l(X; Y )
FIGURE 1.2. Information theory as the extreme points of communication theory.
source is less than the capacity of the channel, asymptotically error-free
communication can be achieved.
Information theory today represents the extreme points of the set of
all possible communication schemes, as shown in the fanciful Figure 1.2.
The data compression minimum I (X; ˆX) lies at one extreme of the set of
communication ideas. All data compression schemes require description


## PDF page 29

INTRODUCTION AND PREVIEW
3
rates at least equal to this minimum. At the other extreme is the data
transmission maximum I (X; Y), known as the channel capacity. Thus,
all modulation schemes and data compression schemes lie between these
limits.
Information theory also suggests means of achieving these ultimate
limits of communication. However, these theoretically optimal communi-
cation schemes, beautiful as they are, may turn out to be computationally
impractical. It is only because of the computational feasibility of sim-
ple modulation and demodulation schemes that we use them rather than
the random coding and nearest-neighbor decoding rule suggested by Shan-
non’s proof of the channel capacity theorem. Progress in integrated circuits
and code design has enabled us to reap some of the gains suggested by
Shannon’s theory. Computational practicality was ﬁnally achieved by the
advent of turbo codes. A good example of an application of the ideas of
information theory is the use of error-correcting codes on compact discs
and DVDs.
Recent work on the communication aspects of information theory has
concentrated on network information theory: the theory of the simultane-
ous rates of communication from many senders to many receivers in the
presence of interference and noise. Some of the trade-offs of rates between
senders and receivers are unexpected, and all have a certain mathematical
simplicity. A unifying theory, however, remains to be found.
Computer
Science
(Kolmogorov
Complexity).
Kolmogorov,
Chaitin, and Solomonoff put forth the idea that the complexity of a string
of data can be deﬁned by the length of the shortest binary computer
program for computing the string. Thus, the complexity is the minimal
description length. This deﬁnition of complexity turns out to be universal,
that is, computer independent, and is of fundamental importance. Thus,
Kolmogorov complexity lays the foundation for the theory of descriptive
complexity. Gratifyingly, the Kolmogorov complexity K is approximately
equal to the Shannon entropy H if the sequence is drawn at random from
a distribution that has entropy H. So the tie-in between information theory
and Kolmogorov complexity is perfect. Indeed, we consider Kolmogorov
complexity to be more fundamental than Shannon entropy. It is the ulti-
mate data compression and leads to a logically consistent procedure for
inference.
There is a pleasing complementary relationship between algorithmic
complexity and computational complexity. One can think about computa-
tional complexity (time complexity) and Kolmogorov complexity (pro-
gram length or descriptive complexity) as two axes corresponding to


## PDF page 30

4
INTRODUCTION AND PREVIEW
program running time and program length. Kolmogorov complexity fo-
cuses on minimizing along the second axis, and computational complexity
focuses on minimizing along the ﬁrst axis. Little work has been done on
the simultaneous minimization of the two.
Physics (Thermodynamics).
Statistical mechanics is the birthplace of
entropy and the second law of thermodynamics. Entropy always increases.
Among other things, the second law allows one to dismiss any claims to
perpetual motion machines. We discuss the second law brieﬂy in Chapter 4.
Mathematics (Probability Theory and Statistics).
The fundamental
quantities of information theory—entropy, relative entropy, and mutual
information—are deﬁned as functionals of probability distributions. In
turn, they characterize the behavior of long sequences of random variables
and allow us to estimate the probabilities of rare events (large deviation
theory) and to ﬁnd the best error exponent in hypothesis tests.
Philosophy of Science (Occam’s Razor).
William of Occam said
“Causes shall not be multiplied beyond necessity,” or to paraphrase it,
“The simplest explanation is best.” Solomonoff and Chaitin argued per-
suasively that one gets a universally good prediction procedure if one takes
a weighted combination of all programs that explain the data and observes
what they print next. Moreover, this inference will work in many problems
not handled by statistics. For example, this procedure will eventually pre-
dict the subsequent digits of π. When this procedure is applied to coin ﬂips
that come up heads with probability 0.7, this too will be inferred. When
applied to the stock market, the procedure should essentially ﬁnd all the
“laws” of the stock market and extrapolate them optimally. In principle,
such a procedure would have found Newton’s laws of physics. Of course,
such inference is highly impractical, because weeding out all computer
programs that fail to generate existing data will take impossibly long. We
would predict what happens tomorrow a hundred years from now.
Economics (Investment).
Repeated investment in a stationary stock
market results in an exponential growth of wealth. The growth rate of
the wealth is a dual of the entropy rate of the stock market. The paral-
lels between the theory of optimal investment in the stock market and
information theory are striking. We develop the theory of investment to
explore this duality.
Computation vs. Communication.
As we build larger computers
out of smaller components, we encounter both a computation limit and
a communication limit. Computation is communication limited and com-
munication is computation limited. These become intertwined, and thus


## PDF page 31

1.1
PREVIEW OF THE BOOK
5
all of the developments in communication theory via information theory
should have a direct impact on the theory of computation.
1.1
PREVIEW OF THE BOOK
The initial questions treated by information theory lay in the areas of
data compression and transmission. The answers are quantities such as
entropy and mutual information, which are functions of the probability
distributions that underlie the process of communication. A few deﬁnitions
will aid the initial discussion. We repeat these deﬁnitions in Chapter 2.
The entropy of a random variable X with a probability mass function
p(x) is deﬁned by
H(X) = −

x
p(x) log2 p(x).
(1.1)
We use logarithms to base 2. The entropy will then be measured in bits.
The entropy is a measure of the average uncertainty in the random vari-
able. It is the number of bits on average required to describe the random
variable.
Example 1.1.1
Consider a random variable that has a uniform distribu-
tion over 32 outcomes. To identify an outcome, we need a label that takes
on 32 different values. Thus, 5-bit strings sufﬁce as labels.
The entropy of this random variable is
H(X) = −
32

i=1
p(i) log p(i) = −
32

i=1
1
32 log 1
32 = log 32 = 5 bits,
(1.2)
which agrees with the number of bits needed to describe X. In this case,
all the outcomes have representations of the same length.
Now consider an example with nonuniform distribution.
Example 1.1.2
Suppose that we have a horse race with eight horses
taking part. Assume that the probabilities of winning for the eight horses
are
1
2, 1
4, 1
8, 1
16, 1
64, 1
64, 1
64, 1
64

. We can calculate the entropy of the horse
race as
H(X) = −1
2 log 1
2 −1
4 log 1
4 −1
8 log 1
8 −1
16 log 1
16 −4 1
64 log 1
64
= 2 bits.
(1.3)


## PDF page 32

6
INTRODUCTION AND PREVIEW
Suppose that we wish to send a message indicating which horse won
the race. One alternative is to send the index of the winning horse. This
description requires 3 bits for any of the horses. But the win probabilities
are not uniform. It therefore makes sense to use shorter descriptions for the
more probable horses and longer descriptions for the less probable ones,
so that we achieve a lower average description length. For example, we
could use the following set of bit strings to represent the eight horses: 0,
10, 110, 1110, 111100, 111101, 111110, 111111. The average description
length in this case is 2 bits, as opposed to 3 bits for the uniform code.
Notice that the average description length in this case is equal to the
entropy. In Chapter 5 we show that the entropy of a random variable is
a lower bound on the average number of bits required to represent the
random variable and also on the average number of questions needed to
identify the variable in a game of “20 questions.” We also show how to
construct representations that have an average length within 1 bit of the
entropy.
The concept of entropy in information theory is related to the concept of
entropy in statistical mechanics. If we draw a sequence of n independent
and identically distributed (i.i.d.) random variables, we will show that the
probability of a “typical” sequence is about 2−nH(X) and that there are
about 2nH(X) such typical sequences. This property [known as the asymp-
totic equipartition property (AEP)] is the basis of many of the proofs in
information theory. We later present other problems for which entropy
arises as a natural answer (e.g., the number of fair coin ﬂips needed to
generate a random variable).
The notion of descriptive complexity of a random variable can be
extended to deﬁne the descriptive complexity of a single string. The Kol-
mogorov complexity of a binary string is deﬁned as the length of the
shortest computer program that prints out the string. It will turn out that
if the string is indeed random, the Kolmogorov complexity is close to
the entropy. Kolmogorov complexity is a natural framework in which
to consider problems of statistical inference and modeling and leads to
a clearer understanding of Occam’s Razor: “The simplest explanation is
best.” We describe some simple properties of Kolmogorov complexity in
Chapter 1.
Entropy is the uncertainty of a single random variable. We can deﬁne
conditional entropy H(X|Y), which is the entropy of a random variable
conditional on the knowledge of another random variable. The reduction
in uncertainty due to another random variable is called the mutual infor-
mation. For two random variables X and Y this reduction is the mutual


