# Human–Machine Reconfigurations: Plans and Situated Actions

Source ID: A06
Authors: Lucy A. Suchman
Original attachment: Human-Machine Reconfigurations_ Plans and Situated Actions, Lucy A Suchman.pdf
Identity: Cambridge University Press, 2nd edition, 2007.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 193

Conclusion to the 1st Edition
179
machines requires essentially the same interpretive work that charac-
terizes interaction between people, but with fundamentally different
resources available to the participants. In particular, people make use
of a rich array of linguistic, nonverbal, and inferential resources in ﬁnd-
ing the intelligibility of actions and events, in making their own actions
sensible, and in managing the troubles in understanding that inevitably
arise. Today’s machines, in contrast, rely on a ﬁxed array of sensory
inputs, mapped to a predetermined set of internal states and responses.
The result is an asymmetry that substantially limits the scope of inter-
action between people and machines. Taken seriously, this asymmetry
poses three outstanding problems for the design of interactive machines:
ﬁrst,theproblemofhowtolessentheasymmetrybyextendingtheaccess
of the machine to the actions and circumstances of the user; second, the
problem of how to make clear to the user the limits on the machine’s
access to those basic interactional resources; and ﬁnally, the problem of
how to ﬁnd ways of compensating for the machine’s lack of access to
the user’s situation with computationally available alternatives.
toward practical solutions
In the design of interactive machines the most common substitute for
access to the user and her situation has been the incorporation into
the machine of a preconceived representation of the user and her sit-
uation or a “user model.” User models, constructed in advance as the
template against which the user’s actual actions are mapped, comprise
propositions about the domain, the task, the typical user, and the like.
Recently, designers concerned with the provision of situated help, or so-
called intelligent tutoring systems, have begun extending such models
to support local or “real-time” assessment of the actions of the computer
user (see Burton and Brown 1982; London and Clancey 1982; Woolf
and McDonald 1983; Farrell, Anderson, and Reiser 1984; Peachey and
McCalla 1986; Shrager and Finin 1982). A primary objective of such sys-
tems is to infer the user’s knowledge and misconceptions about the
system by observing her actions rather than relying on either error
conditions or explicit requests for help. To appreciate the requirements
of this objective, one has simply to imagine those occasions where an
expert, watching a novice engaged in some activity, would be moved to
inspiration for solutions, which then are best addressed through the affordances that
particular artifacts (input devices, graphical displays, and the like) afford. See Luff,
Gilbert, and Frohlich 1990; Thomas 1995.


## PDF page 194

180
Human–Machine Reconﬁgurations
intercede. The outstanding question with respect to this form of coach-
ing is “Just what does seeing those places where assistance is called for,
and knowing what needs to be said, involve?” Researchers pursuing
“real-time user modeling” as the basis for a solution to this problem
have adopted the following design strategies:
(1) Diagnosis based on differential modeling. A principal strategy for so-
called intelligent tutoring systems, or computer-based coaches, has been
to work from an ideal model of expert behavior in a given domain, to
which the actions of the student can be mapped.7 It is then the difference
between expert and student behavior in particular circumstances that
serves as the basis for assessing the student’s knowledge and skills.
The diagnosis works both on manifested errors that arise in the course
of the student’s actions and, more subtly, on the omission of actions
that, given a particular set of conditions, an idealized expert in those
circumstances would take. The rationale for the differential modeling
strategy is a combination of predictions based on the model of expert
behavior, with techniques for local assessment of the student’s actions.
The success of the strategy turns on the degree of ﬁt between the actions
anticipated by the diagnostic model and the actions of the student that
are detectable by the machine.
(2) Detection of diagnostic inconsistencies. However felicitous the ﬁt
between student actions and diagnostic issues, the design must accom-
modate the likelihood of misdiagnosis and provide for its detection and
repair. In the best intelligent tutoring systems, the accumulating record
of student actions includes both actions that manifest some issue that
according to the current diagnosis should not appear and actions that
fail to manifest some issue that the student seems from prior diagnosis to
understand. Evidence of misdiagnosis is found in the amount of “tear”
or inconsistency in the accumulating record of student actions.8 When
the disparity between the developing diagnostic model of what the stu-
dent knows and doesn’t know and the understanding demonstrated
in subsequent actions reaches a certain threshold, the program may
invoke alternative strategies that the student might be using. Possible
alternative strategies, identiﬁed according to local evidence, are then
tested for consistency with the global history of the student’s actions.
7 For a critical survey of the state of the art in intelligent tutoring systems at the time, see
Wenger 1987.
8 The notion of “tear,” and many other subtleties now beginning to be incorporated in the
design of computer-based coaches, originates in Burton and Brown’s work on WEST
(1982). (Original footnote)


