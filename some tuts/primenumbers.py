#Πρόγραμμα για εύρεση πρώτων αριθμών μέσα σε ένα διαστημα 
#εισαγώμενων τιμών

def detect_prime(k):
    print("Prime number detected:"+str(k))

x=input("Give first number:")
y=input("Give second number:")
x=int(x)
y=int(y)
counter=0
if x>y:
    print("Wrong input swapping values")
for i in range(x,y):
    number=i
    prime=2
    for j in range(2,y):
        if(j==number):
            continue
        if(number%j==0):
            prime+=1
    if prime==2:
        detect_prime(number)
        counter+=1
print("Total prime numbers detected:"+str(counter))