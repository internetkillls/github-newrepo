# A Mathematical Theory of Communication

Source ID: C05
Authors: Claude E. Shannon
Source URL: https://www.princeton.edu/~wbialek/rome/refs/shannon_48.pdf
DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x
Identity: Corrected reprint of the two-part Bell System Technical Journal article, 1948. Reprint pagination differs from journal pagination.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 1

Reprinted with corrections from The Bell System Technical Journal,
Vol. 27, pp. 379–423, 623–656, July, October, 1948.
A Mathematical Theory of Communication
By C. E. SHANNON
INTRODUCTION
T
HE recent development of various methods of modulation such as PCM and PPM which exchange
bandwidth for signal-to-noise ratio has intensiﬁed the interest in a general theory of communication. A
basis for such a theory is contained in the important papers of Nyquist1 and Hartley2 on this subject. In the
present paper we will extend the theory to include a number of new factors, in particular the effect of noise
in the channel, and the savings possible due to the statistical structure of the original message and due to the
nature of the ﬁnal destination of the information.
The fundamental problem of communication is that of reproducing at one point either exactly or ap-
proximately a message selected at another point. Frequently the messages have meaning; that is they refer
to or are correlated according to some system with certain physical or conceptual entities. These semantic
aspects of communication are irrelevant to the engineering problem. The signiﬁcant aspect is that the actual
message is one selected from a set of possible messages. The system must be designed to operate for each
possible selection, not just the one which will actually be chosen since this is unknown at the time of design.
If the number of messages in the set is ﬁnite then this number or any monotonic function of this number
can be regarded as a measure of the information produced when one message is chosen from the set, all
choices being equally likely. As was pointed out by Hartley the most natural choice is the logarithmic
function. Although this deﬁnition must be generalized considerably when we consider the inﬂuence of the
statistics of the message and when we have a continuous range of messages, we will in all cases use an
essentially logarithmic measure.
The logarithmic measure is more convenient for various reasons:
1. It is practically more useful. Parameters of engineering importance such as time, bandwidth, number
of relays, etc., tend to vary linearly with the logarithm of the number of possibilities. For example,
adding one relay to a group doubles the number of possible states of the relays. It adds 1 to the base 2
logarithm of this number. Doubling the time roughly squares the number of possible messages, or
doubles the logarithm, etc.
2. It is nearer to our intuitive feeling as to the proper measure. This is closely related to (1) since we in-
tuitively measures entities by linear comparison with common standards. One feels, for example, that
two punched cards should have twice the capacity of one for information storage, and two identical
channels twice the capacity of one for transmitting information.
3. It is mathematically more suitable. Many of the limiting operations are simple in terms of the loga-
rithm but would require clumsy restatement in terms of the number of possibilities.
The choice of a logarithmic base corresponds to the choice of a unit for measuring information. If the
base 2 is used the resulting units may be called binary digits, or more brieﬂy bits, a word suggested by
J. W. Tukey. A device with two stable positions, such as a relay or a ﬂip-ﬂop circuit, can store one bit of
information. N such devices can store N bits, since the total number of possible states is 2N and log2 2N
= N.
If the base 10 is used the units may be called decimal digits. Since
log2 M
= log10 M
=log10 2
= 3 :32log10 M
;
1Nyquist, H., “Certain Factors Affecting Telegraph Speed,” Bell System Technical Journal, April 1924, p. 324; “Certain Topics in
Telegraph Transmission Theory,” A.I.E.E. Trans., v. 47, April 1928, p. 617.
2Hartley, R. V. L., “Transmission of Information,” Bell System Technical Journal, July 1928, p. 535.
1


## PDF page 2

