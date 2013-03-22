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
                 type = "flow type", 
                 what = "none", 
                 direction = "direction"): 
        
        self.type = type
        self.what = what
        self.direction = direction       

class step():
    "A class for each step in the design process"
    def __init__(self, 
                 title = "step title", 
                 participation = "none", 
                 tools = "tools",
                 rules = "rules",
                 roles = "roles",
                 picture = "none",
                 flows = {0:flow()}): 
        
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
        # build the document before saving it
        
        title = etree.SubElement(project, "title")
        title.text = self.title
        version = etree.SubElement(project, "version")
        version.text = self.version
        for j in self.founders:
            founders = etree.SubElement(project, "founders")
            founders.text = j
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
        
        
        outFile = open(filename, 'w')
        doc.write(outFile,pretty_print=True)
        print "File saved successfully as",filename
        return
    
    def load(self,filename):
        loaded = project()
        doc = etree.parse(filename)
        # or etree.iterparse ?
        return loaded

p = project()
print p.license
print p.businessmodel.channels
print p.steps[0].title
print p.steps[0].flows[0].what
p.save("test.meta")