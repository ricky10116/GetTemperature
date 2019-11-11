# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:18:12 2019

@author: rshang
"""

from PyQt5.QtWidgets import QMainWindow
from ABC import Ui_MainWindow
import GetTemperature as Gtemp


class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #self.actionExit.triggered.connect(self.onExitTriggered)

        #self.actionCopy.triggered.connect(self.onCopyTriggered)
        #self.actionPaste.triggered.connect(self.onPasteTriggered)
        #self.actionCut.triggered.connect(self.onCutTriggered)
    '''    
    def onExitTriggered(self):
        print('Exit triggered.')
        
    def onCopyTriggered(self):
        print('Copy triggered.')
        
    def onCutTriggered(self):
        print('Cut triggered.')
        
    def onPasteTriggered(self):
        print('Paste triggered.')
    '''  
    def slot1(self):
        city=self.comboBox.currentText()
        #print("city=",city)
        temp1=Gtemp.Gettemperature(city)
        #print("Temperature=",temp1)
        #self.setupui.label.setText("first line\nsecond line"
        #self.label.setText("1234567")
        #self.comboBox.currentText
        self.label.setText(temp1)
        
    def quit1(self):
        self.close()
        