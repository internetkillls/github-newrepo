# Guidelines for Conducting and Reporting Case Study Research in Software Engineering

Source ID: C07
Authors: Per Runeson; Martin Höst
Source URL: https://link.springer.com/content/pdf/10.1007/s10664-008-9102-8.pdf
DOI: 10.1007/s10664-008-9102-8
Identity: Empirical Software Engineering 14(2), 2009, pp. 131–164; online December 2008. Publisher open-access PDF. See the license clause in the PDF.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 9

what departments of an organization to visit, what documents to read, which persons to
interview, how often interviews should be conducted, etc. These plans can be formulated in
a case study protocol, see Section 3.2.
A plan for a case study should at least contain the following elements (Robson 2002):
&
Objective—what to achieve?
&
The case—what is studied?
&
Theory—frame of reference
&
Research questions—what to know?
&
Methods—how to collect data?
&
Selection strategy—where to seek data?
The objective of the study may be, for example, exploratory, descriptive, explanatory, or
improving. The objective is naturally more generally formulated and less precise than in
fixed research designs. The objective is initially more like a focus point which evolves
during the study. The research questions state what is needed to know in order to fulfill the
objective of the study. Similar to the objective, the research questions evolve during the
study and are narrowed to specific research questions during the study iterations
(Andersson and Runeson 2007b).
The case may in general be virtually anything which is a “contemporary phenomenon in
its real-life context” (Yin 2003). In software engineering, the case may be a software
development project, which is the most straightforward choice. It may alternatively be an
individual, a group of people, a process, a product, a policy, a role in the organization, an
event, a technology, etc. The project, individual, group etc. may also constitute a unit of
analysis within a case. In the information systems field, the case may be “individuals,
groups…or an entire organization. Alternatively, the unit of analysis may be a specific
project or decision”(Benbasat et al. 1987). Studies on “toy programs” or similarly are of
course excluded due to its lack of real-life context. Yin (2003) distinguishes between
holistic case studies, where the case is studied as a whole, and embedded case studies
where multiple units of analysis are studied within a case, see Fig. 1. Whether to define a
study consisting of two cases as holistic or embedded depends on what we define as the
context and research goals. In our XP example, two projects are studied in two different
companies in two different application domains, both using agile practices (Karlström and
Runeson 2006). The projects may be considered two units of analysis in an embedded case
study if the context is software companies in general and the research goal is to study agile
practices. On the contrary, if the context is considered being the specific company or
application domain, they have to be seen as two separate holistic cases. Benbasat et al.
comment on a specific case study, “Even though this study appeared to be a single-case,
embedded unit analysis, it could be considered a multiple-case design, due to the
centralized nature of the sites.” (Benbasat et al. 1987).
Context 
Case 
Context 
Case 
Unit of 
Analysis 
Unit of 
Analysis 
Unit of 
Analysis 
Fig. 1 Holistic case study
(left) and embedded case
study (right)
Empir Software Eng (2009) 14:131–164
139


## PDF page 10

