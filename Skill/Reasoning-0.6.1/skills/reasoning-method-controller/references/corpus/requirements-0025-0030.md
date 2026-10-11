# Four Dark Corners of Requirements Engineering

Source ID: A05
Authors: Pamela Zave; Michael Jackson
Original attachment: Four Dark Corners of Requirements.pdf
Identity: ACM TOSEM 6(1), 1997, pp. 1–30.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 25

—An unshared action is an action in the environment in which the machine
does not participate.
—An environment-controlled action is an action in the environment that is
controlled, performed, or initiated by the environment.
—A machine-controlled action is an action in the environment that is not
controlled, performed, or initiated by the environment. The intention is
that such an action will be controlled by the machine when it is
connected to the environment.
—A requirement is an optative property, intended to express the desires of
the customer concerning the software development project.
—A statement of domain knowledge or domain assumption is an indicative
property intended to be relevant to the software development project.
—A specification is an optative property, intended to be directly implement-
able and to support satisfaction of the requirements.
This terminology applies to all software development projects, although
projects differ in emphasis, and some projects require imaginative applica-
tion of the above definitions. The point is that requirements, specifications,
and domain knowledge always have the same relationship to each other.
For one example, if the proposed machine is automating a currently
existing manual system, then the focus is on the environment as it will be
in the future (when the machine is installed), not as it is now. The
indicative properties are those that will be enforced by the environment,
including new manual operating procedures. The optative properties are
those that will be enforced by the machine; they might be the same as the
properties of the replaced manual system, but some changes are likely.
For another example, if the proposed machine is an augmentation of an
existing (“legacy”) machine, then the environment of this particular devel-
opment project includes the legacy machine. The indicative properties are
the properties that currently hold of the system at large (including both its
manual and automated parts), and the optative properties are the desired
new properties of the environment.
For a final example, if the proposed machine is a new reusable procedure,
then the environment of this particular development project is nothing
more than the procedure interface. The indicative properties are the
guaranteed constraints on the procedure inputs. The only optative property
(a specification as well as a requirement, since it is directly implementable)
is the desired function from inputs to outputs.
6.2 Notation
Formal representations used in requirements engineering should obey
these four rules. If a requirements language is insufficient in this regard,
its users should be able to augment or supplement it as necessary.
(1) Each atomic term must be designated or defined. This means that
everything said is said about the environment, since all atomic terms
are grounded in the environment.
Four Dark Corners of Requirements Engineering
•
25
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 26

(2) Table II characterizes all relevant actions of the environment. Each
action type must be identified as belonging to exactly one of the
categories in Table II.
(3) Whenever necessary to express relevant properties of the environment,
actions in all three categories must be constrained.
(4) Each property or assertion must be identified as a requirement, state-
ment of domain knowledge, or specification.
For clarity and brevity, we have phrased all of our arguments in terms of
action-based notations. However, the concepts apply just as well to state-
based notations as to action-based notations. When a state-based notation
is being used, “action” is just another name for a state change [Abadi and
Lamport 1993].
In a state-based notation, the interface between the machine and envi-
ronment is represented as shared state components, i.e., components whose
values are accessible to both machine and environment. A machine-con-
trolled (shared) component is one whose value is changed only by an action
of the machine. An environment-controlled component is one whose value is
changed only by an action of the environment. Environment-controlled
components can be shared or unshared, i.e., inaccessible to the machine.
The simplest state-based formulation of Rules 2 and 3 demands that all
state components be identified as belonging to one of the three categories
and that state components be able to appear equally freely in assertions no
matter which category they belong to.
Unfortunately, some state components may be changed by both the
machine and the environment. When these “mixed” components are
present, it appears necessary to introduce explicit actions, so that the
machine-controlled and environment-controlled state changes to the mixed
components can be distinguished.
For clarity and brevity, we have also used examples in which the formal
descriptions are collections of distinct, isolated properties. However, the
concepts apply just as well to executable notations such as Statecharts
[Harel 1987] and RSML [Leveson et al. 1994].
The reason is that executable notations and property-oriented notations
are not as different, fundamentally, as they might seem. Consider a large
Buchi automaton—one with many states and transitions. It might be used
as an executable specification, just as a Statechart or RSML specification
might be. At the same time, the results of Alpern and Schneider [1987]
show that it is equivalent to a large number of separate safety (“in state S,
actions of type A cannot occur”) and liveness (“in state S, an action of type
A or B must eventually occur”) properties.
Table II.
Environment-Controlled
Machine-Controlled
Shared
X
X
Unshared
X
26
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 27

