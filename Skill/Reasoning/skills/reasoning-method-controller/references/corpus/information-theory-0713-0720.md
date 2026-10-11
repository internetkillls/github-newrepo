# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 713

HISTORICAL NOTES
687
17.2
Fan’s inequality [200] for ratios of determinants.
For all 1 ≤p ≤
n, for a positive deﬁnite K = K(1, 2, . . . , n), show that
|K|
|K(p + 1, p + 2, . . . , n)| ≤
p

i=1
|K(i, p + 1, p + 2, . . . , n)|
|K(p + 1, p + 2, . . . , n)| .
(17.157)
17.3
Convexity of determinant ratios.
For positive deﬁnite matrices K,
K0, show that ln(|K + K0|/|K|) is convex in K.
17.4
Data-processing inequality.
Let random variable X1, X2, X3, and
X4 form a Markov chain X1 →X2 →X3 →X4. Show that
I (X1; X3) + I (X2; X4) ≤I (X1; X4) + I (X2; X3).
(17.158)
17.5
Markov chains.
Let random variables X, Y, Z, and W form a
Markov chain so that X →Y →(Z, W) [i.e., p(x, y, z, w) =
p(x)p(y|x)p(z, w|y)]. Show that
I (X; Z) + I (X; W) ≤I (X; Y) + I (Z; W).
(17.159)
HISTORICAL NOTES
The entropy power inequality was stated by Shannon [472]; the ﬁrst for-
mal proofs are due to Stam [505] and Blachman [61]. The uniﬁed proof
of the entropy power and Brunn–Minkowski inequalities is in Dembo
et al.[164].
Most of the matrix inequalities in this chapter were derived using
information-theoretic methods by Cover and Thomas [118]. Some of the
subset inequalities for entropy rates may be found in Han [270].


## PDF page 714



## PDF page 715

BIBLIOGRAPHY
[1] J. Abrahams.
Code and parse trees for lossless source encoding.
Proc.
Compression and Complexity of Sequences 1997, pages 145–171, 1998.
[2] N. Abramson. The ALOHA system—another alternative for computer com-
munications. AFIPS Conf. Proc., pages 281–285, 1970.
[3] N. M. Abramson. Information Theory and Coding. McGraw-Hill, New York,
1963.
[4] Y. S. Abu-Mostafa. Information theory. Complexity, pages 25–28, Nov.
1989.
[5] R. L. Adler, D. Coppersmith, and M. Hassner. Algorithms for sliding block
codes: an application of symbolic dynamics to information theory. IEEE
Trans. Inf. Theory, IT-29(1):5–22, 1983.
[6] R. Ahlswede. The capacity of a channel with arbitrary varying Gaussian
channel probability functions. Trans. 6th Prague Conf. Inf. Theory, pages
13–21, Sept. 1971.
[7] R. Ahlswede.
Multi-way communication channels.
In Proc. 2nd Int.
Symp. Inf. Theory (Tsahkadsor, Armenian S.S.R.), pages 23–52. Hungarian
Academy of Sciences, Budapest, 1971.
[8] R. Ahlswede. The capacity region of a channel with two senders and two
receivers. Ann. Prob., 2:805–814, 1974.
[9] R. Ahlswede.
Elimination of correlation in random codes for arbitrarily
varying channels.
Z. Wahrscheinlichkeitstheorie und verwandte Gebiete,
33:159–175, 1978.
[10] R. Ahlswede. Coloring hypergraphs: A new approach to multiuser source
coding. J. Comb. Inf. Syst. Sci., pages 220–268, 1979.
[11] R. Ahlswede. A method of coding and an application to arbitrarily varying
channels. J. Comb. Inf. Syst. Sci., pages 10–35, 1980.
[12] R. Ahlswede and T. S. Han. On source coding with side information via
a multiple access channel and related problems in multi-user information
theory. IEEE Trans. Inf. Theory, IT-29:396–412, 1983.
Elements of Information Theory, Second Edition,
By Thomas M. Cover and Joy A. Thomas
Copyright 2006 John Wiley & Sons, Inc.
689


