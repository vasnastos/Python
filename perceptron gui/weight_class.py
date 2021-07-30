class weight:
    def __init__(self,i):
        self.id=i
        self.save=[]
    def add_weight(self,w):
        self.save.append(float(w))
    def get_Id(self):
        return self.id
    def get(self,i):
        if int(i)>=len(self.save) or int(i)<0:
            return -1.0009876
        return self.save[int(i)]
    def getSize(self):
        return len(self.save)
    def toString(self):
        msg=str(self.id)
        for i in range(0,len(self.save)):
         msg+="--"+str(self.save[i])
        msg+="\n"
        return msg