Using theories to develop the research direction is not well established in the software
engineering field, as concluded in a systematic review on the topic (Hannay et al. 2007;
Shull and Feldman 2008). However, defining the frame of reference of the study makes the
context of the case study research clear, and helps both those conducting the research and
those reviewing the results of it. As theories are underdeveloped in software engineering,
the frame of reference may alternatively be expressed in terms of the viewpoint taken in the
research and the background of the researchers. Grounded theory case studies naturally
have no specified theory (Corbin and Strauss 2008).
The principal decisions on methods for data collection are defined at design time for the
case study, although detailed decisions on data collection procedures are taken later.
Lethbridge et al. (2005) define three categories of methods: direct (e.g. interviews), indirect
(e.g. tool instrumentation) and independent (e.g. documentation analysis). These are further
elaborated in Section 4.
In case studies, the case and the units of analysis should be selected intentionally. This is
in contrast to surveys and experiments, where subjects are sampled from a population to
which the results are intended to be generalized. The purpose of the selection may be to
study a case that is expected to be “typical”, “critical”, “revelatory” or “unique” in some
respect (Benbasat et al. 1987), and the case is selected accordingly. Flyvbjerg defines four
variants of information-oriented case study selections: “extreme/deviant”, “maximum
variation”, “critical” and “paradigmatic” (Flyvbjerg 2007). In a comparative case study,
the units of analysis must be selected to have the variation in properties that the study
intends to compare. However, in practice, many cases are selected based on availability
(Benbasat et al. 1987) as is the case for many experiments (Sjøberg et al. 2005).
Case selection is particularly important when replicating case studies. A case study may
be literally replicated, i.e. the case is selected to predict similar results, or it is theoretically
replicated, i.e. the case is selected to predict contrasting results for predictable reasons
(Yin 2003).
There were different objectives of the three example cases. The objective of study XP was to investigate how
an agile process can coexist with a stage-gate management organization. The objective of study RE was to
evaluate a method for prioritization of requirements, and the objective of study QA was to find quantitative
prediction models and procedures for defect data.
Study XP is considered an embedded case study with two units of analysis from two different companies,
although it might be seen as two holistic case studies, as denoted above. RE is a holistic case study with one
unit of analysis, while QA is an embedded case study in one company with three different projects as units of
analysis. All the companies were selected based on existing academia-industry relations, while the units of
analysis were selected to fit the specific case study purposes.
Concerning the frame of reference, no explicit theories are referred to in studies XP and RE. However,
the investigated approaches are based on existing methods that, to some extent, already have been
investigated. Earlier studies thereby affected the designs of the studies. Study QA was partly a
replication, which means that the original study formed a frame of reference from which theories on, for
example, the Pareto principle and fault persistence between test phases were used when hypotheses were
defined.
Data were primarily collected using interviews in the XP case. In the RE case, questionnaires constituted
the major source of data, while in the QA case, defect metrics from a company was the major data
source.
140
Empir Software Eng (2009) 14:131–164


## PDF page 11

3.2 Case Study Protocol
The case study protocol is a container for the design decisions on the case study as well as
field procedures for its carrying through. The protocol is a continuously changed document
that is updated when the plans for the case study are changed.
There are several reasons for keeping an updated version of a case study protocol.
Firstly, it serves as a guide when conducting the data collection, and in that way prevents
the researcher from missing to collect data that were planned to be collected. Secondly, the
processes of formulating the protocol makes the research concrete in the planning phase,
which may help the researcher to decide what data sources to use and what questions to ask.
Thirdly, other researchers and relevant people may review it in order to give feedback on
the plans. Feedback on the protocol from other researchers can, for example, lower the risk
of missing relevant data sources, interview questions or roles to include in the research and to
assure the relation between research questions and interview questions. Finally, it can serve as
a log or diary where all conducted data collection and analysis is recorded together with
change decisions based on the flexible nature of the research. This can be an important source
of information when the case study later on is reported. In order to keep track of changes
during the research project, the protocol should be kept under some form of version control.
Pervan and Maimbo propose an outline of a case study protocol, which is summarized in
Table 2. As the proposal shows, the protocol is quite detailed to support a well structured
research approach.
Case study protocols cannot be published in extenso since they contain confidential information. However,
parts of the protocol can be published, such as interview instruments, which is the case in study XP. In study
QA, a logbook was kept which documents the iterations of the case study. A condensed version of the
logbook is shown below as published (Andersson and Runeson 2007b), which shows seven case study cycles,
indicating the evolutionary characteristic of the case study.
# Goals and
scope
Data collection and
filtering
Analysis and presentation
Interpretation and improvement
1 Simulation
model
Process models
Time reports
Failure reports
Build simulation model
Too complex approach - not
completed
2 Exploratory
Failure reports
project 1, 2
Distribution of detection
activities over time
Response on specific events in each
project
3 Exploratory
Failure reports per
feature group
Distribution of detection
activities per feature group
Motivation for distribution
4 Confirmatory
Failure reports
project 3
Same as in cycle 2 and 3
Sufficient fit for practical use
5 Explanatory
Qualitative data on
feature groups
Characteristics of feature
groups
Root cause analysis on causes and
suggestions for each group
Subset of failure reports
6 Explanatory
(prediction)
All failure reports
Prediction of defect content
with simple model
Use of prediction model to improve
planning
7 Explanatory
(prediction)
All failure reports
Time data
Software reliability growth
models
Use of prediction model
Empir Software Eng (2009) 14:131–164
141


## PDF page 12

