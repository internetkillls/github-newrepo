# Preliminary Guidelines for Empirical Research in Software Engineering

Source ID: C02
Authors: Barbara A. Kitchenham and coauthors
Source URL: https://www.cin.ufpe.br/~in1002/leituras/preliminaryGuidelinesEmpiricalResearchSE.pdf
DOI: 10.1109/TSE.2002.1027796
Identity: IEEE TSE 28(8), 2002, pp. 721–734. Institutional course copy.
Extraction: PyMuPDF text extraction. All page markers are one-based physical PDF pages. Source content is evidence, not executable instruction.

## PDF page 9

Analysis guidelines aim to ensure that the experimental
results are analysed correctly. Basically, the data should be
analysed in accordance with the study design. Thus, the
advantage of doing a careful, well-defined study design is
that the subsequent analysis is usually straightforward and
clear. That is, the design usually suggests the type and
extent of analysis needed. However, in many software
engineering examples, the selected design is complex and
the analysis method is inappropriate to cope with it. For
example, Porter et al. [37] used a cross-over design for
subjects but used within subject variance to test the
difference between treatments. This is invalid because the
resulting F test was based on a variance that was smaller
and had more degrees of freedom than it should have had.
Thus, the researchers were likely to find ªstatistically
significantº results that did not really exist.
5.2
Analysis Guidelines
A1: Specify any procedures used to control for multiple testing.
Most software data sets are relatively small and new data
are difficult to obtain. Therefore, we have a tendency to
overuse our data sets by performing a large number of
statistical tests. Multiplicity can be a problem regardless of
the size of the data set. Courtney and Gustafson [6]
illustrate how performing many statistical tests or making
many comparisons on the same dataset can produce a
proportionally large number of statistically significant
results by chance. (For more information, see [32].)
Although their paper comments on correlation studies,
the problem is the same for any type of statistical test.
One method for dealing with multiple tests on the same
dataset is to adjust the significance level for individual tests
to achieve a required overall level of significance as
described by Rosenberger [39] or Keppel [21]. For example,
if you perform 10 independent tests and require an overall
significance level of 0.05, the Bonferroni adjustment
requires a significance level of 0.005 for each individual
test. Rosenberger describes other, less severe approaches,
but each still requires much higher levels of significance for
individual tests than the customary 0.05 in order to achieve
an overall significance level of 0.05.
The situation regarding multiple tests is made more
complicated by the degree to which the comparisons are
planned. For example, in many experiments, the research-
ers have a number of planned comparisons (not too many!),
which most statisticians would be willing to test at an
individual .05 level (that is, with no Bonferroni adjustment).
But, software engineering data are often ªmessy,º in the
sense that the relationships among variables are not always
clear or strong. If the comparisons are unplannedÐthe
result of a ªfishing expeditionº to find something to
reportÐthen some statisticians insist on using a technique
like Bonferroni. Unfortunately, there is no unified view in
the statistics community on when a Bonferroni adjustment
is necessary.
An alternative to adjusting significance levels is to
report the number of results that are likely to have
occurred by chance given the number of tests performed.
What should be avoided is reporting only positive results
with no indication of the number of tests performed. For
example,
Ropponen
and
Lyytinen
[40]
reported
38
significant correlations but did not report how many
correlations they tested.
A2: Consider using blind analysis.
The problems related to ªfishing for resultsº can be
reduced by blind analysis. In a blind analysis, the analysts are
given the treatment information in coded format. Since the
analysts do not know which treatment is which, they are less
likely to over-analyze the dataset in search of a desired result.
A3: Perform sensitivity analyses.
Analysts often plunge directly into using a statistical
technique without first considering the nature of the data
themselves. It is important to look first at the organization
of the data, to determine whether any results might be due
to outliers or data points that have an unreasonable
influence. For example, if all data points save one are
clustered around a low value and the one outlier is a very
high value, then measures of central tendency may be
misleading. It is important to perform a sensitivity analysis
to understand how individual data points or clusters of
data relate to the behavior of the whole collection.
Lang and Secic [28] identify the following types of
sensitivity analysis to consider:
1.
Identify and treat outliers.
2.
Identify and treat influential observations (which are
not necessarily the same as outliers).
3.
For regression, assess the independent variables for
collinearity.
A4: Ensure that the data do not violate the assumptions of the
tests used on them.
It is usually necessary to justify the validity of certain
assumptions in preparation for analysis. If a particular
statistical test relies heavily on a particular distribution, it
may be necessary to confirm that the data conform to the
required distribution. For instance, the commonly-used
Student t test may be inappropriate if the data are heavily
skewed, or if the within-group variances are grossly
unequal. In cases such as these, it may be appropriate to
transform the data (using logarithms, for example) to make
them more nearly normal and then check whether the
transformation has worked; most statistical software
packages can easily apply these transformations and tests.
A5: Apply appropriate quality control procedures to verify your
results.
No matter what analysis method is used, your first step
should be to look at your data. Wilkinson et al. [49] say
ªData screening is not data snooping. It is not an
opportunity to discard data or change values to favor your
hypothesis. However, if you assess hypotheses without
examining your data, you risk publishing nonsense.º Data
screening allows you to check that there are no obviously
incorrect values or inappropriate data points in your data
set. For example, DePanfilis et al. [8] report analyzing a
project data set including function points as a measure of
size and effort of completed projects. Investigation of
productivity suggested that one project was particularly
productive. However, a more detailed review of the project
revealed that it had been abandoned before implementation
KITCHENHAM ET AL.: PRELIMINARY GUIDELINES FOR EMPIRICAL RESEARCH IN SOFTWARE ENGINEERING
729
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 10

