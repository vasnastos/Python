#Install wxWidgets FrameWork for windows-->pip install -U wxPython
#Install wxWidgets FrameWorks in unix Systems-->pip install -U \-f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \wxPython

import pages as ps
import perc
import random as r
import wx
import sys

algos=[]
algos.append("WEIGHT_CHANGER")
algos.append("EUCLEIDIAN")

class Frame(wx.Frame):
    perceptrondata=[]
    def menu_selection(self):
       men=wx.Menu()
       bar=wx.MenuBar()
       men.Append(101,"OPEN",)
       men.Append(102,"EXPORT")
       men.Append(103,"EXIT")
       self.Bind(wx.EVT_MENU,self.openfile,None,id=101)
       self.Bind(wx.EVT_MENU,self.export,None,id=102)
       self.Bind(wx.EVT_MENU,self.close,None,id=103)
       bar.Append(men,"OPTIONS")
       self.SetMenuBar(bar)
       self.SetIcon(wx.Icon("central.png",wx.BITMAP_TYPE_PNG))
    def openfile(self,event):
        self.perceptrondata.clear()
        y=wx.FileDialog(None,"Get input perceptron",".")
        if y.ShowModal()==wx.ID_CANCEL:
            return
        x=open(y.GetPath())
        for data in x:
            board=data.split(",")
            if len(board)!=4:
                continue
            a_data=perc.spot(board[0],board[1],board[2],board[3])
            self.perceptrondata.append(a_data)
        r.shuffle(self.perceptrondata)
    def __init__(self):
        self.bx=wx.GridSizer(0,1,300,200)
        wx.Frame.__init__(self,None,wx.ID_ANY,"PERCEPTRON",wx.DefaultPosition,wx.Size(650,450))
        self.image=wx.StaticBitmap(self,wx.EXPAND,wx.Bitmap("perceptron.png",wx.BITMAP_TYPE_ANY),wx.DefaultPosition,wx.Size(640,300))
        self.image.SetBackgroundColour(wx.Colour("#a9d9b6"))
        self.bx.Add(self.image)
        self.menu_selection()
        panel=wx.Panel(self,wx.ID_ANY,wx.DefaultPosition,wx.Size(490,40),wx.Centre)
        panel.SetBackgroundColour(wx.Colour("#a39da6"))
        gridsizer=wx.GridSizer(0,3,5,5)
        text=wx.StaticText(panel,wx.TEXT_ALIGNMENT_CENTER,"PERCEPTRON",wx.DefaultPosition,wx.Size(130,30))
        text.SetBackgroundColour(wx.Colour("#a39da6"))
        text.SetForegroundColour(wx.Colour("#5e1d4b"))
        self.combo=wx.ComboBox(panel,wx.ID_ANY,"",wx.DefaultPosition,wx.Size(120,30))
        self.combo.SetForegroundColour(wx.Colour("#5e1d4b"))
        self.combo.Append(str(algos[0]))
        self.combo.Append(str(algos[1]))

        but=wx.Button(panel,wx.ID_ANY,"VISUALIZE",wx.DefaultPosition,wx.Size(70,30))
        but.SetBackgroundColour(wx.Colour("#a39da6"))
        but.SetForegroundColour(wx.Colour("#5e1d4b"))
        but.Bind(wx.EVT_BUTTON,self.visualize,None)
        gridsizer.Add(text)
        gridsizer.Add(self.combo)
        gridsizer.Add(but)
        panel.SetSizer(gridsizer)
        self.bx.Add(panel,wx.ALIGN_CENTER_HORIZONTAL)
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
        
        option=self.combo.GetSelection()
        option+=1
        print(str(option))
        perc.start_perceptron(self.perceptrondata,option)
    def export(self,event):
        if len(self.perceptrondata)==0:
            wx.MessageBox("No visualization made please make a visualization")
            return
        ps.htmlepochboard()
    def close(self,event):
        sys.exit(0)


#Show the Gui for the Perceptron used
class app(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show(True)
        return True

ap=app(None)
ap.MainLoop()
