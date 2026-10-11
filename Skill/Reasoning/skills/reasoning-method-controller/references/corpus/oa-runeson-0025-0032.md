# Guidelines for Conducting and Reporting Case Study Research in Software Engineering

Source ID: C07
Authors: Per Runeson; Martin Höst
Source URL: https://link.springer.com/content/pdf/10.1007/s10664-008-9102-8.pdf
DOI: 10.1007/s10664-008-9102-8
Identity: Empirical Software Engineering 14(2), 2009, pp. 131–164; online December 2008. Publisher open-access PDF. See the license clause in the PDF.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 25

technical reports. Benbasat et al. propose that due to the extensive amount of data generated
in case studies, “books or monographs might be better vehicles to publish case study
research” (Benbasat et al. 1987).
Guidelines for reporting experiments have been proposed by Jedlitschka and Pfahl
(2005) and evaluated by Kitchenham et al. (2008). Their work aims at defining a
standardized reporting of experiments that enables cross-study comparisons through e.g.
systematic reviews. For case studies, the same high-level structure may be used, but since
they are more flexible and mostly based on qualitative data, the low-level detail is less
standardized and more depending on the individual case. Below, we first discuss the
characteristics of a case study report and then a proposed structure.
6.1 Characteristics
Robson defines a set of characteristics which a case study report should have (Robson
2002), which in summary implies that it should:
&
tell what the study was about
&
communicate a clear sense of the studied case
&
provide a “history of the inquiry” so the reader can see what was done, by whom and
how.
&
provide basic data in focused form, so the reader can make sure that the conclusions are
reasonable
&
articulate the researcher’s conclusions and set them into a context they affect.
In addition, this must take place under the balance between researcher’s duty and goal to
publish their results, and the companies’ and individuals’ integrity (Amschler Andrews and
Pradhan 2001).
Reporting the case study objectives and research questions is quite straightforward. If
they are changed substantially over the course of the study, this should be reported to help
understanding the case.
Describing the case might be more sensitive, since this might enable identification of the
case or its subjects. For example, “a large telecommunications company in Sweden” is most
probably a branch of the Ericsson Corporation. However, the case may be better
characterized by other means than application domain and country. Internal characteristics,
like size of the studied unit, average age of the personnel, etc may be more interesting than
external characteristics like domain and turnover. Either the case constitutes a small subunit
of a large corporation, and then it can hardly be identified among the many subunits, or it is
a small company and hence it is hard to identify it among many candidates. Still, care must
be taken to find this balance.
Table 8 Analysis of collected data checklist items
22. Is the analysis methodology defined, including roles and review procedures?
23. Is a chain of evidence shown with traceable inferences from data to research questions and existing theory?
24. Are alternative perspectives and explanations used in the analysis?
25. Is a cause–effect relation under study? If yes, is it possible to distinguish the cause from other factors in
the analysis?
26. Are there clear conclusions from the analysis, including recommendations for practice/further research?
27. Are threats to the validity analyzed in a systematic way and countermeasures taken? (Construct, internal,
external, reliability)
Empir Software Eng (2009) 14:131–164
155


## PDF page 26

