import functools as ft
class participant:
    def __init__(self,participantid,date,role,Am,mail):
        self.name=participantid
        self.date=date
        self.role=role
        self.am=Am
        self.email=mail
        self.starttime=[]
        self.endtime=[]
        self.duration=[]
    
    def __eq__(self, value):
        return self.am==str(value)

    def Append_STime(self,stime):
        self.starttime.append(stime)
    
    def Append_ETime(self,entime):
        self.endtime.append(entime)
    
    def Append_Dur(self,Duration):
        self.duration.append(Duration)
    
    def TotalDuration(self):
        return ft.reduce(lambda x,y:y+x,self.duration,0)

    def showInfo(self):
        msg=''
        msg+=f'Name:{self.name}\n'
        msg+=f'Role:{self.role}\n'
        msg+=f'Date:{self.date}\n'
        msg+=f'Email:{self.email}\n'
        msg+=f'Student id:{self.am}\n'
        msg+=f'Duration:{ft.reduce(lambda y,x:y+x,self.duration,0)} seconds'
        msg+='\n\tSign in to Lesson\n'
        counter=0
        assert len(self.starttime)==len(self.endtime)
        for x in self.starttime:
          msg+=f'From:{str(x)}--to:{str(self.endtime[int(counter)])}\n'
          counter+=1
        msg+='-----------------------------------------------------\n\n'
        return msg
    
    def ToHtml(self):
        msg='<html><head><style>table{width:100%; height:auto; background-color:blue; border:none; border-collapse:collapse; font-size:17px; font-weight:bold;} th{background-color:white; color:blue; font-size:19px;}</style><table><tr><th>ΩΡΑ ΣΥΜΜΕΤ.</th><th>ΩΡΑ ΑΠΟΧ.</th></tr>'
        counter=0
        print(len(self.starttime))
        for x in self.starttime:
            msg+=f'<tr><td>{x}</td><td>{self.endtime[int(counter)]}</td></tr>'
            counter+=1
        msg+='</table></body></html>'
        print(msg)
        return msg
