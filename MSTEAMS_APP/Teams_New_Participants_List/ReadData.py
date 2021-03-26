import participant as prt
import Time as t

class teams:
    
    def __init__(self):
       self.filename=''
       self.details={}
       self.participants=[]
    
    def Open_Csv(self,filename):
       self.filename=filename
       self.details.clear()
       self.participants.clear()
       dets=False
       firstRow=True
       with open(filename,'r',encoding='utf-8') as f:
          for x in f:
              if str(x)=='\n':
                  dets=True
                  continue
              data=x.split('\t')
              if not dets:
                  if len(data)==1:
                      continue
                  self.details.update({data[0]:data[1]})
                  continue
              
              if firstRow:
                    #Dismiss the first line
                    firstRow=False
                    continue 
              am=data[4].split('@')
              if am[0].startswith('int'):
                 primary_key=am[0][4:]
              elif am[0].startswith('thl'):
                  primary_key=am[0][5:]
              print(primary_key)
              if primary_key in self.participants:
                  starttime=data[1].split(',')
                  starttime_type=starttime[1].split(' ')
                  self.participants[self.participants.index(primary_key)].Append_STime(starttime_type[1])
                  endtime=data[2].split(',')
                  endtime_type=endtime[1].split(' ')
                  self.participants[self.participants.index(primary_key)].Append_ETime(endtime_type[1])
                  self.participants[self.participants.index(primary_key)].Append_Dur(t.ToSeconds(data[3]))
                  continue
              name=data[0]
              date=data[1].split(',')[0]
              starttime=data[1].split(',')[1].split(' ')[1]
              endtime=data[2].split(',')[1].split(' ')[1]
              duration=t.ToSeconds(data[3])
              email=data[4]
              am=data[4].split('@')[0]
              if am.startswith('int'):
                  am=am[4:]
              elif am.startswith('thl'):
                  am=am[5:]
              role=data[5]
              aparticipant=prt.participant(name,date,role,am,email)
              aparticipant.Append_STime(starttime)
              aparticipant.Append_ETime(endtime)
              aparticipant.Append_Dur(duration)
              self.participants.append(aparticipant)

    def show_participants(self):
        LessonInfo='Lesson Information\n'
        for x in self.details:
            LessonInfo+=f'{x}:{self.details[x]}\n'
        print(LessonInfo)
        for x in self.participants:
            print(x.showInfo())

