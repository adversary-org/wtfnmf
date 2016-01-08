#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

##
# Copyright (C) Ben McGinnes, 2014-2016
# Copyright © Ben McGinnes, 2014-2016
#
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.2.0
#
# License:  WTFNMFPLv1
#
# https://github.com/adversary-org/wtfnmf
#
# Requirements:
#
# * Python 3.2 or later.
# * Should work with Python 2.7, but not guaranteed.
#
# Options and notes:
#
# Adapted from my BSD license generator.
#
# Usage:  
#
# wtfnmfgen.py YYYY Danger Mouse
#
# or
#
# wtfnmfgen.py YYYY "Danger Mouse <dmouse@dm.example.org>"
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2014-2016"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2014-2016"
__license__ = "WTFNMFPLv1"
__version__ = "0.2.0"

from datetime import datetime
import sys

print("""
    If entering both options (start year and name) on the command line
    then the year must be the first option and the name second.
    Entering the name in quotation marks is optional unless an email
    address is included with the copyright line.  If including an
    email address using "<" and ">" then the quotation marks are
    required to prevent the shell from using those to direct input or
    output somewhere.".

    Two text files containing the license are created, one in plain
    text and the other in Unicode (UTF-8).
""")

l = len(sys.argv)

if l == 1:
    year1 = input("Enter the year to begin copyright from: ")
    name = input("Enter your name as you want it to appear on the copyright: ")
elif l == 2:
    year1 = sys.argv[1]
    name = input("Enter your name as you want it to appear on the copyright: ")
elif l == 3:
    year1 = sys.argv[1]
    name = sys.argv[2]
elif l >= 4:
    year1 = sys.argv[1]
    name = " ".join(sys.argv[2:])

year2 = str(datetime.now().year)

if year1 == year2:
    year3 = year2
else:
    year3 = year1+"-"+year2

txta = "Copyright (C) {0}, {1}".format(name, year3)
texta = "Copyright (C) {0} {1}".format(year3, name)
txtu = "Copyright © {0}, {1}".format(name, year3)
textu = "Copyright © {0} {1}".format(year3, name)

boilera1 = """ 
This work is free.  You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To But It's Not My Fault Public
License, Version 1, as published by Ben McGinnes.  See the
COPYING.WTFNMFPLv1a.txt file for more details.
"""

boilera2 = """ 
This work is free.  You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To But It's Not My Fault Public
License, Version 1, as published by Ben McGinnes.  See the
COPYING.WTFNMFPLv1a.text file for more details.
"""

ltexta = """
This work is free.  You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To But It's Not My Fault Public
License, Version 1, as published by Ben McGinnes:

    DO WHAT THE FUCK YOU WANT TO BUT IT'S NOT MY FAULT PUBLIC LICENSE
                    Version 1, October 2013

 Copyright (C) 2013 Ben McGinnes <ben@adversary.org>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

   DO WHAT THE FUCK YOU WANT TO BUT IT'S NOT MY FAULT PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

  1. Do not hold the author(s), creator(s), developer(s) or
     distributor(s) liable for anything that happens or goes wrong
     with your use of the work.
"""

boileru1 = """ 
This work is free.  You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To But It's Not My Fault Public
License, Version 1, as published by Ben McGinnes.  See the
COPYING.WTFNMFPLv1u.txt file for more details.
"""

boileru2 = """ 
This work is free.  You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To But It's Not My Fault Public
License, Version 1, as published by Ben McGinnes.  See the
COPYING.WTFNMFPLv1u.text file for more details.
"""

ltextu = """
This work is free.  You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To But It's Not My Fault Public
License, Version 1, as published by Ben McGinnes:

    DO WHAT THE FUCK YOU WANT TO BUT IT'S NOT MY FAULT PUBLIC LICENSE
                    Version 1, October 2013

 Copyright © 2013 Ben McGinnes <ben@adversary.org>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

   DO WHAT THE FUCK YOU WANT TO BUT IT'S NOT MY FAULT PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

  1. Do not hold the author(s), creator(s), developer(s) or
     distributor(s) liable for anything that happens or goes wrong
     with your use of the work.
"""

a1file = open("COPYING.WTFNMFPLv1a.txt", "w")
a1file.write(txta)
a1file.write("\n")
a1file.write(ltexta)
a1file.close()

b1file = open("ascii_boilerplate.txt", "w")
b1file.write(txta)
b1file.write("\n")
b1file.write(boilera1)
b1file.close()

u1file = open("COPYING.WTFNMFPLv1u.txt", "w")
u1file.write(txtu)
u1file.write("\n")
u1file.write(ltextu)
u1file.close()

v1file = open("utf8_boilerplate.txt", "w")
v1file.write(txtu)
v1file.write("\n")
v1file.write(boileru1)
v1file.close()

a2file = open("COPYING.WTFNMFPLv1a.text", "w")
a2file.write(texta)
a2file.write("\n")
a2file.write(ltexta)
a2file.close()

b2file = open("ascii_boilerplate.text", "w")
b2file.write(texta)
b2file.write("\n")
b2file.write(boilera2)
b2file.close()

u2file = open("COPYING.WTFNMFPLv1u.text", "w")
u2file.write(textu)
u2file.write("\n")
u2file.write(ltextu)
u2file.close()

v2file = open("utf8_boilerplate.text", "w")
v2file.write(textu)
v2file.write("\n")
v2file.write(boileru2)
v2file.close()
