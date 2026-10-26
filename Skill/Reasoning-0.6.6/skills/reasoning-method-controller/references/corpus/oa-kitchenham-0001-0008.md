# Preliminary Guidelines for Empirical Research in Software Engineering

Source ID: C02
Authors: Barbara A. Kitchenham and coauthors
Source URL: https://www.cin.ufpe.br/~in1002/leituras/preliminaryGuidelinesEmpiricalResearchSE.pdf
DOI: 10.1109/TSE.2002.1027796
Identity: IEEE TSE 28(8), 2002, pp. 721–734. Institutional course copy.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 1

Preliminary Guidelines for Empirical Research
in Software Engineering
Barbara A. Kitchenham, Member, IEEE Computer Society,
Shari Lawrence Pfleeger, Member, IEEE, Lesley M. Pickard, Peter W. Jones,
David C. Hoaglin, Khaled El Emam, Member, IEEE Computer Society, and
Jarrett Rosenberg, Member, IEEE Computer Society
AbstractÐEmpirical software engineering research needs research guidelines to improve the research and reporting processes. We
propose a preliminary set of research guidelines aimed at stimulating discussion among software researchers. They are based on a
review of research guidelines developed for medical researchers and on our own experience in doing and reviewing software
engineering research. The guidelines are intended to assist researchers, reviewers, and meta-analysts in designing, conducting, and
evaluating empirical studies. Editorial boards of software engineering journals may wish to use our recommendations as a basis for
developing guidelines for reviewers and for framing policies for dealing with the design, data collection, and analysis and reporting of
empirical studies.
Index TermsÐEmpirical software research, research guidelines, statistical mistakes.
æ
1
INTRODUCTION
W
E have spent many years both undertaking empirical
studies in software engineering ourselves and review-
ing reports of empirical studies submitted to journals or
presented as postgraduate theses or dissertations. In our
view, the standard of empirical software engineering
research is poor. This includes case studies, surveys, and
formal experiments, whether observed in the field or in a
laboratory or classroom. This statement is not a criticism of
software researchers in particular; many applied disciplines
have problems performing empirical studies. For example,
Yancey [50] found many articles in the American Journal of
Surgery (1987 and 1988) with ªmethodologic errors so
serious as to render invalid the conclusions of the authors.º
McGuigan [31] reviewed 164 papers that included numerical
results that were published in the British Journal of Psychiatry
in 1993 and found that 40 percent of them had statistical
errors. When Welch and Gabbe [48] reviewed clinical articles
in six issues of the American Journal of Obstetrics, they found
more than half the studies impossible to assess because the
statistical techniques used were not reported in sufficient
detail. Furthermore, nearly one third of the articles con-
tained inappropriate uses of statistics. If researchers have
difficulty in a discipline such as medicine, which has a rich
history of empirical research, it is hardly surprising that
software engineering researchers have problems.
In a previous investigation of the use of meta-analysis in
software engineering [34], three of us identified the need to
assess the quality of the individual studies included in a
meta-analysis. In this paper, we extend those ideas to
discuss several guidelines that can be used both to improve
the quality of on-going and proposed empirical studies and
to encourage critical assessment of existing studies. We
believe that adoption of such guidelines will not only
improve the quality of individual studies but will also
increase the likelihood that we can use meta-analysis to
combine the results of related studies. The guidelines
presented in this paper are a first attempt to formulate a
set of guidelines. There needs to be a wider debate before
the software engineering research community can develop
and agree on definitive guidelines.
Before we describe our guidelines, it may be helpful to
you to understand who we are and how we developed
these guidelines. Kitchenham, Pickard, Pfleeger, and El-
Emam are software engineering researchers with back-
grounds in statistics as well as computer science. We
regularly review papers and dissertations, and we often
participate in empirical research. Rosenberg is a statistician
who applies statistical methods to software engineering
problems. Jones is a medical statistician with experience in
developing standards for improving medical research
studies. Hoaglin is a statistician who has long been
interested in software and computing. He reviewed eight
papers published in Transactions on Software Engineering in
the last few years. These papers were not chosen at random.
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
721
. B.A. Kitchenham and L.M. Pickard are with the Computer Science
Department, Keele University, Keele, Staffordshire ST5 5BG, UK.
E-mail: {barbara, lesley}@cs.keele.ac.uk.
. S.L. Pfleeger is with the RAND Corporation, 1200 South Hayes St.,
Arlington, VA 22202-5050. E-mail: shari_pfleeger@rand.org.
. P.W. Jones is with the Mathematics Department, Keele University, Keele,
Staffordshire ST5 5BG, UK. E-mail: maa11@maths.keele.ac.uk.
. D.C. Hoaglin is with Abt Associates Inc., 55 Wheeler Street, Cambridge,
MA 02138. E-mail: Dave_Hoaglin@abtassoc.com.
. K. El Emam is with the National Research Council of Canada Institute for
Information Technology, Montreal Road, Building M-50 Ottowa, Ontario,
K1J 8H5 Canada. E-mail: khaled.el-emam@seg-nrc.org.
. J. Rosenberg is with Sun Microsystems, San Antonio Road, MS MPK17-
307 Palo Alto, CA 94303. E-mail: Rosenberg@eng.sun.com.
Manuscript received 30 Dec. 1999; revised 26 Jan. 2001; accepted 23 Apr.
2001.
Recommended for acceptance by M. Jazayeri.
For information on obtaining reprints of this article, please send e-mail to:
tse@computer.org, and reference IEEECS Log Number 111161.
0098-5589/02/$17.00 ß 2002 IEEE
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 2

