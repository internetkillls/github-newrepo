# A Mathematical Theory of Communication

Source ID: C05
Authors: Claude E. Shannon
Source URL: https://www.princeton.edu/~wbialek/rome/refs/shannon_48.pdf
DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x
Identity: Corrected reprint of the two-part Bell System Technical Journal article, 1948. Reprint pagination differs from journal pagination.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 9

is the same in statistical properties. Thus the letter frequencies, digram frequencies, etc., obtained from
particular sequences, will, as the lengths of the sequences increase, approach deﬁnite limits independent
of the particular sequence. Actually this is not true of every sequence but the set for which it is false has
probability zero. Roughly the ergodic property means statistical homogeneity.
All the examples of artiﬁcial languages given above are ergodic. This property is related to the structure
of the corresponding graph. If the graph has the following two properties7 the corresponding process will
be ergodic:
1. The graph does not consist of two isolated parts A and B such that it is impossible to go from junction
points in part A to junction points in part B along lines of the graph in the direction of arrows and also
impossible to go from junctions in part B to junctions in part A.
2. A closed series of lines in the graph with all arrows on the lines pointing in the same orientation will
be called a “circuit.” The “length” of a circuit is the number of lines in it. Thus in Fig. 5 series BEBES
is a circuit of length 5. The second property required is that the greatest common divisor of the lengths
of all circuits in the graph be one.
S
S
S
A
A
A
A
A
B
B
B
B
B
B
B
C
D
D
D
D
D
D
E
E
E
E
E
E
E
E
E
E
E
Fig. 5—A graph corresponding to the source in example D.
If the ﬁrst condition is satisﬁed but the second one violated by having the greatest common divisor equal
to d
> 1, the sequences have a certain type of periodic structure. The various sequences fall into d different
classes which are statistically the same apart from a shift of the origin (i.e., which letter in the sequence is
called letter 1). By a shift of from 0 up to d
 1 any sequence can be made statistically equivalent to any
other. A simple example with d
= 2 is the following: There are three possible letters a ;b ;c. Letter a is
followed with either b or c with probabilities 1
3 and 2
3 respectively. Either b or c is always followed by letter
a. Thus a typical sequence is
a b a c a c a c a b a c a b a b a c a c:
This type of situation is not of much importance for our work.
If the ﬁrst condition is violated the graph may be separated into a set of subgraphs each of which satisﬁes
the ﬁrst condition. We will assume that the second condition is also satisﬁed for each subgraph. We have in
this case what may be called a “mixed” source made up of a number of pure components. The components
correspond to the various subgraphs. If L1, L2, L3
;
:
:
: are the component sources we may write
L
= p1L1
+ p2L2
+ p3L3
+



7These are restatements in terms of the graph of conditions given in Fr´echet.
9


## PDF page 10

where pi is the probability of the component source Li.
Physically the situation represented is this: There are several different sources L1, L2, L3
;
:
:
: which are
each of homogeneous statistical structure (i.e., they are ergodic). We do not know a priori which is to be
used, but once the sequence starts in a given pure component Li, it continues indeﬁnitely according to the
statistical structure of that component.
As an example one may take two of the processes deﬁned above and assume p1
=
:2 and p2
=
:8. A
sequence from the mixed source
L
=
:2L1
+
:8L2
would be obtained by choosing ﬁrst L1 or L2 with probabilities .2 and .8 and after this choice generating a
sequence from whichever was chosen.
Except when the contrary is stated we shall assume a source to be ergodic. This assumption enables one
to identify averages along a sequence with averages over the ensemble of possible sequences (the probability
of a discrepancy being zero). For example the relative frequency of the letter A in a particular inﬁnite
sequence will be, with probability one, equal to its relative frequency in the ensemble of sequences.
If Pi is the probability of state i and pi
(j
) the transition probability to state j, then for the process to be
stationary it is clear that the Pi must satisfy equilibrium conditions:
Pj
= ∑
i
Pipi
(j
):
In the ergodic case it can be shown that with any starting conditions the probabilities Pj
(N
) of being in state
j after N symbols, approach the equilibrium values as N
! ∞.
6. CHOICE, UNCERTAINTY AND ENTROPY
We have represented a discrete information source as a Markoff process. Can we deﬁne a quantity which
will measure, in some sense, how much information is “produced” by such a process, or better, at what rate
information is produced?
Suppose we have a set of possible events whose probabilities of occurrence are p1
; p2
;
:
:
:
; pn. These
probabilities are known but that is all we know concerning which event will occur. Can we ﬁnd a measure
of how much “choice” is involved in the selection of the event or of how uncertain we are of the outcome?
If there is such a measure, say H
(p1
; p2
;
:
:
:
; pn
), it is reasonable to require of it the following properties:
1. H should be continuous in the pi.
2. If all the pi are equal, pi
= 1
n, then H should be a monotonic increasing function of n. With equally
likely events there is more choice, or uncertainty, when there are more possible events.
3. If a choice be broken down into two successive choices, the original H should be the weighted sum
of the individual values of H. The meaning of this is illustrated in Fig. 6. At the left we have three
/
/
/
/
/
/
/
/
/
/
Fig. 6—Decomposition of a choice from three possibilities.
possibilities p1
= 1
2, p2
= 1
3, p3
= 1
6. On the right we ﬁrst choose between two possibilities each with
probability 1
2, and if the second occurs make another choice with probabilities 2
3, 1
3. The ﬁnal results
have the same probabilities as before. We require, in this special case, that
H
( 1
2
; 1
3
; 1
6
)
= H
( 1
2
; 1
2
)
+ 1
2H
( 2
3
; 1
3
):
The coefﬁcient 1
2 is because this second choice only occurs half the time.
10


