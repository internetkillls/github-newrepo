# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 17

PREFACE TO THE
SECOND EDITION
In the years since the publication of the ﬁrst edition, there were many
aspects of the book that we wished to improve, to rearrange, or to expand,
but the constraints of reprinting would not allow us to make those changes
between printings. In the new edition, we now get a chance to make some
of these changes, to add problems, and to discuss some topics that we had
omitted from the ﬁrst edition.
The key changes include a reorganization of the chapters to make
the book easier to teach, and the addition of more than two hundred
new problems. We have added material on universal portfolios, universal
source coding, Gaussian feedback capacity, network information theory,
and developed the duality of data compression and channel capacity. A
new chapter has been added and many proofs have been simpliﬁed. We
have also updated the references and historical notes.
The material in this book can be taught in a two-quarter sequence. The
ﬁrst quarter might cover Chapters 1 to 9, which includes the asymptotic
equipartition property, data compression, and channel capacity, culminat-
ing in the capacity of the Gaussian channel. The second quarter could
cover the remaining chapters, including rate distortion, the method of
types, Kolmogorov complexity, network information theory, universal
source coding, and portfolio theory. If only one semester is available, we
would add rate distortion and a single lecture each on Kolmogorov com-
plexity and network information theory to the ﬁrst semester. A web site,
http://www.elementsoﬁnformationtheory.com, provides links to additional
material and solutions to selected problems.
In the years since the ﬁrst edition of the book, information theory
celebrated its 50th birthday (the 50th anniversary of Shannon’s original
paper that started the ﬁeld), and ideas from information theory have been
applied to many problems of science and technology, including bioin-
formatics, web search, wireless communication, video compression, and
xv


## PDF page 18

xvi
PREFACE TO THE SECOND EDITION
others. The list of applications is endless, but it is the elegance of the
fundamental mathematics that is still the key attraction of this area. We
hope that this book will give some insight into why we believe that this
is one of the most interesting areas at the intersection of mathematics,
physics, statistics, and engineering.
Tom Cover
Joy Thomas
Palo Alto, California
January 2006


## PDF page 19

PREFACE TO THE
FIRST EDITION
This is intended to be a simple and accessible book on information theory.
As Einstein said, “Everything should be made as simple as possible, but no
simpler.” Although we have not veriﬁed the quote (ﬁrst found in a fortune
cookie), this point of view drives our development throughout the book.
There are a few key ideas and techniques that, when mastered, make the
subject appear simple and provide great intuition on new questions.
This book has arisen from over ten years of lectures in a two-quarter
sequence of a senior and ﬁrst-year graduate-level course in information
theory, and is intended as an introduction to information theory for stu-
dents of communication theory, computer science, and statistics.
There are two points to be made about the simplicities inherent in infor-
mation theory. First, certain quantities like entropy and mutual information
arise as the answers to fundamental questions. For example, entropy is
the minimum descriptive complexity of a random variable, and mutual
information is the communication rate in the presence of noise. Also,
as we shall point out, mutual information corresponds to the increase in
the doubling rate of wealth given side information. Second, the answers
to information theoretic questions have a natural algebraic structure. For
example, there is a chain rule for entropies, and entropy and mutual infor-
mation are related. Thus the answers to problems in data compression
and communication admit extensive interpretation. We all know the feel-
ing that follows when one investigates a problem, goes through a large
amount of algebra, and ﬁnally investigates the answer to ﬁnd that the
entire problem is illuminated not by the analysis but by the inspection of
the answer. Perhaps the outstanding examples of this in physics are New-
ton’s laws and Schr¨odinger’s wave equation. Who could have foreseen the
awesome philosophical interpretations of Schr¨odinger’s wave equation?
In the text we often investigate properties of the answer before we look
at the question. For example, in Chapter 2, we deﬁne entropy, relative
entropy, and mutual information and study the relationships and a few
xvii


## PDF page 20

