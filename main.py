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


class FlowTab(wx.Panel):
    def __init__(self, parent,pagename="Flow"):
        wx.Panel.__init__(self, parent)
        box = wx.BoxSizer(wx.VERTICAL)
        
        flowtype = ["Financial flow",
                   "Physical resources flow",
                   "Information flow"]
        
        label1 = wx.StaticText(self, label="Flow type:")
        box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.Choice(self, -1, choices = flowtype)
        self.Bind(wx.EVT_CHOICE, self.onChoice, tc1)
        box.Add(tc1, flag=wx.ALL, border=10)
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
        
        flowdirection = ["Both directions",
                         "From the first actor to the second one",
                         "From the second actor to the first one"]
        
        label5 = wx.StaticText(self, label="Direction of the flow:")
        box.Add(label5, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc5 = wx.Choice(self, -1, choices = flowdirection)
        self.Bind(wx.EVT_CHOICE, self.onChoice2, tc5)
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
        
        participationlevels = ["None",
                              "Indirect",
                              "Consultative",
                              "Shared control", 
                              "Full control"]
        
        label1 = wx.StaticText(self, label="Step title:")
        self.box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.TextCtrl(self, size=(530,20), style=wx.TE_MULTILINE)
        self.box.Add(self.tc1, flag=wx.ALL|wx.EXPAND, border=10)
        label2 = wx.StaticText(self, label="Participation of the Open Design community:")
        self.box.Add(label2, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc2 = wx.Choice(self, -1, choices = participationlevels)
        self.Bind(wx.EVT_CHOICE, self.onChoice, tc2)
        self.box.Add(self.tc2, flag=wx.ALL, border=10)
        label3 = wx.StaticText(self, label="Tools:")
        self.box.Add(label3, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc3 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        self.box.Add(self.tc3, flag=wx.ALL|wx.EXPAND, border=10)
        label4 = wx.StaticText(self, label="Rules:")
        self.box.Add(label4, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc4 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        self.box.Add(self.tc4, flag=wx.ALL|wx.EXPAND, border=10)
        label5 = wx.StaticText(self, label="Roles:")
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
        
        self.nestednb = wx.Notebook(self)
        self.tab = FlowTab(self.nestednb)
        self.nestednb.AddPage(self.tab, "Flow n. 1") 
        self.box.Add(self.nestednb,2,wx.EXPAND, border=10)
        
        self.SetSizer(self.box)
        self.SetAutoLayout(1)
        self.SetupScrolling()
    
    def onChoice(self, event):
        choice = event.GetString()
        print choice
        
    def onRemoveFlow(self, event):
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


class WelcomePage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Welcome")
        box = wx.BoxSizer(wx.VERTICAL)
        
        self.bitmap = wx.Bitmap('images/openmetadesign.png')
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
        
        licenses = ["Creative Commons - Attribution (CC BY)",
                    "Creative Commons - Attribution Share Alike (CC BY-SA)",
                    "Creative Commons - Attribution No Derivatives (CC BY-ND)",
                    "Creative Commons - Attribution Non-Commercial (CC BY-NC)", 
                    "Creative Commons - Attribution Non-Commercial Share Alike (CC BY-NC-SA)", 
                    "Creative Commons - Attribution Non-Commercial No Derivatives (CC BY-NC-ND)",
                    "Creative Commons - No Rights Reserved (CC0)"]

        label1 = wx.StaticText(self, label="Project title:")
        box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.TextCtrl(self, size=(530,40), style=wx.TE_MULTILINE)
        box.Add(self.tc1, flag=wx.ALL|wx.EXPAND, border=10)
        label2 = wx.StaticText(self, label="Version:")
        box.Add(label2, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc2 = wx.TextCtrl(self, size=(530,20), style=wx.TE_MULTILINE)
        box.Add(self.tc2, flag=wx.ALL|wx.EXPAND, border=10)
        label3 = wx.StaticText(self, label="Founders:")
        box.Add(label3, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc3 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        box.Add(self.tc3, flag=wx.ALL|wx.EXPAND, border=10)
        label4 = wx.StaticText(self, label="License:")
        box.Add(label4, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc4 = wx.Choice(self, -1, choices = licenses)
        box.Add(self.tc4, flag=wx.ALL|wx.EXPAND, border=10)
        
        self.Bind(wx.EVT_CHOICE, self.onChoice, tc4)
        
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()
    
    def onChoice(self, event):
        choice = event.GetString()
        print choice


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

        label1 = wx.StaticText(self, label="Locality:")
        box.Add(label1, flag=wx.ALL|wx.EXPAND, border=10)
        self.tc1 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        box.Add(self.tc1, flag=wx.ALL|wx.EXPAND, border=10)
        label2 = wx.StaticText(self, label="Activity:")
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
        self.pageCounter = 3
        self.pageTitleCounter = 1          
        self.nb = wx.Notebook(pannel, -1)
        self.page0 = WelcomePage(self.nb)
        self.page1 = GeneralPage(self.nb)
        self.page2 = CommunityPage(self.nb)
        self.page3 = BusinessModelPage(self.nb)
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
        self.m_menuItem5 = wx.MenuItem( self.m_menu2, 13, u"Add a step in the design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem5 )
        self.m_menuItem6 = wx.MenuItem( self.m_menu2, 14, u"Remove the current step from the design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu2.AppendItem( self.m_menuItem6 )
        self.m_menubar1.Append( self.m_menu2, u"Edit" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the participation in the design process", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem7 )
        self.m_menuItem9 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the business model", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem9 )
        self.m_menuItem11 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the System Map", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem11 )
        self.m_menuItem8 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the interactions in the project", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu3.AppendItem( self.m_menuItem8 )
        self.m_menuItem12 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"View the whole canvas", wx.EmptyString, wx.ITEM_NORMAL )
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
        print self.page3.tc1.GetValue()
        dlg.ShowModal()
        dlg.Destroy()
        
    def onOpenFile(self, event):
        dlg = wx.FileDialog(self, message="Choose a file",defaultDir=self.currentDirectory, defaultFile="",wildcard="*.meta",style=wx.OPEN | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            
        # Here save the file
            
        dlg.Destroy()
        
    def onSaveFile(self):
        
        # Here save the current opened file
        
        pass
        
    def onSaveFileAs(self, event):
        dlg = wx.FileDialog(self, message="Save file as ...", defaultDir=self.currentDirectory, defaultFile="", wildcard="*.meta", style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            
            # Here add the code for saving the file
            
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
        page      = StepPage(self.nb, pageTitle)
        self.nb.AddPage(page, pageTitle)
        self.pageTitleCounter += 1

    def onStepRemove(self, event):   
        if self.pageCounter > 4:
            self.nb.DeletePage(self.pageTitleCounter)
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
