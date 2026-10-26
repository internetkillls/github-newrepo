# Guidelines for Conducting and Reporting Case Study Research in Software Engineering

Source ID: C07
Authors: Per Runeson; Martin Höst
Source URL: https://link.springer.com/content/pdf/10.1007/s10664-008-9102-8.pdf
DOI: 10.1007/s10664-008-9102-8
Identity: Empirical Software Engineering 14(2), 2009, pp. 131–164; online December 2008. Publisher open-access PDF. See the license clause in the PDF.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 1

Guidelines for conducting and reporting case study
research in software engineering
Per Runeson & Martin Höst
Published online: 19 December 2008
# The Author(s) 2008. This article is published with open access at Springerlink.com
Editor: Dag Sjoberg
Abstract Case study is a suitable research methodology for software engineering research
since it studies contemporary phenomena in its natural context. However, the understanding
of what constitutes a case study varies, and hence the quality of the resulting studies. This
paper aims at providing an introduction to case study methodology and guidelines for
researchers conducting case studies and readers studying reports of such studies. The
content is based on the authors’ own experience from conducting and reading case studies.
The terminology and guidelines are compiled from different methodology handbooks in
other research domains, in particular social science and information systems, and adapted to
the needs in software engineering. We present recommended practices for software
engineering case studies as well as empirically derived and evaluated checklists for
researchers and readers of case study research.
Keywords Case study. Research methodology. Checklists . Guidelines
1 Introduction
The acceptance of empirical studies in software engineering and their contributions to
increasing knowledge is continuously growing. The analytical research paradigm is not
sufficient for investigating complex real life issues, involving humans and their interactions
with technology. However, the overall share of empirical studies is negligibly small in
computer science research; Sjøberg et al. (2005), found 103 experiments in 5,453 articles
Ramesh et al. (2004) and identified less than 2% experiments with human subjects, and
only 0.16% field studies among 628 articles. Further, existing work on empirical research
Empir Software Eng (2009) 14:131–164
DOI 10.1007/s10664-008-9102-8
P. Runeson (*): M. Höst
Department Computer Science, Lund University, Box 118, SE-221 00 Lund, Sweden
e-mail: per.runeson@cs.lth.se
M. Höst
e-mail: martin.host@cs.lth.se


## PDF page 2

methodology in software engineering has a strong focus on experimental research; the
earliest by Moher and Schneider (1981), Basili et al. (1986), the first methodology
handbook by Wohlin et al. (2000), and promoted by Tichy (1998). All have a tendency
towards quantitative approaches, although also qualitative approaches are discussed during
the later years, e.g. by Seaman (1999). There exist guidelines for experiments’ conduct
(Kitchenham et al. 2002; Wohlin et al. 2000) and reporting (Jedlitschka and Pfahl 2005),
measurements (Basili and Weiss 1984; Fenton and Pfleeger 1996; van Solingen and
Berghout 1999), and systematic reviews (Kitchenham 2007), while only little is written on
case studies in software engineering (Höst and Runeson 2007; Kitchenham et al. 1995;
Wohlin et al. 2003) and qualitative methods (Dittrich 2007; Seaman 1999; Sim et al. 2001).
Recently, a comprehensive view of empirical research issues for software engineering has
been presented, edited by Shull et al. (2008).
The term “case study” appears every now and then in the title of software engineering
research papers. However, the presented studies range from very ambitious and well
organized studies in the field, to small toy examples that claim to be case studies.
Additionally, there are different taxonomies used to classify research. The term case study is
used in parallel with terms like field study and observational study, each focusing on a
particular aspect of the research methodology. For example, Lethbridge et al. use field
studies as the most general term (Lethbridge et al. 2005), while Easterbrook et al. (2008)
call case studies one of five “classes of research methods”. Zelkowitz and Wallace propose
a terminology that is somewhat different from what is used in other fields, and categorize
project monitoring, case study and field study as observational methods (Zelkowitz and
Wallace 1998). This plethora of terms causes confusion and problems when trying to
aggregate multiple empirical studies.
The case study methodology is well suited for many kinds of software engineering
research, as the objects of study are contemporary phenomena, which are hard to study in
isolation. Case studies do not generate the same results on e.g. causal relationships as
controlled experiments do, but they provide deeper understanding of the phenomena under
study. As they are different from analytical and controlled empirical studies, case studies
have been criticized for being of less value, impossible to generalize from, being biased by
researchers etc. This critique can be met by applying proper research methodology practices
as well as reconsidering that knowledge is more than statistical significance (Flyvbjerg
2007; Lee 1989). However, the research community has to learn more about the case study
methodology in order to review and judge it properly.
Case study methodology handbooks are superfluously available in e.g. social sciences
(Robson 2002; Stake 1995; Yin 2003) which literature also has been used in software
engineering. In the field of information systems (IS) research, the case study methodology
is also much more mature than in software engineering. For example, Benbasat et al.
provide a brief overview of case study research in information systems (Benbasat et al.
1987), Lee analyzes case studies from a positivistic perspective (Lee 1989) and Klein and
Myers do the same from an interpretive perspective (Klein and Myers 1999).
It is relevant to raise the question: what is specific for software engineering that
motivates specialized research methodology? In addition to the specifics of the examples,
the characteristics of software engineering objects of study are different from social science
and also to some extent from information systems. The study objects are 1) private
corporations or units of public agencies developing software rather than public agencies or
private corporations using software systems; 2) project oriented rather than line or function
132
Empir Software Eng (2009) 14:131–164


