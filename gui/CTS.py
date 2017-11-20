""" MainWinow for cts """

import sys
import LeftPanel

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from LeftPanel import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Coding Turk System')
        self.setGeometry(100, 80, 1024, 648)
        self.leftPanel = LeftPanel()
        self.leftPanel.setGeometry(50, 60, 100, 200)


def main():
    cts = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(cts.exec_())


main()
