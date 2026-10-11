# Argumentation Schemes (chapter)

Source ID: A01
Authors: Fabrizio Macagno; Douglas Walton; Chris Reed
Original attachment: Argumentation Schemes, Douglas.pdf
Identity: Chapter 11; printed pp. 517–574. Publication container/year not established from the supplied excerpt. Not the 2008 Cambridge monograph.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 41

Argumentation Schemes
557
undercutter but could also perhaps be taken to refer to a conclusion attack. So
here the problem is posed of how to model critical questions given that critical
questions can perform more than one function.
ASPIC+ [Prakken, 2010] is a formal argumentation system that consists
of a logical language L with a binary contrariness relation that operates like
negation along with two kinds of inference rules, strict and defeasible, deﬁned
over L. ASPIC+ is based on the abstract argumentation framework (Dung,
1995) which can be deﬁned as a pair (Args, Def ), where Args is a set of
arguments and Def
Args
Args is a binary attack relation. The underlying
idea of the formalism is that each argument in a sequence of argumentation
forming a directed graph structure can be defeated by other arguments so that
a2 defeats a1, a3 defeats a2, . . ., and defeats an-1. Arguments in the graph
can be labeled as in or out. An argument is rejected (out) if it is attacked by
any other argument that is in. An argument is accepted if it is not attacked by
any other argument that is in. Note that the notions of argument and argument
attack are taken as primitive in an abstract argumentation system, so that such
a system by itself provides no way of modeling the premises and the conclusion.
In the system developed in [Prakken et al., 2015] for case-based reasoning,
preferences among factors are established in the present case, and then these
preferences can be applied to the current case.
One of the argumentation
schemes (CS1) of can be used to brieﬂy explain how such schemes are meant to
be used in legal arguments from precedent. In all these schemes, for purposes
of presentation, it is assumed that the arguer is putting forward the current
argument (curr) to support the side of the plaintiﬀ.
commonPfactors(curr; prec) = p,
commonDfactors(curr; prec) = d,
preferred(p; d)
———————————
outcome(curr) = Plaintiﬀ
According to this scheme, the current argument should be decided for the
plaintiﬀbecause the common p factors were preferred to the common d factors
in the precedent argument. [Prakken et al., 2015] use a running example to
illustrate how an argument ﬁtting a scheme can be attacked by other arguments
in the formal system representing the argumentation in a legal case.
Argument schemes are being used in AI and Law for argument mining.
Moens, Mochales Palau, Boiy and Reed devised techniques for automatically
classifying arguments in legal texts by using indicators of rhetorical structure
expressed by conjunctions and adverbial groupings [Moens et al., 2007, p.226].
They identify words, pairs of successive words, sequences of three successive
words, adverbs, verbs and modal auxiliary verbs. This work has been applied
to legal argumentative texts ([Mochales Palau and Moens, 2009]; [Mochales
Palau and Moens, 2011]). By classifying types of arguments using argumen-
tation schemes they built a system for searching for arguments in legal cases


## PDF page 42

558
Fabrizio Macagno, Douglas Walton, Chris Reed
[Mochales Palau and Moens, 2008]. The project used human annotators su-
pervised by legally trained personnel to identify types of arguments in texts
of the European Court of Human Rights [Mochales Palau and Ieven, 2009].
Their results suggested that it would help to have additional criteria that can
be applied to judge whether a given ﬁts a particular scheme.
Rahwan et al. [Rahwan et al., 2011]) carried forward research on the auto-
mated identiﬁcation of particular schemes by developing an OWL-based ontol-
ogy of argumentation schemes in description logic that showed how description
logic inference techniques can be used to reason about automatic argument
classiﬁcation. Their method of identifying schemes has been implemented in
a web-based system called Avicenna (Rahwan et al., 2011, pp. 1113). A user
can search arguments by using schemes along with other tools.
Gordon and Walton [Gordon and Walton, 2006] proposed a solution to the
problem of how to model critical questions by using three kinds of premises (or-
dinary premises, assumptions and exceptions) in the Carneades Argumentation
System (CAS). This solution used information about the dialectical status of
statements (undisputed, at issue, accepted or rejected) to model critical ques-
tions in such a way as to allow the burden of proof to be allocated to the
proponent of the argument or the critical questioner as appropriate for the
case in point. On this way of proceeding, ordinary premises need to be sup-
ported by further arguments even if they have not been questioned. But in the
case of exceptions, however, the critical questioner is the one who has to oﬀer
evidential support to make his criticism defeat the argument.
Version 4 is the current implemented formal and computational system of
CAS, based on the formal model of argument [Gordon and Walton, 2016] called
CAS2.
CAS2 provides support for cumulative arguments, cyclic argument
graphs, practical reasoning, and multi-criteria decision analysis. The source
code of all four versions can be accessed on the Internet6. Carneades 4 is now
online 7. CAS2, as implemented in version 4 of Carneades, provides a formal
model that uses argumentation schemes.
In the CAS2 model [Gordon and Walton, 2016] an argumentation scheme
is deﬁned as a tuple (e, v, g), where e is a function for weighing arguments
which instantiate a scheme, v is a function for validating arguments, to test
whether they properly instantiate an argumentation scheme, and g is a function
for generating arguments by instantiating the scheme. The validation function
tells us whether the argument instantiates a particular scheme, but then, once
a set of schemes has been speciﬁed, the system can apply their validation
functions to given argument to whether that scheme is instantiated, or not, by
the given argument.
An argument is deﬁned as a tuple (s, P, c, u), where s is the scheme in-
stantiated by the argument; P, a ﬁnite subset of L, is the set of premises of
the argument; c, a member of L, is the conclusion of the argument. U is an
6Retrieved from: https://github.com/carneades
7Retrieved from: http://carneades.fokus.fraunhofer.de/carneades


