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

import wx


def BuildDrawFrame(): # this gets called when needed, rather than on import
    try:
        from floatcanvas import NavCanvas, FloatCanvas, Resources
    except ImportError: # if it's not there locally, try the wxPython lib.
        from wx.lib.floatcanvas import NavCanvas, FloatCanvas, Resources

    class DrawFrame(wx.Frame):
        def __init__(self,parent, id,title,position,size):
            wx.Frame.__init__(self,parent, id,title,position, size)

            MenuBar = wx.MenuBar()

            file_menu = wx.Menu()
            item = file_menu.Append(-1, "&SavePNG","Save the current image as a PNG")
            self.Bind(wx.EVT_MENU, self.OnSavePNG, item)
            item = file_menu.Append(-1, "&Close","Close this frame")
            self.Bind(wx.EVT_MENU, self.OnQuit, item)
            MenuBar.Append(file_menu, "&File")

            view_menu = wx.Menu()
            item = view_menu.Append(-1, "Zoom to &Fit","Zoom to fit the window")
            self.Bind(wx.EVT_MENU, self.ZoomToFit, item)
            MenuBar.Append(view_menu, "&View")

            self.SetMenuBar(MenuBar)
            
            self.CreateStatusBar()

            
            # Add the Canvas
            NC = NavCanvas.NavCanvas(self,
                                     Debug = 0,
                                     BackgroundColor = "GREY")

            self.Canvas = NC.Canvas 

            ##Create a sizer to manage the Canvas and message window
            MainSizer = wx.BoxSizer(wx.VERTICAL)
            MainSizer.Add(NC, 4, wx.EXPAND)
            
            self.SetSizer(MainSizer)
            self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

            self.Canvas.Bind(FloatCanvas.EVT_MOTION, self.OnMove) 
            self.Canvas.Bind(FloatCanvas.EVT_MOUSEWHEEL, self.OnWheel) 
            self.EventsAreBound = False

            return None
        

        def OnSavePNG(self, event=None):
            import os
            dlg = wx.FileDialog(
                self, message="Save file as ...", defaultDir=os.getcwd(), 
                defaultFile="", wildcard="*.png", style=wx.SAVE
                )
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                if not(path[-4:].lower() == ".png"):
                    path = path+".png"
                self.Canvas.SaveAsImage(path)

        def OnWheel(self, event):
            Rot = event.GetWheelRotation()
            Rot = Rot / abs(Rot) * 0.1
            if event.ControlDown(): # move left-right
                self.Canvas.MoveImage( (Rot, 0), "Panel" )
            else: # move up-down
                self.Canvas.MoveImage( (0, Rot), "Panel" )
                
        def OnMove(self, event):
            self.SetStatusText("%.2f, %.2f"%tuple(event.Coords))
            event.Skip()

        def ZoomToFit(self,event):
            self.Canvas.ZoomToBB()

        def Clear(self,event = None):
            self.Canvas.InitAll()
            self.Canvas.Draw()

        def OnQuit(self,event):
            self.Close(True)

        def OnCloseWindow(self, event):
            self.Destroy()

        def ShowFrame(self):
            Object = self.MovingObject
            Range = self.Range
            if  self.TimeStep < self.NumTimeSteps:
                x,y = Object.XY
                if x > Range[1] or x < Range[0]:
                    self.dx = -self.dx
                if y > Range[1] or y < Range[0]:
                    self.dy = -self.dy
                Object.Move( (self.dx,self.dy) )
                Object.Text.Move( (self.dx,self.dy))
                self.Canvas.Draw()
                self.TimeStep += 1
                wx.GetApp().Yield(True)
            else:
                self.Timer.Stop()

        def LoadBitmap(self, path, event= None):
            wx.GetApp().Yield(True)
            Canvas = self.Canvas
            Canvas.InitAll()
            self.bmp = wx.Bitmap(path, wx.BITMAP_TYPE_PNG)
            sb = FloatCanvas.ScaledBitmap2(self.bmp, (0,0), 1, Position="tl")
            self.Canvas.AddObject(sb)
            self.Canvas.ZoomToBB()
            
    return DrawFrame 

class ImageViewerApp(wx.App):
    def __init__(self, imagePath, windowTitle):
        wx.App.__init__(self)
        #wx.InitAllImageHandlers()
        DrawFrame = BuildDrawFrame()
        frame = DrawFrame(None, -1, windowTitle,wx.DefaultPosition,(700,700))
    
        self.SetTopWindow(frame)
        frame.Show()
        frame.LoadBitmap(imagePath)
        
        return

      
if __name__ == "__main__":
    pass