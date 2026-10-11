# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 505

14.5
ALGORITHMICALLY RANDOM AND INCOMPRESSIBLE SEQUENCES
479
where δn is chosen so that
H0
1
2 −δn

= 1 −2 log n + cn + c′
n
,
(14.57)
which implies that δn →0 as n →∞. Thus, 1
n
 xi →1
2 as n →∞. □
We have now proved that incompressible sequences look random in the
sense that the proportion of 0’s and 1’s are almost equal. In general, we
can show that if a sequence is incompressible, it will satisfy all computable
statistical tests for randomness. (Otherwise, identiﬁcation of the test that x
fails will reduce the descriptive complexity of x, yielding a contradiction.)
In this sense, the algorithmic test for randomness is the ultimate test,
including within it all other computable tests for randomness.
We now prove a related law of large numbers for the Kolmogorov
complexity of Bernoulli(θ) sequences. The Kolmogorov complexity of
a sequence of binary random variables drawn i.i.d. according to a
Bernoulli(θ) process is close to the entropy H0(θ). In Theorem 14.3.1
we proved that the expected value of the Kolmogorov complex-
ity of a random Bernoulli sequence converges to the entropy [i.e.,
E 1
nK(X1X2 . . . Xn|n) →H0(θ)]. Now we remove the expectation.
Theorem 14.5.3
Let X1, X2, . . . , Xn be drawn i.i.d. ∼Bernoulli(θ).
Then
1
nK(X1X2 . . . Xn|n) →H0(θ)
in probability.
(14.58)
Proof:
Let Xn = 1
n
 Xi be the proportion of 1’s in X1, X2, . . . , Xn.
Then using the method described in (14.23), we have
K(X1X2 . . . Xn|n) ≤nH0
	
Xn

+ 2 log n + c,
(14.59)
and since by the weak law of large numbers, Xn →θ in probability, we
have
Pr
1
nK(X1X2 . . . Xn|n) −H0(θ) ≥ϵ

→0.
(14.60)
Conversely, we can bound the number of sequences with complexity sig-
niﬁcantly lower than the entropy. From the AEP, we can divide the set
of sequences into the typical set and the nontypical set. There are at


## PDF page 506

480
KOLMOGOROV COMPLEXITY
least (1 −ϵ)2n(H0(θ)−ϵ) sequences in the typical set. At most 2n(H0(θ)−c)
of these typical sequences can have a complexity less than n(H0(θ) −c).
The probability that the complexity of the random sequence is less than
n(H0(θ) −c) is
Pr(K(Xn|n) < n(H0(θ) −c))
≤Pr(Xn /∈A(n)
ϵ ) + Pr(Xn ∈A(n)
ϵ , K(Xn|n) < n(H0(θ) −c))
≤ϵ +

xn∈A(n)
ϵ ,K(xn|n)<n(H0(θ)−c)
p(xn)
(14.61)
≤ϵ +

xn∈A(n)
ϵ ,K(xn|n)<n(H0(θ)−c)
2−n(H0(θ)−ϵ)
(14.62)
≤ϵ + 2n(H0(θ)−c)2−n(H0(θ)−ϵ)
(14.63)
= ϵ + 2−n(c−ϵ),
(14.64)
which is arbitrarily small for appropriate choice of ϵ, n, and c. Hence with
high probability, the Kolmogorov complexity of the random sequence is
close to the entropy, and we have
K(X1, X2, . . . , Xn|n)
n
→H0(θ)
in probability.
(14.65)
□
14.6
UNIVERSAL PROBABILITY
Suppose that a computer is fed a random program. Imagine a monkey
sitting at a keyboard and typing the keys at random. Equivalently, feed a
series of fair coin ﬂips into a universal Turing machine. In either case, most
strings will not make sense to the computer. If a person sits at a terminal
and types keys at random, he will probably get an error message (i.e., the
computer will print the null string and halts). But with a certain probability
she will hit on something that makes sense. The computer will then print
out something meaningful. Will this output sequence look random?
From our earlier discussions, it is clear that most sequences of length n
have complexity close to n. Since the probability of an input program p
is 2−l(p), shorter programs are much more probable than longer ones; and
when they produce long strings, shorter programs do not produce random
strings; they produce strings with simply described structure.
The probability distribution on the output strings is far from uniform.
Under the computer-induced distribution, simple strings are more likely