## PDF page 716

690
BIBLIOGRAPHY
[13] R. Ahlswede and J. K¨orner.
Source coding with side information and a
converse for the degraded broadcast channel.
IEEE Trans. Inf. Theory,
IT-21:629–637, 1975.
[14] R. F. Ahlswede. Arbitrarily varying channels with states sequence known
to the sender. IEEE Trans. Inf. Theory, pages 621–629, Sept. 1986.
[15] R. F. Ahlswede. The maximal error capacity of arbitrarily varying channels
for constant list sizes (corresp.). IEEE Trans. Inf. Theory, pages 1416–1417,
July 1993.
[16] R. F. Ahlswede and G. Dueck. Identiﬁcation in the presence of feedback: a
discovery of new capacity formulas. IEEE Trans. Inf. Theory, pages 30–36,
Jan. 1989.
[17] R. F. Ahlswede and G. Dueck. Identiﬁcation via channels. IEEE Trans. Inf.
Theory, pages 15–29, Jan. 1989.
[18] R. F. Ahlswede, E. H. Yang, and Z. Zhang. Identiﬁcation via compressed
data. IEEE Trans. Inf. Theory, pages 48–70, Jan. 1997.
[19] H. Akaike. Information theory and an extension of the maximum likelihood
principle. Proc. 2nd Int. Symp. Inf. Theory, pages 267–281, 1973.
[20] P. Algoet and T. M. Cover.
A sandwich proof of the Shannon–
McMillan–Breiman theorem. Ann. Prob., 16(2):899–909, 1988.
[21] P. Algoet and T. M. Cover. Asymptotic optimality and asymptotic equipar-
tition property of log-optimal investment. Ann. Prob., 16(2):876–898, 1988.
[22] S. Amari. Differential-Geometrical Methods in Statistics. Springer-Verlag,
New York, 1985.
[23] S. I. Amari and H. Nagaoka. Methods of Information Geometry. Oxford
University Press, Oxford, 1999.
[24] V. Anantharam and S. Verdu. Bits through queues. IEEE Trans. Inf. Theory,
pages 4–18, Jan. 1996.
[25] S. Arimoto. An algorithm for calculating the capacity of an arbitrary discrete
memoryless channel. IEEE Trans. Inf. Theory, IT-18:14–20, 1972.
[26] S. Arimoto. On the converse to the coding theorem for discrete memoryless
channels. IEEE Trans. Inf. Theory, IT-19:357–359, 1973.
[27] R. B. Ash. Information Theory. Interscience, New York, 1965.
[28] J. Acz´el and Z. Dar´oczy. On Measures of Information and Their Character-
ization. Academic Press, New York, 1975.
[29] L. R. Bahl, J. Cocke, F. Jelinek, and J. Raviv. Optimal decoding of linear
codes for minimizing symbol error rate (corresp.). IEEE Trans. Inf. Theory,
pages 284–287, March 1974.
[30] A. Barron.
Entropy and the central limit theorem.
Ann. Prob., 14(1):
336–342, 1986.
[31] A. Barron and T. M. Cover. A bound on the ﬁnancial value of information.
IEEE Trans. Inf. Theory, IT-34:1097–1100, 1988.


## PDF page 717

