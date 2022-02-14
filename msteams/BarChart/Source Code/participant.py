def toSeconds(time):
    data=time.split(':')
    return int(data[0])*3600+int(data[1])*60+int(data[2])

def Convert_to_Default_End_Time(starttime):
    data=starttime.split(':')
    default=str(int(data[0])+2)+':'+str(data[1])+':'+str(data[2])
    return default

class participant:
    def __init__(self,participant_id,starting):
        self.id=participant_id
        self.datetime=[]
        self.action=[]
        self.defaultendtime=Convert_to_Default_End_Time(starting)
        self.timecount=0

    def Append(self,act,adatetime):
        self.datetime.append(adatetime)
        self.action.append(act)

    def GetId(self):
        return self.id

    def Time(self):
        time=[]
        for x in self.datetime:
            spldata=x.split(',')
            spldata2=spldata[1].split(' ')
            time.append(toSeconds(spldata2[1]))
        return time

    def  Participation_table(self):
        message='<html><head><style>table{background-color:blue; width:90%; color:white; font-size:17px; text-align:center; border:1px solid green;} th{background-color:white; color:darkblue; font-size:21px;}</style></head>'
        message+='<body><center><h1>Participant:'+str(self.id)+'</h1><hr style=\"border-top:2px solid azure;\"><table><tr><th>Ενέργεια Χρήστη</th><th>Χρονική σήμανση</th></tr>'
        c=0
        for x in self.adatetime:
            message+='<tr><td>'+str(self.action[int(c)])+'</td><td>'+str(x)+'</td></tr>'
        message+='</table></center></body></html>'
        return message

    def TimeCount(self):
        total=0
        if len(self.datetime)==1:
            data = self.datetime[0].split(',')
            dataB = data[1].split(' ')
            timestart=toSeconds(dataB[1])
            return int(toSeconds(self.defaultendtime))-int(timestart)
        elif len(self.datetime)%2==1:
            for x in range(0,len(self.datetime)-2,2):
                data1=self.datetime[int(x+1)].split(',')
                data2=self.datetime[int(x)].split(',')
                data1B=data1[1].split(' ')
                data2B=data2[1].split(' ')
                timeend=toSeconds(data1B[1])
                timestart=toSeconds(data2B[1])
                total+=timeend-timestart
            data = self.datetime[len(self.datetime)-1].split(',')
            dataB = data[1].split(' ')
            timestart = toSeconds(dataB[1])
            total+=int(toSeconds(self.defaultendtime))-int(timestart)
            return total
        else:
            for x in range(0,len(self.datetime)-1,2):
                data1=self.datetime[int(x+1)].split(',')
                data2=self.datetime[int(x)].split(',')
                data1B=data1[1].split(' ')
                data2B=data2[1].split(' ')
                timeend=toSeconds(data1B[1])
                timestart=toSeconds(data2B[1])
                total+=timeend-timestart
            return total

    def call_out(self):
        counter=0
        stigma=[]
        for x in self.datetime:
            if str(self.action[int(counter)])=='Left' or str(self.action[int(counter)])=='Αποχώρησε':
                  stigma.append(x)
            counter+=1
        if self.datetime[len(self.datetime)-1] in stigma:
            data=self.datetime[len(self.datetime)-1].split(',')
            dataB=data[1].split(' ')
            return  toSeconds(dataB[1])
        else:
            return toSeconds(self.defaultendtime)


    def __eq__(self, other):
        return self.id==str(other)

    def __lt__(self, other):
        return self.TimeCount()<other.TimeCount() and int(other.TimeCount())!=-1

    def __str__(self):
        return self.id+'\n'+str(self.adatetime)+'\n'+str(self.action)