## PDF page 3

oriented; and 3) the studied work is advanced engineering work conducted by highly
educated people rather than routine work. Additionally, the software engineering research
community has a pragmatic and result-oriented view on research methodology, rather than a
philosophical stand, as noticed by Seaman (1999).
The purpose of this paper is to provide guidance for the researcher conducting case
studies, for reviewers of case study manuscripts and for readers of case study papers. It is
synthesized from general methodology handbooks, mainly from the social science field, as
well as literature from the information systems field, and adapted to software engineering
needs. Existing literature on software engineering case studies is of course included as well.
The underlying analysis is done by structuring the information according to a general case
study research process (presented in Section 2.4). Where different recommendations or
terms appear, the ones considered most suited for the software engineering domain are
selected, based on the authors’ experience on conducting case studies and reading case
study reports. Links to data sources are given by regular references. Specifically, checklists
for researchers and readers are derived through a systematic analysis of existing checklists
(Höst and Runeson 2007), and later evaluated by PhD students as well as by members of
the International Software Engineering Research Network and updated accordingly.
This paper does not provide absolute statements for what is considered a “good” case
study in software engineering. Rather it focuses on a set of issues that all contribute to the
quality of the research. The minimum requirement for each issue must be judged in its
context, and will most probably evolve over time. This is similar to the principles by Klein
and Myers for IS case studies (Klein and Myers 1999), “it is incumbent upon authors,
reviewers, and exercise their judgment and discretion in deciding whether, how and which
of the principles should be applied”. We do neither assess the current status of case study
research in software engineering. This is worth a study on its own, similar to the systematic
review on experiments by Sjøberg et al. (2005). Further, examples are used both to illustrate
good practices and lack thereof.
This paper is outlined as follows. We first define a set of terms in the field of
empirical research, which we use throughout the paper (Section 2.1), set case study
research into the context of other research methodologies (Section 2.2) and discuss the
motivations for software engineering case studies (Section 2.3). We define a case study
research process (Section 2.4) and terminology (Section 2.5), which are used for the rest
of the paper. Section 3 discusses the design of a case study and planning for data collection.
Section 4 describes the process of data collection. In Section 5 issues on data analysis are
treated, and reporting is discussed in Section 6. Section 7 discusses reading and reviewing
case study report, and Section 8 summarizes the paper. Checklists for conducting and reading
case study research are linked to each step in the case study process, and summarized in the
Appendix.
Throughout the paper, we use three different case study examples to illustrate the methods. The examples are
selected from the authors’ publications, representing a variety of approaches within case study research.
They illustrate solutions or identify problems in case study research, i.e. are not always compliant with the
guidelines in this paper. The examples are presented in a format like this and they are denoted study XP, RE
and QA after their research area on agile methods (extreme programming), requirements engineering
and quality assurance, respectively. More information about the studies can be found in the original
publications (Karlström and Runeson 2005; 2006) (XP), (Regnell et al. 2001) (RE), and (Andersson and
Runeson 2007a, b) (QA).
Empir Software Eng (2009) 14:131–164
133


## PDF page 4