INFORMATION
SOURCE
MESSAGE
TRANSMITTER
SIGNAL
RECEIVED
SIGNAL
RECEIVER
MESSAGE
DESTINATION
NOISE
SOURCE
Fig. 1—Schematic diagram of a general communication system.
a decimal digit is about 3 1
3 bits. A digit wheel on a desk computing machine has ten stable positions and
therefore has a storage capacity of one decimal digit. In analytical work where integration and differentiation
are involved the base e is sometimes useful. The resulting units of information will be called natural units.
Change from the base a to base b merely requires multiplication by logb a.
By a communication system we will mean a system of the type indicated schematically in Fig. 1. It
consists of essentially ﬁve parts:
1. An information source which produces a message or sequence of messages to be communicated to the
receiving terminal. The message may be of various types: (a) A sequence of letters as in a telegraph
of teletype system; (b) A single function of time f
(t
) as in radio or telephony; (c) A function of
time and other variables as in black and white television — here the message may be thought of as a
function f
(x;y
;t
) of two space coordinates and time, the light intensity at point
(x;y) and time t on a
pickup tube plate; (d) Two or more functions of time, say f
(t
), g (t
), h (t
) — this is the case in “three-
dimensional” sound transmission or if the system is intended to service several individual channels in
multiplex; (e) Several functions of several variables — in color television the message consists of three
functions f
(x;y
;t
), g (x;y
;t
), h (x;y
;t
) deﬁned in a three-dimensional continuum — we may also think
of these three functions as components of a vector ﬁeld deﬁned in the region — similarly, several
black and white television sources would produce “messages” consisting of a number of functions
of three variables; (f) Various combinations also occur, for example in television with an associated
audio channel.
2. A transmitter which operates on the message in some way to produce a signal suitable for trans-
mission over the channel. In telephony this operation consists merely of changing sound pressure
into a proportional electrical current. In telegraphy we have an encoding operation which produces
a sequence of dots, dashes and spaces on the channel corresponding to the message. In a multiplex
PCM system the different speech functions must be sampled, compressed, quantized and encoded,
and ﬁnally interleaved properly to construct the signal. Vocoder systems, television and frequency
modulation are other examples of complex operations applied to the message to obtain the signal.
3. The channel is merely the medium used to transmit the signal from transmitter to receiver. It may be
a pair of wires, a coaxial cable, a band of radio frequencies, a beam of light, etc.
4. The receiver ordinarily performs the inverse operation of that done by the transmitter, reconstructing
the message from the signal.
5. The destination is the person (or thing) for whom the message is intended.
We wish to consider certain general problems involving communication systems. To do this it is ﬁrst
necessary to represent the various elements involved as mathematical entities, suitably idealized from their
2


## PDF page 3

physical counterparts. We may roughly classify communication systems into three main categories: discrete,
continuous and mixed. By a discrete system we will mean one in which both the message and the signal
are a sequence of discrete symbols. A typical case is telegraphy where the message is a sequence of letters
and the signal a sequence of dots, dashes and spaces. A continuous system is one in which the message and
signal are both treated as continuous functions, e.g., radio or television. A mixed system is one in which
both discrete and continuous variables appear, e.g., PCM transmission of speech.
We ﬁrst consider the discrete case. This case has applications not only in communication theory, but
also in the theory of computing machines, the design of telephone exchanges and other ﬁelds. In addition
the discrete case forms a foundation for the continuous and mixed cases which will be treated in the second
half of the paper.
PART I: DISCRETE NOISELESS SYSTEMS
1. THE DISCRETE NOISELESS CHANNEL
Teletype and telegraphy are two simple examples of a discrete channel for transmitting information. Gen-
erally, a discrete channel will mean a system whereby a sequence of choices from a ﬁnite set of elementary
symbols S1
;
:
:
:
;Sn can be transmitted from one point to another. Each of the symbols Si is assumed to have
a certain duration in time ti seconds (not necessarily the same for different Si, for example the dots and
dashes in telegraphy). It is not required that all possible sequences of the Si be capable of transmission on
the system; certain sequences only may be allowed. These will be possible signals for the channel. Thus
in telegraphy suppose the symbols are: (1) A dot, consisting of line closure for a unit of time and then line
open for a unit of time; (2) A dash, consisting of three time units of closure and one unit open; (3) A letter
space consisting of, say, three units of line open; (4) A word space of six units of line open. We might place
the restriction on allowable sequences that no spaces follow each other (for if two letter spaces are adjacent,
it is identical with a word space). The question we now consider is how one can measure the capacity of
such a channel to transmit information.
In the teletype case where all symbols are of the same duration, and any sequence of the 32 symbols
is allowed the answer is easy. Each symbol represents ﬁve bits of information. If the system transmits n
symbols per second it is natural to say that the channel has a capacity of 5n bits per second. This does not
mean that the teletype channel will always be transmitting information at this rate — this is the maximum
possible rate and whether or not the actual rate reaches this maximum depends on the source of information
which feeds the channel, as will appear later.
In the more general case with different lengths of symbols and constraints on the allowed sequences, we
make the following deﬁnition:
Deﬁnition: The capacity C of a discrete channel is given by
C
= Lim
T
!∞
logN
(T
)
T
where N
(T
) is the number of allowed signals of duration T.
It is easily seen that in the teletype case this reduces to the previous result. It can be shown that the limit
in question will exist as a ﬁnite number in most cases of interest. Suppose all sequences of the symbols
S1
;
:
:
:
;Sn are allowed and these symbols have durations t1
;
:
:
:
;tn. What is the channel capacity? If N
(t
)
represents the number of sequences of duration t we have
N
(t
)
= N
(t
t1
)
+N
(t
t2
)
+



