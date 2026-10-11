# Argumentation Schemes (chapter)

Source ID: A01
Authors: Fabrizio Macagno; Douglas Walton; Chris Reed
Original attachment: Argumentation Schemes, Douglas.pdf
Identity: Chapter 11; printed pp. 517–574. Publication container/year not established from the supplied excerpt. Not the 2008 Cambridge monograph.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 1

11
Argumentation Schemes
Fabrizio Macagno, Douglas Walton, Chris Reed
abstract.
The purpose of this chapter is threefold: 1) to describe the
schemes, showing how they evolved and how they have been classiﬁed
in the traditional and the modern theories; 2) to propose a method for
classifying them based on ancient and modern developments; and 3) to
outline and show how schemes can be used to describe and analyze or
produce real arguments. To this purpose, we will build on the traditional
distinctions for building a dichotomic classiﬁcations of schemes, and we
will advance a modular approach to argument analysis, in which diﬀer-
ent argumentation schemes are combined together in order to represent
each step of reasoning on which a complex argument relies. Finally, we
will show how schemes are applied to formal systems, focusing on their
applications to Artiﬁcial Intelligence, AI & Law, argument mining, and
formal ontologies.
1
Introduction
The purpose of this chapter is threefold: 1) to describe the schemes, showing
how they evolved and how they have been classiﬁed in the traditional and
the modern theories; 2) to propose a method for classifying them based on
ancient and modern developments; and 3) to outline and show how schemes
are interrelated and can be organized in a modular way to describe natural
arguments or produce complex arguments. Historically, the schemes evolved
from the Aristotelian topics, the so-called places to ﬁnd arguments. But looking
over the descriptions Aristotle presented of them in the Topics, for the most
part they do not appear to very much resemble the argumentation schemes
in the contemporary list of Walton, Reed and Macagno [Walton et al., 2008].
Of course there are exceptions, such as the topic for argument from analogy
described in Aristotle, which is recognizable as standing for the same kind of
argument as the current scheme for argument from analogy, even though the
detailed description of it is quite diﬀerent.
Argumentation schemes are instruments for argumentation, involving the
activity of critically evaluating a viewpoint and the reasons given in its support.
For this reason, every scheme has a corresponding set of critical questions,
representing its defeasibility conditions and the possible weak points that the
interlocutor can use to question the argument and evaluate its strength. A
critic who has no counterarguments ready to hand can search through the list
of critical questions matching the argument he is confronted with in order to
look for clues on how the argument can be attacked that might suggest sources


## PDF page 2