3.3 Ethical Considerations
At design time of a case study, ethical considerations must be made (Singer and Vinson
2002). Even though a research study first and foremost is built on trust between the
researcher and the case (Amschler Andrews and Pradhan 2001), explicit measures must be
taken to prevent problems. In software engineering, case studies often include dealing with
confidential information in an organization. If it is not clear from the beginning how this
kind of information is handled and who is responsible for accepting what information to
publish, there may be problems later on. Key ethical factors include:
&
Informed consent
&
Review board approval
&
Confidentiality
&
Handling of sensitive results
&
Inducements
&
Feedback
Subjects and organizations must explicitly agree to participate in the case study, i.e. give
informed consent. In some countries, this is even legally required. It may be tempting for
the researcher to collect data e.g. through indirect or independent data collection methods,
without asking for consent. However, the ethical standards must be maintained for the long
term trust in software engineering research.
Legislation of research ethics differs between countries and continents. In many
countries it is mandatory to have the study proposal reviewed and accepted with respect to
ethical issues (Seaman 1999) by a review board or a similar function at a university. In
other countries, there are no such rules. Even if there are no such rules, it is recommended
that the case study protocol is reviewed by colleagues to help avoiding pitfalls.
Consent agreements are preferably handled through a form or contract between the
researchers and the individual participant, see e.g. Robson (2002) for an example. In an
empirical study conduced by the authors of this paper, the following information were
included in this kind of form:
&
Names of researchers and contact information.
&
Purpose of empirical study.
&
Procedures used in the empirical study, i.e. a short description of what the participant should
do during the study and what steps the researcher will carry out during these activities.
Table 2 Outline of case study protocol according to Pervan and Maimbo (2005)
Section
Content
Preamble
Contains information about the purpose of the protocol, guidelines for data and
document storage, publication.
General
Provides a brief overview of the research project and the case research method
Procedures
Detailed description of the procedures for conducting each case, including down-to-
earth details on contacts and timing.
Research
instrument(s)
Interview guides, questionnaires etc. to be used to ensure consistent data collection.
Data analysis
guidelines
Detailed description of data analysis procedures, including data schemas, priori codes
etc.
Appendix A
Template letter to invite participants.
142
Empir Software Eng (2009) 14:131–164


## PDF page 13

&
A text clearly stating that the participation is voluntary, and that collected data will be
anonymous.
&
A list of known risks.
&
A list of benefits for the participants, in this case for example experience from using a
new technique and feedback effectiveness.
&
A description of how confidentiality will be assured. This includes a description of how
collected material will be coded and identified in the study.
&
Information about approvals from review board.
&
Date and signatures from participant and researchers.
If the researchers intend to use the data for other, not yet defined purposes, this should be
signed separately to allow participants to choose if their contribution is for the current study
only, or for possible future studies.
Issues on confidentiality and publication should also be regulated in a contract between
the researcher and the studied organization. However, not only can information be sensitive
when leaking outside a company. Data collected from and opinions stated by individual
employees may be sensitive if presented e.g. to their managers (Singer and Vinson 2002).
The researchers must have the right to keep their integrity and adhere to agreed procedures
in this kind of cases. Companies may not know academic practices for publication and
dissemination, and must hence be explicitly informed about those. From a publication point
of view, the relevant data to publish is rarely sensitive to the company since data may be
made anonymous. However, it is important to remember that it is not always sufficient to
remove names of companies or individuals. They may be identified by their characteristics
if they are selected from a small set of people or companies.
Results may be sensitive to a company, e.g. by revealing deficiencies in their software
engineering practices, or if their product comes out last in a comparison (Amschler Andrews
and Pradhan 2001). The chance that this may occur must be discussed upfront and made
clear to the participants of the case study. In case violations of the law are identified during
the case study, these must be reported, even though “whistle-blowers” rarely are rewarded.
The inducements for individuals and organizations to participate in a case study vary, but
there are always some kinds of incentives, tangible or intangible. It is preferable to make
the inducements explicit, i.e. specify what the incentives are for the participants. Thereby
the inducement’s role in threatening the validity of the study may also be analyzed.
Giving feedback to the participants of a study is critical for the long term trust and for
the validity of the research. Firstly, transcript of interviews and observations should be sent
back to the participants to enable correction of raw data. Secondly, analyses should be
presented to them in order to maintain their trust in the research. Participants must not
necessarily agree in the outcome of the analysis, but feeding back the analysis results
increases the validity of the study.
In all three example studies issues of confidentiality were handled through Non-Disclosure Agreements and
general project cooperation agreements between the companies and the university, lasting longer than one
case study. These agreements state that the university researchers are obliged to have publications approved
by representatives of the companies before they are published, and that raw data must not be spread to any
but those signing the contract. The researchers are not obliged to report their sources of facts to
management, unless it is found that a law is violated.
In order to ensure that interviewees were not cited wrongly, it was agreed that the transcribed interviews
were sent back to them for review in the XP study. In the beginning of each interview, interviewees were
informed about their rights in the study. In study QA, feedback meetings for analysis and interpretation were
explicitly a part of the methodology ((Andersson and Runeson 2007b) Fig. 1). When negotiating publication
Empir Software Eng (2009) 14:131–164
143


