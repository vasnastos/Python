import sqlite3 as sq
import car as car
import format as frm

class database:
    def __init__(self):
        try:
            conn=sq.connect("tut9\\test.db")
            self.c=conn.cursor()
        except:
            print('Error on Connection')
    
    def close(self):
        self.c.close()

    def extract_data(self):
        data=[]
        sql='select * from car'
        for x in self.c.execute(sql):
            cr=car.car(x[0],x[1],x[2])
            data.append(cr)
        return data

    def lowest(self,pr):
        data=[]
        for x in self.c.execute('select * from car where price<=%f' % (pr)):
             cr=car.car(x[0],x[1],x[2])
             data.append(cr)
        return data
    
    def getBrands(self):
        data=[]
        for x in self.c.execute('select distinct brand from car'):
            data.append(x[0])
        return data

def show_data(table):
    for x in table:
       print(x)

def main():
    print('SqliteVersion Used:'+sq.version)
    mydb=database()
    data=mydb.extract_data()
    brands=mydb.getBrands()
    lowest10000=mydb.lowest(10000)
    mydb.close()
    print(frm.format.HEADER+'\t\tVihicles')
    print(frm.format.END+frm.format.HR)
    print(frm.format.END+frm.format.BLUE)
    show_data(data)
    print(frm.format.END)
    print(frm.format.HEADER+'\t\tBrands')
    print(frm.format.END+frm.format.HR+frm.format.END)
    print(frm.format.BLUE)
    show_data(brands)
    print(frm.format.END)
    print(frm.format.ENDL)
    print(frm.format.END+'\t\tBelow 5000 $')
    print(frm.format.END+frm.format.HR)
    print(frm.format.END+frm.format.BLUE)
    show_data(lowest10000)
    print(frm.format.END)

if __name__=='__main__':
    main()    