BIBLIOGRAPHY
691
[32] A. Barron and T. M. Cover. Minimum complexity density estimation. IEEE
Trans. Inf. Theory, 37(4):1034–1054, July 1991.
[33] A. R. Barron. Logically smooth density estimation. Ph.D. thesis, Department
of Electrical Engineering, Stanford University, Stanford, CA, 1985.
[34] A. R. Barron. The strong ergodic theorem for densities: generalized Shan-
non–McMillan–Breiman theorem. Ann. Prob., 13:1292–1303, 1985.
[35] A. R. Barron. Are Bayes’ rules consistent in information? Prob. Commun.
Computation, pages 85–91, 1987.
[36] A. R. Barron, J. Rissanen, and Bin Yu. The minimum description length prin-
ciple in coding and modeling. IEEE Trans. Inf. Theory, pages 2743–2760,
Oct. 1998.
[37] E. B. Baum.
Neural net algorithms that learn in polynomial time from
examples and queries. IEEE Trans. Neural Networks, pages 5–19, 1991.
[38] W. Beckner. Inequalities in Fourier analysis. Ann. Math., 102:159–182,
1975.
[39] R. Bell and T. M. Cover. Competitive optimality of logarithmic investment.
Math. Oper. Res., 5(2):161–166, May 1980.
[40] R. Bell and T. M. Cover. Game-theoretic optimal portfolios. Manage. Sci.,
34(6):724–733, 1988.
[41] T. C. Bell, J. G. Cleary, and I. H. Witten. Text Compression. Prentice-Hall,
Englewood Cliffs, NJ, 1990.
[42] R. Bellman. Notes on matrix theory. IV: An inequality due to Bergstrøm.
Am. Math. Monthly, 62:172–173, 1955.
[43] C. H. Bennett and G. Brassard. Quantum cryptography: public key distri-
bution and coin tossing. Proc. IEEE Int. Conf. Comput., pages 175–179,
1984.
[44] C. H. Bennett, D. P. DiVincenzo, J. Smolin, and W. K. Wootters. Mixed
state entanglement and quantum error correction.
Phys. Rev. A, pages
3824–3851, 1996.
[45] C. H. Bennett, D. P. DiVincenzo, and J. A. Smolin. Capacities of quantum
erasure channels. Phys. Rev. Lett., pages 3217–3220, 1997.
[46] C. H. Bennett and S. J. Wiesner. Communication via one- and two-particle
operators on Einstein–podolsky–Rosen states.
Phys. Rev. Lett., pages
2881–2884, 1992.
[47] C. H. Bennett.
Demons, engines and the second law.
Sci. Am.,
259(5):108–116, Nov. 1987.
[48] C. H. Bennett and R. Landauer. The fundamental physical limits of compu-
tation. Sci. Am., 255(1):48–56, July 1985.
[49] C. H. Bennett and P. W. Shor. Quantum information theory. IEEE Trans.
Inf. Theory, IT-44:2724–2742, Oct. 1998.
[50] J. Bentley, D. Sleator, R. Tarjan, and V. Wei.
Locally adaptive data
compression scheme. Commun. ACM, pages 320–330, 1986.


## PDF page 718

