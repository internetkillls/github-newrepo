# Human–Machine Reconfigurations: Plans and Situated Actions

Source ID: A06
Authors: Lucy A. Suchman
Original attachment: Human-Machine Reconfigurations_ Plans and Situated Actions, Lucy A Suchman.pdf
Identity: Cambridge University Press, 2nd edition, 2007.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 41

Preface to the 1st Edition
27
actions, in favor of those aspects of the actions that can be seen to accord
with the plan.
This third implication, it seems, is not just a symmetric alternative to
the other two but is different in kind and somewhat more serious. That
is, it calls into question not just the adequacy of our distinctions along the
dimensions of culture, kinds of activity, or degrees of expertise, but the
very productivity of our starting premises that representations of action
such as plans could be the basis for an account of actions in particular
situations. Because the third implication has to do with foundations,
and not because there is no truth in the other two, I take the idea that
actions are primarily situated and that situated actions are essentially
ad hoc as the starting point for my investigations.4
The view of action exempliﬁed by the European navigator is now
being reiﬁed in the design of intelligent machines. In this book I examine
one such machine, as a way of uncovering the strengths and limitations
of the general view that its design embodies. The view, that purposeful
action is determined by plans, is deeply rooted in the Western human
sciences as the correct model of the rational actor. The logical form of
plans makes them attractive for the purpose of constructing a compu-
tational model of action, to the extent that for those ﬁelds devoted to
what is now called cognitive science, the analysis and synthesis of plans
effectively constitute the study of action. My own contention, however,
is that as students of human action we ignore the Trukese navigator at
our peril. Although an account of how the European navigates may be
in hand, the essential nature of action, however planned or unplanned,
is situated. It behooves us, therefore, to study and to begin to ﬁnd ways
to describe the “Trukese” system.
There is an injunction in social studies of science to eschew interest
in the validity of the products of science in favor of an interest in their
4 I see my choice of the term ad hoc here as an unfortunate one, particularly in light of
subsequent readings of the text. The problem lies in the term’s common connotations of
things done anew, or narrowly, without reference to historically constituted or broader
concerns. Perhaps a better way of phrasing this would be to say that situated actions are
always, and irremediably, contingent on speciﬁc, unfolding circumstances that are them-
selves substantially constituted through those same actions. This is the case however
much actions may also be informed by prescriptive representations, past experience,
future considerations, received identities, entrenched social relations, established pro-
cedures, built environments, material contraints, and the like. To be rendered effective
the signiﬁcance and relevance of any of those must be reiterated, or transformed, in rela-
tion to what is happening just here and just now. For a brilliant and generative proposal
for what he names a “science of singularity,” see de Certeau (1988).


## PDF page 42

28
Human–Machine Reconﬁgurations
production.5 Although I generally agree with this injunction, my inves-
tigation of one of the prevailing models of human action in cognitive
science is admittedly and unabashedly interested. That is to say, I take
it that there is a reality of human action, beyond either the cognitive
scientist’s models or my own accounts, to which both are trying to do
justice. In that sense, I am examining the cognitive science model not
just with the dispassion of the uncommitted anthropologist of science
but also in light of an alternative account of human action to which I am
committed and that I attempt to clarify in the process.
5 I would now take this to be an oversimpliﬁcation of the so-called principle of sym-
metry in science studies, which argues that rather than take positions deemed “true”
at a particular moment as explicable by nature, and only those considered “false” as
amenable to social analysis, all scientiﬁc positions should be analyzable in the same
terms. Those terms now increasingly involve attempts to come to grips with the simul-
taneously social/cultural and material/natural constitution of scientiﬁc practices and
attendant knowledges.


## PDF page 43

3
Introduction to the 1st Edition
The famous anthropological absorption with the (to us) exotic . . . is, thus,
essentially a device for displacing the dulling sense of familiarity with
which the mysteriousness of our own ability to relate perceptively to one
another is concealed from us.
(Geertz 1973: 14)
The problem of shared understanding, or mutual intelligibility, has
deﬁned the ﬁeld of social studies for the past hundred years. On the one
hand, interpreting the actions of others has been the social scientist’s
task; to come up with accounts of the signiﬁcance of human actions is,
afterall,theprincipalchargeofethnographicanthropology.Ontheother
hand, to understand the mutual intelligibility of action as a mundane,
practical accomplishment of members of the society is, in large mea-
sure, the social scientist’s problem or subject matter. An account of that
accomplishment would constitute an account of the foundation of social
order. Although studies of mutual intelligibility have been concerned
exclusively with human action, we now have a technology that has
brought with it the idea that rather than just using machines, we interact
with them as well.1 Already, the notion of “human–machine interaction”
pervades both technical and popular discussion of computers, whether
about their design or their use. In the debate over speciﬁc problems
in the design and use of interactive machines, however, no question is
1 Although meant to set up the contrast with machines, this statement regrettably ignores
the long-standing and still lively ﬁeld of ethology (see, for example, Crist 2000, 2004).
It would be more accurate to say that the social sciences have been concerned with
interactions between and among animal species.
29


