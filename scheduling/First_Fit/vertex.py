class vertex:
    def __init__(self,name):
        self.data=[]
        self.id=name
    def Vertex_Name(self):
        return self.id
    def Append(self,name):
        for x in self.data:
            if str(x)==str(name):
                return
        self.data.append(name)
    def Get(self):
        return self.data
    def Length(self):
        return len(self.data)