Providing a “history of the inquiry” requires a level of substantially more detail than
pure reporting of used methodologies, e.g. “we launched a case study using semi-structured
interviews”. Since the validity of the study is highly related to what is done, by whom and
how, it must be reported about the sequence of actions and roles acting in the study process.
On the other hand, there is no room for every single detail of the case study conduct, and
hence a balance must be found.
Data is collected in abundance in a qualitative study, and the analysis has as its main
focus to reduce and organize data to provide a chain of evidence for the conclusions.
However, to establish trust in the study, the reader needs relevant snapshots from the data
that support the conclusions. These snapshots may be in the form of e.g. citations (typical
or special statements), pictures, or narratives with anonymized subjects. Further, categories
used in the data classification, leading to certain conclusions may help the reader follow the
chain of evidence.
Finally, the conclusions must be reported and set into a context of implications, e.g. by
forming theories. A case study can not be generalized in the meaning of being
representative of a population, but this is not the only way of achieving and transferring
knowledge. Conclusions can be drawn without statistics, and they may be interpreted and
related to other cases. Communicating research results in terms of theories is an
underdeveloped practice in software engineering (Hannay et al. 2007).
6.2 Structure
Yin proposes several alternative structures for reporting case studies in general (Yin 2003).
&
Linear-analytic—the standard research report structure (problem, related work,
methods, analysis, conclusions)
&
Comparative—the same case is repeated twice or more to compare alternative
descriptions, explanations or points of view.
&
Chronological—a structure most suitable for longitudinal studies.
&
Theory-building—presents the case according to some theory-building logic in order to
constitute a chain of evidence for a theory.
&
Suspense—reverts the linear-analytic structure and reports conclusions first and then
backs them up with evidence.
&
Unsequenced—with none of the above, e.g. when reporting general characteristics of a
set of cases.
For the academic reporting of case studies which we focus on, the linear-analytic
structure is the most accepted structure. The high level structure for reporting experiments
in software engineering proposed by Jedlitschka and Pfahl (2005) therefore also fits the
purpose of case study reporting. However, some changes are needed, based on specific
characteristics of case studies and other issues based on an evaluation conducted by
Kitchenham et al. (2008). The resulting structure is presented in Table 9. The differences
and our considerations are presented below.
In a case study, the theory may constitute a framework for the analysis; hence, there are
two kinds of related work: a) earlier studies on the topic and b) theories on which the
current study is based.
The design section corresponds to the case study protocol, i.e. it reports the planning of
the case study including the measures taken to ensure the validity of the study.
156
Empir Software Eng (2009) 14:131–164


## PDF page 27

Table 9 Proposed reporting structure by Jedlitschka and Pfahl (2005) and modification proposed by
Kitchenham et al. (2008) and adaptations to case study reporting, influenced by Robson (2002)
Experiments
Case studies
Section
heading
Subsections
Section
headings
Subsections
Title
Title
Authorship
Authorship
Structured abstract
(Structured) abstract
Motivation
Problem statement
Introduction
Problem statement
Research
objectives
Research objectives
Context
Context
Related work
Related work
Earlier studies
Theory
Experimental
design
Goals, hypotheses
and variables
Case study
design
Research questions
Design
Case and subjects selection
Subjects
Data collection procedure(s)
Objects
Analysis procedure(s)
Instrumentation
Validity procedure(s)
Data collection
procedure
Analysis procedure
Evaluation of
validity
Execution
Sample
Results
Case and subjects description, covering execution,
analysis and interpretation issues.
Preparation
Subsections may be structured e.g. according to
coding scheme, each linking observations to
conclusions
Data collection
performed
Evaluation of validity
Validity procedure
Analysis
Descriptive
statistics
Data set reduction
Hypothesis testing
Interpretation
Evaluation of
results and
implications
Conclusions
and Future
work
Relation to
existing evidence
Conclusions
and Future
work
Summary of conclusions
Impact
Relation to existing evidence
Limitations
Impact/Implications
Future work
Limitations
Future work
Acknowledgements
Acknowledgements
References
References
Appendices
Appendices
Empir Software Eng (2009) 14:131–164
157


## PDF page 28