2 Background and Definition of Concepts
2.1 Research Methodology
In order to set the scope for the type of empirical studies we address in this paper, we put
case studies into the context of other research methodologies and refer to general definitions
of the term case study according to Robson (2002), Yin (2003) and Benbasat et al. (1987)
respectively.
The three definitions agree on that case study is an empirical method aimed at
investigating contemporary phenomena in their context. Robson calls it a research strategy
and stresses the use of multiple sources of evidence, Yin denotes it an inquiry and remarks
that the boundary between the phenomenon and its context may be unclear, while Benbasat
et al. make the definitions somewhat more specific, mentioning information gathering from
few entities (people, groups, organizations), and the lack of experimental control.
There are three other major research methodologies which are related to case studies:
&
Survey, which is the “collection of standardized information from a specific population,
or some sample from one, usually, but not necessarily by means of a questionnaire or
interview” (Robson 2002).
&
Experiment, or controlled experiment, which is characterized by “measuring the effects
of manipulating one variable on another variable” (Robson 2002) and that “subjects are
assigned to treatments by random.”(Wohlin et al. 2000). Quasi-experiments are similar
to controlled experiments, except that subjects are not randomly assigned to treatments.
Quasi-experiments conducted in an industry setting may have many characteristics in
common with case studies.
&
Action research, with its purpose to “influence or change some aspect of whatever
is the focus of the research” (Robson 2002), is closely related to case study. More
strictly, a case study is purely observational while action research is focused on and
involved in the change process. In software process improvement (Dittrich et al. 2008;
Iversen et al. 2004) and technology transfer studies (Gorschek et al. 2006), the
research method should be characterized as action research. However, when studying
the effects of a change, e.g. in pre- and post-event studies, we classify the
methodology as case study. In IS, where action research is widely used, there is a
discussion on finding the balance between action and research, see e.g. (Avison et al.
2001; Baskerville and Wood-Harper 1996). For the research part of action research,
these guidelines apply as well.
Easterbrook et al. (2008) also count ethnographic studies among the major research
methodologies. We prefer to consider ethnographic studies as a specialized type of case
studies with focus on cultural practices (Easterbrook et al. 2008) or long duration studies
with large amounts of participant-observer data (Klein and Myers 1999). Zelkowitz and
Wallace define four different “observational methods” in software engineering (Zelkowitz
and Wallace 1998); project monitoring, case study, assertion and field study. Our guidelines
apply to all these, except assertion which is not considered a proper research method. In
general, the borderline between the types of study is not always distinct. We prefer to see
project monitoring as a part of a case study and field studies as multiple case studies.
Robson summarizes his view, which seems functional in software engineering as well:
“Many flexible design studies, although not explicitly labeled as such, can be usefully
viewed as case studies.” (Robson 2002) p 185.
134
Empir Software Eng (2009) 14:131–164


## PDF page 5

Finally, a case study may contain elements of other research methods, e.g. a survey may
be conducted within a case study, literature search often precede a case study and archival
analyses may be a part of its data collection. Ethnographic methods, like interviews and
observations are mostly used for data collection in case studies.
2.2 Characteristics of Research Methodologies
Different research methodologies serve different purposes; one type of research
methodology does not fit all purposes. We distinguish between four types of purposes for
research based on Robson’s (2002) classification:
&
Exploratory—finding out what is happening, seeking new insights and generating ideas
and hypotheses for new research.
&
Descriptive—portraying a situation or phenomenon.
&
Explanatory—seeking an explanation of a situation or a problem, mostly but not
necessary in the form of a causal relationship.1
&
Improving—trying to improve a certain aspect of the studied phenomenon.2
Case study methodology was originally used primarily for exploratory purposes, and
some researchers still limit case studies for this purpose, as discussed by Flyvbjerg (2007).
However, it is also used for descriptive purposes, if the generality of the situation or
phenomenon is of secondary importance. Case studies may be used for explanatory
purposes, e.g. in interrupted time series design (pre- and post-event studies) although the
isolation of factors may be a problem. This involves testing of existing theories in
confirmatory studies. Finally, as indicated above, case studies in the software engineering
discipline often take an improvement approach, similar to action research; see e.g. the QA
study (Andersson and Runeson 2007b).
Klein and Myers define three types of case study depending on the research perspective,
positivist, critical and interpretive (Klein and Myers 1999). A positivist case study searches
evidence for formal propositions, measures variables, tests hypotheses and draws inferences
from a sample to a stated population, i.e. is close to the natural science research model (Lee
1989) and related to Robson’s explanatory category. A critical case study aims at social
critique and at being emancipatory, i.e. identifying different forms of social, cultural and
political domination that may hinder human ability. Improving case studies may have a
character of being critical. An interpretive case study attempts to understand phenomena
through the participants’ interpretation of their context, which is similar to Robson’s
exploratory and descriptive types. Software engineering case studies tend to lean towards a
positivist perspective, especially for explanatory type studies.
Conducting research on real world issues implies a trade-off between level of control
and degree of realism. The realistic situation is often complex and non-deterministic, which
hinders the understanding of what is happening, especially for studies with explanatory
purposes. On the other hand, increasing the control reduces the degree of realism,
sometimes leading to the real influential factors being set outside the scope of the study.
1 Easterbrook et al. distinguish between exploratory and confirmatory case studies. We interpret Robson’s
explanatory category being closely related to Easterbrook’s confirmatory category.
2 Robson denotes this category “emancipatory” in the social science context, while improvement is our
adaptation to an engineering context.
Empir Software Eng (2009) 14:131–164
135


