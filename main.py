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


        
class StepPage(scrolled.ScrolledPanel):
    def __init__(self, parent,pagename="Step"):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(550,400),name=pagename)
        box = wx.BoxSizer()        
        
        
        
class GeneralPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(550,400),name="General information")
        box = wx.BoxSizer()

        wx.StaticBox(self, -1, 'General Information', (5, 5), size=(550, 240))
        wx.CheckBox(self, -1 ,'Male', (15, 30))
        wx.CheckBox(self, -1 ,'Married', (15, 55))
        wx.StaticText(self, -1, 'Age', (15, 95))
        wx.SpinCtrl(self, -1, '1', (55, 90), (60, -1), min=1, max=120)
        wx.Button(self, 1, 'Ok', (90, 185), (60, -1))
        
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()

class BusinessModelPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Business model")
        box = wx.BoxSizer()
        
        fgs = wx.FlexGridSizer(9, 1, 20, 0)

        label1 = wx.StaticText(self, label="Value proposition:")
        label2 = wx.StaticText(self, label="Customer segments:")
        label3 = wx.StaticText(self, label="Customer relationships:")
        label4 = wx.StaticText(self, label="Channels:")
        label5 = wx.StaticText(self, label="Key partners:")
        label6 = wx.StaticText(self, label="Key activities:")
        label7 = wx.StaticText(self, label="Key resources:")
        label8 = wx.StaticText(self, label="Revenue stream:")
        label9 = wx.StaticText(self, label="Cost structure:")

        tc1 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc2 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc3 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc4 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc5 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc6 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc7 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc8 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc9 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        

        fgs.AddMany([
                     (label1), 
                     (tc1, 1, wx.EXPAND), 
                     (label2), 
                     (tc2, 1, wx.EXPAND), 
                     (label3), 
                     (tc3, 1, wx.EXPAND),
                     (label4),
                     (tc4, 1, wx.EXPAND),
                     (label5), 
                     (tc5, 1, wx.EXPAND),
                     (label6), 
                     (tc6, 1, wx.EXPAND),
                     (label7), 
                     (tc7, 1, wx.EXPAND),
                     (label8), 
                     (tc8, 1, wx.EXPAND),
                     (label9), 
                     (tc9, 1, wx.EXPAND)
                     ])


        box.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()

        
        
        

class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = u"Open MetaDesign", size=(600, 400),style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
        self.SetMinSize( self.GetSize() )
        
        self.currentDirectory = os.getcwd()

        pannel  = wx.Panel(self)
        vbox    = wx.BoxSizer(wx.VERTICAL)
        hbox    = wx.BoxSizer(wx.HORIZONTAL)    
        
        vbox.Add(hbox)

        self.Notebook3 = wx.Notebook(pannel)
        self.Notebook3.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED,self.onTabChanged)
        vbox.Add(self.Notebook3, 2, flag=wx.EXPAND)
        

        pannel.SetSizer(vbox)
        
        # Insert here the code from wxFormBuilder 
        
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
        
        
        
        # Initializing the notebook
        
        generalpage = GeneralPage(self.Notebook3)
        self.Notebook3.AddPage(generalpage, "General information")
        
        businesspage = BusinessModelPage(self.Notebook3)
        self.Notebook3.AddPage(businesspage, "Business model")

        self.pageCounter = 2
        self.pageTitleCounter = 1
        self.addNotebookPage()
        
        
    def onAbout(self,event):
        dlg = wx.MessageDialog( self, "An open source app for designing the process of an Open Design project.\nLicense: GPL v.3\nhttp://www.openmetadesign.org", "About Open MetaDesign v. 0.1", wx.OK)
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
        pageTitle = "Step: {0}".format(str(self.pageCounter-2))
        page      = StepPage(self.Notebook3, pageTitle)
        self.Notebook3.AddPage(page, pageTitle)
        self.pageTitleCounter += 1

    def onStepRemove(self, event):   
        if self.pageCounter > 2:
            self.Notebook3.DeletePage(self.pageTitleCounter)
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
