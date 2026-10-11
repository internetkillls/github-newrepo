# Human–Machine Reconfigurations: Plans and Situated Actions

Source ID: A06
Authors: Lucy A. Suchman
Original attachment: Human-Machine Reconfigurations_ Plans and Situated Actions, Lucy A Suchman.pdf
Identity: Cambridge University Press, 2nd edition, 2007.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 137

Case and Methods
123
THE USER
THE MACHINE
Actions not
Actions
Effects
Design rationale
available to
available
available
the machine
to the machine
to the user
ﬁgure 8.2. The analytic framework.
in using a relatively simple machine like a photocopier are faced with
the problem of doing together what either could do alone. In the interest
of the collaboration, each makes available to the other what she believes
to be going on: what the task is, how it is to be accomplished, what
has already been done and what remains, rationales for this way of
proceeding over that, and so forth. Through the ways in which each
collaborator works to provide her sense of what is going on to the other,
she provides that sense to the researcher as well. An artifact of such a
collaboration, therefore, is a naturally generated protocol.10
A second methodological commitment, which arose from the particu-
lar problem of looking at human–machine communication, directed the
analysis itself. The aim of the analysis was to ﬁnd the sense of “shared
understanding” in human–machine communication. More particularly,
I wanted to compare the user’s and the system’s respective views of the
interaction, over a sequence of events. In working to organize the tran-
scripts of the videotapes, therefore, I arrived at a simple framework (see
Figure 8.2). The framework revealed two initial facts about the relation-
ship of user and system. First, it showed that the coherence of the user’s
actions was largely unavailable to the system and something of why that
was the case. Beginning with the observation that what the user was try-
ing to do was, somehow, available to me as the researcher, I could ask
how that was so. The richest source of information for the researcher is
the verbal protocol (recorded in the ﬁrst column). In reading the instruc-
tions aloud, the user locates the problem that she is working on. Her
questions about the instructions identify the problem more particularly
10 Brown, Rubenstein, and Burton (1976) argue persuasively for the use of teams to gener-
ate protocols, where the discussions and arguments that unfold are treated as evidence
for the individual reasoning of the participants. The actions of the team members can
also be viewed as organized by the task of collaboration itself, however, although in the
interest of looking at the interaction of both users with the machine I have deliberately
avoided taking that view here. It is worth noting, in this regard, that analyses of “dis-
course” undertaken in the interest of building interactive Al systems generally tend to
view communication as the coincidence of individual reasoning processes, rather than
as an activity with a distinctive character arising from the collaboration itself. (Original
footnote.)


## PDF page 138

124
Human–Machine Reconﬁgurations
and further talk provides her interpretations of the machine’s behavior
and clariﬁes her actions in response.
A second, but equally crucial, resource is visual access to the user’s
actions. Of all of her actions, one could clearly see the very small subset,
recorded in the second column, that were actually detected by the sys-
tem. From the system’s “point of view,” correspondingly, one could see
how it was that those traces of the user’s actions available to the system
were mapped onto the system’s plan, under the design assumption that,
for example, button x pushed at this particular point in the procedure
must mean that the user is doing y.
The framework proved invaluable for taking seriously the idea that
user and machine were interacting. By treating the center two columns
as the mutually available, human–machine “interface,” one could com-
pare and contrast them with the outer columns, as the respective inter-
pretations of the user and the design. This comparison located precisely
the points of confusion, as well as the points of intersection or “shared
understanding.” Both are discussed at length in the next chapter.


## PDF page 139

9
Human–Machine Communication
Interaction is always a tentative process, a process of continuously testing
the conception one has of . . . the other.
(Turner 1962: original emphasis)
In Chapter 6 I outlined the view that the signiﬁcance of actions and
their intelligibility resides neither in what is strictly observable about
behavior, nor in a prior mental state of the actor, but in a contingently
constructed relationship among observable behavior, embedding cir-
cumstances, and intent. Rather than enumerating an a priori system of
normative rules for meaningful behavior, Chapter 7 described resources
for constructing shared understanding, collaboratively and in situ. Face-
to-face interaction was presented as the most fundamental and highly
developed system for accomplishing mutual intelligibility, exploiting a
range of linguistic, demonstrative, and inferential resources.
Given this view of the basis for action’s intelligibility, the situation
of action can be deﬁned as the full range of resources that the actor
has available to convey the signiﬁcance of his or her own actions and
to interpret the actions of others.1 Taking that preliminary deﬁnition of
the situation as a point of departure, my interest in this chapter is to
1 In light of subsequent readings, I realize that this statement could be taken to imply that
“the situation” exists somehow in advance of action and that it could at least in principle
be fully enumerated and represented in the form of a model to be referenced. The sense
of the situation I am after, however, is a radically performative and interactional one,
such that action’s situation is in signiﬁcant respects constituted through, or stands in
a reﬂexive relationship with, ongoing activity. It is through the latter that the sense
and relevance – just what the situation comprises – is produced, reenacted, contested,
and/or transformed.
125


