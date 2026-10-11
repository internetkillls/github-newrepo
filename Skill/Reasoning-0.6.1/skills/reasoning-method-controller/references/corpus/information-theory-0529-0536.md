# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 529

PROBLEMS
503
Equivalence of K(x) and log

1
PU (x)

. There exists a constant c inde-
pendent of x such that
log
1
PU(x) −K(x)
 ≤c
(14.123)
for all strings x. Thus, the universal probability of a string x is essen-
tially determined by its Kolmogorov complexity.
Deﬁnition
The Kolmogorov structure function Kk(xn|n) of a binary
string xn ∈{0, 1}n is deﬁned as
Kk(xn|n) =
min
p : l(p) ≤k
U(p, n) = S
x ∈S
log |S|.
(14.124)
Deﬁnition
Let k∗be the least k such that
Kk∗(xn|n) + k∗= K(xn|n).
(14.125)
Let S∗∗be the corresponding set and let p∗∗be the program that prints
out the indicator function of S∗∗. Then p∗∗is the Kolmogorov minimal
sufﬁcient statistic for x.
PROBLEMS
14.1
Kolmogorov complexity of two sequences.
Let x, y ∈{0, 1}∗.
Argue that K(x, y) ≤K(x) + K(y) + c.
14.2
Complexity of the sum
(a) Argue that K(n) ≤log n + 2 log log n + c.
(b) Argue that K(n1 + n2) ≤K(n1) + K(n2) + c.
(c) Give an example in which n1 and n2 are complex but the sum
is relatively simple.
14.3
Images.
Consider an n × n array x of 0’s and 1’s . Thus, x has
n2 bits.


## PDF page 530

504
KOLMOGOROV COMPLEXITY
Find the Kolmogorov complexity K(x | n) (to ﬁrst order) if:
(a) x is a horizontal line.
(b) x is a square.
(c) x is the union of two lines, each line being vertical or hori-
zontal.
14.4
Do computers reduce entropy?
Feed a random program P into
an universal computer. What is the entropy of the corresponding
output? Speciﬁcally, let X = U(P ), where P is a Bernoulli(1
2)
sequence. Here the binary sequence X is either undeﬁned or is
in {0, 1}∗. Let H(X) be the Shannon entropy of X. Argue that
H(X) = ∞. Thus, although the computer turns nonsense into
sense, the output entropy is still inﬁnite.
14.5
Monkeys on a computer.
Suppose that a random program is
typed into a computer. Give a rough estimate of the probability
that the computer prints the following sequence:
(a) 0n followed by any arbitrary sequence.
(b) π1π2 . . . πn followed by any arbitrary sequence, where πi is
the ith bit in the expansion of π.
(c) 0n1 followed by any arbitrary sequence.
(d) ω1ω2 . . . ωn followed by any arbitrary sequence.
(e) A proof of the four-color theorem.
14.6
Kolmogorov complexity and ternary programs.
Suppose that the
input programs for a universal computer U are sequences in
{0, 1, 2}∗(ternary inputs). Also, suppose that U prints ternary out-
puts. Let K(x|l(x)) = minU(p,l(x))=x l(p). Show that:
(a) K(xn|n) ≤n + c.
(b) |xn ∈{0, 1}∗: K(xn|n) < k| < 3k.
14.7
Law of large numbers.
Using ternary inputs and outputs as in
Problem 14.14.6, outline an argument demonstrating that if a
sequence x is algorithmically random [i.e., if K(x|l(x)) ≈l(x)],
the proportion of 0’s, 1’s, and 2’s in x must each be near 1
3. It
may be helpful to use Stirling’s approximation n! ≈(n/e)n.


## PDF page 531

PROBLEMS
505
14.8
Image complexity.
Consider two binary subsets A and B (of an
n × n grid): for example,
Find general upper and lower bounds, in terms of K(A|n) and
K(B|n), for:
(a) K(Ac|n).
(b) K(A ∪B|n).
(c) K(A ∩B|n).
14.9
Random program.
Suppose that a random program (symbols
i.i.d. uniform over the symbol set) is fed into the nearest available
computer. To our surprise the ﬁrst n bits of the binary expansion
of 1/
√
2 are printed out. Roughly what would you say the proba-
bility is that the next output bit will agree with the corresponding
bit in the expansion of 1/
√
2 ?
14.10
Face–vase illusion
(a) What is an upper bound on the complexity of a pattern on an
m × m grid that has mirror-image symmetry about a vertical
axis through the center of the grid and consists of horizontal
line segments?
(b) What is the complexity K if the image differs in one cell
from the pattern described above?
14.11
Kolmogorov complexity.
Assume that n is very large and known.
Let all rectangles be parallel to the frame.


## PDF page 532

506
KOLMOGOROV COMPLEXITY
(a) What is the (maximal) Kolmogorov complexity of the union
of two rectangles on an n × n grid?
(b) What if the rectangles intersect at a corner?
(c) What if they have the same (unknown) shape?
(d) What if they have the same (unknown) area?
(e) What is the minimum Kolmogorov complexity of the union
of two rectangles? That is, what is the simplest union?
(f) What is the (maximal) Kolmogorov complexity over all images
(not necessarily rectangles) on an n × n grid?
14.12
Encrypted text.
Suppose that English text xn is encrypted into
yn by a substitution cypher: a 1-to-1 reassignment of each of the
27 letters of the alphabet (A–Z, including the space character)
to itself. Suppose that the Kolmogorov complexity of the text
xn is K(xn) = n
4. (This is about right for English text. We’re
now assuming a 27-symbol programming language, instead of a
binary symbol-set for the programming language. So, the length
of the shortest program, using a 27-ary programming language,
that prints out a particular string of English text of length n, is
approximately n/4.)
(a) What is the Kolmogorov complexity of the encryption map?


