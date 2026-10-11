# Guidelines for Conducting and Reporting Case Study Research in Software Engineering

Source ID: C07
Authors: Per Runeson; Martin Höst
Source URL: https://link.springer.com/content/pdf/10.1007/s10664-008-9102-8.pdf
DOI: 10.1007/s10664-008-9102-8
Identity: Empirical Software Engineering 14(2), 2009, pp. 131–164; online December 2008. Publisher open-access PDF. See the license clause in the PDF.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 17

differences instead of trying to replicate similarities, as discussed in Section 3.1. This means
that it is good to try to involve different roles, personalities, etc in the interview. The
number of interviewees has to be decided during the study. One criterion for when
sufficient interviews are conducted is “saturation”, i.e. when no new information or
viewpoint is gained from new subjects (Corbin and Strauss 2008).
Interviews were conducted in study XP. The researchers had an initial hypothesis about potential problems of
combining agile methods with a traditional stage-gate model. However no details about this were known and
the hypotheses were not detailed with respect to this. Hence a semi-structured approach was chosen, which
supports the combination of exploratory and explanatory type of case study. An interview guide was
developed, based on knowledge of agile and stage-gate models, together with the hypotheses of the study.
The interviews were semi-structure, where the structure was given in terms of topics, which we wanted to
cover and approximate time budget for each topic, see (Karlström and Runeson 2006) “Appendix A”.
Relevant people to interview were identified in cooperation with the involved organizations. All interviewed
persons were promised that only anonymous data would be presented externally and internally in the
organization. Two researchers conducted most of the interviews together, which were audio recorded, and
later transcribed. The interviewers also took notes on what they spontaneously found relevant.
4.3 Observations
Observations can be conducted in order to investigate how a certain task is conducted by
software engineers. This is a first or second degree method according to the classification in
Section 4.1. There are many different approaches for observation. One approach is to
monitor a group of software engineers with a video recorder and later on analyze the
recording, for example through protocol analysis (Owen et al. 2006; von Mayrhauser and
Vans 1996). Another alternative is to apply a “think aloud” protocol, where the researcher
are repeatedly asking questions like “What is your strategy?” and “What are you thinking?”
to remind the subjects to think aloud. This can be combined with recording of audio and
keystrokes as proposed e.g. by Wallace et al. (2002). Observations in meetings is another
type, where meeting attendants interact with each other, and thus generate information
about the studied object. An alternative approach is presented by Karahasanović et al.
(2005) where a tool for sampling is used to obtain data and feedback from the participants.
Approaches for observations can be divided into high or low interaction of the researcher
and high or low awareness of the subjects of being observed, see Table 5.
Interview 
session 
b)
a)
c)
Fig. 2 General principles for
interview sessions. a funnel, b
pyramid, and c time-glass
Table 5 Different approaches to observations.
High awareness of
being observed
Low awareness of
being observed
High degree of interaction by the researcher
Case 1
Case 2
Low degree of interaction by the researcher
Case 3
Case 4
Empir Software Eng (2009) 14:131–164
147


## PDF page 18

