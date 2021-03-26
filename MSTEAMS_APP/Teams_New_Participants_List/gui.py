from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ReadData as rd

class window(QMainWindow):
    def make_menu(self):
        self.men=QMenu('OPTIONS')
        # men.setTitle()
        a1=QAction('OPEN',self)
        a2=QAction('PARTICIPATIONS',self)
        a1.triggered.connect(lambda:self.Open())
        a2.triggered.connect(lambda:self.Parts())
        self.men.addAction(a1)
        self.men.addAction(a2)
        self.menuBar().addMenu(self.men) 

    def __init__(self):
        super().__init__(None)
        self.teams=rd.teams()
        self.setWindowTitle('Show New Format')
        self.setFixedSize(900,600)
        self.table=QTableWidget()
        self.table.setFixedSize(self.width(),self.height())
        self.table.setWindowTitle('Filename Open')
        headers=['ΟΝ/ΝΥΜΟ','HMEROMHNIA','ΣΥΜΜΕΤΟΧΗ','ΑΜ','EMAIL','ΔΙΑΡΚΕΙΑ','ΡΟΛΟΣ']
        self.table.setColumnCount(len(headers))
        self.table.setStyleSheet('font-size:19px; border-collapse:collapse; border:1px solid;')
        for x in range(len(headers)):
            self.table.setColumnWidth(int(x),0.995*self.table.width()/len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.make_menu()
        self.setCentralWidget(self.table)
        self.show()


    def Open(self):
        files=QFileDialog.getOpenFileName(self,'Open Participation List','.','csv Files (*.csv)')
        if len(files)==0 or len(files[0])==0:
             QMessageBox.critical(self,'Error On Opening','<b style=\"color:red;\">No file selected</b>')
             return
        self.teams.Open_Csv(files[0])
        self.table.clearContents()
        counter=0
        self.table.setRowCount(len(self.teams.participants))
        c1=QColor(65,13,79)
        for x in self.teams.participants:
            self.table.setRowHeight(int(counter),0.1*int(self.table.height()))
            it1=QTableWidgetItem()
            it1.setTextAlignment(Qt.AlignCenter)
            it1.setForeground(c1)
            it1.setText(x.name)
            self.table.setItem(int(counter),0,it1)
            it2=QTableWidgetItem()
            it2.setTextAlignment(Qt.AlignCenter)
            it2.setForeground(c1)
            it2.setText(x.date)
            self.table.setItem(int(counter),1,it2)
            b1=QPushButton('INFO')
            b1.setStyleSheet('color:blue; background-color:gray; font-size:21px;')
            b1.setFixedSize(self.table.columnWidth(int(counter)),self.table.rowHeight(int(counter)))
            self.table.setCellWidget(int(counter),2,b1)
            it3=QTableWidgetItem()
            it3.setTextAlignment(Qt.AlignCenter)
            it3.setForeground(c1)
            it3.setText(x.am)
            self.table.setItem(int(counter),3,it3)
            it4=QTableWidgetItem()
            it4.setTextAlignment(Qt.AlignCenter)
            it4.setForeground(c1)
            it4.setText(x.email)
            self.table.setItem(int(counter),4,it4)
            it6=QTableWidgetItem()
            it6.setTextAlignment(Qt.AlignCenter)
            it6.setForeground(c1)
            it6.setText(str(x.TotalDuration()))
            self.table.setItem(int(counter),5,it6)
            it7=QTableWidgetItem()
            it7.setTextAlignment(Qt.AlignCenter)
            it7.setForeground(c1)
            it7.setText(x.role)
            self.table.setItem(int(counter),6,it7)
            counter+=1


         
    def Parts(self):
        print('Participate Slot')

    def Send(self):
        print('Send Email to instructor')


a=QApplication([''])
window()
a.exec() 
