# Four Dark Corners of Requirements Engineering

Source ID: A05
Authors: Pamela Zave; Michael Jackson
Original attachment: Four Dark Corners of Requirements.pdf
Identity: ACM TOSEM 6(1), 1997, pp. 1–30.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 9

An important optative property of this environment is that a withdrawal
request leads to a withdrawal payout, provided that the requested amount
does not exceed the current balance:
(
a, m, p, b u withdrawal-request(a, m) ` ends(a, p) ` balance(b, p)
` b $ m:
(
a9 u ; withdrawal-payout(a9, m) ` earlier(a, a9)))
A requirements method should provide for specification of both indicative
and optative properties and should make a clear distinction between them.
For example, the recent version of the A-7 method [Parnas and Madey
1995; van Schouwen et al. 1992] features two relations NAT and REQ. NAT
documents the constraints on the values of environmental quantities
imposed by nature and previously installed systems; it is in the indicative
mood. REQ documents further constraints on the environmental quantities
to be imposed by the machine; it is in the optative mood.
3.3 Consequences
The idea that a requirements specification should include a model of the
environment has been familiar since the early 1980s [Balzer and Goldman
1979; Jackson 1978; 1983; Lehman 1980; Zave 1982]. To the best of our
knowledge, we are the first to propose that requirements should contain
nothing but information about the environment.
The proposed shift in perspective might not seem to make much differ-
ence. For example, we have mentioned two properties of the banking
system: the balance is the sum of the deposits minus the sum of the
withdrawal payouts, and a withdrawal request leads to a withdrawal
payout if the balance is large enough. We have said that the first property
is indicative, that the second is optative, and that the balance is part of the
environment state. But the formal representations of these properties
would fit equally well into a more conventional setting in which the balance
is considered to be machine state and in which both properties describe
requirements on the machine.
One consequence of the difference concerns the popular subject of “do-
main knowledge” [Iscoe et al. 1991; Jarke et al. 1992]. If specification state
is considered to be machine state, then the problem of implementation bias
forces the specification to be minimal—there must be nothing that is not
necessary to carry out the currently proposed machine functions. When
specification state is understood to be environment state, however, then we
are free to collect and record interesting information about the environ-
ment even before we are sure it will be needed. This freedom is clearly
necessary for collecting libraries of reusable information about important
portions of the real world. Given the thin spread of domain knowledge
[Curtis et al. 1988], any true and relevant indicative statement is a
contribution.
Another consequence of the difference concerns designations. Obviously,
an implemented machine often maintains internal state that mimics the
Four Dark Corners of Requirements Engineering
•
9
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 10

current environment state. The imitation is usually imperfect, however,
because there may be delay, errors, and factors in the real world that the
machine does not know about.
For example, an inventory control machine for a warehouse gets reports
of receive and ship actions, each having a bin and quantity attribute. From
these reports the machine maintains an internal model of the contents of
the warehouse. However, due to theft, breakage, mishandling, update
delays, clerical errors, and other misfortunes, it is extremely likely that the
quantity actually present in a warehouse bin at a particular time is not
exactly the same as the quantity indicated by the machine’s model.
Section 5 discusses how errors and unknown factors can be managed
(Bubenko [1983] has treated the subject of update delays). In the mean-
time, we can point out that components of the machine state cannot be
designated. Designations refer to the real world, and the machine state
may have no direct correspondence to the real world.
In practice, effective specification usually requires many auxiliary terms
that would be awkward to designate and that may correspond more closely
to the eventual machine state than designated terms. These can always be
introduced and grounded in reality by defining them using designated
terms. For example, if needed for the requirements of the inventory control
machine, the expected-quantity-in-bin can be defined using the designated
terms receive(a, s, b), meaning that a is an action in which quantity s for
bin b is received by the warehouse, and ship(a, s, b), meaning that a is an
action in which quantity s from bin b is shipped from the warehouse:
expected-quantity-in-bin(q, p, b)def%
(q 5 (1s u (
a u ; receive(a, s, b) ` earlier(a, p)) ; s)
2 (1s u (
a u ; ship(a, s, b) ` earlier(a, p)) ; s))
4. CONTROL OF ACTIONS
In requirements engineering we are always concerned with two actors or
agents: the environment and the machine. In any situation with two or
more agents, it is always of primary importance to understand issues of
control. If a requirements language or method is deficient in representation
of actions or control—as many are—then it is necessary to augment it or
compose it with other formal languages better suited to the job.
The first subsection presents two expressive capabilities that are needed
for requirements engineering and shows how they are used. The second
subsection comments on their presence or absence in several well-known
requirements languages or methods; their absence causes a variety of
difficulties.
4.1 Two Necessary Expressive Capabilities
A sufficiently expressive requirements language must provide for the
declaration of a finite collection of “action types.” These action types
partition all possible actions.
10
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 11

