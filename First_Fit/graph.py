import vertex as v
import wx
import time
import random as ran

class color:
    def __init__(self,red,green,blue):
        self.r=red;
        self.g=green;
        self.b=blue;
    def Red(self):
        return self.r
    def Green(self):
        return self.g
    def Blue(self):
        return self.b

ran.seed(time.time()*1000)

#Παραγωγή τυχαίων χρωμάτων
colors=[]
def make_colors(total):
     colors.clear()
     i=0
     while int(i)<int(total):
         colors.append(color(ran.randint(0,255),ran.randint(0,255),ran.randint(0,255)))
         i+=1


class graph:
    def __init__(self):
        self.data=[]
        self.csvStr=""
        self.htmlcode=""
        self.filename=""
    
    def isIn(self,a_vertex):
        counter=0
        for x in self.data:
            if str(x.Vertex_Name())==str(a_vertex):
                return counter
            counter+=1
        return -1
    def getHtml(self):
        return self.htmlcode
    def open_File(self,file):
        self.data.clear()
        self.filename=file
        y=open(str(file))
        for x in y:
            line=x.split(" ")
            for k in line:
                if str(k)=="\n":
                    continue
                print(str(k))
                l=self.isIn(k)
                if int(l)==-1:
                    print("is in")
                    self.data.append(v.vertex(k))
                    l=len(self.data)-1
                for m in line:
                    if str(k)==str(m):
                        continue
                    self.data[l].Append(m)
        print("Data:"+str(len(self.data)))
        y.close()
    def position(self,value):
        pos=0
        for x in self.data:
            if str(x.Vertex_Name())==str(value):
                return pos
            pos+=1
        return -1
    def first_fit(self):
        self.htmlcode="<html><head><style>table{background-color:gray; color:blue; font-size:14px;} th{background-color:red; color:gray; font-weight:bold; font-size:17px; text-decoration:underline;}<body><center><h2><u>File Used:"+str(self.filename)+"</u></h2><hr><table border=\"3\"><tr><th>VERTEX</th><th>COLOR</th></tr>"
        show_data=""
        available=[]
        color=[]
        for x in range(len(self.data)):
            available.append(True)
            color.append(-1)
        color[0]=0
        for i in range(1,len(self.data)):
            nbs=self.data[i].Get()
            for x in nbs:
                available[int(color[int(self.position(x))])]=False
            c=0
            while bool(available[c])==False:
                c+=1
            color[i]=int(c)
            for x in nbs:
                available[int(color[int(self.position(x))])]=True
        j=0     
        self.csvStr="Vertex;Color_Number\n"
        max=0       
        for x in color:
            if int(x)>int(max):
                max=x
        max+=1
        make_colors(max)
        for x in color:
            show_data+="\t\t"+str(self.data[j].Vertex_Name())+"-->"+str(x)+"\n"
            self.htmlcode+="<tr><td>"+str(self.data[j].Vertex_Name())+"</td><td style=\"background-color:rgb("+str(colors[x].Red())+","+str(colors[x].Green())+","+str(colors[x].Blue())+")></td></tr>"
            self.csvStr+=str(self.data[j].Vertex_Name())+";"+str(x)+"\n"
            j+=1
        self.htmlcode+="</table></center></body></html>"
        show_data+="============================================\n"
        show_data+="\t\tTotal colors used:"+str(max)+"\n"
        return show_data
    def export_csv(self): 
        if len(self.csvStr)==0:
            wx.MessageBox("First Fit Algorithm Does Not execute")
            return
        savdial=wx.FileDialog(None,"Save First Fit Details",".","","csv files *.csv",wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if savdial.ShowModal()!=wx.ID_CANCEL:
            y=open(str(savdial.GetPath()),"w")
            y.write(str(self.csvStr))
            y.close()
            
                 
