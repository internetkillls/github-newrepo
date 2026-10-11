# Four Dark Corners of Requirements Engineering

Source ID: A05
Authors: Pamela Zave; Michael Jackson
Original attachment: Four Dark Corners of Requirements.pdf
Identity: ACM TOSEM 6(1), 1997, pp. 1–30.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 17

ment-controlled actions (the upper-right corner of Table I) are also impor-
tant because many of the true requirements reside there and are enforced
only indirectly by machine actions. Indicative properties (the left half of
Table I) are often the intermediaries through which machine actions
enforce optative constraints in the environment. These topics are explored
further in Section 5.
4.2 Examples of Control Issues
A Z specification [Spivey 1992] is organized in terms of operations that
affect the specification state. There is no formal notion of control. Some Z
specifications include operations controlled by diverse agents, for example,
Spivey’s real-time kernel [Spivey 1990]. Since there is no way to say which
agent controls which operation, from a formal perspective such specifica-
tions are as bizarre as Lamport’s example of a queue that spontaneously
initiates its own put and get actions [Lamport 1989].
More commonly, users of Z assume that the specification state is the
machine state and that the operations are the interface between the
machine and its environment. Operations are always initiated by the
environment and have “input” and “output” variables for conveying infor-
mation across the machine/environment interface.
The computed precondition of a Z operation gives the circumstances
under which it can be invoked safely (the operation can be carried out, and
all state invariants can be preserved).6 The trouble with the common usage
of Z outlined above is that there is no mechanism for recording constraints
on what the environment can and cannot do. In particular, there is no way
of answering the all-important question: “What properties of the environ-
ment justify ignoring the possibility that an operation is initiated when its
precondition is not satisfied?”
The Software Cost Reduction (SCR) method [Heitmeyer et al. 1995a;
1995b] emphasizes constraints on the machine and has limited capabilities
for constraining the environment.7 These limitations can cause gaps or
anomalies.
The problem is illustrated by an SCR specification of a real-time railroad
crossing system [Atlee and Gannon 1993]. The environment is described in
terms of boolean variables such as Train (which is true when a train is
close to the crossing) and TrainXing (which is true when the train is
actually going through the crossing). Within some versions of the SCR
method it is possible to say that these two variables cannot be true at the
same time, but in no version is it possible to say that when Train becomes
true, it stays true for at least 300 seconds.
6 Again, this is only the most common interpretation, and others are possible [Jackson 1996].
7 The recent version of the A-7 method [Parnas and Madey 1995; van Schouwen et al. 1992]
and the SCR method have common roots in the early version of the A-7 method [Heninger
1980; Parnas and Clements 1986], but the two have now diverged and are quite different with
respect to the issues discussed in this article.
Four Dark Corners of Requirements Engineering
•
17
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 18

As a result of this deficiency, Atlee and Gannon specify this crucial
information as a constraint on the machine. The specified machine is in
mode BC when Train is true and in mode Crossing when TrainXing is true.
The machine specification states that a mode transition from BC to
Crossing occurs if and only if TrainXing becomes true and if the machine
has been in mode BC for at least 300 seconds.
This is a dangerous specification if taken literally. The BC and Crossing
modes provide the gate control algorithm with its information on the
location of the train. If a train is faster than expected, then these modes
will become decoupled from the train location they are supposed to reflect.
In CSP [Hoare 1985], the concept of “shared actions” conflates two
concepts that we have kept separate: control and joint observability.
Section 5 will show that these two concepts play different roles in refine-
ment of requirements, so that there is practical value in distinguishing
them.
Suppose that an environment and a machine are represented formally as
two concurrent processes in CSP. Consider the problem of recovering from
this representation which action types fall into which of the three catego-
ries. It is easy enough to recover which actions are jointly observable by the
two processes (“shared” in our sense) and which are private to the environ-
ment process, because that is a syntactic property.
Recovering the control information is harder. For each jointly observable
action type and each process, there are exactly two possibilities: the process
sometimes refuses to participate in actions of that type, or the process
never refuses to participate in actions of that type. If one process some-
times refuses an action type, and the other process never refuses it, then
actions of that type are controlled by the sometimes-refusing process. If
both processes sometimes refuse an action type, then actions of that type
are jointly controlled, which we believe is a misrepresentation in essen-
tially all real situations. If both processes never refuse an action type, then
it is impossible to tell which process controls it. (Pay actions in the
turnstile system are like this—they are controlled by the environment, but
in the environment as described they can occur at any time.)
Thus CSP is almost expressive enough in terms of control of actions, but
it might be confusing. When CSP is used for requirements, engineers would
do well to augment it with a more explicit statement of their intentions.
Naturally, there are many good examples as well as bad ones. Lamport’s
method [Lamport 1989] has precise identification and flexible treatment of
all shared actions, but no unshared actions. The recent A-7 method uses a
state-oriented formalism; it has precise identification and flexible treat-
ment of all shared state components, but no unshared state components.
Agent formalisms [Dardenne et al. 1993; Dubois et al. 1993; Feather 1987;
Feather et al. 1991; Jeremaes et al. 1986; Johnson 1988] have all the
recommended expressive capabilities. Each agent has specific actions that
it can perform. Typically some agents represent the environment while
some represent the machine, and environment agents are not limited to
those that interact directly with the machine. If the agent formalism is also
18
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 19

