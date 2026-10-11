# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 33

1.1
PREVIEW OF THE BOOK
7
information
I (X; Y) = H(X) −H(X|Y) =

x,y
p(x, y) log p(x, y)
p(x)p(y).
(1.4)
The mutual information I (X; Y) is a measure of the dependence between
the two random variables. It is symmetric in X and Y and always non-
negative and is equal to zero if and only if X and Y are independent.
A communication channel is a system in which the output depends
probabilistically on its input. It is characterized by a probability transition
matrix p(y|x) that determines the conditional distribution of the output
given the input. For a communication channel with input X and output
Y, we can deﬁne the capacity C by
C = max
p(x) I (X; Y).
(1.5)
Later we show that the capacity is the maximum rate at which we can send
information over the channel and recover the information at the output
with a vanishingly low probability of error. We illustrate this with a few
examples.
Example 1.1.3
(Noiseless binary channel)
For this channel, the binary
input is reproduced exactly at the output. This channel is illustrated in
Figure 1.3. Here, any transmitted bit is received without error. Hence,
in each transmission, we can send 1 bit reliably to the receiver, and the
capacity is 1 bit. We can also calculate the information capacity C =
max I (X; Y) = 1 bit.
Example 1.1.4
(Noisy four-symbol channel)
Consider the channel
shown in Figure 1.4. In this channel, each input letter is received either as
the same letter with probability 1
2 or as the next letter with probability 1
2.
If we use all four input symbols, inspection of the output would not reveal
with certainty which input symbol was sent. If, on the other hand, we use
1
0
1
0
FIGURE 1.3. Noiseless binary channel. C = 1 bit.


## PDF page 34

8
INTRODUCTION AND PREVIEW
1
2
3
4
1
2
3
4
FIGURE 1.4. Noisy channel.
only two of the inputs (1 and 3, say), we can tell immediately from the
output which input symbol was sent. This channel then acts like the noise-
less channel of Example 1.1.3, and we can send 1 bit per transmission
over this channel with no errors. We can calculate the channel capacity
C = max I (X; Y) in this case, and it is equal to 1 bit per transmission,
in agreement with the analysis above.
In general, communication channels do not have the simple structure of
this example, so we cannot always identify a subset of the inputs to send
information without error. But if we consider a sequence of transmissions,
all channels look like this example and we can then identify a subset of the
input sequences (the codewords) that can be used to transmit information
over the channel in such a way that the sets of possible output sequences
associated with each of the codewords are approximately disjoint. We can
then look at the output sequence and identify the input sequence with a
vanishingly low probability of error.
Example 1.1.5
(Binary symmetric channel)
This is the basic example
of a noisy communication system. The channel is illustrated in Figure 1.5.
1 −p
1 −p
0
0
1
1
p
p
FIGURE 1.5. Binary symmetric channel.


## PDF page 35

1.1
PREVIEW OF THE BOOK
9
The channel has a binary input, and its output is equal to the input with
probability 1 −p. With probability p, on the other hand, a 0 is received
as a 1, and vice versa. In this case, the capacity of the channel can be cal-
culated to be C = 1 + p log p + (1 −p) log(1 −p) bits per transmission.
However, it is no longer obvious how one can achieve this capacity. If we
use the channel many times, however, the channel begins to look like the
noisy four-symbol channel of Example 1.1.4, and we can send informa-
tion at a rate C bits per transmission with an arbitrarily low probability
of error.
The ultimate limit on the rate of communication of information over
a channel is given by the channel capacity. The channel coding theorem
shows that this limit can be achieved by using codes with a long block
length. In practical communication systems, there are limitations on the
complexity of the codes that we can use, and therefore we may not be
able to achieve capacity.
Mutual information turns out to be a special case of a more general
quantity called relative entropy D(p||q), which is a measure of the “dis-
tance” between two probability mass functions p and q. It is deﬁned
as
D(p||q) =

x
p(x) log p(x)
q(x) .
(1.6)
Although relative entropy is not a true metric, it has some of the properties
of a metric. In particular, it is always nonnegative and is zero if and only
if p = q. Relative entropy arises as the exponent in the probability of
error in a hypothesis test between distributions p and q. Relative entropy
can be used to deﬁne a geometry for probability distributions that allows
us to interpret many of the results of large deviation theory.
There are a number of parallels between information theory and the
theory of investment in a stock market. A stock market is deﬁned by a
random vector X whose elements are nonnegative numbers equal to the
ratio of the price of a stock at the end of a day to the price at the beginning
of the day. For a stock market with distribution F(x), we can deﬁne the
doubling rate W as
W =
max
b:bi≥0, bi=1