Rather, they were selected (by those of us whose primary
focus is software engineering) because their authors are
well-known for their empirical software engineering work
and because their techniques are typical of papers sub-
mitted to this journal. Hoaglin's independent comments on
these papers confirmed our suspicions that the current state
of empirical studies as published in Transactions on Software
Engineering is similar to that found in medical studies. He
found examples of poor experimental design, inappropriate
use of statistical techniques and conclusions that did not
follow from the reported results. We omit the titles of these
papers. We want the focus of our guidelines to be overall
improvement of our discipline, not finger-pointing at
previous work. We do, however, cite papers that include
specific statistical mistakes when they help illustrate the
reason that a particular guideline should be followed.
The main sources for this paper, apart from our own
experience, are:
.
The Yancey paper already mentioned. Yancey
identifies 10 rules for reading clinical research
results. Many of the rules can also serve as guide-
lines for authors.
.
A paper by Sacks et al. [43] that considers quality
criteria for meta-analyses of randomized controlled
trials. Sacks et al. point out that the quality of papers
included in a meta-analysis is important. In parti-
cular, they suggest considering the quality of
features such as the randomization process, the
statistical analysis, and the handling of withdrawals.
.
A paper on guidelines for contributors to journals by
Altman [1].
.
The guidelines for statistical review of general
papers and clinical trials prepared by the British
Medical Journal. (These guidelines are listed in
Altman et al. [3], chapter 10 of Gardner and
Altman [14], and on the journal's web page:
http://www.bmj.com/advice.)
.
A book by Lang and Secic [28] with guidelines for
reporting medical statistics.
.
The CONSORT statement on reporting the results of
randomized trials in medicine [4]. This statement
has been adopted by 70 medical journals.
.
A paper defining guidelines for reporting results of
statistical analysis in the Japanese Journal of Clinical
Oncology [12]. This paper also discusses common
statistical errors.
.
A paper defining guidelines for the American
Psychological Society [49].
.
Three papers discussing the types of statistical errors
found in medical papers [31], [2], [38].
We have concentrated on medical guidelines because
medical statisticians have been particularly active in
pointing out the poor standards of statistical analysis in
their journals. In addition, we also reviewed the guidelines
of the American Psychological Association. We have
adapted advice from the above sources to the problems of
empirical studies of software engineering phenomena.
Some problems with statistics arise because there are
methodological difficulties applying standard statistical
procedures to software experiments. Nonetheless, the
majority of problems result from lack of statistical expertise
in the empirical research community. Altman suggests the
same is true in medicine [2]. He says ªThe main reason for
the plethora of statistical errors is that the majority of
statistical analyses are performed by people with an
inadequate understanding of statistical methods. They are
then peer reviewed by people who are generally no more
knowledgeable.º Our guidelines consider both types of
problem, but some methodological problems are, as yet,
unsolved. In these cases, we point out the problems, but we
have no ready solutions.
In principle, empirical guidelines can represent the
concerns of many different parties
.
The reader of a published paper.
.
The reviewer of a paper prior to its publication.
.
The authors of a paper.
.
Researchers planning an empirical study.
.
A meta-analyst wanting to combine information
from different studies of the same phenomenon.
.
A journal editorial board.
In addition, empirical guidelines are often specialized to
consider particular types of study e.g., randomized trials,
surveys, exploratory studies. Clearly, the particular require-
ments for a set of guidelines influence their content and
format. In the long term, if the software community accepts
the need for experimental guidelines, we would expect to
find specialized guidelines for different purposes. In this
paper, however, we are concerned with developing guide-
lines to assist researchers to avoid major pitfalls in their
research activities and to report their research correctly.
Some guidelines pertain to particular types of studies but
most are fairly general. We believe that our guidelines will
cover most of the issues of relevance to the researchers. We
cannot claim that the guidelines are necessarily compatible
with all the requirements of other interested parties.
We consider guidelines for what do to and what not to
do under six basic topic areas:
.
Experimental context,
.
Experimental design,
.
Conduct of the experiment and data collection
.
Analysis,
.
Presentation of results, and
.
Interpretation of results.
The experimental guidelines and advice we reviewed
were at varying levels of abstraction. Some appeared to be
metaguidelines identifying the goal of a set of guidelines.
For example, the BMJ General Guidelines say ªSelect a
study design that is appropriate to achieve the study
objectiveº which can be considered a metagoal for all the
design level guidelines. Alternatively, some guidelines are
very detailed. For example, Lang and Secic [28] say ªWhen
reporting percentages, always give the numerators and
denominators of the calculationsº which is more like a
checklist item for a more general guideline ªProvide
appropriate descriptive statistics.º We have tried to ensure
that our guidelines are at a level below metaguidelines,
which are incorporated into the introduction to each set of
guidelines, and above the very detailed level guidelines,
which are incorporated as checklists associated with the
relevant guideline.
722
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 3

2
EXPERIMENTAL CONTEXT
2.1
Introduction
Most medical guidelines have little to say about experi-
mental context. However, we regard experimental context
as extremely important for software engineering research.
Experimental context has three elements:
1.
Background information about the industrial cir-
cumstances in which an empirical study takes place
or in which a new software engineering technique is
developed.
2.
Discussion of the research hypotheses and how they
were derived.
3.
Information about related research.
The main goals of context guidelines are:
1.
To ensure that the objectives of the research are
properly defined
2.
To ensure that the description of the research
provides enough detail for other researchers and
for practitioners.
2.2
Context Guidelines
C1: Be sure to specify as much of the industrial context as
possible. In particular, clearly define the entities, attributes,
and measures that are capturing the contextual information.
Industrial context information is important in two types
of empirical software engineering studies: observational
studies (i.e., in situ studies of industrial practice) and formal
experiments evaluating techniques developed in industry
(e.g., inspections or design patterns). We discuss these
situations below.
2.2.1 Observational Studies
There is an immense variety to be found in development
procedures, organizational culture, and products. This
breadth implies that empirical studies based on observing
or measuring some aspect of software development in a
particular company must report a great deal of contextual
information if any results and their implications are to be
properly understood. Researchers need to identify the
particular factors that might affect the generality and utility
of the conclusions. For example, they may need to identify
factors such as:
1.
The industry in which products are used (e.g., bank-
ing, consumer goods, telecommunications, travel).
2.
The nature of the software development organiza-
tion (e.g., in-house information systems department,
independent software supplier).
3.
The skills and experience of software staff (e.g., with
a language, a method, a tool, an application domain)
4.
The type of software products used (e.g., a design
tool, a compiler)
5.
The software processes being used (e.g., a company-
standard process, the quality assurance procedures,
the configuration management process).
Such information is essential if the same or other
researchers want to replicate a study or include it in a
meta-analysis. Further, if practitioners want to use experi-
mental results, they need to be sure that the results are
applicable in their specific circumstances
Unlike other disciplines, software engineering has no
well-defined standards for determining what contextual
information should be included in the study design,
collected during the study, and reported with the results.
Standard contextual information allows us to compare and
contrast similar studies, and to build a fabric of under-
standing from individual threads of evidence about a tool,
technique or practice. Research guidelines are incomplete,
because identification of standards for reporting research
context requires further research in two areas:
1.
Identification of general confounding factors for
specific types of empirical studies. For example, El-
Emam et al. [10] have demonstrated that size is a
confounding factor when using object-oriented
coupling measures to predict fault-proneness, but
more research is needed to identify other confound-
ing factors for other standard types of experiments
and analyses.
2.
Specification of a taxonomy or an ontology of
context. Kitchenham et al. [23] have suggested an
ontology of software maintenance aimed at defining
factors that need to be reported in empirical studies.
This work identifies a very large number of factors
but does not offer any advice as to which factors are
most important, nor what minimum reporting
requirements should be.
It is important not only to identify appropriate contextual
variables but also to measure them consistently. Again,
software engineering studies suffer from specific problems
because software measurements are not standardized.
Fenton and Pfleeger [11] provide many examples of
product, process, and resource characteristics that are
measured inconsistently across different development and
maintenance organizations. For example, there are multiple
standards for counting function-points, and confusion exists
about what is meant by counting a line of code. Similarly,
several measures purport to measure ªcomplexity,º but it is
not clear what aspect of complexity is being measured;
neither is it clear whether that aspect is being measured
appropriately or consistently. Kitchenham et al. [24] suggest
several ways to help researchers and practitioners focus on
what they mean by entities and attributes and how to define
and measure them more consistently. Still, much work
remains in making sure we mean the same things when we
discuss and measure variables in empirical studies.
2.2.2 Formal Experiments
For formal experiments evaluating techniques developed in
industry (e.g., inspections, or design patterns), we need to
be sure that the versions of the techniques that we evaluate
and the outcome measures we use for testing are not
oversimplified. Unlike techniques developed in academia,
industrial techniques have usually been developed in a rich
complex setting. We need to understand how the technique
works in an industrial setting before we develop an abstract
version for formal experimentation.
Research on inspections illustrates some of the problems
of over-simplification. Many inspection experiments have
concentrated on assessing easily quantifiable benefits and
ignored other types of benefit. In the context of experiments
KITCHENHAM ET AL.: PRELIMINARY GUIDELINES FOR EMPIRICAL RESEARCH IN SOFTWARE ENGINEERING
723
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 4

aimed at optimization, this is a particular problem since
optimization in one dimension can suboptimize overall
performance. For example, some studies have suggested
that inspection meetings are not necessary to maximize
defect detection, the hypothesized synergy of inspection
meetings does not exist [20], [27], [47]. This lack of effect
may be true, but it does not imply that inspection meetings
can be abandoned. We can omit the inspection meetings
only when all other benefits are shown to be illusionary or
unaffected by the meeting process.
Observational studies give a better overview of the full
range of benefits accruing from inspections. For example, a
study by Doolan [9] identified a number of benefits of
inspections other than simple fault detection:
1.
Inspections promote teamwork and are a good
means of developing team spirit in a large group.
2.
Inspections are an excellent means for transferring
technology, especially if key people leave the project.
3.
Inspections provide on-the-job training on stan-
dards, technical material, organizational culture,
and the inspection process itself.
4.
Inspectors can identify root causes of defects.
Siy and Votta [44] conclude that inspections improve the
maintainability of code by identifying ªsoft issuesº such as
making code conform to standards, minimizing redundan-
cies, improving safety and portability, and raising the
quality of the documentation. Each of these benefits makes
the code easier to understand and change. However,
absence of these characteristics would not necessarily be
classified as a defect because each one does not always lead
to a visible, particular failure. Thus, formal experiments
based only on defect counts provide an incomplete picture
of the true costs and benefits.
C2: If a specific hypothesis is being tested, state it clearly prior to
performing the study and discuss the theory from which it is
derived, so that its implications are apparent.
Confirmatory experiments are the foundation of experi-
mental science. They are designed to test formal hypotheses
as rigorously as possible. In particular, hypotheses are
formulated during experimental design prior to the collec-
tion or analysis of any data.
Software engineering researchers are becoming more
familiar with the concept of stating their scientific hypoth-
eses. However, all too often the so-called hypothesis is
simply a statement of the tests to be performed. For
example, if researchers want to know whether there is a
relationship between the cyclomatic number and the
number of faults found in a module, they may state the
null hypothesis as ªthere is no correlation between
cyclomatic number and faults found.º We call this state-
ment a shallow hypothesis because it does not reflect an
underlying, explanatory theory. That is, whatever the result
of the experiment, we will not be increasing our software
engineering knowledge in any significant way. Further-
more, this approach is ultimately sterile since it leads to
experimental results that are not of great interest.
Unfortunately, the inspection and reading literature
offers many examples of shallow hypotheses and unexcit-
ing research. Often, the hypothesis under test is artificial, in
the sense that it is aimed at optimization within a specific
context, rather than testing an aspect of a theory. That is,
there is no well-defined theory about how software
engineers introduce defects into software artifacts, nor
any theory about how they recognize those defects. Even
more important, there is no real theory about why
inspections work, even though there is evidence that they
do. Useful research may flow solely from empirical
observations. For example, the development of the small-
pox vaccination by Edward Jenner was based solely on the
observation that women who had had cowpox did not
catch smallpox [15]. However, Jenner succeeded because
there was an underlying cause-effect relationship, even
though current medical research had not yet discovered it.
Unfortunately, empirical studies of software engineering
phenomena are often contradictory. Without any under-
lying theories, we cannot understand the reason why
empirical studies are inconsistent. When we do have
consistent results, as in the case of inspections, we cannot
be sure how to improve or optimize the result if we do not
understand why the phenomenon occurs.
Other scientific disciplines search for a deep hypothesis
that arises from an underlying theory, so that testing the
hypothesis tests the validity of the theory. For example,
rather than merely documenting a relationship between
cyclomatic number and faults found, we can use theories of
cognition and problem-solving to help us understand the
effects of complexity on software. Vinter et al. [46] provide a
good example of deriving hypothesis from theory in their
work, concerned with assessing the effectiveness of formal
methods. Vinter et al. investigated the logical errors made
by experienced software engineers (who knew their
performance was being tested) and compared their results
with cognitive psychology studies of reasoning errors found
in the general population. They found many similarities in
the errors made by software engineers and the general
population. The importance of their research is that it
considered the claims made for formalisms in terms of the
psychological assumptions underpinning those claims.
Without the link from theory to hypothesis, empirical
results cannot contribute to a wider body of knowledge.
C3: If the research is exploratory, state clearly and, prior to data
analysis, what questions the investigation is intended to
address and how it will address them.
There is always a tension between gaining the maximum
value from an experiment by performing many subsidiary
analyses to look for areas for future research and having the
most convincing experimental results by concentrating on a
single purpose confirmatory study. Many researchers will
perform a complex study to investigate multiple hypoth-
eses, but they emphasize only the results that bear on the
primary hypothesis. The other analyses act as prestudies
that allow them to formulate further hypotheses to be tested
in subsequent experiments. Such prestudies can also ensure
that the researchers have sufficient information to plan
future experiments better, by predicting the number of
experimental subjects needed and the expected power of
the test.
Thus, exploratory studies are an important mechanism
for generating hypotheses and guiding further research
724
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 5

activities. However, if researchers apply extensive statistical
analyses to exploratory studies, the analyses may suffer
from methodological problems:
1.
Too many tests. Researchers may perform so many
tests that a large number of statistically significant
results occur by chance.
2.
Fishing for results. Researchers may trawl all
possible combinations and subsets of the data,
however unlikely, in order to find statistically
significant results.
We present analysis guidelines later that help to avoid these
problems, but the starting point is to define the research
questions in advance.
Defining research questions in advance addresses an-
other major problem with exploratory analysis, which is the
temptation to undertake too many research activities in a
single study. For example, Ropponen and Lyytinen [40]
surveyed project managers about their experiences of
various risk factors. They performed principal component
analysis on the results and interpreted the six largest
principal components as identifying components of project
risk. In effect, they had generated hypotheses about the
nature of risk component from their analysis. They did not
report that it was now necessary to perform a second
independent survey to test their hypotheses. In fact, they
used the principal components in further exploratory
correlation studies to identify strategies for managing those
components. Furthermore, they attempted to validate the
survey instrument using the same data set. They derived
Cronbach alpha statistics, which measure the agreement
among respondents to questions that address the same
topic [7], using the risk components identified by the
principal component analysis. They found high values and
concluded that they had validated their survey instrument.
However, one would expect the Cronbach alpha values to
be high because they measure structure known to be
present in the data.
C4: Describe research that is similar to, or has a bearing on, the
current research and how current work relates to it.
The relationship between the current research activity
and other research should be defined, so that researchers
can combine to build an integrated body of knowledge
about software engineering phenomena.
3
EXPERIMENTAL DESIGN
3.1
Introduction
The study design describes the products, resources and
processes involved in the study, including:
.
the population being studied,
.
the rationale and technique for sampling from that
population,
.
the process for allocating and administering the
treatments (the term ªinterventionº is often used as
an alternative to treatment), and
.
the methods used to reduce bias and determine
sample size.
The overall goal of experimental design is to ensure that
the design is appropriate for the objectives of the study.
The following design guidelines are intended to indicate
what you need to consider when selecting an experi-
mental design.
3.2
Design Guidelines
D1: Identify the population from which the subjects and objects
are drawn.
If you cannot define the population from which your
subject/objects are drawn, it is not possible to draw any
inferences from the results of your experiment. This seems
to be a particular problem for software engineering surveys.
For example, Lethbridge [29] reports a survey where
participants were recruited ªby directly approaching
companies and by advertising on the internet.º He states
that ªThe sample appears to be a balanced coverage of a
wide spectrum of software professionals, with a bias
towards North AmericaÐand possibly towards those who
were interested enough to take the time to participate.º
However, the absence of a scientific sampling method
means that the results cannot be generalized to any defined
population.
Lethbridge's survey can be contrasted with a much more
rigorous definition of the population and sampling method
given by Ropponen and Lyytinen [40]. They stated ªWe
collected a representative data set using a survey instru-
ment by mailing the developed questionnaire to a selected
sample of the members of the Finnish Information Proces-
sing Association (1991) whose job title was project manager
or equivalent. In order to avoid bias, we sent the
questionnaire to at most two persons in one company.º
D2: Define the process by which the subjects and objects were
selected.
The subjects and objects must be representative of the
population or you cannot draw any conclusions from the
results of your experiment. The most convincing way of
obtaining subjects is by random sampling. If a random
sample has been obtained, the method of selection should
be specified. If the method of selection was not random, it
should be explained and you must justify that the sampling
method still permits the results of the experiment to
generalize to the population of interest.
It is often necessary to define inclusion criteria and
exclusion criteria. These are used to identify subjects who
will or will not be candidates for participation in the
experiment. For example, in software experiments, re-
searchers often use student subjects. In such circumstances,
they might choose to exclude any mature students with
previous computing experience in order to make sure the
participants in the study all have comparable experience.
D3: Define the process by which subjects and objects are assigned
to treatments.
Subject/objects should be allocated to treatments in an
unbiased manner or the experiment will be compromised. It
is customary to allocate subjects/objects to treatments by
randomization. However, researchers often have small
samples in software experiments and simple randomization
does not always lead to unbiased allocation nor to equal
sample sizes. For example, you might find, by chance, that
the two most able subjects are assigned to one treatment and
KITCHENHAM ET AL.: PRELIMINARY GUIDELINES FOR EMPIRICAL RESEARCH IN SOFTWARE ENGINEERING
725
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 6

the two least able to another treatment. In such circum-
stances, a more complex randomization process may be
necessary (see, for example, [35], chapter 5), a nonrando-
mized study may be appropriate [16], or some posttrial
adjustment may be necessary to deal with biased groups.
If you decide to use more complex designs or non-
randomized designs, you need to be aware that complex or
nonstandard designs may be more difficult to analyze and
interpret (see D4).
Wilkinson et al. [49] point out that random assignment is
sometimes not feasible. In such cases, you need to be
particularly careful to identify and control or measure
confounding factors and other sources of bias. You must
also prepare plans to minimize dropouts and noncompli-
ance with the study protocol and to cope with missing data.
If you intend to perform some post-trial adjustment, you
should:
1.
Specify how you intend to detect the presence of
bias. Such specification usually involves confirming
whether the subjects in each of the treatment groups
are similar with respect to various characteristics of
importance. For example, report whether subjects
have similar educational background, or the treat-
ment groups have a similar ratio of male and female
subjects.
2.
Specify how any bias will be handled during the
analysis. For example, to avoid possible bias due to
missing values, you may decide to use imputation
methods (i.e., methods of replacing missing values
with estimated values, see for example [30]).
D4: Restrict yourself to simple study designs or, at least, to
designs that are fully analyzed in the statistical literature. If
you are not using a well-documented design and analysis
method, you should consult a statistician to see whether yours
is the most effective design for what you want to accomplish.
If you attempt to address the problem of small sample
sizes by using more complex designs, you must be sure that
you understand all the implications of the selected design.
Before developing a new type of experimental design, you
should consult an expert. Researchers can easily make
mistakes if they attempt to create new designs on their own.
In particular,
1.
They can produce nested designs where the experi-
mental unit is a group of subjects rather than the
individual subject and not realize that this radically
changes the nature of the experiment and how it
should be analyzed. For example, suppose a
researcher in a university wanted to investigate
two different methods of testing. Suppose (s)he has
four separate tutorial groups each of 10 students. If
(s)he assigned each student at random to one of the
testing methods, (s)he would have 38 degrees of
freedom to test differences between the testing
methods. If (s)he assigned each tutorial group as a
whole to one of the testing methods, (s)he would
have only two degrees of freedom to test any
differences between the methods. (In general, the
more degrees of freedom, the better the experiment.)
2.
They can devise a very complex design that they do
not know how to analyze properly. For example,
researchers often use cross-over designs to reduce
the problem of small sample sizes. In cross-over
designs, one experimental unit (team or person) is
subjected to several different treatments. However,
the cross-over design may have learning or matura-
tion effects (referred to as carryover effects); that is,
participation with the first treatment may influence
the outcome of the second treatment. For example, a
second attempt at debugging or inspection might be
easier than the first, regardless of the technique
being used. To avoid learning bias, the order in
which subjects perform tasks must be randomized or
balanced by blocking. Cross-over designs with
blocking are more difficult to analyze correctly than
researchers may expect (see [33], chapter 32). For
instance, when Porter and Johnson [36] reported on
two cross-over experiments, the analysis of the first
experiment used the Wilcoxon signed rank test.
However, this analysis technique cannot be used to
analyze a cross-over design of the complexity used
in the experiment.
D5: Define the experimental unit.
In order to reduce the chance of mistaking the size of
experimental unit, identify the experimental unit explicitly
when defining your randomization procedure.
Surveys often make mistakes with the experimental unit
when questionnaires are sent to multiple respondents in an
organization, but the questions concern the organization as
a whole. In this case, the unit of observation is the
individual, but the experimental unit is the organization.
If this problem is not recognized, the total sample size will
be incorrectly inflated and the chance of a significant result
unfairly increased.
D6: For formal experiments, perform a pre-experiment or
precalculation to identify or estimate the minimum required
sample size.
The sample size determines the probability of finding a
difference (by rejecting the null hypothesis) when one
exists. For a well-conducted confirmatory experiment,
researchers are expected to have information about the
expected size of the difference between treatment effects
and the variance of the experimental units. From such
information, you can calculate the number of subjects (or
more correctly, experimental units) required to have a given
probability of rejecting the null hypothesis when it is false.
This probability is called the power of the test and it is
customary to design for a power of at least 0.8. (For more
information on sample sizes and appropriate tests, see [5].)
D7: Use appropriate levels of blinding.
Medical researchers use double-blind experiments to
prevent the participants' expectations (both researchers and
subjects) from influencing the study's results. However, it is
impossible for participants in a software engineering study
not to be aware of the technology they are using. So, it is
clear that any expectations about that technology, positive
or negative, will influence the study's outcome. For
example, the extensive media coverage of the claimed
726
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 7