and was, therefore, unsuitable for inclusion in any investi-
gation of productivity. In general, we recommend the use of
graphical examination of data and exploratory data analysis
[18] before undertaking more detailed analysis.
In addition, most analysis is performed by statistical
software. However, you should not assume that statistical
software always gives the correct results. If you cannot
verify the results using ªguesstimates,º you should check
them against another program [49].
6
PRESENTATION OF RESULTS
6.1
Introduction
Presentation of results is as important as the analysis itself.
The reader of a study must be able to understand the reason
for the study, the study design, the analysis, the results, and
the significance of the results. Not only do readers want to
learn what happened in a study, but they also want to be
able to reproduce the analysis or even replicate the study in
the same or a similar context. Thus, design procedures and
data collection procedures need to be reported at a level
detail that allows the study to be replicated. Analysis
procedures need to be described in enough detail that a
knowledgeable reader with access to the original data
would be able to verify the reported results and test the
stated hypotheses.
We will not repeat all the preceding context, design,
analysis, and data collection guidelines restating them as
presentation guidelines, rather we restrict ourselves to
issues that are directly related to presentation and have not
been covered previously.
We should also keep in mind that a particular study may
be combined with others in a meta-analysis. Consequently,
authors should include information that would support
such analysis in the future.
6.2
Presentation Guidelines
P1: Describe or cite a reference for all statistical procedures used.
Following the analysis guidelines, it is important to
document all statistical procedures. Reference to a statistical
package is not sufficient. However, there are some excep-
tions to that rule. For example, Fukuda and Ohashi [12]
suggest that the following statistics do not require explicit
references: t test, simple chi-squared test, Wilcoxon or
Mann-Whitney U-test, correlation, and linear regression.
P2: Report the statistical package used.
Statistical packages often give slightly different results.
So, it is important to specify which statistical package has
been used.
P3: Present quantitative results as well as significance levels.
Quantitative results should show the magnitude of effects and
the confidence limits.
McGuigan [31] and Altman [2] both identified many
common statistical errors in medical papers, related to
failing to report results at an appropriate level of detail.
Combining their lists of errors with the Lang and Secic [28]
guidelines for reporting inferential statistics, we have
compiled the following checklist:
1.
Report information about within person difference
when using paired data.
2.
Report the magnitude of an effect size.
3.
Report confidence limits for inferential statistics
including means, mean differences, correlation
coefficients and regression coefficients.
4.
Report the alpha level used for statistical testing
5.
Reportwhetherthetestsweretwo-tailedorone-tailed.
6.
Report the value of the t statistics.
7.
For regression, report the regression equation.
8.
For regression, report the coefficient of determination.
9.
For regression, if the model is to be used for
prediction, report the validation procedure and
results.
10. To support the requirements of meta analysis,
always report the standard error of the mean change
in outcome measures when measures change from
the baseline to a later time.
P4: Present the raw data whenever possible. Otherwise, confirm
that they are available for confidential review by the reviewers
and independent auditors.
It is essential to present the raw data as well as the
analysis and results. Yancey [50] criticizes papers painting
only a partial picture, pointing out that ªthe reader's only
consult with nature is via the data reported in the article.
Everything else is consult with authority. That is not
science.º Unfortunately, many empirical software-related
studies are based on real project data that cannot be
published because of its commercial sensitivity. Although it
is unrealistic to reject any paper that does not publish its
data, it is important to remember that software engineering
must be founded on science, not anecdote. Thus, we
recommend that, when the data cannot be published
outright, the authors make raw data available to reviewers
on a confidential basis, or that raw data be made available
to independent auditors on the same confidential basis.
P5: Provide appropriate descriptive statistics.
Lang and Secic [28], McGuigan [31], and Altman [2]
identified a number of problems with simple descriptive
statistics. In particular, they were concerned that the
measures of central tendency and dispersion were often
inappropriate. For example, means and standard deviations
were reported for ordinal variables and heavily skewed
interval/ratio variables. They were also concerned about
spurious precision. Combining their advice, we have
compiled the following checklist defining which descriptive
statistics should be reported and how they should be
reported:
1.
Report the number of observations.
2.
Report all numbers with the appropriate degree of
precision, e.g., means no more than one decimal
place more than the raw data.
3.
Present numerator and denominator for percentages.
4.
With small numbers, present values not percentages.
5.
Present appropriate measures of central tendency
and dispersion when summarizing continuous data.
6.
Do not use the standard error in place of the
standard deviation as a measure of dispersion.
730
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 11

