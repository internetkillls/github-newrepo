# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 193

6.3
DEPENDENT HORSE RACES AND ENTROPY RATE
167
The quantity 1
nH(X1, X2, . . . , Xn) is the average entropy per race. For
a stationary process with entropy rate H(X), the limit in (6.35) yields
lim
n→∞
1
nE log Sn + H(X) = log m.
(6.36)
Again, we have the result that the entropy rate plus the doubling rate is a
constant.
The expectation in (6.36) can be removed if the process is ergodic. It
will be shown in Chapter 16 that for an ergodic sequence of horse races,
Sn
.= 2nW
with probability 1,
(6.37)
where W = log m −H(X) and
H(X) = lim 1
nH(X1, X2, . . . , Xn).
(6.38)
Example 6.3.1
(Red and black)
In this example, cards replace horses
and the outcomes become more predictable as time goes on. Consider the
case of betting on the color of the next card in a deck of 26 red and 26
black cards. Bets are placed on whether the next card will be red or black,
as we go through the deck. We also assume that the game pays 2-for-1;
that is, the gambler gets back twice what he bets on the right color. These
are fair odds if red and black are equally probable.
We consider two alternative betting schemes:
1. If we bet sequentially, we can calculate the conditional probability
of the next card and bet proportionally. Thus, we should bet ( 1
2, 1
2)
on (red, black) for the ﬁrst card, ( 26
51, 25
51) for the second card if the
ﬁrst card is black, and so on.
2. Alternatively, we can bet on the entire sequence of 52 cards at once.
There are

52
26

possible sequences of 26 red and 26 black cards, all
of them equally likely. Thus, proportional betting implies that we
put 1/

52
26

of our money on each of these sequences and let each
bet “ride.”
We will argue that these procedures are equivalent. For example, half
the sequences of 52 cards start with red, and so the proportion of money
bet on sequences that start with red in scheme 2 is also one-half, agreeing
with the proportion used in the ﬁrst scheme. In general, we can verify that
betting 1/

52
26

of the money on each of the possible outcomes will at each


## PDF page 194

168
GAMBLING AND DATA COMPRESSION
stage give bets that are proportional to the probability of red and black
at that stage. Since we bet 1/

52
26

of the wealth on each possible output
sequence, and a bet on a sequence increases wealth by a factor of 252 on
the sequence observed and 0 on all the others, the resulting wealth is
S∗
52 = 252

52
26
 = 9.08.
(6.39)
Rather interestingly, the return does not depend on the actual sequence.
This is like the AEP in that the return is the same for all sequences. All
sequences are typical in this sense.
6.4
THE ENTROPY OF ENGLISH
An important example of an information source is English text. It is
not immediately obvious whether English is a stationary ergodic process.
Probably not! Nonetheless, we will be interested in the entropy rate of
English. We discuss various stochastic approximations to English. As we
increase the complexity of the model, we can generate text that looks like
English. The stochastic models can be used to compress English text. The
better the stochastic approximation, the better the compression.
For the purposes of discussion, we assume that the alphabet of English
consists of 26 letters and the space symbol. We therefore ignore punctua-
tion and the difference between upper- and lowercase letters. We construct
models for English using empirical distributions collected from samples
of text. The frequency of letters in English is far from uniform. The most
common letter, E, has a frequency of about 13%, and the least common
letters, Q and Z, occur with a frequency of about 0.1%. The letter E is
so common that it is rare to ﬁnd a sentence of any length that does not
contain the letter. [A surprising exception to this is the 267-page novel,
Gadsby, by Ernest Vincent Wright (Lightyear Press, Boston, 1997; orig-
inal publication in 1939), in which the author deliberately makes no use
of the letter E.]
The frequency of pairs of letters is also far from uniform. For example,
the letter Q is always followed by a U. The most frequent pair is TH,
which occurs normally with a frequency of about 3.7%. We can use
the frequency of the pairs to estimate the probability that a letter fol-
lows any other letter. Proceeding this way, we can also estimate higher-
order conditional probabilities and build more complex models for the
language. However, we soon run out of data. For example, to build
a third-order Markov approximation, we must estimate the values of


## PDF page 195

