import participant as p

def find_in_list(participants,name):
    counter=0
    for x in participants:
        if x==str(name):
            return counter
        counter+=1
    return -1


def openFile(participation,participants):
    participation.clear()
    participants.clear()
    y=open('lab_source.csv',encoding='utf16')
    for x in y:
        data=x.split('\t')
        if len(data)!=3:
            continue
        if data[0] in participation:
            previousval=participation[data[0]]
            if str(data[1])=='Συμμετέχει':
                previousval+=1
            participant_position=find_in_list(participants,data[0])
            participants[int(participant_position)].Append(data[1],data[2])
            participation[data[0]]=previousval
        else:
            participation.update({data[0]:1})
            newparticipant=p.participant(data[0])
            newparticipant.Append(data[1],data[2])
            participants.append(newparticipant)
    y.close()

def show_connections(participation,participants):
    for x in participation:
        pos=find_in_list(participants,str(x))
        print(f'{x}  Συνδέσεις:{participation[x]}')

def main():
   participation={}
   participants=[]
   openFile(participation,participants)
   show_connections(participation,participants)
