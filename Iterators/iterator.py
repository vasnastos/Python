#Παράδειγμα χρήσης iterators στην python
from random import seed
from random import randint
from datetime import datetime
#Παραγωγή σπόρου με την χρήση της ώρας του συστήματος
def get_seed():
    now=datetime.now()
    time=now.strftime("%H:%M:%S")
    inf=time.split(":")
    secnds=0
    for x in inf:
       secnds+=int(x)*3
    return secnds
array=[]
size=10
LIMIT=20
i=1
#παραγωγή τυχαίων αριθμών
seed(get_seed())
while i<=size:
   array.append(randint(2,200))
   i+=1
#Εμφάνιση με την χρήση iterator!!!!
arrayiterator=iter(array)
for itr in arrayiterator:
    str="{:.2f}".format(itr)
    print(str)