+N
(t
tn
):
The total number is equal to the sum of the numbers of sequences ending in S1
;S2
;
:
:
:
;Sn and these are
N
(t
t1
);N
(t
t2
);
:
:
:
;N
(t
tn
), respectively. According to a well-known result in ﬁnite differences, N
(t
)
is then asymptotic for large t to Xt
0 where X0 is the largest real solution of the characteristic equation:
X
t1
+X
t2
+



+X
tn
= 1
3


## PDF page 4

and therefore
C
= logX0
:
In case there are restrictions on allowed sequences we may still often obtain a difference equation of this
type and ﬁnd C from the characteristic equation. In the telegraphy case mentioned above
N
(t
)
= N
(t
2 )
+N
(t
4 )
+N
(t
5 )
+N
(t
7 )
+N
(t
8 )
+N
(t
10 )
as we see by counting sequences of symbols according to the last or next to the last symbol occurring.
Hence C is
log
0 where
0 is the positive root of 1
=
2
+
4
+
5
+
7
+
8
+
10. Solving this we ﬁnd
C
= 0 :539.
A very general type of restriction which may be placed on allowed sequences is the following: We
imagine a number of possible states a1
;a2
;
:
:
:
;am. For each state only certain symbols from the set S1
;
:
:
:
;Sn
can be transmitted (different subsets for the different states). When one of these has been transmitted the
state changes to a new state depending both on the old state and the particular symbol transmitted. The
telegraph case is a simple example of this. There are two states depending on whether or not a space was
the last symbol transmitted. If so, then only a dot or a dash can be sent next and the state always changes.
If not, any symbol can be transmitted and the state changes if a space is sent, otherwise it remains the same.
The conditions can be indicated in a linear graph as shown in Fig. 2. The junction points correspond to the
DASH
DOT
DASH
DOT
LETTER SPACE
WORD SPACE
Fig. 2—Graphical representation of the constraints on telegraph symbols.
states and the lines indicate the symbols possible in a state and the resulting state. In Appendix 1 it is shown
that if the conditions on allowed sequences can be described in this form C will exist and can be calculated
in accordance with the following result:
Theorem 1: Let b
(s)
ij be the duration of the sth symbol which is allowable in state i and leads to state j.
Then the channel capacity C is equal to logW where W is the largest real root of the determinant equation:


∑
s
W
b
(s)
ij
ij



= 0
where
ij
= 1 if i
= j and is zero otherwise.
For example, in the telegraph case (Fig. 2) the determinant is:




1
(W
2
+W
4
)
(W
3
+W
6
)
(W
2
+W
4
1 )




= 0 :
On expansion this leads to the equation given above for this case.
2. THE DISCRETE SOURCE OF INFORMATION
We have seen that under very general conditions the logarithm of the number of possible signals in a discrete
channel increases linearly with time. The capacity to transmit information can be speciﬁed by giving this
rate of increase, the number of bits per second required to specify the particular signal used.
We now consider the information source. How is an information source to be described mathematically,
and how much information in bits per second is produced in a given source? The main point at issue is the
effect of statistical knowledge about the source in reducing the required capacity of the channel, by the use
4


