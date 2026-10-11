# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 145

5.6
HUFFMAN CODES
119
Codeword
Length
Codeword
X
Probability
2
01
1
0.25
0.3
0.45
0.55
1
2
10
2
0.25
0.25
0.3
0.45
2
11
3
0.2
0.25
0.25
3
000
4
0.15
0.2
3
001
5
0.15
This code has average length 2.3 bits.
Example 5.6.2
Consider a ternary code for the same random variable.
Now we combine the three least likely symbols into one supersymbol and
obtain the following table:
Codeword
X
Probability
1
1
0.25
0.5
1
2
2
0.25
0.25
00
3
0.2
0.25
01
4
0.15
02
5
0.15
This code has an average length of 1.5 ternary digits.
Example 5.6.3
If D ≥3, we may not have a sufﬁcient number of sym-
bols so that we can combine them D at a time. In such a case, we add
dummy symbols to the end of the set of symbols. The dummy symbols
have probability 0 and are inserted to ﬁll the tree. Since at each stage of
the reduction, the number of symbols is reduced by D −1, we want the
total number of symbols to be 1 + k(D −1), where k is the number of
merges. Hence, we add enough dummy symbols so that the total number
of symbols is of this form. For example:
This code has an average length of 1.7 ternary digits.


## PDF page 146

120
DATA COMPRESSION
A proof of the optimality of Huffman coding is given in Section 5.8.
5.7
SOME COMMENTS ON HUFFMAN CODES
1. Equivalence of source coding and 20 questions. We now digress
to show the equivalence of coding and the game “20 questions”.
Suppose that we wish to ﬁnd the most efﬁcient series of yes–no
questions to determine an object from a class of objects. Assuming
that we know the probability distribution on the objects, can we ﬁnd
the most efﬁcient sequence of questions? (To determine an object,
we need to ensure that the responses to the sequence of questions
uniquely identiﬁes the object from the set of possible objects; it is
not necessary that the last question have a “yes” answer.)
We ﬁrst show that a sequence of questions is equivalent to a code
for the object. Any question depends only on the answers to the
questions before it. Since the sequence of answers uniquely deter-
mines the object, each object has a different sequence of answers,
and if we represent the yes–no answers by 0’s and 1’s, we have a
binary code for the set of objects. The average length of this code
is the average number of questions for the questioning scheme.
Also, from a binary code for the set of objects, we can ﬁnd a
sequence of questions that correspond to the code, with the average
number of questions equal to the expected codeword length of the
code. The ﬁrst question in this scheme becomes: Is the ﬁrst bit equal
to 1 in the object’s codeword?
Since the Huffman code is the best source code for a random
variable, the optimal series of questions is that determined by the
Huffman code. In Example 5.6.1 the optimal ﬁrst question is: Is
X equal to 2 or 3? The answer to this determines the ﬁrst bit of
the Huffman code. Assuming that the answer to the ﬁrst question
is “yes,” the next question should be “Is X equal to 3?”, which
determines the second bit. However, we need not wait for the answer
to the ﬁrst question to ask the second. We can ask as our second
question “Is X equal to 1 or 3?”, determining the second bit of the
Huffman code independent of the ﬁrst.
The expected number of questions EQ in this optimal scheme
satisﬁes
H(X) ≤EQ < H(X) + 1.
(5.61)


## PDF page 147

5.7
SOME COMMENTS ON HUFFMAN CODES
121
2. Huffman coding for weighted codewords. Huffman’s algorithm for
minimizing  pili can be applied to any set of numbers pi ≥0,
regardless of  pi. In this case, the Huffman code minimizes the
sum of weighted code lengths  wili rather than the average code
length.
Example 5.7.1
We perform the weighted minimization using the
same algorithm.
In this case the code minimizes the weighted sum of the codeword
lengths, and the minimum weighted sum is 36.
3. Huffman coding and “slice” questions (Alphabetic codes). We have
described the equivalence of source coding with the game of 20
questions. The optimal sequence of questions corresponds to an
optimal source code for the random variable. However, Huffman
codes ask arbitrary questions of the form “Is X ∈A?” for any set
A ⊆{1, 2, . . . , m}.
Now we consider the game “20 questions” with a restricted set
of questions. Speciﬁcally, we assume that the elements of X =
{1, 2, . . . , m} are ordered so that p1 ≥p2 ≥· · · ≥pm and that the
only questions allowed are of the form “Is X > a?” for some a. The
Huffman code constructed by the Huffman algorithm may not cor-
respond to slices (sets of the form {x : x < a}). If we take the code-
word lengths (l1 ≤l2 ≤· · · ≤lm, by Lemma 5.8.1) derived from the
Huffman code and use them to assign the symbols to the code tree
by taking the ﬁrst available node at the corresponding level, we
will construct another optimal code. However, unlike the Huffman
code itself, this code is a slice code, since each question (each bit
of the code) splits the tree into sets of the form {x : x > a} and
{x : x < a}.
We illustrate this with an example.
Example 5.7.2
Consider the ﬁrst example of Section 5.6. The
code that was constructed by the Huffman coding procedure is not a