## PDF page 507

14.6
UNIVERSAL PROBABILITY
481
than complicated strings of the same length. This motivates us to deﬁne
a universal probability distribution on strings as follows:
Deﬁnition
The universal probability of a string x is
PU(x) =

p: U(p)=x
2−l(p) = Pr(U(p) = x),
(14.66)
which is the probability that a program randomly drawn as a sequence of
fair coin ﬂips p1, p2, . . . will print out the string x.
This probability is universal in many senses. We can consider it as the
probability of observing such a string in nature; the implicit belief is that
simpler strings are more likely than complicated strings. For example, if
we wish to describe the laws of physics, we might consider the simplest
string describing the laws as the most likely. This principle, known as
Occam’s Razor, has been a general principle guiding scientiﬁc research
for centuries: If there are many explanations consistent with the observed
data, choose the simplest. In our framework, Occam’s Razor is equivalent
to choosing the shortest program that produces a given string.
This probability mass function is called universal because of the fol-
lowing theorem.
Theorem 14.6.1
For every computer A,
PU(x) ≥c′
APA(x)
(14.67)
for every string x ∈{0, 1}∗, where the constant c′
A depends only on U and
A.
Proof:
From the discussion of Section 14.2, we recall that for every
program p′ for A that prints x, there exists a program p for U of length
not more than l(p′) + cA produced by preﬁxing a simulation program for
A. Hence,
PU(x) =

p: U(p)=x
2−l(p) ≥

p′:A(p′)=x
2−l(p′)−cA = c′
APA(x).
(14.68)
□
Any sequence drawn according to a computable probability mass func-
tion on binary strings can be considered to be produced by some computer
A acting on a random input (via the probability inverse transformation
acting on a random input). Hence, the universal probability distribution
includes a mixture of all computable probability distributions.


## PDF page 508

482
KOLMOGOROV COMPLEXITY
Remark
(Bounded likelihood ratio). In particular, Theorem 14.6.1 guar-
antees that a likelihood ratio test of the hypothesis that X is drawn
according to PU versus the hypothesis that it is drawn according to
PA will have bounded likelihood ratio. If U and A are universal, the
PU(x)/PA(x) is bounded away from 0 and inﬁnity for all x. This is in
contrast to other simple hypothesis-testing problems (like Bernoulli(θ1)
versus Bernoulli(θ2)), where the likelihood ratio goes to 0 or ∞as the
sample size goes to inﬁnity. Apparently, PU, which is a mixture of all
computable distributions, can never be rejected completely as the true
distribution of any data drawn according to some computable probability
distribution. In that sense we cannot reject the possibility that the universe
is the output of monkeys typing at a computer. However, we can reject
the hypothesis that the universe is random (monkeys with no computer).
In Section 14.11 we prove that
PU(x) ≈2−K(x),
(14.69)
thus showing that K(x) and log
1
PU (x) have equal status as universal algo-
rithmic complexity measures. This is especially interesting since log
1
PU (x)
is the ideal codeword length (the Shannon codeword length) with respect
to the universal probability distribution PU(x).
We conclude this section with an example of a monkey at a typewriter
vs. a monkey at a computer keyboard. If the monkey types at random
on a typewriter, the probability that it types out all the works of Shake-
speare (assuming that the text is 1 million bits long) is 2−1,000,000. If the
monkey sits at a computer terminal, however, the probability that it types
out Shakespeare is now 2−K(Shakespeare) ≈2−250,000, which although
extremely small is still exponentially more likely than when the monkey
sits at a dumb typewriter.
The example indicates that a random input to a computer is much more
likely to produce “interesting” outputs than a random input to a typewriter.
We all know that a computer is an intelligence ampliﬁer. Apparently, it
creates sense from nonsense as well.
14.7
THE HALTING PROBLEM AND THE NONCOMPUTABILITY
OF KOLMOGOROV COMPLEXITY
Consider the following paradoxical statement:
This statement is false.
This paradox is sometimes stated in a two-statement form:


