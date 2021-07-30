#Εκτέλεση ένος for loop με χρήση για εκτύπωση πίνακα μία συνάρτηση
def printbrd(board):
    for x in range(0,len(board)):
        print(str(board[x]))
integers=[1,2,3,4,5,6,7,8,9]
floats=[5.6,7.8,9.8,7.34,1.23,6.43]
for x in range(0,9):
    print(integers[x])
print(floats[3:8])
printbrd(floats)

#εκτύπωση αριθμών από το 1 εως το 10
print("Numbers between [1,10]::")
i=1
while i<=10:
    print(i)
    i+=1
else:
    print("Loop finished!!!!!!!!!")  

