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

#from modules.classes import *

from classes import *

# project, currentFolder

temp = project()
temp.load("test2.meta")

# Open a file
fo = open("README.md", "w")

# Write a title
fo.write(temp.title+"\n");
titleFormat = ""
for i in temp.title:
    titleFormat += "="
titleFormat += "\n"
fo.write(titleFormat)
fo.write("\n")


fo.write("# General Information\n");
fo.write("\n");

# Write founders
founders = "The **" + temp.title + "** project has been started by "
for j,i in enumerate(temp.founders):
    founders += i
    if j > 0:
        founders += ", "
founders += "."
fo.write(founders+"\n");
fo.write("Its metadesign component, that here explains how the project works and how it has been developed is now at version "+temp.version+"\n")
fo.write("\n")



# Write img tag for process participation
fo.write("# Participation Process\n");
fo.write("\n");
fo.write('<img src="'+temp.repo+"/blob/master/metadesign/"+"participation_process.png"+'">'+"\n");


# Write img tag for actors and flows
fo.write("# Actors and Flows in the process\n");
fo.write("\n");
fo.write('<img src="'+temp.repo+"/blob/master/metadesign/"+"actors_flows_system.png"+'">'+"\n");


# Write img tag for business models, or text?

# Write img tag for network analysis
fo.write("# The network of interactions in the project\n");
fo.write("\n");
fo.write('<img src="'+temp.repo+"/blob/master/metadesign/"+"network_interactions.png"+'">'+"\n");

# Write license for metadesign project


# Close opend file
fo.close()