xviii
PREFACE TO THE FIRST EDITION
interpretations of them, showing how the answers ﬁt together in various
ways. Along the way we speculate on the meaning of the second law of
thermodynamics. Does entropy always increase? The answer is yes and
no. This is the sort of result that should please experts in the area but
might be overlooked as standard by the novice.
In fact, that brings up a point that often occurs in teaching. It is fun
to ﬁnd new proofs or slightly new results that no one else knows. When
one presents these ideas along with the established material in class, the
response is “sure, sure, sure.” But the excitement of teaching the material
is greatly enhanced. Thus we have derived great pleasure from investigat-
ing a number of new ideas in this textbook.
Examples of some of the new material in this text include the chapter
on the relationship of information theory to gambling, the work on the uni-
versality of the second law of thermodynamics in the context of Markov
chains, the joint typicality proofs of the channel capacity theorem, the
competitive optimality of Huffman codes, and the proof of Burg’s theorem
on maximum entropy spectral density estimation. Also, the chapter on
Kolmogorov complexity has no counterpart in other information theory
texts. We have also taken delight in relating Fisher information, mutual
information, the central limit theorem, and the Brunn–Minkowski and
entropy power inequalities. To our surprise, many of the classical results
on determinant inequalities are most easily proved using information the-
oretic inequalities.
Even though the ﬁeld of information theory has grown considerably
since Shannon’s original paper, we have strived to emphasize its coher-
ence. While it is clear that Shannon was motivated by problems in commu-
nication theory when he developed information theory, we treat informa-
tion theory as a ﬁeld of its own with applications to communication theory
and statistics. We were drawn to the ﬁeld of information theory from
backgrounds in communication theory, probability theory, and statistics,
because of the apparent impossibility of capturing the intangible concept
of information.
Since most of the results in the book are given as theorems and proofs,
we expect the elegance of the results to speak for themselves. In many
cases we actually describe the properties of the solutions before the prob-
lems. Again, the properties are interesting in themselves and provide a
natural rhythm for the proofs that follow.
One innovation in the presentation is our use of long chains of inequal-
ities with no intervening text followed immediately by the explanations.
By the time the reader comes to many of these proofs, we expect that he
or she will be able to follow most of these steps without any explanation
and will be able to pick out the needed explanations. These chains of


## PDF page 21

PREFACE TO THE FIRST EDITION
xix
inequalities serve as pop quizzes in which the reader can be reassured
of having the knowledge needed to prove some important theorems. The
natural ﬂow of these proofs is so compelling that it prompted us to ﬂout
one of the cardinal rules of technical writing; and the absence of verbiage
makes the logical necessity of the ideas evident and the key ideas per-
spicuous. We hope that by the end of the book the reader will share our
appreciation of the elegance, simplicity, and naturalness of information
theory.
Throughout the book we use the method of weakly typical sequences,
which has its origins in Shannon’s original 1948 work but was formally
developed in the early 1970s. The key idea here is the asymptotic equipar-
tition property, which can be roughly paraphrased as “Almost everything
is almost equally probable.”
Chapter 2 includes the basic algebraic relationships of entropy, relative
entropy, and mutual information. The asymptotic equipartition property
(AEP) is given central prominence in Chapter 3. This leads us to dis-
cuss the entropy rates of stochastic processes and data compression in
Chapters 4 and 5. A gambling sojourn is taken in Chapter 6, where the
duality of data compression and the growth rate of wealth is developed.
The sensational success of Kolmogorov complexity as an intellectual
foundation for information theory is explored in Chapter 14. Here we
replace the goal of ﬁnding a description that is good on the average with
the goal of ﬁnding the universally shortest description. There is indeed
a universal notion of the descriptive complexity of an object. Here also
the wonderful number  is investigated. This number, which is the binary
expansion of the probability that a Turing machine will halt, reveals many
of the secrets of mathematics.
Channel capacity is established in Chapter 7. The necessary material
on differential entropy is developed in Chapter 8, laying the groundwork
for the extension of previous capacity theorems to continuous noise chan-
nels. The capacity of the fundamental Gaussian channel is investigated in
Chapter 9.
The relationship between information theory and statistics, ﬁrst studied
by Kullback in the early 1950s and relatively neglected since, is developed
in Chapter 11. Rate distortion theory requires a little more background
than its noiseless data compression counterpart, which accounts for its
placement as late as Chapter 10 in the text.
The huge subject of network information theory, which is the study
of the simultaneously achievable ﬂows of information in the presence of
noise and interference, is developed in Chapter 15. Many new ideas come
into play in network information theory. The primary new ingredients are
interference and feedback. Chapter 16 considers the stock market, which is