superiority of object-oriented methods suggests that a
comparison of object-oriented and structured methods is
likely to be biased.
However, several types of blinding are possible in
software engineering experiments:
1.
Blind allocation of materials. This simply means that
the procedure for assigning subjects to treatment
groups is separate from the process by which
subjects are given any of the materials they will use
during the experiment. In software engineering
experiments, allocation of subjects and materials
can be computerized, thus minimizing the interac-
tion between subjects and researchers during the
experiment.
2.
Blind marking. Some experimental outcomes are
answers to questions that need to be assessed for
correctness. If the format of the experimental out-
comes is not influenced by the treatment, it is
sensible for the scripts to be coded prior to being
marked, so the markers cannot tell to which subject
or to which treatment group a particular outcome
script belongs. For example, if the experiment is
concerned with comparing testing methods, and
subjects are asked to identify defects in a program,
the result of the experiment would be a list of
identified defects. The format of the answer would
not indicate which testing method had been used, so
blind marking would be appropriate.
3.
Blind analysis (see A2). For blind analysis, the
treatments are coded, and the analyst does not know
which treatment group is which. Some statisticians
believe blind analysis is an effective counter to the
problem of fishing for results.
D8: If you cannot avoid evaluating your own work, then make
explicit any vested interests (including your sources of
support) and report what you have done to minimize bias.
Since it is impossible to use double-blinding in software
engineering experiments, it is extremely difficult to evaluate
any research in which you have a vested interest. For
example, if the researchers have themselves created or
implemented one of the technologies under evaluation, or if
they are champions of a competing technology, there is a
strong possibility that their enthusiasm for their own work
will bias the trial. Thus, although researchers have a
responsibility to identify the hypotheses implicit in their
research and provide some preliminary validation of their
results, they are not the best people to perform objective,
rigorous evaluations of their own technologies. The only
direct (but partial) solution to this problem is to employ
independent, impartial assessors, taking care to monitor
their biases, too. Rosenthal [41] addresses these problems at
length and describes several approaches to mitigate experi-
menter effects.
D9: Avoid the use of controls unless you are sure the control
situation can be unambiguously defined.
For software experiments, controls are difficult to define
because software engineering tasks depend on human
skills. Usually, there is no common default technology
(i.e., method or procedure or tool) for performing a task
against which a new method, procedure, or tool can be
compared. That is, we cannot ask one group to use a new
design technique and the other to use no design technique.
At best, our empirical studies within a particular company
can use its standard or current practice as the basis for
evaluating a new technology. However, this situation
allows us to compare the new technology only with a
baseline (i.e., the current industrial practice), not with a
defined control. Thus, studies of a new technology in
different companies or organizations are difficult to
compare because it is highly unlikely that the baselines
are the same. For laboratory studies, we can compare two
defined technologies, one against the other, but it is usually
not valid to compare using a technology with not using it.
D10: Fully define all treatments (interventions).
Treatments must be properly defined if experiments are
to be replicated and/or their results are to be taken up by
industry.
In addition, if we define treatments properly, we can
study the same treatment or technique in different
organizations. For example, several organizations could
collaborate to agree on a common protocol. Such an
approach might make it possible to get a better handle on
the organization effects as well as the comparison of
variables of interest.
D11: Justify the choice of outcome measures in terms of their
relevance to the objectives of the empirical study.
You must justify that outcome measures are relevant to
the objectives of the study to confirm that the design is
appropriate to meet the study objectives. The choice of
outcome measures is particularly important when they are
surrogate measures. For example, researchers wanting to
investigate the amount of maintenance effort directed to
individual components sometimes count the number of
lines of code changed instead of measuring the time
software maintainers spend on their maintenance tasks.
However, the number of line of code changed is a poor
surrogate for maintenance effort and its use in place of task
effort should be justified. Inability to measure task effort is
not a justification; it is an excuse.
4
CONDUCTING THE EXPERIMENT AND
DATA COLLECTION
4.1
Introduction
The process of conducting an experiment involves collect-
ing the experimental outcome measures. This is a particular
problem for software experiments because our measures
are not standardized. Thus, one goal of the data collection
guidelines is to ensure that we have defined our data
collection process well enough for our experiment to be
replicated.
In addition, we need to monitor and record any
deviations from our experimental plans. This includes
monitoring all dropouts in experiments and nonresponse
in surveys.
4.2
Data Collection Guidelines
DC1: Define all software measures fully, including the entity,
attribute, unit and counting rules.
KITCHENHAM ET AL.: PRELIMINARY GUIDELINES FOR EMPIRICAL RESEARCH IN SOFTWARE ENGINEERING
727
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 8