Since the case study is of flexible design, and data collection and analysis are more
intertwined, these sections may be combined into one. Consequently, the contents at the
lower level must be adjusted, as proposed in Table 9. Specifically for the combined data
section, the coding scheme often constitutes a natural subsection structure. Alternatively, for a
comparative case study, the data section may be structured according to the compared cases,
and for a longitudinal study, the time scale may constitute the structure of the data section.
This combined results section also includes an evaluation of the validity of the final results.
The case studies were presented in different formats. Study XP was, for example, presented to the involved
companies in seminar format, and to the research community in journal format (Karlström and Runeson
2006), to practitioners in a magazine format (Karlström and Runeson 2005), and in the form of a Ph.D.
thesis (Karlström 2004). The journal format paper is structured similar to the proposed model above,
although the outline hierarchy differs slightly.
6.3 Checklist
The checklist items for reporting are shown in Table 10.
7 Reading and Reviewing Case Study Research
7.1 Reader’s Perspective
The reader of a case study report—independently of whether the intention is to use the
findings or to review it for inclusion in a journal—must judge the quality of the study based
on the written material. Case study reports tend to be large, firstly since case studies often
are based on qualitative data, and hence the data cannot be presented in condensed form,
like quantitative data may be in tables, diagrams and statistics. Secondly, the conclusions in
qualitative analyses are not based on statistical significance which can be interpreted in
terms of a probability for erroneous conclusion, but on reasoning and linking of
observations to conclusions.
Reviewing empirical research in general must be done with certain care (Tichy 2000).
Reading case study reports requires judging the quality of the report, without having the
power of strict criteria which govern experimental studies to a larger extent, e.g. statistical
Table 10 Reporting checklist items
28. Are the case and its units of analysis adequately presented?
29. Are the objective, the research questions and corresponding answers reported?
30. Are related theory and hypotheses clearly reported?
31. Are the data collection procedures presented, with relevant motivation?
32. Is sufficient raw data presented (e.g. real life examples, quotations)?
33. Are the analysis procedures clearly reported?
34. Are threats to validity analyses reported along with countermeasures taken to reduce threats?
35. Are ethical issues reported openly (personal intentions, integrity issues, confidentiality)
36. Does the report contain conclusions, implications for practice and future research?
37. Does the report give a realistic and credible impression?
38. Is the report suitable for its audience, easy to read and well structured?
158
Empir Software Eng (2009) 14:131–164


## PDF page 29

confidence levels. This does however not say that any report can do as a case study report.
The reader must have a decent chance of finding the information of relevance, both to judge
the quality of the case study and to get the findings from the study and set them into
practice or build further research on.
The criteria and guidance presented above for performing and reporting case studies are
relevant for the reader as well. However, in our work with derivation of checklists for case
study research (Höst and Runeson 2007), evaluation feedback identified a need for a more
condensed checklist for readers and reviewers. This is presented in Table 11 with numbers
referring to the items of the other checklists for more in depth criteria.
8 Summary
Case study research is conducted in order to investigate contemporary phenomena in their
natural context. That is, no laboratory environment is set up by the researcher, where factors
can be controlled. Instead the phenomena are studied in their normal context, allowing the
researcher to understand how the phenomena interact with the context. Selection of subjects
and objects is not based on statistically representative samples. Instead, research findings
are obtained through the analysis in depth of typical or special cases.
Cases study research is conducted by iteration over a set of phases. In the design phase
objectives are decided and the case is defined. Data collection is first planned with respect
to data collection techniques and data sources, and then conducted in practice. Methods for
data collection include, for example, interviews, observation, and usage of archival data.
During the analysis phase, insights are both generated and analyzed, e.g. through coding of
data and looking for patterns. During the analysis it is important to maintain a chain of
evidence from the findings to the original data. The report should include sufficient data
and examples to allow the reader to understand the chain of evidence.
Table 11 Reader’s checklist items
39. Are the objective, research questions, and hypotheses (if applicable) clear and relevant? 1, 2, 5, 29, 30
40. Are the case and its units of analysis well defined? 1, 5, 28
41. Is the suitability of the case to address the research questions clearly motivated? 8, 9, 14
42. Is the case study based on theory or linked to existing literature? 3
43. Are the data collection procedures sufficient for the purpose of the case study (data sources, collection,
validation)? 11, 13, 16, 18, 21, 31
44. Is sufficient raw data presented to provide understanding of the case and the analysis? 32
45. Are the analysis procedures sufficient for the purpose of the case study (repeatable, transparent)? 22, 33
46. Is a clear chain of evidence established from observations to conclusions? 6, 17, 20, 23, 25
47. Are threats to validity analyses conducted in a systematic way and are countermeasures taken to reduce
threats? 27, 34, 37
48. Is triangulation applied (multiple collection and analysis methods, multiple authors, multiple theories)? 7,
12, 22, 24
49. Are ethical issues properly addressed (personal intentions, integrity, confidentiality, consent, review
board approval)? 4, 10, 15, 19, 35
50. Are conclusions, implications for practice and future research, suitably reported for its audience? 26, 29,
36, 37, 38
The numbers after each item refer to corresponding items in the checklists for each process step
Empir Software Eng (2009) 14:131–164
159