## PDF page 11

In Appendix 2, the following result is established:
Theorem 2: The only H satisfying the three above assumptions is of the form:
H
=
K
n
∑
i=1
pi log pi
where K is a positive constant.
This theorem, and the assumptions required for its proof, are in no way necessary for the present theory.
It is given chieﬂy to lend a certain plausibility to some of our later deﬁnitions. The real justiﬁcation of these
deﬁnitions, however, will reside in their implications.
Quantities of the form H
=
∑pi log pi (the constant K merely amounts to a choice of a unit of measure)
play a central role in information theory as measures of information, choice and uncertainty. The form of H
will be recognized as that of entropy as deﬁned in certain formulations of statistical mechanics8 where pi is
the probability of a system being in cell i of its phase space. H is then, for example, the H in Boltzmann’s
famous H theorem. We shall call H
=
∑pi log pi the entropy of the set of probabilities p1
;
:
:
:
; pn. If x is a
chance variable we will write H
(x) for its entropy; thus x is not an argument of a function but a label for a
number, to differentiate it from H
(y) say, the entropy of the chance variable y.
The entropy in the case of two possibilities with probabilities p and q
= 1
 p, namely
H
=
(plog p
+qlogq )
is plotted in Fig. 7 as a function of p.
H
BITS
p
0
.
.
.
.
.
.
.
.
.	
.0
0
.
.
.
.
.
.
.
.
.	
.0
Fig. 7—Entropy in the case of two possibilities with probabilities p and
(1
 p).
The quantity H has a number of interesting properties which further substantiate it as a reasonable
measure of choice or information.
1. H
= 0 if and only if all the pi but one are zero, this one having the value unity. Thus only when we
are certain of the outcome does H vanish. Otherwise H is positive.
2. For a given n, H is a maximum and equal to logn when all the pi are equal (i.e., 1
n). This is also
intuitively the most uncertain situation.
8See, for example, R. C. Tolman, Principles of Statistical Mechanics, Oxford, Clarendon, 1938.
11


## PDF page 12

3. Suppose there are two events, x and y, in question with m possibilities for the ﬁrst and n for the second.
Let p (i; j
) be the probability of the joint occurrence of i for the ﬁrst and j for the second. The entropy of the
joint event is
H
(x;y)
=
∑
i;j
p (i; j
)log p (i; j
)
while
H
(x)
=
∑
i;j
p (i; j
)log∑
j
p (i; j
)
H
(y)
=
∑
i;j
p (i; j
)log∑
i
p (i; j
):
It is easily shown that
H
(x;y)
 H
