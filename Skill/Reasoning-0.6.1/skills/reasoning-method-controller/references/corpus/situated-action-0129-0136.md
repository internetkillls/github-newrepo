# Human–Machine Reconfigurations: Plans and Situated Actions

Source ID: A06
Authors: Lucy A. Suchman
Original attachment: Human-Machine Reconfigurations_ Plans and Situated Actions, Lucy A Suchman.pdf
Identity: Cambridge University Press, 2nd edition, 2007.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 129

Case and Methods
115
nonlinguistic resources to the use of language (for a “taxonomy” of
these resources, see Rubin 1980).
In an analysis of transcripts of instructors communicating with an
apprentice through face-to-face, telephone, audio-taped, and written
media about the assembly of a toy water pump, Burke (1982) found that
the most obvious difference, that between speaking and writing, is actu-
ally less crucial than the difference between interactive (e.g., a keyboard)
and noninteractive (e.g., audio-taped) instruction. The restrictions gen-
erally associated with written instruction, in other words, derive not
from the writing so much as from the absence of interaction, whereas the
effectiveness of verbal instruction derives less from the speech than from
the interaction that is generally associated with it. Ochs (1979) relates the
distinction of interactive and noninteractive communication to degrees
of planning, arguing that in the case of interaction speakers plan only
at a general level (the concretization of the plan being contingent and
emergent), whereas noninteractive discourse can be entirely planned in
advance. Instead, Burke takes the point of view that the instructor’s task
is one of adequate description rather than planning and reports that in
the noninteractive modalities of instruction on the assembly task there
is a tendency to “overelaborate” descriptions, in an apparent attempt to
anticipate possible troubles and to compensate for the lack of opportuni-
ties for their on-site clariﬁcation. In face-to-face instruction, in contrast,
Burke found that instructors initially provided minimal descriptions
and then monitored the apprentice’s actions for evidence of the descrip-
tion’s adequacy or inadequacy. By telephone, where visual access was
unavailable but where the interaction remained, the resources for mon-
itoring the actions of the apprentice changed from visual to verbal (e.g.,
afﬁrmations, repeats, and transformed repeats of the instructions by the
apprentice), but the monitoring again guided the description.
Cohen’s (n.d.) analysis of transcripts of instructor and apprentice
communicating by telephone or keyboard on the same assembly task
conﬁrms the ability of instructors to adjust the level of their descriptions
in response to the demonstrated understanding or misunderstanding by
the apprentice. He concludes that the principal difference between spo-
ken and written interactive media is that experts in spoken instruction
more often explicitly request that the novice identify an object, and often
question the novice on his or her success, whereas experts using key-
boards subsume reference to objects into instructions for action unless
some prior referential miscommunication has occurred (ibid.: 21). Spo-
ken interaction between expert and novice, in that sense, is more ﬁnely


## PDF page 130

116
Human–Machine Reconﬁgurations
calibrated than written, though insofar as both are interactive both sup-
port the collaborative construction of a useful description of the objects
and actions in question, through practical analyses of the communica-
tion’s success at each turn.
the basic interaction
The aim of the expert help system analyzed in the next chapter is to use
the power of the computer to combine the portability of noninteractive
instructions with the timeliness, relevance, and effectiveness of inter-
action. The machine presents the user with a series of video displays.
Each display presented to the user either describes the machine’s behav-
ior or provides the user with some next instructions. In the latter case,
the ﬁnal instruction of each display prescribes an action whose effect is
detectable by the system, thereby triggering a change to the next display
(Figure 8.1).
Through the device of display changes keyed to actions by the user,
the design accomplishes a simple form of occasioned response, in spite
of the fact that only a partial trace of the user’s behavior is available to
the system. Among those user actions that are not available to the system
is the actual work of locating referents and interpreting action descrip-
tions: the system has access only to the product of that work. More-
over, within the instruction provided by a given display are embedded
instructions for actions whose effects are not detectable by the system. To
anticipate our discussion of troubles that arise, if one of these instructions
is misconstrued, the error will go by unnoticed. Because the implication
of a next display is that prior actions have been noted and that they have
1. MACHINE PRESENTS INSTRUCTION
User reads instruction
interprets referents
and action descriptions
2. USER TAKES ACTION
Design assumes
that the user has understood
the instruction
3. MACHINE PRESENTS NEXT INSTRUCTION
ﬁgure 8.1. The basic instructional sequence.


## PDF page 131

