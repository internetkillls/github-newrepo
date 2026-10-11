# Argumentation Schemes (chapter)

Source ID: A01
Authors: Fabrizio Macagno; Douglas Walton; Chris Reed
Original attachment: Argumentation Schemes, Douglas.pdf
Identity: Chapter 11; printed pp. 517–574. Publication container/year not established from the supplied excerpt. Not the 2008 Cambridge monograph.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 49

Argumentation Schemes
565
Figure 17. Snippet of Argumentation Scheme Ontology
In the ﬁrst stanza, the conclusion and premises concerning the knowledge
assertion (that the expert said something) and the ﬁeld expertise (that the
speaker is indeed an expert) are set up. In the second stanza, the remain-
ing premises (those captured as presumptions and exceptions) are added in,
covering credibility, backup evidence, consistency between experts and expert
reliability. The third stanza shows how one of these, consistency between ex-
perts, can be used to drive a stereotypical way of attacking this inference i.e.
the posing of a critical question (see [Reed and Walton, 2005] for the mechanics
of operationalizing critical questions in this way). The aim here is just to give a


## PDF page 50

566
Fabrizio Macagno, Douglas Walton, Chris Reed
ﬂavour of how all the important components of argumentation schemes struc-
ture, description and critical questions can be captured in a formal ontology.
The full ontology is available online at http://arg.tech/aif.owl, and is used by
many of the Argument Web online services.
Two beneﬁts of this approach are demonstrated in [Rahwan et al., 2011].
The ﬁrst is an economy in speciﬁcation, that allows more speciﬁc schemes to
be deﬁned in terms of minor additions to more general ones.
The second,
much more importantly, is that these structures support automated reasoning,
in three distinct ways. First, it becomes possible to reason across argument
structures, identifying, for example, transitivity of inferences, so that if X is
used to infer Y, and Y to infer Z, the dependence of X on Z can be inferred auto-
matically. Of course such reasoning is not at all unique to ontologically based
systems, but is a convenient side beneﬁt. An ontologically more interesting
way of performing automated reasoning is to perform automatic classiﬁcation.
This is where formal ontologies, and the reasoning systems constructed on top
of them, excel. Rahwan et al., exemplify this technique by showing how fear
appeal arguments are naturally classiﬁable as a subset of negative consequence
arguments. The third and ﬁnal way of performing automated reasoning is also
of use in designing and implementing dialogue systems. By virtue of hierarchi-
cal relationships between schemes that are represented in, or inferable from, the
ontology, it also becomes possible to infer appropriate critical questions that
might be asked of a given argument. Thus, for example, all of the critical ques-
tions of a superclass can be asked of an instance of a sub-class of argumentation
schemes. In these ways, formal representation of argumentation schemes in an
explicit ontology can contribute to the computational techniques for analysing,
processing and interacting with arguments.
11
Conclusions
Argumentation schemes represent the abstract structures of the most common
and stereotypical arguments used in everyday conversation and speciﬁc ﬁelds,
such as law, science and politics. They appear as a set of premises having an
abstract form with variables and constants, leading to an abstract conclusion.
They are abstract in the sense that they provide a form for structuring inferen-
tial relation between the premises and the conclusion. Some schemes are based
on the most abstract relations (classiﬁcation, cause, authority), while others
specify the most abstract premises including some further detail (negative con-
sequences; expert opinion ad populum argument) [Walton et al., 2008].
The abstract nature of the schemes allows the analyst to detect the structure
of natural arguments, and recognize patterns occurring in everyday reasoning.
This chapter has shown how they can be applied to real arguments in natural
language discourse, and in technical discourse as well, for that matter. In this
chapter it has been shown how these schemes, at their current state of develop-
ment can be used as tools to identify kinds of arguments in a text, and beyond
that how they can be an important part of argument evaluation. Throughout


## PDF page 51

