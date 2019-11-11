# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:17:51 2019

@author: rshang
"""

import sys
from PyQt5.QtWidgets import QApplication
from Logic import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
   