## PDF page 195

Conclusion to the 1st Edition
181
Crucially, the domain must be sufﬁciently closed that the set of possible
alternative strategies can be enumerated.
(3) Separation of local and global interpretations. Recent tutoring systems
begin to make use of a mechanism basic to everyday human commu-
nication, namely, the separation and productive interaction between
local and global interpretations of the other’s actions. The diagnosis of
student actions in computer-based tutoring systems is accomplished
through two independent though interrelated mechanisms: one com-
ponent that is data driven from the local context of a given action and
another that runs over an accumulating history of the student’s actions
with the goal of identifying weaknesses or misunderstandings. As in
the interpretation of action in the course of a developing conversation,
it is the interaction of these two perspectives that affords the power of
the diagnosis. The locality of the data-driven component supports an
assessment of each particular action, relatively unconstrained by global
preconceptions, whereas the global perspective of the evaluative com-
ponent supports the interpretation of that action as a reﬂection of the
student’s general strategies and skills.
(4) The constructive use of trouble. In much the way that ordinary conver-
sation relies on the successful detection, repair, and even exploitation of
troubles in understanding, recent tutoring systems adopt a “construc-
tivist position” toward errors, such that the inevitability of student mis-
conceptions or weaknesses is turned to pedagogical advantage (Burton
and Brown 1982). The goal of the coach in such systems is not to avoid
student errors but to make them accessible to the student and therefore
instructive. If the student has enough information to identify and repair
an error, then it is considered a constructive one. If, on the other hand,
the error is not manifest in such a way as to be visible, or is perceived but
the student lacks the necessary information for its repair, the trouble is
nonconstructive. One major task of the coach, on this view, is to give the
student the information required to transform nonconstructive troubles
into constructive ones, either by diagnosing the trouble and making it
accessible or by providing the information required for its repair.
This last strategy has recently been generalized as a call to design
for the management of trouble (see Brown and Newman 1985). Such
an objective implies at least that users are encouraged to use the wider
social setting in which a machine is embedded as a resource to rem-
edy the troubles in understanding that inevitably arise. Applied to the
design of machines, this recommends incorporating the kind of diag-
nostic and interactional abilities that characterize the human coach into


## PDF page 196

182
Human–Machine Reconﬁgurations
the machine itself. The problem in applying this later recommendation
is that often the “grain size” of machine-readable actions is either too
small or too large to constrain the analysis of the user’s actions ade-
quately. So, for example, in the case of the help system examined in
Chapter 9, to appreciate the signiﬁcance of a given user action – say,
putting a document into the document handler – may require reference
to a history that extends across procedures as the system tracks them.
Alternatively, assessing the user’s actions may require reference to sub-
procedures, such as ordering pages of a document correctly, for which
there is no trace. In general, if there is more than one understanding that
can produce what appears to be the same action, detecting the action
does not serve as unequivocal evidence that the understanding is actu-
ally in hand. By the same token, if a given skill can be manifest in some
indeﬁnite number of different actions, then the absence of an expected
action does not necessarily mean the absence of the skill. While in the
case of the human coach these ambiguities are resolved through interac-
tion, in the case of a computer-based coach the limits on the machine’s
access pose a difﬁcult design problem. The problem is not simply that
communicative troubles arise that do not arise in human communica-
tion but rather that when the inevitable troubles do arise, there are not
the same resources available for their detection and repair.9
plans as resources for action
Some researchers in human–computer interaction make the claim that
cognitive science and computer technologies have advanced to the point
where it is now feasible to build instructional computer systems that are
as effective as experienced human tutors (see, for example, Anderson,
Boyle, and Reiser 1985). In contrast to this optimism, I have argued that
there is a profound and persisting asymmetry in interaction between
people and machines, due to a disparity in their relative access to the
9 Although this discussion locates strategies for the solution of the problems identiﬁed
in the previous chapters in various approaches to the design of so-called intelligent
tutoring systems, or “help” systems more generally, I would now take a rather different
tack. Along with ongoing efforts to develop the art of interface design, the problem of
human–machinecommunicationsuggestswhatisatonceamoremodestandamorerad-
ical approach. That is to abandon the attempt to create the “self-explanatory” machine
in favor of encouraging social arrangements that provide for the necessary time and
resources needed to incorporate unfamiliar artifacts effectively into relevant forms of
practice. This latter strategy shifts the focus away from the interface narrowly deﬁned
and, in so doing, implicates much broader and more profound forms of social change.
I return to approaches that adopt this strategy, as various projects in participatory or
cooperative design, in Chapter 15.


