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


import os
import wx
import wx.lib.mixins.inspection
import wx.lib.scrolledpanel as scrolled
from classes import *

temp = project()
currentFile = ""


class FlowTab(wx.Panel):
    def __init__(self, parent,pagename="Flow"):
        wx.Panel.__init__(self, parent)
        box = wx.BoxSizer(wx.VERTICAL)
        
        self.flowtype = ["Financial flow",
                   "Physical resources flow",
                   "Information flow"]
        
        label1 = wx.StaticText(self, label="Flow type:")
        box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.Choice(self, -1, choices = self.flowtype)
        self.Bind(wx.EVT_CHOICE, self.onChoice, self.tc1)
        box.Add(self.tc1, flag=wx.ALL, border=10)
        label2 = wx.StaticText(self, label="What does flow?")
        box.Add(label2, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc2 = wx.TextCtrl(self, size=(530,20), style=wx.TE_MULTILINE)
        box.Add(self.tc2, flag=wx.ALL|wx.EXPAND, border=10)
        label3 = wx.StaticText(self, label="First actor of the flow:")
        box.Add(label3, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc3 = wx.TextCtrl(self, size=(530,20), style=wx.TE_MULTILINE)
        box.Add(self.tc3, flag=wx.ALL|wx.EXPAND, border=10)
        label4 = wx.StaticText(self, label="Second actor of the flow:")
        box.Add(label4, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc4 = wx.TextCtrl(self, size=(530,20), style=wx.TE_MULTILINE)
        box.Add(self.tc4, flag=wx.ALL|wx.EXPAND, border=10)
        
        self.flowdirection = ["Both directions",
                         "From the first actor to the second one",
                         "From the second actor to the first one"]
        
        label5 = wx.StaticText(self, label="Direction of the flow:")
        box.Add(label5, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc5 = wx.Choice(self, -1, choices = self.flowdirection)
        self.Bind(wx.EVT_CHOICE, self.onChoice2, self.tc5)
        box.Add(self.tc5, flag=wx.ALL, border=10)
        
        self.SetSizer(box)
        
    def onChoice(self, event):
        choice = event.GetString()
        print choice
        
    def onChoice2(self, event):
        choice = event.GetString()
        print choice

        
class StepPage(scrolled.ScrolledPanel):
    def __init__(self, parent,pagename="Step"):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name=pagename)
        self.panel = wx.Panel(self, -1)
        self.box = wx.BoxSizer(wx.VERTICAL)
        
        self.participationlevels = ["None",
                              "Indirect",
                              "Consultative",
                              "Shared control", 
                              "Full control"]
        
        label1 = wx.StaticText(self, label="The title of this step in the design process:")
        self.box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.TextCtrl(self, size=(530,20), style=wx.TE_MULTILINE)
        self.box.Add(self.tc1, flag=wx.ALL|wx.EXPAND, border=10)
        label2 = wx.StaticText(self, label="Participation of the community in the Open Design process:")
        self.box.Add(label2, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc2 = wx.Choice(self, -1, choices = self.participationlevels)
        self.Bind(wx.EVT_CHOICE, self.onChoice, self.tc2)
        self.box.Add(self.tc2, flag=wx.ALL, border=10)
        label3 = wx.StaticText(self, label="Tools used in this step of the Open Design process:")
        self.box.Add(label3, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc3 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        self.box.Add(self.tc3, flag=wx.ALL|wx.EXPAND, border=10)
        label4 = wx.StaticText(self, label="Rules in use in this step of the Open Design process:")
        self.box.Add(label4, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc4 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        self.box.Add(self.tc4, flag=wx.ALL|wx.EXPAND, border=10)
        label5 = wx.StaticText(self, label="Roles of this step of the Open Design process:")
        self.box.Add(label5, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc5 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        self.box.Add(self.tc5, flag=wx.ALL|wx.EXPAND, border=10)
        
        
        
        buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.flowsnumber = 1
        self.flowmessage = "Number of flows in the step: " + str(self.flowsnumber)
        self.label6 = wx.StaticText(self, label=self.flowmessage)
        buttons.Add(self.label6, flag=wx.ALL|wx.EXPAND, border=10)
        addflow = wx.Button(self, 20, "Add a flow")
        buttons.Add(addflow, flag=wx.ALL, border=10)
        addflow.Bind(wx.EVT_BUTTON, self.onAddFlow, addflow)
        
        removeflow = wx.Button(self, 20, "Remove a flow")
        buttons.Add(removeflow, flag=wx.ALL, border=10)
        removeflow.Bind(wx.EVT_BUTTON, self.onRemoveFlow, removeflow)
        
        self.box.Add(buttons,flag=wx.ALL|wx.EXPAND, border=10)
        
        self.tabs = {}
        self.nestednb = wx.Notebook(self)
        self.tab = FlowTab(self.nestednb)
        self.tabs[0] = self.tab
        self.nestednb.AddPage(self.tab, "Flow n. 1") 
        self.box.Add(self.nestednb,2,wx.EXPAND, border=10)
        
        self.SetSizer(self.box)
        self.SetAutoLayout(1)
        self.SetupScrolling()
    
    def onChoice(self, event):
        choice = event.GetString()
        print choice
        
    def onRemoveFlow(self, event):
        del self.tabs[self.flowsnumber]
        self.flowsnumber -= 1
        self.flowmessage = "Number of flows in the step: " + str(self.flowsnumber)
        self.label6.SetLabel(self.flowmessage)
        self.nestednb.DeletePage(self.flowsnumber)
        
    def onAddFlow(self, event):
        self.flowsnumber += 1
        self.flowmessage = "Number of flows in the step: " + str(self.flowsnumber)
        self.label6.SetLabel(self.flowmessage)
        tab = FlowTab(self.nestednb)
        self.nestednb.AddPage(tab, "Flow n. " + str(self.flowsnumber)) 
        self.tabs[self.flowsnumber] = tab


class WelcomePage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Welcome")
        box = wx.BoxSizer(wx.VERTICAL)
        
        self.bitmap = wx.Bitmap('images/welcome.png')
        wx.EVT_PAINT(self, self.OnPaint)

        
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()
        
    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 60, 20)

        
class GeneralPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="General Information")
        box = wx.BoxSizer(wx.VERTICAL)
        
        self.licenses = ["Creative Commons - Attribution (CC BY)",
                    "Creative Commons - Attribution Share Alike (CC BY-SA)",
                    "Creative Commons - Attribution No Derivatives (CC BY-ND)",
                    "Creative Commons - Attribution Non-Commercial (CC BY-NC)", 
                    "Creative Commons - Attribution Non-Commercial Share Alike (CC BY-NC-SA)", 
                    "Creative Commons - Attribution Non-Commercial No Derivatives (CC BY-NC-ND)",
                    "Creative Commons - No Rights Reserved (CC0)"]

        label1 = wx.StaticText(self, label="The title of the Open Design project:")
        box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.TextCtrl(self, size=(530,40), style=wx.TE_MULTILINE)
        box.Add(self.tc1, flag=wx.ALL|wx.EXPAND, border=10)
        label2 = wx.StaticText(self, label="Version of the Open Design project:")
        box.Add(label2, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc2 = wx.TextCtrl(self, size=(530,20), style=wx.TE_MULTILINE)
        box.Add(self.tc2, flag=wx.ALL|wx.EXPAND, border=10)
        label3 = wx.StaticText(self, label="Founders of the Open Design project:")
        box.Add(label3, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc3 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        box.Add(self.tc3, flag=wx.ALL|wx.EXPAND, border=10)
        label4 = wx.StaticText(self, label="License of the Open Design process (not the project!):")
        box.Add(label4, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc4 = wx.Choice(self, -1, choices = self.licenses)
        box.Add(self.tc4, flag=wx.ALL|wx.EXPAND, border=10)
        
        self.Bind(wx.EVT_CHOICE, self.onChoice, self.tc4)
        
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()
    
    def onChoice(self, event):
        choice = event.GetString()
        temp.license = choice


class BusinessModelPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Business Model")
        box = wx.BoxSizer(wx.VERTICAL)
        
        label1 = wx.StaticText(self, label="Value proposition:")
        box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc1, flag=wx.ALL|wx.EXPAND, border=10)
        label2 = wx.StaticText(self, label="Customer segments:")
        box.Add(label2, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc2 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc2, flag=wx.ALL|wx.EXPAND, border=10)
        label3 = wx.StaticText(self, label="Customer relationships:")
        box.Add(label3, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc3 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc3, flag=wx.ALL|wx.EXPAND, border=10)
        label4 = wx.StaticText(self, label="Channels:")
        box.Add(label4, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc4 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc4, flag=wx.ALL|wx.EXPAND, border=10)
        label5 = wx.StaticText(self, label="Key partners:")
        box.Add(label5, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc5 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc5, flag=wx.ALL|wx.EXPAND, border=10)
        label6 = wx.StaticText(self, label="Key activities:")
        box.Add(label6, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc6 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc6, flag=wx.ALL|wx.EXPAND, border=10)
        label7 = wx.StaticText(self, label="Key resources:")
        box.Add(label7, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc7 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc7, flag=wx.ALL|wx.EXPAND, border=10)
        label8 = wx.StaticText(self, label="Revenue stream:")
        box.Add(label8, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc8 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc8, flag=wx.ALL|wx.EXPAND, border=10)
        label9 = wx.StaticText(self, label="Cost structure:")
        box.Add(label9, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc9 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc9, flag=wx.ALL|wx.EXPAND, border=10)


        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()


class CommunityPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Community Analysis")
        box = wx.BoxSizer(wx.VERTICAL)

        label1 = wx.StaticText(self, label="The locality of the community:")
        box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc1, flag=wx.ALL|wx.EXPAND, border=10)
        label2 = wx.StaticText(self, label="The main activity of the community:")
        box.Add(label2, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc2 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc2, flag=wx.ALL|wx.EXPAND, border=10)
        label3 = wx.StaticText(self, label="Who is doing the activity:")
        box.Add(label3, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc3 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc3, flag=wx.ALL|wx.EXPAND, border=10)
        label4 = wx.StaticText(self, label="The object of the activity:")
        box.Add(label4, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc4 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc4, flag=wx.ALL|wx.EXPAND, border=10)
        label5 = wx.StaticText(self, label="The outcome of the activity:")
        box.Add(label5, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc5 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc5, flag=wx.ALL|wx.EXPAND, border=10)
        label6 = wx.StaticText(self, label="The needs of the community:")
        box.Add(label6, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc6 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc6, flag=wx.ALL|wx.EXPAND, border=10)
        label7 = wx.StaticText(self, label="The tools of the activity:")
        box.Add(label7, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc7 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc7, flag=wx.ALL|wx.EXPAND, border=10)
        label8 = wx.StaticText(self, label="The rules of the activity:")
        box.Add(label8, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc8 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc8, flag=wx.ALL|wx.EXPAND, border=10)
        label9 = wx.StaticText(self, label="The roles within the activity:")
        box.Add(label9, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc9 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc9, flag=wx.ALL|wx.EXPAND, border=10)
        label10 = wx.StaticText(self, label="The larger context of the activity:")
        box.Add(label10, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc10 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc10, flag=wx.ALL|wx.EXPAND, border=10)
       
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()

        
        
        

class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = u"Open MetaDesign", size=(620, 400))
        self.SetMinSize( self.GetSize() )
        
        self.currentDirectory = os.getcwd()

        pannel  = wx.Panel(self)
        vbox    = wx.BoxSizer(wx.VERTICAL)
        
        # Initializing the notebook
        self.pages = {}
        self.pageCounter = 3
        self.pageTitleCounter = 1          
        self.nb = wx.Notebook(pannel, -1)
        self.page0 = WelcomePage(self.nb)
        self.pages[0] = self.page0
        self.page1 = GeneralPage(self.nb)
        self.pages[1] = self.page1
        self.page2 = CommunityPage(self.nb)
        self.pages[2] = self.page2
        self.page3 = BusinessModelPage(self.nb)
        self.pages[3] = self.page3
        self.nb.AddPage(self.page0, "Welcome!") 
        self.nb.AddPage(self.page1, "General Information")
        self.nb.AddPage(self.page2, "Community Analysis")
        self.nb.AddPage(self.page3, "Business Model")
        self.addNotebookPage()
        self.nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED,self.onTabChanged)
        
        vbox.Add(self.nb, 2, flag=wx.EXPAND)

        pannel.SetSizer(vbox)
        
        # Initializing the Menu
        
        self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem1 )
        self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem2 )
        self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem3 )
        self.m_menuItem4 = wx.MenuItem( self.m_menu1, 12, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.AppendItem( self.m_menuItem4 )
        self.m_menubar1.Append( self.m_menu1, u"File" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menu2, 13, u"Add a step in the Open Design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem5 )
        self.m_menuItem6 = wx.MenuItem( self.m_menu2, 14, u"Remove the current step from the Open Design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem6 )
        self.m_menubar1.Append( self.m_menu2, u"Edit" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the participation in the Open Design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem7 )
        self.m_menuItem9 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the business model of the Open Design project and process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem9 )
        self.m_menuItem11 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the System Map of the Open Design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem11 )
        self.m_menuItem8 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the interactions in the Open Design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem8 )
        self.m_menuItem12 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the whole canvas of the Open Design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem12 )
        self.m_menubar1.Append( self.m_menu3, u"View" ) 
        
        self.m_menu4 = wx.Menu()
        self.m_menuItem10 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu4.AppendItem( self.m_menuItem10 )
        self.m_menubar1.Append( self.m_menu4, u"Help" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        

        
        # Set events for the Menu
        
        self.Bind(wx.EVT_MENU, self.onOpenFile, self.m_menuItem1)
        self.Bind(wx.EVT_MENU, self.onSaveFile, self.m_menuItem2)
        self.Bind(wx.EVT_MENU, self.onSaveFileAs, self.m_menuItem3)
        self.Bind(wx.EVT_MENU, self.onQuit, self.m_menuItem4)
        self.Bind(wx.EVT_MENU, self.onStepInsert, self.m_menuItem5)
        self.Bind(wx.EVT_MENU, self.onStepRemove, self.m_menuItem6)
        self.Bind(wx.EVT_MENU, self.onAbout, self.m_menuItem10)
                
        
    def onAbout(self,event):
        dlg = wx.MessageDialog( self, "An open source app for designing the process of an Open Design project.\nLicense: GPL v.3\nhttp://www.openmetadesign.org", "About Open MetaDesign v. 0.1", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def onOpenFile(self, event):
        dlg = wx.FileDialog(self, message="Choose a file",defaultDir=self.currentDirectory, defaultFile="",wildcard="*.meta",style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
        
        # Load the project in the current file
        temp.load(paths[0])
        global currentFile
        currentFile = paths[0]
        
        # Update the values in the GUI
        self.page1.tc1.SetValue(temp.title)
        self.page1.tc2.SetValue(temp.version) 
        self.page1.tc3.SetValue(", ".join(temp.founders))
        self.page1.tc4.SetStringSelection(temp.license)
        
        self.page2.tc1.SetValue(temp.community.locality[0])
        self.page2.tc2.SetValue(temp.community.activity[0])
        self.page2.tc3.SetValue(temp.community.subject[0])
        self.page2.tc4.SetValue(temp.community.object[0])
        self.page2.tc5.SetValue(temp.community.outcome[0])
        self.page2.tc6.SetValue(temp.community.needs[0])
        self.page2.tc7.SetValue(temp.community.tools[0])
        self.page2.tc8.SetValue(temp.community.rules[0])
        self.page2.tc9.SetValue(temp.community.roles[0])
        self.page2.tc10.SetValue(temp.community.context[0])
        
        self.page3.tc1.SetValue(temp.businessmodel.valueproposition[0])
        self.page3.tc2.SetValue(temp.businessmodel.customersegments[0])
        self.page3.tc3.SetValue(temp.businessmodel.customerrelationships[0])
        self.page3.tc4.SetValue(temp.businessmodel.channels[0])
        self.page3.tc5.SetValue(temp.businessmodel.keypartners[0])
        self.page3.tc6.SetValue(temp.businessmodel.keyactivities[0])
        self.page3.tc7.SetValue(temp.businessmodel.keyresources[0])
        self.page3.tc8.SetValue(temp.businessmodel.revenuestreams[0])
        self.page3.tc9.SetValue(temp.businessmodel.coststructure[0])
        
        for j,i in enumerate(range(4,self.pageCounter+1)): 
            self.pages[i].tc1.SetValue(temp.steps[j].title)
            self.pages[i].tc2.SetStringSelection(temp.steps[j].participation)
            self.pages[i].tc3.SetValue(temp.steps[j].tools)
            self.pages[i].tc4.SetValue(temp.steps[j].rules)
            self.pages[i].tc5.SetValue(temp.steps[j].roles)
            
            for k in range(self.pages[i].flowsnumber):
                self.pages[i].tabs[k].tc1.SetStringSelection(temp.steps[j].flows[k].type)
                self.pages[i].tabs[k].tc2.SetValue(temp.steps[j].flows[k].what)
                self.pages[i].tabs[k].tc3.SetValue(temp.steps[j].flows[k].fromrole)
                self.pages[i].tabs[k].tc4.SetValue(temp.steps[j].flows[k].torole)
                self.pages[i].tabs[k].tc5.SetStringSelection(temp.steps[j].flows[k].direction)
        
        self.statusBar.SetStatusText("Loaded successfully file "+currentFile)
    
        dlg.Destroy()
        
    def SaveFile(self):
        # Load the current values for General information
        temp.title = self.page1.tc1.GetValue()
        temp.version = self.page1.tc2.GetValue()
        
        temp.founders = [x.strip() for x in self.page1.tc3.GetValue().split(',')]
        temp.license = self.page1.licenses[self.page1.tc4.GetCurrentSelection()]
        
        # Add automatically url of license
        if temp.license == "Creative Commons - Attribution (CC BY)":
            temp.licenseurl = "http://creativecommons.org/licenses/by/3.0/"
        elif temp.license == "Creative Commons - Attribution Share Alike (CC BY-SA)":
            temp.licenseurl = "http://creativecommons.org/licenses/by-sa/3.0"
        elif temp.license == "Creative Commons - Attribution No Derivatives (CC BY-ND)":
            temp.licenseurl = "http://creativecommons.org/licenses/by-nd/3.0"
        elif temp.license == "Creative Commons - Attribution Non-Commercial (CC BY-NC)":
            temp.licenseurl = "http://creativecommons.org/licenses/by-nc/3.0"
        elif temp.license == "Creative Commons - Attribution Non-Commercial Share Alike (CC BY-NC-SA)":
            temp.licenseurl = "http://creativecommons.org/licenses/by-nc-sa/3.0"
        elif temp.license == "Creative Commons - Attribution Non-Commercial No Derivatives (CC BY-NC-ND)":
            temp.licenseurl = "http://creativecommons.org/licenses/by-nc-nd/3.0"
        elif temp.license == "Creative Commons - No Rights Reserved (CC0)":
            temp.licenseurl = "http://creativecommons.org/publicdomain/zero/1.0/"
         
        
        # Load the current values for Community analysis
        temp.community.locality = self.page2.tc1.GetValue()
        temp.community.activity = self.page2.tc2.GetValue()
        temp.community.subject = self.page2.tc3.GetValue()
        temp.community.object = self.page2.tc4.GetValue()
        temp.community.outcome = self.page2.tc5.GetValue()
        temp.community.needs = self.page2.tc6.GetValue()
        temp.community.tools = self.page2.tc7.GetValue()
        temp.community.rules = self.page2.tc8.GetValue()
        temp.community.roles = self.page2.tc9.GetValue()
        temp.community.context = self.page2.tc10.GetValue()
        
        # Load the current values for Business model
        temp.businessmodel.valueproposition = self.page3.tc1.GetValue()
        temp.businessmodel.customersegments = self.page3.tc2.GetValue()
        temp.businessmodel.customerrelationships = self.page3.tc3.GetValue()
        temp.businessmodel.channels = self.page3.tc4.GetValue()
        temp.businessmodel.keypartners = self.page3.tc5.GetValue()
        temp.businessmodel.keyactivities =  self.page3.tc6.GetValue()
        temp.businessmodel.keyresources = self.page3.tc7.GetValue()
        temp.businessmodel.revenuestreams = self.page3.tc8.GetValue()
        temp.businessmodel.coststructure = self.page3.tc9.GetValue()
        
        # Load the current values for the Steps
        for j,i in enumerate(range(4,self.pageCounter+1)):
            temp.steps[j] = step()
            temp.steps[j].stepnumber = j 
            temp.steps[j].title = self.pages[i].tc1.GetValue()
            temp.steps[j].participation = self.pages[i].participationlevels[self.pages[i].tc2.GetSelection()]
            temp.steps[j].tools = self.pages[i].tc3.GetValue()
            temp.steps[j].rules = self.pages[i].tc4.GetValue()
            temp.steps[j].roles = self.pages[i].tc5.GetValue()
            
            # Load the current values for the Flows
            for k in range(self.pages[i].flowsnumber):
                temp.steps[j].flows[k] = flow()
                temp.steps[j].flows[k].type = self.pages[i].tabs[k].flowtype[self.pages[i].tabs[k].tc1.GetSelection()]
                temp.steps[j].flows[k].what = self.pages[i].tabs[k].tc2.GetValue()
                temp.steps[j].flows[k].fromrole = self.pages[i].tabs[k].tc3.GetValue()
                temp.steps[j].flows[k].torole = self.pages[i].tabs[k].tc4.GetValue()
                temp.steps[j].flows[k].direction = self.pages[i].tabs[k].flowdirection[self.pages[i].tabs[k].tc5.GetSelection()]

        
    def onSaveFile(self,event):
        
        # Load temporary project
        self.SaveFile()
        
        # Save file
        global currentFile
        temp.save(currentFile)
        self.statusBar.SetStatusText("Saved successfully file "+currentFile)
        
            
    def onSaveFileAs(self, event):
        
        dlg = wx.FileDialog(self, message="Save file as ...", defaultDir=self.currentDirectory, defaultFile="", wildcard="*.meta", style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            
        # Load temporary project
        self.SaveFile()
            
        # Save file
        global currentFile
        temp.save(path)
        currentFile = path
        self.statusBar.SetStatusText("Saved successfully file "+currentFile)
            
        dlg.Destroy()
        
    def onTabChanged(self,event):
        tab = event.EventObject.GetChildren()[event.Selection]
        currentTab = tab.GetName()
        event.Skip()     
    
    def onQuit(self, event):
        self.Close()

    def addNotebookPage(self):
        self.pageCounter += 1
        pageTitle = "Step: {0}".format(str(self.pageCounter-3))
        page = StepPage(self.nb, pageTitle)
        self.nb.AddPage(page, pageTitle)
        self.pages[self.pageCounter] = page
        self.pageTitleCounter += 1

    def onStepRemove(self, event):  
        if self.nb.GetSelection() > 4:
            self.nb.DeletePage(self.nb.GetSelection())
            del self.pages[self.pageCounter]
            self.pageTitleCounter -= 1
            self.pageCounter -= 1
        else:
            pass

    def onStepInsert(self, event):   
        self.addNotebookPage()

class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def OnInit(self):
        self.Init()
        frame = Main()
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == "__main__":
    
    app = MyApp(redirect=False)
    app.MainLoop()