Each action type is either “environment controlled” or “machine con-
trolled,” indicating which agent controls, performs, or takes responsibility
for actions of that type.3 If actions of a type are sometimes environment-
controlled and sometimes machine-controlled, then the type can be divided
into two subtypes.
Each action type is also either “shared” or “unshared.” If it is shared,
then it is part of the real world that is shared between (belonging to,
observable by) both the machine and environment. If it is unshared, then it
is private to the environment and unobservable by the machine.
Obviously an action cannot be both machine-controlled and unshared.
This leaves three possible combined action categories: environment-con-
trolled/unshared, environment-controlled/shared, and machine-controlled/
shared. A requirements language must be able to express which category
each action type belongs to. The importance of this information should be
self-evident. The implemented machine must perform the machine-con-
trolled actions and not the environment-controlled ones. The implemented
machine can observe and make use of its knowledge of the shared actions,
while the unshared actions are beyond its reach.
The second necessary expressive capability is the full ability to state
constraints on actions in all three categories. The requirements engineer
should be able to make assertions about all actions in both the indicative
and optative moods. If a kind of property can be expressed about actions in
one category, then it should be possible to state the same property of
actions in other categories.
To show why the second expressive capability is necessary, we wish to
give examples of almost all the possibilities suggested above. In some
formalisms, however, it can be difficult to separate different kinds of
properties and difficult to determine exactly which actions are constrained
by a property. So, for the purpose of giving illustrative examples, we shall
use a formal language in which both of these are straightforward.
Buchi automata are equivalent in expressive power to linear-time tempo-
ral logic. In linear-time temporal logic any property can be expressed as a
combination of safety and liveness properties [Alpern and Schneider 1987].
Safety properties can be paraphrased as “something bad must not happen,”
and liveness properties can be paraphrased as “something good must
happen.”
Alpern and Schneider show that the structure of a Buchi automaton
reveals whether it expresses a “pure” safety property, a “pure” liveness
property, or a combination of the two. A nontrivial safety property is
specified by an automaton with no nonaccepting states, but with at least
3 The term “machine-controlled” may seem to indicate a departure from the principle that
requirements say nothing about the machine, but the lapse is only terminological. We would
prefer to use “active” (actively controlled by the environment) and “passive” (passively done to
the environment), where a passive action must be machine-controlled because it is not
performed by the environment, and there is no other relevant agent to perform it. The
“active/passive” terminology is properly centered on the environment, but unfortunately the
meaning of these words is much harder to remember.
Four Dark Corners of Requirements Engineering
•
11
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 12

Table I.
Indicative Statement (assumption, domain knowledge)
Optative Statement (requirement)
Liveness Property
Safety Property
Liveness Property
Constrained action
is environment-
controlled,
unshared
(unobservable by
machine)
(G2) A push leads to
an enter.
(G1) Pushes and enters alternate.
(L1) Begin-group-waiting[floor,
direction] alternates with end-
group-waiting[floor, direction].
(G5) Enters do not
outnumber pays.
(L2) A begin-group-
waiting[floor, direction]
action leads to an end-
group-waiting[floor,
direction] action.
Constrained action
is environment-
controlled, shared
(jointly
observable)
(L3) A begin-group-
waiting[floor,
direction] action
leads to a
request[floor,
direction] action.
(G1) Pushes and enters alternate.
(G4) When the turnstile is
locked, pushes do not occur.
(L7) Foolish
arrive[floor]
actions do not
occur.
(L8) Group waiting at a
floor leads to an
arrive[floor] action.
Constrained action
is machine-
controlled, shared
(jointly
observable)
(L5) Motor-ups and motor-downs
alternate.
(G3) Locks and
unlocks
alternate.
(L4) When the
motor is on,
motor-ups and
motor-downs do
not occur.
(G7) Locks and
unlocks do not
occur when
inappropriate.
(L6) A request[floor,
direction] action leads to
a request-light-on[floor,
direction] action.
(G6) Locks and unlocks
occur when appropriate.
12
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 13

