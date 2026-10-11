# A Mathematical Theory of Communication

Source ID: C05
Authors: Claude E. Shannon
Source URL: https://www.princeton.edu/~wbialek/rome/refs/shannon_48.pdf
DOI: 10.1002/j.1538-7305.1948.tb01338.x; 10.1002/j.1538-7305.1948.tb00917.x
Identity: Corrected reprint of the two-part Bell System Technical Journal article, 1948. Reprint pagination differs from journal pagination.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 25

As in the noiseless case a delay is generally required to approach the ideal encoding. It now has the
additional function of allowing a large sample of noise to affect the signal before any judgment is made
at the receiving point as to the original message. Increasing the sample size always sharpens the possible
statistical assertions.
The content of Theorem 11 and its proof can be formulated in a somewhat different way which exhibits
the connection with the noiseless case more clearly. Consider the possible signals of duration T and suppose
a subset of them is selected to be used. Let those in the subset all be used with equal probability, and suppose
the receiver is constructed to select, as the original signal, the most probable cause from the subset, when a
perturbed signal is received. We deﬁne N
(T
;q ) to be the maximum number of signals we can choose for the
subset such that the probability of an incorrect interpretation is less than or equal to q.
Theorem 12: Lim
T
!∞
logN
(T
;q )
T
= C, where C is the channel capacity, provided that q does not equal 0 or
1.
In other words, no matter how we set out limits of reliability, we can distinguish reliably in time T
enough messages to correspond to aboutCT bits, when T is sufﬁciently large. Theorem 12 can be compared
with the deﬁnition of the capacity of a noiseless channel given in Section 1.
15. EXAMPLE OF A DISCRETE CHANNEL AND ITS CAPACITY
A simple example of a discrete channel is indicated in Fig. 11. There are three possible symbols. The ﬁrst is
never affected by noise. The second and third each have probability p of coming through undisturbed, and
q of being changed into the other of the pair. We have (letting

=
[plog p
+ qlogq ] and P and Q be the
p
p
q
q
TRANSMITTED
SYMBOLS
RECEIVED
SYMBOLS
Fig. 11—Example of a discrete channel.
probabilities of using the ﬁrst and second symbols)
H
(x)
=
PlogP
2QlogQ
Hy
(x)
= 2Q:
We wish to choose P and Q in such a way as to maximize H
(x)
Hy
(x), subject to the constraint P
+2Q
= 1.
Hence we consider
U
=
PlogP
2QlogQ
2Q
+
(P
+2Q)
∂U
∂P
=
1
logP
+

= 0
∂U
∂Q
=
2
2logQ
2 
+2 
= 0 :
Eliminating

logP
= logQ
+

P
= Qe

= Q
25


## PDF page 26

P
=


+2
Q
=
1

+2
:
The channel capacity is then
C
= log

+2

:
Note how this checks the obvious values in the cases p
= 1 and p
= 1
2. In the ﬁrst,

= 1 and C
= log3,
which is correct since the channel is then noiseless with three possible symbols. If p
= 1
2,

= 2 and
C
= log2. Here the second and third symbols cannot be distinguished at all and act together like one
symbol. The ﬁrst symbol is used with probability P
= 1
2 and the second and third together with probability
1
2. This may be distributed between them in any desired way and still achieve the maximum capacity.
For intermediate values of p the channel capacity will lie between log2 and log3. The distinction
between the second and third symbols conveys some information but not as much as in the noiseless case.
The ﬁrst symbol is used somewhat more frequently than the other two because of its freedom from noise.
16. THE CHANNEL CAPACITY IN CERTAIN SPECIAL CASES
If the noise affects successive channel symbols independently it can be described by a set of transition
probabilities pij. This is the probability, if symbol i is sent, that j will be received. The maximum channel
rate is then given by the maximum of
∑
i;j
Pipij log∑
i
Pipij
+∑
i;j
Pipij log pij
where we vary the Pi subject to ∑Pi
= 1. This leads by the method of Lagrange to the equations,
∑
j
psj log
psj
∑i Pipij
=

s
= 1 ;2 ;
:
:
:
:
Multiplying by Ps and summing on s shows that