## PDF page 5

of proper encoding of the information. In telegraphy, for example, the messages to be transmitted consist of
sequences of letters. These sequences, however, are not completely random. In general, they form sentences
and have the statistical structure of, say, English. The letter E occurs more frequently than Q, the sequence
TH more frequently than XP, etc. The existence of this structure allows one to make a saving in time (or
channel capacity) by properly encoding the message sequences into signal sequences. This is already done
to a limited extent in telegraphy by using the shortest channel symbol, a dot, for the most common English
letter E; while the infrequent letters, Q, X, Z are represented by longer sequences of dots and dashes. This
idea is carried still further in certain commercial codes where common words and phrases are represented
by four- or ﬁve-letter code groups with a considerable saving in average time. The standardized greeting
and anniversary telegrams now in use extend this to the point of encoding a sentence or two into a relatively
short sequence of numbers.
We can think of a discrete source as generating the message, symbol by symbol. It will choose succes-
sive symbols according to certain probabilities depending, in general, on preceding choices as well as the
particular symbols in question. A physical system, or a mathematical model of a system which produces
such a sequence of symbols governed by a set of probabilities, is known as a stochastic process.3 We may
consider a discrete source, therefore, to be represented by a stochastic process. Conversely, any stochastic
process which produces a discrete sequence of symbols chosen from a ﬁnite set may be considered a discrete
source. This will include such cases as:
1. Natural written languages such as English, German, Chinese.
2. Continuous information sources that have been rendered discrete by some quantizing process. For
example, the quantized speech from a PCM transmitter, or a quantized television signal.
3. Mathematical cases where we merely deﬁne abstractly a stochastic process which generates a se-
quence of symbols. The following are examples of this last type of source.
(A) Suppose we have ﬁve letters A, B, C, D, E which are chosen each with probability .2, successive
choices being independent. This would lead to a sequence of which the following is a typical
example.
B D C B C E C C C A D C B D D A A E C E E A
A B B D A E E C A C E E B A E E C B C E A D.
This was constructed with the use of a table of random numbers.4
(B) Using the same ﬁve letters let the probabilities be .4, .1, .2, .2, .1, respectively, with successive
choices independent. A typical message from this source is then:
A A A C D C B D C E A A D A D A C E D A
E A D C A B E D A D D C E C A A A A A D.
(C) A more complicated structure is obtained if successive symbols are not chosen independently
but their probabilities depend on preceding letters. In the simplest case of this type a choice
depends only on the preceding letter and not on ones before that. The statistical structure can
then be described by a set of transition probabilities pi
(j
), the probability that letter i is followed
by letter j. The indices i and j range over all the possible symbols. A second equivalent way of
specifying the structure is to give the “digram” probabilities p (i; j
), i.e., the relative frequency of
the digram i j. The letter frequencies p (i), (the probability of letter i), the transition probabilities
3See, for example, S. Chandrasekhar, “Stochastic Problems in Physics and Astronomy,” Reviews of Modern Physics, v. 15, No. 1,
January 1943, p. 1.
4Kendall and Smith, Tables of Random Sampling Numbers, Cambridge, 1939.
5


## PDF page 6