## PDF page 30

This paper aims to provide a frame of reference for researchers when conducting case
study research in software engineering, which is based on an analysis of existing case study
literature and the author’s own experiences of conducting case studies. As with other
guidelines, there is a need to evaluate them through practical usage.
Acknowledgement The authors are grateful to the feedback to the checklists from the ISERN members and
IASESE attendants in September 2007. A special thank to Professor Claes Wohlin, Mr. Kim Weyns and Mr.
Andreas Jedlitschka for their review of an earlier draft of the paper. Thanks also to the anonymous reviewers
for proposals on substantial improvements. The work is partly funded by the Swedish Research Council
under grant 622-2004-552 for a senior researcher position in software engineering.
Open Access This article is distributed under the terms of the Creative Commons Attribution
Noncommercial License which permits any noncommercial use, distribution, and reproduction in any
medium, provided the original author(s) and source are credited.
Appendix A
Table 12 Researcher’s checklist
Case study design
1. What is the case and its units of analysis?
2. Are clear objectives, preliminary research questions, hypotheses (if any) defined in advance?
3. Is the theoretical basis—relation to existing literature or other cases—defined?
4. Are the authors’ intentions with the research made clear?
5. Is the case adequately defined (size, domain, process, subjects…)?
6. Is a cause–effect relation under study? If yes, is it possible to distinguish the cause from other factors
using the proposed design?
7. Does the design involve data from multiple sources (data triangulation), using multiple methods (method
triangulation)?
8. Is there a rationale behind the selection of subjects, roles, artifacts, viewpoints, etc.?
9. Is the specified case relevant to validly address the research questions (construct validity)?
10. Is the integrity of individuals/organizations taken into account?
Preparation for data collection
11. Is a case study protocol for data collection and analysis derived (what, why, how, when)? Are
procedures for its update defined?
12. Are multiple data sources and collection methods planned (triangulation)?
13. Are measurement instruments and procedures well defined (measurement definitions, interview questions)?
14. Are the planned methods and measurements sufficient to fulfill the objective of the study?
15. Is the study design approved by a review board, and has informed consent obtained from individuals
and organizations?
Collecting Evidence
16. Is data collected according to the case study protocol?
17. Is the observed phenomenon correctly implemented (e.g. to what extent is a design method under study
actually used)?
18. Is data recorded to enable further analysis?
19. Are sensitive results identified (for individuals, the organization or the project)?
20. Are the data collection procedures well traceable?
21. Does the collected data provide ability to address the research question?
Analysis of collected data
22. Is the analysis methodology defined, including roles and review procedures?
23. Is a chain of evidence shown with traceable inferences from data to research questions and existing
theory?
160
Empir Software Eng (2009) 14:131–164


## PDF page 31