(x)
+H
(y)
with equality only if the events are independent (i.e., p (i; j
)
= p (i)p (j
)). The uncertainty of a joint event is
less than or equal to the sum of the individual uncertainties.
4. Any change toward equalization of the probabilities p1
; p2
;
:
:
:
; pn increases H. Thus if p1
< p2 and
we increase p1, decreasing p2 an equal amount so that p1 and p2 are more nearly equal, then H increases.
More generally, if we perform any “averaging” operation on the pi of the form
p
0
i
= ∑
j
aijp j
where ∑i aij
= ∑j aij
= 1, and all aij
 0, then H increases (except in the special case where this transfor-
mation amounts to no more than a permutation of the p j with H of course remaining the same).
5. Suppose there are two chance events x and y as in 3, not necessarily independent. For any particular
value i that x can assume there is a conditional probability pi
(j
) that y has the value j. This is given by
pi
(j
)
=
p (i; j
)
∑j p (i; j
)
:
We deﬁne the conditional entropy of y, Hx
(y) as the average of the entropy of y for each value of x, weighted
according to the probability of getting that particular x. That is
Hx
(y)
=
∑
i;j
p (i; j
)log pi
(j
)
:
This quantity measures how uncertain we are of y on the average when we know x. Substituting the value of
pi
(j
) we obtain
Hx
(y)
=
∑
i;j
p (i; j
)log p (i; j
)
+∑
i;j
p (i; j
)log∑
j
p (i; j
)
= H
(x;y)
H
(x)
or
H
(x;y)
= H
(x)
+Hx
(y):
The uncertainty (or entropy) of the joint event x;y is the uncertainty of x plus the uncertainty of y when x is
known.
6. From 3 and 5 we have
H
(x)
+H
(y)
 H
(x;y)
= H
(x)
+Hx
(y):
Hence
H
(y)
 Hx
(y):
The uncertainty of y is never increased by knowledge of x. It will be decreased unless x and y are independent
events, in which case it is not changed.
12


## PDF page 13

7. THE ENTROPY OF AN INFORMATION SOURCE
Consider a discrete source of the ﬁnite state type considered above. For each possible state i there will be a
set of probabilities pi
(j
) of producing the various possible symbols j. Thus there is an entropy Hi for each
state. The entropy of the source will be deﬁned as the average of these Hi weighted in accordance with the
probability of occurrence of the states in question:
H
= ∑
i
PiHi
=
∑
i;j
Pipi
(j
)log pi
(j
)
:
This is the entropy of the source per symbol of text. If the Markoff process is proceeding at a deﬁnite time
rate there is also an entropy per second
H
0
= ∑
i
fiHi
where fi is the average frequency (occurrences per second) of state i. Clearly
H
0
= mH
where m is the average number of symbols produced per second. H or H
0 measures the amount of informa-
tion generated by the source per symbol or per second. If the logarithmic base is 2, they will represent bits
per symbol or per second.
If successive symbols are independent then H is simply
∑pi log pi where pi is the probability of sym-
bol i. Suppose in this case we consider a long message of N symbols. It will contain with high probability
about p1N occurrences of the ﬁrst symbol, p2N occurrences of the second, etc. Hence the probability of this
particular message will be roughly
p
= pp1N
1
pp2N
2


 ppnN
n
or
log p
:
= N∑
i
pi log pi
log p
:
=
NH
H
:
= log1 =p
N
:
H is thus approximately the logarithm of the reciprocal probability of a typical long sequence divided by the
number of symbols in the sequence. The same result holds for any source. Stated more precisely we have
(see Appendix 3):
Theorem 3: Given any

> 0 and

> 0, we can ﬁnd an N0 such that the sequences of any length N
 N0
fall into two classes:
1. A set whose total probability is less than
.
2. The remainder, all of whose members have probabilities satisfying the inequality




log p
1
N
H




<

:
In other words we are almost certain to have log p
1
N
very close to H when N is large.
A closely related result deals with the number of sequences of various probabilities. Consider again the
sequences of length N and let them be arranged in order of decreasing probability. We deﬁne n (q ) to be
the number we must take from this set starting with the most probable one in order to accumulate a total
probability q for those taken.
13


## PDF page 14