Argumentation Schemes
567
the history of logic and rhetoric there has always been some uncertainty about
the role of the topics [Bird, 1962]. Some have seen them as forms of logical in-
ference that can be used to show that arguments are valid, where the term valid
is used in a wider sense that can include not only deductively valid arguments
but also defeasible arguments that have an identiﬁable structure as ﬁtting a
particular topic. Others have seen the topics of as having a search function that
can be used to ﬁnd arguments to prove a designated conclusion. The search
function is supposed to help an arguer select arguments that have premises
accepted by the audience to whom the argument is directed [Kienpointner and
Kindt, 1997].
Schemes can also be used for argument construction.
As we saw in this
chapter, an argumentation scheme is taken to have a warranting function that
enables an inference to be drawn from a set of premises to a conclusion. This
practical way of justifying schemes indicates their usefulness not only for ar-
gument evaluation, but also for argument construction, also called argument
invention in the long history of the subject tracing back to the Sophists and
Aristotle. An argument invention device would enable an arguer to search for
an argument that could be used to support a claim s/he wants to prove [Kien-
pointner, 1987]. When viewed in this way, topics can be seen to have a use as
components of argument construction function, for use in a system for ﬁnding
arguments. The schemes can be used as instruments for producing arguments,
allowing the user to decide the type of argument he considers the most ap-
plicable to his purpose, and then develop a speciﬁc line of reasoning from the
premises or evidential facts he has to the conclusion he needs to prove. In this
guise, the schemes are dialectical instruments for use in the task of argument
construction.
The advent of IBMs new Watson Debater tool [Aharoni et al., 2014] is a
leap forward for argument invention because it enables a user to quickly search
through a database such as Wikpedia and ﬁnd useful pro and con arguments
supporting or attacking a designated claim. Once this tool comes onto the
market, it will greatly stimulate research on argument invention in argumen-
tation studies. The Debater tool does not (so far) use argumentation schemes,
but there is a formal and computational argumentation system, the Carneades
Argumentation System (CAS)12. By inputting information into the CAS ﬁnd
arguments assistant, a user who has a database containing propositions record-
ing the commitments of the audience, the automated assistant constructs a
chain of argumentation where the conclusion of the chain is the proposition is
the goal proposition that the speaker wants to persuade the audience to accept,
called the arguers ultimate claim, or ultimate probandum, the proposition to
be proved, in the language of the ancient stasis theory [Walton and Gordon,
2012]. The argument assistant searches through the commitments of the audi-
ence and uses a repository of argumentation schemes in its knowledge base to
collect a set of arguments moving from these premises to the ultimate claim.
12https://carneades.github.io/ (Accessed on 10 May 2016)


## PDF page 52

568
Fabrizio Macagno, Douglas Walton, Chris Reed
If there are such arguments available the assistant gives that information, but
may suggest a partial way forward.
Argumentation schemes are instruments that can be used in diﬀerent ways to
many disciplines addressing the analysis of discourse in general, and reasoned
discourse in particular. The current research on schemes can improve notice-
ably the ﬁeld of application and make this tool crucial for a deeper analysis of
argumentative exchanges. To this purpose, argumentation schemes need ﬁrst to
be integrated within a theory of discourse interpretation. Schemes can be pow-
erful instruments for representing arguments and relations between sentences.
However, at present they presuppose an interpretation of discourse. This line
of research could show how schemes can represent interpretation, and how they
can be used to assess what interpretation is the best one [Macagno, 2012]. A
second challenge in this area is to link the theory of dialogue types and discourse
moves (utterances) to argumentation schemes [Macagno and Bigi, 2017]. By
showing how certain schemes are the most adequate to pursue speciﬁc dialogical
ends, it is possible to map not only a set of useful tools for argument produc-
tion, but also a set of presumptions for interpreting and classifying arguments
based on the type of dialogue.
Acknowledgments
Fabrizio Macagno would like to thank the Fundao para a Cincia e a Tecnologia for the
research grants no. IF/00945/2013, PTDC/IVC-HFC/1817/2014, and PTDC/MHC-
FIL/0521/2014.
Douglas Walton would like to thank the Social Sciences and Humanities Research
Council of Canada for Insight Grant 435-2012-0104.
BIBLIOGRAPHY
[Abaelardus, 1970] Petrus Abaelardus. Dialectica. Van Gorcum, Assen, 1970.
[Aharoni et al., 2014] Ehud Aharoni, Carlos Alzate, Roy Bar-Haim, Yonatan Bilu, Lena
Dankin, Iris Eiron, Daniel Hershcovich, and Shay Hummel. Claims on demand–an initial
demonstration of a system for automatic detection and polarity identiﬁcation of context
dependent claims in massive corpora. In COLING 2014, the 25th International Confer-
ence on Computational Linguistics: System Demonstrations, pages 6–9, 2014.
[Aleven, 1997] Vincent Aleven.
Teaching case-based argumentation through a model and
examples. PhD thesis, University of Pittsburgh, 1997.
[Aristotle, 1991a] Aristotle. Rhetoric. In Jonathan Barnes, editor, The complete works of
Aristotle, vol. I. Princeton University Press, Princeton, 1991.
[Aristotle, 1991b] Aristotle.
Topics.
In Jonathan Barnes, editor, The complete works of
Aristotle, vol. I. Princeton University Press, Princeton, 1991.
[Ashley, 1990] Kevin Ashley. Modeling Legal Argument: Reasoning with Cases and Hypo-
theticals. MIT Press, Cambridge, Mass., 1990.
[Atkinson et al., 2005] Katie Atkinson, Trevor Bench-Capon, and Peter McBurney. Arguing
about cases as practical reasoning. In Giovanni Sartor, editor, Proceedings of the 10th
international conference on Artiﬁcial intelligence and law, pages 35–44, New York, 2005.
ACM Press.
[Bench-Capon, 2003] Trevor Bench-Capon. Persuasion in practical argument using value-
based argumentation frameworks.
Journal of Logic and Computation, 13(3):429–448,
2003.