## PDF page 44

30
Human–Machine Reconﬁgurations
raised about the bases for the very idea of human–machine interaction
as such. And recent developments in the social sciences regarding the
foundations of human interaction have had remarkably little inﬂuence
on the discussion of interactive machines.2
The following chapters examine the conception of purposeful action,
and consequently of interaction, informing the design of interactive
machines. My central concern in the investigation is a new manifesta-
tion of an old problem in the study of mutual intelligibility; namely, the
relation between observable behavior and the processes, not available to
direct observation, that make behavior meaningful. For psychological
studies, the crucial processes are essentially cognitive, located inside the
head of the actor, and include the formation and effect of beliefs, desires,
intentions, and the like. For social studies, the crucial processes are inter-
actional and circumstantial, located in the relationships among actors
and between actors and their embedding situations. In either case, the
problem of meaningful action turns on the observation that behavior is
inherently subject to indeﬁnitely many ascriptions of meaning or intent,
while meaning and intent are expressible through an indeﬁnite number
of possible behaviors. Whether the ﬁnal arbiter of action’s signiﬁcance
is taken to be private psychological processes or accountability to the
public world, the question to be resolved – what constitutes purposeful
action and how is it understood – is the same.
The new manifestation of this question concerning the nature of pur-
poseful action and its interpretation arises in research on machine intelli-
gence. Theoretically, the goal of that research is a computational model
of intelligent behavior that not only, given some input, produces the
right output behavior but also that does so by simulating human cog-
nitive processes. Practically, the goal is just a machine that, given some
input, produces behavior that is useful and appropriate to the situation
at hand.3 In either case, insofar as rightness or appropriateness of behav-
ior means that behavior is accountably rational in the eyes of an other,
the measure of success is at bottom an interactional one.
For the moment at least, the question of theoretical versus practical
criteria of adequacy for machine intelligence is rendered moot by the
2 There has been some signiﬁcant engagement in the years since; see, for example, the
articles collected in Luff, Gilbert, and Frohlich (1990); Thomas (1995). Despite these
interventions, however, I would maintain that there is remarkably little substantive
effect on discourses and practices of the so-called conversational machine.
3 What I characterize as a theoretical/practical distinction here maps on to some versions
of what have been distinguished as “strong” versus “weak” AI.


## PDF page 45

Introduction to the 1st Edition
31
problems involved in constructing a device that even appears to behave
in ways that are purposeful or intelligent, at least outside of the most
highly constrained domains. It may simply turn out that the resistance
of meaningful action to simulation in the absence of any deep under-
standing will defend us against false impressions of theoretical success.
In any case, my purpose here is not to resolve the question of whether
artiﬁcial intelligence is possible but rather to clarify some existing trou-
bles in the project of constructing intelligent, interactive machines, as
a way of contributing to our understanding of human intelligence and
interaction.
Every human tool relies on, and materializes, some underlying con-
ception of the activity that it is designed to support. As a consequence,
one way to view the artifact is as a test on the limits of the underlying
conception. In this book I examine an artifact built on a planning model
of human action. The model treats a plan as something located in the
actor’s head, which directs his or her behavior. In contrast, I argue that
artifacts built on the planning model confuse plans with situated actions
and recommend instead a view of plans as formulations of antecedent
conditions and consequences of action that account for action in a plau-
sible way. Stated in advance plans are necessarily vague, insofar as they
are designed to accommodate the unforeseeable contingencies of actual
situations of action. As ways of talking about action, plans as such
neither determine the actual course of situated action nor adequately
reconstruct it.4 Although for purposes of practical action this limitation
on plans is irrelevant, for purposes of a science of practical action it is
crucial.5 Speciﬁcally, if we are interested in situated action itself we need
to look at how it is that actors use the resources that a particular occasion
provides (including, but crucially not reducible to, formulations such as
plans) to construct their action’s developing purpose and intelligibility.
Beginning with a view of interaction or communication (I use the
two terms interchangeably) as the mutual intelligibility of action, I
4 The sense of “adequacy” implied here is an anthropological/sociological one; that is,
plans cannot be taken as speciﬁc, or comprehensive, or experiential descriptions of
how some course of action went. For practical purposes of everyday talk, of course, an
account of actions taken with reference to a plan (for example, the itinerary of a journey)
may be quite sufﬁcient.
5 The notion of a “science of practical action” sits uncomfortably with my current appre-
ciation for the connotations of universality and generality implied. I would say instead
that we cannot simply take plans as isomorphic with actions if our interest is in recov-
ering the latter’s enactment in situ.


## PDF page 46

