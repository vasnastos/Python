from tkinter.filedialog import askopenfilename
import Lexicon
import sys
import re
class lexicon:
   data=[]
   def __init__(self,filename):
       y=open(filename,"r")
       for x in y:
           self.data.append(x)
       y.close()
   def equal(self,size):
        match=[]
        for x in self.data:
            if len(x)==int(size):
                match.append(x)
        return match
   def startswith(self,startstream):
        match=[]
        regex="^"+startstream+"([.])*"
        for x in self.data:
            if re.search(regex,str(x))!=None:
              match.append(x)
        return match
   def endswith(self,endstream):
        match=[]
        regex="[.]*"+endstream+"$"
        for x in self.data:
            if re.search(regex,x)!=None:
                match.append(x)
        return match
   def replay(self,sequence,size):
       match=[]
       regex="([.]*"+sequence+"[.]*){"+size+"}"
       for x in self.data:
           if re.search(regex,x)!=None:
               match.append(x)
       return match
   def sequence(self,seq):
      match=[]
      regex=""
      for i in range(0,len(seq)):
          if seq[i]!='-':
              regex+=str(seq[i])
          else:
              regex+=str(".")
      for x in self.data:
        if re.search(regex,x)!=None:
            match.append(x)
      return match


def show_data(data):
    print('********************************************\n')
    print('\tTotal words:'+str(len(data)))
    for x in data:
        print('\t'+str(x))
    print('********************************************\n')

def menu():
    print('1-Find Words by Len\n')
    print('2-Find words by Start Sequence\n')
    print('3-Find Words by end Sequence\n')
    print('4-Find Replay Sequence\n')
    print('5-Find words by sub-sequence\n')
    print('6-Exit\n')
    x=input('Select choice:')
    return x

def switch(l):
    choice=menu()
    if int(choice)==1:
        k=input('Give word size:')
        show_data(l.equal(k))
    elif int(choice)==2:
        str=input('Give word:')
        show_data(l.startswith(str))
    elif int(choice)==3:
        str=input('Give word:')
        show_data(l.endswith(str))
    elif int(choice)==4:
        str=input('Give word:')
        size=input('Give number of replays:')
        show_data(l.replay(str,size))
    elif int(choice)==5:
        str=input('Give word:')
        show_data(l.sequence(str))
    elif int(choice)==6:
        sys.exit(0)
    else:
        print('Invalid Choice!!!!')


#Main Configuration
filename=askopenfilename()
l=lexicon(filename)
while True:
    switch(l)