x=input('Give number of children')
salary=input('Give Salary:')
k=input('Give Gender:')
if k=='M':
    if x==1:
        salary=float(salary)+20.0
    elif x==2:
        salary=float(salary)+50
    else:
        salary=float(salary)+120
else:
    if(x==1):
       salary=float(salary)+30
    elif x==2:
       salary=float(salary)+80
    else:
        salary=float(salary)+160
print("Gender :"+k)
print("Number of children:"+str(x))
print("Total salary after extra:"+str(salary))