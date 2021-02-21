import random as r
#Lists demo
list=[]
size=r.randint(20,30)
for x in range(1,size+1):
   list.append(x)
print(list)
print('List elements:'+str(len(list)))
list.insert(3,89)
print('-------------------------------------')
print('Sorted List ')
list.sort()
print(list)