## PDF page 43

Argumentation Schemes
559
undercutter of the argument [Pollock, 1995]. In version 4 of CAS an issue is
deﬁned as a tuple (O, f ), where O represents the options (called the alterna-
tive positions) of the issue, and f is the proof standard of the issue. Argument
graphs in CAS version 4 are tripartite, rather than bipartite, as in the previous
versions, with separate nodes for statements, arguments and issues. Argument
diagrams in version 4 are extended with a new node type, diamonds, for repre-
senting issues. There can be any number of issues you like in a single diagram.
Argument evaluation is carried out by labeling statements in, out or undecided.
A statement is in if and only if it has been assumed to be acceptable to a ra-
tional audience, or has been derived from such assumptions via the application
of the arguments, argument weighing functions and proof standards used in
CAS. A statement is out if and only if it is neither assumed nor supported by
arguments and would therefore be rejected by a rational audience. A statement
is undecided if it is neither in nor out.
Carneades 3 uses backwards-chaining, in a goal-directed way, whereas Car-
neades 4 uses forwards-reasoning to derive arguments from argumentation
schemes and assumptions. Both strategies, forwards and backwards reasoning,
have their advantages. Forwards reasoning allows CAS to invent arguments
using argumentation schemes, such as the scheme for argument from expert
opinion, where the conclusion is a second-order variable ranging over proposi-
tions. Only Carneades 4 can construct arguments using formalizations of all of
the twenty or so schemes currently built into the system.
Case-based reasoning (CBR) is vitally important for AI and Law and for
understanding legal reasoning generally. CBR evaluates an argument in a given
case by comparing and contrasting its features to those of prior cases that
have already been evaluated [Aleven, 1997]. These prior cases are stored in
a knowledge base which supplies similar precedent cases that can be pro or
con the evaluation being considered in the given case. In some systems widely
known in AI and law [Ashley, 1990], judgments of similarity between a pair
of cases are decided by the factors that they share.
Special argumentation
schemes have been built to model arguments from precedent using factors in
case-based reasoning ([Gordon and Walton, 2009]; [Wyner and Bench-Capon,
2007]; [Wyner et al., 2011]). Prakken et al. [Prakken et al., 2015] oﬀered a
formal version of these legal case-based argumentation schemes using ASPIC+.
Walton, Sartor and Macagno [Walton et al., 2016] showed how canons of
interpretation can be translated into argumentation schemes. This project was
carried out by by analyzing the most common types of statutory arguments
found in legal examples and certain key forms of interpretive legal argumenta-
tion found in the work of Tarello [Tarello, 1980] and McCormick and Summers
[MacCormick and Summers, 1991]. Steps were carries out to show how these
legally recognizable forms of argument can be formulated as argumentation
schemes. Among the schemes modeled are argument from ordinary meaning,
argument from technical meaning, argument from precedent, argument from
purpose, a contrario argument, historical argument and the non-redundancy


## PDF page 44

