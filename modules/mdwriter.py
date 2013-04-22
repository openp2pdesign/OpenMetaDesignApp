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
fo.write(temp.title+": Metadesign\n")
titleFormat = ""
for i in temp.title+": Metadesign":
    titleFormat += "="
titleFormat += "\n"
fo.write(titleFormat)
fo.write("\n")


fo.write("# General Information\n")
fo.write("\n")

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
fo.write("The project has been developed together and for a community that:\n")
if temp.community.locality != "":
    fo.write(" + lives in "+temp.community.locality+"\n")
if temp.community.activity != "":
    fo.write(" + works in the activity of "+temp.community.activity+"\n")
if temp.community.subject != "":
    fo.write(" + is described as "+temp.community.subject+"\n")
if temp.community.object != "":
    fo.write(" + works in the activity upon "+temp.community.object+"\n")
if temp.community.outcome != "":
    fo.write(" + works in the activity in order to get "+temp.community.outcome+"\n")
if temp.community.needs != "":
    fo.write(" + works in the activity because its needs are "+temp.community.needs+"\n")
if temp.community.tools != "":
    fo.write(" + uses these tools in the activity: "+temp.community.tools+"\n")
if temp.community.rules != "":
    fo.write(" + uses these rules in the activity: "+temp.community.rules+"\n")
if temp.community.roles != "":
    fo.write(" + adopt these roles in the activity: "+temp.community.roles+"\n")
if temp.community.context != "":
    fo.write(" + works in the bigger context of: "+temp.community.context+"\n")
fo.write("\n")


# Write img tag for process participation
fo.write("# Participation Process\n")
fo.write("\n")
fo.write('<img src="'+temp.repo+"/blob/master/metadesign/"+"participation_process.png"+'">'+"\n")
fo.write("\n")

# Write img tag for actors and flows
fo.write("# Actors and Flows in the process\n")
fo.write("\n")
fo.write('<img src="'+temp.repo+"/blob/master/metadesign/"+"actors_flows_system.png"+'">'+"\n")
fo.write("\n")

# Write business model
fo.write("# Business Model\n")
fo.write("\n")
if temp.businessmodel.valueproposition != "":
    fo.write(" + its Value Proposition is: "+temp.businessmodel.valueproposition+"\n")
if temp.businessmodel.customersegments != "":
    fo.write(" + its Customer Segments are: "+temp.businessmodel.customersegments+"\n")
if temp.businessmodel.customerrelationships != "":
    fo.write(" + its Customer Relationships are: "+temp.businessmodel.customerrelationships+"\n")
if temp.businessmodel.channels != "":
    fo.write(" + its Channels are: "+temp.businessmodel.channels+"\n")
if temp.businessmodel.revenuestreams != "":
    fo.write(" + its Revenue Streams are: "+temp.businessmodel.revenuestreams+"\n")
if temp.businessmodel.coststructure != "":
    fo.write(" + its Cost Structure is: "+temp.businessmodel.coststructure+"\n")
if temp.businessmodel.keyactivities != "":
    fo.write(" + its Key Activities are: "+temp.businessmodel.keyactivities+"\n")
if temp.businessmodel.keyresources != "":
    fo.write(" + its Key Resources are: "+temp.businessmodel.keyresources+"\n")
if temp.businessmodel.keypartners != "":
    fo.write(" + its Key Partners are: "+temp.businessmodel.keypartners+"\n")
fo.write("\n")

# Write img tag for network analysis
fo.write("# The network of interactions in the project\n")
fo.write("\n")
fo.write('<img src="'+temp.repo+"/blob/master/metadesign/"+"network_interactions.png"+'">'+"\n")
fo.write("\n")

# Write license for metadesign project


# Close opend file
fo.close()