## PDF page 533

HISTORICAL NOTES
507
(b) Estimate the Kolmogorov complexity of the encrypted text
yn.
(c) How high must n be before you would expect to be able to
decode yn?
14.13
Kolmogorov complexity.
Consider the Kolmogorov complexity
K(n) over the integers n. If a speciﬁc integer n1 has a low Kol-
mogorov complexity K(n1), by how much can the Kolmogorov
complexity K(n1 + k) for the integer n1 + k vary from K(n1)?
14.14
Complexity of large numbers.
Let A(n) be the set of positive
integers x for which a terminating program p of length less than
or equal to n bits exists that outputs x. Let B(n) be the com-
plement of A(n) [i.e., B(n) is the set of integers x for which no
program of length less than or equal to n outputs x]. Let M(n)
be the maximum integer in A(n), and let S(n) be the minimum
integer in B(n). What is the Kolmogorov complexity K(M(n))
(approximately)? What is K(S(n)) (approximately)? Which is
larger (M(n) or S(n))? Give a reasonable lower bound on M(n)
and a reasonable upper bound on S(n).
HISTORICAL NOTES
The original ideas of Kolmogorov complexity were put forth indepen-
dently and almost simultaneously by Kolmogorov [321, 322], Solomonoff
[504], and Chaitin [89]. These ideas were developed further by students of
Kolmogorov such as Martin-L¨of [374], who deﬁned the notion of algorith-
mically random sequences and algorithmic tests for randomness, and by
Levin and Zvonkin [353], who explored the ideas of universal probability
and its relationship to complexity. A series of papers by Chaitin [90]–[92]
developed the relationship between algorithmic complexity and mathemat-
ical proofs. C. P. Schnorr studied the universal notion of randomness and
related it to gambling in [466]–[468].
The concept of the Kolmogorov structure function was deﬁned by Kol-
mogorov at a talk at the Tallin conference in 1973, but these results
were not published. V’yugin pursues this in [549], where he shows that
there are some very strange sequences xn that reveal their structure arbi-
trarily slowly in the sense that Kk(xn|n) = n −k, k < K(xn|n). Zurek
[606]–[608] addresses the fundamental questions of Maxwell’s demon
and the second law of thermodynamics by establishing the physical con-
sequences of Kolmogorov complexity.


## PDF page 534

508
KOLMOGOROV COMPLEXITY
Rissanen’s minimum description length (MDL) principle is very close
in spirit to the Kolmogorov sufﬁcient statistic. Rissanen [445, 446] ﬁnds a
low-complexity model that yields a high likelihood of the data. Barron and
Cover [32] argue that the density minimizing K(f ) + log
1
 f (Xi) yields
consistent density estimation.
A nontechnical introduction to the various measures of complexity can
be found in a thought-provoking book by Pagels [412]. Additional refer-
ences to work in the area can be found in a paper by Cover et al. [114] on
Kolmogorov’s contributions to information theory and algorithmic com-
plexity. A comprehensive introduction to the ﬁeld, including applications
of the theory to analysis of algorithms and automata, may be found in the
book by Li and Vitanyi [354]. Additional coverage may be found in the
books by Chaitin [86, 93].


## PDF page 535

CHAPTER 15
NETWORK INFORMATION
THEORY
A system with many senders and receivers contains many new elements
in the communication problem: interference, cooperation, and feedback.
These are the issues that are the domain of network information theory.
The general problem is easy to state. Given many senders and receivers
and a channel transition matrix that describes the effects of the interference
and the noise in the network, decide whether or not the sources can be
transmitted over the channel. This problem involves distributed source
coding (data compression) as well as distributed communication (ﬁnding
the capacity region of the network). This general problem has not yet been
solved, so we consider various special cases in this chapter.
Examples of large communication networks include computer networks,
satellite networks, and the phone system. Even within a single computer,
there are various components that talk to each other. A complete theory
of network information would have wide implications for the design of
communication and computer networks.
Suppose that m stations wish to communicate with a common satellite
over a common channel, as shown in Figure 15.1. This is known as a
multiple-access channel. How do the various senders cooperate with each
other to send information to the receiver? What rates of communication are
achievable simultaneously? What limitations does interference among the
senders put on the total rate of communication? This is the best understood
multiuser channel, and the above questions have satisfying answers.
In contrast, we can reverse the network and consider one TV station
sending information to m TV receivers, as in Figure 15.2. How does
the sender encode information meant for different receivers in a common
signal? What are the rates at which information can be sent to the different
receivers? For this channel, the answers are known only in special cases.
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
509


## PDF page 536

510
NETWORK INFORMATION THEORY
FIGURE 15.1. Multiple-access channel.
FIGURE 15.2. Broadcast channel.
There are other channels, such as the relay channel (where there is
one source and one destination, but one or more intermediate sender–
receiver pairs that act as relays to facilitate the communication between the
source and the destination), the interference channel (two senders and two
receivers with crosstalk), and the two-way channel (two sender–receiver
pairs sending information to each other). For all these channels, we have
only some of the answers to questions about achievable communication
rates and the appropriate coding strategies.
All these channels can be considered special cases of a general com-
munication network that consists of m nodes trying to communicate with
each other, as shown in Figure 15.3. At each instant of time, the ith node
sends a symbol xi that depends on the messages that it wants to send