## PDF page 53

Argumentation Schemes
569
[Bex and Reed, 2011] Floris Bex and Christopher Reed.
Schemes of inference, conﬂict,
and preference in a computational model of argument. Studies in Logic, Grammar and
Rhetoric, 23(36):39–58, 2011.
[Bex et al., 2013] Floris Bex, John Lawrence, Mark Snaith, and Chris Reed. Implementing
the argument web. Communications of the ACM, 56(10):66–73, oct 2013.
[Bird, 1960] Otto Bird. The formalizing of the topics in mediaeval logic. Notre Dame Journal
of Formal Logic, 1(4):138–149, 1960.
[Bird, 1962] Otto Bird. The tradition of the logical Topics: Aristotle to Ockham. Journal
of the History of Ideas, 23(3):307–323., 1962.
[Brockriede and Ehninger, 1963] Wayne Brockriede and Douglas Ehninger. Decision by de-
bate. Dodd, Mead & Co,, New York, 1963.
[Budzysnka and Reed, 2011] Katarzyna Budzysnka and Chris Reed. Speech acts of argu-
mentation: Inference anchors and peripheral cues in dialogue. In Computational models
of natural argument: Papers from the 2011 AAAI workshop, pages 3–10, Menlo Park,
2011. AAAI Press.
[Ches˜nevar et al., 2006] Carlos Ches˜nevar, Sanjay Modgil, Iyad Rahwan, Chris Reed,
Guillermo Simari, Matthew South, Gerard Vreeswijk, and Steven Willmott.
Towards
an argument interchange format.
The Knowledge Engineering Review, 21(4):293–316,
dec 2006.
[Christensen, 1988] Johnny Christensen. The formal character of koinoi topoi in Aristotle’s
rhetoric and dialectic. Illustrated by the list in Rhetorica II, 23. Cahiers de l’institut du
moyen ˆage grec et latin, (57):3–10, 1988.
[Cicero, 2003] Marcus Tullius Cicero. Topica. Oxford University Press, Oxford, 2003.
[De Pater, 1965] Wilhelm A De Pater. Les Topiques d’Aristote et la dialectique platonici-
enne. ´Editions de St. Paul, Fribourg, 1965.
[Drehe, 2011] Iovan Drehe. The Aristotelian dialectical topos. Argumentum, 9(2):129–139,
2011.
[Dung, 1995] Phan Minh Dung. On the acceptability of arguments and its fundamental role
in nonmonotonic reasoning, logic programming and n-person games.
Artiﬁcial Intelli-
gence, 77(2):321–357, 1995.
[Duschl et al., 1999] Richard Duschl, Kirsten Ellenbogen, and Sibel Erduran. Promoting
argumentation in middle school science classrooms: A project SEPIA evaluation.
In
Annual Meeting of the National Association for Research in Science Teaching, pages
1–19, Boston, 1999. ERIC Document Reproduction Service No.ED453050.
[Duthie et al., 2016] Rory Duthie, Katarzyna Budzysnka, and Chris Reed. Mining ethos in
political debate. In Proceedings of the Sixth International Conference on Computational
Models of Argument, pages 299–310, Amsterdam, 2016. IOS Press.
[Erduran and Jimenez-Aleixandre, 2007] Sibel Erduran and M Pilar Jimenez-Aleixandre,
editors. Argumentation in science education: perspectives from classroom-based research.
Springer, Dordrecht, 2007.
[Erduran and Jim´enez Aleixandre, 2012] Sibel Erduran and Maria Pilar Jim´enez Aleixan-
dre.
Argumentation in science education research.
In Doris Jorde and Justin Dillon,
editors, Science Education Research and Practice in Europe: Retrospective and Prospec-
tive, pages 253–289. SensePublishers, Rotterdam, 2012.
[Freeman, 1991] James Freeman. Dialectics and the Macrostructure of Arguments. A The-
ory of Argument Structure. Foris, Berlin/New York, 1991.
[Gabbay and Woods, 2008] Dov Gabbay and John Woods, editors. Handbook of the history
of logic. Volume 2. Mediaeval and Renaissance Logic. Elsevier, Amsterdam, 2008.
[Garssen, 2001] Bart Garssen.
Argumentation schemes.
In Frans Van Eemeren, editor,
Crucial concepts in argumentation theory, pages 81–99. Amsterdam University Press,
Amsterdam, 2001.
[Gordon and Walton, 2006] Thomas Gordon and Douglas Walton.
The Carneades argu-
mentation framework: Using presumptions and exceptions to model critical questions. In
Proceedings of the 2006 conference on Computational Models of Argument: Proceedings
of COMMA 2006, pages 195–207, Amsterdam, 2006. IOS Press.
[Gordon and Walton, 2009] Thomas Gordon and Douglas Walton.
Legal reasoning with
argumentation schemes. In Carole D. Hafner, editor, Proceedings of the 12th International
Conference on Artiﬁcial Intelligence and Law, pages 137–146, New York, 2009. ACM.