6.4
THE ENTROPY OF ENGLISH
169
p(xi|xi−1, xi−2, xi−3). There are 274 = 531, 441 entries in this table, and
we would need to process millions of letters to make accurate estimates
of these probabilities.
The conditional probability estimates can be used to generate random
samples of letters drawn according to these distributions (using a random
number generator). But there is a simpler method to simulate randomness
using a sample of text (a book, say). For example, to construct the second-
order model, open the book at random and choose a letter at random on
the page. This will be the ﬁrst letter. For the next letter, again open the
book at random and starting at a random point, read until the ﬁrst letter is
encountered again. Then take the letter after that as the second letter. We
repeat this process by opening to another page, searching for the second
letter, and taking the letter after that as the third letter. Proceeding this
way, we can generate text that simulates the second-order statistics of the
English text.
Here are some examples of Markov approximations to English from
Shannon’s original paper [472]:
1. Zero-order approximation. (The symbols are independent and equi-
probable.)
XFOML RXKHRJFFJUJ ZLPWCFWKCYJ
FFJEYVKCQSGXYD QPAAMKBZAACIBZLHJQD
2. First-order approximation. (The symbols are independent. The fre-
quency of letters matches English text.)
OCRO HLI RGWR NMIELWIS EU LL NBNESEBYA TH EEI
ALHENHTTPA OOBTTVA NAH BRL
3. Second-order approximation. (The frequency of pairs of letters
matches English text.)
ON IE ANTSOUTINYS ARE T INCTORE ST BE S DEAMY
ACHIN D ILONASIVE TUCOOWE AT TEASONARE FUSO
TIZIN ANDY TOBE SEACE CTISBE
4. Third-order approximation. (The frequency of triplets of letters
matches English text.)
IN NO IST LAT WHEY CRATICT FROURE BERS GROCID
PONDENOME OF DEMONSTURES OF THE REPTAGIN IS
REGOACTIONA OF CRE


## PDF page 196

170
GAMBLING AND DATA COMPRESSION
5. Fourth-order approximation. (The frequency of quadruplets of let-
ters matches English text. Each letter depends on the previous three
letters. This sentence is from Lucky’s book, Silicon Dreams [366].)
THE GENERATED JOB PROVIDUAL BETTER TRAND THE DISPLAYED
CODE, ABOVERY UPONDULTS WELL THE CODERST IN THESTICAL
IT DO HOCK BOTHE MERG. (INSTATES CONS ERATION. NEVER
ANY OF PUBLE AND TO THEORY. EVENTIAL CALLEGAND TO ELAST
BENERATED IN WITH PIES AS IS WITH THE )
Instead of continuing with the letter models, we jump to word
models.
6. First-order word model. (The words are chosen independently but
with frequencies as in English.)
REPRESENTING AND SPEEDILY IS AN GOOD APT OR COME CAN
DIFFERENT NATURAL HERE HE THE A IN CAME THE TO OF TO
EXPERT GRAY COME TO FURNISHES THE LINE MESSAGE HAD BE
THESE.
7. Second-order word model. (The word transition probabilities match
English text.)
THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER
THAT THE CHARACTER OF THIS POINT IS THEREFORE ANOTHER
METHOD FOR THE LETTERS THAT THE TIME OF WHO EVER TOLD
THE PROBLEM FOR AN UNEXPECTED
The approximations get closer and closer to resembling English. For
example, long phrases of the last approximation could easily have occurred
in a real English sentence. It appears that we could get a very good approx-
imation by using a more complex model. These approximations could be
used to estimate the entropy of English. For example, the entropy of the
zeroth-order model is log 27 = 4.76 bits per letter. As we increase the
complexity of the model, we capture more of the structure of English,
and the conditional uncertainty of the next letter is reduced. The ﬁrst-
order model gives an estimate of the entropy of 4.03 bits per letter, while
the fourth-order model gives an estimate of 2.8 bits per letter. But even
the fourth-order model does not capture all the structure of English. In
Section 6.6 we describe alternative methods for estimating the entropy of
English.
The distribution of English is useful in decoding encrypted English text.
For example, a simple substitution cipher (where each letter is replaced


## PDF page 197

6.5
DATA COMPRESSION AND GAMBLING
171
by some other letter) can be solved by looking for the most frequent letter
and guessing that it is the substitute for E, and so on. The redundancy in
English can be used to ﬁll in some of the missing letters after the other
letters are decrypted: for example,
TH R
S NLY N W Y T F LL N TH V W LS N TH S S NT NC .
Some of the inspiration for Shannon’s original work on information
theory came out of his work in cryptography during World War II. The
mathematical theory of cryptography and its relationship to the entropy
of language is developed in Shannon [481].
Stochastic models of language also play a key role in some speech
recognition systems. A commonly used model is the trigram (second-order
Markov) word model, which estimates the probability of the next word
given the preceding two words. The information from the speech signal
is combined with the model to produce an estimate of the most likely
word that could have produced the observed speech. Random models do
surprisingly well in speech recognition, even when they do not explicitly
incorporate the complex rules of grammar that govern natural languages
such as English.
We can apply the techniques of this section to estimate the entropy rate
of other information sources, such as speech and images. A fascinating
nontechnical introduction to these issues may be found in the book by
Lucky [366].
6.5
DATA COMPRESSION AND GAMBLING
We now show a direct connection between gambling and data compres-
sion, by showing that a good gambler is also a good data compressor. Any
sequence on which a gambler makes a large amount of money is also a
sequence that can be compressed by a large factor. The idea of using
the gambler as a data compressor is based on the fact that the gambler’s
bets can be considered to be his estimate of the probability distribution
of the data. A good gambler will make a good estimate of the probability
distribution. We can use this estimate of the distribution to do arithmetic
coding (Section 13.3). This is the essential idea of the scheme described
below.
We assume that the gambler has a mechanically identical twin, who
will be used for the data decompression. The identical twin will place the
same bets on possible sequences of outcomes as the original gambler (and
will therefore make the same amount of money). The cumulative amount


