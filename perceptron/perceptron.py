from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as mt
import random
import sys
import tkinter.messagebox as tk

#----------------------------------------
#yp-->Λίστα που αποθηκεύει την τιμή target με βάση τα βάρη
#u-->Λίστα Διέγερσης
#n-->Ρυθμός μάθησης
#Η συνάρτηση ενεργοποίησης προκύπτει με βάση την διέγερση που 
#εξαρτάται από τις αλλαγές των βαρών
#class spot-->Αναπαράσταση σημείων από αρχείο csv στους 3 άξονες
#data-->Λίστα που περιέχει τα δεδομένα
#n-->Μέγεθος διανύσματος Βαρών
#----------------------------------------
#Set Learning Rate as 0.6
#Weight vector 
n=3
lr=0.6

#Αρχικά βάρη/Τυχαία τιμή από το διάστημα [-1,1]
w=[]
meter=0
while meter<=n:
    w.append(random.randrange(-1,1))
    meter+=1
#Plotting
fig = mt.figure()
ax = mt.axes(projection='3d')
X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
a = 2;
b = -0.5;
c = 0.5;
d = 1.5;
X, Y = np.meshgrid(X, Y)
Z= (-a/c)*X+(-b/c)*Y+(-d/c);
#----------------------------------------

#-----------------------------------------
#class for input data points
class spot:
    def __init__(self,x_,y_,z_,t):
        self.x=x_
        self.y=y_
        self.z=z_
        if int(t)==1:
            self.target=0
        elif int(t)==2:
            self.target=1
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    def getTarget(self):
        return self.target
    def get(self,i):
        if int(i)==1:
            return self.x
        elif int(i)==2:
            return self.y
        elif int(i)==3:
            return self.z
        else:
            return 1
    def toStr(self):
        return str(self.x)+"-"+str(self.y)+"-"+str(self.z)+"-"+str(self.target)

#open exdata.csv(Ανοιγμα αρχείου δεδομένων και τοποθέτηση σε
# λίστα που περιέχει αντικείμενα spot(Μοντελοποίηση διανύσματος με κλάση).)
def opendata(board):
     y=open("exdata.csv","r")
     for x in y:
        data=x.split(",")
        adata=spot(data[0],data[1],data[2],data[3])
        board.append(adata) 
     y.close()
     #shuffle δεδομένων ώστε να πάρουν τυχαίες θέσεις στην λίστα
     random.shuffle(board)

#------------------------------------------------

#calculate stimulation
#Initiate original data
#Εισαγωγή δεδομένων σε πίνακες
def ONINIT(data):
    opendata(data)

def calcY(data,pos):
       if float(w[0])+float(w[1])*float(data[int(pos)].getX())+float(w[2])*float(data[int(pos)].getY())+float(w[3])*float(data[int(pos)].getZ())>=0:
          return 0
       elif float(w[0])+float(w[1])*float(data[int(pos)].getX())+float(w[2])*float(data[int(pos)].getY())+float(w[3])*float(data[int(pos)].getZ())<0: 
          return 1

#Συνάρτηση αλλαγής βαρών
def weightChanger(data):
    changes=0
    for i in range(0,len(data)):
        targ=calcY(data,i)
        if(int(targ)!=int(data[i].getTarget())):
            temp0=float(w[0])-float(lr)*float(int(data[i].getTarget())-int(targ))
            temp1=float(w[1])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getX())
            temp2=float(w[2])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getY())
            temp3=float(w[3])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getZ())     
            w[0]=temp0
            w[1]=temp1
            w[2]=temp2
            w[3]=temp3
            changes+=1
    return changes

#Συνάρτηση Perceptron
def Percepton(data):
    epochs=100
    j=0
    while int(j)<int(epochs):
       epoch=weightChanger(data)
       print(str(epoch))
       if int(epoch)==0:
           break
       j+=1
    return j

#Display Data in Command Line
#Εμφάνιση αρχικών δεδομένων στην γραμμή εντολών
def show_data(board):
    print('Patterns used')
    for x in board:
        print('pattern_:'+x.toStr())
#-----------------------------------------------------------

#-----------------------------------------------------
#Define a command line menu
#Μενού γραμμής εντολών
def menu():
    print('Welcome to Perceptron Algorithm Exucutable!!!!')
    print('1-Display Data\n')
    print('2-Show Initial Plotting\n')
    print('3-End Task\n')
    x=input('Select option:')
    return x
#-----------------------------------------------------------
#Main Code
data=[]
ONINIT(data)
option=menu() 
if int(option)==1:
    show_data(data)
elif int(option)==2:
   #Εμφάνιση δεδομένων Plotting
   epoch=Percepton(data)
   Z=(-float(w[1])*X-float(w[2])*Y-float(w[0]))/w[3]
   ax.plot_surface(X,Y,Z) 
   for x in range(0,len(data)):
       if int(data[x].getTarget())==0:
           ax.scatter(float(data[x].getX()),float(data[x].getY()),float(data[x].getZ()),c="blue",marker='o')
       else:
           ax.scatter(float(data[x].getX()),float(data[x].getY()),float(data[x].getZ()),c="red",marker='x')
   #Εμφάνιση συνολικού αριθμού εποχών που χρειάστηκαν
   tk.showinfo("EPOCH USAGE","Total epochs used:"+str(epoch))
   mt.grid()
   mt.show()       
else:
   sys.exit(0)

#----------------------------------------------------------