Observations according to case 1 or case 2 are typically conducted in action research or
classical ethnographic studies where the researcher is part of the team, and not only seen as
a researcher by the other team members. The difference between case 1 and case 2 is that in
case 1 the researcher is seen as an “observing participant” by the other subjects, while she is
more seen as a “normal participant” in case 2. In case 3 the researcher is seen only as a
researcher. The approaches for observation typically include observations with first degree
data collection techniques, such as a “think aloud” protocol as described above. In case 4
the subjects are typically observed with a second degree technique such as video recording
(sometimes called video ethnography).
An advantage of observations is that they may provide a deep understanding of the
phenomenon that is studied. Further, it is particularly relevant to use observations, where it
is suspected that there is a deviation between an “official” view of matters and the “real”
case (Robinson et al. 2007). It should however be noted that it produces a substantial
amount of data which makes the analysis time consuming.
In the three example studies no extensive observations, e.g. through video recording or think-aloud
procedures, were conducted. In a study, related to the XP study, Sharp and Robinson use observations (Sharp
and Robinson 2004). The observer spent 1 week with an XP team, taking part in everyday activities,
including pair programming, i.e. an approach like Case 1 above. Data collected consisted of field notes,
audio recordings of meetings and discussions, photographs and copies of artifacts.
4.4 Archival Data
Archival data refers to, for example, meeting minutes, documents from different
development phases, organizational charts, financial records, and previously collected
measurements in an organization. Benbasat et al. (1987) and Yin (2003) distinguish
between documentation and archival records, while we treat them together and see the
borderline rather between qualitative data (minutes, documents, charts) and quantitative
data (records, metrics), the latter discussed in Section 4.5.
Archival data is a third degree type of data that can be collected in a case study. For this
type of data a configuration management tool is an important source, since it enables the
collection of a number of different documents and different versions of documents. As for
other third degree data sources it is important to keep in mind that the documents were not
originally developed with the intention to provide data to research in a case study. A
document may, for example, include parts that are mandatory according to an
organizational template but of lower interest for the project, which may affect the quality
of that part. It should also be noted that it is possible that some information that is needed
by the researcher may be missing, which means that archival data analysis must be
combined with other data collection techniques, e.g. surveys, in order to obtain missing
historical factual data (Flynn et al. 1990). It is of course hard for the researcher to assess the
quality of the data, although some information can be obtained by investigating the purpose
of the original data collection, and by interviewing relevant people in the organization.
In study QA, archival data was a major source of information. Three different projects from one organization
were studied. One of the projects was conducted prior to the study, which meant that the data from this
project was analyzed in retrospect. We studied process models as well as project specifications and reports.
In study XP, archival data in the form of process models were used as complementary sources of information.
148
Empir Software Eng (2009) 14:131–164


## PDF page 19

4.5 Metrics
The above mentioned data collection techniques are mostly focused on qualitative data.
However, quantitative data is also important in a case study. Software measurement is the
process of representing software entities, like processes, products, and resources, in
quantitative numbers (Fenton and Pfleeger 1996).
Collected data can either be defined and collected for the purpose of the case study, or
already available data can be used in a case study. The first case gives, of course, most
flexibility and the data that is most suitable for the research questions under investigation.
The definition of what data to collect should be based on a goal-oriented measurement
technique, such as the Goal Question Metric method (GQM) (Basili and Weiss 1984; van
Solingen and Berghout 1999). In GQM, goals are first formulated, and the questions are
refined based on these goals, and after that metrics are derived based on the questions. This
means that metrics are derived based on goals that are formulated for the measurement
activity, and thus that relevant metrics are collected. It also implies that the researcher can
control the quality of the collected data and that no unnecessary data is collected.
Examples of already available data are effort data from older projects, sales figures of
products, metrics of product quality in terms of failures etc. This kind of data may, for
example, be available in a metrics database in an organization. When this kind of data is
used it should be noticed that all the problems are apparent that otherwise are solved with a
goal oriented measurement approach. The researcher can neither control nor assess the
quality of the data, since it was collected for another purpose, and as for other forms of
archival analysis there is a risk of missing important data.
The archival data in study QA was mainly in the form of metrics collected from defect reporting and
configuration management systems but also from project specifications. Examples of metrics that were
collected are number of faults in modules, size of modules and duration for different test phases. In study XP,
defect metrics were used as complementary data for triangulation purposes.
4.6 Checklists
The checklist items for preparation and conduct of data collection are shown in Tables 6
and 7, respectively.
Table 6 Preparation for data collection checklist items
11. Is a case study protocol for data collection and analysis derived (what, why, how, when)? Are procedures
for its update defined?
12. Are multiple data sources and collection methods planned (triangulation)?
13. Are measurement instruments and procedures well defined (measurement definitions, interview
questions)?
14. Are the planned methods and measurements sufficient to fulfill the objective of the study?
15. Is the study design approved by a review board, and has informed consent obtained from individuals and
organizations?
Empir Software Eng (2009) 14:131–164
149


## PDF page 20

