def printarray(array):
  for x in array:
      print(x)

def summary(array):
    sum=0
    for x in array:
        sum+=int(x)
    return sum

def average(array):
    sum=0
    for x in array:
        sum+=int(x)
    return sum/len(array)

def max(array):
    max=array[0]
    for x in range(1,len(array)):
        if array[x]>max:
            max=array[x]
    return max

def min(array):
    min=array[0]
    for x in range(1,len(array)):
      if array[x]<min:
          min=array[x]
    return min

#Main code in program
arrays=[]
i=0
while i<10:
    x=input("Give number:")
    arrays.append(x)
    i+=1
print("List of numbers::")
printarray(arrays)
print("Summary:"+str(summary(arrays)))
print("Average:"+str(average(arrays)))
print("Max:"+str(max(arrays)))
print("Min:"+str(min(arrays)))