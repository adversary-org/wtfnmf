Do What The Fuck You Want To But It's Not My Fault
==================================================

The Do What The Fuck You Want To But It's Not My Fault Public License
(WTFNMFPL or WTFNMFPLv1) is a variation on the Do What The Fuck You Want
Public License (WTFPL) by Sam Hocevar. Essentially it is the same as the
WTFPL, except with an additional clause to indemnify the author,
creator, developer or distributor against anything a third party might
do or encounter with or as a result of whatever's being licensed with
it.

This license was `first published at Organised
Adversary <http://www.adversary.org/wp/2013/10/14/do-what-the-fuck-you-want-but-its-not-my-fault/>`__
in October, 2013.

The license is free to use by anyone as per the terms of itself.


WTFNMF Public License Generator
-------------------------------

Now includes a Python script to generate the license files with a
correct copyright field for the user/developer toset for themselves.
The script takes two parameters: the year to start the copyright from
and the name.  If including an email address with the name then that
must be in quotation marks to prevent the shell trying to pipe the
command into itself:

::
    wtfnmfgen.py 2015 Danger Mouse

or:

::
    wtfnmfgen.py 2015 "Danger Mouse <dm@superspy.example.net>"

The script detects whether or not an email address is present (by the
@ symbol) and selects the form of the copyright string on that basis.
So the first command would produce:

::
    Copyright (C) Danger Mouse, 2015-2016
    Copyright © Danger Mouse, 2015-2016

While the second command would produce:

::
   Copyright (C) 2015-2016 Danger Mouse <dm@superspy.example.net>
   Copyright © 2015-2016 Danger Mouse <dm@superspy.example.net>
