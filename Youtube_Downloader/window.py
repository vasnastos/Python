from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import sys

resourcemanager=os.path.join("","Resources")

class window(QMainWindow):
    
    def Menu(self):
        menu=QMenu("APP")
        a1=QAction("Window",self)
        a1.triggered.connect(lambda:self.windowapp)
        a2=QAction("Settings",self)
        a2.triggered.connect(lambda:self.settings)
        a3=QAction("Exit",self)
        a3.triggered.connect(lambda:sys.exit(0))
        menu.addAction(a1)
        menu.addAction(a2)
        self.menuBar().addAction(a3)
    
    def __init__(self):
        QMainWindow.__init__(None)
        self.setFixedSize(600,600)
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon(os.path.join(resourcemanager,"central.jpg")))
        mw=QWidget()
        self.layout=QVBoxLayout()
        mw.setLayout(self.layout)
        self.setCentralWidget(mw)
        self.editl=QLineEdit()
        self.editl.setFixedSize(0.8*self.width())
        self.editl.setStyleSheet("QLineEdit"
                                 "{"
                                 "color:blue;"
                                 "border:1px lightgray;"
                                 "font-size:15px;"
                                 "font-weight:bold;"
                                 "}"
                                 "QLineEdit::hover()"
                                 "{"
                                 "font-weight:bold;"
                                 "font-size:16px;"
                                 "color:red;"
                                 "}"
                                 "")
        self.editl.setPlaceholderText("Insert The Youtube Link")
        self.b1=QPushButton()
        self.b1.setFixedWidth(0.1*self.width())
        self.b1.setStyleSheet("border:null")
        size=QSize(self.b1.width(),self.b1.height())
        self.b1.setIcon(os.path.join(resourcemanager,"download.png"))
        self.b1.setIconSize(size)
        self.b1.clicked.connect(lambda:self.download)
        lay=QHBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        lay.addWidget(self.editl)
        lay.addWidget(self.b1)
        self.layout.addLayout(lay)
        previewer=QWidget()
        previewer.setFixedSize(0.9*self.width(),0.2*self.height())
        lay1=QVBoxLayout()
        previewer.setLayout(lay1)
        lay1.setAlignment(Qt.AlignTop)
        youtubelabel=QLabel()
        youtubelabel.setFixedSize(0.3*self.width(),0.2*self.height())
        youtubelabel.setStyleSheet("border:none")
        discreaber=QLabel()
        discreaber.setFixedSize(0.7*self.width(),0.15*self.height())
        discreaber.setStyleSheet("border:2px solid; font-weight:bold; color:blue;")
        # Adding message to descreaber
        firstrow=QHBoxLayout()
        firstrow.addWidget(youtubelabel)
        firstrow.addSpacing(5)
        firstrow.addWidget(discreaber)
        lay1.addLayout(firstrow)
        self.layout.addWidget(previewer)        

        
    def windowapp(self):
        pass

    def settings(self):
        pass

    def download(self):
        pass