692
BIBLIOGRAPHY
[51] R. Benzel.
The capacity region of a class of discrete additive degraded
interference channels. IEEE Trans. Inf. Theory, IT-25:228–231, 1979.
[52] T. Berger.
Rate Distortion Theory: A Mathematical Basis for Data
Compression. Prentice-Hall, Englewood Cliffs, NJ, 1971.
[53] T. Berger. Multiterminal source coding. In G. Longo (Ed.), The Information
Theory Approach to Communications. Springer-Verlag, New York, 1977.
[54] T. Berger and R. W. Yeung. Multiterminal source encoding with one dis-
tortion criterion. IEEE Trans. Inf. Theory, IT-35:228–236, 1989.
[55] P. Bergmans. Random coding theorem for broadcast channels with degraded
components. IEEE Trans. Inf. Theory, IT-19:197–207, 1973.
[56] E. R. Berlekamp. Block Coding with Noiseless Feedback. Ph.D. thesis, MIT,
Cambridge, MA, 1964.
[57] C. Berrou, A. Glavieux, and P. Thitimajshima. Near Shannon limit error-
correcting coding and decoding: Turbo codes. Proc. 1993 Int. Conf. Com-
mun., pages 1064–1070, May 1993.
[58] D. Bertsekas and R. Gallager. Data Networks, 2nd ed.. Prentice-Hall, Engle-
wood Cliffs, NJ, 1992.
[59] M. Bierbaum and H. M. Wallmeier. A note on the capacity region of the
multiple access channel. IEEE Trans. Inf. Theory, IT-25:484, 1979.
[60] E. Biglieri, J. Proakis, and S. Shamai. Fading channels: information-theoretic
and communications aspects. IEEE Trans. Inf. Theory, pages 2619–2692,
October 1998.
[61] N. Blachman. The convolution inequality for entropy powers. IEEE Trans.
Inf. Theory, IT-11:267–271, Apr. 1965.
[62] D. Blackwell, L. Breiman, and A. J. Thomasian. Proof of Shannon’s trans-
mission theorem for ﬁnite-state indecomposable channels. Ann. Math. Stat.,
pages 1209–1220, 1958.
[63] D. Blackwell, L. Breiman, and A. J. Thomasian. The capacity of a class of
channels. Ann. Math. Stat., 30:1229–1241, 1959.
[64] D. Blackwell, L. Breiman, and A. J. Thomasian.
The capacities of cer-
tain channel classes under random coding. Ann. Math. Stat., 31:558–567,
1960.
[65] R. Blahut. Computation of channel capacity and rate distortion functions.
IEEE Trans. Inf. Theory, IT-18:460–473, 1972.
[66] R. E. Blahut. Information bounds of the Fano–Kullback type. IEEE Trans.
Inf. Theory, IT-22:410–421, 1976.
[67] R. E. Blahut.
Principles and Practice of Information Theory.
Addison-
Wesley, Reading, MA, 1987.
[68] R. E. Blahut. Hypothesis testing and information theory. IEEE Trans. Inf.
Theory, IT-20:405–417, 1974.
[69] R. E. Blahut. Theory and Practice of Error Control Codes. Addison-Wesley,
Reading, MA, 1983.


## PDF page 719

BIBLIOGRAPHY
693
[70] B. M. Hochwald, G. Caire, B. Hassibi, and T. L. Marzetta (Eds.). IEEE
Trans. Inf. Theory, Special Issue on Space-Time Transmission, Reception,
Coding and Signal-Processing, Vol. 49, Oct. 2003.
[71] L. Boltzmann.
Beziehung
Zwischen
dem
zweiten
Hauptsatze
der
mechanischen W¨armertheorie und der Wahrscheilichkeitsrechnung respek-
tive den Saetzen uber das W¨armegleichgwicht. Wien. Ber., pages 373–435,
1877.
[72] R. C. Bose and D. K. Ray-Chaudhuri. On a class of error correcting binary
group codes. Inf. Control, 3:68–79, Mar. 1960.
[73] H. J. Brascamp and E. J. Lieb. Best constants in Young’s inequality, its
converse and its generalization to more than three functions. Adv. Math.,
20:151–173, 1976.
[74] L. Breiman. The individual ergodic theorems of information theory. Ann.
Math. Stat., 28:809–811, 1957. With correction made in 31:809-810.
[75] L. Breiman. Optimal gambling systems for favourable games. In Fourth
Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1,
pages 65–78. University of California Press, Berkeley, CA, 1961.
[76] L. Breiman, J. H. Friedman, R. A. Olshen, and C. J. Stone. Classiﬁcation
and Regression Trees. Wadsworth & Brooks, Paciﬁc Grove, CA, 1984.
[77] L. Brillouin. Science and Information Theory. Academic Press, New York,
1962.
[78] J. A. Bucklew.
The source coding theorem via Sanov’s theorem.
IEEE
Trans. Inf. Theory, pages 907–909, Nov. 1987.
[79] J. A. Bucklew.
Large Deviation Techniques in Decision, Simulation, and
Estimation. Wiley, New York, 1990.
[80] J. P. Burg. Maximum entropy spectral analysis. Ph.D. thesis, Department of
Geophysics, Stanford University, Stanford, CA, 1975.
[81] M. Burrows and D. J. Wheeler. A Block-Sorting Lossless Data Compression
Algorithm (Tech. Rept. 124). Digital Systems Research Center, Palo Alto,
CA, May 1994.
[82] A. R. Calderbank. The art of signaling: ﬁfty years of coding theory. IEEE
Trans. Inf. Theory, pages 2561–2595, Oct. 1998.
[83] A. R. Calderbank and P. W. Shor. Good quantum error-correcting codes
exist. Phys. Rev. A, pages 1098–1106, 1995.
[84] A. Carleial. Outer bounds on the capacity of the interference channel. IEEE
Trans. Inf. Theory, IT-29:602–606, 1983.
[85] A. B. Carleial. A case where interference does not reduce capacity. IEEE
Trans. Inf. Theory, IT-21:569–570, 1975.
[86] G. Chaitin. Information-Theoretic Incompleteness. World Scientiﬁc, Singa-
pore, 1992.
[87] G. J. Chaitin. On the length of programs for computing binary sequences.
J. ACM, pages 547–569, 1966.