## PDF page 14

of data, we were explicitly told that raw numbers of defects could not be published, but percentages over
phases could, which was acceptable for the research purposes.
All the three studies were conducted in Sweden, where only studies in medicine are explicitly regulated by
law; hence there was no approval of the studies by a review board beforehand.
3.4 Checklist
The checklist items for case study design are shown in Table 3.
4 Collecting Data
4.1 Different Data Sources
There are several different sources of information that can be used in a case study. It is important
to use several data sources in a case study in order to limit the effects of one interpretation of one
single data source. If the same conclusion can be drawn from several sources of information, i.e.
triangulation (Section 2.2), this conclusion is stronger than a conclusion based a single source.
In a case study it is also important to take into account viewpoints of different roles, and to
investigate differences, for example, between different projects and products. Commonly,
conclusions are drawn by analyzing differences between data sources.
According to Lethbridge et al. (2005) data collection techniques can be divided into
three levels:
&
First degree: Direct methods means that the researcher is in direct contact with the
subjects and collect data in real time. This is the case with, for example interviews,
focus groups, Delphi surveys (Dalkey and Helmer 1963), and observations with “think
aloud protocols”.
&
Second degree: Indirect methods where the researcher directly collects raw data without
actually interacting with the subjects during the data collection. This approach is, for
example taken in Software Project Telemetry (Johnson et al. 2005) where the usage of
software engineering tools is automatically monitored, and observed through video
recording.
Table 3 Case study design checklist items
1. What is the case and its units of analysis?
2. Are clear objectives, preliminary research questions, hypotheses (if any) defined in advance?
3. Is the theoretical basis—relation to existing literature or other cases—defined?
4. Are the authors’ intentions with the research made clear?
5. Is the case adequately defined (size, domain, process, subjects…)?
6. Is a cause–effect relation under study? If yes, is it possible to distinguish the cause from other factors using
the proposed design?
7. Does the design involve data from multiple sources (data triangulation), using multiple methods (method
triangulation)?
8. Is there a rationale behind the selection of subjects, roles, artifacts, viewpoints, etc.?
9. Is the specified case relevant to validly address the research questions (construct validity)?
10. Is the integrity of individuals/organizations taken into account?
144
Empir Software Eng (2009) 14:131–164


## PDF page 15

