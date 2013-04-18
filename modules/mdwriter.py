# -*- coding: utf-8 -*-
#
# Open MetaDesign 0.1
#
# Author: Massimo Menichinelli
# Website:
# http://openmetadesign.org
# http://openp2pdesign.org
#
# License: GPL v.3
#

from modules.classes import *


a = project()
a.load("test2.meta")
print "Flows0",a.steps[0].flows

# Open a file
fo = open("README.md", "w")

# Write a title
fo.write(a.title+"\n");
titleFormat = ""
for i in a.title:
    titleFormat += "="
titleFormat += "\n"
fo.write(titleFormat)
fo.write("\n")


# Write a description

# Write founders

# Write img tag for process participation

# Write img tag for actors and flows

# Write img tag for business models, or text?

# Write img tag for network analysis


# Close opend file
fo.close()