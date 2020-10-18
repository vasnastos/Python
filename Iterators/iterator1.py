#Να κατασκευαστεί πρόγραμμα που με την χρήση ενός πίνακα 
#ο οποίος θα γεμίζει με 15 ακεραίους να υπολογίζει το
#μέγιστο στοιχείο του πίνακα και την θέση του,το ελάχιστο στοιχείο του πίνακα και την θέση του.
#Επίσης να εμφανίστουν τα στοιχεία του πίνακα με την χρήση iterator
from random import seed
from random import randint
from datetime import datetime
size=15
def max(array):
   mx=array[0]
   for i in range(1,len(array)):
       if float(array[i])>mx:
          mx=array[i]
   return mx
def min(array):
    mn=array[0]
    for i in range(1,len(array)):
        if float(array[i])<mn:
            mn=array[i]
    return mn
def average(array):
    sum=0
    for x in array:
        sum+=float(x)
    return sum/len(array)
def seed():
  time=datetime.now()
  timestr=time.strftime("%H:%M:%S")
  secns=0
  splt=timestr.split(":")
  for x in splt:
      secns+=int(x)*2
  return secns   

def fill_board(array):
    for kv in range(0,15):
        array.append(randint(2,400))

def show(array):
    myiter=iter(array)
    for itr in myiter:
        print(itr)

myarray=[]
fill_board(myarray)
show(myarray)
print("Max:"+str(max(myarray)))
print("Min:"+str(min(myarray)))
print("Average:{:.3f}".format(average(myarray)))