## PDF page 6

Case studies are by definition conducted in real world settings, and thus have a high degree
of realism, mostly at the expense of the level of control.
The data collected in an empirical study may be quantitative or qualitative. Quantitative
data involves numbers and classes, while qualitative data involves words, descriptions,
pictures, diagrams etc. Quantitative data is analyzed using statistics, while qualitative data is
analyzed using categorization and sorting. Case studies tend mostly to be based on qualitative
data, as these provide a richer and deeper description. However, a combination of qualitative
and quantitative data often provides better understanding of the studied phenomenon
(Seaman 1999), i.e. what is sometimes called “mixed methods” (Robson 2002).
The research process may be characterized as fixed or flexible according to Anastas and
MacDonald (1994) and Robson (2002). In a fixed design process, all parameters are defined at
the launch of the study, while in a flexible design process key parameters of the study may be
changed during the course of the study. Case studies are typically flexible design studies, while
experiments and surveys are fixed design studies. Other literature use the terms quantitative
and qualitative design studies, for fixed and flexible design studies respectively. We prefer to
adhere to the fixed/flexible terminology since it reduces the risk for confusion that a study with
qualitative design may collect both qualitative and quantitative data. Otherwise it may be
unclear whether the term qualitative refers to the data or the design of the study,
Triangulation is important to increase the precision of empirical research. Triangulation
means taking different angles towards the studied object and thus providing a broader
picture. The need for triangulation is obvious when relying primarily on qualitative data,
which is broader and richer, but less precise than quantitative data. However, it is relevant
also for quantitative data, e.g. to compensate for measurement or modeling errors. Four
different types of triangulation may be applied (Stake 1995):
&
Data (source) triangulation—using more than one data source or collecting the same
data at different occasions.
&
Observer triangulation—using more than one observer in the study.
&
Methodological triangulation—combining different types of data collection methods,
e.g. qualitative and quantitative methods.
&
Theory triangulation—using alternative theories or viewpoints.
Table 1 shows an overview of the primary characteristics of the above discussed research
methodologies
Yin adds specifically to the characteristics of a case study that it (Yin 2003):
&
“copes with the technically distinctive situation in which there will be many more
variables than data points, and as one result
&
relies on multiple sources of evidence, with data needing to converge in a triangulating
fashion, and as another result
&
benefits from the prior development of theoretical propositions to guide data collection
and analysis.”
Table 1 Overview of research methodology characteristics
Methodology
Primary objective
Primary data
Design
Survey
Descriptive
Quantitative
Fixed
Case study
Exploratory
Qualitative
Flexible
Experiment
Explanatory
Quantitative
Fixed
Action research
Improving
Qualitative
Flexible
136
Empir Software Eng (2009) 14:131–164


## PDF page 7

