#Να κατασκευαστεί πρόγραμμα το οποίο θα πραγματοποιεί εύρεση των μονών αριθμών 
#μέσω ενός πίνακα που θα αποτελείται από τυχαίους αριθμούς
from random import randint
def find_max(array):
    mx=array[0]
    for j in range(1,len(array)):
        if int(array[j])>mx:
            mx=array[j]
    return mx 
def prime_detected(num):
    print("Prime Number:"+str(num))
def is_prime(number):
    counter=2
    for x in range(2,number):
        if number==x:
            continue
        if number%x==0:
            counter+=1
    if counter==2:
        return True
    else:
        return False

def find_primes(array):
   for x in array:
     if is_prime(x):
         prime_detected(x)

def show_board(array):
    print("Array List")
    itr=iter(array)
    for y in itr:
        print("Number:"+str(y))
    print("")

def fill_board():
    array=[]
    size=20
    for x in range(0,20):
        array.append(randint(4,300))
    show_board(array)
    print("")
    print("Primes board")
    find_primes(array)

fill_board()