Case and Methods
117
been found adequate, the appearance of a next instruction will conﬁrm
the correctness not only of the prior action narrowly deﬁned but also of
all of the embedded actions prescribed by the last instruction.
To compensate for the machine’s limited access to the user’s actions,
the design relies on a partial enforcement of the order of user actions
within the procedural sequence. This strategy works fairly wells inso-
far as a particular effect produced by the user (such as closing a cover
on the copier) can be taken to imply that a certain condition obtains (a
document has been placed in the machine for copying), which, in turn,
implies a machine response (the initiation of the printing process). In
this sense, the order of user and machine “turns,” and what is to be
accomplished in each, are predetermined. The system’s “recognition”
of turn-transition places is essentially reactive; that is, there is a deter-
minate relationship between certain actions by the user, read as changes
to the state of the machine, and the machine’s transition to a next dis-
play. By establishing a determinate relationship between detectable user
actions and machine responses, the design unilaterally administers con-
trol over the interaction, but in a way that is conditional on the actions
of the user.
At the same time that the system controls the sequence of user actions,
the design avoids certain problems that arise when instructions are pro-
vided consecutively and in a strict order. Every procedure is represented
in the system as a series of steps, each of which has an associated precon-
dition (the effect of a prior action by user or machine) and an associated
machine response (display of instructions and/or setting of machine
state). Rather than proceeding through these steps consecutively, the
system begins processing at the last step of the procedure and checks
to see whether that step has been completed. If not, the preconditions
are checked and, if they are all satisﬁed, the step is executed. Each pre-
condition carries with it a reference to the earlier step in the procedure
that will satisfy that precondition, so that if an unmet precondition is
found the system will return to the earlier step and proceed from there.
If, therefore, a procedure is repeated but in the second instance certain
conditions hold over from the ﬁrst, the system will not display instruc-
tions for the actions that have already been taken. Beginning with the
ﬁnal step, it will work backwards through the procedure just to the point
where an unmet precondition is found and will provide the instruction
from that point on. Similarly, if the user takes an action that undoes a
condition satisﬁed earlier, the system will encounter that state again at
the next check. This technique produces appropriate instructions not


## PDF page 132

118
Human–Machine Reconﬁgurations
because the system knows that this time through differs from the last,
but just because, regardless of how they come about, certain detectable
conditions (e.g., a document is in the machine) are linked unequivocally
to appropriate response (e.g., initiating the printing process). Chap-
ter 9 examines how this design strategy works and how, for the very
same reason that it works in some instances, in other instances troubles
arise.
methods
The study was directed by two methodological commitments, one gen-
eral, and the other particular to the problem at hand. Generally, the study
began with a commitment to an empirical approach, along with the
conviction that situated action cannot be captured empirically through
either examples constructed by the researcher, paper-and-pencil obser-
vations, or interview reports. Analyses of contrived examples, observa-
tions, or interviews all rest on accounts of circumstances that are either
imagined or recollected. One objective in studying situated action is
to consider just those ﬂeeting circumstances that our interpretations of
action systematically rely on, but which our accounts of action routinely
ignore. A second objective is to make the relation between interpreta-
tions of action and action’s circumstances our subject matter. Both objec-
tives are clearly lost if we use reports of action as our data.4
4 This is not to say that paper-and-pencil observations have no place. The video analysis
was preceded by approximately twenty hours of observation of new users of the same
machine, minus the expert help system but equipped with written instructions, in actual
ofﬁce settings. That earlier study was undertaken in response to an unelaborated report,
from those who supported the machine and its users “in the ﬁeld,” of user complaints
that the machine was too complicated. Given the relative simplicity of even the most
complex photocopier, this complaint on face value was puzzling, particularly to the
machine’s designers. The combination of the vagueness of the complaint as reported,
and the bewilderment of the designers, intrigued both me and my colleagues Austin
Henderson and Richard Fikes at the research center, and we set about to try to ascertain
what the “complexity” was really about. That led to the paper-and-pencil observations,
which convinced us that indeed the machine was somehow too complicated for the
novice user who had no previous training; that is, people trying to use the machine
were very visibly confused. The methodological problem at that point was that I, as
an observer of their troubles, was equally confused. From the observations, therefore,
I learned two important lessons. First, that there was indeed a problem. And, second,
that to understand the problem would require the use of an adequate, i.e., a videotaped,
record. For an analysis of users’ troubles with the original instruction set, see Suchman
(1982). (Original footnote.)


## PDF page 133