560
Fabrizio Macagno, Douglas Walton, Chris Reed
argument. It was shown using classical examples of statutory interpretation in
law how these schemes (and others) can be incorporated into computational
argumentation systems such as CAS and APSIC+ and applied to displaying
the pro-contra structure argumentation in legal cases using argument mapping
tools.
In the following sections we will illustrate shortly two other computational
applications of argumentation schemes, namely their role in argument mining
and formal ontologies.
9
Using Schemes for Argument Mining
Argumentation schemes also have an important role to play in a major new area
of computational research into argumentation: argument mining. Argument
mining focuses on the development of algorithms and techniques for the auto-
matic extraction of argument structure from natural language text. Though
it has connections to areas such as sentiment analysis and opinion mining, it
represents a substantially more demanding task. There are two features that
make argument mining so diﬃcult. The ﬁrst concerns the availability of data
and the second, the limits of statistical approaches to language understanding.
Many approaches to mining syntactic and semantic structure from unre-
stricted natural language have, since the late 1990s, been based heavily in
statistical analysis: essentially, modelling the regularities in language by exam-
ining and comparing many, many diﬀerent examples. The most robust syntac-
tic parsers, for example, are based not on theoretical linguistic analysis which
proved on the whole to be too limited and too brittle but on statistical models
based on corpora typically comprising millions of examples [Koehn et al., 2003].
Though the machine learning mechanisms upon which such techniques depend
vary, one feature that they share is the need for such large datasets from which
to draw regularities. If, therefore, argument mining is to be able to deploy
the same techniques, it requires large datasets, and datasets not just of argu-
mentation per se, by argumentation that has been analysed for its structure.
As anyone involved in the teaching of critical thinking skills will attest, such
analysis of argument structure is both demanding and extremely time consum-
ing. Until very recently there were few datasets, and those that did exist were
available in idiosyncratic representation languages, with little re-use between
research teams and projects so what eﬀort was invested in data collection and
analysis was regularly lost. Two approaches have started to change this.
First, there have been attempts to collect datasets speciﬁcally for community
use. The ﬁrst example is the Internet Argument Corpus, IAC [Walker et al.,
2012], which collects 390,000 examples. The problem facing the IAC is that it is
designed primarily from a text-processing viewpoint, with little argumentation
theory sitting behind it. As a result, the conception of argument that it embod-
ies is very thin and more or less unrecognisable to researchers from argumenta-
tion theory and computational models of argument, viz., quote-response pairs
with associated polarity (additional features including sarcasm and nastiness


## PDF page 45

Argumentation Schemes
561
are marked for subsets). A second example is more directly rooted in informed
models of argumentation. The Potsdam Microtext Corpus [Peldszus and Stede,
2016] provides artiﬁcially constrained but completely human-generated, natu-
ral language arguments that are structured according to the work of Freeman
[Freeman, 1991] with explicit distinction between, for example, linked and con-
vergent arguments, undercutting and rebutting attacks and so on. Another
unique advantage of the Microtext Corpus is that it has been professionally
translated so that both English and German versions exist: to our knowledge
this is the ﬁrst parallel corpus of argumentation. On the other hand, the fact
that every argument is required to contain a total of ﬁve components (premises
and conclusions), whilst providing a vitally useful laboratory for testing tech-
niques, risks placing a severe limitation on the subsequent generalizability of
those techniques to unrestricted arguments in the wild. The limited size of the
corpus just 130 examples also places limitations on what can be accomplished
using traditional statistical machine learning techniques.
The second approach has been to provide infrastructure speciﬁcally for col-
lecting, publishing, sharing and re-using corpora. Whilst there are now several
platforms for online analysis of argument (argunet 8, debategraph 9, AGORA-
net 10, RationaleOnline 11, etc.)
none provide open access to the data in
machine processable ways, except, as far as we are aware, for the infrastructure
oﬀered by the Argument Web ([Rahwan et al., 2011]; [Bex et al., 2013]). The
Argument Web is a vision for an interconnected web of arguments and debates,
regardless of the software used to create them, analyse them or extract them,
and regardless, too, of the uses academic, social or commercial to which they
might be put. The vision supports, for example, the academic analysis of an ar-
gument presented in a political broadcast; the automated analysis of responses
to it on social media; the deployment of automated dialogue games for online
users to interact with both original and responses; the automated summary of
the status of the debate to a government policy department; and the delivery
of a corpus comprising the debate to researchers in argument mining. Argu-
mentation schemes in the style of [Walton et al., 2008]form a cornerstone of
the Argument Web, as a way of providing a rich ontology of reasoning forms.
Further details of this ontology occur in the next section; here we focus on the
tools and the ways in which they can be used to develop corpora.
Though the ﬁrst publicly available corpus of argumentation was developed
using Araucaria (viz. AraucariaDB, see [Reed and Walton, 2005]), the soft-
ware itself is now very old and virtually obsolete. Though it remains the only
software to handle large analyses, such as the ones developed by Wigmore
for mapping cases, and the only to interchange between Wigmore, Toulmin
and Freeman styles of analysis, it has been superseded in its core functional-
8Retrieved from: http://www.argunet.org/ (Accessed on 10 May 2016)
9Retrieved
from:
http://debategraph.org/Stream.aspx?nid=61932&vt=ngraph&
dc=focus (Accessed on 10 May 2016)
10http://agora.gatech.edu/ (Accessed on 10 May 2016)
11https://www.rationaleonline.com/ (Accessed on 10 May 2016)