log btx dF(x).
(1.7)
The doubling rate is the maximum asymptotic exponent in the growth
of wealth. The doubling rate has a number of properties that parallel the
properties of entropy. We explore some of these properties in Chapter 16.


## PDF page 36

10
INTRODUCTION AND PREVIEW
The quantities H, I, C, D, K, W arise naturally in the following areas:
• Data compression. The entropy H of a random variable is a lower
bound on the average length of the shortest description of the random
variable. We can construct descriptions with average length within 1
bit of the entropy. If we relax the constraint of recovering the source
perfectly, we can then ask what communication rates are required to
describe the source up to distortion D? And what channel capacities
are sufﬁcient to enable the transmission of this source over the chan-
nel and its reconstruction with distortion less than or equal to D?
This is the subject of rate distortion theory.
When we try to formalize the notion of the shortest description
for nonrandom objects, we are led to the deﬁnition of Kolmogorov
complexity K. Later, we show that Kolmogorov complexity is uni-
versal and satisﬁes many of the intuitive requirements for the theory
of shortest descriptions.
• Data transmission. We consider the problem of transmitting infor-
mation so that the receiver can decode the message with a small prob-
ability of error. Essentially, we wish to ﬁnd codewords (sequences
of input symbols to a channel) that are mutually far apart in the
sense that their noisy versions (available at the output of the channel)
are distinguishable. This is equivalent to sphere packing in high-
dimensional space. For any set of codewords it is possible to calculate
the probability that the receiver will make an error (i.e., make an
incorrect decision as to which codeword was sent). However, in most
cases, this calculation is tedious.
Using a randomly generated code, Shannon showed that one can
send information at any rate below the capacity C of the channel
with an arbitrarily low probability of error. The idea of a randomly
generated code is very unusual. It provides the basis for a simple
analysis of a very difﬁcult problem. One of the key ideas in the proof
is the concept of typical sequences. The capacity C is the logarithm
of the number of distinguishable input signals.
• Network information theory. Each of the topics mentioned previously
involves a single source or a single channel. What if one wishes to com-
press each of many sources and then put the compressed descriptions
together into a joint reconstruction of the sources? This problem is
solved by the Slepian–Wolf theorem. Or what if one has many senders
sending information independently to a common receiver? What is the
channel capacity of this channel? This is the multiple-access channel
solved by Liao and Ahlswede. Or what if one has one sender and many


## PDF page 37

1.1
PREVIEW OF THE BOOK
11
receivers and wishes to communicate (perhaps different) information
simultaneously to each of the receivers? This is the broadcast channel.
Finally, what if one has an arbitrary number of senders and receivers in
an environment of interference and noise. What is the capacity region
of achievable rates from the various senders to the receivers? This is
the general network information theory problem. All of the preceding
problems fall into the general area of multiple-user or network informa-
tion theory. Although hopes for a comprehensive theory for networks
may be beyond current research techniques, there is still some hope that
all the answers involve only elaborate forms of mutual information and
relative entropy.
• Ergodic theory. The asymptotic equipartition theorem states that most
sample n-sequences of an ergodic process have probability about 2−nH
and that there are about 2nH such typical sequences.
• Hypothesis testing. The relative entropy D arises as the exponent in
the probability of error in a hypothesis test between two distributions.
It is a natural measure of distance between distributions.
• Statistical mechanics. The entropy H arises in statistical mechanics
as a measure of uncertainty or disorganization in a physical system.
Roughly speaking, the entropy is the logarithm of the number of
ways in which the physical system can be conﬁgured. The second law
of thermodynamics says that the entropy of a closed system cannot
decrease. Later we provide some interpretations of the second law.
• Quantum mechanics.
Here, von Neumann entropy S = tr(ρ ln ρ) =

i λi log λi plays the role of classical Shannon–Boltzmann entropy
H = −
i pi log pi. Quantum mechanical versions of data compres-
sion and channel capacity can then be found.
• Inference. We can use the notion of Kolmogorov complexity K to
ﬁnd the shortest description of the data and use that as a model to
predict what comes next. A model that maximizes the uncertainty or
entropy yields the maximum entropy approach to inference.
• Gambling and investment.
The optimal exponent in the growth rate
of wealth is given by the doubling rate W. For a horse race with
uniform odds, the sum of the doubling rate W and the entropy H is
constant. The increase in the doubling rate due to side information is
equal to the mutual information I between a horse race and the side
information. Similar results hold for investment in the stock market.
• Probability theory.
The asymptotic equipartition property (AEP)
shows that most sequences are typical in that they have a sam-
ple entropy close to H. So attention can be restricted to these
approximately 2nH typical sequences. In large deviation theory, the


