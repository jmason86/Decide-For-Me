"""Call the GUI and attach it to functions."""
__author__ = "James Paul Mason"
__contact__ = "jmason86@gmail.com"

import sys
import os
import logging
from PySide.QtGui import *
from PySide.QtCore import *
from ui_mainWindow import Ui_MainWindow
from PySide import QtCore, QtGui
import random

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()
    
    def assignWidgets(self):
        self.pushButton_decide.clicked.connect(self.decisionbuttonClicked)

    def decisionbuttonClicked(self):
        # Read in the options and parse them
        options = self.textEdit_inputBox.toPlainText().split(",")
    
        # Randomly choose and display an option
        self.label_result.setText(random.choice(options))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