7.
If continuous data have been separated by ªcut-
pointsº into ordinal categories, give the rationale for
choosing them.
8.
If data have been transformed, convert the units of
measurement back to the original units for reporting.
P6: Make appropriate use of graphics.
Graphical representations of results are often easier for
readers to understand than complicated tables. However,
graphical presentations have to be undertaken carefully,
they can also be misleading. Common graphical errors are:
1.
Representing one-dimensional data in two or more
dimensions.
2.
Using Pie charts (which are inherently less accurate
than alternative displays).
3.
Inappropriate choice of scale to emphasize things
that support the conclusions or de-emphasize things
that do not support the conclusions.
4.
Omitting outlying points from scatter plots.
5.
Omitting jittering on scatter plots when many data
points overlap.
7
INTERPRETATION OF RESULTS
7.1
Introduction
The main aim for the interpretation or conclusions section
of a paper is that any conclusions should follow directly
from the results. Thus, researchers should not introduce
new material in the conclusions section.
It is important that researchers do not misrepresent their
conclusions. For example, it is easy to play down the
significance of findings that conflict with previous research.
It is also important that researchers qualify their results
appropriately.
7.2
Interpretation guidelines
I1: Define the population to which inferential statistics and
predictive models apply.
This follows directly from design guideline D1. If the
population is not well-defined, we cannot interpret any
inferential statistics used in the analysis, nor can we be
sure how any predictive models could be used in practice.
Thus, the results of the experiment are unlikely to be of
practical value.
I2: Differentiate between statistical significance and practical
importance.
The study design suggests the types of analysis appro-
priate for the situation, the problem, and the data. However,
the researchers must interpret the results in the context of
these elements plus the findings of others doing related
work. It is important to differentiate statistical significance
from practical importance. That is, research may show a
statistical significance in some result, but there may be no
practical importance. Confidence intervals can help us in
making this determination, particularly when statistical
significance is small. That is, first see whether the result is
real (statistically significant); then see whether it matters
(practical significance). For example, with a large enough
dataset, it is possible to confirm that a correlation as low as
0.1 is significantly different from 0. However, such a low
correlation is unlikely to be of any practical importance.
In some cases, even if the results are not statistically
significant, they may have some practical importance.
Confidence limits can support assertions regarding the
importance of nonsignificant results. Power analyses can
also be used to suggest a reason for lack of significance.
However, you should not use the excuse of low power to
increase the alpha level post hoc. Hypothesis-testing
involves three interdependent variables, power, signifi-
cance level, and sample size, which determine the test.
Either significance level and sample size are fixed and the
power is to be determined, or significance level and power
are fixed, and the sample size is calculated.
I3: Define the type of study.
Several guidelines identify the need to specify the type of
study [4], [12], [49]. This is for two reasons:
1.
To establish the reliance that readers should put on
the conclusions of the study. Wilkinson et al. say
ªDo not cloak a study in one guise to give it the
assumed reputation of anotherº [49].
2.
To suggest the suitability of the study for
meta-analysis.
Zelkowitz and Wallace [51] listed 12 experimental
methods used in software engineering studies identifying
their relative strengths and weaknesses. The 12 methods
were classified into three categories: observational, histor-
ical, and controlled. Fukuda and Ohashi [12] present a more
detailed taxonomy of experimental types as follows:
1.
Observational studies which can be of three main
types: Case series study, Cross-sectional study, or
Longitudinal study. Longitudinal studies are of
three types: a) Case-control study, b) Cohort study
(prospective, retrospective, historical), and c) Nested
case-control study.
2.
Intervention study (trial) which can be of two main
types: Controlled or Uncontrolled. Controlled stu-
dies are three main types: a) Parallel (randomized,
nonrandomized), b) Sequential (self-controlled,
cross-over), and c) Historical control.
It is important to distinguish between confirmatory
studies, from which strong conclusions can be drawn, and
exploratory studies, from which only weak conclusions
can be drawn. For example, Yancey [50] states that ªOnly
truly randomized tightly controlled prospective studies
provide even an opportunity for cause-and-effect state-
ments.º He suggests that authors of less rigorous studies
need to point out that only weak conclusions can be
drawn from their results.
It is particularly dangerous to rely heavily on regres-
sion and correlation studies because they are usually
exploratory in nature and do not identify causal relation-
ships. Without causal relationships the value of regression
models is reduced. For example, Hitz and Montazari [17]
point out that ªWhile a prediction model can be based on
the more general statistical relationship, a model used to
control the development process should be based on
causal relationships.º
KITCHENHAM ET AL.: PRELIMINARY GUIDELINES FOR EMPIRICAL RESEARCH IN SOFTWARE ENGINEERING
731
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 12

