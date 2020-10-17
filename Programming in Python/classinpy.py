#δημιουργία κλάσης που αποθηκεύει στοιχεία για αυτοκίνητα
#μοντελο
#μάρκα 
#τιμή

class car:

    def __init__(self,m,br,pr):
        self.model=m
        self.brand=br
        self.price=pr
        print("Object created!!!!")
    def printobj(self):
       print(self.model+"-"+self.brand+"-"+str(self.price))

arrays=[]
i=0
size=5
while i<size:
  model=input('Give Car model:')
  brand=input('Give Car brand:')
  price=input('Give Car price')
  price=float(price)
  arrays.append(car(model,brand,price))
  i+=1

i=0
while i<size:
    arrays[i].printobj()
    i+=1

#Διαγραφή αντικειμένων
i=0
while i<size:
    del arrays[i]
    i+=1