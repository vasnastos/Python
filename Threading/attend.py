import re
class attend:
    def __init__(self,i):
        self.id=i
        self.acts=[]
        self.datetimes=[]
    
    def getId(self):
        return self.id

    def Append(self,datetime,act):
        self.datetimes.append(datetime)
        self.acts.append(act)
    
    def datetimes(self):
        counter=0
        for x in self.datetimes:
            print('\t'+str(self.acts[int(counter)])+'-'+str(x))
    
    def __eq__(self, value):
        return self.id==str(value)

    def display(self):
        print('\t'+str(self.id))
        print('------------------------')
        counter=0
        for x in self.datetimes:
            print(str(x)+'--'+str(self.acts[int(counter)]))
            counter+=1