pi
(j
) and the digram probabilities p (i; j
) are related by the following formulas:
p (i)
= ∑
j
p (i; j
)
= ∑
j
p (j
;i)
= ∑
j
p (j
)p j
(i)
p (i; j
)
= p (i)pi
(j
)
∑
j
pi
(j
)
= ∑
i
p (i)
= ∑
i;j
p (i; j
)
= 1 :
As a speciﬁc example suppose there are three letters A, B, C with the probability tables:
pi
(j
)
j
A
B
C
A
0
4
5
1
5
i
B
1
2
1
2
0
C
1
2
2
5
1
10
i
p (i)
A
9
27
B
16
27
C
2
27
p (i; j
)
j
A
B
C
A
0
4
15
1
15
i
B
8
27
8
27
0
C
1
27
4
135
1
135
A typical message from this source is the following:
A B B A B A B A B A B A B A B B B A B B B B B A B A B A B A B A B B B A C A C A B
B A B B B B A B B A B A C B B B A B A.
The next increase in complexity would involve trigram frequencies but no more. The choice of
a letter would depend on the preceding two letters but not on the message before that point. A
set of trigram frequencies p (i; j
;k
) or equivalently a set of transition probabilities pij
(k
) would
be required. Continuing in this way one obtains successively more complicated stochastic pro-
cesses. In the general n-gram case a set of n-gram probabilities p (i1
;i2
;
:
:
:
;in
) or of transition
probabilities pi1
;i2
;:::;in1
(in
) is required to specify the statistical structure.
(D) Stochastic processes can also be deﬁned which produce a text consisting of a sequence of
“words.” Suppose there are ﬁve letters A, B, C, D, E and 16 “words” in the language with
associated probabilities:
.10 A
.16 BEBE
.11 CABED
.04 DEB
.04 ADEB
.04 BED
.05 CEED
.15 DEED
.05 ADEE
.02 BEED
.08 DAB
.01 EAB
.01 BADD
.05 CA
.04 DAD
.05 EE
Suppose successive “words” are chosen independently and are separated by a space. A typical
message might be:
DAB EE A BEBE DEED DEB ADEE ADEE EE DEB BEBE BEBE BEBE ADEE BED DEED
DEED CEED ADEE A DEED DEED BEBE CABED BEBE BED DAB DEED ADEB.
If all the words are of ﬁnite length this process is equivalent to one of the preceding type, but
the description may be simpler in terms of the word structure and probabilities. We may also
generalize here and introduce transition probabilities between words, etc.
These artiﬁcial languages are useful in constructing simple problems and examples to illustrate vari-
ous possibilities. We can also approximate to a natural language by means of a series of simple artiﬁcial
languages. The zero-order approximation is obtained by choosing all letters with the same probability and
independently. The ﬁrst-order approximation is obtained by choosing successive letters independently but
each letter having the same probability that it has in the natural language.5 Thus, in the ﬁrst-order ap-
proximation to English, E is chosen with probability .12 (its frequency in normal English) and W with
probability .02, but there is no inﬂuence between adjacent letters and no tendency to form the preferred
5Letter, digram and trigram frequencies are given in Secret and Urgent by Fletcher Pratt, Blue Ribbon Books, 1939. Word frequen-
cies are tabulated in Relative Frequency of English Speech Sounds, G. Dewey, Harvard University Press, 1923.
6


## PDF page 7

digrams such as TH, ED, etc. In the second-order approximation, digram structure is introduced. After a
letter is chosen, the next one is chosen in accordance with the frequencies with which the various letters
follow the ﬁrst one. This requires a table of digram frequencies pi
(j
). In the third-order approximation,
trigram structure is introduced. Each letter is chosen with probabilities which depend on the preceding two
letters.
3. THE SERIES OF APPROXIMATIONS TO ENGLISH
To give a visual idea of how this series of processes approaches a language, typical sequences in the approx-
imations to English have been constructed and are given below. In all cases we have assumed a 27-symbol
“alphabet,” the 26 letters and a space.
1. Zero-order approximation (symbols independent and equiprobable).
XFOML RXKHRJFFJUJ ZLPWCFWKCYJ FFJEYVKCQSGHYD QPAAMKBZAACIBZL-
HJQD.
2. First-order approximation (symbols independent but with frequencies of English text).
OCRO HLI RGWR NMIELWIS EU LL NBNESEBYA TH EEI ALHENHTTPA OOBTTVA
NAH BRL.
3. Second-order approximation (digram structure as in English).
ON IE ANTSOUTINYS ARE T INCTORE ST BE S DEAMY ACHIN D ILONASIVE TU-
COOWE AT TEASONARE FUSO TIZIN ANDY TOBE SEACE CTISBE.
4. Third-order approximation (trigram structure as in English).
IN NO IST LAT WHEY CRATICT FROURE BIRS GROCID PONDENOME OF DEMONS-
TURES OF THE REPTAGIN IS REGOACTIONA OF CRE.
5. First-order word approximation. Rather than continue with tetragram,
:
:
: , n-gram structure it is easier
and better to jump at this point to word units. Here words are chosen independently but with their
appropriate frequencies.
REPRESENTING AND SPEEDILY IS AN GOOD APT OR COME CAN DIFFERENT NAT-
URAL HERE HE THE A IN CAME THE TO OF TO EXPERT GRAY COME TO FURNISHES
THE LINE MESSAGE HAD BE THESE.
6. Second-order word approximation. The word transition probabilities are correct but no further struc-
ture is included.
THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHAR-
ACTER OF THIS POINT IS THEREFORE ANOTHER METHOD FOR THE LETTERS THAT
THE TIME OF WHO EVER TOLD THE PROBLEM FOR AN UNEXPECTED.
The resemblance to ordinary English text increases quite noticeably at each of the above steps. Note that
these samples have reasonably good structure out to about twice the range that is taken into account in their
construction. Thus in (3) the statistical process insures reasonable text for two-letter sequences, but four-
letter sequences from the sample can usually be ﬁtted into good sentences. In (6) sequences of four or more
words can easily be placed in sentences without unusual or strained constructions. The particular sequence
of ten words “attack on an English writer that the character of this” is not at all unreasonable. It appears then
that a sufﬁciently complex stochastic process will give a satisfactory representation of a discrete source.
The ﬁrst two samples were constructed by the use of a book of random numbers in conjunction with
(for example 2) a table of letter frequencies. This method might have been continued for (3), (4) and (5),
since digram, trigram and word frequency tables are available, but a simpler equivalent method was used.
7