## PDF page 54

570
Fabrizio Macagno, Douglas Walton, Chris Reed
[Gordon and Walton, 2016] Thomas Gordon and Douglas Walton. Formalizing Balancing
Arguments. In Proceedings of the 2016 Conference on Computational Models of Argument
(COMMA 2016), pages 327–338, Amsterdam, 2016. IOS Press.
[Gordon et al., 2007] Thomas Gordon, Henry Prakken, and Douglas Walton. The Carneades
model of argument and burden of proof. Artiﬁcial Intelligence, 171(10-15):875–896, jul
2007.
[Green-Pedersen, 1984] Niels Jørgen Green-Pedersen.
The tradition of the Topics in the
Middle Ages: The commentaries on Aristotle’s and Boethius’ Topics. Philosophia, Mu-
nich, 1984.
[Green-Pedersen, 1987] Niels Jørgen Green-Pedersen. The topics in medieval logic. Argu-
mentation, 1(4):407–417, 1987.
[Grennan, 1997] Wayne Grennan. Informal logic. McGill-Queen’s University Press, Mon-
treal, Quebec, 1997.
[Hastings, 1963] Arthur Hastings. A reformulation of the modes of reasoning in argumen-
tation. Ph.D. Dissertation, Northwestern University, Evanston, Illinois, 1963.
[Heath, 1994] Malcolm Heath. The Substructure of stasis-theory from Hermagoras to Her-
mogenes. The Classical Quarterly, 44(01):114, may 1994.
[Janier et al., 2014] Mathilde Janier, John Lawrence, and Chris Reed. OVA+: An argument
analysis interface. In Proceedings of the Fifth International Conference on Computational
Models of Argument (COMMA 2014), pages 463–464, Amsterdam, 2014. IOS Press.
[Katzav and Reed, 2004a] Joel Katzav and Chris Reed. A Classiﬁcation System for Argu-
ments. Technical report, University of Dundee, Dundee, 2004.
[Katzav and Reed, 2004b] Joel Katzav and Chris Reed. On argumentation schemes and the
natural classiﬁcation of arguments. Argumentation, 18(2):239–259, 2004.
[Kennedy, 1963] George Kennedy.
The art of persuasion in ancient Greece.
Princeton
University Press, Princeton, 1963.
[Kienpointner and Kindt, 1997] Manfred Kienpointner and Walther Kindt. On the problem
of bias in political argumentation: An investigation into discussions about political asylum
in Germany and Austria. Journal of Pragmatics, 27(5):555–585, 1997.
[Kienpointner, 1987] Manfred Kienpointner. Towards a typology of argumentative schemes.
In Frans van Eemeren, Rob Grootendorst, Anthony Blair, and Charles Willard, editors,
Argumentation: Across the lines of discipline, pages 275–287. Foris, Dordrech, 1987.
[Kienpointner, 1992] Manfred Kienpointner. Alltagslogik: Struktur und Funktion von Ar-
gumentationsmustern. Fromman-Holzboog, Stuttgart, Germany, 1992.
[Kim et al., 2010] Mijung Kim, Robert Anthony, and David Blades. Argumentation as a
Tool to Understand Complexity of Knowledge Integration.
In Proceedings of the 2nd
International STEM in Education Conference
Beijing, China
24-27 November 2012,
pages 154–160, Beijing, 2010. Beijing Normal University.
[Koehn et al., 2003] Philipp Koehn, Franz Josef Och, and Daniel Marcu. Statistical phrase-
based translation. In Proceedings of the 2003 Conference of the North American Chap-
ter of the Association for Computational Linguistics on Human Language Technology -
NAACL ’03, volume 1, pages 48–54, Morristown, NJ, USA, 2003. Association for Com-
putational Linguistics.
[Lawrence and Reed, 2015] John Lawrence and Chris Reed. Combining Argument Mining
Techniques. In Proceedings of the 2nd Workshop on Argumentation Mining, pages 127–
136, Stroudsburg, PA, USA, 2015. Association for Computational Linguistics.
[Lawrence et al., 2012] John Lawrence, Floris Bex, Chris Reed, and Mark Snaith. AIFdb:
Infrastructure for the argument web. In Proceedings of the fourth international conference
on computational models of argument (COMMA 2012), pages 515–516, Amsterdam, 2012.
IOS Press.
[Lawson, 1885] John Lawson. The law of presumptive evidence. Bancroft & Co., San Fran-
cisco, 1885.
[Macagno and Bigi, 2017] Fabrizio Macagno and Sarah Bigi. Analyzing the pragmatic struc-
ture of dialogues. Discourse Studies, 19(2):148–168, apr 2017.
[Macagno and Konstantinidou, 2013] Fabrizio Macagno and Aikaterini Konstantinidou.
What students’ arguments can tell us: Using argumentation schemes in science educa-
tion. Argumentation, 27(3):225–243, 2013.
[Macagno and Walton, 2014] Fabrizio Macagno and Douglas Walton. Emotive Language in
Argumentation. Cambridge University Press, Cambridge, 2014.