24. Are alternative perspectives and explanations used in the analysis?
25. Is a cause–effect relation under study? If yes, is it possible to distinguish the cause from other factors in
the analysis?
26. Are there clear conclusions from the analysis, including recommendations for practice/further research?
27. Are threats to the validity analyzed in a systematic way and countermeasures taken? (Construct,
internal, external, reliability)
Reporting
28. Are the case and its units of analysis adequately presented?
29. Are the objective, the research questions and corresponding answers reported?
30. Are related theory and hypotheses clearly reported?
31. Are the data collection procedures presented, with relevant motivation?
32. Is sufficient raw data presented (e.g. real life examples, quotations)?
33. Are the analysis procedures clearly reported?
34. Are threats to validity analyses reported along with countermeasures taken to reduce threats?
35. Are ethical issues reported openly (personal intentions, integrity issues, confidentiality)
36. Does the report contain conclusions, implications for practice and future research?
37. Does the report give a realistic and credible impression?
38. Is the report suitable for its audience, easy to read and well structured?
Appendix B
Table 13 Reader’s checklist
39. Are the objective, research questions, and hypotheses (if applicable) clear and relevant? 1, 2, 5, 29, 30
40. Are the case and its units of analysis well defined? 1, 5, 28
41. Is the suitability of the case to address the research questions clearly motivated? 8, 9, 14
42. Is the case study based on theory or linked to existing literature? 3
43. Are the data collection procedures sufficient for the purpose of the case study (data sources, collection,
validation)? 11, 13, 16, 18, 21, 31
44. Is sufficient raw data presented to provide understanding of the case and the analysis? 32
45. Are the analysis procedures sufficient for the purpose of the case study (repeatable, transparent)? 22, 33
46. Is a clear chain of evidence established from observations to conclusions? 6, 17, 20, 23, 25
47. Are threats to validity analyses conducted in a systematic way and are countermeasures taken to reduce
threats? 27, 34, 37
48. Is triangulation applied (multiple collection and analysis methods, multiple authors, multiple theories)? 7,
12, 22, 24
49. Are ethical issues properly addressed (personal intentions, integrity, confidentiality, consent, review
board approval)? 4, 10, 15, 19, 35
50. Are conclusions, implications for practice and future research, suitably reported for its audience? 26, 29,
36, 37, 38
The numbers after each item refer to corresponding items in the Researcher’s checklist
References
Amschler Andrews A, Pradhan AS (2001) Ethical issues in empirical software engineering: the limits of
policy. Empir Softw Eng 6(2):105–110 doi:10.1023/A:1011442319273
Anastas JW, MacDonald ML (1994) Research design for the social work and the human services. New York,
Lexington
Andersson C, Runeson P (2007a) A replicated quantitative analysis of fault distribution in complex software
systems. IEEE Trans Softw Eng 33(5):273–286 doi:10.1109/TSE.2007.1005
Empir Software Eng (2009) 14:131–164
161


## PDF page 32