518
Fabrizio Macagno, Douglas Walton, Chris Reed
of evidence that could be used to build up a whole line of argumentation that
furnish a way of refuting the argument.
The fundamental challenge that a theory of argumentation schemes needs
to face is the problem of ﬁnding a useful and sound classiﬁcation system. The
schemes need to be usable, easily identiﬁable, and at the same time they need
to allow the user to detect the most speciﬁc pattern of argument that can ﬁt
the text or that can be employed for producing an argument suitable to the
circumstances and the purpose. In any classiﬁcation system, entities can be
classiﬁed in many diﬀerent ways, depending on the purpose of the classiﬁcation.
The purpose of the classiﬁcation system will determine the criteria for classi-
ﬁcation that are adopted in that system. For example, a much more detailed
classiﬁcation of animals may be useful in biology than the kind of classiﬁcation
that might be useful for law, or for classifying animals as they are spoken and
written about in everyday conversational English. We need to begin by specify-
ing the purpose of the classiﬁcation, so that some guidance can be given on how
to identify the criteria used in the classiﬁcation system. From this perspective
it is useful to examine how the study of argumentation schemes evolved.
2
Introducing argumentation schemes
Argumentation schemes represent forms of argument that are widely used in
everyday conversational argumentation, and in other contexts such as legal
and scientiﬁc argumentation. But for the most part these arguments are not
adequately modeled by deductive forms of reasoning of the kind familiar in
classical logic or as statistical inferences based on the standard Bayesian ac-
count of probability. They represent the premise-conclusion structure of an
argument, and they are defeasible. Their defeasibility conditions are shown as
a set of critical questions, dialectical instruments to help begin the procedure
of testing the strength and acceptability of an argument by weighing the pro
and con arguments.
2.1
Nature of the schemes
Argumentation schemes are stereotypical patterns of inference, combining sem-
anticontological relations with types of reasoning and logical axioms and repre-
senting the abstract structure of the most common types of natural arguments
[Macagno and Walton, 2015]. The argumentation schemes provided in [Wal-
ton et al., 2008] describe the patterns of the most typical arguments, without
drawing distinctions between material relations (namely relations between con-
cepts expressed by the warrant of an argument), types of reasoning (such as
induction, deduction, abduction), and logical rules of inference characterizing
the various types of reasoning (such as modus ponens, modus tollens, etc.).
For this reason, argumentation schemes fall into distinct patterns of reasoning
such as abductive, analogical, or inductive ones, and ones from classiﬁcation or
cause to eﬀect.
In order to design a system for classifying the schemes, it is useful to under-
stand their limits, and investigate how the dimensions of an argument (material


## PDF page 3

Argumentation Schemes
519
relation and logical form) are merged. For example, consider argument from
cause to eﬀect [Walton et al., 2008, p.328]:
Table 1. Argument from cause to eﬀect
Major premise
Generally, if A occurs, then B will (might) occur.
Minor premise
In this case, A occurs (might occur).
Conclusion
Therefore, in this case B will (might) occur).
This argumentation scheme is based on a defeasible modus ponens scheme
[Verheij, 2003a] which is combined with a semantic causal relation between
two events. The material (semantic) relation is merged with the logical one.
However, this combination represents only one of the possible types of infer-
ences that can be drawn from the same semantic-ontological connection. The
actual relationship between the material and the logical relation is much more
complex. For example, we consider the classic Aristotelian causal link between
having fever and breathing fast, and see how this cause-eﬀect relation can be
used to draw a conclusion based on diﬀerent logical rules ([Macagno and Wal-
ton, 2015]; [Macagno, 2015]):
1. He had fever. (Fever causes breathing fast). Therefore, he (must have)
breathed fast.
2. He did not breathe fast. (Fever causes breathing fast). Therefore, he had
no fever.
3. He is breathing fast. (Fever causes breathing fast). Therefore, he might
have fever.
4. He has no fever. (Fever causes breathing fast). Therefore, he may be not
breathing fast.
5. You may have fever. When I had fever, I was breathing fast, and you are
breathing fast.
Cases (1) and (2) proceed logically from defeasible deductive axioms, i.e.
the defeasible modus ponens (in 1), and the defeasible modus tollens (in 2).
Cases 3 and 4 proceed from abductive reasoning. In (3) the conclusion is drawn
by aﬃrming the consequent, while in (4) the denial of the antecedent can be
rephrased by contraposition as not breathing fast is caused by having no fever,
leading to a conclusion drawn abductively [Walton et al., 2008, pp.169173]. In
(5) the conclusion is based on an inductive generalization from one single case.
Schemes represent only the prototypical matching between semantic rela-
tions and logical rules (types of reasoning and axioms).
This matching is,
however, only the most common one. The material and the logical relations
can combine in several diﬀerent ways. Hence this distinction needs to be taken
into account order to classify the schemes.


## PDF page 4