5 Data Analysis
5.1 Quantitative Data Analysis
Data analysis is conducted differently for quantitative and qualitative data. For quantitative
data, the analysis typically includes analysis of descriptive statistics, correlation analysis,
development of predictive models, and hypothesis testing. All of these activities are
relevant in case study research.
Descriptive statistics, such as mean values, standard deviations, histograms and scatter
plots, are used to get an understanding of the data that has been collected. Correlation
analysis and development of predictive models are conducted in order to describe how a
measurement from a later process activity is related to an earlier process measurement.
Hypothesis testing is conducted in order to determine if there is a significant effect of one or
several variables (independent variables) on one or several other variables (dependent variables).
It should be noticed that methods for quantitative analysis assume a fixed research
design. For example, if a question with a quantitative answer is changed halfway in a series
of interviews, this makes it impossible to interpret the mean value of the answers. Further,
quantitative data sets from single cases tend to be very small, due to the number of
respondents or measurement points, which causes special concerns in the analysis.
Quantitative analysis is not covered any further in this paper, since it is extensively
covered in other texts. The rest of this chapter covers qualitative analysis. For more
information about quantitative analysis, refer for example to (Wohlin et al. 2000; Wohlin
and Höst 2001; Kitchenham et al. 2002).
In study RE and study QC the main analyses were conducted with quantitative methods, mainly through
analysis of correlation and descriptive statistics, such as scatter plots. In the QC case, the quantitative data
acted as a trigger for deeper understanding. Patterns in the data, and lack thereof generated questions in the
feedback session. The answers lead to changes in the data analysis, e.g. filtering out some data sources, and
to identification of real patterns in the data.
In study XP, the main analysis was conducted with qualitative methods, but this was combined with a limited
quantitative analysis of number of defects found during different years in one of the organizations. However,
there would probably have been possibilities to conduct more complementary analyses in order to
corroborate or develop the results from the qualitative analysis.
5.2 Qualitative Data Analysis
Since case study research is a flexible research method, qualitative data analysis methods
(Seaman 1999) are commonly used. The basic objective of the analysis is to derive
conclusions from the data, keeping a clear chain of evidence. The chain of evidence means
Table 7 Collecting evidence checklist items
16. Is data collected according to the case study protocol?
17. Is the observed phenomenon correctly implemented (e.g. to what extent is a design method under study
actually used)?
18. Is data recorded to enable further analysis?
19. Are sensitive results identified (for individuals, the organization or the project)?
20. Are the data collection procedures well traceable?
21. Does the collected data provide ability to address the research question?
150
Empir Software Eng (2009) 14:131–164


## PDF page 21

that a reader should be able to follow the derivation of results and conclusions from the
collected data (Yin 2003). This means that sufficient information from each step of the
study and every decision taken by the researcher must be presented.
In addition to the need to keep a clear chain of evidence in mind, analysis of qualitative
research is characterized by having analysis carried out in parallel with the data collection
and the need for systematic analysis techniques. Analysis must be carried out in parallel
with the data collection since the approach is flexible and that new insights are found
during the analysis. In order to investigate these insights, new data must often be collected,
and instrumentation such as interview questionnaires must be updated. The need to be
systematic is a direct result of that the data collection techniques can be constantly updated,
while the same time being required to maintain a chain of evidence.
In order to reduce bias by individual researchers, the analysis benefits from being
conducted by multiple researchers. The preliminary results from each individual researcher
is merged into a common analysis result in a second step. Keeping track and reporting the
cooperation scheme helps increasing the validity of the study.
5.2.1 General Techniques for Analysis
There are two different parts of data analysis of qualitative data, hypothesis generating
techniques and hypothesis confirmation techniques (Seaman 1999), which can be used for
exploratory and explanatory case studies, respectively.
Hypothesis generation is intended to find hypotheses from the data. When using these
kinds of techniques, there should not be too many hypotheses defined before the analysis is
conducted. Instead the researcher should try to be unbiased and open for whatever hypotheses
are to be found in the data. The results of these techniques are the hypotheses as such.
Examples of hypotheses generating techniques are “constant comparisons” and “cross-case
analysis” (Seaman 1999). Hypothesis confirmation techniques denote techniques that can be
used to confirm that a hypothesis is really true, e.g. through analysis of more data. Triangulation
and replication are examples of approaches for hypothesis confirmation (Seaman 1999).
Negative case analysis tries to find alternative explanations that reject the hypotheses. These
basic types of techniques are used iteratively and in combination. First hypotheses are
generated and then they are confirmed. Hypothesis generation may take place within one
cycle of a case study, or with data from one unit of analysis, and hypothesis confirmation may
be done with data from another cycle or unit of analysis (Andersson and Runeson 2007b).
This means that analysis of qualitative data is conducted in a series of steps (based on
(Robson 2002), p. 459). First the data is coded, which means that parts of the text can be
given a code representing a certain theme, area, construct, etc. One code is usually assigned
to many pieces of text, and one piece of text can be assigned more than one code. Codes
can form a hierarchy of codes and sub-codes. The coded material can be combined with
comments and reflections by the researcher (i.e. “memos”). When this has been done, the
researcher can go through the material to identify a first set of hypotheses. This can, for
example, be phrases that are similar in different parts of the material, patterns in the data,
differences between sub-groups of subjects, etc. The identified hypotheses can then be used
when further data collection is conducted in the field, i.e. resulting in an iterative approach
where data collection and analysis is conducted in parallel as described above. During the
iterative process a small set of generalizations can be formulated, eventually resulting in a
formalized body of knowledge, which is the final result of the research attempt. This is, of
course, not a simple sequence of steps. Instead, they are executed iteratively and they affect
each other.
Empir Software Eng (2009) 14:131–164
151