## PDF page 46

562
Fabrizio Macagno, Douglas Walton, Chris Reed
ity by the Online Visualisation of Argument tool, OVA [Janier et al., 2014].
OVA provides a simple-to-use interface for analysing existing argumentation
in both monologue and, in the extended OVA+, also dialogue. It supports
enthymeme reconstruction; argumentation scheme analysis; critical question
processing; serial, linked, convergent and divergent structures; undercutting,
rebutting and undermining attacks; and in OVA+, locution analysis; dialogue
game rule analysis; illocutionary force identiﬁcation; the role of ethos [Duthie
et al., 2016] and personal attacks; and ultimately, full Inference Anchoring The-
ory analysis [Budzysnka and Reed, 2011]. Analyses from OVA can be stored
in AIFdb, a database infrastructure fabric for storing and accessing argument
data [Lawrence et al., 2012].
One side eﬀect of using AIFdb is that the data is easily transportable to other
forms, both representational (in being able to convert to formats required for
Carneades [Walton and Gordon, 2012] and Rationale [van Gelder, 2007], for
example), and processable (in being able to convert via ASPIC+ [Modgil and
Prakken, 2013] to abstract frameworks [Dung, 1995] via formal equivalences
established in [Bex et al., 2013]. More importantly for our current purposes,
sets of analyses in AIFdb can be conﬁgured to constitute a corpus using the
AIFdb corpus management tools [Lawrence and Reed, 2015] available online at
corpora.aifdb.org, and AIFdb current constitutes the largest publicly available
dataset of analysed argumentation. These tools enable research teams to deﬁne
corpora comprising both analysed argumentation and raw text; both argumen-
tative and non-argumentative source material; both raw data and metadata.
Corpora themselves are aggregable providing ﬂexible structuring options to
manage dependencies between teams, projects, and objectives. The original
AraucariaDB corpus is available on this infrastructure, but so too are smaller
datasets focusing speciﬁcally on argumentation schemes, such as the Argument
Schemes in the Moral Maze, comprising excerpts from the BBC Moral Maze
radio programme that involve 35 instances of argumentation schemes and the
ExpertOpinion-PositiveConsequences corpus comprising 71 examples of just
these two schemes.
With the availability of appropriate datasets becoming less of an impedi-
ment, various approaches to automatically recognising argument structure have
been developed. The majority have been focused speciﬁcally on statistical mod-
els, which brings us to the second major challenge facing argument mining: the
limits of such models. Whilst it is certainly the case that statistical approaches
are starting to deliver results for argument mining, and will undoubtedly con-
tinue to do so, it is also the case that the more sophisticated conceptions of
argument developed in argumentation theory remain extraordinarily demand-
ing. The reason for this lies precisely in their sophistication. With so many
patterns of argumentation, so many structures, so many ways in which com-
ponents can be left implicit, so many types of reasoning, the amount of data
required to train statistical models becomes not just unwieldy but unreasonable
and, quite probably, unattainable.


## PDF page 47

Argumentation Schemes
563
Consider a comparison with syntactic analysis, where statistical models have
been so successful. The number of rules governing how diﬀerent parts of speech
can be legally combined run in theoretical linguistics to tens of examples in
statistical models, it is hundreds (which is why they are so successful). The
number of rules governing how argument components can be assembled (and
left implicit) runs, by combination across argumentation schemes, to thousands
or more. So whilst we might expect statistically oriented techniques to deliver
us good results on simple and strongly generalizable aspects of argument recog-
nition, for the type of analysis that is typically taught to students of critical
thinking classes, more is required. It is looking increasingly likely that having
strong, well deﬁned conceptions of argument, dialogue and argument schemes
provide exactly the sort of additional information required to guide machine
learning processes by acting, in essence, as priors to that process: deﬁning
expectations about what is likely to be seen. This combination of statistical
and structural approaches is looking very promising. In particular, we pro-
vide examples here that tap in speciﬁcally to structure provided by argument
schemes.
Feng and Hirst [Wei Feng and Hirst, 2011] aimed to classify arguments into
the type of scheme employed.
Like some of the earliest work in argument
mining, such as [Moens and Mochales Palau, 2007], they also used the Arau-
cariaDB corpus as a starting point, because it was the only dataset at that
time with annotated examples of argumentation schemes. They used the 65
argumentation schemes from [Walton et al., 2008], but emphasized the impor-
tance of the ﬁve schemes they found to be the most commonly used ones in
their corpus: argument from example, argument from cause to eﬀect, practical
reasoning, argument from consequences and argument from verbal classiﬁca-
tion [Wei Feng and Hirst, 2011]. The number of occurrences of these most
common ﬁve schemes constituted 61% of the kinds of arguments identiﬁed in
their database [Wei Feng and Hirst, 2011, p.998]. They used a variety of fea-
tures with which to train the machine learning classiﬁers including key words
and phrases as textual indicators of argumentation schemes. They identiﬁed,
for example, twenty-eight keywords and phrases associated with the scheme
for practical reasoning, including want, aim, objective, and modal verbs like
should, must and need [Wei Feng and Hirst, 2011, p.991]. Their results were
extremely promising, providing classiﬁcation accuracies ranging from 0.64 to
0.98.
Building on this approach, Lawrence and Reed ([Lawrence and Reed, 2015]
extended the model to use argumentation schemes not just as a target for ma-
chine learning but to aid the very process of identifying argumentative structure
(rather than presupposing it as input, as in Feng and Hirst). The intuition is
that argumentation schemes do not connect propositions that are all alike, but
rather are associated with particular types of propositions. In this way, ar-
guments from positive consequence will typically conclude with a normative
statement in the subjunctive mood; arguments from expert opinion will typi-


## PDF page 48

564
Fabrizio Macagno, Douglas Walton, Chris Reed
cally have a premise which reports, either directly or indirectly, the speech of
another; arguments from analogy will include a premise which attributes some
property to some individual; and so on. If it is possible to identify instances
of some of these types, it will constrain the potential argument structures that
can be reassembled. If, for example, an automatic algorithm can spot the lex-
eme said, there is a reasonable chance that we have reported speech, which
in turn increases the chance that it is part of an expert opinion argument. If
we can ﬁnd the lexeme expert in a sentence close by, we can be even more
sure we have argument from expert opinion and can start looking nearby for
a conclusion and that conclusion is likely to be a sentence which has strong
semantic similarity with the clause that follows said. In this way, knowing a
priori about argumentation scheme structure helps to constrain the problem
of automatically recognising the argument structure. It turns out that this
hypothesis is borne out by results.
Lawrence and Reed report (ibid.) results ranging from an F1 performance
of 0.59 to 0.91 for detecting scheme components and of 0.62 to 0.88 for iden-
tifying scheme instances. Operationalising argumentation scheme structure in
this way depends, however, upon knowledge engineering, or, more speciﬁcally,
ontology engineering the construction of explicit computational models that
capture scheme structure and the commonalities, similarities and classiﬁcatory
relationships between schemes. It is to this question that we turn next.
10
Schemes in Formal Ontologies
The Argument Interchange Format, AIF, is not just a representation language
for argument structure; it also has a formal deﬁnition rooted in description
logic; that is to say, it provides a core ontology for describing argument (though
that core is rather compact, it admits of extension using adjunct ontologies that
extend it to handle features such as dialogical interaction, user- and social-
oriented features, and so on). The AIF was laid out initially in [Ches˜nevar
et al., 2006] and extended in its description logic speciﬁcation in [Rahwan et
al., 2007]. Given this basis, it is then rather straightforward to extend it to
further specify not just that two propositions might be linked by an application
of a rule of inference (or RA), but to also specify the diﬀerent types of such
rules of inference, that is to deﬁne an ontology of argumentation schemes.
This ontology not only describes the structure of argumentation schemes in
machine-processable form, but also deﬁnes relationships between schemes (such
as generalisation-speciﬁcation relationships) and relationships between scheme
components (such as that knowledge assertions occur as premises in several
diﬀerent schemes).
By way of example, snippets of the ontology concerned
with the argumentation scheme from expert opinion are shown in Figure 17
below.


