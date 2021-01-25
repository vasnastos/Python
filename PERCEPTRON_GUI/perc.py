from mpl_toolkits import mplot3d
import numpy as np
import math
import matplotlib.pyplot as mt
import random
import wx
import sys
import tkinter.messagebox as tk
import weight_class as wc

# ----------------------------------------
# yp-->Λίστα που αποθηκεύει την τιμή target με βάση τα βάρη
# u-->Λίστα Διέγερσης
# n-->Ρυθμός μάθησης
# Η συνάρτηση ενεργοποίησης προκύπτει με βάση την διέγερση που
# εξαρτάται από τις αλλαγές των βαρών
# class spot-->Αναπαράσταση σημείων από αρχείο csv στους 3 άξονες
# data-->Λίστα που περιέχει τα δεδομένα
# n-->Μέγεθος διανύσματος Βαρών
# ----------------------------------------
# Set Learning Rate as 0.6
# Weight vector
# Αρχικά δεδομένα

# Αρχικά βάρη/Τυχαία τιμή από το διάστημα [-1,1]
w = []
n = 3
lr = 0.6
e=10**(-2)
fig = mt.figure()
savedata=[]

def Init_Weights():
    savedata.clear()
    w.clear()
    meter = 0
    while meter <= n:
        w.append(random.randrange(-1, 1))
        meter += 1
# ----------------------------------------

# -----------------------------------------
# class for input data points


class spot:
    def __init__(self, x_, y_, z_, t):
        self.x = x_
        self.y = y_
        self.z = z_
        self.target=int(t)%2

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getTarget(self):
        return self.target

    def get(self, i):
        if int(i) == 1:
            return self.x
        elif int(i) == 2:
            return self.y
        elif int(i) == 3:
            return self.z
        else:
            return 1

    def toStr(self):
        return str(self.x)+"-"+str(self.y)+"-"+str(self.z)+"-"+str(self.target)


# calculate stimulation
# Initiate original data
# Εισαγωγή δεδομένων σε πίνακες

def calcY(data, pos):
    if float(w[0])+float(w[1])*float(data[int(pos)].getX())+float(w[2])*float(data[int(pos)].getY())+float(w[3])*float(data[int(pos)].getZ()) > 0:
        return 0
    elif float(w[0])+float(w[1])*float(data[int(pos)].getX())+float(w[2])*float(data[int(pos)].getY())+float(w[3])*float(data[int(pos)].getZ()) <= 0:
        return 1

# Συνάρτηση αλλαγής βαρών


def weightChanger(data):
    print("Weight Changer termination sequence is used")
    changes = 0
    for i in range(0, len(data)):
        targ = calcY(data, i)
        if(int(targ) != int(data[i].getTarget())):
            temp0 = float(w[0])-float(lr)*float(int(data[i].getTarget())-int(targ))
            temp1 = float(w[1])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getX())
            temp2 = float(w[2])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getY())
            temp3 = float(w[3])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getZ())
            w[0] = temp0
            w[1] = temp1
            w[2] = temp2
            w[3] = temp3
            print("Change Detected")
            changes += 1
        newweight=wc.weight(i+1)
        for k in w:
         newweight.add_weight(k)
        savedata.append(newweight)
    savedata.append(-1)
    return changes

def distance(initw0,initw1,initw2,initw3):
    p=math.pow(float(w[0])-initw0,2)+math.pow(float(w[1])-initw1,2)+math.pow(float(w[2])-initw2,2)+math.pow(float(w[3])-initw3,2)
    return math.sqrt(p)<float(e)

def weightChangerEucl(data):
    print("Eucleidian Termination sequence is used")
    initw0=w[0]
    initw1=w[1]
    initw2=w[2]
    initw3=w[3]
    for i in range(0, len(data)):
        targ = calcY(data, i)
        if int(targ) != int(data[i].getTarget()):
            temp0 = float(w[0])-float(lr)*float(int(data[i].getTarget())-int(targ))
            temp1 = float(w[1])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getX())
            temp2 = float(w[2])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getY())
            temp3 = float(w[3])-float(lr)*float(int(data[i].getTarget())-int(targ))*float(data[i].getZ())
            w[0] = temp0
            w[1] = temp1
            w[2] = temp2
            w[3] = temp3
            newweight=wc.weight(i+1)
            newweight.add_weight(float(temp0))
            newweight.add_weight(float(temp1))
            newweight.add_weight(float(temp2))
            newweight.add_weight(float(temp3))
            savedata.append(newweight)
        else:
         newweight=wc.weight(i+1)
         for k in w:
          newweight.add_weight(float(k))
        savedata.append(newweight)
    savedata.append(wc.weight(-1))
    return bool(distance(initw0,initw1,initw2,initw3))==True


# Συνάρτηση Perceptron
def visual_data(data,weights,epoch):
    ax = mt.axes(projection='3d') 
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    Z = []
    X, Y = np.meshgrid(X, Y)
    Z=(-float(weights[1])*X-float(weights[2])*Y-float(weights[0]))/float(weights[3])
    ax.plot_surface(X, Y, Z)
    for x in range(0, len(data)):
        if int(data[x].getTarget()) == 0:
            ax.scatter(float(data[x].getX()), float(data[x].getY()), float(data[x].getZ()), c="blue", marker='o')
        else:
            ax.scatter(float(data[x].getX()), float(data[x].getY()), float(data[x].getZ()), c="red", marker='x')
    mt.title("epoch_"+str(epoch))
    mt.grid()
    mt.show()


def Percepton(data,option):
    epochs = 100
    j = 0
    while int(j) < int(epochs):
        if int(option)==1:
            epoch = weightChanger(data)
        else:
            epoch=weightChangerEucl(data)
        visual_data(data,w,int(j)+1)
        j += 1
        if int(option)==1:
            if int(epoch) == 0:
              break
        elif int(option)==2:
            if bool(epoch)==True:
              break
    return j

def start_perceptron(data,op):
    Init_Weights()
    # Εμφάνιση δεδομένων Plotting
    epoch = Percepton(data,op)
    # Εμφάνιση συνολικού αριθμού εποχών που χρειάστηκαν
    wx.MessageBox("Epochs used:"+str(epoch))
# ----------------------------------------------------------
