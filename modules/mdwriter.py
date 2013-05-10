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

import os
from classes import *


def insert(original, new, pos):
    return original[:pos] + new + original[pos:] 

def mdwrite(temp,currentFolder):
    
    # The correct link for the raw images
    repo_raw = insert(temp.repo,"raw.",8)
    
    # Open a file
    fo = open(currentFolder+"README.md", "w")
    
    # Write a title
    fo.write(temp.title+": Metadesign\n")
    titleFormat = ""
    for i in temp.title+": Metadesign":
        titleFormat += "="
    titleFormat += "\n"
    fo.write(titleFormat)
    fo.write("\n")
    
    
    fo.write("## General Information\n")
    fo.write("\n")
    
    # Write founders
    founders = "The **" + temp.title + "** project has been started by "
    for j,i in enumerate(temp.founders):
        founders += i
        if j > 0:
            founders += ", "
    founders += "."
    fo.write(founders+"\n");
    fo.write("Its metadesign component (version "+temp.version+"), that here explains how the project works and how it has been developed is now at version "+temp.version+"\n")
    fo.write("\n")
    fo.write("The project has been developed together and for a community that:\n")
    if temp.community.locality != "":
        fo.write(" + **lives** in "+temp.community.locality+"\n")
    if temp.community.activity != "":
        fo.write(" + works in the **activity** of "+temp.community.activity+"\n")
    if temp.community.subject != "":
        fo.write(" + is **described** as "+temp.community.subject+"\n")
    if temp.community.object != "":
        fo.write(" + works in the activity **upon** "+temp.community.object+"\n")
    if temp.community.outcome != "":
        fo.write(" + works in the activity **in order to get** "+temp.community.outcome+"\n")
    if temp.community.needs != "":
        fo.write(" + works in the activity because **its needs** are "+temp.community.needs+"\n")
    if temp.community.tools != "":
        fo.write(" + uses these **tools** in the activity: "+temp.community.tools+"\n")
    if temp.community.rules != "":
        fo.write(" + uses these **rules** in the activity: "+temp.community.rules+"\n")
    if temp.community.roles != "":
        fo.write(" + adopt these **roles** in the activity: "+temp.community.roles+"\n")
    if temp.community.context != "":
        fo.write(" + works in the **bigger context** of: "+temp.community.context+"\n")
    fo.write("\n")
    
    
    # Write img tag for process participation
    if os.path.exists(currentFolder+"participation_process.png"):
        fo.write("## Participation Process\n")
        fo.write("\n")
        fo.write('<img width="890" src="'+repo_raw+"/master/metadesign/"+"participation_process.png"+'">'+"\n")
        fo.write("\n")
    
    # Write img tag for actors and flows
    if os.path.exists(currentFolder+"actors_flows_system.png"):
        fo.write("## Actors and Flows in the process\n")
        fo.write("\n")
        fo.write('<img width="890" src="'+repo_raw+"/master/metadesign/"+"actors_flows_system.png"+'">'+"\n")
        fo.write("\n")
    
    # Write business model
    fo.write("## Business Model\n")
    fo.write("\n")
    if temp.businessmodel.valueproposition != "":
        fo.write(" + its **Value Proposition** is: "+temp.businessmodel.valueproposition+"\n")
    if temp.businessmodel.customersegments != "":
        fo.write(" + its **Customer Segments** are: "+temp.businessmodel.customersegments+"\n")
    if temp.businessmodel.customerrelationships != "":
        fo.write(" + its **Customer Relationships** are: "+temp.businessmodel.customerrelationships+"\n")
    if temp.businessmodel.channels != "":
        fo.write(" + its **Channels** are: "+temp.businessmodel.channels+"\n")
    if temp.businessmodel.revenuestreams != "":
        fo.write(" + its **Revenue Streams** are: "+temp.businessmodel.revenuestreams+"\n")
    if temp.businessmodel.coststructure != "":
        fo.write(" + its **Cost Structure** is: "+temp.businessmodel.coststructure+"\n")
    if temp.businessmodel.keyactivities != "":
        fo.write(" + its **Key Activities** are: "+temp.businessmodel.keyactivities+"\n")
    if temp.businessmodel.keyresources != "":
        fo.write(" + its **Key Resources** are: "+temp.businessmodel.keyresources+"\n")
    if temp.businessmodel.keypartners != "":
        fo.write(" + its **Key Partners** are: "+temp.businessmodel.keypartners+"\n")
    fo.write("\n")
    
    # Write img tag for network analysis
    if os.path.exists(currentFolder+"network_interactions.png"):
        fo.write("## The network of interactions in the project\n")
        fo.write("\n")
        fo.write('<img width="890" src="'+repo_raw+"/master/metadesign/"+"network_interactions.png"+'">'+"\n")
        fo.write("\n")
    
    # Write license for metadesign project
    fo.write("## License of this metadesign project\n")
    fo.write("\n")
    
    if temp.license == "Creative Commons - Attribution (CC BY)":
        fo.write('<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.')
    elif temp.license == "Creative Commons - Attribution Share Alike (CC BY-SA)":
        fo.write('<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.')
    elif temp.license == "Creative Commons - Attribution No Derivatives (CC BY-ND)":
        fo.write('<a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nd/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/deed.en_US">Creative Commons Attribution-NoDerivs 3.0 Unported License</a>.')
    elif temp.license == "Creative Commons - Attribution Non-Commercial (CC BY-NC)":
        fo.write('<a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/3.0/deed.en_US">Creative Commons Attribution-NonCommercial 3.0 Unported License</a>.')
    elif temp.license == "Creative Commons - Attribution Non-Commercial Share Alike (CC BY-NC-SA)":
        fo.write('<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.')
    elif temp.license == "Creative Commons - Attribution Non-Commercial No Derivatives (CC BY-NC-ND)":
        fo.write('<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License</a>.')
    elif temp.license == "Creative Commons - No Rights Reserved (CC0)":
        fo.write('<p xmlns:dct="http://purl.org/dc/terms/"><a rel="license"href="http://creativecommons.org/publicdomain/zero/1.0/"><img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" /></a><br />To the extent possible under law,<span rel="dct:publisher" resource="[_:publisher]">the person who associated CC0</span>with this work has waived all copyright and related or neighboring rights to this work.</p>')
        
    fo.write("\n")
    
    # Close opend file
    fo.close()


if __name__ == "__main__":
    pass