32
Human–Machine Reconﬁgurations
investigate the grounds for beginning to speak of interaction between
humans and machines. Chapter 4 introduces the notion of interactive
artifacts and its basis in certain properties of computing machines.6
Chapter 5 examines the view of plans as the basis for action and
communication held by designers of artiﬁcially intelligent, interactive
machines, while Chapters 6 and 7 present an alternative view of action
and communication as situated, drawn from recent developments in
social science. Finally, Chapters 8 and 9 offer an analysis of encoun-
ters between novice users of a machine and a computer-based system
intended to be intelligent and interactive. The aim of the case study is
not to criticize the particular design but to view the design as reifying
certain premises about purposeful action.7 The task is to articulate those
premises, to see how they succeed as a basis for human–machine com-
munication and how they fail, and to explore the implications of their
success and failure both for the design of human–machine communi-
cation and for the broader explication of purposeful action and mutual
intelligibility.
6 Chapter numbers have been changed to reﬂect the current text.
7 The term reifying in this context seems overly ﬁxed and might be better replaced with
incorporating or materializing.


## PDF page 47

4
Interactive Artifacts
Marginal objects, objects with no clear place, play important roles. On the
lines between categories, they draw attention to how we have drawn the
lines. Sometimes in doing so they incite us to reafﬁrm the lines, sometimes
to call them into question, stimulating different distinctions.
(Turkle 1984: 31)
In The Second Self (1984), Sherry Turkle describes the computer as an
evocative object, one that raises new questions regarding our com-
mon sense of the distinction between artifacts and intelligent others.
Her studies include an examination of the impact of computer-based
artifacts on children’s conceptions of the difference between categories
such as “alive” versus “not alive” and “machine” versus “person.” In
dealing with the questions that computer-based objects evoke, children
make clear that the differentiation of physical from psychological enti-
ties, which as adults we largely take for granted, is the end product
of a process of establishing the relationship between the observable
behavior of a thing and its underlying nature.1 Children have a ten-
dency, for example, to attribute life to physical objects on the basis of
behaviors such as autonomous motion or reactivity, though they reserve
humanity for entities evidencing such things as emotion, speech, and
apparent thought or purposefulness. Turkle’s observation with respect
to computational artifacts is that children ascribe to them an “almost
aliveness” and a psychology, while maintaining their distinctness from
1 Though see Carey (1985, Chapter 1) for a critique of the Piagetian notion that chil-
dren at ﬁrst have no concept for mechanical causation apart from intentional causation.
(Original footnote.)
33


## PDF page 48

34
Human–Machine Reconﬁgurations
human beings: a view that, as Turkle points out, is remarkable among
other things for its correspondence to the views held by those who are
the artifacts’ designers.2
In this book I take as a point of departure a particular aspect of the
phenomenon that Turkle identiﬁes: namely, the apparent challenge that
computational artifacts pose to the long-standing distinction between
the physical and the social, in the special sense of those things that one
designs, builds, and uses, on the one hand, and those things with which
one communicates, on the other. Although this distinction has been
relatively nonproblematic to date, now for the ﬁrst time the term inter-
action, in a sense previously reserved for describing a uniquely interper-
sonalactivity,seemsappropriately tocharacterize whatgoeson between
people and certain machines as well.3 Interaction between people and
machines implies mutual intelligibility or shared understanding. What
motivates my inquiry, therefore, is not only the recent question of how
there could be mutual intelligibility between people and machines but
also the prior question of how we account for the shared understanding
or mutual intelligibility that we experience as people in our interactions
with others whose essential sameness is not in question. An answer to
the more recent question, theoretically at least, presupposes an answer
to the earlier one.
In this chapter I relate the idea of human–machine communication to
some distinctive properties of computational artifacts and to the emer-
gence of disciplines dedicated to making those artifacts intelligent. I
begin with a brief discussion of cognitive science, the interdisciplinary
ﬁeld devoted to modeling cognitive processes, and its role in the project
2 See especially pp. 62–3; Turkle ﬁnds some cause for alarm in the fact that for chil-
dren the distinction of machine and person seems to turn centrally on a separation of
thought from feeling; that is, computers exhibit the former but lack the latter. This view,
she argues, includes a kind of dissociation of intellect and emotion, and consequent
trivialization of both, that characterizes the attitudes of many in the ﬁeld of artiﬁcial
intelligence. (Original footnote.)
3 Actually, the term interaction has its origins in the physical sciences to describe a recipro-
cal action or inﬂuence. I use it here in the common sense assigned to it by social science:
namely, to mean communication between persons. The migration of the term from the
physical sciences to the social, and now back to some ground that stands between them,
relates in intriguing ways to a general blurring of the distinction between physical and
social in modern science and to the general question of whether machines are actually
becoming more like people or whether, in fact, people are coming to deﬁne themselves
more as machines. There is clearly a mutual inﬂuence at work. For more on this last
point, see Dreyfus 1979 (Chapter 9). (Original footnote.)