Theorem 4:
Lim
N
!∞
logn (q )
N
= H
when q does not equal 0 or 1.
We may interpret logn (q ) as the number of bits required to specify the sequence when we consider only
the most probable sequences with a total probability q. Then logn (q )
N
is the number of bits per symbol for
the speciﬁcation. The theorem says that for large N this will be independent of q and equal to H. The rate
of growth of the logarithm of the number of reasonably probable sequences is given by H, regardless of our
interpretation of “reasonably probable.” Due to these results, which are proved in Appendix 3, it is possible
for most purposes to treat the long sequences as though there were just 2HN of them, each with a probability
2
HN.
The next two theorems show that H and H
0 can be determined by limiting operations directly from
the statistics of the message sequences, without reference to the states and transition probabilities between
states.
Theorem 5: Let p (Bi
) be the probability of a sequence Bi of symbols from the source. Let
GN
=
 1
N ∑
i
p (Bi
)log p (Bi
)
where the sum is over all sequences Bi containing N symbols. Then GN is a monotonic decreasing function
of N and
Lim
N
!∞GN
= H
:
Theorem 6: Let p (Bi
;S j
) be the probability of sequence Bi followed by symbol S j and pBi
(S j
)
=
p (Bi
;S j
)=p (Bi
) be the conditional probability of S j after Bi. Let
FN
=
∑
i;j
p (Bi
;S j
)log pBi
(S j
)
where the sum is over all blocks Bi of N
 1 symbols and over all symbols S j. Then FN is a monotonic
decreasing function of N,
FN
= NGN
(N
1 )GN
1
;
GN
= 1
N
N
∑
n =1
Fn
;
FN
 GN
;
and LimN
!∞FN
= H.
These results are derived in Appendix 3. They show that a series of approximations to H can be obtained
by considering only the statistical structure of the sequences extending over 1
;2 ;
:
:
:
;N symbols. FN is the
better approximation. In fact FN is the entropy of the Nth order approximation to the source of the type
discussed above. If there are no statistical inﬂuences extending over more than N symbols, that is if the
conditional probability of the next symbol knowing the preceding
(N
1 ) is not changed by a knowledge of
any before that, then FN
= H. FN of course is the conditional entropy of the next symbol when the
(N
1 )
preceding ones are known, while GN is the entropy per symbol of blocks of N symbols.
The ratio of the entropy of a source to the maximum value it could have while still restricted to the same
symbols will be called its relative entropy. This is the maximum compression possible when we encode into
the same alphabet. One minus the relative entropy is the redundancy. The redundancy of ordinary English,
not considering statistical structure over greater distances than about eight letters, is roughly 50%. This
means that when we write English half of what we write is determined by the structure of the language and
half is chosen freely. The ﬁgure 50% was found by several independent methods which all gave results in
14


## PDF page 15

this neighborhood. One is by calculation of the entropy of the approximations to English. A second method
is to delete a certain fraction of the letters from a sample of English text and then let someone attempt to
restore them. If they can be restored when 50% are deleted the redundancy must be greater than 50%. A
third method depends on certain known results in cryptography.
Two extremes of redundancy in English prose are represented by Basic English and by James Joyce’s
book “Finnegans Wake”. The Basic English vocabulary is limited to 850 words and the redundancy is very
high. This is reﬂected in the expansion that occurs when a passage is translated into Basic English. Joyce
on the other hand enlarges the vocabulary and is alleged to achieve a compression of semantic content.
The redundancy of a language is related to the existence of crossword puzzles. If the redundancy is
zero any sequence of letters is a reasonable text in the language and any two-dimensional array of letters
forms a crossword puzzle. If the redundancy is too high the language imposes too many constraints for large
crossword puzzles to be possible. A more detailed analysis shows that if we assume the constraints imposed
by the language are of a rather chaotic and random nature, large crossword puzzles are just possible when
the redundancy is 50%. If the redundancy is 33%, three-dimensional crossword puzzles should be possible,
etc.
8. REPRESENTATION OF THE ENCODING AND DECODING OPERATIONS
We have yet to represent mathematically the operations performed by the transmitter and receiver in en-
coding and decoding the information. Either of these will be called a discrete transducer. The input to the
transducer is a sequence of input symbols and its output a sequence of output symbols. The transducer may
have an internal memory so that its output depends not only on the present input symbol but also on the past
history. We assume that the internal memory is ﬁnite, i.e., there exist a ﬁnite number m of possible states of
the transducer and that its output is a function of the present state and the present input symbol. The next
state will be a second function of these two quantities. Thus a transducer can be described by two functions:
yn
= f
(xn
;
n
)
n +1
= g (xn
;
n
)
where
xn is the nth input symbol,
n is the state of the transducer when the nth input symbol is introduced,
yn is the output symbol (or sequence of output symbols) produced when xn is introduced if the state is
n.
If the output symbols of one transducer can be identiﬁed with the input symbols of a second, they can be
connected in tandem and the result is also a transducer. If there exists a second transducer which operates
on the output of the ﬁrst and recovers the original input, the ﬁrst transducer will be called non-singular and
the second will be called its inverse.
Theorem 7: The output of a ﬁnite state transducer driven by a ﬁnite state statistical source is a ﬁnite
state statistical source, with entropy (per unit time) less than or equal to that of the input. If the transducer
is non-singular they are equal.
Let
 represent the state of the source, which produces a sequence of symbols xi; and let
 be the state of
