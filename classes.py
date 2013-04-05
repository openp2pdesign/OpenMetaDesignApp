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

from lxml import etree

class businessmodel():
    "A class for the business model of the project"
    def __init__(self): 
        self.valueproposition = "Value proposition"
        self.customerrelationships = "Customer relationships"
        self.channels = "Channels"
        self.customersegments = "Customer segments"
        self.revenuestreams = "Revenue streams"
        self.coststructure = "Cost structure"
        self.keyactivities = "Key activities"
        self.keyresources = "Key resources"
        self.keypartners = "Key partners"
   
   
class flow():
    "A class for each flow in the design process"
    def __init__(self): 
        self.number = "0"
        self.type = "flow type"
        self.what = "what"
        self.direction = "Both directions"
        self.actor1 = "first actor"
        self.actor2 = "second actor" 


class step():
    "A class for each step in the design process"
    def __init__(self): 
        self.stepnumber = "0"
        self.title = "step title"
        self.participation = "none"
        self.tools = "tools"
        self.rules = "rules"
        self.actors = "actors"
        self.picture = "picture"
        self.flows = {} 


class community:
    "A class for a community analysis"
    def __init__(self): 
        self.locality = "Locality"
        self.activity = "Activity"
        self.subject = "Subject"
        self.object = "Object"
        self.outcome = "Outcome"
        self.needs = "Needs"
        self.tools = "Tools"
        self.rules = "Rules"
        self.roles = "Roles"
        self.context = "Context"