520
Fabrizio Macagno, Douglas Walton, Chris Reed
2.2
Why schemes are important
Critics often ask how these schemes can be justiﬁed, given that they resisted
analysis as deductive or inductive forms of argument of the kind recognized as
valid in the dominant 20th-century logic tradition [Walton and Sartor, 2013].
Schemes are becoming extremely important for practical reasons. First, ar-
gumentation schemes are instruments for analyzing and recognizing natural
arguments occurring in ordinary and specialized discourse. For example, argu-
ments from political discourses have been analyzed using the schemes, and the
argumentative proﬁles of the candidates has been brought to light considering
their preferences of the types of arguments used (Hansen & Walton, 2013).
Thousands of real examples of these forms of argument have been analyzed in
the argumentation literature, such as the considerable literature on fallacies,
with the aid of tools like argument mapping ([Reed et al., 2007][Rowe et al.,
2006]). On this basis, the structure, use, and importance of schemes for argu-
mentation studies has been justiﬁed inductively. This method consists in the
following steps:
1. The structure of a scheme is outlined considering the literature on the
topic.
2. A signiﬁcant mass of examples of arguments is analyzed using the scheme,
adapting and modifying the scheme so that it can best describe the spe-
ciﬁc natural arguments.
3. It is shown that the form of argument represented by the scheme under
analysis is signiﬁcantly important for the study of argumentation as it
occurs in natural language discourse (and other specialized contexts such
as legal discourse)
4. Empirical justiﬁcation is given that this form of argument needs to be
recognized as a basic scheme for argumentation.
Second, schemes are instruments that can be used for the purpose of teaching
critical thinking. Informal logic is a ﬁeld is known for having grown from its ori-
gins in textbooks that departed from formal logic and instead proceeded on the
basis of analyzing numerous examples of arguments from ordinary discourse,
such as those taken from magazines and newspapers. There is an abundance of
such textbooks full of examples of everyday arguments related to topics such
as the informal fallacy of appeal to authority, false cause, and so forth. During
its growth stage and more theoretical ﬂowering, the ﬁeld followed this trend
by stressing the importance of analyzing real arguments on the hoof. For ex-
ample, the handbook Informal Logic [Walton, 1989] was based on hundred 150
key examples, many of them illustrating forms of argument now identiﬁed with
argumentation schemes, including personal attack, uses and abuses of expert
opinion, arguments from analogy arguments from correlation to cause, and so
forth. These textbooks and continued academic writings on informal logic con-
tained a very large number of such examples, often analyzed in minute detail,


## PDF page 5

Argumentation Schemes
521
and argumentation schemes, such as argument from expert opinion, are tested
against the real examples, to discuss the respects in which the abstract scheme
ﬁts or does not ﬁt the vagaries of the real-life example. This body of data con-
ﬁrms that certain types of arguments, mainly the ones subsequently identiﬁed
as argumentation schemes, are not only extremely common, but are also highly
inﬂuential in daily practices of argumentation.
Third, schemes can be used in education for both teaching students how to
argue and learning through argumentation ([Erduran and Jimenez-Aleixandre,
2007]; [Erduran and Jim´enez Aleixandre, 2012]; [Rapanta and Walton, 2016]).
The interest in argumentation and the patterns for representing natural argu-
ments is growing [Rapanta et al., 2013]. The argumentation schemes illustrated
in ([Walton, 1995]; [Walton et al., 2008]) have been applied to science educa-
tion in order to represent students arguments and improve the quality thereof
([Rapanta and Macagno, 2016]), retrieve the implicit premises, and assess and
rebut their reasoning in a systematic fashion ([Macagno and Konstantinidou,
2013]), or to assess the quality of argumentation ([Duschl et al., 1999]; [Ozdem
et al., 2013]). However, a crucial problem arising out of the use of schemes in
education is their diﬀerentiation ([Kim et al., 2010]; [Nussbaum and Edwards,
2011]). Students often fail to understand the diﬀerences between various types
of arguments, and the recent developments in education tend to conﬂate the
schemes instead of providing criteria for classifying or distinguishing between
them.
Fourth, schemes have now been recognized as important for argument min-
ing, and it has also been recognized that there are too many schemes for handy
use [Mochales Palau and Moens, 2009]; [Mochales Palau and Moens, 2011]).
Conﬁguring the relationships between clusters of them, and the internal struc-
ture of each cluster, would help in the research eﬀorts to apply the schemes
as working tools to a broader range of problems as the ﬁeld of computational
linguistics has moved forward.
From a theoretical point of view, schemes ﬁt into current formal argu-
mentation models such as ASPIC+ ([Prakken et al., 2015]), DefLog ([Ver-
heij, 2003a]) and the Carneades Argumentation System ([Walton and Gordon,
2012]). Among the basic schemes presented in the list of 60+ schemes in chap-
ter 9 of ([Walton et al., 2008]) are argument from expert opinion, argument
from sign, argument from example, argument from commitment, argument
from position to know, argument from lack of knowledge, practical reasoning
(argument from goal to action), argument from cause to eﬀect, the sunk costs
argument, argument from analogy, ad hominem argument, and the slippery
slope argument. These schemes are at this point well enough recognized in the
argumentation literature that no detailed account of them needs to be given
in this chapter, except for the ones that we will focus on to illustrate general
characteristics of schemes discussed in detail in the chapter.
Moreover, Walton and Sartor ([Walton and Sartor, 2013]) have shown that
the basic defeasible schemes can be justiﬁed by the teleological argument. Ac-