= C. Let the inverse of psj (if it exists) be hst so that
∑s hst psj
=
t j. Then:
∑
s;j
hst psj log psj
log∑
i
Pipit
= C∑
s
hst
:
Hence:
∑
i
Pipit
= exp
h
C∑
s
hst
+∑
s;j
hst psj log psj
i
or,
Pi
=∑
t
hit exp
h
C∑
s
hst
+∑
s;j
hst psj log psj
i
:
This is the system of equations for determining the maximizing values of Pi, with C to be determined so
that ∑Pi
= 1. When this is done C will be the channel capacity, and the Pi the proper probabilities for the
channel symbols to achieve this capacity.
If each input symbol has the same set of probabilities on the lines emerging from it, and the same is true
of each output symbol, the capacity can be easily calculated. Examples are shown in Fig. 12. In such a case
Hx
(y) is independent of the distribution of probabilities on the input symbols, and is given by
∑pi log pi
where the pi are the values of the transition probabilities from any input symbol. The channel capacity is
Max

H
(y)
Hx
(y)

= MaxH
(y)
+∑pi log pi
:
The maximum of H
(y) is clearly logm where m is the number of output symbols, since it is possible to make
them all equally probable by making the input symbols equally probable. The channel capacity is therefore
C
= logm
+∑pi log pi
:
26


## PDF page 27

a
b
c
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
/
/
/
/
/
Fig. 12—Examples of discrete channels with the same transition probabilities for each input and for each output.
In Fig. 12a it would be
C
= log4
log2
= log2 :
This could be achieved by using only the 1st and 3d symbols. In Fig. 12b
C
= log4
 2
3 log3
 1
3 log6
= log4
log3
 1
3 log2
= log 1
32
5
3
:
In Fig. 12c we have
C
= log3
 1
2 log2
 1
3 log3
 1
6 log6
= log
3
2
1
2 3
1
3 6
1
6
:
Suppose the symbols fall into several groups such that the noise never causes a symbol in one group to
be mistaken for a symbol in another group. Let the capacity for the nth group be Cn (in bits per second)
when we use only the symbols in this group. Then it is easily shown that, for best use of the entire set, the
total probability Pn of all symbols in the nth group should be
Pn
= 2Cn
∑2Cn
:
Within a group the probability is distributed just as it would be if these were the only symbols being used.
The channel capacity is
C
= log∑2Cn
:
17. AN EXAMPLE OF EFFICIENT CODING
The following example, although somewhat unrealistic, is a case in which exact matching to a noisy channel
is possible. There are two channel symbols, 0 and 1, and the noise affects them in blocks of seven symbols.
A block of seven is either transmitted without error, or exactly one symbol of the seven is incorrect. These
eight possibilities are equally likely. We have
C
= Max

H
(y)
Hx
(y)

= 1
7

7
+ 8
8 log 1
8

= 4
7 bits/symbol
:
An efﬁcient code, allowing complete correction of errors and transmitting at the rate C, is the following
(found by a method due to R. Hamming):
27


## PDF page 28

Let a block of seven symbols be X1
;X2
;
:
:
:
;X7. Of these X3, X5, X6 and X7 are message symbols and
chosen arbitrarily by the source. The other three are redundant and calculated as follows:
X4
is chosen to make

= X4
+X5
+X6
+X7
even
X2
“
“
“
“

= X2
+X3
+X6
+X7
“
X1
“
“
“
“

= X1
+X3
+X5
+X7
“
When a block of seven is received
;
 and
 are calculated and if even called zero, if odd called one. The
binary number


 then gives the subscript of the Xi that is incorrect (if 0 there was no error).
APPENDIX 1
THE GROWTH OF THE NUMBER OF BLOCKS OF SYMBOLS WITH A FINITE STATE CONDITION
Let Ni
(L) be the number of blocks of symbols of length L ending in state i. Then we have
Nj
(L)
= ∑
i;s
Ni
L
b
(s)
ij

where b1
ij
;b2
ij
;
:
:
:
;bm
ij are the length of the symbols which may be chosen in state i and lead to state j. These
are linear difference equations and the behavior as L
! ∞must be of the type
Nj
= AjW L
:
Substituting in the difference equation
AjW L
= ∑
i;s
AiW Lb
(s)
ij
or
Aj
= ∑
i;s
AiW
b
(s)
ij
∑
i

∑
s
W
b
(s)
ij
ij

Ai
= 0 :
For this to be possible the determinant
D(W
)
=
jaij
j
=


∑
s
W
b
(s)
ij
ij



must vanish and this determines W, which is, of course, the largest real root of D
= 0.
The quantity C is then given by
C
= Lim
L!∞
log∑AjW L
L
= logW
and we also note that the same growth properties result if we require that all blocks start in the same (arbi-
trarily chosen) state.
APPENDIX 2
DERIVATION OF H
=
∑pi log pi
Let H
1
n
; 1
n
;
:
:
:
; 1
n