There is no reason whatsoever why an executable notation cannot obey
the first three rules; it is only necessary to ensure that its states and
actions are environment phenomena and that no category of action is
discriminated against.
There may be a slight problem with distinguishing indicative and opta-
tive properties in executable specifications because, as noted above, many
distinct properties are grouped together in a unified whole. This problem
can be solved by putting indicative and optative properties in separate
modules or by establishing conventions for determining which aspects of a
single module are meant to be indicative and which optative.
6.3 Completion
If the five following criteria are satisfied, then requirements engineering,
in the strongest sense, is complete. We are guaranteed that the specifica-
tion is implementable (at least in principle) without recourse to any
additional information. We are also guaranteed that if the specification is
implemented as a machine which is subsequently connected to the environ-
ment, then the requirements will be satisfied.
(1) There is a set R of requirements. Each member of R has been validated
(checked informally) as acceptable to the customer, and R as a whole
has been validated as expressing all the customer’s desires with respect
to the software development project.
(2) There is a set K of statements of domain knowledge. Each member of K
has been validated (checked informally) as true of the environment.
(3) There is a set S of specifications. The members of S do not constrain the
environment; they are not stated in terms of any unshared actions or
state components; and they do not refer to the future.
(4) A proof shows that
S, K £ R.
This proof ensures that an implementation of S will satisfy the require-
ments.
(5) There is a proof that S and K are consistent. This ensures that the
specification is internally consistent and consistent with the environ-
ment. Note that the two proofs together imply that S, K, and R are
consistent with each other.
The most commonly understood use of verification is to show that an
implementation satisfies a specification. The completion rules show that
verification also has a role to play in requirements engineering. First,
verification is necessary to establish the satisfaction result.
Second, some consistency checking is supported by verification. This
occurs when there is some redundancy among the various parts to be
shown consistent—a natural-enough occurrence in large specifications,
with reuse, multiple views, etc. In the presence of redundancy, the state-
Four Dark Corners of Requirements Engineering
•
27
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 28

