import math as m
import os
#Υπερφόρτωση τελεστών
#<	__LT__(SELF, OTHER)
#>	__GT__(SELF, OTHER)
#<=__LE__(SELF, OTHER)
#>=__GE__(SELF, OTHER)
#==__EQ__(SELF, OTHER)
#!=__NE__(SELF, OTHER)


class format:
   END='\033[0m'
   HEADER='\033[95m'
   BLUE='\033[94m'
   RED='\033[91m'
   ENDL='\n'
   HR='\033[91m============================================='

class vertex:
   def __init__(self,n):
      self.name=n
      self.connected=[]
   def Append(self,k):
      for j in self.connected:
         if str(j)==str(k):
            return 
      self.connected.append(k)
   def __eq__(self, value):
          return self.name==str(value)
   def grade(self):
      return len(self.connected)
   def __lt__(self, value):
      return self.grade()<value.grade()
   def __str__(self):
         return str(self.grade())

def find(data,j):
   for i in range(0,len(data)):
      if data[i]==j:
         return i
   return -1

def open_file(data):
   filename=os.getcwd()+'\\tut8\\yor-f-83.stu'
   y=open(filename,'r')
   #k=y.readline()
   for k in y:
      all_data=k.split(' ')
      for j in all_data:
        if len(j)==1:
               continue
        pos=find(data,j)
        if int(pos)!=-1:
         for l in all_data:
           if str(l)==' ':
                  continue
           if data[int(pos)]==l:
                  continue
           data[int(pos)].Append(l)
        else:
           n=vertex(j)
           for l in all_data:
              if str(j)==str(l):
                 continue
              n.Append(l)
           data.append(n)
   y.close()

def density(data):
   sum=0
   for x in data:
      if x.grade()!=0:
         sum+=x.grade()
   return sum/m.pow(len(data),2)

def max(data):
   max=0
   for x in data:
      if int(x.grade())>int(max):
         max=x.grade()
   return max        

def min(data):
   min=data[0].grade()
   for k in data:
      if int(k.grade())<int(min):
         min=k.grade()
   return min

def mean(data):
   sum=0
   for x in data:
      sum+=x.grade()
   return sum/len(data)

def cv(data):
   mn=mean(data)
   s=0
   for j in data:
      calc=float(j.grade())-float(mn)
      s+=float(calc)**2
   s/=(len(data)-1)
   s=m.sqrt(s)
   s/=mn
   s*=100.0
   return s  

def median(data):
   data.sort()
   return data[int(len(data)/2)]

def show_vertices(data):
       for x in data:
         print(str(x.name)+'---'+str(x.grade()))

def main():
   data=[]
   open_file(data)
   show_vertices(data)
   print(format.HEADER+'\tyor-f-83.stu statistics'+format.END)
   print(format.HR+format.END)
   print('\t %sDensity:%.3f' % (format.BLUE,density(data)))
   print('\t '+'Max:'+str(max(data)))
   print('\t Min:'+str(min(data)))
   print('\t Mean:'+str(mean(data)))
   print('\t CV:%.3f%%' % (cv(data)))
   print('\t Median:'+str(median(data))+format.END)
   print(format.HR)
   print(format.RED+'\t   Total Vertices:'+str(len(data))+format.END)

if __name__=='__main__':
    main()