## PDF page 509

14.7
KOLMOGOROV COMPLEXITY
483
The next statement is false.
The preceding statement is true.
These paradoxes are versions of what is called the Epimenides liar para-
dox, and it illustrates the pitfalls involved in self-reference. In 1931, G¨odel
used this idea of self-reference to show that any interesting system of
mathematics is not complete; there are statements in the system that are
true but that cannot be proved within the system. To accomplish this, he
translated theorems and proofs into integers and constructed a statement
of the above form, which can therefore not be proved true or false.
The halting problem in computer science is very closely connected
with G¨odel’s incompleteness theorem. In essence, it states that for any
computational model, there is no general algorithm to decide whether a
program will halt or not (go on forever). Note that it is not a statement
about any speciﬁc program. Quite clearly, there are many programs that
can easily be shown to halt or go on forever. The halting problem says
that we cannot answer this question for all programs. The reason for this
is again the idea of self-reference.
To a practical person, the halting problem may not be of any immediate
signiﬁcance, but it has great theoretical importance as the dividing line
between things that can be done on a computer (given unbounded memory
and time) and things that cannot be done at all (such as proving all true
statements in number theory). G¨odel’s incompleteness theorem is one of
the most important mathematical results of the twentieth century, and its
consequences are still being explored. The halting problem is an essential
example of G¨odel’s incompleteness theorem.
One of the consequences of the nonexistence of an algorithm for the
halting problem is the noncomputability of Kolmogorov complexity. The
only way to ﬁnd the shortest program in general is to try all short programs
and see which of them can do the job. However, at any time some of
the short programs may not have halted and there is no effective (ﬁnite
mechanical) way to tell whether or not they will halt and what they will
print out. Hence, there is no effective way to ﬁnd the shortest program to
print a given string.
The noncomputability of Kolmogorov complexity is an example of the
Berry paradox. The Berry paradox asks for the shortest number not name-
able in under 10 words. A number like 1,101,121 cannot be a solution
since the deﬁning expression itself is less than 10 words long. This illus-
trates the problems with the terms nameable and describable; they are
too powerful to be used without a strict meaning. If we restrict ourselves
to the meaning “can be described for printing out on a computer,” we can
resolve Berry’s paradox by saying that the smallest number not describable


## PDF page 510

484
KOLMOGOROV COMPLEXITY
in less than 10 words exists but is not computable. This “description” is
not a program for computing the number. E. F. Beckenbach pointed out
a similar problem in the classiﬁcation of numbers as dull or interesting;
the smallest dull number must be interesting.
As stated at the beginning of the chapter, one does not really anticipate
that practitioners will ﬁnd the shortest computer program for a given
string. The shortest program is not computable, although as more and more
programs are shown to produce the string, the estimates from above of
the Kolmogorov complexity converge to the true Kolmogorov complexity.
(The problem, of course, is that one may have found the shortest program
and never know that no shorter program exists.) Even though Kolmogorov
complexity is not computable, it provides a framework within which to
consider questions of randomness and inference.
14.8

In this section we introduce Chaitin’s mystical, magical number, , which
has some extremely interesting properties.
Deﬁnition
 =

p: U(p) halts
2−l(p).
(14.70)
Note that  = Pr(U(p) halts), the probability that the given universal
computer halts when the input to the computer is a binary string drawn
according to a Bernoulli(1
2) process.
Since the programs that halt are preﬁx-free, their lengths satisfy the
Kraft inequality, and hence the sum above is always between 0 and 1. Let
n = .ω1ω2 · · · ωn denote the ﬁrst n bits of . The properties of  are
as follows:
1.  is noncomputable. There is no effective (ﬁnite, mechanical) way
to check whether arbitrary programs halt (the halting problem), so
there is no effective way to compute .
2.  is a “philosopher’s stone”.
Knowing  to an accuracy of n
bits will enable us to decide the truth of any provable or ﬁnitely
refutable mathematical theorem that can be written in less than n
bits. Actually, all that this means is that given n bits of , there
is an effective procedure to decide the truth of n-bit theorems; the
procedure may take an arbitrarily long (but ﬁnite) time. Of course,
without knowing , it is not possible to check the truth or falsity of