ments made during the course of requirements engineering are not all
independent, and some are implied by others. A proof that some statements
imply others necessarily establishes the consistency of the consequences
with the antecedents.
ACKNOWLEDGMENTS
We are grateful for the helpful comments of Joanne Atlee, Martin Feather,
the referees, and the editors.
REFERENCES
ABADI, M. AND LAMPORT, L.
1993.
Composing specifications. ACM Trans. Program. Lang.
Syst. 15, 1 (Jan.), 73–132.
ALPERN, B. AND SCHNEIDER, F. B.
1987.
Recognizing safety and liveness. Distrib. Comput. 2,
117–126.
ATLEE, J. M. AND GANNON, J.
1993.
Analyzing timing requirements. In Proceedings of the
1993 International Symposium on Software Testing and Analysis. Softw. Eng. Notes 18, 3
(July), 117–127.
BALZER, R.
AND GOLDMAN, N.
1979.
Principles of good software specification and their
implications for specification language. In Proceedings of the Specifications of Reliable
Software Conference. IEEE Computer Society, Washington, D.C., 58–67.
BRACHMAN, R. J., FIKES, R. E., AND LEVESQUE, H. J.
1983.
Krypton: A functional approach to
knowledge representation. IEEE Comput. 16, 10 (Oct.), 67–73.
BUBENKO, J. A., JR., Ed.
1983.
On concepts and strategies for requirements and information
analysis. In Information Modeling. Chartwell-Bratt, Bromley, England, 125–169.
CURTIS, B., KRASNER, H., AND ISCOE, N.
1988.
A field study of the software design process for
large systems. Commun. ACM 31, 11 (Nov.), 1268–1287.
DARDENNE, A.,
VAN LAMSWEERDE, A.,
AND FICKAS, S.
1993.
Goal-directed requirements
acquisition. Sci. Comput. Program. 20, 3–50.
DOBSON, J. E., BLYTH, A. J. C., CHUDGE, J., AND STRENS, R.
1994.
The ORDIT approach to
organisational requirements. In Requirements Engineering: Social and Technical Issues, M.
Jirotka and J. A. Goguen, Eds. Academic Press, New York, 87–106.
DUBOIS, E., DU BOIS, PH.,
AND PETIT, M.
1993.
O-O requirements analysis: An agent
perspective. In Proceedings of the 7th European Conference on Object-Oriented Programming
(ECOOP 93). Lecture Notes in Computer Science, vol. 707. Springer-Verlag, 458–481.
FEATHER, M. S.
1987.
Language support for the specification and development of composite
systems. ACM Trans. Program. Lang. Syst. 9, 2 (Apr.), 198–234.
FEATHER, M. S.
1994.
Towards a derivational style of distributed system design—An
example. Automated Softw. Eng. 1, 1 (Mar.), 31–59.
FEATHER, M. S., FICKAS, S., AND HELM, B. R.
1991.
Composite system design: The good news
and the bad news. In Proceedings of the 6th Annual Knowledge-Based Software Engineering
Conference. IEEE Computer Society, Washington, D.C., 16–25.
GRIES, D. AND SCHNEIDER, F. B.
1993.
A Logical Approach to Discrete Math. Springer-
Verlag, Berlin.
HAREL, D.
1987.
Statecharts: A visual formalism for complex systems. Sci. Comput. Pro-
gram. 8, 231–274.
HEITMEYER, C., BULL, A., GASARCH, C., AND LABAW, B.
1995a.
SCR*: A toolset for specifying
and analyzing requirements. In Proceedings of the 10th Annual Conference on Computer
Assurance (COMPASS ’95). IEEE, New York, 109–122.
HEITMEYER, C., LABAW, B., AND KISKIS, D.
1995b.
Consistency checking of SCR-style require-
ments specifications. In Proceedings of the 2nd IEEE International Symposium on Require-
ments Engineering. IEEE Computer Society, Washington, D.C., 56–63.
HENINGER, K. L.
1980.
Specifying software requirements for complex systems: New tech-
niques and their application. IEEE Trans. Softw. Eng. 6, 1 (Jan.), 2–13.
28
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 29