= A(n ). From condition (3) we can decompose a choice from sm equally likely possi-
bilities into a series of m choices from s equally likely possibilities and obtain
A(sm
)
= mA(s):
28


## PDF page 29

Similarly
A(tn
)
= nA(t
):
We can choose n arbitrarily large and ﬁnd an m to satisfy
sm
 tn
< s
(m+1 )
:
Thus, taking logarithms and dividing by nlogs,
m
n
 log t
log s
 m
n
+ 1
n
or


m
n
 log t
log s



<

where
 is arbitrarily small. Now from the monotonic property of A(n ),
A(sm
)
 A(tn
)
 A(sm+1
)
mA(s)
 nA(t
)

(m
+1 )A(s):
Hence, dividing by nA(s),
m
n
 A(t
)
A(s)
 m
n
+ 1
n
or


m
n
 A(t
)
A(s)



<



 A(t
)
A(s)
 logt
logs



< 2 
A(t
)
= K logt
where K must be positive to satisfy (2).
Now suppose we have a choice from n possibilities with commeasurable probabilities pi
= ni
∑ni
where
the ni are integers. We can break down a choice from ∑ni possibilities into a choice from n possibilities
with probabilities p1
;
:
:
:
; pn and then, if the ith was chosen, a choice from ni with equal probabilities. Using
condition (3) again, we equate the total choice from ∑ni as computed by two methods
K log∑ni
= H
(p1
;
:
:
:
; pn
)
+K∑pi logni
:
Hence
H
= K
h
∑pi log∑ni
∑pi logni
i
=
K∑pi log ni
∑ni
=
K∑pi log pi
:
If the pi are incommeasurable, they may be approximated by rationals and the same expression must hold
by our continuity assumption. Thus the expression holds in general. The choice of coefﬁcient K is a matter
of convenience and amounts to the choice of a unit of measure.
APPENDIX 3
THEOREMS ON ERGODIC SOURCES
If it is possible to go from any state with P
> 0 to any other along a path of probability p
> 0, the system is
ergodic and the strong law of large numbers can be applied. Thus the number of times a given path pij in
the network is traversed in a long sequence of length N is about proportional to the probability of being at
i, say Pi, and then choosing this path, PipijN. If N is large enough the probability of percentage error
 in
this is less than
 so that for all but a set of small probability the actual numbers lie within the limits
(Pipij


)N
:
Hence nearly all sequences have a probability p given by
p
= ∏p
(Pipij

)N
ij
29


## PDF page 30

and log p
N
is limited by
log p
N
= ∑
(Pipij


)log pij
or


log p
N
∑Pipij log pij



<

:
This proves Theorem 3.
Theorem 4 follows immediately from this on calculating upper and lower bounds for n (q ) based on the
possible range of values of p in Theorem 3.
In the mixed (not ergodic) case if
L
= ∑piLi
and the entropies of the components are H1
 H2




 Hn we have the
Theorem: Lim
N
!∞
logn (q )
N
=
'(q ) is a decreasing step function,
'(q )
= Hs
in the interval
s1
∑
1
i
< q
<
s
∑
1
i
:
To prove Theorems 5 and 6 ﬁrst note that FN is monotonic decreasing because increasing N adds a
subscript to a conditional entropy. A simple substitution for pBi
(S j
) in the deﬁnition of FN shows that
FN
= NGN
(N
1 )GN
1
and summing this for all N gives GN
= 1
N ∑Fn. Hence GN
 FN and GN monotonic decreasing. Also they