Hence, a case study will never provide conclusions with statistical significance. On the
contrary, many different kinds of evidence, figures, statements, documents, are linked
together to support a strong and relevant conclusion.
Perry et al. define similar criteria for a case study (Perry et al. 2005). It is expected that a
case study:
&
“Has research questions set out from the beginning of the study
&
Data is collected in a planned and consistent manner
&
Inferences are made from the data to answer the research question
&
Explores a phenomenon, or produces an explanation, description, or causal analysis of it
&
Threats to validity are addressed in a systematic way.”
In summary, the key characteristics of a case study are that 1) it is of flexible type, coping with
the complex and dynamic characteristics of real world phenomena, like software engineering, 2)
its conclusions are based on a clear chain of evidence, whether qualitative or quantitative,
collected from multiple sources in a planned and consistent manner, and 3) it adds to existing
knowledge by being based on previously established theory, if such exist, or by building theory.
2.3 Why Case Studies in Software Engineering?
Case studies are commonly used in areas like psychology, sociology, political science,
social work, business, and community planning (e.g. Yin 2003). In these areas case studies
are conducted with objectives to increase knowledge about individuals, groups, and
organizations, and about social, political, and related phenomena. It is therefore reasonable
to compare the area of software engineering to those areas where case study research is
common, and to compare the research objectives in software engineering to the objectives
of case study research in other areas.
The area of software engineering involves development, operation, and maintenance of
software and related artifacts, e.g. (Jedlitschka and Pfahl 2005). Research on software
engineering is to a large extent aimed at investigating how this development, operation, and
maintenance are conducted by software engineers and other stakeholders under different
conditions. Software development is carried out by individuals, groups and organizations,
and social and political questions are of importance for this development. That is, software
engineering is a multidisciplinary area involving areas where case studies normally are
conducted. This means that many research questions in software engineering are suitable
for case study research.
The definition of case study in Section 2.1 focuses on studying phenomena in their
context, especially when the boundary between the phenomenon and its context is unclear.
This is particularly true in software engineering. Experimentation in software engineering has
clearly shown, e.g. when trying to replicate studies, that there are many factors impacting on
the outcome of a software engineering activity (Shull et al. 2002). Case studies offer an
approach which does not need a strict boundary between the studied object and its
environment; perhaps the key to understanding is in the interaction between the two?
2.4 Case Study Research Process
When conducting a case study, there are five major process steps to be walked through:
1.
Case study design: objectives are defined and the case study is planned.
2.
Preparation for data collection: procedures and protocols for data collection are defined.
Empir Software Eng (2009) 14:131–164
137


## PDF page 8

3.
Collecting evidence: execution with data collection on the studied case.
4.
Analysis of collected data
5.
Reporting
This process is almost the same for any kind of empirical study; compare e.g. to the
processes proposed by Wohlin et al. (2000) and Kitchenham et al. (2002). However, as case
study methodology is a flexible design strategy, there is a significant amount of iteration
over the steps (Andersson and Runeson 2007b). The data collection and analysis may be
conducted incrementally. If insufficient data is collected for the analysis, more data
collection may be planned etc. However, there is a limit to the flexibility; the case study
should have specific objectives set out from the beginning. If the objectives change, it is a
new case study rather than a change to the existing one, though this is a matter of judgment
as all other classifications. Eisenhardt adds two steps between 4 and 5 above in her process
for building theories from case study research (Eisenhardt 1989) a) shaping hypotheses and
b) enfolding literature, while the rest except for terminological variations are the same as
above.
2.5 Definitions
In this paper, we use the following terminology. The overall objective is a statement of what
is expected to be achieved in the case study. Others may use goals, aims or purposes as
synonyms or hyponyms for objective. The objective is refined into a set of research
questions, which are to be answered through the case study analysis. A case may be based
on a software engineering theory. It is beyond the scope of this article to discuss in detail
what is meant by a theory. However, Sjøberg et al., describe a framework for theories
including constructs of interest, relations between constructs, explanations to the relations,
and scope of the theory (Sjøberg et al. 2008). With this way of describing theories, software
engineering theories include at least one construct from software engineering. A research
question may be related to a hypothesis (sometimes called a proposition (Yin 2003)), i.e. a
supposed explanation for an aspect of the phenomenon under study. Hypotheses may
alternatively be generated from the case study for further research. The case is referred to as
the object of the study (e.g. a project), and it contains one or more units of analysis (e.g.
subprojects). Data is collected from the subjects of the study, i.e. those providing the
information. Data may be quantitative (numbers, measurements) or qualitative (words,
descriptions). A case study protocol defines the detailed procedures for collection and
analysis of the raw data, sometimes called field procedures.
The guidelines for conducting case studies presented below are organized according to
this process. Section 3 is about setting up goals for the case study and preparing for data
collection, Section 4 discusses collection of data, Section 5 discusses data analysis and
Section 6 provides some guidelines for reporting.
3 Case Study Design and Planning
3.1 Defining a Case
Case study research is of flexible type, as mentioned before. This does not mean planning is
unnecessary. On the contrary, good planning for a case study is crucial for its success. There
are several issues that need to be planned, such as what methods to use for data collection,
138
Empir Software Eng (2009) 14:131–164


