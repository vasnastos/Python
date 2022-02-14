from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
from PyQt5.Qt import QColor
from PyQt5.QtGui import *
import session_teams as s
import sys
import random as r

r.seed()

def Random_colors(rng):
    return [QColor(r.randint(0,255),r.randint(0,255),r.randint(0,255)) for x in range(int(rng))]

class window(QMainWindow):

    def make_menu(self):
        self.menu=QMenu()
        self.menu.setTitle('OPTIONS')
        a1=QAction('OPEN',self)
        a2=QAction('SAVE',self)
        aex=QAction(QIcon('RESOURCES/information.png'),'',self)
        a3=QAction('CLOSE',self)
        a1.triggered.connect(lambda: self.Open())
        a2.triggered.connect(lambda: self.Save())
        aex.triggered.connect(lambda: self.printinfo())
        a3.triggered.connect(lambda: sys.exit(0))
        self.menu.addAction(a1)
        self.menu.addAction(a2)
        self.menu.addAction(a3)
        self.menuBar().addMenu(self.menu)
        self.menuBar().addAction(aex)

    def Open(self):
        files=QFileDialog.getOpenFileName(self,'Open File','.','teams participation file (*.csv)')
        if len(files)==0 or len(files[0])==0:
            QMessageBox.critical(self,'File Error','You did not select a file')
            return
        self.information=self.teams.OpenFile(files[0])
        participants=self.teams.Participants()
        chronos=self.teams.TotalTime()
        self.chart.removeSeries(self.series)
        self.series.clear()
        dur=self.teams.duration()
        data=dur.split(':')
        pieslicesplit=int(data[0])**2+1
        slices=[int(x)*30 for x in range(int(pieslicesplit)) if int(x)!=0]
        colors=Random_colors(pieslicesplit)
        #Threading Options not in single thread only
        for k in range(len(slices)):
            parts=[]
            for i in participants:
                if int(k)==0:
                    if int(int(i.TimeCount()/60))<=int(slices[int(k)]):
                        parts.append(i)
                else:
                    if int(int(i.TimeCount() / 60)) > int(slices[int(k)-1]) and int(i.TimeCount() / 60) <= int(slices[int(k)]):
                        parts.append(i)
            slice=QPieSlice()
            label=''
            text=slices[int(k)]
            if int(k)==0:
                label='<b style=\"font-size:18px;\">0-'+str(text)+' minutes</b>'
            else:
                label='<b style=\"font-size:18px;\">'+str(slices[int(k)-1]+1)+'-'+str(slices[int(k)])+' minutes</b>'
            slice.setLabel(label)
            slice.setColor(colors[k])
            percent=(len(parts)/len(participants))*100.0
            slice.setValue(percent)
            slice.setLabelVisible(True)
            slice.setLabelArmLengthFactor(0.27)
            self.series.append(slice)
        slice=QPieSlice()
        slice.setLabel('<b style=\"font-size:18px;\">'+str(slices[len(slices)-1]+1)+'> minutes</b>')
        slice.setColor(colors[len(colors)-1])
        parts = []
        for i in participants:
            if int(i.TimeCount()/60) > int(slices[len(slices)-1]):
                parts.append(i)
        slice.setValue((len(parts)/len(participants))*100.0)
        slice.setLabelVisible(True)
        slice.setLabelArmLengthFactor(0.27)
        self.series.append(slice)
        self.chart.addSeries(self.series)

    def Save(self):
        files=QFileDialog.getSaveFileName(self,'Save Chartview','.','image file (*.png)')
        if len(files)==0:
            QMessageBox.critical(self,'Error','<b>You did not select a file</b>')
            return
        self.view.grab().save(files[0])

    def printinfo(self):
        QMessageBox.information(self,'Lesson Information','<h2>'+str(self.information)+'</h2>')


    def __init__(self):
        super().__init__(None)
        #width=QDesktopWidget().geometry().width()/1.3
        #height=QDesktopWidget().geometry().height()/1.3
        self.setFixedSize(900,600)
        self.information=''
        self.teams=s.msteams(30)
        self.make_menu()
        self.setWindowTitle('Pie Chart view')
        self.chart=QChart()
        self.chart.setTitle("<b style=\"color:red; font-size:25px;\">Participation List</b>")
        self.series=QPieSeries()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.view=QChartView(self.chart)
        self.view.setStyleSheet('background-color:white; font-size:19px; color:blue;')
        self.setCentralWidget(self.view)
        self.show()

a=QApplication([''])
window()
a.exec()