## PDF page 197

Conclusion to the 1st Edition
183
moment-by-moment contingencies that constitute the conditions of sit-
uated interaction. Because of the asymmetry of user and machine, inter-
face design is less a project of simulating human communication than
of engineering alternatives to interaction’s situated properties. The pri-
mary alternative has been to substitute a generalized representation of
the situation of action for access to the details of the user’s particular
situation. As in the expert help system analyzed in Chapter 9, the rep-
resentational scheme favored by many designers has been the plan. The
problem for designers is that, as commonsense formulations of intent,
plans are inherently vague. To the cognitive scientist, this representa-
tional vagueness is a fault to be remedied insofar as a plan is the prereq-
uisite for purposeful action, and the details of action are derived from
the completion and modiﬁcation of the plan. The task of the designer
who would model situated action, therefore, is to improve on, or render
more precise and axiomatic, the plan.
For situated action, however, the vagueness of plans is ideally suited
to the fact that the detail of intent and action must be contingent on the
circumstantial and interactional particulars of actual situations. Given
this view of plans, namely, as resources for action rather than as control-
ling structures, the outstanding problem is not to improve on them but to
understand what kind of resource they are. The most promising approach is
to begin from the observation that plans are representations or abstrac-
tions over action.10 In one sense, this simply joins the problem of plans
to the more general, and no less difﬁcult, question of representation. But
in another sense, viewing plans as representations is suggestive of what
their relation to unrepresented actions might be.
Chapter 6 introduced a view, developed recently by Barwise and
Perry (1985), that language can be characterized in terms of its efﬁ-
ciency and indexicality. By efﬁciency is meant simply the ways in which
“expressions used by different people, in different space–time locations,
with different connections to the world around them, can have different
interpretations, even though they retain the same linguistic meaning”
(ibid.: 5). In its efﬁciency, language provides us with a shareable resource
for talk about the world. At the same time, the efﬁciency of language
10 My phrasing here might suggest that I see this kind of reconceptualization as sufﬁ-
cient, but I would emphasize now that this is simply a starting place from which to
pursue investigations of how plans, as orienting devices that work in multiple ways
are created and used in practice (see Chapter 11). I am grateful to Eevi Beck for having
pointed out the potential misreading of this statement and urging me to emphasize the
importance of empirical studies. For a study of the ﬂuid nature of rules and agreements
in collaborative writing practices, see Beck (1995).


## PDF page 198

184
Human–Machine Reconﬁgurations
requires that our utterances always be anchored to the unique and par-
ticularoccasionsoftheiruse.Inthisrespect,languageisindexical;thatis,
dependent for its signiﬁcance on connections to particular occasions and
to the concrete circumstances in which an utterance is spoken. This view
of language is taken as foundational by Garﬁnkel (1967) and Garﬁnkel
and Sacks (1970) with respect to the intelligibility and signiﬁcance of
action.
Like other linguistic representations, plans are efﬁcient formulations
of situated actions. By abstracting uniformities across situations, plans
allow us to bring past experience and projected outcomes to bear on
our present actions. As efﬁcient formulations, however, the signiﬁcance
of plans turns on their relation back to the unique circumstances and
unarticulated practices of situated activities. A problem for an account
of situated action, on this view, is to describe the processes by which
efﬁcient representations are brought into productive interaction with
particular actions in particular environments. A rich description of this
process comes, for example, from research on Micronesian navigation
reported by Edwin Hutchins (1983).11 The natives of the Caroline Islands
routinely embark on ocean-going canoe voyages that take them several
days out of the sight of land. Western researchers traveling with them
have found that at any time during the voyage the navigators can indi-
cate the bearings of the port of departure, the target island, and other
islands off to the side of the course they are steering, even though these
may all be over the horizon and out of sight. They are able to do this
and other feats of navigation that are simply impossible for a West-
ern navigator without instruments. What Hutchins reports is that they
maintain their course by substituting other environmental referents, that
are accessible, for the inaccessible land. In particular, they follow a star
path, selected with reference to a sidereal compass or star chart that
forms a map between pairs of islands. To maintain their orientation to
the star path at any given point in their voyage requires that they con-
sult not only the stars, but also a rich set of changing environmental
circumstances – the color of the water, the waves, winds and clouds,
birds, and so forth – which through experience become interpretable
for information about the relative position of the canoe. What is notable
about Hutchins’s account of the resources of the Micronesian navigator
is that nowhere is a preconceived plan in evidence. The basis for navi-
gation seems to be, instead, local interactions with the environment. In
11 See also Gladwin (1970), Turnbull (1990, 2000), Lewis (1972), Hutchins (1995).


