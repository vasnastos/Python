import threading as th
from threading import Thread
global data
data=[]
def Open():
    y=open('source(1).csv',encoding='utf-8')
    for x in y:
       data.append(x)

def Print(start,end):
    for x in range(int(start),int(end)):
        print(data[int(x)])


if __name__=='__main__':
    Open()
    threads=4
    endpoint=0
    jobs=[]
    for i in range(threads):
       athread=Thread(target=Print(endpoint,int(len(data)*(int(i)+1)/int(threads))))
       endpoint=len(data)*(int(i)+1)/int(threads)
       jobs.append(athread)
    for k in jobs:
        k.start()
    for k in jobs:
        k.join()