one state having no out-transition on at least one action type in its
vocabulary. It asserts that in a state with missing out-transitions, actions
of the missing types do not occur. In other words, it constrains certain
action types by prohibiting their occurrence in certain states. A nontrivial
liveness property is specified by an automaton with no missing out-
transitions, but with at least one nonaccepting state. It asserts that,
whenever a nonaccepting state is reached, actions must eventually occur to
cause a transition to an accepting state. In other words, it constrains
certain action types by requiring them to occur in certain states.
We shall now discuss two software development projects and many of
their relevant properties. Most of these properties are formalized as Buchi
automata, which shows whether they are safety or liveness properties and
which action types they constrain. The properties are paraphrased briefly
and classified in Table I.
First consider a real-world environment consisting of a gate, a physical
turnstile guarding the gate, a coin slot, and the customers who wish to
enter the gate. The desired machine is a computer-based controller for the
gate complex.
There are five important action types in the gate complex. A pay action
occurs whenever a customer puts enough money in the coin slot to be
allowed to enter the gate. A push action occurs whenever a customer
pushes the turnstile and thereby starts it moving. An enter action occurs
whenever a customer pushes the turnstile through to its home position,
thus entering the gate. These three action types are environment-con-
trolled; pays and pushes are shared with the machine, while enters are not.
In addition, there are machine-controlled lock and unlock actions. Five
properties of interest are specified formally in Figure 1.
G1 is an indicative safety property, expressed in terms of the action types
push and enter. It says that the turnstile is constructed so that pushes and
enters alternate strictly, beginning with a push. Since both enters and
pushes are constrained, G1 appears in two different places in Table I, one
reflecting the fact that it constrains enters (environment-controlled, un-
shared actions) and one reflecting the fact that it constrains pushes
(environment-controlled, shared actions).
To eliminate the possibility that a customer pushes the turnstile and
then stops without entering the gate, the turnstile is also constructed with
a hydraulic mechanism so that a push always leads to an enter. This
indicative property (G2) is a liveness constraint on enter actions.4
The manufacturers of the turnstile hardware have designed it under the
assumption that the controller will perform lock and unlock actions in a
strictly alternating sequence. Because of this fault-intolerant design, an
improperly controlled turnstile may break, enter an undocumented state,
or enter a randomly chosen state. The only way to avoid problems is to
4By itself, G2 appears to be a liveness constraint on both enters and pushes. When G1 is also
considered, however, we see that the only legal exit from the nonaccepting state in G2 is an
enter.
Four Dark Corners of Requirements Engineering
•
13
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 14

ensure that (G3) lock and unlock actions alternate strictly, as the hardware
expects them to do. This safety constraint on locks and unlocks is optative
because these actions are just electronic signals emitted by the machine,
and nothing in the environment imposes any order on them.
As long as the alternation of locks and unlocks is maintained, after a lock
action the turnstile is locked and remains locked until the next unlock
action. The turnstile is designed so that whenever it is locked, push actions
cannot occur (G4). This is an indicative safety constraint on push actions,
and it is the main property that enables the turnstile to do its job of
guarding the gate.
The most important requirement on the gate complex is that people are
forced to pay for the privilege of entering. Forcing the alternation of enters
and pays would be too restrictive, however, because a teacher should be
able to pay at once for a whole classful of students and then lead them in
without interruption. The correct property is that the accumulated number
Fig. 1.
Some properties of the gate complex.
14
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 15

