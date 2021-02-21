class car:
    def __init__(self,b,m,p):
        self.brand=b
        self.model=m
        self.price=p
    def __str__(self):
        return str(self.brand)+'-'+str(self.model)+'-'+str(self.price)