## PDF page 22

The activity where hypotheses are identified requires some more information. This is in
no way a simple step that can be carried out by following a detailed, mechanical, approach.
Instead it requires ability to generalize, innovative thinking, etc. from the researcher. This
can be compared to quantitative analysis, where the majority of the innovative and
analytical work of the researcher is in the planning phase (i.e. deciding design, statistical
tests, etc). There is, of course, also a need for innovative work in the analysis of quantitative
data, but it is not as clear as in the planning phase. In qualitative analysis there are major
needs for innovative and analytical work in both phases.
One example of a useful technique for analysis is tabulation, where the coded data is
arranged in tables, which makes it possible to get an overview of the data. The data can, for
example be organized in a table where the rows represent codes of interest and the columns
represent interview subjects. However, how to do this must be decided for every case study.
There are specialized software tools available to support qualitative data analysis, e.g.
NVivo and Atlas. However, in some cases standard tools such as word processors and
spreadsheet tools are useful when managing the textual data.
In study XP, the transcribed interviews were initially analyzed by one of the researchers. A preliminary set of
codes were derived from the informal notes and applied to the transcripts. The preliminary set of codes was:
project model, communication, planning, follow-up, quality, technical issues and attitudes. Each statement in
the transcribed interviews was given a unique identification, and classified by two researchers. The
transcribed data was then filled into tables, allowing for analysis of patterns in the data by sorting issues
found by, for example, interviewee role or company. The chain of evidence is illustrated with the figure below
(from Karlström and Runeson 2006)
 
In study RE and QA the main analysis was quantitative, although some 
qualitative analysis was conducted on the information that was gathered in
 
feedback sessions. However, this analysis would probably benefit from being  
conducted in a more structured way, e.g. by recording, transcribing, and 
coding feedback data before analysis.  
EMW 
ABB 
Actual events within case context 
Subjects’ perceptions based on their 
observations and experiences  
Sound recording of interview 
Transcription of recording 
Grouped quotes 
Conclusions 
152
Empir Software Eng (2009) 14:131–164


## PDF page 23

