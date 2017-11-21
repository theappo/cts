""" MainWinow for cts """

import sys
import LeftPanel

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from PyQt5.QtGui import QPalette
from LeftPanel import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        # MainWindown belong None
        super(MainWindow, self).__init__(parent)

        # set layout manager to be Horizontal Box layout
        self.layout = QHBoxLayout()
        # declare leftPanel
        self.leftPanel = LeftPanel(self)
        # start initUI
        self.initUI()

    def initUI(self):
        # set title and size of MainWindow
        self.setWindowTitle('Coding Turk System')
        self.setGeometry(100, 80, 1024, 648)
        # add leftPanel to layout manager
        self.layout.addWidget(self.leftPanel)


def main():
    cts = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    # disable resize
    mainWindow.setFixedSize(1024, 648)
    sys.exit(cts.exec_())


main()
