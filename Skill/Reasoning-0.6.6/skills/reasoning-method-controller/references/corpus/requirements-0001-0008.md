# Four Dark Corners of Requirements Engineering

Source ID: A05
Authors: Pamela Zave; Michael Jackson
Original attachment: Four Dark Corners of Requirements.pdf
Identity: ACM TOSEM 6(1), 1997, pp. 1–30.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 1

Four Dark Corners of Requirements
Engineering
PAMELA ZAVE
AT&T Research
and
MICHAEL JACKSON
AT&T Research and MAJ Consulting Limited
Research in requirements engineering has produced an extensive body of knowledge, but there
are four areas in which the foundation of the discipline seems weak or obscure. This article
shines some light in the “four dark corners,” exposing problems and proposing solutions. We
show that all descriptions involved in requirements engineering should be descriptions of the
environment. We show that certain control information is necessary for sound requirements
engineering, and we explain the close association between domain knowledge and refinement
of requirements. Together these conclusions explain the precise nature of requirements,
specifications, and domain knowledge, as well as the precise nature of the relationships among
them. They establish minimum standards for what information should be represented in a
requirements language. They also make it possible to determine exactly what it means for
requirements engineering to be successfully completed.
Categories and Subject Descriptors: D.2.1 [Software Engineering]: Requirements/Specifica-
tions—methodologies
General Terms: Theory, Verification
Additional Key Words and Phrases: Control of actions, domain knowledge, implementation
bias, refinement of requirements
1. INTRODUCTION
There was a time when the epigram “requirements say what the system
will do and not how it will do it” summarized all of requirements engineer-
ing. That time is long past. Research in requirements engineering has now
produced a body of knowledge including terminology, methods, languages,
tools, and issues acknowledged to be critical.
Authors’ addresses: P. Zave, AT&T Research, 700 Mountain Avenue, Room 2B-413, Murray
Hill, NJ 07974; email: pamela@research.att.com; M. Jackson, AT&T Research and MAJ
Consulting Limited, 101 Hamilton Terrace, London NW8 9QX, United Kingdom; email:
jacksonma@attmail.att.com.
Permission to make digital/hard copy of part or all of this work for personal or classroom use
is granted without fee provided that the copies are not made or distributed for profit or
commercial advantage, the copyright notice, the title of the publication, and its date appear,
and notice is given that copying is by permission of the ACM, Inc. To copy otherwise, to
republish, to post on servers, or to redistribute to lists, requires prior specific permission
and/or a fee.
© 1997 ACM 1049-331X/97/0100–0001 $03.50
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997, Pages 1–30.


## PDF page 2

Despite this progress, we have identified four areas in which the founda-
tion of the discipline seems weak or obscure. This article attempts to shine
some light in these dark corners, exposing the problems and proposing
some solutions. We are led to these conclusions:
(1) All the terminology used in requirements engineering should be
grounded in the reality of the environment for which a machine1 is to be
built.
(2) It is not necessary or desirable to describe (however abstractly) the
machine to be built. Rather, the environment is described in two ways:
as it would be without or in spite of the machine and as we hope it will
become because of the machine.
(3) Assuming that formal descriptions focus on actions, it is essential to
identify which actions are controlled by the environment, which actions
are controlled by the machine, and which actions of the environment
are shared with the machine. All types of actions are relevant to
requirements engineering, and they might need to be described or
constrained formally. If formal descriptions focus on states, then the
same basic principles apply in a slightly different form.
(4) The primary role of domain knowledge in requirements engineering is
in supporting refinement of requirements to implementable specifica-
tions. Correct specifications, in conjunction with appropriate domain
knowledge, imply the satisfaction of the requirements.
The four areas of inquiry have not been chosen randomly. Together they
explain the precise nature of requirements, specifications, and domain
knowledge, as well as the precise nature of the relationships among them.
They establish minimum standards for what information should be repre-
sented in a requirements language. They also make it possible to determine
exactly what it means for requirements engineering to be successfully
completed. The final section of the article summarizes these recommenda-
tions and elaborates how they can be applied to the wide range of systems
and needs served by requirements engineering.
The purposes of this article are not to promote any particular notation,
method, or tool, still less to propose new ones. Its purposes are to clarify the
nature of requirements engineering, to show the importance of certain
information that is often absent or implicit, and to solve some persistent
foundational problems. These results can be used to evaluate and improve
current and future approaches to requirements engineering.
This work is limited to the formal aspects of requirements engineering. It
does not cover the sociological aspects of requirements engineering, such as
how to communicate with customers or resolve their conflicts.
1 Throughout this article we use “system” only to refer to a general artifact that might have
both manual and automatic components, such as an “airline reservation system.” Whenever
we are referring to the computer-based artifact that is the target of software development, we
use the more precise term “machine.”
2
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 3