## PDF page 199

Conclusion to the 1st Edition
185
this way, navigators maintain their orientation to the star path, which
in turn is ﬁxed to the islands of origin and destination.
The Micronesian example demonstrates how the nature of an activ-
ity can be missed unless one views purposeful action as an interac-
tion between a representation and the particular, contingent details
of the environment. With respect to plans and actions, Feitelson and
Steﬁk (1977) found this same relation present in the work of geneticists
planning scientiﬁc experiments. Speciﬁcally, they found that geneticists
elaborated their plans only far enough to act as a framework in which
to organize the constraints of the laboratory. Rather than planning the
experiment through an a priori analysis, the experimenters decided
what to do next by relating each current observation to their research
goals. The experimenters’ expertise lay not in completing the plan but in
the ability to generate hypotheses continually and to exploit serendipity
in the course of the experiment. The experimental process, being what
Feitelson and Steﬁk call “event driven,” allowed the experimenter to
“ﬁsh for interesting possibilities”; that is, to follow up on unanticipated
observations and opportunities provided by a particular experimental
setup.
From these and other examples, we can begin to draw an alterna-
tive account of the relation of plans to situated actions. The foundation
of actions by this account is not plans but local interactions with our
environment, more and less informed by reference to abstract repre-
sentations of situations and of actions and more and less available to
representation themselves. The function of abstract representations is
not to serve as speciﬁcations for the local interactions but rather to ori-
ent or position us in a way that will allow us, through local interactions,
to exploit some contingencies of our environment and to avoid others.
Although plans can be elaborated indeﬁnitely, they elaborate actions
just to the extent that elaboration is useful; they are vague with respect
to the details of action precisely at the level at which it makes sense to
forego abstract representation and rely on the availability of a particular,
embodied response.
The interesting problem for an account of action, ﬁnally, is to describe
how it is that we are able to bring efﬁcient descriptions (such as plans)
and particular circumstances into productive interaction. The assump-
tion in planning research in cognitive science has been that this process
consists in ﬁlling in the details of the plan to some operational level. But
when we look at actual studies of situated action, it seems that situated
action turns on local interactions between the actor and contingencies
that, although they are made accountable to a plan, remain essentially


## PDF page 200

186
Human–Machine Reconﬁgurations
outside of the plan’s scope. Just as it would seem absurd to claim that a
map in some strong sense controlled the traveler’s movements through
the world, it is wrong to imagine plans as controlling actions. However,
the questions of how a map is produced for speciﬁc purposes, how in
any actual instance it is interpreted vis-`a-vis the world, and how its
use is a resource for traversing the world are both reasonable and pro-
ductive.12 In the last analysis, it is in the interaction of representation
and represented where, so to speak, the action is.13 To get at the action
in situ requires accounts not only of efﬁcient, symbolic representations
but also of their productive interaction with the unique, unrepresented
circumstances in which action in every instance and invariably occurs.
A starting premise of this book was that the project of building inter-
active machines has more to gain by understanding the differences
between human interaction and machine operation than by simply
assuming their similarity. My argument has been that as long as machine
actions are determined by stipulated conditions, machine interaction
with the world, and with people in particular, will be limited to the
intentions of designers and their ability to anticipate and constrain the
user’s actions.14 The generality of various representations of situations
and actions is the principle resource for this task, whereas the context
insensitivity of such representational schemes is the principle limita-
tion. The question, ﬁnally, is “What are the consequences of that limita-
tion?” The answer will differ according to whether our concern is with
practical or theoretical consequences. Practically, ingenious design com-
bined with testing may do much to extend the range of useful machine
behavior. Theoretically, understanding the limits of machine behavior
challenges our understanding of the resources of human action. Just as
the project of building intelligent artifacts has been enlisted in the ser-
vice of a theory of mind, the attempt to build interactive artifacts, taken
seriously, could contribute much to an account of situated human action
and shared understanding.
12 For an illuminating treatment of the relation of maps to territories, see Turnbull (1993).
13 This phrase is echoed in Dourish’s (2001) syncretic review of revisions to cognitivist
thinking about action in the computer and information sciences.
14 This refers, of course, to those “programs of action” that are inscribed in the machine’s
design:thelatterbynomeanslimittherangeofpossibleappropriationsfortechnologies
in use (Akrich 1992; Latour 1992; Woolgar 1991). The limits to designers’ conﬁguration
of the possibilities for technologies in use result not simply in user “misunderstanding”
but in a wide range of creative appropriations, which have since been explored through
a large, and still growing, body of work in social studies of technology (for a recent
collection see Oudshoorn and Pinch 2003).


