#Install wxWidgets FrameWork for windows-->pip install -U wxPython
#Install wxWidgets FrameWorks in unix Systems-->pip install -U \-f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \wxPython

import perc
import random as r
import wx
import sys


class Frame(wx.Frame):
    perceptrondata=[]
    def openfile(self,event):
        self.perceptrondata.clear()
        y=wx.FileDialog(None,"Get input perceptron",".")
        y.ShowModal()
        x=open(y.GetPath())
        for data in x:
            board=data.split(",")
            if len(board)!=4:
                continue
            a_data=perc.spot(board[0],board[1],board[2],board[3])
            self.perceptrondata.append(a_data)
        r.shuffle(self.perceptrondata)
    def __init__(self):
        self.bx=wx.BoxSizer(wx.VERTICAL)
        wx.Frame.__init__(self,None,wx.ID_ANY,"PERCEPTRON",wx.DefaultPosition,wx.Size(300,300))
        self.image=wx.StaticBitmap(self,wx.ID_ANY,wx.Bitmap("perceptron.png",wx.BITMAP_TYPE_ANY),wx.DefaultPosition,wx.Size(290,200))
        panel=wx.Panel(self,wx.ID_ANY)
        text=wx.StaticText(panel,wx.ID_ANY,"HANDLING FIELD",wx.DefaultPosition,wx.Size(70,30))
        text.SetForegroundColour(wx.Colour("#402835"))
        text.SetBackgroundColour(wx.Colour("#c4c235"))
        button=wx.Button(panel,wx.ID_ANY,"FILE",wx.DefaultPosition,wx.Size(50,30))
        self.pattern=wx.Button(panel,wx.ID_ANY,"Pattern",wx.DefaultPosition,wx.Size(50,30))
        self.vis=wx.Button(panel,wx.ID_ANY,"Visualize",wx.DefaultPosition,wx.Size(60,30))
        self.Bind(wx.EVT_BUTTON,self.patternshow,self.pattern)
        self.Bind(wx.EVT_BUTTON,self.visualize,self.vis)
        self.Bind(wx.EVT_BUTTON,self.openfile,button)
        gs=wx.GridSizer(0,4,3,3)
        gs.Add(text)
        gs.Add(button)
        gs.Add(self.pattern)
        gs.Add(self.vis)
        panel.SetSizer(gs)
        self.bx.Add(self.image)
        self.bx.Add(panel)
        self.SetSizer(self.bx)
    def patternshow(self,event):
        k="\tPerceptronData\n"
        for x in self.perceptrondata:
            k+=str(x.toStr())+"\n"
        wx.MessageBox(str(k),"Patterns find")
    def visualize(self,event):
        if len(self.perceptrondata)==0:
            wx.MessageBox("Please select a training set")
            return
        perc.start_perceptron(self.perceptrondata)


#Show the Gui for the Perceptron used
class app(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show(True)
        return True

app=app(None)
app.MainLoop()
