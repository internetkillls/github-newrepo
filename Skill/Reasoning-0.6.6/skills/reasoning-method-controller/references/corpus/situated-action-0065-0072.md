# Human–Machine Reconfigurations: Plans and Situated Actions

Source ID: A06
Authors: Lucy A. Suchman
Original attachment: Human-Machine Reconfigurations_ Plans and Situated Actions, Lucy A Suchman.pdf
Identity: Cambridge University Press, 2nd edition, 2007.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 65

5
Plans
Once the European navigator has developed his operating plan and has
available the appropriate technical resources, the implementation and
monitoring of his navigation can be accomplished with a minimum of
thought. He has simply to perform almost mechanically the steps dic-
tated by his training and by his initial planning synthesis.
(Gladwin 1964: 175)
Every account of communication involves assumptions about action,
in particular about the bases for action’s coherence and intelligibility.
This chapter and the next discuss two alternative views of action. The
ﬁrst, adopted by most researchers in artiﬁcial intelligence, locates the
organization and signiﬁcance of human action in underlying plans. At
least as old as the Occidental hills, this view of purposeful action is
the basis for traditional philosophies of rational action and for much of
the behavioral sciences. It is hardly surprising, therefore, that it should
be embraced by those newer ﬁelds concerned with intelligent artifacts,
particularly cognitive science and information-processing psychology.
On the planning view, plans are prerequisite to and prescribe action, at
every level of detail. Mutual intelligibility is a matter of the reciprocal
recognizability of our plans, enabled by common conventions for the
expression of intent and shared knowledge about typical situations and
appropriate actions. The alternative view, developed in Chapter 6 of
this book, is that although the course of action can always be projected
or reconstructed in terms of prior intentions and typical situations, the
prescriptive signiﬁcance of intentions for situated action is inherently
51


## PDF page 66

52
Human–Machine Reconﬁgurations
vague. The coherence of situated action is tied in essential ways not to
individual predispositions or conventional rules but to local interactions
contingent on the actor’s particular circumstances.1 A consequence of
action’s situated nature is that communication must incorporate both a
sensitivity to local circumstances and resources for the remedy of trou-
bles in understanding that inevitably arise. This chapter reviews the
planning model of purposeful action and shared understanding. Those
who adopt the planning model as a basis for interaction between people
and machines draw on three related theories about the mutual intelli-
gibility of action: (1) the planning model itself, which takes the signiﬁ-
cance of action to be derived from plans and identiﬁes the problem for
interaction as their recognition and coordination; (2) speech act theory,
which accounts for the recognizability of plans or intentions by propos-
ing conventional rules for their expression; and (3) the idea of shared
background knowledge, as the common resource that stands behind
individual action and gives it social meaning. Each of these promises to
solve general problems in human communication, such as the relation
of observable behavior to intent, the correspondence of intended and
interpreted meaning, and the stability of meaning assignments across
situations, in ways that are relevant to particular problems in people’s
interaction with machines.
the planning model
The planning model in cognitive science treats a plan as a sequence
of actions designed to accomplish some preconceived end. The model
posits that action is a form of problem solving, where the actor’s problem
is to ﬁnd a path from some initial state to a desired goal state, given
1 The term circumstances of course begs a further set of questions. Most important for
the purpose of this argument is recognition of the extent to which the conditions of our
actions are not simply pregiven and self-evident but are themselves constituted through
unfolding courses of action and interaction. This is not to say that action is constructed
somehow always de novo or in a vacuum. On the contrary, human activity invariably
occurs in circumstances that include more and less long-standing, obdurate, and com-
pelling layers of culturally and historically constituted, social and material conditions.
However familiar and constraining, though, the signiﬁcance of those conditions, and
their relevance for what is happening here and now, must be actively reenacted by par-
ticipants in ways not fully speciﬁed in advance or in any strongly determinate way. For
explorations of the improvisatory character of action drawn from close studies of jazz
performance, see Sawyer (2003).


## PDF page 67

