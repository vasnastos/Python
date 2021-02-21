import random as r
from tkinter import messagebox as tk
class employee:
    def __init__(self,n,id,sal):
        self.name=n
        self.id=id
        self.salary=sal
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getSalary(self):
        return self.salary
    def toString(self):
        return self.name+'-'+str(self.id)+'-'+str(self.salary)

def main():
    employees=[]
    for i in range(1,20):
        employees.append(employee('name '+str(i),r.randint(56,1000),r.randint(500,4000)+r.random()))
    msg='Employees\n'
    msg+='---------------------------------------\n'
    for x in employees:
       msg+=x.toString()+'\n'
    tk.showinfo('Employees',msg)

if __name__ == '__main__':
    print('Main Executed')
    main()