## PDF page 148

122
DATA COMPRESSION
slice code. But using the codeword lengths from the Huffman pro-
cedure, namely, {2, 2, 2, 3, 3}, and assigning the symbols to the ﬁrst
available node on the tree, we obtain the following code for this
random variable:
1 →00,
2 →01,
3 →10,
4 →110,
5 →111
It can be veriﬁed that this code is a slice code, codes known as
alphabetic codes because the codewords are ordered alphabetically.
4. Huffman codes and Shannon codes. Using codeword lengths of
⌈log 1
pi ⌉(which is called Shannon coding) may be much worse than
the optimal code for some particular symbol. For example, con-
sider two symbols, one of which occurs with probability 0.9999 and
the other with probability 0.0001. Then using codeword lengths of
⌈log 1
pi ⌉gives codeword lengths of 1 bit and 14 bits, respectively.
The optimal codeword length is obviously 1 bit for both symbols.
Hence, the codeword for the infrequent symbol is much longer in
the Shannon code than in the optimal code.
Is it true that the codeword lengths for an optimal code are always
less than ⌈log 1
pi ⌉? The following example illustrates that this is not
always true.
Example 5.7.3
Consider a random variable X with a distribution
1
3, 1
3, 1
4, 1
12

. The Huffman coding procedure results in codeword
lengths of (2, 2, 2, 2) or (1, 2, 3, 3) [depending on where one puts
the merged probabilities, as the reader can verify (Problem 5.5.12)].
Both these codes achieve the same expected codeword length. In the
second code, the third symbol has length 3, which is greater than
⌈log 1
p3 ⌉. Thus, the codeword length for a Shannon code could be
less than the codeword length of the corresponding symbol of an
optimal (Huffman) code. This example also illustrates the fact that
the set of codeword lengths for an optimal code is not unique (there
may be more than one set of lengths with the same expected value).
Although either the Shannon code or the Huffman code can be
shorter for individual symbols, the Huffman code is shorter on aver-
age. Also, the Shannon code and the Huffman code differ by less
than 1 bit in expected codelength (since both lie between H and
H + 1.)


## PDF page 149

5.8
OPTIMALITY OF HUFFMAN CODES
123
5. Fano codes. Fano proposed a suboptimal procedure for constructing
a source code, which is similar to the idea of slice codes. In his
method we ﬁrst order the probabilities in decreasing order. Then we
choose k such that

k
i=1 pi −m
i=k+1 pi
 is minimized. This point
divides the source symbols into two sets of almost equal probability.
Assign 0 for the ﬁrst bit of the upper set and 1 for the lower set.
Repeat this process for each subset. By this recursive procedure, we
obtain a code for each source symbol. This scheme, although not
optimal in general, achieves L(C) ≤H(X) + 2. (See [282].)
5.8
OPTIMALITY OF HUFFMAN CODES
We prove by induction that the binary Huffman code is optimal. It is
important to remember that there are many optimal codes: inverting all
the bits or exchanging two codewords of the same length will give another
optimal code. The Huffman procedure constructs one such optimal code.
To prove the optimality of Huffman codes, we ﬁrst prove some properties
of a particular optimal code.
Without loss of generality, we will assume that the probability masses
are ordered, so that p1 ≥p2 ≥· · · ≥pm. Recall that a code is optimal if
 pili is minimal.
Lemma 5.8.1
For any distribution, there exists an optimal instantaneous
code (with minimum expected length) that satisﬁes the following proper-
ties:
1. The lengths are ordered inversely with the probabilities (i.e., if pj >
pk, then lj ≤lk).
2. The two longest codewords have the same length.
3. Two of the longest codewords differ only in the last bit and corre-
spond to the two least likely symbols.
Proof:
The proof amounts to swapping, trimming, and rearranging, as
shown in Figure 5.3. Consider an optimal code Cm:
• If pj > pk, then lj ≤lk. Here we swap codewords.
Consider C′
m, with the codewords j and k of Cm interchanged. Then
L(C′
m) −L(Cm) =

pili′ −

pili
(5.62)
= pjlk + pklj −pjlj −pklk
(5.63)
= (pj −pk)(lk −lj).
(5.64)


## PDF page 150