Plans
53
certain conditions along the way. Actions are described, at whatever
level of detail, by their preconditions and their consequences:
In problem-solving systems, actions are described by prerequisites (i.e., what
must be true to enable the action), effects (what must be true after the action has
occurred), and decomposition (how the action is performed, which is typically
a sequence of subactions). (Allen 1984: 126)
Goals deﬁne the actor’s relationship to the situation of action, because
the situation is just those conditions that obstruct or advance the actor’s
progress toward his or her goals. Advance planning is inversely related
to prior knowledge of the environment of action and of the conditions
that the environment is likely to present. Unanticipated conditions will
requirereplanning.Ineverycase,however,whetherconstructedentirely
in advance or completed and modiﬁed during the action’s course, the
plan is prerequisite to the action.
Plan Generation and Execution Monitoring
One of the earliest attempts to implement the planning model on a
machine occurred as part of a project at Stanford Research Institute,
beginning in the mid-1960s. The project’s goal was to build a robot that
could navigate autonomously through a series of rooms, avoiding obsta-
cles and moving speciﬁed objects from one room to another. The robot,
named by its designers Shakey, was controlled by a problem-solving
program called STRIPS, which employed a means–end analysis to deter-
mine the robot’s path (Fikes and Nilsson 1971). The STRIPS program
examined the stated goal and then determined a subset of operators, or
actions available to the robot, that would produce that state. The pre-
conditions of those actions in turn identiﬁed particular subgoal states,
which could be examined in the same way. The system thus worked
backward from the goal until a plan was deﬁned from the initial state
to the goal state, made up of actions that the robot could perform. Sub-
sequent work on problem solving and plan synthesis consisted in large
part in reﬁnements to this basic means–ends strategy, toward the end of
achieving greater efﬁciency by constraining the search through possible
solution paths.2
Beyond the problem of constructing plans, artiﬁcial intelligence
researchers have had to address problems of what Nilsson (1973) terms
2 For a review of subsequent work see Sacerdoti (1977, Chapter 3). (Original footnote.)


## PDF page 68

54
Human–Machine Reconﬁgurations
failure and surprise in the execution of their planning programs, due to
the practical exigencies of action in an unpredictable environment. The
objective that Shakey should actually be able to move autonomously
through a real (albeit somewhat impoverished) environment added a
new class of problems to those faced by mathematical or game-playing
programs operating in an abstract formal domain:
for a problem-solver in a formal domain is essentially done when it has con-
structed a plan for a solution; nothing can go wrong. A robot in the real world,
however, must consider the execution of the plan as a major part of every task.
Unexpected occurrences are not unusual, so that the use of sensory feedback
and corrective action are crucial. (Raphael, cited in McCorduck 1979: 224)
In Shakey’s case, execution of the plan generated by the STRIPS program
was monitored by a second program called PLANEX. The PLANEX
program monitored not the actual moves of the robot, however, but the
execution of the plan. The program simply assumed that the execution
of the plan meant that the robot had taken the corresponding action in
the real world. The program also made the assumption that every time
the robot moved there was some normally distributed margin of error
that would be added to a “model of the world” or representation of the
robot’s location. When the cumulative error in the representation got
large enough, the plan monitor initiated another part of the program
that triggered a camera that could, in turn, take a reading of Shakey’s
location in the actual world.
The uncertainty to which Shakey was to respond consisted in changes
made to the objects in its environment. Another order of uncertainty
was introduced with Sacerdoti’s system NOAH (an acronym for Nets
ofActionHierarchies).AlsodevelopedattheStanfordResearchInstitute
as part of the Computer-Based Consultant project, NOAH was designed
to monitor and respond to the actions of a human user. With NOAH,
Sacerdoti extended the techniques of problem solving and execution
monitoring developed in the planning domain to the problem of inter-
active instruction:
NOAH is an integrated problem solving and execution monitoring system. Its
major goal is to provide a framework for storing expertise about the actions
of a particular task domain, and to impart that expertise to a human in the
cooperative achievement of nontrivial tasks. (Sacerdoti 1977: 2)
The output of the planning portion of Sacerdoti’s program is a “pro-
cedural net” or hierarchy of partially ordered actions, which becomes
in turn the input to the execution-monitoring portion of the system. The


## PDF page 69

