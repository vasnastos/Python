import time as tm
import datetime as d
filename="results(dist).out"

def weightInit(w):
    y=open(str(filename),'a')
    y.write(' Init weight values:'+str(w)+"\n")
    y.close()

def epochopener(w):
    time=d.datetime.now()
    current_time=time.strftime("%H:%M:%S")
    current_date=time.date()
    y=open(str(filename),"w")
    y.write("  ©Nastos Vasileios 2020 ARTA\n")
    y.write(" Execute Perceptron Algorithm using Euclidean Distance Between the initial weights and the last weights of every epoch\n")
    y.write(" File created at:"+str(current_time)+"--"+str(current_date)+"\n")
    y.close()
    weightInit(w)
    y=open(str(filename),"a")
    y.write("---------------------------------------------------\n")
    y.write("\tNUMBER_SEQUENCE(e)\tEPOCHS\n")
    y.close()

def saver(e,epochs):
  y=open(str(filename),"a")
  y.write("   \t"+str(e)+"\t   \t\t\t   "+str(epochs)+"\n")
  y.close()