## PDF page 140

126
Human–Machine Reconﬁgurations
consider “communication” between a person and a machine in terms
of the nature of their respective situations. For purposes of the analysis,
and without ascribing intent in any way, I will assume that the machine
is behaving on the basis of resources provided by “its” situation, the user
in accord with the resources of hers. The aim of the analysis then is to
view the organization of human–machine communication, including its
troubles, in terms of constraints posed by asymmetries in the respective
situation resources of human and machine.
In the case considered here, we can assume that the situation of the
user comprises preconceptions about the nature of the machine and the
operations required to use it, combined with moment-by-moment inter-
pretations of evidence found in and through the actual course of its use.
The situation of the machine or expert help system, in contrast, is con-
stituted by a plan for the use of the machine, written by the designer,
and implemented as the program that determines the machine’s behav-
ior and sensors that register changes to the machine’s state, including
some changes produced by the user’s actions. The design plan deﬁnes
what constitutes intelligible action by the user insofar as the machine
is concerned and determines what stands as an appropriate machine
response. The intersection of the situations of user and machine is the
locus both for successful exploitation of mutually available resources
and for problems of understanding that arise out of the disparity of
their respective situations.
engineering an appropriate response
The practical problem with which the designer of an interactive machine
must contend is how to ensure that the machine responds appropri-
ately to the user’s actions. As in human communication, an appropriate
response implies an adequate interpretation of the prior action’s sig-
niﬁcance. And as in human communication, the interpretation of any
action’s signiﬁcance is only weakly determined by the action as such.
Every action assumes not only the intent of the actor, but also the inter-
pretive work of the other in determining its signiﬁcance.2 That work, in
turn, is available only through the other’s response. The signiﬁcance of
any action and the adequacy of its interpretation are judged indirectly,
by responses to actions taken and by an interpretation’s usefulness in
2 See Bruner (1986) for a recent discussion of the contingency of interpretation with respect
both to text and to face-to-face interaction. (Original footnote.)


## PDF page 141

Human–Machine Communication
127
understanding subsequent actions. It is just this highly contingent pro-
cess that we call interaction.
For purposes of analysis, we can begin by considering two alter-
native perspectives on face-to-face interaction, with commensurately
different implications for the project of designing interactive machines.
The ﬁrst perspective ties successful interaction to each participant’s suc-
cess at anticipating the actions of the other and recommends an interac-
tive interface based on a preconceived model of the user that supports
the prediction of actions, the speciﬁcation of recognition criteria for the
actions predicted, and the prescription of an appropriate response. The
second view focuses on the ways in which interactional success com-
prisesresponsesthatareoccasionedby,andresponsiveto,unanticipated
actions of the other. This focus recommends an interactive interface that
maximizes sensitivity to actions actually taken by minimizing predeter-
mined sequences of machine behavior. The former recommendation is
constrained by limitations on the designer’s ability to predict any user’s
actions and the latter by limitations on the system’s access to and ability
to make sense out of the actions that a particular user takes.
The design strategy in the expert help system is to try to provide
the effect of an occasioned response through the use of a predictive
model. That is to say, the designer predicts that the user will have one
of a set of possible goals, of the form “use the machine to accomplish
outcome x.” Given that statement of intent, the machine displays a set of
instructions that prescribe the actions to be taken, at a level of generality
designedtoensuretheirrelevancetoanyuser,whateverthedetailsofher
particular situation. Ideally, the instructions tell the user what aspects
of her particular situation are relevant for the execution of this plan
through the machine’s operation. By ﬁnding or producing the objects
and actions described, the user anchors the general instructions to her
unique circumstances.
This chapter looks at some of the consequences of taking a state-
ment of intent and an ascribed plan as grounds for the interpretation of
situated action. To anticipate, that strategy involves an insensitivity to
particular circumstances that is both the system’s central resource and
its fundamental problem. I look ﬁrst at the system’s resources for con-
struing the actions of the user; namely, plans and states. I then consider the
problems posed for the designer by the user’s principal resource, orga-
nized under the general rubric of situated inquiries, and by the user’s
ability to ﬁnd the relevance of the system’s response to those inquiries.
Finally, I look at two classes of communicative breakdown, the false alarm


## PDF page 142