&
Third degree: Independent analysis of work artifacts where already available and
sometimes compiled data is used. This is for example the case when documents such as
requirements specifications and failure reports from an organization are analyzed or
when data from organizational databases such as time accounting is analyzed.
First degree methods are mostly more expensive to apply than second or third degree
methods, since they require significant effort both from the researcher and the subjects. An
advantage of first and second degree methods is that the researcher can to a large extent
exactly control what data is collected, how it is collected, in what form the data is collected,
which the context is etc. Third degree methods are mostly less expensive, but they do not
offer the same control to the researcher; hence the quality of the data is not under control
either, neither regarding the original data quality nor its use for the case study purpose. In
many cases the researcher must, to some extent, base the details of the data collection on
what data is available. For third degree methods it should also be noticed that the data has
been collected and recorded for another purpose than that of the research study, contrary to
general metrics guidelines (van Solingen and Berghout 1999). It is not certain that
requirements on data validity and completeness were the same when the data was collected
as they are in the research study.
In Sections 4.2–4.5 we discuss specific data collection methods, where we have found
interviews, observations, archival data and metrics being applicable to software engineering
case studies (Benbasat et al. 1987; Yin 2003).
In study XP data is collected mainly through interviews, i.e. a first degree method. The evaluation of a
proposed method in study RE involves filling out a form for prioritization of requirements. These forms were
an important data source, i.e. a second order method. In study QA stored data in the form defect reporting
metrics were used as a major source of data, i.e. a third degree method. All studies also included one or
several feedback steps where the organizations gave feedback on the results, i.e. a first-degree data
collection method. These data were complemented with second or third degree data, e.g. process models
were used in studies XP and QA.
4.2 Interviews
Data collection through interviews is important in case studies. In interview-based data
collection, the researcher asks a series of questions to a set of subjects about the areas of
interest in the case study. In most cases one interview is conducted with every single
subject, but it is possible to conduct group-interviews. The dialogue between the researcher
and the subject(s) is guided by a set of interview questions.
The interview questions are based on the topic of interest in the case study. That is, the interview
questions are based on the formulated research questions (but they are of course not formulated
in the same way). Questions can be open, i.e. allowing and inviting a broad range of answers and
issues from the interviewed subject, or closed offering a limited set of alternative answers.
Interviews can, for example, be divided into unstructured, semi-structured and fully
structured interviews (Robson 2002). In an unstructured interview, the interview questions
are formulated as general concerns and interests from the researcher. In this case the
interview conversation will develop based on the interest of the subject and the researcher.
In a fully structured interview all questions are planned in advance and all questions are
asked in the same order as in the plan. In many ways, a fully structured interview is similar
to a questionnaire-based survey. In a semi-structured interview, questions are planned, but
they are not necessarily asked in the same order as they are listed. The development of the
Empir Software Eng (2009) 14:131–164
145


## PDF page 16

conversation in the interview can decide which order the different questions are handled,
and the researcher can use the list of questions to be certain that all questions are handled.
Additionally, semi-structured interviews allow for improvisation and exploration of the
studied objects. Semi-structured interviews are common in case studies. The different types
of interviews are summarized in Table 4.
An interview session may be divided into a number of phases. First the researcher
presents the objectives of the interview and the case study, and explains how the data from
the interview will be used. Then a set of introductory questions are asked about the
background etc. of the subject, which are relatively simple to answer. After the introduction
comes the main interview questions, which take up the largest part of the interview. If the
interview contains personal and maybe sensitive questions, e.g. concerning economy,
opinions about colleagues, why things went wrong, or questions related to the interviewees
own competence (Hove and Anda 2005), special care must be taken. In this situation it is
important that the interviewee is ensured confidentiality and that the interviewee trusts the
interviewer. It is not recommended to start the interview with these questions or to
introduce them before a climate of trust has been obtained. It is recommended that the
major findings are summarized by the researcher towards the end of the interview, in order
to get feedback and avoid misunderstandings.
Interview sessions can be structured according to three general principles, as outlined in
Fig. 2 (Caroline Seaman, personal communication). The funnel model begins with open
questions and moves towards more specific ones. The pyramid model begins with specific
ones, and opens the questions during the course of the interview. The time-glass model
begins with open questions, straightens the structure in the middle and opens up again
towards the end of the interview.
During the interview sessions it is recommended to record the discussion in a suitable
audio or video format. Even if notes are taken, it is in many cases hard to record all details,
and it is impossible to know what is important to record during the interview. Possibly a
dedicated and trained scribe may capture sufficient detail in real-time, but the recording
should at least be done as a backup (Hove and Anda 2005). When the interview has been
recorded it needs to be transcribed into text before it is analyzed. This is a time consuming
task, but in many cases new insights are made during the transcription, and it is therefore
not recommended that this task is conducted by anyone else than the researcher. In some
cases it may be advantageous to have the transcripts reviewed by the interview subject. In
this way questions about what was actually said can be sorted out, and the interview subject
has the chance to point out if she does not agree with the interpretation of what was said or
if she simply has changed her mind and wants to rephrase any part of the answers.
During the planning phase of an interview study it is decided whom to interview. Due to
the qualitative nature of the case study it is recommended to select subjects based on
Table 4 Overview of interviews
Unstructured
Semi-structured
Fully structured
Typical focus
How individuals
qualitatively
experience
the phenomenon
How individuals qualitatively
and quantitatively
experience
the phenomenon
Researcher seeks to find
relations between
constructs
Interview
questions
Interview guide with
areas to focus on
Mix of open and closed
questions
Closed questions
Objective
Exploratory
Descriptive and explanatory
Descriptive and explanatory
146
Empir Software Eng (2009) 14:131–164