Case and Methods
119
Another approach to the analysis of instructions might be to look at
the textual cogency of the instructions themselves. An example offered
by Searle (1979) illustrates the problem with such a strategy:5
Suppose a man goes to the supermarket with a shopping list given him by his
wife on which are written the words “beans, butter, bacon, and bread.” Suppose
as he goes around with his shopping cart selecting these items, he is followed by
a detective who writes down everything he takes. As they emerge from the store
both the shopper and detective will have identical lists. But the function of the
two lists will be quite different. In the case of the shopper’s list, the purpose of
the list is, so to speak, to get the world to match the words; the man is supposed
to make his actions ﬁt the list. In the case of the detective, the purpose of the
list is to make the words match the world; the man is supposed to make the list
ﬁt the actions of the shopper. This can be further demonstrated by observing
the role of “mistake” in the two cases. If the detective goes home and suddenly
realizes that the man bought pork chops instead of bacon, he can simply erase
the word “bacon” and write “pork chops.” But if the shopper gets home and
his wife points out that he has bought pork chops when he should have bought
bacon he cannot correct the mistake by erasing “bacon” from the list and writing
“pork chops.” (ibid.: 4)
The subject of the present analysis, the user of the expert help system,
is in the position of the shopper with respect to the instructions that the
system provides; that is, she must make her actions match the words. But
in what sense? Like the instructions, a shopping list may be consulted to
decide what to do next or to know when the shopping is done, may be
cited after the fact to explain why things were done the way they were,
and so forth. But also like the instructions, the list does not actually
describe the practical activity of shopping (how to ﬁnd things, which
aisles to go down in what order, how to decide between competing
brands, etc.); it simply says how that activity is to turn out.6
Just as the list of the shopping’s outcomes does not actually describe
the organization of the activity of shopping, an analysis of instructions
will not yield an analysis of the activity of carrying them out. In fact,
contrary to the case in the story, there is no reason to believe that if a
person has a set of instructions for operating a machine and we generate
a description of the activity of operating a machine from watching the
5 Searle credits this example to Anscombe (1957). The point that Searle is interested in
concerns the notion of “direction of ﬁt” between words and the world. (Original foot-
note.)
6 For an inspired ethnographic account of actual practices of shopping, with a particular
focus on practical forms of quantitative reasoning see Lave (1988, Chapter 7).


## PDF page 134

120
Human–Machine Reconﬁgurations
person, that the description we generate should look anything like the
instructions. In fact, if our description of the situated activity does mirror
the structure of the instructions, there is reason to believe that something
is amiss.
Unlike the detective in the story who is supposed to generate a list,
our problem as students of situated action is more akin to the problem
of a detective who is just sent out and told to report back on what
going to the grocery store is all about and how shopping is done. What
that description should look like – what its terms should be, what its
structure should be, what of all that goes on it should report – is an open
methodological question. If, to put some constraints on the description,
we set out with a template that asks for a list just of what the actions come
to, then what counts as “an action” is prescribed ahead of time as “its
outcome,” and the list format prescribes the structure of the description.
Only that part of the activity that ﬁlls in the template will be recorded.
The action’s structure, in other words, will be decided in advance and
the method employed by the scientist will ensure that that structure is
what is found.
One further issue that the story touches on is the problem of validity.
The story says the detective might “suddenly realize” that there is some
error in his description. But how might he actually realize that? If we
just look for a discrepancy between the shopper’s list and the detective’s,
what we ﬁnd might reﬂect either an error in the shopper’s activity (it
doesn’tmatchthelist)orinthedescription(itdoesn’tmatchtheactivity).
Toevaluatewhich,wemusthave(a)independentaccesstotheshopper’s
list to compare against the activity and (b) a record of activity. That is
to say, two essential methodological resources are (a) the comparison of
our own interpretations with those of our subjects and (b) a record that
is not contingent on either.
However adequate the record, of course, the empirical basis of social
studies is not a positive one because we cannot, by deﬁnition, provide
a literal description of our phenomenon.7 As Wilson (1970) deﬁnes lit-
eral description: “Any description of a phenomenon is based on per-
ceived features that the phenomenon displays to the observer. A literal
7 Galaty (1981) makes a useful distinction between “data sources,” as the business of the
social world independent of the anthropologist’s interest in it; “data,” as the anthropo-
logically [worked-up] information that appears in the form of, for example, transcripts;
and “analytic objects,” conceptualized as events, troubles, and the like (ibid.: 91, note 2).
The point is that for the social scientist, the data are interpreted already at their source.
(Original footnote.)


