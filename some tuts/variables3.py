def myfunc(): #δήλωση συνάρτησης
   global x #δηλωση καθολικής μεταβλητής
   x=23
   y=input('Insert an integer:')
   k=input('Insert a double:')
   sum=int(y)+float(k) #Πρόσθεση δύο αριθμών με μετατροπή τους στους κατάλληλους τύπους
   print('Summary of two input numbers:'+str(sum))
z=input('Give a number:')
myfunc() #κλήση συνάρτησης
sum=int(x)+float(z) #casting σε αντίστοιχους τύπους αλλιώς αναγνώριση της μεταβλητής σαν αλφαριθμητικό
print("Global variable and input number summary:"+str(sum)) #str-->casting σε αλφαριθμητικό