For empirical software studies, data collection is proble-
matic, in part because, as noted above, software measures
are not well-defined. Kitchenham et al. [22] discuss many of
the problems with data collection; they suggest several
standards for defining and using software measures. From
the perspectives of design and data collection, the non-
standard nature of software measures makes it difficult for
researchers to replicate studies or to perform meta-analysis
of studies of the same phenomenon. That is, without clear
standards, we can never be sure that we are measuring the
same things or measuring them in the same way. This lack
of standards does not mean that everyone should always
define and use the same measures. Rather, it means that we
need to define measures carefully enough so that we can
understand the differences in measurement and, thus, can
determine whether we can translate from one measurement
scheme to another. For example, it is fine for some
researchers or practitioners to measure effort in hours,
while others measure it in days; we know how to convert
from the one to the other.
DC2: For subjective measures, present a measure of interrater
agreement, such as the kappa statistic or the intraclass
correlation coefficient for continuous measures.
If measures are subjective, the skill and bias of the person
determining the measure can affect the results. Empirical
studies should discuss the methods used to ensure that
measurement is correct and consistent. For data collected by
questionnaires, it is necessary to report measures of validity
and reliability and other qualities affecting conclusions [49].
For example, researchers have performed studies to in-
vestigate the interrater agreement among SPICE model
assessors [13].
DC3: Describe any quality control method used to ensure
completeness and accuracy of data collection.
In order to provide evidence that data collection has been
undertaken in an appropriate manner, it is useful to define
and report quality control procedures to support the data
collection process.
DC4: For surveys, monitor and report the response rate and
discuss the representativeness of the responses and the impact
of nonresponse.
For surveys, it is important to determine the response
rate, but it is even more critical to ensure that the
nonresponders have not biased the results. It is sometimes
possible to sample the nonresponders in order to determine
reasons for nonresponse. For example, Ropponen and
Lyytinen [40] phoned a random sample of nonrespondents
to investigate the reasons why they had not responded.
Otherwise, demographic information can be used to justify
the representativeness of the responses.
DC5: For observational studies and experiments, record data
about subjects who drop out from the studies.
Often, subjects who begin a study drop out before the
study is complete. For example, a subject may be reassigned
to another project, may leave the company, or may refuse to
continue to participate. Such situations must be reported
carefully in any paper describing the study. It is important
to be sure that the dropouts have not biased your results.
For example, if all those who dropped out were the most
familiar with the baseline technology, then you cannot truly
understand the effects of any new technology being
evaluated. One means of determining whether or not
dropouts have caused systematic bias is to compare
dropouts with other subjects on the basis of characteristics
such as experience, age, and any preliminary measures
available.
Another common example found when undertaking
observational studies in industry is that some projects are
abandoned before completion. It is important to consider
whether incomplete projects will bias any subsequent
analysis. This is a particular problem for cost estimation
studies, where data about completed projects is used to
construct cost models. If a cost model is conditional upon
project completion, it has some problems when used to
predict costs for a new project. An estimate from a
statistically-based cost model is usually assumed to have
an implied probability of being achieved (often 0.5 if the
model predicts the most likely value). However, if the
model has ignored the chance of a project being abandoned
before completion, the implied probability will be an
overestimate.
DC6: For observational studies and experiments, record data
about other performance measures that may be affected by the
treatment, even if they are not the main focus of the study.
In medical pharmaceutical studies, it is important to
record all adverse effects of drugs under test. In software
engineering, many of our outcome measures (defect rates,
productivity, lead time) are related to each other. Thus, if
our main interest is in whether a development method
decreases lead time, it may still be important to investigate
whether it has adverse or beneficial effects on productivity
or defect rates.
5
ANALYSIS
5.1
Introduction
There are two main approaches to analyzing experimental
results:
1.
Classical analysis (often referred to as the ªfrequen-
tistº approach). This approach is adopted by most
statistical packages.
2.
Bayesian analysis. This approach provides a sys-
tematic means of making use of ªprior information.º
Prior information may be obtained from previous
studies of the phenomenon of interest or from expert
opinion.
Our guidelines are independent of the choice of statistical
approach. However, Bayesian methods are not usually used
in software engineering studies; so, if you decide to adopt a
Bayesian approach, you should consult a statistician.
Another fairly general issue is the choice between
parametric and nonparametric analysis. If the distribution
of variables can be identified, appropriate parametric tests
will be more powerful than nonparametric tests. However,
if the distribution of variables is unknown, nonparametric
methods are usually more appropriate; most are very
efficient relative to their parametric counterparts and they
are effective with small sample sizes.
728
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


