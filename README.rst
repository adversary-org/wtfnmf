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
correct copyright field for the user/developer to set for themselves.
The script takes two parameters: the year to start the copyright from
and the name.  If including an email address with the name then that
must be in quotation marks to prevent the shell trying to pipe the
command into itself:

::
   
    wtfnmfgen.py 2015 Danger Mouse

or:

::
   
    wtfnmfgen.py 2015 "Danger Mouse <dm@superspy.example.net>"

The first command would produce:

::
   
    Copyright (C) Danger Mouse, 2015-2016
    Copyright (C) 2015-2016 Danger Mouse
    Copyright © Danger Mouse, 2015-2016
    Copyright © 2015-2016 Danger Mouse

While the second command would produce:

::

   Copyright (C) Danger Mouse <dm@superspy.example.net>, 2015-2016
   Copyright (C) 2015-2016 Danger Mouse <dm@superspy.example.net>
   Copyright © Danger Mouse <dm@superspy.example.net>, 2015-2016
   Copyright © 2015-2016 Danger Mouse <dm@superspy.example.net>

Either option should be fine, it's up to the end user's preference as
to which file(s) to keep and which to delete.  The output of the
script is always eight files; four versions of the license file and
four versions of the boilerplate to add to code or anything else.


FAQ
---

1. Why did you include a copyright notice with the license text
   instead of making it public domain?

I am in Australia, everything I write is automatically under copyright
whether it is labelled or not.

Furthermore, public domain means different things in different
jurisdictions and the (usually American) assumption that making
something public domain makes it more free or more permissive and thus
more usable is actually false in many places.  By retaining copyright
and releasing the license under the terms of itself I actually achieve
what you want rather than play to what you incorrectly think is true.