## PDF page 22

xx
PREFACE TO THE FIRST EDITION
the generalization of the gambling processes considered in Chapter 6, and
shows again the close correspondence of information theory and gambling.
Chapter 17, on inequalities in information theory, gives us a chance to
recapitulate the interesting inequalities strewn throughout the book, put
them in a new framework, and then add some interesting new inequalities
on the entropy rates of randomly drawn subsets. The beautiful relationship
of the Brunn–Minkowski inequality for volumes of set sums, the entropy
power inequality for the effective variance of the sum of independent
random variables, and the Fisher information inequalities are made explicit
here.
We have made an attempt to keep the theory at a consistent level.
The mathematical level is a reasonably high one, probably the senior or
ﬁrst-year graduate level, with a background of at least one good semester
course in probability and a solid background in mathematics. We have,
however, been able to avoid the use of measure theory. Measure theory
comes up only brieﬂy in the proof of the AEP for ergodic processes in
Chapter 16. This ﬁts in with our belief that the fundamentals of infor-
mation theory are orthogonal to the techniques required to bring them to
their full generalization.
The essential vitamins are contained in Chapters 2, 3, 4, 5, 7, 8, 9,
11, 10, and 15. This subset of chapters can be read without essential
reference to the others and makes a good core of understanding. In our
opinion, Chapter 14 on Kolmogorov complexity is also essential for a deep
understanding of information theory. The rest, ranging from gambling to
inequalities, is part of the terrain illuminated by this coherent and beautiful
subject.
Every course has its ﬁrst lecture, in which a sneak preview and overview
of ideas is presented. Chapter 1 plays this role.
Tom Cover
Joy Thomas
Palo Alto, California
June 1990


## PDF page 23

ACKNOWLEDGMENTS
FOR THE SECOND EDITION
Since the appearance of the ﬁrst edition, we have been fortunate to receive
feedback, suggestions, and corrections from a large number of readers. It
would be impossible to thank everyone who has helped us in our efforts,
but we would like to list some of them. In particular, we would like
to thank all the faculty who taught courses based on this book and the
students who took those courses; it is through them that we learned to
look at the same material from a different perspective.
In particular, we would like to thank Andrew Barron, Alon Orlitsky,
T. S. Han, Raymond Yeung, Nam Phamdo, Franz Willems, and Marty
Cohn for their comments and suggestions. Over the years, students at
Stanford have provided ideas and inspirations for the changes—these
include George Gemelos, Navid Hassanpour, Young-Han Kim, Charles
Mathis, Styrmir Sigurjonsson, Jon Yard, Michael Baer, Mung Chiang,
Suhas Diggavi, Elza Erkip, Paul Fahn, Garud Iyengar, David Julian, Yian-
nis Kontoyiannis, Amos Lapidoth, Erik Ordentlich, Sandeep Pombra, Jim
Roche, Arak Sutivong, Joshua Sweetkind-Singer, and Assaf Zeevi. Denise
Murphy provided much support and help during the preparation of the
second edition.
Joy Thomas would like to acknowledge the support of colleagues
at IBM and Stratify who provided valuable comments and suggestions.
Particular thanks are due Peter Franaszek, C. S. Chang, Randy Nelson,
Ramesh Gopinath, Pandurang Nayak, John Lamping, Vineet Gupta, and
Ramana Venkata. In particular, many hours of dicussion with Brandon
Roy helped reﬁne some of the arguments in the book. Above all, Joy
would like to acknowledge that the second edition would not have been
possible without the support and encouragement of his wife, Priya, who
makes all things worthwhile.
Tom Cover would like to thank his students and his wife, Karen.
xxi


## PDF page 24



