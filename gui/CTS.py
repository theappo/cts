""" MainWinow for cts """

import sys
import LeftPanel
import RightPanel

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from LeftPanel import *
from RightPanel import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        # MainWindown belong None
        super(MainWindow, self).__init__(parent)

        # set layout manager to be Horizontal Box layout
        self.layout = QHBoxLayout()

        # declare LeftPanel
        self.leftPanel = LeftPanel(140, 648, self)

        # declare RightPanel
        self.rightPanel = RightPanel(884, 648, self)

        # start initUI
        self.initUI()

    def initUI(self):
        # set title and size of MainWindow
        self.setWindowTitle('Coding Turk System')
        self.setGeometry(100, 80, 1024, 648)

        # move rightPanel to the correct position
        self.rightPanel.move(141, 0)

        # connect signal
        self.leftPanel.homeB.clicked.connect(lambda: self.rightPanel.setCurrentIndex(0))
        self.leftPanel.searchB.clicked.connect(lambda: self.rightPanel.setCurrentIndex(1))
        self.leftPanel.currentProjectB.clicked.connect(lambda: self.rightPanel.setCurrentIndex(2))
        self.leftPanel.submitProjectB.clicked.connect(lambda: self.rightPanel.setCurrentIndex(3))
        self.leftPanel.postProjectB.clicked.connect(lambda: self.rightPanel.setCurrentIndex(4))
        self.leftPanel.messageB.clicked.connect(lambda: self.rightPanel.setCurrentIndex(5))
        self.leftPanel.historyB.clicked.connect(lambda: self.rightPanel.setCurrentIndex(6))
        self.leftPanel.manageTeam.clicked.connect(lambda: self.rightPanel.setCurrentIndex(7))

    def setControlIndex(self, i):
        """ set LeftPanel.controlPabel.index """
        self.leftPanel.setControlPanel(i)


def main():
    cts = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    # disable resize
    mainWindow.setFixedSize(1024, 648)
    sys.exit(cts.exec_())


main()