class project:
    "A class for a metadesign project"
    def __init__(self):
        self.title = "project title"
        self.version = "0.1"
        self.founders = ["founder"]
        self.license = "license"
        self.licenseurl = "http://"
        self.community = community()
        self.businessmodel = businessmodel()
        self.steps = {}
    
    def save(self,filename):
        project = etree.Element('project')
        doc = etree.ElementTree(project)
        
        # build the document  and the general information before saving it
        title = etree.SubElement(project, "title")
        title.text = self.title
        version = etree.SubElement(project, "version")
        version.text = self.version
        founders = etree.SubElement(project, "founders")
        for j in self.founders:
            founder = etree.SubElement(founders, "founder")
            founder.text = j
        license = etree.SubElement(project, "license")
        license.text = self.license
        licenseurl = etree.SubElement(project, "licenseurl")
        licenseurl.text = self.licenseurl
        
        # build the community analysis
        community = etree.SubElement(project, "community")
        locality = etree.SubElement(community, "locality")
        locality.text = self.community.locality
        activity = etree.SubElement(community, "activity")
        activity.text = self.community.activity
        subject = etree.SubElement(community, "subject")
        subject.text = self.community.subject
        object = etree.SubElement(community, "object")
        object.text = self.community.object
        outcome = etree.SubElement(community, "outcome")
        outcome.text = self.community.outcome
        needs = etree.SubElement(community, "needs")
        needs.text = self.community.needs
        activitytools = etree.SubElement(community, "communitytools")
        activitytools.text = self.community.tools
        activityrules = etree.SubElement(community, "communityrules")
        activityrules.text = self.community.rules
        activityroles = etree.SubElement(community, "communityroles")
        activityroles.text = self.community.roles
        context = etree.SubElement(community, "context")
        context.text = self.community.context
        
        # build the business model
        businessmodel = etree.SubElement(project, "businessmodel")
        valueproposition = etree.SubElement(businessmodel, "valueproposition")
        valueproposition.text = self.businessmodel.valueproposition
        customerrelationships = etree.SubElement(businessmodel,"customerrelationships")
        customerrelationships.text = self.businessmodel.customerrelationships
        channels = etree.SubElement(businessmodel,"channels")
        channels.text = self.businessmodel.channels
        customersegments = etree.SubElement(businessmodel,"customersegments")
        customersegments.text = self.businessmodel.customersegments
        revenuestreams = etree.SubElement(businessmodel,"revenuestreams")
        revenuestreams.text = self.businessmodel.revenuestreams
        coststructure = etree.SubElement(businessmodel,"coststructure")
        coststructure.text = self.businessmodel.coststructure
        keyactivities = etree.SubElement(businessmodel,"keyactivities")
        keyactivities.text = self.businessmodel.keyactivities
        keyresources = etree.SubElement(businessmodel,"keyresources")
        keyresources.text = self.businessmodel.keyresources
        keypartners = etree.SubElement(businessmodel,"keypartners")
        keypartners.text = self.businessmodel.keypartners
        
        # build the step
        for n,i in enumerate(self.steps):
            step = etree.SubElement(project, "step")
            stepnumber = etree.SubElement(step, "stepnumber")
            stepnumber.text = str(n)
            steptitle = etree.SubElement(step, "steptitle")
            steptitle.text = self.steps[n].title
            participation = etree.SubElement(step, "participation")
            participation.text = self.steps[n].participation
            tools = etree.SubElement(step, "tools")
            tools.text = self.steps[n].tools
            rules = etree.SubElement(step, "rules")
            rules.text = self.steps[n].rules
            actors = etree.SubElement(step, "actors")
            for j in self.steps[n].actors:
                actor = etree.SubElement(actors, "actor")
                actor.text = j
            picture = etree.SubElement(step, "picture")
            picture.text = self.steps[n].picture
            
            # build the flows
            flows = etree.SubElement(step, "flows")            
            for m,k in enumerate(self.steps[n].flows):
                flow = etree.SubElement(flows, "flow")
                flownumber = etree.SubElement(flow, "number")
                flownumber.text = self.steps[n].flows[m].number
                flowtype = etree.SubElement(flow, "type")
                flowtype.text = self.steps[n].flows[m].type
                what = etree.SubElement(flow, "what")
                what.text = self.steps[n].flows[m].what
                direction = etree.SubElement(flow, "direction")
                direction.text = self.steps[n].flows[m].direction
                actor1 = etree.SubElement(flow, "firstactor")
                actor1.text = self.steps[n].flows[m].actor1
                actor2 = etree.SubElement(flow, "secondactor")
                actor2.text = self.steps[n].flows[m].actor2
            
        # save the file
        outFile = open(filename, 'w')
        doc.write(outFile,pretty_print=True,xml_declaration=True, encoding="UTF-8")
        print "File saved successfully as",filename
        return
    
    def load(self,filename):
        doc = etree.parse(filename)
        
        # load general information
        self.title = doc.findtext("title")
        self.version = doc.findtext("version")
        founders = doc.xpath("//project/founders/founder/text()")
        for j,i in enumerate(founders):
            if j == 0:
                self.founders[j] = i
            else:
                self.founders.append(i)
        self.license = doc.findtext("license")
        self.licenseurl = doc.findtext("licenseurl")
        
        # load community analysis
        self.community.locality = doc.xpath("//project/community/locality/text()")
        self.community.activity = doc.xpath("//project/community/activity/text()")
        self.community.subject = doc.xpath("//project/community/subject/text()")
        self.community.object = doc.xpath("//project/community/object/text()")
        self.community.outcome = doc.xpath("//project/community/outcome/text()")
        self.community.needs = doc.xpath("//project/community/needs/text()")
        self.community.tools = doc.xpath("//project/community/communitytools/text()")
        self.community.rules = doc.xpath("//project/community/communityrules/text()")
        self.community.roles = doc.xpath("//project/community/communityroles/text()")
        self.community.context = doc.xpath("//project/community/context/text()")
        
        # load business model
        self.businessmodel.valueproposition = doc.xpath("//project/businessmodel/valueproposition/text()")
        self.businessmodel.customerrelationships = doc.xpath("//project/businessmodel/customerrelationships/text()")
        self.businessmodel.channels = doc.xpath("//project/businessmodel/channels/text()")
        self.businessmodel.customersegments = doc.xpath("//project/businessmodel/customersegments/text()")
        self.businessmodel.revenuestreams = doc.xpath("//project/businessmodel/revenuestreams/text()")
        self.businessmodel.coststructure = doc.xpath("//project/businessmodel/coststructure/text()")
        self.businessmodel.keyactivities = doc.xpath("//project/businessmodel/keyactivities/text()")
        self.businessmodel.keyresources = doc.xpath("//project/businessmodel/keyresources/text()")
        self.businessmodel.keypartners = doc.xpath("//project/businessmodel/keypartners/text()")
        
        # load steps 
        steplist = doc.xpath("//project/step")
        for k,m in enumerate(steplist):
            stepelements = m.getchildren()
            for l in stepelements:
                if l.tag == "stepnumber":
                    self.steps[k] = step()
                    self.steps[k].stepnumber = l.text
                elif l.tag == "steptitle":
                    self.steps[k].title = l.text
                elif l.tag == "participation":
                    self.steps[k].participation = l.text
                elif l.tag == "tools":
                    self.steps[k].tools = l.text
                elif l.tag == "rules":
                    self.steps[k].rules = l.text
                elif l.tag == "actors":
                    self.steps[k].actors = []
                    for j,i in enumerate(l.getchildren()):
                        self.steps[k].actors.append(l.getchildren()[j].text)
                elif l.tag == "picture":
                    self.steps[k].picture = l.text
                elif l.tag == "flows":
                    for s,r in enumerate(l.getchildren()):
                        self.steps[k].flows[s] = flow()
                        self.steps[k].flows[s].number = r.getchildren()[0].text
                        self.steps[k].flows[s].type = r.getchildren()[1].text
                        self.steps[k].flows[s].what = r.getchildren()[2].text
                        self.steps[k].flows[s].direction = r.getchildren()[3].text
                        self.steps[k].flows[s].actor1 = r.getchildren()[4].text
                        self.steps[k].flows[s].actor2 = r.getchildren()[5].text
                        
                                       
        return


if __name__ == "__main__":
    #p = project()
    #p.save("test.meta")
    print ""
    
    a = project()
    a.load("test2.meta")
    print "Flows0",a.steps[0].flows
    print "Flows1",a.steps[1].flows
    print "Flows2",a.steps[2].flows
    print "-"
    #print a.steps[0].flows[0].direction
    #print a.steps[0].flows[0].actor1
    #print a.steps[0].flows[0].actor2
    #print a.steps[0].flows[0].type
    #print a.steps[0].flows[0].what
    
    for i in range(len(a.steps)):
        print "---"
        print "I",i
        for u in range(len(a.steps[i].flows)):
            print "v:",u
            print "n.",a.steps[i].flows[u].number
            print "DIR",a.steps[i].flows[u].direction
            print "AR1",a.steps[i].flows[u].actor1
            print "AR2",a.steps[i].flows[u].actor2
            print "-"

