import wx
from enum import Enum
import os
import sys 
import graph as g
from wx.adv import Animation, AnimationCtrl
import webbrowser as wb
#Enumaration
#class Id(Enum):
#    OPEN=1
#    CLOSE=2
#    EXPORT=3
#    FF=4
#    HTML=5
#    def value(self,i):
#        return self.value

class Frame(wx.Frame):
    def openFile(self,event):
        opdial=wx.FileDialog(None,"Select input File",".","","",wx.FD_OPEN)
        file=""
        if opdial.ShowModal()!=wx.ID_CANCEL:
            file=opdial.GetPath()
        self.handler.open_File(file)
    def close(self,event):
        sys.exit(0)
    def export(self,event):
        self.handler.export_csv()
    def html_code(self,event):
        output=self.handler.getHtml()
        y=open("first_fit.html","w")
        y.write(output)
        y.close()
        path=os.getcwd()
        file=path+"//first_fit.html"
        wb.open_new_tab(file)
    def first_fit(self,event):
        result=self.handler.first_fit()
        self.results.SetValue(str(result))
    def make_menu(self):
        bar=wx.MenuBar()
        menu=wx.Menu()
        menu.Append(101,"OPEN")
        menu.Append(102,"EXPORT_CSV")
        menu.Append(103,"FIRST_FIT")
        menu.Append(104,"HTML_BOARD")
        menu.Append(1001,"WEBSITE")
        menu.Append(105,"CLOSE")
        self.Bind(wx.EVT_MENU,self.openFile,None,id=101)
        self.Bind(wx.EVT_MENU,self.export,None,id=102)
        self.Bind(wx.EVT_MENU,self.first_fit,None,id=103)
        self.Bind(wx.EVT_MENU,self.html_code,None,id=104)
        self.Bind(wx.EVT_MENU,self.visit,None,id=1001)
        self.Bind(wx.EVT_MENU,self.close,None,id=105)
        bar.Append(menu,"OPTIONS")
        self.SetMenuBar(bar)
    def __init__(self):
      self.handler=g.graph()
      wx.Frame.__init__(self,None,wx.ID_ANY,"Graph Coloring",wx.DefaultPosition,wx.Size(400,650))
      self.bx=wx.BoxSizer(wx.VERTICAL)
      self.SetIcon(wx.Icon("icon.png"))
      self.make_menu()
      Gif=Animation("central.gif")
      GifCtrl=AnimationCtrl(self,wx.ID_ANY,Gif,wx.DefaultPosition,wx.Size(399,300))
      GifCtrl.Play()
      self.bx.Add(GifCtrl)
      self.results=wx.TextCtrl(self,wx.ID_ANY,"",wx.DefaultPosition,wx.Size(399,300),wx.TE_MULTILINE)
      self.bx.Add(self.results)
      self.SetSizer(self.bx)
    def visit(self,event):
        wb.open_new_tab("https://vasnastos.github.io/Algorithms_and_complexity/")
      
class App(wx.App):
   def OnInit(self):
    f=Frame()
    f.Show()
    return True

#Εμφάνιση παραθύρου
a=App()
a.MainLoop()