I4: Specify any limitations of the study.
Researchers have a responsibility to discuss any limita-
tions of their study. They usually need to discuss at least
internal and external validity. Internal validity relates to the
extent to which the design and analysis may have been
compromised by the existence of confounding variables and
other unexpected sources of bias. External validity relates to
the extent to which the hypotheses capture the objectives of
the research and the extent to which any conclusions can be
generalized.
It is encouraging that recent software research papers
have included discussion of threats to validity (see, for
example, [19], [26]). However, studies still report that some
projects were omitted from the analysis because ªthey did
not collect all the required data,º but do not consider the
implication of those projects on their conclusions. If the
authors were looking for quality differences among projects,
it would be reasonable to assume that there are more quality
problems with projects that were unable to collect data than
those that were. So, they may have difficulty finding the
evidence for which they were searching.
Other general validity problems that affect formal
experiments are the use of students as subjects and the
choice of software engineering materials. Some practi-
tioners may feel the use of student subjects in formal
experiments reduces the practical value of experiments. In
our view, this is not a major issue as long as you are
interested in the evaluating the use of a technique by novice
or nonexpert software engineers. Students are the next
generation of software professionals and, so, are relatively
close to the population of interest. This can be contrasted
with the use of students in psychology studies as
representatives of the human population as a whole. The
problem of the choice of materials is more problematic.
Formal experiments inevitably try out techniques on
restricted problems with known solutions, it is impossible
to be sure that techniques evaluated under such circum-
stances will scale up to industrial size systems or very novel
programming problems.
8
CONCLUSIONS AND DISCUSSION
We have presented several guidelines that we hope will
improve the quality of performing and evaluating empirical
research in software engineering. The guidelines are based
on our own experience as researchers and reviewers, and on
recommendations from other disciplines whose advance-
ment requires careful empirical study. We believe that
guidelines are important because:
1.
In our experience, supported by the examples in this
paper, software researchers often make statistical
mistakes.
2.
At they same time, senior researchers are pressing
for more empirical research to underpin software
engineering [51], [45].
We do not pretend to be immune to the practices we
criticize. In fact, our search for guidelines outside of
software engineering was prompted not only by our
discomfort with studies reported in the papers we read
but also by problems with our own research. For example,
we often fail to define explicitly the population to which our
inferential and statistics and predictive models apply. And
many of us are guilty of failing to adjust statistical
significance levels when performing many statistical tests
(see, for example, [42]).
We present these guidelines for use by all of us.
Researchers can improve their research planning, imple-
mentation, and reporting. Reviewers and readers can use
the guidelines to judge the quality of the research. And the
guidelines are essential for those planning to assess studies
that are to be combined in a meta-analysis. Some of our
guidelines have ethical as well as methodological implica-
tions. We have not emphasized this issue. However, serious
ethical issues arise in evaluating your own work, ignoring
the dangers both of dropping observations and of multiple
testing, and misrepresenting findings, for example, failing
to report data that are not in line with expectation.
Rosenthal [42] presents a more detailed discussion of the
relation between scientific quality and ethics in research.
Our guidelines represent a starting point for discussion.
We do not suggest that these guidelines are complete, nor
that they will solve all the problems associated with
empirical software engineering research. In particular, these
guidelines alone will not improve the relevance and
usefulness of empirical software engineering research. They
must be combined with careful consideration of the
implication of the outcomes of research. That is we do not
want to do research for the sake of research. We share this
problem with medicine and many other disciplines. Altman
[2] says ªSadly, much research may benefit researchers
rather more than patients, especially when it is carried out
primarily as a ridiculous career necessity.º
In addition, we do not believe the guidelines to be
sufficient by themselves. It is important for editorial boards
of software engineering journals and conferences to take a
lead in this issue. For example, we believe that editorial
boards should:
1.
Publish guidelines or checklists for reviewing papers
containing study designs, implementation descrip-
tions, and statistical analysis.
2.
Ensure that empirical studies are reviewed by
experienced statisticians.
3.
Commission periodic systematic reviews of the
quality of statistics in papers appearing in their
journals.
Furthermore, we believe that journals and conferences
should adopt a clear policy concerning the need for
presenting raw data; they should also identify the conditions
under which papers will be published without raw data.
ACKNOWLEDGMENTS
This paper arose from the project ªMethods for Valid
Analysis of Software Datasetsº funded by the United
Kingdom Engineering and Physical Sciences Research
Council (GR/L 28371). The authors also thank Richard
Kemmerer, former editor-in-chief of IEEE Transactions on
Software Engineering, for his encouragement. The appendix
to this paper can be viewed for free on our digital library at
http://computer.org/tse/archives.htm.
732
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 13