## PDF page 55

Argumentation Schemes
571
[Macagno and Walton, 2015] Fabrizio Macagno and Douglas Walton. Classifying the pat-
terns of natural arguments. Philosophy and Rhetoric, 48(1):26–53, 2015.
[Macagno et al., 2014] Fabrizio Macagno, Douglas Walton, and Christopher Tindale. Ana-
logical reasoning and semantic rules of inference. Revue internationale de philosophie,
270(4):419–432, 2014.
[Macagno et al., 2016] Fabrizio Macagno, Douglas Walton, and Christopher Tindale. Ana-
logical Arguments: Inferential Structures and Defeasibility Conditions. Argumentation,
pages 1–23, 2016.
[Macagno, 2012] Fabrizio Macagno. Presumptive reasoning in interpretation. Implicatures
and conﬂicts of presumptions. Argumentation, 26(2):233–265, 2012.
[Macagno, 2015] Fabrizio Macagno. A means-end classiﬁcation of argumentation schemes.
In Frans van Eemeren and Bart Garssen, editors, Reﬂections on theoretical issues in
argumentation theory, pages 183–201. Springer, Cham, 2015.
[MacCormick and Summers, 1991] Neil MacCormick and Robert Summers.
Interpreting
Statutes: A Comparative Study. Dartmouth, Aldershot, 1991.
[Mochales Palau and Ieven, 2009] Raquel Mochales Palau and Aagje Ieven.
Creating an
argumentation corpus: do theories apply to real arguments?: a case study on the legal
argumentation of the ECHR.
In Proceedings of the 12th International Conference on
Artiﬁcial Intelligence and Law, pages 21– 30, New York, 2009. ACM Press.
[Mochales Palau and Moens, 2008] Raquel Mochales Palau and Marie-Francine Moens.
Study on the structure of argumentation in case law. In Enrico Francesconi, Giovanni
Sartor, and Daniela Tiscornia, editors, Proceedings of the 2008 Conference on Legal
Knowledge and Information Systems, pages 11–20, Amsterdam, 2008. IOS Press.
[Mochales Palau and Moens, 2009] Raquel Mochales Palau and Marie Francine Moens. Ar-
gumentation mining:
The Detection, Classiﬁcation and Structuring of Arguments in
Text.
In Belgian/Netherlands Artiﬁcial Intelligence Conference, pages 351–352, New
York, 2009. ACM.
[Mochales Palau and Moens, 2011] Raquel Mochales Palau and Marie Francine Moens. Ar-
gumentation mining. Artiﬁcial Intelligence and Law, 19(1):1–22, 2011.
[Modgil and Prakken, 2013] Sanjay Modgil and Henry Prakken. A general account of argu-
mentation with preferences. Artiﬁcial Intelligence, 195:361–397, 2013.
[Moens and Mochales Palau, 2007] Marie-Francine Moens and Raquel Mochales Palau.
Study on Sentence Relations in the Automatic Detection of Argumentation in Legal Cases.
In Arno Lodder and Laurens Mommers, editors, Legal Knowledge and Information Sys-
tems: JURIX 2007, pages 89–98, Amsterdam, 2007. IOS Press.
[Moens et al., 2007] Marie-Francine Moens, Erik Boiy, Raquel Mochales Palau, and Chris
Reed. Automatic detection of arguments in legal texts. In Proceedings of the 11th inter-
national conference on Artiﬁcial intelligence and law, pages 225–230, New York, 2007.
ACM Press.
[Nussbaum and Edwards, 2011] Michael Nussbaum and Ordene V. Edwards. Critical ques-
tions and argument stratagems: A framework for enhancing and analyzing students’ rea-
soning practices. Journal of the Learning Sciences, 20(3):443–488, 2011.
[Ozdem et al., 2013] Yasemin Ozdem, Hamide Ertepinar, Jale Cakiroglu, and Sibel Erdu-
ran. The nature of pre-service science teachers’ argumentation in inquiry-oriented labo-
ratory contex. International Journal of Science Education, 35(15):2559–2586, 2013.
[Peldszus and Stede, 2016] Andreas Peldszus and Manfred Stede. An annotated corpus of
argumentative microtexts. In Argumentation and Reasoned Action: Proceedings of the
1st European Conference on Argumentation, pages 801–815, London, 2016. College Pub-
lications.
[Perelman and Olbrechts-Tyteca, 1969] Chaim Perelman and Lucie Olbrechts-Tyteca. The
New Rhetoric: A treatise on argumentation.
University of Notre Dame Press, Notre
Dame, Ind., 1969.
[Pollock, 1995] John Pollock. Cognitive Carpentry. MIT Press, Cambridge, Mass., 1995.
[Prakken et al., 2015] Henry Prakken, Adam Wyner, Trevor Bench-Capon, and Katie
Atkinson.
A formalization of argumentation schemes for legal case-based reasoning in
ASPIC+. Journal of Logic and Computation, 25(5):1141–1166, oct 2015.
[Prakken, 2005] Henry Prakken. AI & Law, logic and argument schemes. Argumentation,
19(3):303–320, 2005.