## PDF page 198

172
GAMBLING AND DATA COMPRESSION
of money that the gambler would have made on all sequences that are
lexicographically less than the given sequence will be used as a code
for the sequence. The decoder will use the identical twin to gamble on
all sequences, and look for the sequence for which the same cumulative
amount of money is made. This sequence will be chosen as the decoded
sequence.
Let X1, X2, . . . , Xn be a sequence of random variables that we wish
to compress. Without loss of generality, we will assume that the random
variables are binary. Gambling on this sequence will be deﬁned by a
sequence of bets
b(xk+1 | x1, x2, . . . , xk) ≥0,

xk+1
b(xk+1 | x1, x2, . . . , xk) = 1,
(6.40)
where b(xk+1 | x1, x2, . . . , xk) is the proportion of money bet at time k on
the event that Xk+1 = xk+1 given the observed past x1, x2, . . . , xk. Bets
are paid at uniform odds (2-for-1). Thus, the wealth Sn at the end of the
sequence is given by
Sn = 2n
n

k=1
b(xk | x1, . . . , xk−1)
(6.41)
= 2nb(x1, x2, . . . , xn),
(6.42)
where
b(x1, x2, . . . , xn) =
n

k=1
b(xk|xk−1, . . . , x1).
(6.43)
So sequential gambling can also be considered as an assignment of proba-
bilities (or bets) b(x1, x2, . . . , xn) ≥0, 
x1,...,xn b(x1, . . . , xn) = 1, on the
2n possible sequences.
This gambling elicits both an estimate of the true probability of the text
sequence ( ˆp(x1, . . . , xn) = Sn/2n) as well as an estimate of the entropy
 ˆH = −1
n log ˆp

of the text from which the sequence was drawn. We now
wish to show that high values of wealth Sn lead to high data compression.
Speciﬁcally, we argue that if the text in question results in wealth Sn,
then log Sn bits can be saved in a naturally associated deterministic data
compression scheme. We further assert that if the gambling is log optimal,
the data compression achieves the Shannon limit H.


## PDF page 199

