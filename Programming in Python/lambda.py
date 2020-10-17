def function(s):
   print("divided by two:::")
def increase(s):
    return s*s
x=input('Give a number:')
x=int(x)
z=lambda x:x%2==0 #lambda-->lambda arguments:body
if z: #z==true
    function(x)
    x=increase(x)
    print("SQUARE:"+str(x))