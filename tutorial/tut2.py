def factorial(n):
    sum=1
    for x in range(1,int(n)+1):
      sum*=x
    return sum

#Main Code 
print('Factorial calculating program')
print('************************************')
y=input('Give number you want to find the factorial:')
print('Factorial:'+str(factorial(y)))
