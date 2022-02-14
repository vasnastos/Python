import participant as p
import logging as log

def toTime(seconds):
    time=''
    hours=int(int(seconds)/3600)
    minutes=int((int(seconds)%3600)/60)
    secs=(int(seconds)%3600)%60
    hours='0'+str(hours) if int(hours)<=9 else hours
    minutes='0'+str(minutes) if int(minutes)<=9 else minutes
    secs='0'+str(secs) if int(secs)<=9 else secs
    return str(hours)+':'+str(minutes)+':'+str(secs)

class msteams:
    def __init__(self,limit):
        self.participants=[]
        self.participation= {}
        self.date=''
        self.timecount=0
        self.participation_time_limit=limit

    def find_Position(self,id):
        for x in range(0,len(self.participants)):
            if self.participants[int(x)]==id:
                return x
        return -1

    def OpenFile(self,filename):
        self.participation.clear()
        self.participants.clear()
        y=open(filename,encoding='utf16')
        start=True
        getDate=False
        for x in y:
            if start:
                start=False
                continue
            data=x.split('\t')
            if len(data)!=3:
               log.error('Unsupported fileRecord')
               continue
            if data[0] in self.participation:
                previous_val=self.participation[str(data[0])]
                if str(data[1])=='Συμμετέχει':
                    previous_val+=1
                self.participants[int(self.find_Position(data[0]))].Append(data[1],data[2])
                self.participation[str(data[0])]=previous_val
            else:
                self.participation.update({str(data[0]):1})
                newparticipant=p.participant(data[0])
                newparticipant.Append(data[1],data[2])
                if not getDate:
                    getDate=True
                    datelist=data[2].split(',')
                    self.date=datelist[0]
                self.participants.append(newparticipant)

    def Connections(self):
        for x in self.participation:
            print(str(x)+'  Συνδέσεις:'+str(self.participation[x]))

    def meeting_details(self):
        timetable=[]
        for x in self.participants:
           timetable+=x.Time()
        #Ώρα Εκκίνησης-->Ώρα που συνδέθηκε ο πρώτος συμμετέχων εως ότου αποσυνδέθηκε και ο τελευταίος
        starttime=min(timetable)
        endtime=max(timetable)
        print(self.date)
        print(f'Έναρξη={self.date}  {toTime(starttime)}  Λήξη:{self.date}  {toTime(endtime)}   Διάρκεια:{toTime(endtime-starttime)}')
        self.timecount=toTime(endtime-starttime)

    def meeting_time_hold_per_person(self):
        self.participants.sort()
        for x in self.participants:
           time2seconds=x.TimeCount()
           if int(time2seconds)==-1:
                print(f'Διαχειριστής Πλατφόρμας-Διαρκεια={self.timecount}')
           else:
               hourinfo = toTime(time2seconds)
               print(f'{x.id}-Διαρκεια={hourinfo}')

    def Export_Participation_List(self):
        limittime=int(self.participation_time_limit)*60
        formatdate=self.date.replace('/','_')
        y=open('Partcipant_List('+str(formatdate)+').csv','w')
        y.write('PARTICIPANT;'+str(self.date)+'\n')
        for x in self.participants:
            count=x.TimeCount()
            if int(count)==-1:
                continue
            else:
                if int(count)>=limittime:
                    y.write(str(x.id)+';1\n')
                else:
                    y.write(str(x.id)+';0\n')
        y.close()
        print('Participation List has been created as:Participant_List('+str(formatdate)+').csv')