## PDF page 38

12
INTRODUCTION AND PREVIEW
probability of a set is approximately 2−nD, where D is the relative
entropy distance between the closest element in the set and the true
distribution.
• Complexity theory. The Kolmogorov complexity K is a measure of
the descriptive complexity of an object. It is related to, but different
from, computational complexity, which measures the time or space
required for a computation.
Information-theoretic quantities such as entropy and relative entropy
arise again and again as the answers to the fundamental questions in
communication and statistics. Before studying these questions, we shall
study some of the properties of the answers. We begin in Chapter 2 with
the deﬁnitions and basic properties of entropy, relative entropy, and mutual
information.


## PDF page 39

CHAPTER 2
ENTROPY, RELATIVE ENTROPY,
AND MUTUAL INFORMATION
In this chapter we introduce most of the basic deﬁnitions required for
subsequent development of the theory. It is irresistible to play with their
relationships and interpretations, taking faith in their later utility. After
deﬁning entropy and mutual information, we establish chain rules, the
nonnegativity of mutual information, the data-processing inequality, and
illustrate these deﬁnitions by examining sufﬁcient statistics and Fano’s
inequality.
The concept of information is too broad to be captured completely by
a single deﬁnition. However, for any probability distribution, we deﬁne a
quantity called the entropy, which has many properties that agree with the
intuitive notion of what a measure of information should be. This notion is
extended to deﬁne mutual information, which is a measure of the amount
of information one random variable contains about another. Entropy then
becomes the self-information of a random variable. Mutual information is
a special case of a more general quantity called relative entropy, which is
a measure of the distance between two probability distributions. All these
quantities are closely related and share a number of simple properties,
some of which we derive in this chapter.
In later chapters we show how these quantities arise as natural answers
to a number of questions in communication, statistics, complexity, and
gambling. That will be the ultimate test of the value of these deﬁnitions.
2.1
ENTROPY
We ﬁrst introduce the concept of entropy, which is a measure of the
uncertainty of a random variable. Let X be a discrete random variable
with alphabet X and probability mass function p(x) = Pr{X = x}, x ∈X.
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
13


## PDF page 40

14
ENTROPY, RELATIVE ENTROPY, AND MUTUAL INFORMATION
We denote the probability mass function by p(x) rather than pX(x), for
convenience. Thus, p(x) and p(y) refer to two different random variables
and are in fact different probability mass functions, pX(x) and pY(y),
respectively.
Deﬁnition
The entropy H(X) of a discrete random variable X is
deﬁned by
H(X) = −

x∈X
p(x) log p(x).
(2.1)
We also write H(p) for the above quantity. The log is to the base 2
and entropy is expressed in bits. For example, the entropy of a fair coin
toss is 1 bit. We will use the convention that 0 log 0 = 0, which is easily
justiﬁed by continuity since x log x →0 as x →0. Adding terms of zero
probability does not change the entropy.
If the base of the logarithm is b, we denote the entropy as Hb(X). If
the base of the logarithm is e, the entropy is measured in nats. Unless
otherwise speciﬁed, we will take all logarithms to base 2, and hence all
the entropies will be measured in bits. Note that entropy is a functional
of the distribution of X. It does not depend on the actual values taken by
the random variable X, but only on the probabilities.
We denote expectation by E. Thus, if X ∼p(x), the expected value of
the random variable g(X) is written
Epg(X) =

x∈X
g(x)p(x),
(2.2)
or more simply as Eg(X) when the probability mass function is under-
stood from the context. We shall take a peculiar interest in the eerily
self-referential expectation of g(X) under p(x) when g(X) = log
1
p(X).
Remark
The entropy of X can also be interpreted as the expected value
of the random variable log
1
p(X), where X is drawn according to probability
mass function p(x). Thus,
H(X) = Ep log
1
p(X).
(2.3)
This deﬁnition of entropy is related to the deﬁnition of entropy in ther-
modynamics; some of the connections are explored later. It is possible
to derive the deﬁnition of entropy axiomatically by deﬁning certain prop-
erties that the entropy of a random variable must satisfy. This approach
is illustrated in Problem 2.46. We do not use the axiomatic approach to