a deontic logic [Jeremaes et al. 1986], then permissions and obligations are
like safety and liveness in our example—it must be possible to assert them
in both the indicative and optative moods.
5. THE ROLE OF DOMAIN KNOWLEDGE
A requirement is an optative property. Let R be the set of requirements for
a software development project, i.e., the set of optative properties whose
satisfaction will fully satisfy the customer.
A specification is also an optative property, but one that must be
implementable.8 Let S be the set of specifications for a software develop-
ment project. S can be given to a software development team, which can
implement it successfully without recourse to any additional information. S
must be such that an implementation of it, connected to the environment,
ensures that all the properties of R are satisfied.
The gap between requirements and specifications has long been recog-
nized. The process of bridging this gap is often referred to as refinement of
requirements, by analogy with specification or program refinement. Speci-
fication refinement is concerned with (1) removing the features of a
specification that are not executable by the target implementation platform
and (2) replacing them with features that are executable on that platform.
Requirements refinement is concerned with (1) identifying the aspects of a
requirement that cannot be guaranteed or effected by a computer alone and
(2) augmenting or replacing them until they are fully implementable.
It has also long been recognized that domain knowledge (or domain
modeling, assumptions about the environment, etc.) should play an impor-
tant role in requirements engineering, but there is uncertainty about what
it is for. Because there is uncertainty about what it is for, there is also
uncertainty about how much of it to gather [Iscoe et al. 1991].
The primary role of domain knowledge is to bridge the gap between
requirements and specifications. Requirements that are not specifications
are always converted into specifications with the help of domain knowl-
edge. Let K be the relevant domain knowledge, i.e., the set of relevant
indicative properties. Then S and K together must be sufficient to guaran-
tee that the requirements are satisfied:
S, K £ R
It is important to note that a precise characterization of the difference
between specifications and requirements depends on precise location of the
interface between the machine and environment, i.e., on knowing what the
shared actions are. Many papers in requirements engineering are con-
cerned with the flexibility of the machine/environment boundary [Dar-
denne et al. 1993; Dobson et al. 1994; Feather 1987; 1994; Feather et al.
8 We are discussing implementability in principle. A specification that is implementable in
principle may not be implementable in practice—for instance, because all of the available
computers are too slow.
Four Dark Corners of Requirements Engineering
•
19
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 20

1991; Mostow 1983; Swartout and Balzer 1982]. Thus we are characterizing
the possible results of their explorations, not the explorations themselves.
Some requirements are already implementable, so they can be copied
directly from R to S. Requirements that are not implementable fail to be so
for three general reasons. We shall discuss these reasons in the next three
subsections, followed by a subsection of comparisons to related ideas.
5.1 Environment Constraint
Some requirements are not directly implementable because the only way to
satisfy them is to constrain an action that is controlled by the environment.
As an example of a requirement with an environment constraint, there is a
requirement on the gate complex that (G5) enters do not outnumber pays.
The Buchi automaton in Figure 1 makes it clear that this is a constraint on
enter actions, which are controlled by the environment.
To satisfy this requirement, we need several pieces of domain knowledge.
It is important that (G1) pushes and enters alternate, so that enters can be
prevented by preventing pushes. It is important that (G4) whenever the
turnstile is locked, pushes cannot occur. The effects of lock and unlock
actions are also important, because they are used to put the turnstile into a
locked state. Finally, we also need domain knowledge giving us a lower
bound on the elapsed time between two consecutive pushes (because if
pushes can follow each other arbitrarily closely, then the machine must be
infinitely fast).
The resultant specification [Jackson and Zave 1995] consists of proper-
ties constraining when lock and unlock actions must and must not occur
(these properties are summarized as G6 and G7 in Table I). These appro-
priate actions keep the turnstile locked at the right times, because of the
indicative properties, to satisfy G5.
The lift requirement L2 must be refined to several other requirements,
including (L8) group waiting at a floor leads to an arrive[floor] action. L8 is
not a specification because arrive actions are environment-controlled. Sat-
isfaction of this requirement relies (1) on the domain knowledge that
certain motor states will cause the lift to move and (2) on specification of
machine actions that control the motor state appropriately.
To summarize, requirements that constrain the environment cannot be
satisfied by a machine acting alone. Such requirements are always satisfied
by coordinating specifications with domain knowledge. A requirement with
an environment constraint should always be verified by a demonstration or
proof that specified properties, conjoined with domain knowledge, guaran-
tee the satisfaction of the requirement.
In this context, Buchi automata are an easy notation to understand
because they make it clear which actions are constrained. Thus it is always
possible to determine syntactically whether a requirement is a specification
or not and to refine it (if the environment allows) to a property that is
obviously a specification. For example, in Figure 3 the requirement R
constrains both ec (an environment-controlled action type) and mc (a
20
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 21

machine-controlled action type). Provided that the domain knowledge K
holds, then R can be satisfied by the specification S, which clearly con-
strains only the machine.
Unfortunately, in other formalisms it may not be so clear what is being
constrained by a requirement. In these situations it may be more difficult
to determine when the requirements phase is over or to be sure that the
specification alone contains everything that the implementors need.
5.2 Unshared Information
Some requirements are not directly implementable because they are stated
in terms of unshared phenomena. In the banking environment (Section
3.2), for example, there is a requirement (a withdrawal request leads to a
withdrawal payout, provided that the requested amount does not exceed
the current balance) stated in terms of the account balance. The only
shared phenomena in this example are the action types deposit, withdrawal-
request, and withdrawal-payout. Since the balance state component (a legal
debt) exists in the environment and is not shared with the machine, the
machine cannot directly implement this requirement.
Requirements with unshared information are refined using domain
knowledge relating unshared information to shared information. For exam-
ple, the banking requirement can be refined using the indicative property
also given in Section 3.2, which states an equivalence between the balance
and an expression on deposit and withdrawal-payout actions. The following
is a version of the requirement with the balance replaced by its equivalent
action expression. It is implementable (it uses nothing but shared phenom-
ena) and is therefore a specification.
(
a, m, p u withdrawal-request(a, m) ` ends(a, p) ` m #
((1m u (
a u ; deposit(a, m) ` earlier(a, p)) ; m) 2
(1m u (
a u ; withdrawal-payout(a, m) ` earlier(a, p)) ; m));
(
a9 u ; withdrawal-payout(a9, m) ` earlier(a, a9)))
Fig. 3.
An easy example of refinement.
Four Dark Corners of Requirements Engineering
•
21
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 22

In the presence of the indicative equivalence between the balance and the
action expression, it can be proved that the above property satisfies the
original requirement.
Another way to achieve the same effect would be to define a new term
expected-balance as the sum of the amounts of all previous deposits, minus
the sum of the amounts of all previous withdrawal payouts. If a require-
ment referring to balance is rewritten as referring to expected-balance, then
the rewritten form is a specification. In the presence of the definition of
expected-balance, it is directly implementable. In the presence of informa-
tion about balance, it provably satisfies the original requirement.
As another example of unshared information, the requirement (L8) that
the lift must arrive at a floor where people are waiting for it is not
implementable. How can the machine know that people are waiting?
Request and arrive actions are shared with the machine. There is already
domain knowledge that (L3) the beginning of group waiting leads to a
request action. Other indicative statements must say that people continue
to wait until the lift arrives at their floor going in their direction, at which
point they enter the lift and end group waiting. From these assumptions
about human behavior, and the occurrences of requests and arrivals, the
lift controller can compute where people are presumed to be waiting for the
lift.
In the warehouse example (Section 3.3), if requirements are stated in
terms of quantity-in-bin, designated as the quantity actually present in the
warehouse bin, then refinement is not possible. We know that expected-
quantity-in-bin is not the same as quantity-in-bin, and there are no shared
phenomena from which the machine can compute the actual quantity-in-
bin.
This problem must be solved by changing and elaborating the require-
ments. Probably the requirements will be stated in terms of expected-
quantity-in-bin, which is a defined term representing the best implement-
able estimate of quantity-in-bin. There will probably be extra requirements
for shipping failure (when a bin has unexpectedly run dry) and for periodic
stock inventories to reduce the difference between quantity-in-bin and
expected-quantity-in-bin. expected-quantity-in-bin will be defined in terms
of shared, designated actions including ship, receive, and inventory adjust-
ments.
Turski [1988] has pointed out that real time often appears in specifica-
tions because of unshared information. If the beginning of a physical
process is a shared action, and the ending of the process is not, then the
machine can estimate the ending time from a description of the physical
process including elapsed time.
5.3 Future Reference
Some requirements are not directly implementable because they are stated
in terms of the future. For example, consider the liveness requirement in a
switching environment that, whenever the telephone user has dialed the
22
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 23

last digit, eventually a connect-to-ringback or connect-to-busytone or con-
nect-to-errortone action occurs. In other words, the tone must be produced
when (1) a digit has been dialed and (2) no additional digits will be dialed
in the future.
Like requirements with unshared information, requirements with future
reference are satisfied with the help of domain knowledge, in this case
relating the future to the past. The switching requirement can be satisfied
using an approximate kind of domain knowledge: if the user is going to dial
another digit, he or she will almost always do so within four seconds of the
last digit.
The resulting specification says that the system must respond after a
dialed digit followed by a four-second silence. The silence enables the
machine to distinguish the final digit from nonfinal ones and thus satisfy
the original requirement.
5.4 Other Views of Requirements Refinement
Some of these ideas have appeared in the literature before, in a variety of
forms. Johnson’s refinements called “defining capabilities” and “removing
the perfect knowledge assumption” [Johnson 1988] are addressing essen-
tially the same gaps as environment constraint and unshared information,
respectively, but they are described in very different terms and without the
special emphasis on domain knowledge. Mostow’s “operationalization”
goals IsAchievable and IsEvaluable are also similar in purpose [Mostow
1983]. But Mostow’s work focuses on automated problem solving and thus
assumes—if applied to requirements engineering—that the environment is
as malleable as the machine.
A recent trend in the study of requirements refinement is emphasis on
various agents within the environment [Dardenne et al. 1993; Feather et
al. 1991]. It is recognized that these agents often cooperate with the
machine and with each other to satisfy unrefined requirements.
Agent-centered refinement is a special case of refinement as we have
characterized it. A description of an agent in the environment is indeed
domain knowledge, but not all domain knowledge takes the form of agent
descriptions. Some domain knowledge simply captures static relationships
in the environment.
For example, “indirect access” is a requirements refinement in which the
machine needs some information it does not have direct access to; an agent
in the environment gets it and communicates it to the machine [Feather et
al. 1991]. This is the only strategy mentioned by Feather et al. for dealing
with unshared information, but there are others. In the lift example, the
machine needs to know where people are waiting. It does not obtain this
information through the intercession of another agent. Rather, it computes
it from a known, fixed relationship between past shared actions (requests
and floor arrivals) and the behavior of groups of people waiting for the lift
to arrive.
“Soft” requirements as discussed by Yu et al. [1995] are “soft” for two
reasons. They may be vague and imprecise, such as requirements that a
Four Dark Corners of Requirements Engineering
•
23
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 24

system be “secure,” “reliable,” or “easy to use.” Until they are precise
enough to be formalized, our description of refinement is not relevant to
them. Requirements are also characterized as “soft” if the domain knowl-
edge that supports their satisfaction is not absolutely reliable. For exam-
ple, the lift requirement that a waiting group is eventually served (L2) is
satisfiable partly because (L3) someone in the waiting group pushes the
request button. But L3 is a highly probable assumption rather than an
unalterable fact. In those rare cases where the assumption is not true, the
requirement will not be satisfied, even if the lift controller is perfect.
In contrast to the requirements refinements discussed above, in which
domain knowledge is invoked to bridge the gap from a requirement to a
specification, some requirements transformations are equivalence preserv-
ing. They restructure the available information, often for the purpose of
deriving an acceptable specification, without adding to it. Since the notion
of an “acceptable” specification depends on the expressive power of the
chosen specification language, categorization of these transformations as
requirements refinements or specification refinements is somewhat subjec-
tive. For example, unfolding of invariants and finite differencing have been
used as requirements refinements by Feather [1994], but they are also used
as specification refinements by several authors cited by Feather.
6. FOUR CORNERS MARK A FOUNDATION
So far this article has focused on four miscellaneous problems of require-
ments engineering and has suggested improved ways of understanding or
managing them. But the problems are related. Their solutions fit together
to define and regulate some of the primary concepts of requirements
engineering. The results are summarized in this section.
6.1 Terminology and Applicability
Here are brief definitions of the major terms we have used:
—The environment is the portion of the real world relevant to the software
development project.
—The machine is a computer-based machine that will be constructed and
connected to the environment, as a result of the software development
project.
—A designation is an informal description of the meaning of an atomic
formal term referring to the environment.
—A definition is a formal description of an atomic term, using other defined
or designated terms.
—A statement (assertion, property) in the indicative mood describes the
environment as it would be without or in spite of the machine.
—A statement (assertion, property) in the optative mood describes the
environment as we would like it to be because of the machine.
—A shared action is an action in the environment in which the machine
also participates.
24
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


