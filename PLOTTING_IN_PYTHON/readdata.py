from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as mt
import sys
class spot:
    def __init__(self,x_,y_,z_,bias):
        self.x=x_
        self.y=y_
        self.z=z_
        self.bias=bias
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    def getBias(self):
        return self.bias
    def toStr(self):
        return str(self.x)+"-"+str(self.y)+"-"+str(self.z)+"-"+str(self.bias)

def opendata(board):
     y=open("exdata.csv","r")
     for x in y:
        data=x.split(",")
        adata=spot(data[0],data[1],data[2],data[3])
        board.append(adata) 
     y.close()

def openNumpyData(board):
    y=open("exdata.csv","r")
    while x in y:
        data=x.split(",")

def x_axis(board):
    x=[]
    for y in board:
        x.append(y.getX())
    return x

def y_axis(board):
    y=[]
    for x in board:
        y.append(x.getY())
    return y

def z_axis(board):
    z=[]
    for x in board:
        z.append(x.getZ())
    return z

def menu():
    print('Welcome to Perceptron Algorithm Exucutable!!!!')
    print('1-Display Data\n')
    print('2-Show Initial Plotting\n')
    print('3-End Task\n')
    print('Give Choice:')
    x=input()
    return x


def show_data(board):
    print('Patterns used')
    for x in board:
        print('pattern_:'+x.toStr())

#Main Code
data=[]
opendata(data)
fig = mt.figure()
ax = mt.axes(projection='3d')
option=int(menu())
if int(option)==1:
    show_data(data)
elif int(option)==2:
   for pattern in data:
        if int(pattern.getBias())==1:
            ax.scatter(float(pattern.getX()),float(pattern.getY()),float(pattern.getZ()),c='red',marker='x')
        elif int(pattern.getBias())==2:
            ax.scatter(float(pattern.getX()),float(pattern.getY()),float(pattern.getZ()),c='blue',marker='o')
        else:
            print('Invalid data....!!!!')
   mt.show()
   print('Ploting Complete')
else:
   sys.exit(0)
    