HOARE, C. A. R.
1985.
Communicating Sequential Processes. Prentice-Hall International,
Chichester, U.K.
ISCOE, N., WILLIAMS, G. B., AND ARANGO, G.
1991.
Domain modeling for software engineer-
ing. In Proceedings of the 13th International Conference on Software Engineering. IEEE
Computer Society, Washington, D.C., 340–343.
JACKSON, D.
1995a.
Structuring Z specifications with views. ACM Trans. Softw. Eng.
Methodol. 4, 4 (Oct.), 365–389.
JACKSON, M.
1978.
Information systems: Modelling, sequencing, and transformations. In
Proceedings of the 3rd International Conference on Software Engineering. IEEE Computer
Society Press, Los Alamitos, Calif., 73–81.
JACKSON, M.
1983.
System Development. Prentice-Hall International, Chichester, U.K.
JACKSON, M.
1995b.
Software Requirements and Specifications: A Lexicon of Practice, Prin-
ciples, and Prejudices. Addison-Wesley, Reading, Mass.
JACKSON, M. AND ZAVE, P.
1995.
Deriving specifications from requirements: An example. In
Proceedings of the 17th International Conference on Software Engineering. ACM, New York,
15–24.
JARKE, M., BUBENKO, J., ROLLAND, C., SUTCLIFFE, A.,
AND VASSILIOU, Y.
1992.
Theories
underlying requirements engineering: An overview of NATURE at genesis. In Proceedings of
the IEEE International Symposium on Requirements Engineering. IEEE Computer Society,
Washington, D.C., 19–31.
JEREMAES, P., KHOSLA, S., AND MAIBAUM, T. S. E.
1986.
A modal (action) logic for require-
ments specification. In Software Engineering 86, D. Barnes and P. Brown, Eds. Peter
Peregrinus, 278–294.
JOHNSON, W. L.
1988.
Deriving specifications from requirements. In Proceedings of the 10th
International Conference on Software Engineering. IEEE Computer Society, Washington,
D.C., 428–438.
JONES, C. B.
1990.
Systematic Software Development Using VDM. 2nd ed. Prentice-Hall
International, Chichester, U.K.
KHOSHAFIAN, S. N.
AND COPELAND, G. P.
1990.
Object identity. In Readings in Object-
Oriented Database Systems, Stanley B. Zdonik and David Maier, Eds. Morgan Kaufmann,
San Mateo, Calif., 37–46.
LAMPORT, L.
1989.
A simple approach to specifying concurrent systems. Commun. ACM 32,
1 (Jan.), 32–45.
LEHMAN, M. M.
1980.
Programs, life cycles, and laws of software evolution. Proc. IEEE 68, 9
(Sept.), 1060–1076.
LEVESON, N. G., HEIMDAHL, M. P. E., HILDRETH, H., AND REESE, J. D.
1994.
Requirements
specification for process-control systems. IEEE Trans. Softw. Eng. 20, 9 (Sept.), 684–707.
LISKOV, B. H. AND ZILLES, S. N.
1975.
Specification techniques for data abstractions. IEEE
Trans. Softw. Eng. 1, 1 (Mar.), 7–19.
MOSTOW, J.
1983.
A problem-solver for making advice operational. In Proceedings of the
National Conference on Artificial Intelligence (AAAI-83). AAAI, Menlo Park, Calif., 279–283.
PARNAS, D. L. AND CLEMENTS, P. C.
1986.
A rational design process: How and why to fake it.
IEEE Trans. Softw. Eng. 12, 2 (Feb.), 251–257.
PARNAS, D. L. AND MADEY, J.
1995.
Functional documentation for computer systems engi-
neering. Sci. Comput. Program. 25, 41–61.
SPIVEY, J. M.
1990.
Specifying a real-time kernel. IEEE Softw. 7, 5 (Sept.), 21–28.
SPIVEY, J. M.
1992.
The Z Notation: A Reference Manual. 2nd ed. Prentice-Hall, Englewood
Cliffs, N.J.
SWARTOUT, W. AND BALZER, R.
1982.
On the inevitable intertwining of specification and
implementation. Commun. ACM 25, 7 (July), 438–440.
TURSKI, W. M.
1988.
Time considered irrelevant for real-time systems. BIT 28, 473–486.
VAN SCHOUWEN, A. J., PARNAS, D. L., AND MADEY, J.
1992.
Documentation of requirements
for computer systems. In Proceedings of the IEEE International Symposium on Require-
ments Engineering. IEEE Computer Society, Washington, D.C., 198–207.
WING, J. M.
1990.
A specifier’s introduction to formal methods. IEEE Comput. 23, 9 (Sept.),
8–24.
Four Dark Corners of Requirements Engineering
•
29
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 30

WORDSWORTH, J. B.
1992.
Software Development with Z: A Practical Approach to Formal
Methods in Software Engineering. Addison-Wesley, Reading, Mass.
YU, E., DU BOIS, PH., DUBOIS, E., AND MYLOPOULOS, J.
1995.
From organization models to
system requirements: A “cooperating agents” approach. In Proceedings of the 3rd Interna-
tional Conference on Cooperative Information Systems. 194–204.
ZAVE, P.
1982.
An operational approach to requirements specification for embedded sys-
tems. IEEE Trans. Softw. Eng. 8, 3 (May), 250–269.
ZAVE, P.
AND JACKSON, M.
1993.
Conjunction as composition. ACM Trans. Softw. Eng.
Methodol. 2, 4 (Oct.), 379–411.
Received May 1995; revised October 1995 and May 1996; accepted August 1996
30
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