6.6
GAMBLING ESTIMATE OF THE ENTROPY OF ENGLISH
173
Consider the following data compression algorithm that maps the
text x = x1x2 · · · xn ∈{0, 1}n into a code sequences c1c2 · · · ck, ci ∈
{0, 1}. Both the compressor and the decompressor know n. Let
the
2n
text
sequences
be
arranged
in
lexicographical
order:
for
example, 0100101 < 0101101. The encoder observes the sequence
xn = (x1, x2, . . . , xn). He then calculates what his wealth Sn(x
′(n))
would
have
been
on
all
sequences
x
′(n) ≤x(n)
and
calculates
F(x(n)) = 
x′(n)≤x(n) 2−nSn(x
′(n)). Clearly, F(x(n)) ∈[0, 1]. Let k =
⌈n −log Sn(x(n))⌉. Now express F(x(n)) as a binary decimal to k-place
accuracy: ⌊F(x(n))⌋= .c1c2 · · · ck. The sequence c(k) = (c1, c2, . . . , ck)
is transmitted to the decoder.
The decoder twin can calculate the precise value S(x
′(n)) associated
with each of the 2n sequences x
′(n). He thus knows the cumulative sum
of 2−nS(x
′(n)) up through any sequence x(n). He tediously calculates
this sum until it ﬁrst exceeds .c(k). The ﬁrst sequence x(n) such that
the cumulative sum falls in the interval [.c1 · · · ck, .c1 . . . ck + (1/2)k] is
deﬁned uniquely, and the size of S(x(n))/2n guarantees that this sequence
will be precisely the encoded x(n).
Thus, the twin uniquely recovers x(n). The number of bits required
is
k = ⌈n −log S(x(n))⌉.
The
number
of
bits
saved
is
n −k =
⌊log S(x(n))⌋. For proportional gambling, S(x(n)) = 2np(x(n)). Thus,
the expected number of bits is Ek =  p(x(n))⌈−log p(x(n))⌉≤
H(X1, . . . , Xn) + 1.
We see that if the betting operation is deterministic and is known
both to the encoder and the decoder, the number of bits necessary to
encode x1, . . . , xn is less than n −log Sn + 1. Moreover, if p(x) is known,
and if proportional gambling is used, the description length expected is
E(n −log Sn) ≤H(X1, . . . , Xn) + 1. Thus, the gambling results corre-
spond precisely to the data compression that would have been achieved
by the given human encoder–decoder identical twin pair.
The data compression scheme using a gambler is similar to the idea
of arithmetic coding (Section 13.3) using a distribution b(x1, x2, . . . , xn)
rather than the true distribution. The procedure above brings out the duality
between gambling and data compression. Both involve estimation of the
true distribution. The better the estimate, the greater the growth rate of
the gambler’s wealth and the better the data compression.
6.6
GAMBLING ESTIMATE OF THE ENTROPY OF ENGLISH
We now estimate the entropy rate for English using a human gambler to
estimate probabilities. We assume that English consists of 27 characters


## PDF page 200

174
GAMBLING AND DATA COMPRESSION
(26 letters and a space symbol). We therefore ignore punctuation and case
of letters. Two different approaches have been proposed to estimate the
entropy of English.
1. Shannon guessing game.
In this approach the human subject is
given a sample of English text and asked to guess the next letter.
An optimal subject will estimate the probabilities of the next letter
and guess the most probable letter ﬁrst, then the second most prob-
able letter next, and so on. The experimenter records the number of
guesses required to guess the next letter. The subject proceeds this
way through a fairly large sample of text. We can then calculate the
empirical frequency distribution of the number of guesses required
to guess the next letter. Many of the letters will require only one
guess; but a large number of guesses will usually be needed at the
beginning of words or sentences.
Now let us assume that the subject can be modeled as a computer
making a deterministic choice of guesses given the past text. Then
if we have the same machine and the sequence of guess numbers,
we can reconstruct the English text. Just let the machine run, and if
the number of guesses at any position is k, choose the kth guess of
the machine as the next letter. Hence the amount of information in
the sequence of guess numbers is the same as in the English text.
The entropy of the guess sequence is the entropy of English text. We
can bound the entropy of the guess sequence by assuming that the
samples are independent. Hence, the entropy of the guess sequence
is bounded above by the entropy of the histogram in the experiment.
The experiment was conducted in 1950 by Shannon [482], who
obtained a value of 1.3 bits per symbol for the entropy of English.
2. Gambling estimate. In this approach we let a human subject gamble
on the next letter in a sample of English text. This allows ﬁner
gradations of judgment than does guessing. As in the case of a horse
race, the optimal bet is proportional to the conditional probability
of the next letter. The payoff is 27-for-1 on the correct letter.
Since sequential betting is equivalent to betting on the entire
sequence, we can write the payoff after n letters as
Sn = (27)nb(X1, X2, . . . , Xn).
(6.44)
Thus, after n rounds of betting, the expected log wealth satisﬁes
E 1
n log Sn = log 27 + 1
nE log b(X1, X2, . . . , Xn)
(6.45)