## PDF page 6

522
Fabrizio Macagno, Douglas Walton, Chris Reed
cording to this reasoning, the use of a speciﬁc scheme is warranted by the fact
that it can serve an agents goals better than nothing, and better than other
alternative schemata the agent has at its disposal. This kind of justiﬁcation
of basic schemes is essentially a practical one saying that these schemes, even
at their current state of development, are proving to be useful in such areas
as artiﬁcial intelligence and multiagent computing. Defeasible schemes allow
agents to arrive at a presumptive conclusion on how to proceed in a situation
where continuing to collect evidence may cause delay, taking time and cost
money.
This form of justiﬁcation of schemes applies both to goals of epistemic cogni-
tion (getting to the truth of a matter) and goals of practical cognition (making
the best choice in given circumstances). The importance of the schemes has
also been acknowledged in the history of dialectics. The forms of argument,
their critical and defeasible dimension, and their structure was long ago ac-
knowledged in the earlier concerns of the Sophists, who pointed out forms of
argument useful for persuasion and deliberation ([Schiappa, 1999]; [Tindale,
2010]). In the Topics [Aristotle, 1991b]and in the Rhetoric [Aristotle, 1991a],
Aristotle set out a list of topics that, providing the abstract and general hypo-
thetical premises of dialectical syllogisms, can be considered to be the prede-
cessors of the argument patterns developed in modern times ([Macagno et al.,
2014]; [Rubinelli, 2009]; [Macagno et al., 2014]).
The tradition of the topics was continued through the Middle Ages, with
various theories aimed at providing a classiﬁcation and an analysis of the na-
ture of the schemes [Bird, 1962]; [Gabbay and Woods, 2008]; [Green-Pedersen,
1984]; [Green-Pedersen, 1987]; [Stump, 1982]; [Stump, 1989]). Study of the
kinds of schemes that are the focus of this chapter was eclipsed during the
Enlightenment, as the dominant view became ﬁrmly entrenched that the only
forms of reasoning that can be identiﬁed with rational thinking are those of de-
ductive logic, and inductive reasoning of the kind used in games of chance. But
the study of these schemes made a comeback in the 20th century at the begin-
ning of, and after the rise of argumentation studies as a respectable discipline,
once the basic schemes were identiﬁed by Hastings ([Hastings, 1963]), Perelman
and Olbrechts-Tyteca ([Perelman and Olbrechts-Tyteca, 1969]), Kienpointner
([Kienpointner, 1992]), Walton ([Walton, 1995]), Grennan ([Grennan, 1997]),
and Walton, Reed and Macagno ([Walton et al., 2008]). From that point on-
wards, the study of schemes has been recognized as important for building com-
putational models of argumentation, and especially for applying these models
to argumentation in natural language discourse.
2.3
Classiﬁcation of the schemes: how to proceed
In this chapter, it is shown how the complex project of classifying schemes needs
to proceed by matching a top-down approach with a bottom-up approach,
and in particular that this bottom-up approach needs to begin by studying
relationships between clusters of nested schemes. From a top-down approach,
dichotomic criteria of classiﬁcation need to be found, allowing the user to decide


## PDF page 7