## PDF page 720

694
BIBLIOGRAPHY
[88] G. J. Chaitin.
The limits of mathematics.
J. Universal Comput. Sci.,
2(5):270–305, 1996.
[89] G. J. Chaitin. On the length of programs for computing binary sequences.
J. ACM, 13:547–569, 1966.
[90] G. J. Chaitin. Information theoretical limitations of formal systems. J. ACM,
21:403–424, 1974.
[91] G. J. Chaitin. Randomness and mathematical proof. Sci. Am., 232(5):47–52,
May 1975.
[92] G. J. Chaitin. Algorithmic information theory. IBM J. Res. Dev., 21:350–359,
1977.
[93] G. J. Chaitin. Algorithmic Information Theory. Cambridge University Press,
Cambridge, 1987.
[94] C. S. Chang and J. A. Thomas. Huffman algebras for independent random
variables. Discrete Event Dynam. Syst., 4:23–40, 1994.
[95] C. S. Chang and J. A. Thomas. Effective bandwidth in high speed digital
networks. IEEE J. Select. Areas Commun., 13:1091–1114, Aug. 1995.
[96] R. Chellappa. Markov Random Fields: Theory and Applications. Academic
Press, San Diego, CA, 1993.
[97] H. Chernoff. A measure of the asymptotic efﬁciency of tests of a hypo-
thesis based on a sum of observations.
Ann. Math. Stat., 23:493–507,
1952.
[98] B. S. Choi and T. M. Cover.
An information-theoretic proof of Burg’s
maximum entropy spectrum. Proc. IEEE, 72:1094–1095, 1984.
[99] N. Chomsky. Three models for the description of language. IEEE Trans.
Inf. Theory, pages 113–124, Sept. 1956.
[100] P. A. Chou, M. Effros, and R. M. Gray. A vector quantization approach to
universal noiseless coding and quantization. IEEE Trans. Inf. Theory, pages
1109–1138, July 1996.
[101] K. L. Chung. A note on the ergodic theorem of information theory. Ann.
Math. Stat., 32:612–614, 1961.
[102] B. S. Clarke and A. R. Barron. Information-theoretic asymptotics of Bayes’
methods. IEEE Trans. Inf. Theory, pages 453–471, May 1990.
[103] B. S. Clarke and A. R. Barron. Jeffreys’ prior is asymptotically least favor-
able under entropy risk. J. Stat. Planning Inf., pages 37–60, Aug. 1994.
[104] M. Costa and T. M. Cover. On the similarity of the entropy power inequal-
ity and the Brunn–Minkowski inequality.
IEEE Trans. Inf. Theory, IT-
30:837–839, 1984.
[105] M. H. M. Costa. On the Gaussian interference channel. IEEE Trans. Inf.
Theory, pages 607–615, Sept. 1985.
[106] M. H. M. Costa and A. A. El Gamal. The capacity region of the discrete
memoryless interference channel with strong interference. IEEE Trans. Inf.
Theory, pages 710–711, Sept. 1987.