## PDF page 511

14.8

485
every theorem by an effective procedure (G¨odel’s incompleteness
theorem).
The basic idea of the procedure using n bits of  is simple: We
run all programs until the sum of the masses 2−l(p) contributed
by programs that halt equals or exceeds n = 0.ω1ω2 · · · ωn, the
truncated version of  that we are given. Then, since
 −n < 2−n,
(14.71)
we know that the sum of all further contributions of the form 2−l(p)
to  from programs that halt must also be less than 2−n. This implies
that no program of length ≤n that has not yet halted will ever halt,
which enables us to decide the halting or nonhalting of all programs
of length ≤n.
To complete the proof, we must show that it is possible for a com-
puter to run all possible programs in “parallel” in such a way that
any program that halts will eventually be found to halt. First, list all
possible programs, starting with the null program, :
, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, . . . .
(14.72)
Then let the computer execute one clock cycle of  for the ﬁrst
cycle. In the next cycle, let the computer execute two clock cycles
of  and two clock cycles of the program 0. In the third cycle, let
it execute three clock cycles of each of the ﬁrst three programs, and
so on. In this way, the computer will eventually run all possible
programs and run them for longer and longer times, so that if any
program halts, it will eventually be discovered to halt. The com-
puter keeps track of which program is being executed and the cycle
number so that it can produce a list of all the programs that halt.
Thus, we will ultimately know whether or not any program of less
than n bits will halt. This enables the computer to ﬁnd any proof
of the theorem or a counterexample to the theorem if the theorem
can be stated in less than n bits. Knowledge of  turns previously
unprovable theorems into provable theorems. Here  acts as an
oracle.
Although  seems magical in this respect, there are other numbers
that carry the same information. For example, if we take the list of
programs and construct a real number in which the ith bit indicates
whether program i halts, this number can also be used to decide
any ﬁnitely refutable question in mathematics. This number is very
dilute (in information content) because one needs approximately 2n


## PDF page 512

486
KOLMOGOROV COMPLEXITY
bits of this indicator function to decide whether or not an n-bit
program halts. Given 2n bits, one can tell immediately without any
computation whether or not any program of length less than n halts.
However,  is the most compact representation of this information
since it is algorithmically random and incompressible.
What are some of the questions that we can resolve using ?
Many of the interesting problems in number theory can be stated
as a search for a counterexample. For example, it is straightforward
to write a program that searches over the integers x, y, z, and n
and halts only if it ﬁnds a counterexample to Fermat’s last theorem,
which states that
xn + yn = zn
(14.73)
has no solution in integers for n ≥3. Another example is Goldbach’s
conjecture, which states that any even number is a sum of two
primes. Our program would search through all the even numbers
starting with 2, check all prime numbers less than it and ﬁnd a
decomposition as a sum of two primes. It will halt if it comes across
an even number that does not have such a decomposition. Knowing
whether this program halts is equivalent to knowing the truth of
Goldbach’s conjecture.
We can also design a program that searches through all proofs
and halts only when it ﬁnds a proof of the theorem required. This
program will eventually halt if the theorem has a ﬁnite proof. Hence
knowing n bits of , we can ﬁnd the truth or falsity of all theorems
that have a ﬁnite proof or are ﬁnitely refutable and which can be
stated in less than n bits.
3.  is algorithmically random.
Theorem 14.8.1
 cannot be compressed by more than a constant;
that is, there exists a constant c such that
K(ω1ω2 . . . ωn) ≥n −c
for all n.
(14.74)
Proof:
We know that if we are given n bits of , we can determine
whether or not any program of length ≤n halts. Using K(ω1ω2 · · ·
ωn) bits, we can calculate n bits of , and then we can generate a list
of all programs of length ≤n that halt, together with their corresponding
outputs. We ﬁnd the ﬁrst string x0 that is not on this list. The string x0
is then the shortest string with Kolmogorov complexity K(x0) > n. The


