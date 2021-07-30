def function(array):
    for x in array:
        print(x)

def summary(file):
    sum=0
    for x in file:
        sum+=int(x)
    return sum

def max(file):
    m=0
    cnt=0
    for x in file:
        if cnt==0:
           m=int(x)
        else:
            if int(x)>m:
                m=int(x)
        cnt+=1  
    return m
y=open("C:/Users/nasto/Desktop/numbers.txt","r")
numbers=[]
x=y.readline()
while x:
    numbers.append(int(x))
    x=y.readline()
y.close()
function(numbers)


#Δεύτερος τρόπος ανάγνωσης δεδομένων από αρχείο
#x=y.readline()
#while x:
#    print(x)
#    x=y.readline()

print("Summary of file numbers:"+str(summary(numbers)))
print("Max number in file:"+str(max(numbers)))

