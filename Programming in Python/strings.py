def printlist(list):
    for y in list:
        print(y)


x="Hello world from dit uoi my name is vasileios Nastos"
print('String x has length '+str(len(x)))
print(x.upper()) #Μετατροπή σε κεφαλαία από πεζά
print(x[2:9]) #εκτύπωση από τις θέσεις 2 εως εννέα του αλφαριθμητικού
print(x.split(" ")) #εκτύπωση λέξεων που έχουν διαχωριστεί με βάση το space
y="from" in x
print(y) #έλεγχος αν η λέξη from είναι εντός του αλφαριθμητικού
value1=56
value2=2
value3="America"
z="""i want {1} tickets to travel in {2}
     which each cost {0}$"""
print(z.format(value1,value2,value3)) #εκτύπωση με format.
list=["A","B","C","D","E","F"]
print(list[3:6]) #εκτύπωση από την θέση 3 της λίστας εως την θέση 5.
printlist(list)
list.append("G")
printlist(list)
list.remove("C") #απομάκρυνση από την λίστα του αλφαριθμητικού C.
printlist(list)