124
DATA COMPRESSION
0
0
1
1
1
1
1
0
0
0
p1
p3
p4
p2
p5
(a)
(b)
0
1
1
1
1
0
0
0
p1
p3
p4
p2
p5
(c)
(d)
1
1
1
0
0
1
0
0
p5
p2
p1
p3
p4
1
1
1
0
0
1
0
0
p2
p2
p3
p4
p5
FIGURE 5.3. Properties of optimal codes. We assume that p1 ≥p2 ≥· · · ≥pm. A possible
instantaneous code is given in (a). By trimming branches without siblings, we improve the
code to (b). We now rearrange the tree as shown in (c), so that the word lengths are ordered
by increasing length from top to bottom. Finally, we swap probability assignments to improve
the expected depth of the tree, as shown in (d). Every optimal code can be rearranged and
swapped into canonical form as in (d), where l1 ≤l2 ≤· · · ≤lm and lm−1 = lm, and the last
two codewords differ only in the last bit.
But pj −pk > 0, and since Cm is optimal, L(C′
m) −L(Cm) ≥0.
Hence, we must have lk ≥lj. Thus, Cm itself satisﬁes property 1.
• The two longest codewords are of the same length. Here we trim the
codewords. If the two longest codewords are not of the same length,
one can delete the last bit of the longer one, preserving the preﬁx
property and achieving lower expected codeword length. Hence, the
two longest codewords must have the same length. By property 1, the
longest codewords must belong to the least probable source symbols.
• The two longest codewords differ only in the last bit and correspond
to the two least likely symbols. Not all optimal codes satisfy this
property, but by rearranging, we can ﬁnd an optimal code that does.
If there is a maximal-length codeword without a sibling, we can delete
the last bit of the codeword and still satisfy the preﬁx property. This
reduces the average codeword length and contradicts the optimality


## PDF page 151

5.8
OPTIMALITY OF HUFFMAN CODES
125
of the code. Hence, every maximal-length codeword in any optimal
code has a sibling. Now we can exchange the longest codewords so
that the two lowest-probability source symbols are associated with
two siblings on the tree. This does not change the expected length,
 pili. Thus, the codewords for the two lowest-probability source
symbols have maximal length and agree in all but the last bit.
Summarizing, we have shown that if p1 ≥p2 ≥· · · ≥pm, there exists
an optimal code with l1 ≤l2 ≤· · · ≤lm−1 = lm, and codewords C(xm−1)
and C(xm) that differ only in the last bit.
□
Thus, we have shown that there exists an optimal code satisfy-
ing the properties of the lemma. We call such codes canonical codes.
For any probability mass function for an alphabet of size m, p =
(p1, p2, . . . , pm) with p1 ≥p2 ≥· · · ≥pm, we deﬁne the Huffman reduc-
tion p′ = (p1, p2, . . . , pm−2, pm−1 + pm) over an alphabet of size m −1
(Figure 5.4). Let C∗
m−1(p′) be an optimal code for p′, and let C∗
m(p) be
the canonical optimal code for p.
The proof of optimality will follow from two constructions: First, we
expand an optimal code for p′ to construct a code for p, and then we
(c)
p1
p2
p3
0
0
0
1
1
1
p4 + p5
(a)
p1
p2
p3
p4
p5
0
0
0
0
1
1
1
1
(b)
p1
p2
p3
p4 + p5
0
0
0
1
1
1
FIGURE 5.4. Induction step for Huffman coding. Let p1 ≥p2 ≥· · · ≥p5. A canonical
optimal code is illustrated in (a). Combining the two lowest probabilities, we obtain the
code in (b). Rearranging the probabilities in decreasing order, we obtain the canonical code
in (c) for m −1 symbols.


## PDF page 152

126
DATA COMPRESSION
condense an optimal canonical code for p to construct a code for the
Huffman reduction p′. Comparing the average codeword lengths for the
two codes establishes that the optimal code for p can be obtained by
extending the optimal code for p′.
From the optimal code for p′, we construct an extension code for m
elements as follows: Take the codeword in C∗
m−1 corresponding to weight
pm−1 + pm and extend it by adding a 0 to form a codeword for symbol
m −1 and by adding 1 to form a codeword for symbol m. The code
construction is illustrated as follows:
C∗
m−1(p′)
Cm(p)
p1
w′
1
l′
1
w1 = w′
1
l1 = l′
1
p2
w′
2
l′
2
w2 = w′
2
l2 = l′
2
...
...
...
...
...
pm−2
w′
m−2
l′
m−2
wm−2 = w′
m−2
lm−2 = l′
m−2
pm−1 + pm
w′
m−1
l′
m−1
wm−1 = w′
m−10
lm−1 = l′
m−1 + 1
wm = w′
m−11
lm = l′
m−1 + 1
(5.65)
Calculation of the average length 
i p′
il′
i shows that
L(p) = L∗(p′) + pm−1 + pm.
(5.66)
Similarly, from the canonical code for p, we construct a code for p′ by
merging the codewords for the two lowest-probability symbols m −1 and
m with probabilities pm−1 and pm, which are siblings by the properties
of the canonical code. The new code for p′ has average length
L(p′) =
m−2

i=1
pili + pm−1(lm−1 −1) + pm(lm −1)
(5.67)
=
m

i=1
pili −pm−1 −pm
(5.68)
= L∗(p) −pm−1 −pm.
(5.69)
Adding (5.66) and (5.69) together, we obtain
L(p′) + L(p) = L∗(p′) + L∗(p)
(5.70)
or
(L(p′) −L∗(p′)) + (L(p) −L∗(p)) = 0.
(5.71)


