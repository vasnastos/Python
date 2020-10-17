from random import seed
from random import random
import os

seed(300) #όριο ποσού αριθμών που θα παραχθούν με τυχαιότητα
numbers=[]
size=10
i=0
while i<size:
    numbers.append(random())
    i+=1
x=input("Give name of file:")
currentdirectory=os.getcwd()
print(currentdirectory)
filename=currentdirectory+"\\"+x
y=open(filename,"w")
i=1
for x in numbers:
    y.write("Number "+str(i)+":"+str(x))
    i+=1
y.close()