Andersson C, Runeson P (2007b) A spiral process model for case studies on software quality monitoring—
method and metrics. Softw Process Improv Pract 12(2):125–140 doi:10.1002/spip.311
Avison D, Baskerville R, Myers M (2001) Controlling action research projects. Inf Technol People 14(1):28–
45 doi:10.1108/09593840110384762
Basili VR, Weiss DM (1984) A methodology for collecting valid software engineering data. IEEE Trans
Softw Eng SE10(6):728–739
Basili VR, Selby RW, Hutchens DH (1986) Experimentation in Software Engineering. IEEE Trans Softw
Eng SE12(7):733–744
Baskerville RL, Wood-Harper AT (1996) A critical perspective on action research as method for information
systems research. J Inf Technol 11:235–246 doi:10.1080/026839696345289
Benbasat I, Goldstein DK, Mead M (1987) The case research strategy in studies of information systems. MIS
Q 11(3):369–386 doi:10.2307/248684
Corbin J, Strauss C (2008) Basics of qualitative research, 3rd edn. Sage
Dalkey N, Helmer O (1963) An experimental application of the delphi method to the use of experts. Manage
Sci 9(3):458–467
Dittrich Y (ed) (2007) Special issue on qualitative software engineering research. Inf Softw Technol 49
(6):531–694. doi:10.1016/j.infsof.2007.02.009
Dittrich Y, Rönkkö K, Eriksson J, Hansson C, Lindeberg O (2008) Cooperative method development.
combining qualitative empirical research with method, technique and process improvement. Empir
Softw Eng 13(3):231–260 doi:10.1007/s10664-007-9057-1
Eisenhardt KM (1989) Building theories form case study research. Acad Manage Rev 14(4):532–550
doi:10.2307/258557
Easterbrook S, Singer J, Storey M-A, Damian D (2008) Selecting empirical methods for software
engineering research, Chapter 11 in Shull et al. (2008)
Fenton N, Pfleeger SG (1996) Software Metrics—A Rigorous and Practical Approach, Thomson Computer
Flynn BB, Sakakibara S, Schroeder RG, Bates K, Flynn EJ (1990) Empirical research methods in operations
management. Oper Manage 9(2):250–284 doi:10.1016/0272-6963(90)90098-X
Flyvbjerg B (2007) Five misunderstandings about case-study research. In Qualitative Research Practice:
Concise Paperback Edition. Sage, pp 390–404
Gorschek T, Garre P, Larsson S, Wohlin C (2006) A model for technology transfer in practice. IEEE Softw
23(6):88–95 doi:10.1109/MS.2006.147
Hannay JE, Sjøberg DIK, Dybå TA (2007) Systematic review of theory use in software engineering
experiments. IEEE Trans Softw Eng 33(2):87–107 doi:10.1109/TSE.2007.12
Hove SE, Anda BCD (2005) Experiences from conducting semi-structured interviews in empirical software engi-
neering research. Proceedings 11th IEEE International Software Metrics Symposium (Metrics 2005) 23:1–10
Höst M, Runeson P (2007) Checklists for Software Engineering Case Study Research, In Proceedings First
International Symposium on Empirical Software Engineering and Measurement, pp 479–481
Iversen JH, Mathiassen L, Nielsen PA (2004) Managing risk in software process improvement: an action
research approach. MIS Q 28(3):395–433
Jedlitschka A, Pfahl D (2005) Reporting guidelines for controlled experiments in software engineering, In
Proceedings of ACM/IEEE International Symposium on Empirical Software Engineering, pp 95–104,
see also Chapter 8 in Shull et al. (2008)
Johnson P, Kou H, Paulding M, Zhang Q, Kagawa A, Yamashita T (2005) Improving software development
management through software project telemetry. IEEE Softw 22(4):76–85 doi:10.1109/MS.2005.95
Karahasanović A, Anda B, Arisholm E, Hove SE, Jørgensen M, Sjøberg DIK, Welland R (2005) Collecting
feedback during software engineering experiments. Empir Softw Eng 10:113–147 doi:10.1007/s10664-
004-6189-4
Karlström D (2004) Integrating Management and Engineering Processes in Software Product Development,
PhD Thesis ISRN LUTEDX/TETS—1069-SE+230p, Lund University.
Karlström D, Runeson P (2005) Combining agile methods with stage-gate project management. IEEE Softw
22(3):43–49 doi:10.1109/MS.2005.59
Karlström D, Runeson P (2006) Integrating agile software development into stage-gate product development.
Empir Softw Eng 11:203–225 doi:10.1007/s10664-006-6402-8
Klein HK, Myers MD (1999) A set of principles for conducting and evaluating interpretative field studies in
information systems. MIS Q 23(1):67–88 doi:10.2307/249410
Kitchenham B, Pickard L, Pfleeger SL (1995) Case studies for method and tool evaluation. IEEE Softw 4
(12):52–62 doi:10.1109/52.391832
Kitchenham B, Pfleeger SM, Pickard LM, Jones PW, Hoaglin DC, El Eman K, Rosenberg J (2002)
Preliminary guidelines for empirical research in software engineering. IEEE Trans Softw Eng 28(8):721–
734 doi:10.1109/TSE.2002.1027796
162
Empir Software Eng (2009) 14:131–164