128
Human–Machine Reconﬁgurations
and the garden path. Chapter 10 concludes with implications of the anal-
ysis for a general account of mutual intelligibility and for the particular
requirements on the design of artifacts that would interact with their
users.
the system’s situation: plans and detectable states
The resources of the expert help system include a program that controls
its behavior and sensors that register certain changes to its state effected
by actions of the user. Initially, the user’s response to a series of questions
about her original documents and desired copies is taken as a statement
of her intent, and that statement in turn determines the selection by
the machine of one from a set of possible plans (see display 0, p. 169).
The plan is then presented to the user in the form of a stepwise set of
procedural instructions. The designer assumes that the plan matches
the user’s intent and that in following the procedural instructions the
user effectively is engaged in carrying out the plan.
The design premise is further that as the user takes the actions pre-
scribed by the instructions, those actions will change the state of the
machine in predictable ways. By taking those changes to the machine’s
state as traces of the user’s actions, the designer can effectively specify
how the user’s actions are to be recognized by the system and how the
system is to respond. The instructions are grouped in a series of dis-
plays such that the last action prescribed by each display produces an
effect that is detectable by the system, thereby initiating the process that
produces the next display. The design assumption is that by detecting
certain of the user’s actions, the system can follow her course in the
procedure and provide instructions as needed along the way.3
3 Because instructions were sometimes read by the users differently from the way that
they were actually written on the displays, the reader will ﬁnd some inconsistencies
between sequences and the displays to which they refer. The sequences comprise ver-
batim transcriptions of the users’ talk. Double quotes indicate that the user is reading
an instruction from the display. The displays reproduce the visual presentation (both
textual and illustrative) that the user ﬁnds on a video display terminal attached to the
photocopier. This includes headings that identify the type of information offered (i.e.,
“Assumptions,” “Overview,” “Instructions”), the instructions themselves, and pictures
of the copier and its parts. The boxed text at the bottom of each display (i.e., “Change
Task Description,” “Help,” “Start”) act as virtual “buttons” that, when selected by the
user with the cursor provided, initiate an associated operation. “Change Task Descrip-
tion” returns the user to display 0, “Help” brings up a display that expands on the
current instructions, and “Start” begins the copying operation. (Original footnote.)


## PDF page 143

Human–Machine Communication
129
The strategy of tying certain machine states to the presentation of par-
ticular next instructions enables the appearance of machine responses
occasioned by the user’s actions. So, in this light, we can view the interac-
tion between A and B in sequence I as the adept completion of what the
design attempts. Speciﬁcally, A decomposes and re-presents the instruc-
tions provided by the system, such that they are ﬁt more precisely to
B’s actions in carrying them out. A is able to do this because of her
sensitivity to what B is doing, including B’s troubles.
sequence i. A and B are proceeding from a display that established their goal as
making two-sided copies of a bound document. Two-sided copying requires an
unbound document, so they must begin by making a master unbound copy of
their document, using the “Bound Document Aid” or BDA.
The Users
The Machine
Not Available
to the Machine
Available
to the Machine
Available
to the User
Design
Rationale
A: “To access the BDA,
pull the latch labeled
Bound Document Aid”:
(A and B turn to
machine)
display 2
Instructions for
copying a bound
document:
Accessing the
bound document
aid.
(Points) Right there.
B: (Hands on latch)
A: “And lift up to the left.”
(Looks to B, who
struggles with the latch)
“Lift up and to the left.”
B: (Still struggling)
A: Okay::
B: Pu::ll, and lift up to the
left.
(Looks at picture)
Oh, the whole thing.
[
A:
Yea.
B: Lift up and to the left.
Opens BDA


## PDF page 144

130
Human–Machine Reconﬁgurations
Below is the procedure from sequence 1, as represented in the pro-
gram that controls the display of instructions to the user:
Step 1
Set Panel
[display 1]
Step 2: Tell User “You need to use the Bound Document Aid . . . ”
[display 2]
Step 3: Tell User “Place your original face down . . . Slide the docu-
ment cover left . . . ”
[display 3]
Step 4: Make Ready.
Step 5: Tell User “Press Start.” Requirements:
Panel Set (If not, try Step I)
RDH raised (if not, try Step 2)
Document cover closed (if not, try Step 3)
Ready State (if not, try Step 4)
[display 4]
Step 6: Complete printing Step.
Requirements: Printing State (if not, try Step 5)
Rather than proceeding through the steps of the procedure consecu-
tively, the system starts with the last step of the procedure, Step 6 in this
case, and checks to see whether it is completed. A step is completed if a
check of the machine’s state conﬁrms that the conditions represented by
that step’s requirements have been met. The requirements in this sense
represent features of the system’s situation (or, more accurately, of the
system’s own state) that are resources in determining an appropriate
next instruction or action. When a requirement is found that is not met,
a further set of speciﬁcations, tied to that requirement, sends the system
back to an earlier step in the procedural sequence. The system then dis-
plays the instructions tied to that earlier step to the user until another
change in state begins the same process again. Each time the user takes
an action that changes the machine’s state, the system compares the
resulting state with the end state, returns to the ﬁrst unﬁnished step in
the sequence, and presents the user with the instructions for that and
any subsequent step.
Through this simple device of working backward through the pro-
cedure, the presentation of redundant instructions can be avoided. In
sequence II, having discovered that their original document is larger
than standard paper, A and B decide to redo the job. They return to the