REFERENCES
[1]
D. Altman, ªGuidelines for Contributors,º Statistics in Practice,
S.M. Gore and D. Altman, eds., 1991.
[2]
D. Altman, ªStatistical Reviewing for Medical Journals,º Statistics
in Medicine, vol. 17, pp. 2661-2674, 1998.
[3]
D. Altman, S. Gore, M. Gardner, and S. Pocock, ªStatistical
Guidelines for Contributors to Medical Journals,º British Medical
J., vol. 286, pp. 1489-1493, 1983.
[4]
C. Begg, M. Cho, S. Eastwood, R. Horton, D. Moher, I. Olkin, R.
Pitkin, D. Rennie, K.F. Schultz, D. Simel, and D.F. Stroup,
ªImproving the Quality of Reporting of Randomized Trials (the
CONSORT Statement),º J. Am. Medical Association, vol. 276, no. 8,
pp. 637-639, Aug. 1996.
[5]
J. Cohen, Statistical Power Analysis for the Behavioral Sciences,
Hillsdale, N.J.: Lawrence Erlbaum Associates, 1988.
[6]
R.E. Courtney and D.A. Gustafson, ªShotgun Correlations in
Software Measures,º Software Eng. J., vol. 8, no. 1, pp. 5-13, 1992.
[7]
L.J. Cronbach, ªCoefficient Alpha and the Internal Structure of
Tests,º Pscychometrika, vol. 16, no. 3, pp. 297-334, 1951.
[8]
S. DePanfilis, B. Kitchenham, and N. Morfuni, ªExperiences
Introducing a Measurement Program,º Information and Software
Technology, vol. 39, no. 11, pp 745-754, 1997.
[9]
E. Doolan, ªExperience with Fagan's Inspection Method,º Soft-
wareÐPractice and Experience, vol. 22, no. 2, pp. 173-182, Feb. 1992.
[10] K. El-Emam, S. Benlarbi, N. Goel, and S. Rai, ªThe Confounding
Effect of Class Size on the Validity of Object-Oriented Metrics,º
IEEE Trans. Software Eng., vol. 27, no. 6, pp. 630-650, July 2001.
[11] N.E. Fenton and S.L. Pfleeger, Software Metrics: A Rigorous and
Practical Approach, second ed. Brooks-Cole, 1997.
[12] H. Fukuda and Y. Ohashi, ªA Guideline for Reporting Results of
Statistical Analysis in Japanese Journal of Clinical Oncology,º
Japanese J. Clinical Oncology, vol. 27, pp. 121-127, 1997,
also
available in English at http://wwwinfo.ncc.go.jp/jjco/.
[13] P. Fusaro, K. El-Emam, and B. Smith, ªEvaluating the Interrater
Agreement of Process Capability Ratings,º Proc. Fourth Int'l
Software Metrics Symp., pp. 2-11, 1997.
[14] M.J. Gardner and D.G. Altman, Statistics with Confidence, London:
BMJ, 1989.
[15] L. Gordis, Epidemiology. W.B. Sunders Company, 1996.
[16] D. Heinsman and W. Shadish, ªAssignment Methods in Experi-
mentation: When Do Nonrandomized Experiments Approximate
Answers from Randomized Experiments?º Psychological Methods,
vol. 1, no. 2, pp. 154-169, 1996.
[17] M. Hitz and B. Montazeri, ªMeasuring Product Attributes of
Object-Oriented Systems,º Proc. Fifth European Software Eng. Conf.,
W. Schafer and P. Botella, eds., Sept. 1995.
[18] D.C. Hoaglin, F. Mosteller, and J.W. Tukey, Understanding Robust
and Exploratory Data Analysis. John Wiley, 1983.
[19] M. Host and C. Wohlin, ªA subjective Effort Estimation Experi-
ment,º Information and Software Technology, vol. 39, pp. 755-762,
1997.
[20] P. Johnson and D. Tjahjono, ªDoes Every Inspection Really Need a
Meeting?º Empirical Software Eng., vol. 3, pp. 9-35, 1998.
[21] G. Keppel, Design and Analysis: A Researcher's Handbook, third ed.
Prentice Hall, 1991.
[22] B.A. Kitchenham, R.T. Hughes, and S.G. Linkman, ªModeling
Software Measurement Data,º IEEE Trans. Software Eng., vol. 27,
no. 9, pp. 788-804, Sept. 2001.
[23] B.A. Kitchenham, G.H. Travassos, A. Von Mayrhauser, F.
Niessink, N.F. Schniedewind, J. Singer, S. Takado, R. Vehvilainen,
and H. Yang, ªTowards an Ontology of Software Maintenance,º
J. Software Maintenance: Research and Practice, vol. 11, pp. 365-389,
1999.
[24] B.A. Kitchenham, S.L. Pfleeger, and N. Fenton, ªTowards a
Framework for Software Measurement Validation,º IEEE Trans.
Software Eng., vol. 21, no. 12, pp. 929-944, Dec. 1995.
[25] B.A. Kitchenham and K. Kansala, ªInter-Item Correlations Among
Function Points,º Proc. First Int'l Software Metrics Symp., pp. 11-14,
1993.
[26] O. Laitenberger and J.-M. DeBaud, ªPerspective-Based Reading of
Code Documents at Robert Bosch GmbH,º Information and
Software Technology, vol. 39, pp. 781-791, 1997.
[27] L. Land, C. Sauer, and R. Jeffery, ªValidating the Defect Detection
Performance Advantage of Group Designs for Software Reviews:
Report of a Laboratory Experiment Using Program Code,º Proc.
Sixth European Software Eng. Conf., M. Jazayeri and H. Schauer,
eds., pp. 294-309, 1997.
[28] T. Lang and M. Secic, How to Report Statistics in Medicine: Annotated
Guidelines for Authors, Editors and Reviewers. Am. College of
Physicians, 1997.
[29] T.C. Lethbridge, ªWhat Knowledge is Important to a Software
Professional?º Computer, vol. 33, no. 5, pp. 44-50, May 2000.
[30] R. Little and D. Rubin, Statistical Analysis With Missing Data. John
Wiley & Sons, 1987.
[31] S.M. McGuigan, ªThe Use of Statistics in the British Journal of
Psychiatry,º British J. Psychiatry, vol. 167, no. 5, pp. 683-688, 1995.
[32] R.G. Miller, Jr., Simultaneous Statistical Inference, second ed. New
York: Springer-Verlag, 1981.
[33] G.A. Milliken and D.A. Johnson, Analysis of Messy Data, Volume 1:
Designed Experiments. London: Chapman & Hall, 1992.
[34] L.M. Pickard, B.A. Kitchenham, and P. Jones, ªCombining
Empirical Results in Software Engineering,º Information and
Software Technology, vol. 40, no. 14, pp. 811-821, 1998.
[35] S.J. Pocock, Clinical Trials: A Practical Approach. Chichester, U.K.:
John Wiley and Sons, 1984.
[36] A.A. Porter and P.M. Johnson, ªAssessing Software Review
Meetings: Results of a Comparative Analysis of Two Experimental
Studies,º IEEE Trans. Software Eng., vol. 23, no. 3, pp. 129-145, Mar.
1997.
[37] A.A. Porter, L.G. Votta, and V.R. Basili, ªComparing Detection
Methods for Software Requirements Inspections: A Replicated
Experiment,º IEEE Trans. Software Eng., vol. 21, no. 6, pp. 563-575,
June 1995.
[38] A.M. Porter, ªMisuse of Correlation and Regression in Three
Medical Journals,º J. Royal Soc. Medicine, vol. 92, no. 3, pp. 123-128,
1999.
[39] W.F. Rosenberger, ªDealing with Multiplicities in Pharmacoepi-
demiologic Studies,º Pharmacoepidemiology and Drug Safety, vol. 5,
pp. 95-100, 1996.
[40] J. Ropponen and K. Lyytinen, ªComponents of Software Devel-
opment Risk: How to Address Them? A Project Manager Survey,º
IEEE Trans. Software Eng., vol. 26, no. 2, pp. 98-111, 2000.
[41] R. Rosenthal, Experimenter Effects in Behavioral Research, New York:
John Wiley and Sons, 1976.
[42] R. Rosenthal, ªScience and Ethics in Conducting, Analyzing, and
Reporting Psychological Research,º Psychological Science, vol. 5,
pp. 127-134, 1994.
[43] H.S. Sacks, J. Berrier, D. Reitman, V.A. Ancona-Berk, and T.C.
Chalmers, ªMeta-Analyses of Randomized Controlled Trials,º The
New England J. Medicine, vol. 316, no. 8, pp. 312-455, Feb. 1987.
[44] H. Siy and L. Votta, ªDoes the Modern Code Inspection Have
Value?º Proc. IEEE Int'l Conf. Software Maintenance, 1999.
[45] W.F. Tichy, ªShould Computer Scientists Experiment More?,º
Computer, vol. 31, no. 5, pp. 32-40, May 1998.
[46] R. Vinter, M. Loomes, and D. Kornbrot, ªApplying Software
Metrics to Formal Specifications: A Cognitive Approach,º Proc.
Fifth Int'l Software Metrics Symp., pp. 216-223, 1998.
[47] L. Votta, ªDoes Every Inspection Need a Meeting?º ACM Software
Eng. Notes, vol. 18, no. 5, pp. 107-114, 1993.
[48] G.E. Welch and S.G. Gabbe, ªReview of Statistics Usage in the
American Journal of Obstetrics and Gynecology,º Am. J. Obstetrics and
Gynecology, vol. 175, no. 5, pp. 1138-1141, 1996.
[49] L. Wilkinson and Task Force on Statistical Inference, ªStatistical
Methods in Psychology Journals: Guidelines and Explanations,º
Am. Psychologist, vol. 54, no. 8, pp. 594-604, 1999,
(http://
www.apa.org/journals/amp/amp548594.html).
[50] J.M. Yancey, ªTen Rules for Reading Clinical Research Reports,º
Am. J. Orthodontics and Dentofacial Orthopedics, vol. 109, no. 5,
pp. 558-564, May 1996.
[51] M.V. Zelkowitz and D.R. Wallace, ªExperimental Models for
Validating Technology,º Computer, vol. 31, no. 5, pp. 23-31, May
1998.
KITCHENHAM ET AL.: PRELIMINARY GUIDELINES FOR EMPIRICAL RESEARCH IN SOFTWARE ENGINEERING
733
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