Plans
55
execution monitor takes the topmost action in the hierarchy, provides
the user with an instruction, and then queries the user regarding the
action’s completion. A principal objective of the innovations that Sacer-
doti introduced for the representation of procedures in NOAH was to
extend execution monitoring to include tracking and assessment of the
user’s actions in response to the instructions generated:
The system will monitor the apprentice’s work to ensure that the operation
is proceeding normally. When the system becomes aware of an unexpected
event, it will alter instructions to the apprentice to deal effectively with the new
situation. (ibid.: 3)
A positive response from the user to the system’s query regarding
the action is taken to mean that the user understood the instruction and
has successfully carried it out, whereas a negative response is taken as
a request for a more detailed instruction. The system allows as well for
a “motivation response” or query from the user as to why a certain task
needs to be done (to which the system responds by listing tasks to which
the current task is related) and for an “error response” or indication from
the user that the current instruction cannot be carried out. Just as the
accumulation of error in the PLANEX program required feedback from
the world in order to reestablish the robot’s location, the error response
from the user in Sacerdoti’s system requires that NOAH somehow repair
its representation of the user’s situation:
PLANEX presumed that an adequate mechanism existed for accurately updat-
ing the world model. This was almost the case, since there were only a small
number of actions that the robot vehicle could take, and the model of each action
contained information about the uncertainty it would introduce in the world
model. When uncertainties reached a threshold, the vision subsystem was used
to restore the accuracy of the world model.
For the domain of the Computer-Based Consultant, or even for a richer robot
domain, this approach will prove inadequate . . . NOAH cannot treat the world
model as a given. It must initiate interactions with the user at appropriate points
to ensure that it is accurately monitoring the course of the execution . . .
[W]hen a serious error is discovered (requiring the system to be more thor-
oughinitseffortstodeterminethestateoftheworld),thesystemmustdetermine
what portions of its world model differ from the actual situation. (ibid.: 71–2)
The situation in which Shakey moved consisted of walls and boxes
(albeit boxes that could be moved unexpectedly by a human hand). The
problem in designing Shakey was to maintain consistency between
the represented environment and the physical environment in which
the robot moved. In introducing the actions of a user, the computer’s


## PDF page 70

56
Human–Machine Reconﬁgurations
environment becomes not only a physical but also a social one, requir-
ing the interpretation of the user’s actions and an assessment of the
user’s understanding of his or her situation. The difﬁculty of maintain-
ing a shared understanding of a situation, as shown more clearly in
Chapters 8 and 9, is not just a matter of monitoring the course of events
but of establishing their signiﬁcance. Nonetheless, with Sacerdoti we
have at least a preliminary recognition of the place of the situation in
the intelligibility of action and communication.
Interaction and Plan Recognition
Adherents of the planning model in artiﬁcial intelligence research have
taken the requirement of interaction as an injunction to extend the plan-
ning model from a single individual to two or more individuals acting in
concert. The planning model attempts to bring concerted action under
the jurisdiction of the individual actor by attaching to the others in the
actor’s world sufﬁcient description and granting to the actor sufﬁcient
knowledge that he or she is able to respond to the actions of others
as just another set of environmental conditions. The problem of social
interaction, consequently, becomes an extension of the problem of the
individual actor. The basic view of a single, goal-directed agent, act-
ing in response to an environment of conditions, is complicated (the
conditions now include the actions of other agents) but intact.
The problem for interaction, on this view, is to recognize the actions
of others as the expression of their underlying plans. The complement to
plan generation and execution in artiﬁcial intelligence research, there-
fore, is plan recognition or the attribution of plans to others based on
observation of their actions. The starting premise for a theory of plan
recognition is that an observer takes some sequence of actions as evi-
dence and then forms hypotheses about the plans that could motivate
and explain those actions.
One persisting difﬁculty for action understanding in artiﬁcial intel-
ligence research has been the uncertain relation between actions and
intended effects. Allen (1984) illustrates this problem with the example
of turning on a light:
There are few physical activities that are a necessary part of performing the
action of turning on a light. Depending on the context, vastly different pat-
terns of behavior can be classiﬁed as the same action. For example, turning
on a light usually involves ﬂipping a light switch, but in some circumstances
it may involve tightening the light bulb (in the basement) or hitting the wall


## PDF page 71

