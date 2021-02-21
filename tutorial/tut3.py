import os
#File handling
def calculate_summary(list):
    sum=0
    for x in list:
        sum+=float(x)
    return sum

def open_file(filename,list):
    y=open(str(filename),'r')
    for x in y:
        list.append(x)
    y.close()

#Main Code
print('working on:'+str(os.getcwd()))
files=os.listdir('.')
counter=1
for x in files:
    print(str(counter)+'.'+x)
    counter+=1
choice=input('select file you to use:')
numbers=[]
open_file(files[int(choice)-1],numbers)
print('File opened!!!!')
print('Summary:'+str(calculate_summary(numbers)))