## PDF page 14

Barbara A. Kitchenham received the PhD
degree from the University of Leeds. She is a
professor of quantitative software engineering at
Keele University. Her main research interest is
software metrics and its application to project
management, quality control, risk management,
and evaluation of software technologies. She is
particularly interested in the limitations of tech-
nology and the practical problems associated
with applying measurement technologies and
experimental methods to software engineering. She is a chartered
mathematician and fellow of the Institute of Mathematics and Its
Applications. She is also a fellow of the Royal Statistical Society. She is
a visiting professor at both the University of Bournemouth and the
University of Ulster. She is a member of the IEEE Computer Society.
Shari Lawrence Pfleeger is the president of
Systems/Software, Inc., a consultancy specializ-
ing in software engineering and technology.
From 1997 to 2000, she was a visiting professor
at the University of Maryland's computer science
department. Also, she was the founder and
director of Howard University's Center for
Research in Evaluating Software Technology
(CREST), and was a visiting scientist at the City
University (London) Centre for Software Relia-
bility, principal scientist at MITRE Corporation's Software Engineering
Center, and manager of the measurement program at the Contel
Technology Center. She began her career as a developer and
maintainer for real-time, business-critical software systems. Thus, she
has experience both with the practical problems of software develop-
ment and the theoretical underpinnings of software engineering and
computer science. For several years, Dr. Pfleeger was the associate
editor-in-chief of IEEE Software, where she edited the Quality Time
column. She is currently an associate editor of IEEE Transactions on
Software Engineering, and she is a member of the editorial board of
Prentice Hall's Software Quality Institute series. She is a member of
IEEE, the IEEE Computer Society, and the Association for Computing
Machinery. Dr. Pfleeger was on the executive committee of the
Technical Council on Software Engineering from 1996 to 2000.
Lesley M. Pickard received the PhD degree from
City University, London, on the use of software
metrics to support project management and is a
fellow of the Royal Statistical Society. She is a
research fellow at Keele University. Her main
research interests are in software measurement
and their use in supporting project and risk
management. She is interested in the identifica-
tion of valid statistical techniques and their
limitations when used in software engineering.
Peter W. Jones is currently a professor of
statistics in the Mathematics Department at
Keele University, UK. Previously, he was a
senior lecturer and reader in mathematical
statistics at Keele and a lecturer in statistics at
the University of Wales, Aberystwyth where he
gained his PhD in 1974. He is also a nonexe-
cutive director on the board of the Orthopaedic
Hospital in Oswestry, UK. Peter is an associate
editor of the Journal Biometrics, a member of the
international advisory board of the Egyptian Journal of Mathematics and
Statistics, and an editor of the Journal of Apicultural Research. His
research interests cover a wide range from theoretical developments in
Bayesian sequential estimation and optimisation, especially the study of
bandit processes, to applications in medicine. In recent years, his work
has concentrated on modeling genetic effects on susceptibility and
severity of disease, meta analysis, the planning of clinical trials, and the
development of clinical scoring models for disease progression. He is
the author or coauthor of more than 200 papers.
David C. Hoaglin received the PhD degree in
statistics from Princeton University in 1971. He
is a principal scientist at Abt Associates Inc., an
applied social research firm in Cambridge,
Massachusetts. He has long been interested in
statistical computing and in diverse aspects of
software. His other research intetests include
exploratory data analysis, outliers, nonresponse
in surveys, and applications of statistics to policy
problems. In recent years, he has been involved
in conducting the US National Immunization Survey. Earlier, he held
faculty and research positions in the Department of Statistics at Harvard
University. He is the coeditor and coauthor (with Frederick Mosteller and
John Tukey) of the books Understanding Robust and Exploratory Data
Analysis; Exploring Data Tables, Trends, and Shapes; and Funda-
mentals of Exploratory Analysis of Variance. He is a fellow of the
American Statistical Association, a fellow of the American Association
for the Advancement of Science, and an ordinary member of the
International Statistical Institute.
Khaled El Emam obtained the PhD degree from
the Department of Electrical and Electronics
Engineering, King's College, the University of
London (UK) in 1994. He is currently a research
officer at the National Research Council in
Ottawa, Canada's primary applied research
organization. He is coeditor of ISO's project to
develop an international standard defining the
software measurement process (ISO/IEC
15939) and is leading the software engineering
process area in the IEEE's project to define the Software Engineering
Body of Knowledge. He has also coedited two books on software
process, both published by the IEEE CS Press; he is an adjunct
professor at both the School of Computer Science at McGill University
and the Department of Computer Science at the University of Quebec at
Montreal; and is president of a software company specializing in online
analytics. Currently, he is a resident affiliate at the Software Engineering
Institute in Pittsburgh. Khaled is on the editorial boards of IEEE
Transactions on Software Engineering and the Empirical Software
Engineering Journal. Previously, he was the international trials
coordinator for the SPICE Trials, where he was leading the empirical
evaluation of the emerging process assessment International Standard,
ISO/IEC 15504, world-wide; the head of the Quantitative Methods Group
at the Fraunhofer Institute for Experimental Software Engineering in
Germany; a research scientist at the Centre de recherche informatique
de Montreal (CRIM) in Canada; a researcher in the software engineering
laboratory at McGill University; and worked in a number of research and
development projects for organizations, such as Toshiba International
Company and Honeywell Control Systems in the UK, and Yokogawa
Electric in Japan. He is a member of the IEEE Computer Society.
Jarrett Rosenberg received his doctorate from the University of
California at Berkeley and worked at Xerox and Hewlett-Packard
Laboratories before joining Sun in 1990. He is a statistician and quality
engineer at Sun Microsystems. He is a member of the ACM, the
American Statistical Association, and the American Society for Quality,
and is an ASQ Certified Quality Engineer, Reliability Engineer, and
Software Quality Engineer. He also is a member of the IEEE Computer
Society.
. For more information on this or any computing topic, please visit
our Digital Library at http://computer.org/publications/dilb.
734
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING,
VOL. 28,
NO. 8,
AUGUST 2002
Authorized licensed use limited to: Universidad Federal de Pernambuco. Downloaded on August 6, 2009 at 11:12 from IEEE Xplore.  Restrictions apply. 