There are many additional motivations and ramifications not covered in
this article [Jackson 1995b]. Although this article uses many brief and
partial examples, the same ideas have also been used to work through a
complete case study [Jackson and Zave 1995]. In this article the ideas are
more fully related to ongoing research in requirements engineering.
2. GROUNDING FORMAL REPRESENTATIONS IN REALITY
Any formal representation uses primitive terms with no inherent formal
meaning. In requirements engineering, the meaning of these terms lies in
the real world, and the validity of any formal assertion relies on it. Here is
a hypothetical dialogue between two requirements engineers working on an
information system for a university:
Able: Two important basic types are student and course. There is also a
binary relation enrolled. If types and relations are formalized as predicates,
then
; s ; c~enrolled~s, c!fstudent~s! ` course~c!!.
Baker: Do only students enroll in courses? I don’t think that’s true.
Able: But that’s what I mean by student!
If a student is a person who is enrolled in a course at this university, then
Able’s assertion is nearly vacuous. If a student is a person who has
matriculated at the university and not yet graduated or withdrawn, then
Able’s assertion is a strong constraint on who can take courses at the
university.
The only way to establish the meaning of a primitive term is to provide
an informal explanation of it. This explanation must be clear and precise; it
must be written down; and it must be maintained as an essential part of
the requirements documentation. We call such an explanation a “designa-
tion.”2
It is well known that pinning down the real-world meaning of a primitive
term can be extremely difficult—it can be fraught with subtleties and
ambiguities. Everyone with experience in requirements engineering has, in
some situation, used a term freely for a long time before noticing that its
meaning is unclear. Yet very few requirements methods address this
problem by enforcing the presence of a designation for every primitive
term.
A notable exception is the A-7 method. In an early version [Heninger
1980; Parnas and Clements 1986], for every input or output data item a
form must be filled out, and the form requires a “description” entry which is
a designation of the data item. A later version [Parnas and Madey 1995;
van Schouwen et al. 1992] says that “the association between the physical
2In logic, a designation is called an “interpretation.” We avoid the word “interpretation”
because it is highly overloaded in computing. It also carries the unfortunate connotation that
the logic is real and important, while any correspondence it might have to the world is casual
and incidental.
Four Dark Corners of Requirements Engineering
•
3
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 4

quantities of interest and their mathematical representations must be
carefully defined” and claims to have demonstrated that “the use of prose in
specifications—a major source of ambiguity and imprecision—can be lim-
ited to the environmental-quantity descriptions only.”
Another good example is the textual convention for Z recommended by
Wordsworth [1992]. Each schema has text preceding it to explain (desig-
nate) the variables declared in it and text following it to explain (para-
phrase) the assertions made about those variables.
The remainder of this section points out additional benefits of the use of
designations. The examples show how designations provide new perspec-
tives on old problems and answer some not-so-obvious questions.
The Difference between Assertion and Definition.
The difference be-
tween assertion and definition is well known [Brachman et al. 1983].
However, the concept of a designation provides a slightly new perspective
on it.
The assertion
s(student~s!N
c enrolled~s, c!)
presupposes a designation of student (perhaps as a person who has matric-
ulated at the university and not yet graduated or withdrawn) and a
designation of enrolled. The assertion constrains the real world by express-
ing a relationship between two real-world phenomena. It might be true or
false and should be validated before it is used. The definition
student~s!
def%
c enrolled~s, c!
precludes a designation of student. It extends the formal vocabulary with-
out constraining the real world in any way. It might be useless or mislead-
ing, but it cannot be false.
In some logical systems the assertion and the definition would be
considered equivalent, and in most logical systems the same inferences
could be made from both of them. They are different because of designa-
tions; if designations are ignored then there is no real difference between
them.
Goal Regress.
Requirements engineering is about the satisfaction of
goals [Dardenne et al. 1993]. But goals by themselves do not make a good
starting point for requirements engineering. To see why, consider a project
to develop a computer-controlled turnstile guarding the entrance to a zoo
[Jackson and Zave 1995].
If the engineers are told that the goal of the system is to deny entrance to
people who have not paid the admission charge, they may decide that the
goal has been stated too narrowly. Is not the real goal to ensure the
profitability of the zoo? Should they consider other ways of improving
profits, such as cutting costs? What if there is more money to be made by
closing the zoo and selling the land? And what is the goal of profit? If the
4
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 5

goal of profit is the happiness of the zoo owner, would religion or devotion
to family be more effective? Obviously there is something wrong here.
Almost every goal is a subgoal with some higher purpose. Both engineering
and religion are concerned with goal satisfaction; what distinguishes them
is their subject matter.
The engineers should be told, in addition to the goal, that the subject
matter is the zoo entrance. This information should take the form of
designations of phenomena observable at the zoo entrance, such as visitors,
coins, and the action of entering the zoo. These designations circumscribe
the area in which alternative goal satisfaction strategies can be considered,
at the same time that they provide the basis for formal representation of
requirements.
Identity.
The concept of identity is known to be an important aspect of
formal representation schemes [Khoshafian and Copeland 1990]. But for-
mal notions of identity and distinguishability are useless if they do not
correspond reliably to the real world. Designations help pin down their
real-world meanings.
Consider, for example, a specification of a bounded buffer in temporal
logic [Wing 1990]. This particular specification includes the constraint that
for each message m currently placed on the input channel and for each
previously placed message m9, m and m9 are not identical. Wing’s discus-
sion says, “This property is . . . an assumption of the environment. This
assumption is essential to the validity of the specification.”
Since the term message is ambiguous, it is not clear what this assump-
tion means or how to satisfy it. If message refers to the message content,
then the same bit pattern cannot be transmitted twice. This interpretation
seems stronger than intended or necessary, but without a designation there
is no way to rule it out.
A good designation of the term message might include information about
message creation and usage:
A process calls the procedure send-msg for the purpose of transmitting
data to some other process. A message is the result of a particular call to
send-msg and contains the data to be transmitted.
Now it is clear that each call to send-msg creates a distinct message,
regardless of content. Furthermore, if a call to send-msg includes placing
the message on the input channel of the bounded buffer, then the buffer’s
messages m and m9 are guaranteed to be distinct because each is inevi-
tably the result of a distinct call.
3. IMPLEMENTATION BIAS
Requirements are supposed to describe what the desired machine does, not
how it does it. More precisely, requirements are supposed to describe what
is observable at the interface between the environment and the machine,
and nothing else about the machine. To say anything else about the
machine is regarded as implementation bias.
Four Dark Corners of Requirements Engineering
•
5
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 6

State is used frequently in specifications and specification languages.
Very few machines are simple or specialized enough to be specified entirely
without state. This causes a problem: specifying a machine in terms of its
states appears to introduce serious implementation bias, because its states
are internal and not directly observable at the interface between the
machine and its environment.
The next subsection reviews some previously proposed solutions to this
problem. Then we propose a completely different way of looking at require-
ments specification that eliminates the problem altogether. A third subsec-
tion expands on the differences and their consequences.
3.1 Previous Approaches to the Problem
Property-oriented specification techniques [Wing 1990] seek to avoid the
use of explicit internal state by stating the minimal constraints on the
machine state in the form of assertions. Algebraic and axiomatic techniques
are the major techniques in this category. Despite eloquent justifications of
this approach [Liskov and Zilles 1975], many people consider it difficult to
use, and model-oriented techniques are gaining in popularity.
Model-oriented specification techniques represent the system state as
abstractly as possible, using mathematical structures such as sets, rela-
tions, and tuples. Thus model-oriented specifications run a greater risk of
implementation bias. In attempting to escape this dilemma, Jones [1990]
defines implementation bias as follows:
A model-oriented specification is based on an underlying set of states. The
model is biased (with respect to a given set of operations) if there exist
different elements of the set of states which cannot be distinguished by any
sequence of operations.
For example, a telephone switch may allow a subscriber to enter telephone
numbers from which he or she is protected—calls to the subscriber from
those numbers will not go through. If the telephone numbers blocked by a
subscriber appear only in this requirement, then representing them as a
set would be unbiased by Jones’ definition. Representing them as a list
would be biased by the same definition, because a list would contain
ordering information that could not be observed by using any machine
function.
Jones’ recommendation is to use only states that are unbiased by his
definition. But trouble arises because the definition is with respect to a
given set of operations. For real machines, the requirements change and
expand frequently. It is possible that a new function will be required of the
telephone switch, allowing the subscriber to play back his or her blocked
numbers in the order entered. After this change, a set representation will
be inadequate, and a list will be necessary. Thus Jones’ recommendation
brings freedom from implementation bias into conflict with maintainabil-
ity.
Lamport’s solution to the problem of implementation bias focuses on the
exact relationship between the specification and an implementation that
6
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 7

satisfies it [Lamport 1989]. In his method, the machine has an unspecified
state space S. Each state component ci used in the specification is actually
a function ci: S 3 Vi from the state space to a set of values Vi.
The formal meaning of any specification is a temporal-logic formula in
which the state components ci are existentially quantified variables. The
specification is satisfied by any implemented machine with any state space
whatsoever, provided that there exist functions ci on the state space that
satisfy the temporal-logic formula. The specification does not bias the
implementation because a “specification state” (c1(s), c2(s), . . . , cn(s))
can look completely different from an “implementation state” s [ S.
Also note that, since the ci can be many-to-one functions, many imple-
mentation states can map to the same specification state. This accommo-
dates the realistic situation in which a single specification action is
implemented by dozens or even thousands of separate implementation
actions.
3.2 Requirements Exist Only in the Environment
A portion of the real world becomes the “environment” of a development
project because its current behavior is unsatisfactory in some way. The
developers propose to build a computer-based machine and connect it to the
existing environment in such a way that the behavior of the environment
becomes satisfactory. Although we are accustomed to think of machine
inputs and outputs, it is important to realize that those inputs and outputs
are phenomena in the environment. If they were not part of the environ-
ment, then they could not possibly connect the machine to the environment
or affect the behavior of the environment.
From this perspective, all statements made in the course of requirements
engineering are statements about the environment. The primary distinc-
tion necessary for requirements engineering is captured by two grammati-
cal moods. Statements in the “indicative” mood describe the environment
as it is in the absence of the machine or regardless of the actions of the
machine; these statements are often called “assumptions” or “domain
knowledge.” Statements in the “optative” mood describe the environment as
we would like it to be and as we hope it will be when the machine is
connected to the environment. Optative statements are commonly called
“requirements.” The ability to describe the environment in the optative
mood makes it unnecessary to describe the machine.
This perspective avoids the problem of implementation bias because no
statements are made about the proposed machine. The specification state is
not a description of the state of the machine, but rather a description of the
state of the environment. The specification might be compromised by poor
designations or invalid indicative statements, but it cannot overconstrain
the implementation.
Some of our examples are given in Gries and Schneider’s equational logic
[Gries and Schneider 1993]. Time and temporal properties are encoded in
logic as follows [Zave and Jackson 1993].
Four Dark Corners of Requirements Engineering
•
7
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 8

We assume that actions are atomic and sequential. They are represented
by distinct individuals satisfying the predicate action(a). The binary pred-
icate earlier(a1, a2) establishes a nondense total order (with an initial
member) on actions.
Because the action sequence is nondense, we can postulate a unique
pause between each adjacent pair of actions during which the state has
changed in response to the first action, cannot change again until the next
action, and can be observed. These pauses are formalized as individuals
satisfying the predicate pause( p). begins(a, p) means that action a begins
pause p, i.e., precedes it immediately in the temporal sequence. ends(a, p)
means that action a ends pause p, i.e., succeeds it immediately in the
temporal sequence.
Note that a specific earlier predicate, a specific begins predicate, and a
specific ends predicate combine to represent a single behavior or trace. In
other words, each model that satisfies the specification represents one
behavior that satisfies the specification. Because most specifications are
satisfied by many behaviors, they are also satisfied by many different
models.
For a simple example of indicative and optative properties, consider a
single-customer banking environment with designations of three action
types: deposit(a, m) means that a is an action in which amount m is
deposited; withdrawal-request(a, m) means that a is an action in which a
withdrawal of amount m is requested; and withdrawal-payout(a, m) means
that a is an action in which amount m is paid out as a withdrawal.
Deposits and withdrawal requests are performed by the customer, while
withdrawal payouts are performed by the machine (control of actions will
be discussed in detail in the next section).
The current account balance is part of the state of the environment—it is
a legal debt owed by the bank to the customer. Formally, balance(b, p)
means that during pause p the balance is amount b. An indicative property
of this environment is that, at any time, the balance is equal to the sum of
the amounts of all the previous deposits, minus the sum of the amounts of
all the previous withdrawal payouts:
(
b, p u ; balance(b, p) [
(b 5 (1m u (
a u ; deposit(a, m) ` earlier(a, p)) ; m)
2 (1m u (
a u ; withdrawal-payout(a, m) ` earlier(a, p)) ; m)))
This property uses the uniform quantification of equational logic, in which
~piuR~i!;P~i!!
denotes the accumulation of values P(i), using operator p, over all values i
for which predicate R(i) holds. The “accumulation” of
is a conjunction;
the “accumulation” of
is a disjunction; and the “accumulation” of 1 is an
arithmetic sum. We have also extended earlier to cover pauses as well as
actions.
8
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


