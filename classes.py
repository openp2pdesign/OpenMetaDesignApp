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
    def __init__(self, 
                 valueproposition = "Value proposition", 
                 customerrelationships = "Customer relationships", 
                 channels = "Channels",
                 customersegments = "Customer segments",
                 revenuestreams = "Revenue streams",
                 coststructure = "Cost structure",
                 keyactivities = "Key activities",
                 keyresources = "Key resources",
                 keypartners = "Key partners"): 
        
        self.valueproposition = valueproposition
        self.customerrelationships = customerrelationships
        self.channels = channels
        self.customersegments = customersegments
        self.coststructure = coststructure
        self.keyactivities = keyactivities
        self.keyresources = keyresources
        self.keypartners = keypartners
   
class flow():
    "A class for each flow in the design process"
    def __init__(self, 
                 number = "0",
                 type = "flow type", 
                 what = "none", 
                 direction = "direction",
                 fromrole = "from",
                 torole =  "to" ): 
        
        self.number = number
        self.type = type
        self.what = what
        self.direction = direction
        self.fromrole = fromrole
        self.torole = torole 

class step():
    "A class for each step in the design process"
    def __init__(self, 
                 stepnumber = "0",
                 title = "step title", 
                 participation = "none", 
                 tools = "tools",
                 rules = "rules",
                 roles = "roles",
                 picture = "none",
                 flows = {0:flow()}): 
        
        self.stepnumber = stepnumber
        self.title = title
        self.participation = participation
        self.tools = tools
        self.rules = rules
        self.roles = roles
        self.picture = picture
        self.flows = flows


class project:
    "A class for a metadesign project"
    
    def __init__(self, 
                 title = "project title", 
                 version = "0.1", 
                 founders = ["founder"],
                 license = "CC",
                 licenseurl = "http://",
                 businessmodel = businessmodel(),
                 steps = {0:step()}):
        
        self.title = title
        self.version = version
        self.founders = founders
        self.license = license
        self.licenseurl = licenseurl
        self.businessmodel = businessmodel
        self.steps = steps
    
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
            roles = etree.SubElement(step, "roles")
            roles.text = self.steps[n].roles
            picture = etree.SubElement(step, "picture")
            picture.text = self.steps[n].picture
            
            # build the flows
            flow = etree.SubElement(step, "flow")
            for m,k in enumerate(self.steps[n].flows):
                flownumber = etree.SubElement(flow, "number")
                flownumber.text = self.steps[n].flows[m].number
                flowtype = etree.SubElement(flow, "type")
                flowtype.text = self.steps[n].flows[m].type
                what = etree.SubElement(flow, "what")
                what.text = self.steps[n].flows[m].what
                direction = etree.SubElement(flow, "direction")
                direction.text = self.steps[n].flows[m].direction
                fromrole = etree.SubElement(flow, "from")
                fromrole.text = self.steps[n].flows[m].fromrole
                torole = etree.SubElement(flow, "to")
                torole.text = self.steps[n].flows[m].torole
            
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
            self.founders.append(i)
        self.license = doc.findtext("license")
        self.licenseurl = doc.findtext("licenseurl")
        
        # load business model
        self.businessmodel.valueproposition = doc.xpath("//project/businessmodel/valueproposition/text()")
        self.businessmodel.customerrelationships = doc.xpath("//project/businessmodel/customerrelationships/text()")
        self.businessmodel.channels = doc.xpath("//project/businessmodel/channels/text()")
        self.businessmodel.customersegments = doc.xpath("//project/businessmodel/customersegments/text()")
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
                elif l.tag == "roles":
                    self.steps[k].roles = l.text
                elif l.tag == "picture":
                    self.steps[k].picture = l.text
                elif l.tag == "flow":
                    flowelements = l.getchildren()
                    f = 0
                    for j in flowelements:
                        if j.tag == "number" and j.text == "0":
                            f = int(j.text)
                            self.steps[k].flows[f].number = j.text
                        elif j.tag == "number" and j.text != "0":
                            f = int(j.text)
                            self.steps[k].flows[f] = flow()
                            self.steps[k].flows[f].number = j.text
                        elif j.tag == "type":
                            self.steps[k].flows[f].type = j.text
                        elif j.tag == "what":
                            self.steps[k].flows[f].what = j.text
                        elif j.tag == "direction":
                            self.steps[k].flows[f].direction = j.text
                        elif j.tag == "from":
                            self.steps[k].flows[f].fromrole = j.text
                        elif j.tag == "to":
                            self.steps[k].flows[f].torole = j.text
                
        return

p = project()
print p.license
print p.businessmodel.channels
print p.steps[0].title
print p.steps[0].flows[0].what
#p.save("test.meta")
print ""

a = project()
a.title = "prova"
a.businessmodel.valueproposition = "X"
a.load("test.meta")
print a.title
print a.founders
print a.businessmodel.valueproposition
print a.steps[0].title
print a.steps[1].title
print a.steps[0].participation
print a.steps[1].participation

print a.steps[0].flows[0].type
print a.steps[1].flows[0].type
print a.steps[1].flows[1].type
print a.steps[1].flows[1].what