## PDF page 8

To construct (3) for example, one opens a book at random and selects a letter at random on the page. This
letter is recorded. The book is then opened to another page and one reads until this letter is encountered.
The succeeding letter is then recorded. Turning to another page this second letter is searched for and the
succeeding letter recorded, etc. A similar process was used for (4), (5) and (6). It would be interesting if
further approximations could be constructed, but the labor involved becomes enormous at the next stage.
4. GRAPHICAL REPRESENTATION OF A MARKOFF PROCESS
Stochastic processes of the type described above are known mathematically as discrete Markoff processes
and have been extensively studied in the literature.6 The general case can be described as follows: There
exist a ﬁnite number of possible “states” of a system; S1
;S2
;
:
:
:
;Sn. In addition there is a set of transition
probabilities; pi
(j
) the probability that if the system is in state Si it will next go to state S j. To make this
Markoff process into an information source we need only assume that a letter is produced for each transition
from one state to another. The states will correspond to the “residue of inﬂuence” from preceding letters.
The situation can be represented graphically as shown in Figs. 3, 4 and 5. The “states” are the junction
A
B
C
D
E
.
.
.
.
.
Fig. 3—A graph corresponding to the source in example B.
points in the graph and the probabilities and letters produced for a transition are given beside the correspond-
ing line. Figure 3 is for the example B in Section 2, while Fig. 4 corresponds to the example C. In Fig. 3
A
A
B
B
B
C
C
.
.
.
.
.
.
.
Fig. 4—A graph corresponding to the source in example C.
there is only one state since successive letters are independent. In Fig. 4 there are as many states as letters.
If a trigram example were constructed there would be at most n2 states corresponding to the possible pairs
of letters preceding the one being chosen. Figure 5 is a graph for the case of word structure in example D.
Here S corresponds to the “space” symbol.
5. ERGODIC AND MIXED SOURCES
As we have indicated above a discrete source for our purposes can be considered to be represented by a
Markoff process. Among the possible discrete Markoff processes there is a group with special properties
of signiﬁcance in communication theory. This special class consists of the “ergodic” processes and we
shall call the corresponding sources ergodic sources. Although a rigorous deﬁnition of an ergodic process is
somewhat involved, the general idea is simple. In an ergodic process every sequence produced by the process
6For a detailed treatment see M. Fr´echet, M´ethode des fonctions arbitraires. Th´eorie des ´ev´enements en chaˆıne dans le cas d’un
nombre ﬁni d’´etats possibles. Paris, Gauthier-Villars, 1938.
8