must approach the same limit. By using Theorem 3 we see that Lim
N
!∞GN
= H.
APPENDIX 4
MAXIMIZING THE RATE FOR A SYSTEM OF CONSTRAINTS
Suppose we have a set of constraints on sequences of symbols that is of the ﬁnite state type and can be
represented therefore by a linear graph. Let
`
(s)
ij be the lengths of the various symbols that can occur in
passing from state i to state j. What distribution of probabilities Pi for the different states and p
(s)
ij for
choosing symbol s in state i and going to state j maximizes the rate of generating information under these
constraints? The constraints deﬁne a discrete channel and the maximum rate must be less than or equal to
the capacity C of this channel, since if all blocks of large length were equally likely, this rate would result,
and if possible this would be best. We will show that this rate can be achieved by proper choice of the Pi and
p
(s)
ij .
The rate in question is
∑Pip
(s)
ij log p
(s)
ij
∑Pip
(s)
ij
`
(s)
ij
= N
M
:
Let
`ij
= ∑s
`
(s)
ij . Evidently for a maximum p
(s)
ij
= kexp
`
(s)
ij . The constraints on maximization are ∑Pi
=
1, ∑j pij
= 1, ∑Pi
(pij
ij
)
= 0. Hence we maximize
U
=
∑Pipij log pij
∑Pipij
`ij
+
∑
i
Pi
+∑
ipij
+∑
jPi
(pij
ij
)
∂U
∂pij
=
MPi
(1
+logpij
)
+NPi
`ij
M2
+

+
i
+
iPi
= 0 :
30


## PDF page 31

Solving for pij
pij
= AiBjD
`ij
:
Since
∑
j
pij
= 1 ;
A
1
i
= ∑
j
BjD
`ij
pij
=
BjD
`ij
∑s BsD
`is
:
The correct value of D is the capacity C and the Bj are solutions of
Bi
=∑BjC
`ij
for then
pij
= Bj
Bi
C
`ij
∑Pi
Bj
Bi
C
`ij
= Pj
or
∑
Pi
Bi
C
`ij
= Pj
Bj
:
So that if
i satisfy
∑
iC
`ij
=
j
Pi
= Bi
i
:
Both the sets of equations for Bi and
i can be satisﬁed since C is such that
jC
`ij
ij
j
= 0 :
In this case the rate is
∑Pipij log Bj
Bi C
`ij
∑Pipij
`ij
= C
∑Pipij log Bj
Bi
∑Pipij
`ij
but
∑Pipij
(logBj
logBi
)
= ∑
j
Pj logBj
∑Pi logBi
= 0
Hence the rate is C and as this could never be exceeded this is the maximum, justifying the assumed solution.
31


## PDF page 32

PART III: MATHEMATICAL PRELIMINARIES
In this ﬁnal installment of the paper we consider the case where the signals or the messages or both are
continuously variable, in contrast with the discrete nature assumed heretofore. To a considerable extent the
continuous case can be obtained through a limiting process from the discrete case by dividing the continuum
of messages and signals into a large but ﬁnite number of small regions and calculating the various parameters
involved on a discrete basis. As the size of the regions is decreased these parameters in general approach as
limits the proper values for the continuous case. There are, however, a few new effects that appear and also
a general change of emphasis in the direction of specialization of the general results to particular cases.
We will not attempt, in the continuous case, to obtain our results with the greatest generality, or with
the extreme rigor of pure mathematics, since this would involve a great deal of abstract measure theory
and would obscure the main thread of the analysis. A preliminary study, however, indicates that the theory
can be formulated in a completely axiomatic and rigorous manner which includes both the continuous and
discrete cases and many others. The occasional liberties taken with limiting processes in the present analysis
can be justiﬁed in all cases of practical interest.
18. SETS AND ENSEMBLES OF FUNCTIONS
We shall have to deal in the continuous case with sets of functions and ensembles of functions. A set of
functions, as the name implies, is merely a class or collection of functions, generally of one variable, time.
It can be speciﬁed by giving an explicit representation of the various functions in the set, or implicitly by
giving a property which functions in the set possess and others do not. Some examples are:
1. The set of functions:
f

(t
)
= sin(t
+

):
Each particular value of
 determines a particular function in the set.
2. The set of all functions of time containing no frequencies over W cycles per second.
3. The set of all functions limited in band to W and in amplitude to A.
4. The set of all English speech signals as functions of time.
An ensemble of functions is a set of functions together with a probability measure whereby we may
determine the probability of a function in the set having certain properties.1 For example with the set,
f

(t
)
= sin (t
+

);
we may give a probability distribution for
, P(
). The set then becomes an ensemble.
Some further examples of ensembles of functions are:
1. A ﬁnite set of functions fk
(t
) (k
= 1 ;2 ;
:
:
:
;n) with the probability of fk being pk.
2. A ﬁnite dimensional family of functions
f
(1
;
2
;
:
:
:
;
n;t
)
with a probability distribution on the parameters
i:
p (1
;
:
:
:
;
n
):
For example we could consider the ensemble deﬁned by
f
(a1
;
:
:
:
;an
;
1
;
:
:
:
;
n;t
)
=
n
∑
i=1
ai sini(!t
+
i
)
with the amplitudes ai distributed normally and independently, and the phases
i distributed uniformly
(from 0 to 2 ) and independently.
1In mathematical terminology the functions belong to a measure space whose total measure is unity.
32