5.2.2 Level of Formalism
A structured approach is, as described above, important in qualitative analysis. This means,
for example, in all cases that a pre-planned approach for analysis must be applied, all
decisions taken by the researcher must be recorded, all versions of instrumentation must be
kept, links between data, codes, and memos must be explicitly recorded in documentation,
etc. However, the analysis can be conducted at different levels of formalism. In (Robson
2002) the following approaches are mentioned:
&
Immersion approaches: These are the least structured approaches, with very low level of
structure, more reliant on intuition and interpretive skills of the researcher. These
approaches may be hard to combine with requirements on keeping and communicating
a chain of evidence.
&
Editing approaches: These approaches include few a priori codes, i.e. codes are defined
based on findings of the researcher during the analysis.
&
Template approaches: These approaches are more formal and include more a priori
based on research questions.
&
Quasi-statistical approaches: These approaches are much formalized and include, for
example, calculation of frequencies of words and phrases.
To our experience editing approaches and template approaches are most suitable in
software engineering case studies. It is hard to present and obtain a clear chain of evidence
in informal immersion approaches. It is also hard to interpret the result of, for example,
frequencies of words in documents and interviews.
Study XP used an editing approach. The analysis started with a set of codes (see Section 5.2.1), which
was extended and modified during the analysis. For example, the code “communication” was split into four
codes: “horizontal communication”, “vertical communication”, “internal communication” and, “external
communication”.
5.2.3 Validity
The validity of a study denotes the trustworthiness of the results, to what extent the results
are true and not biased by the researchers’ subjective point of view. It is, of course, too late
to consider the validity during the analysis. The validity must be addressed during all
previous phases of the case study. However, the validity is discussed in this section, since it
cannot be finally evaluated until the analysis phase.
There are different ways to classify aspects of validity and threats to validity in the literature.
Here we chose a classification scheme which is also used by Yin (2003) and similar to what is
usually used in controlled experiments in software engineering (Wohlin et al. 2000). Some
researchers have argued for having a different classification scheme for flexible design studies
(credibility, transferability, dependability, confirmability), while we prefer to operationalize this
scheme for flexible design studies, instead of changing the terms (Robson 2002). This scheme
distinguishes between four aspects of the validity, which can be summarized as follows:
&
Construct validity: This aspect of validity reflect to what extent the operational
measures that are studied really represent what the researcher have in mind and what is
investigated according to the research questions. If, for example, the constructs
discussed in the interview questions are not interpreted in the same way by the
researcher and the interviewed persons, there is a threat to the construct validity.
Empir Software Eng (2009) 14:131–164
153


## PDF page 24

&
Internal validity: This aspect of validity is of concern when causal relations are
examined. When the researcher is investigating whether one factor affects an
investigated factor there is a risk that the investigated factor is also affected by a third
factor. If the researcher is not aware of the third factor and/or does not know to what
extent it affects the investigated factor, there is a threat to the internal validity.
&
External validity: This aspect of validity is concerned with to what extent it is possible
to generalize the findings, and to what extent the findings are of interest to other people
outside the investigated case. During analysis of external validity, the researcher tries to
analyze to what extent the findings are of relevance for other cases. There is no
population from which a statistically representative sample has been drawn. However,
for case studies, the intention is to enable analytical generalization where the results are
extended to cases which have common characteristics and hence for which the findings
are relevant, i.e. defining a theory.
&
Reliability: This aspect is concerned with to what extent the data and the analysis are
dependent on the specific researchers. Hypothetically, if another researcher later on
conducted the same study, the result should be the same. Threats to this aspect of
validity is, for example, if it is not clear how to code collected data or if questionnaires
or interview questions are unclear.
It is, as described above, important to consider the validity of the case study from the
beginning. Examples of ways to improve validity are triangulation, developing and
maintaining a detailed case study protocol, having designs, protocols, etc. reviewed by peer
researchers, having collected data and obtained results reviewed by case subjects, spending
sufficient time with the case, and giving sufficient concern to analysis of “negative cases”,
i.e. looking for theories that contradict your findings.
In study XP, validity threats were analyzed based on a checklist by Robson (2002). It would also have been
possible to analyze threats according to construct validity, internal validity, external validity, and reliability.
Countermeasures against threats to validity were then taken. For example, triangulation was achieved in
different ways, results were reviewed by case representatives, and potential negative cases were identified by
having two researchers working with the same material in parallel. It was also seen as important that
sufficient time was spent with the organization in order to understand it. Even if the case study lasted for a
limited time, this threat was lowered by the fact that the researchers had had a long-term cooperation with
the organization before the presented case study.
In study QA, e.g. data triangulation was used to check which phase the defect reports originated from. The alignment
between the phase reported in the trouble report, and the person’s tasks in the project organization was checked.
5.3 Checklist
The checklist items for analysis of collected data are shown in Table 8.
6 Reporting
An empirical study cannot be distinguished from its reporting. The report communicates the
findings of the study, but is also the main source of information for judging the quality of
the study. Reports may have different audiences, such as peer researchers, policy makers,
research sponsors, and industry practitioners (Yin 2003). This may lead to the need of
writing different reports for difference audiences. Here, we focus on reports with peer
researchers as main audience, i.e. journal or conference articles and possibly accompanying
154
Empir Software Eng (2009) 14:131–164