## PDF page 56

572
Fabrizio Macagno, Douglas Walton, Chris Reed
[Prakken, 2010] Henry Prakken. An abstract framework for argumentation with structured
arguments. Argument & Computation, 1(2):93–124, 2010.
[Rahwan et al., 2007] Iyad Rahwan, Fouad Zablith, and Chris Reed. Laying the foundations
for a World Wide Argument Web. Artiﬁcial Intelligence, 171(10-15):897–921, jul 2007.
[Rahwan et al., 2011] Iyad Rahwan, Bita Banihashemi, Christopher Reed, Douglas Walton,
and Sherief Abdallah. Representing and classifying arguments on the semantic web. The
Knowledge Engineering Review, 26(04):487–511, 2011.
[Rapanta and Macagno, 2016] Chrysi Rapanta and Fabrizio Macagno.
Argumentation
methods in educational contexts: Introduction to the special issue. International Journal
of Educational Research, 79:online ﬁrst, 2016.
[Rapanta and Walton, 2016] Chrysi Rapanta and Douglas Walton.
The use of argument
maps as an assessment tool in higher education. International Journal of Educational
Research, 79:211–221, 2016.
[Rapanta et al., 2013] Chrysi Rapanta, Merce Garcia-Mila, and Sandra Gilabert. What is
meant by argumentative competence? An integrative review of methods of analysis and
assessment in education. Review of Educational Research, 83(4):483–520, 2013.
[Reed and Walton, 2005] Chris Reed and Douglas Walton. Towards a Formal and Imple-
mented Model of Argumentation Schemes. In Iyad Rahwan, Pavlos Moraitis, and Chris
Reed, editors, Agent Communication, Argumentation in Multi-Agent Systems, pages 19–
30. Springer-Verlag, Berlin/Heidelberg, 2005.
[Reed et al., 2007] Christopher Reed, Douglas Walton, and Fabrizio Macagno. Argument
diagramming in logic, law and artiﬁcial intelligence.
Knowledge Engineering Review,
22(1):87–109, 2007.
[Rowe et al., 2006] Glenn Rowe, Fabrizio Macagno, Christopher Reed, and Douglas Walton.
Araucaria as a tool for diagramming arguments in teaching and studying philosophy.
Teaching Philosophy, 29(2):111–124, 2006.
[Rubinelli, 2009] Sara Rubinelli. Ars Topica: The classical technique of constructing argu-
ments from Aristotle to Cicero, volume 15. Springer, Amsterdam, 2009.
[Schiappa, 1999] Edward Schiappa.
The Beginnings of Rhetorical Theory in Classical
Greece. Yale University Press, New Haven & London, 1999.
[Slomkowski, 1997] Paul Slomkowski. Aristotele’s Topics. Brill, Leiden, 1997.
[Stump, 1982] Eleonore Stump.
Topics:
their development and absorption into conse-
quences. In Norman Kretzmann, Anthony Kenny, and Jan Pinborg, editors, Cambridge
History of Later Medieval Philosophy, pages 273–299. Cambridge University Press, Cam-
bridge, 1982.
[Stump, 1989] Eleonore Stump. Dialectic and its place in the development of Medieval logic.
Cornell University Press, Ithaca and London, 1989.
[Stump, 2004] Eleonore Stump.
Boethius’s ”De topicis diﬀerentiis”.
Cornell University
Press, Ithaca and London, 2004.
[Tarello, 1980] Giovanni Tarello. L’interpretazione della legge. Giuﬀr`e, Milano, 1980.
[Tindale, 2010] Christopher Tindale. Reason’s Dark Champions: Constructive Strategies of
Sophistical Argument. University of South Carolina Press, Columbia, 2010.
[Toulmin et al., 1984] Stephen Toulmin, Richard Rieke, and Allan Janik. An introduction
to reasoning. Number Sirsi) i9780024211606. Macmillan Publishing Company, New York,
1984.
[Van Eemeren and Grootendorst, 1992] Frans Van Eemeren and Rob Grootendorst. Argu-
mentation, communication and fallacies. Erlbaum, Hillsdale, NJ, 1992.
[van Gelder, 2007] Tim van Gelder. The rationale for RationaleTM. Law, Probability and
Risk, 6(1-4):23–42, oct 2007.
[Verheij, 2003a] Bart Verheij. Deﬂog: on the logical interpretation of prima facie justiﬁed
assumptions. Journal of Logic and Computation, 13(3):319–346, 2003.
[Verheij, 2003b] Bart Verheij. Dialectical Argumentation with Argumentation Schemes. Ar-
tiﬁcial Intelligence and Law, 11(2):167–195, 2003.
[Walker et al., 2012] Marilyn Walker, Jean Fox Tree, Pranav Anand, Rob Abbott, and
Joseph King. A Corpus for Research on Deliberation and Debate. In Nicoletta Calzolari,
Khalid Choukri, Thierry Declerck, Mehmet Uur Doan, Bente Maegaard, Joseph Mari-
ani, Asuncion Moreno Piperidis, Jan Odijk, and Stelios Piperidis, editors, Proceedings of
the 8th International Conference on Language Resources and Evaluation (LREC),, pages
812–817. European Language Resources Association, 2012.


