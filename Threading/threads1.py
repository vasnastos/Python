import threading as th
from threading import Thread
import attend as at
import csv as c
import re

global watchers
watchers=[]

def processing(start,end,attendes,parts):
    for j in range(int(start),int(end)):
        if int(j)==0:
             #Πρώτη γραμμή περιγραφές
             continue
        data=attendes[int(j)].split('\t')
        if len(data)!=3:
            continue
        print(int(j))
        if data[0] in parts:
            init_limit=parts[data[0]]
            init_limit+=1
            parts[data[0]]=init_limit
            watchers[watchers.index(data[0])].Append(data[1],data[2])
        else:
            an_attendant=at.attend(data[0])
            an_attendant.Append(data[1],data[2])
            watchers.append(an_attendant)
            parts.update({data[0]:1})
        

def openSource(parts):
    filename='source.csv'
    parts.clear()
    try:
      y=open(filename,encoding='utf16')
      for x in y:
          if len(x)==0 or str(x)=='\n':
              continue
          parts.append(x)
      y.close()
    except IOError as e:
        print(e)
   

if __name__=='__main__':
    attendees=[]
    openSource(attendees)
    jobs=[]
    watchers=[]
    threads=4
    participation={}
    endpoint=0
    for i in range(threads-1):
        athread=Thread(target=processing(endpoint,int((len(attendees)/int(threads)))*int(i+1),attendees,participation),name='Thread_'+str(i))
        jobs.append(athread)
        endpoint=int((len(attendees)/int(threads))*int(i+1))
    print(endpoint)
    athread=Thread(target=processing(endpoint,len(attendees),attendees,participation),name='Thread_3')
    jobs.append(athread)
    for k in jobs:
        k.start()
        print('Worker '+k.getName()+' starts processing data')
    for k in jobs:
        k.join()
    print('All thread finish treir job!!!!')
    print('Exit sequence!!!')
    print(len(attendees))
    for x in watchers:
        x.display()

#target: the function to be executed by thread