of enters never exceeds the accumulated number of pays. This is a safety
constraint on enter actions (G5).
For another set of examples, consider a lift (environment) and its
controller (machine). The lift environment has a number of designated
action types and properties. Some of the properties are formalized as Buchi
automata in Figure 2.
A begin-group-waiting[floor, direction]5 action occurs when the first
person approaches the lift at the indicated floor, with the intention of
traveling in the indicated direction. “First” means that no previously
arrived person is waiting at that floor for travel in that direction. An
end-group-waiting[floor, direction] action occurs when the members of a
waiting group (all at the same floor, intending to travel in the same
direction) enter the lift. Both these actions are environment-controlled and
unshared. It is easy to see that, by their nature, begin-group-waiting and
end-group-waiting must alternate (L1).
The primary lift requirement is that (L2) each begin-group-waiting action
leads to a corresponding end-group-waiting action. Note that L1 and L2 are
syntactically similar to G1 and G2, but G2 is indicative while L2 is
optative. G2 is enforced by the turnstile hardware, while L2 can only be
enforced by an effective lift controller.
A request[floor, direction] action occurs when a waiting person pushes the
indicated request button. Because we cannot expect the lift to serve a group
5 Lift action types are more complex. They have arguments or attributes, shown in brackets.
Fig. 2.
Some properties of the lift complex. Each diagram represents a set of distinct
automata, one for each distinct value of [floor, direction].
Four Dark Corners of Requirements Engineering
•
15
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


## PDF page 16

without knowing that it is waiting, we must assume about the environment
that (L3) a begin-group-waiting action leads to a corresponding request
action. This is an indicative liveness constraint on requests. Note that
requests and begin-group-waiting actions need not alternate. For example,
an impatient person might push the button more than once.
Among the action types controlled by the machine are motor-on, motor-
off, motor-up, motor-down, request-light-on[floor, direction], and request-
light-off[floor, direction], where the last two control up/down indicator
lights at each floor. The motor may break if the controller attempts to
change its direction while it is running, in which case there must be an
optative safety constraint that (L4) motor-ups and motor-downs do not
occur while the motor is on. This is similar in purpose to G3.
The remaining lift properties are not worth formalizing as Buchi autom-
ata, either because they are too repetitive or too complex. The previous
examples should be sufficient to show what phrases such as “do not occur”
and “leads to” mean in the brief paraphrases of these properties found in
Table I.
Note from L4 that motor-ons and motor-offs need not alternate—extra
commands are simply ignored by the motor. In a totally different situation,
a motor-up action could actually be designated as an action of changing the
motor direction from down to up (and similarly, from up to down for the
motor-down action). In this situation there is an indicative constraint that
(L5) motor-ups and motor-downs alternate. L5 is indicative because, given
the real-world meanings of motor-up and motor-down, no other behavior is
possible—you cannot change a direction from down to up when the direc-
tion is already up! Compare this to G3, which is optative because there is
nothing in the environment preventing two consecutive lock signals (it is
just that we will be sorry if the machine performs two consecutive locks and
thus breaks the turnstile).
One of the simpler lift requirements is that (L6) a request action leads to
a corresponding request-light-on action.
An arrive[floor] action occurs when the lift arrives at the indicated floor
(arrival at a floor does not necessarily mean that the lift stops there).
Arrive actions are shared with the machine by means of sensors. For
efficient lift scheduling, there might be a requirement that (L7) foolish
arrive actions do not occur, where “foolish” means that they do not satisfy
or move toward satisfying any outstanding request.
Further properties of the gate complex (G6, G7) and lift environment (L8)
will be added in the next section. By the time we have finished with these
examples, all of the spaces in Table I will have sample entries except the
space for indicative liveness constraints on machine-controlled actions.
Although we have no examples of these particular constraints and believe
they do not occur, the general point of the table is established without
them.
Any specification method will provide for optative constraints on ma-
chine-controlled actions (the lower-right corner of Table I) because they
describe what the machine must do. But optative constraints on environ-
16
•
Pamela Zave and Michael Jackson
ACM Transactions on Software Engineering and Methodology, Vol. 6, No. 1, January 1997.