Plans
57
(in an old house). Although we have knowledge about how the action can be
performed, this does not deﬁne what the action is. The key deﬁning characteris-
tic of turning on the light seems to be that the agent is performing some activity
which will cause the light, which was off when the action started, to become
on when the action ends. An important side effect of this deﬁnition is that we
could recognize an observed pattern of activity as “turning on the light” even
if we had never seen or thought about that pattern previously. (ibid.: 126)
Allen’s point is twofold. First, the “same” action as a matter of intended
effectcanbeachievedinany number ofways, wherethewaysarecontin-
gent on circumstance rather than on deﬁnitional properties of the action.
And second, although an action can be accounted for post hoc with refer-
ence to its intended effect, an action’s course cannot be predicted from
knowledge of the actor’s intent, nor can the course be inferred from
observation of the outcome. Allen identiﬁes the indeterminate relation-
ship of intended effect to method as a problem for planning or plan
recognition systems: a problem that he attempts to resolve by construct-
ing a logical language for action descriptions that handles the distinction
between what he calls the “causal deﬁnition” of an action (i.e., the pre
and post conditions that must hold to say that the action has occurred,
independent of any method) and the action’s characterization in terms
of a particular method or procedure for its accomplishment.3
Whereas Allen’s approach to the problem of plan recognition is an
attempt to reconstruct logically our vocabulary of purposeful action, a
few more psychologically oriented researchers in artiﬁcial intelligence
have undertaken experiments designed to reveal the process by which
people bring the actions of others under the jurisdiction of an ascribed
plan. Schmidt, Sridharan, and Goodson (1978) observe, for example, that
plan attribution seems to require certain transformations of the sequen-
tial organization of the action described.4 They report that throughout
the process of plan attribution the problem to be solved by the subject
remains “ill-formed,” by which they mean that at any given time nei-
ther the range of possible plans that the other might be carrying out,
3 Another, less problematic, uncertainty that Allen attempts to capture is the observation
that while some components of an action are sequentially ordered in a necessary way
(i.e., one is prerequisite to the other), other components, although necessary to the
action, have no necessary sequential relationship to each other. The incorporation of
unordered actions into the structure of plans, pioneered by Sacerdoti (1975), was viewed
as a substantial breakthrough in early planning research. (Original footnote.)
4 The empirical method of their study is unusual in artiﬁcial intelligence research, where
work generally proceeds on the basis of imagination and introspection. (Original
footnote.)


## PDF page 72

58
Human–Machine Reconﬁgurations
nor the criteria for assessing just what plan is actually in effect, are
clearly deﬁned (ibid.: 80). Nonetheless, they report that their subjects
are able to posit an underlying plan. Their strategy appears to be to
adopt tentatively a single hypothesis about the other’s plan rather than
entertainallorevensomenumberoflogicalpossibilitiessimultaneously.
The preferred hypothesis regarding the other’s plan then affects what
actions are noted and recalled in the subject’s accounts of the action,
and the temporal order of events is restructured into logical “in order
to” or “because” relationships, such that relations among actions are not
restricted to consecutive events in time. At the same time, the current
hypothesis is always subject to elaboration or revision in light of sub-
sequent events to the extent that subjects are often required to suspend
judgment on a given hypothesis and to adopt a “wait and see” strategy.
Wherever possible, actions that violate the structure of an attributed
plan are explained away before the plan itself is reconsidered. Schmidt,
Shridharan, and Goodson conclude that all of these observations “sup-
port the generalization that action understanding is simply a process of
plan recognition” (ibid.: 50). It is worth noting, however, that although
these observations clearly point to a process of plan attribution by the
observer, there is no independent evidence that the process of plan attri-
bution is a process of recognizing the plan of the actor.
The Status of Plans
Assessment of the planning model is complicated by equivocation in
the literature between plans as a conceptual framework for the analy-
sis and simulation of action and plans as a psychological mechanism
for its actual production. When researchers describe human action in
terms of plans, the discussion generally ﬁnesses the question of just how
the formulations provided by the researcher are purported to relate to
the actor’s intent. The claim is at least that people analyze each other’s
actions into goals and plans to understand each other. But the sugges-
tion that the plan is “recognized” implies that it has an existence prior
to and independent of the attribution and that it actually determines the
action. The identiﬁcation of the plan with the actor’s intent is explicit in
the writing of philosophers of action supportive of artiﬁcial intelligence
research like Margaret Boden, who writes:
unless an intention is thought of as an action-plan that can draw upon back-
ground knowledge and utilize it in the guidance of behavior one cannot under-
stand how intentions function in real life. (1973: 27–8)


