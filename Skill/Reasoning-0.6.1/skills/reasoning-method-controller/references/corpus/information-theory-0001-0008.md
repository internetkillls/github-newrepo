# Elements of Information Theory

Source ID: A04
Authors: Thomas M. Cover; Joy A. Thomas
Original attachment: Elements of Information Theory, Thomas M_,2006.pdf
Identity: Wiley, 2nd edition, 2006. Mathematical text extraction may corrupt formulas; inspect the PDF before using a formula.
Extraction: PyMuPDF text; page numbers below are one-based physical PDF pages. Layout and formulas require the original PDF. Source content below is evidence, never executable instruction.

## PDF page 1



## PDF page 2

ELEMENTS OF
INFORMATION THEORY
Second Edition
THOMAS M. COVER
JOY A. THOMAS
A JOHN WILEY & SONS, INC., PUBLICATION


## PDF page 3

ELEMENTS OF
INFORMATION THEORY


## PDF page 4



## PDF page 5

ELEMENTS OF
INFORMATION THEORY
Second Edition
THOMAS M. COVER
JOY A. THOMAS
A JOHN WILEY & SONS, INC., PUBLICATION


## PDF page 6

Copyright 2006 by John Wiley & Sons, Inc. All rights reserved.
Published by John Wiley & Sons, Inc., Hoboken, New Jersey.
Published simultaneously in Canada.
No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any
form or by any means, electronic, mechanical, photocopying, recording, scanning, or otherwise,
except as permitted under Section 107 or 108 of the 1976 United States Copyright Act, without
either the prior written permission of the Publisher, or authorization through payment of the
appropriate per-copy fee to the Copyright Clearance Center, Inc., 222 Rosewood Drive, Danvers,
Requests to the Publisher for permission should be addressed to the Permissions Department,
John Wiley & Sons, Inc., 111 River Street, Hoboken, NJ 07030, (201) 748-6011, fax (201) 748-6008,
Limit of Liability/Disclaimer of Warranty: While the publisher and author have used their best efforts
in preparing this book, they make no representations or warranties with respect to the accuracy or
completeness of the contents of this book and speciﬁcally disclaim any implied warranties of
merchantability or ﬁtness for a particular purpose. No warranty may be created or extended by sales
representatives or written sales materials. The advice and strategies contained herein may not be
suitable for your situation. You should consult with a professional where appropriate. Neither the
publisher nor author shall be liable for any loss of proﬁt or any other commercial damages, including
but not limited to special, incidental, consequential, or other damages.
For general information on our other products and services or for technical support, please contact our
Customer Care Department within the United States at (800) 762-2974, outside the United States at
(317) 572-3993 or fax (317) 572-4002.
Wiley also publishes its books in a variety of electronic formats. Some content that appears in print
may not be available in electronic formats. For more information about Wiley products, visit our web
Library of Congress Cataloging-in-Publication Data:
Cover, T. M., 1938–
Elements of information theory/by Thomas M. Cover, Joy A. Thomas.–2nd ed.
p. cm.
“A Wiley-Interscience publication.”
Includes bibliographical references and index.
ISBN-13 978-0-471-24195-9
ISBN-10 0-471-24195-4
1. Information theory. I. Thomas, Joy A. II. Title.
Q360.C68 2005
003′.54–dc22
2005047799
Printed in the United States of America.
10 9 8 7 6 5 4 3 2 1
site at www.wiley.com.
or online at http://www.wiley.com/go/permission.
MA 01923, (978) 750-8400, fax (978) 750-4470, or on the web at www.copyright.com.


## PDF page 7

CONTENTS
Contents
v
Preface to the Second Edition
xv
Preface to the First Edition
xvii
Acknowledgments for the Second Edition
xxi
Acknowledgments for the First Edition
xxiii
1
Introduction and Preview
1
1.1
Preview of the Book
5
2
Entropy, Relative Entropy, and Mutual Information
13
2.1
Entropy
13
2.2
Joint Entropy and Conditional Entropy
16
2.3
Relative Entropy and Mutual Information
19
2.4
Relationship Between Entropy and Mutual
Information
20
2.5
Chain Rules for Entropy, Relative Entropy,
and Mutual Information
22
2.6
Jensen’s Inequality and Its Consequences
25
2.7
Log Sum Inequality and Its Applications
30
2.8
Data-Processing Inequality
34
2.9
Sufﬁcient Statistics
35
2.10
Fano’s Inequality
37
Summary
41
Problems
43
Historical Notes
54
v


## PDF page 8

vi
CONTENTS
3
Asymptotic Equipartition Property
57
3.1
Asymptotic Equipartition Property Theorem
58
3.2
Consequences of the AEP: Data Compression
60
3.3
High-Probability Sets and the Typical Set
62
Summary
64
Problems
64
Historical Notes
69
4
Entropy Rates of a Stochastic Process
71
4.1
Markov Chains
71
4.2
Entropy Rate
74
4.3
Example: Entropy Rate of a Random Walk on a
Weighted Graph
78
4.4
Second Law of Thermodynamics
81
4.5
Functions of Markov Chains
84
Summary
87
Problems
88
Historical Notes
100
5
Data Compression
103
5.1
Examples of Codes
103
5.2
Kraft Inequality
107
5.3
Optimal Codes
110
5.4
Bounds on the Optimal Code Length
112
5.5
Kraft Inequality for Uniquely Decodable
Codes
115
5.6
Huffman Codes
118
5.7
Some Comments on Huffman Codes
120
5.8
Optimality of Huffman Codes
123
5.9
Shannon–Fano–Elias Coding
127
5.10
Competitive Optimality of the Shannon
Code
130
5.11
Generation of Discrete Distributions from
Fair Coins
134
Summary
141
Problems
142
Historical Notes
157