the transducer, which produces, in its output, blocks of symbols yj. The combined system can be represented
by the “product state space” of pairs
(;

). Two points in the space
(1
;
1
) and
(2
;
2
), are connected by
a line if
1 can produce an x which changes
1 to
2, and this line is given the probability of that x in this
case. The line is labeled with the block of yj symbols produced by the transducer. The entropy of the output
can be calculated as the weighted sum over the states. If we sum ﬁrst on
 each resulting term is less than or
equal to the corresponding term for
, hence the entropy is not increased. If the transducer is non-singular
let its output be connected to the inverse transducer. If H
0
1, H
0
2 and H
0
3 are the output entropies of the source,
the ﬁrst and second transducers respectively, then H
0
1
 H
0
2
 H
0
3
= H
0
1 and therefore H
0
1
= H
0
2.
15


## PDF page 16

Suppose we have a system of constraints on possible sequences of the type which can be represented by
a linear graph as in Fig. 2. If probabilities p
(s)
ij were assigned to the various lines connecting state i to state j
this would become a source. There is one particular assignment which maximizes the resulting entropy (see
Appendix 4).
Theorem 8: Let the system of constraints considered as a channel have a capacity C
= logW. If we
assign
p
(s)
ij
= Bj
Bi
W
`
(s)
ij
where
`
(s)
ij is the duration of the sth symbol leading from state i to state j and the Bi satisfy
Bi
= ∑
s;j
BjW
`
(s)
ij
then H is maximized and equal to C.
By proper assignment of the transition probabilities the entropy of symbols on a channel can be maxi-
mized at the channel capacity.
9. THE FUNDAMENTAL THEOREM FOR A NOISELESS CHANNEL
We will now justify our interpretation of H as the rate of generating information by proving that H deter-
mines the channel capacity required with most efﬁcient coding.
Theorem 9: Let a source have entropy H
(bits per symbol) and a channel have a capacity C
(bits per
second ). Then it is possible to encode the output of the source in such a way as to transmit at the average
rate C
H
 symbols per second over the channel where
 is arbitrarily small. It is not possible to transmit at
an average rate greater than C
H .
The converse part of the theorem, that C
H cannot be exceeded, may be proved by noting that the entropy
of the channel input per second is equal to that of the source, since the transmitter must be non-singular, and
also this entropy cannot exceed the channel capacity. Hence H
0
 C and the number of symbols per second
= H
0
=H
 C
=H.
The ﬁrst part of the theorem will be proved in two different ways. The ﬁrst method is to consider the
set of all sequences of N symbols produced by the source. For N large we can divide these into two groups,
one containing less than 2
(H
+
)N members and the second containing less than 2RN members (where R is
the logarithm of the number of different symbols) and having a total probability less than
. As N increases
 and
 approach zero. The number of signals of duration T in the channel is greater than 2
(C

)T with

small when T is large. if we choose
T
=
H
C
+


N
then there will be a sufﬁcient number of sequences of channel symbols for the high probability group when
N and T are sufﬁciently large (however small
) and also some additional ones. The high probability group
is coded in an arbitrary one-to-one way into this set. The remaining sequences are represented by larger
sequences, starting and ending with one of the sequences not used for the high probability group. This
special sequence acts as a start and stop signal for a different code. In between a sufﬁcient time is allowed
to give enough different sequences for all the low probability messages. This will require
T1
=
R
C
+
'

N
where
' is small. The mean rate of transmission in message symbols per second will then be greater than

(1

)T
N
+
 T1
N
#
1
=

(1

)
H
C
+


+

R
C
+
'


1
:
16


