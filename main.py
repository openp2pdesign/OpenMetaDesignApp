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



class StepPage(wx.Panel):
    def __init__(self, parent,pagename="Step"):
        wx.Panel.__init__(self, parent, name=pagename)
        testo = "THIS IS A PAGE OBJECT n." + pagename
        t = wx.StaticText(self, -1, testo, (20,20))
        
class GeneralPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, name="General information")
        t = wx.StaticText(self, -1, "THIS IS A GENERAL PAGE OBJECT", (20,20))
        
class BusinessModelPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,name="Business model")
        t = wx.StaticText(self, -1, "THIS IS A BUSINESS PAGE OBJECT", (20,20))
        

class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = u"Open MetaDesign", size=(600, 400))
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
        currenttab = tab.GetName()
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
