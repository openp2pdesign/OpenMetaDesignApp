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
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name=pagename)
        box = wx.BoxSizer()
        
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()


class WelcomePage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Welcome")
        box = wx.BoxSizer()
        
        #text3 = "text..."
        #lyrics3 = wx.StaticText(self, -1, text3)
        
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
        box = wx.BoxSizer()
        
        fgs = wx.FlexGridSizer(9, 1, 20, 0)
        
        licenses = ["Creative Commons - Attribution (CC BY)",
                    "Creative Commons - Attribution Share Alike (CC BY-SA)",
                    "Creative Commons - Attribution No Derivatives (CC BY-ND)",
                    "Creative Commons - Attribution Non-Commercial (CC BY-NC)", 
                    "Creative Commons - Attribution Non-Commercial Share Alike (CC BY-NC-SA)", 
                    "Creative Commons - Attribution Non-Commercial No Derivatives (CC BY-NC-ND)",
                    "Creative Commons - No Rights Reserved (CC0)"]

        label1 = wx.StaticText(self, label="Project title:")
        label2 = wx.StaticText(self, label="Version:")
        label3 = wx.StaticText(self, label="Founders:")
        label4 = wx.StaticText(self, label="License:")

        tc1 = wx.TextCtrl(self, size=(530,40), style=wx.TE_MULTILINE)
        tc2 = wx.TextCtrl(self, size=(530,40), style=wx.TE_MULTILINE)
        tc3 = wx.TextCtrl(self, size=(530,80), style=wx.TE_MULTILINE)
        tc4 = wx.Choice(self, -1, choices = licenses)
        
        self.Bind(wx.EVT_CHOICE, self.onChoice, tc4)

        fgs.AddMany([
                     (label1), 
                     (tc1, 1, wx.EXPAND), 
                     (label2), 
                     (tc2, 1, wx.EXPAND), 
                     (label3), 
                     (tc3, 1, wx.EXPAND),
                     (label4),
                     (tc4, 1, wx.EXPAND)
                     ])


        box.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()
    
    def onChoice(self, event):
        choice = event.GetString()
        print choice


class BusinessModelPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Business Model")
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


class CommunityPage(scrolled.ScrolledPanel):
    def __init__(self, parent):
        scrolled.ScrolledPanel.__init__(self, parent, -1,size=(570,400),name="Community Analysis")
        box = wx.BoxSizer()
        
        fgs = wx.FlexGridSizer(10, 1, 20, 0)

        label1 = wx.StaticText(self, label="Locality:")
        label2 = wx.StaticText(self, label="Activity:")
        label3 = wx.StaticText(self, label="Who is doing the activity:")
        label4 = wx.StaticText(self, label="The object of the activity:")
        label5 = wx.StaticText(self, label="The outcome of the activity:")
        label6 = wx.StaticText(self, label="The needs of the community:")
        label7 = wx.StaticText(self, label="The tools of the activity:")
        label8 = wx.StaticText(self, label="The rules of the activity:")
        label9 = wx.StaticText(self, label="The roles within the activity:")
        label10 = wx.StaticText(self, label="The larger context of the activity:")


        tc1 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc2 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc3 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc4 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc5 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc6 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc7 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc8 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc9 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        tc10 = wx.TextCtrl(self, size=(550,120), style=wx.TE_MULTILINE)
        

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
                     (tc9, 1, wx.EXPAND),
                     (label10),
                     (tc10, 1, wx.EXPAND)
                     ])


        box.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        self.SetSizer(box)
        self.SetAutoLayout(1)
        self.SetupScrolling()

        
        
        

class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = u"Open MetaDesign", size=(610, 400),style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
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
        page      = StepPage(self.nb, pageTitle)
        self.nb.AddPage(page, pageTitle)
        
        
        self.pageTitleCounter += 1

    def onStepRemove(self, event):   
        if self.pageCounter > 2:
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