Argumentation Schemes
523
the scheme needed, both by direct identiﬁcation and by exclusion. For this
purpose, an overview of the existing classiﬁcation systems developed in the
tradition and in the recent theories can provide useful criteria. From a bottom-
up approach, relationships within groups of schemes need to be studied, and
then how one group ﬁts with another can be studied. Walton [Walton, 2012]
took a bottom-up approach that began with some examples at the ground
level of cases where two schemes seem to apply to the same real example of an
argument found in a text, leading to a diﬃculty of determining which scheme
ﬁts the argument. Working from there, we identify clusters of schemes that
ﬁt together, and then at the next step, we examine how these clusters can be
ﬁtted together. Once clusters of schemes are ﬁtted together into larger groups,
we can gradually learn how they ﬁt into an overarching system.
3
The topics in the dialectical and rhetorical tradition
Argumentation schemes describe patterns from which speciﬁc arguments can
be drawn. In this sense, they can be seen as the modern development of the
traditional concept of topos, the conditional expressing a generic principle from
which some of the speciﬁc premises warranting the conclusion in an argument
can be drawn. The purpose of this section is to show how the ancient account
of topoi and loci can be considered as the ground and the predecessor of the
modern theory of schemes.
3.1
Aristotle
The idea of providing general principles of inference from which various argu-
ments can be drawn was the ground of Aristotles Topics and Rhetoric. The
Aristotelian topoi can be conceived as principles [De Pater, 1965, pp.150–159]
having often the form of If P, then Q. The various semantic (material) relations
between P and Q, or the nature of the things which the terms of the argument
represent or stand for [Green-Pedersen, 1987, p.413], constitute the diﬀerences
between the various topoi. For example, P and Q can be related by a relation
of genus-species, deﬁniens-deﬁniendum, contraries, similarity, etc. The func-
tion of the topoi in the mechanism of argument production can be explained
as follows [Slomkowski, 1997, p.45]:
The enthymemes seem to be instances of topoi; or, expressed diﬀerently,
enthymemes are arguments which are warranted by the principle ex-
pressed in the topos.
Thus hypothetical syllogism would fall under a
topos insofar as it falls under its major premiss in which the essence of
the hypothetical syllogism is expressed.
Topoi can be considered as the external general rules of reasoning of an
enthymeme, or the genera of the major premises of dialectical and rhetorical
syllogisms. Topoi can work as rules, namely as the principle of inference guar-
anteeing the passage from an enthymematic premise to the conclusion. For
example, we consider the following enthymeme [Slomkowski, 1997, p.51]:


## PDF page 8

524
Fabrizio Macagno, Douglas Walton, Chris Reed
Doing greater injustice is a greater evil.
From what is more A is more B, you may infer: A is B.
Doing injustice is an evil.
The topos can be also used as a general principle from which it is possible
to draw the speciﬁc premises of a hypothetical syllogism ([Bird, 1960]; [Bird,
1962]; [Macagno et al., 2014]). For example, the same argument mentioned
above can be completed by adding the major premise that is an instantiation
(an axiom-instance) of the topos from the more [Slomkowski, 1997, p.53] (Table
2):
Table 2. Topoi as general principles of inference
General principle
If being more A is more B, then A is B.
Speciﬁc instantiation of
the topos as a premise
If doing greater injustice (A) is a greater evil
(B), then doing injustice (A) is an evil (B).
Minor premise
Doing greater injustice (A) is a greater
evil (B).
Conclusion
Doing injustice (A) is an evil (B)
The aforementioned mechanism of speciﬁcation (or instantiation) of the topoi
brings to light a fundamental distinction that Aristotle draws between generic
topoi and the idia (the speciﬁc topics) [Rubinelli, 2009, pp.5970]. While generic
topoi are abstract and commonly shared conditionals under which speciﬁc
premises can be found, the speciﬁc topoi represent premises warranting the
conclusion ([De Pater, 1965, p.134]; [Stump, 1989, p.29]) that are accepted
within speciﬁc disciplines, such as ethics, law, or medicine. For example, we
consider the following speciﬁc topic [Lawson, 1885, p.262]:
Where a person does an act, he is presumed in so doing to have intended
that the natural and legal consequences of his act shall result.
In speciﬁc domains of knowledge, speciﬁc topoi can be listed as instruments
of invention, premises that can be used to construct arguments in support of
typical conclusions.
Generic topics can be considered as abstractions from the speciﬁc ones, or
more correctly, an abstraction from a large number of speciﬁc topics. They
provide classes of both necessary and defeasible inferences ([Bird, 1960];[Bird,
1962];[Christensen, 1988];[Drehe, 2011];[Stump, 2004]). In the ﬁrst class fall
some maxims setting out deﬁnitional properties of meta-semantic concepts, i.e.
concepts representing semantic relations between concepts, such as deﬁnition,
genus, and property. For example the locus from deﬁnition, which establishes
the convertibility between deﬁnition and deﬁniendum, represents also the essen-
tial logical characteristic that a predicate needs to have in order be considered
as a discourse signifying what a thing is. Other loci, such as the ones based


