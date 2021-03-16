#pip install PyQtChart
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from  PyQt5.QtChart import *
import session_teams as st
import sys

class window(QMainWindow):
    def pannel1(self):
        return

    def barPanel(self):
        return

    def Open(self):
        filename=QFileDialog.getOpenFileName(self,'Open Participation List','.','comma seperated value files (*.csv)')
        if len(filename[0])==0:
            QMessageBox.critical(self,'Error Message','<html><b style=\"color:red; font-size:18px;\">You did not select a file</html>')
            return
        print(filename[0])
        self.label.setText(self.teams.OpenFile(filename[0]))
        participants=self.teams.Participants()
        self.series.clear()
        self.chart.removeSeries(self.series)
        chronos = self.teams.TotalTime()
        c = 0
        categories = []
        aset =QBarSet("")
        for x in participants:
            categories.append(x.id)
            # Pass the values
            aset.append(chronos[int(c)])
            c += 1
        print(participants)
        self.series.append(aset)
        self.axisx =QBarCategoryAxis()
        self.axisx.append(categories)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.addAxis(self.axisx, Qt.AlignBottom)
        self.series.attachAxis(self.axisx)
        self.axisY =QValueAxis()
        self.axisY.setRange(min(chronos)/60, max(chronos)/60)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        self.series.attachAxis(self.axisY)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.addSeries(self.series)

    def save(self):
        filename=QFileDialog.getSaveFileName(self,'Save Image','.','image (*.png)')
        if len(filename[0])==0:
            QMessageBox.critical(self,'Image Error','<html><b>You did not select a file</b></html>')
            return
        self.view.grab().save(filename[0])

    def Close(self):
        sys.exit(0)

    def make_menu(self):
        self.men = QMenu('OPTIONS')
        ac1 = QAction('Open', self)
        ac2 = QAction('Save', self)
        ac3 = QAction('Close', self)
        self.men.addAction(ac1)
        self.men.addAction(ac2)
        self.men.addAction(ac3)
        ac1.triggered.connect(lambda: self.Open())
        ac2.triggered.connect(lambda: self.save())
        ac3.triggered.connect(lambda: self.Close())
        self.menuBar().addMenu(self.men)

    def __init__(self):
        super().__init__(None)
        self.teams=st.msteams(30)
        width=QDesktopWidget().geometry().width()/2
        height=QDesktopWidget().geometry().height()/1.3
        self.setFixedSize(width,height)
        self.setWindowTitle('MSTEAMS PARTICIPATION APP')
        self.mw=QWidget()
        self.make_menu()
        #self.lay=QStackedLayout()
        self.lay=QVBoxLayout()
        self.setCentralWidget(self.mw)
        self.mw.setLayout(self.lay)
        self.chart=QChart()
        self.chart.setTitle("<html><h3 style=\"color:blue;\">Participators BarChart Example</h3></html>")
        self.series=QBarSeries()
        self.chart.addSeries(self.series)
        self.view=QChartView(self.chart)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setStyleSheet('border:1px solid;')
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setFixedSize(0.96*self.width(),0.86*self.height())
        self.label=QLabel()
        self.lay.setAlignment(self.mw,Qt.AlignCenter)
        self.label.setStyleSheet('border:2px solid; font-weight:bold; font-size:19px; background-color:gray; color:blue; font-size:27px;')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(0.98*self.width(),0.3*self.height())
        self.lay.addWidget(self.label)
        self.lay.addWidget(self.view)