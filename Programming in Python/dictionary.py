def function(set):
    for x in set:
        print(x)
x={1,2,5,6,7}
x.add(2)
function(x)
x.add(13)
function(x)
#set-->Δομή που δεν εισάγει ένα στοιχείο παραπάνω από 1 μία φορα,και
#έχει θέσεις χωρίς αρίθμηση
x.pop()
function(x)
x.remove(5)
extraset=set((56,78,12,25,7))
x.update(extraset)
print("After union of two sets")
function(x)
print("Length of set is:"+str(len(x)))