## PDF page 135

Case and Methods
121
description, then, amounts to asserting that on the basis of those fea-
tures the phenomenon has some clearly designated property, or what is
logically the same thing, belongs to some particular, well-deﬁned class
of phenomena” (ibid.: 72). For a description to be literal, in other words,
the class of phenomena of which the described is an instance must be
deﬁnable in terms of sufﬁcient conditions for counting some instance as
a member of the class. For situated action, that would require classiﬁ-
cation of action not only as the relation of intent to behavior but also as
the relation of both to mitigating circumstances – a classiﬁcation that, I
argued in Chapter 5, is functionally and criterially different from that
applied to intentional descriptions of actions and situations. Moreover,
the social scientist’s description is yet another order of remove from a
literal description if the subject of the descriptions is not only the intent
of some actor, but also the interpretations of that actor’s intent by others
on the scene. Judgments of correctness and veridicality are replaced in
social studies by judgments of adequacy or verisimilarity (Heap 1980:
104), the latter resting on criteria of evidence and warranted inference
rather than conditions of truth.
The problems that the social scientist struggles with in deﬁning her
methods are the same problem that, from another view, constitute her
subject matter: namely, the uncertain relation between accounts of the
signiﬁcance of action and the observations and inferences on which
those accounts must be based. There is no privileged analytic stance
for the social scientist that exempts her from the problems of adju-
dicating the practical objectivity of the social world. The only advan-
tage that accrues to the researcher (a substantial one, it turns out) is
recourse to a record of the action and its circumstances, independent
of her analysis. The availability of audiovisual technology that can pro-
vide such a record, for repeated inspection by the researcher and by col-
leagues, avoids the reliance on unexplicated resources that characterizes
traditional ethnographic accounts. In traditional accounts, the ﬂeeting
nature of the events that the ethnographer describes means that the only
record that is available for inspection by others is the ethnographer’s
description.
This study proceeded, therefore, in a setting where video technology
could be used in a sort of uncontrolled experimentation. On one hand,
the situation was constructed so as to make certain issues observable;
speciﬁcally, the work of using the machine with the assistance of the
expert help system. The construction consisted in the selection of tasks
observed to pose problems for new users in “the real world.” On the


## PDF page 136

122
Human–Machine Reconﬁgurations
other hand, once given those tasks, the subjects were left entirely on their
own. In the analysis, by the same token, the goal was to construct a char-
acterization of the interaction that ensued rather than to apply a prede-
termined coding scheme. Both predetermined coding schemes and con-
trolled experiments presuppose a characterization of the phenomenon
studied, varying only certain parameters to test the characterization.
Application of that methodology to the problem of human–machine
interaction would be at the least premature. The point of departure for
the study was the assumption that we lack a description of the struc-
ture of situated action. And because the hunch is that the structure lies
in a relation between action and its circumstances that we have yet to
uncover, we do not want to presuppose what are the relevant conditions
or their relationship to the course of the action. We need to begin, there-
fore, with observations that capture as much of the phenomenon, and
presuppose as little, as possible.8
The consequence of this commitment to examining the circumstances
of action is that we need to begin with a record of events that is not
prejudged as to its analytic interest either in advance or in the mak-
ing. The data for this study, accordingly, are a corpus of videotapes of
ﬁrst-time users of the expert help system.9 First-time users were cho-
sen on the grounds that the system was intended by its designers to
be self-explanatory or usable by people with no previous introduction
to the machine. More generally, the troubles encountered by ﬁrst-time
users of a system are valuable in that they disclose work required to
understand the system’s behavior that, for various reasons, is masked
by the proﬁcient user. This disclosure of the requisite work is the value
of studying interactional troubles generally (see Gumperz 1982b: 308)
and distinguishes this analysis from the usual “operability tests.” That
is to say, I am not simply interested in distinguishing “correct” from
“erroneous” moves by the user. Rather, by studying what things look
like when they are unfamiliar and troublesome, I hope to understand
better what is involved in their mastery.
In each of the sessions two people, neither of whom had ever used the
systembefore,workedtogetherinpairs.Twopeopleaskedtocollaborate
8 I would phrase this characterization of the implications of the contingency of situated
activity for research methods more strongly now, as recommending against the project
of establishing a “structure” altogether. On the premises of poststructural social studies
and their implications for method, see, for example, Lynch 1993; Law 2004.
9 The corpus from which the analysis of Chapter 9 is drawn comprises four sessions, each
lasting from one and a half to two hours.


