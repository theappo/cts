""" MainWinow for cts """


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
        self.leftPanel.homeB0.clicked.connect(lambda: self.rightPanel.setCurrentIndex(0))
        self.leftPanel.homeB1.clicked.connect(lambda: self.rightPanel.setCurrentIndex(1))
        self.leftPanel.homeB2.clicked.connect(lambda: self.rightPanel.setCurrentIndex(2))
        self.leftPanel.homeB3.clicked.connect(lambda: self.rightPanel.setCurrentIndex(1))
        self.leftPanel.homeB4.clicked.connect(lambda: self.rightPanel.setCurrentIndex(2))

        self.leftPanel.searchB0.clicked.connect(lambda: self.rightPanel.setCurrentIndex(3))
        self.leftPanel.searchB1.clicked.connect(lambda: self.rightPanel.setCurrentIndex(3))
        self.leftPanel.searchB2.clicked.connect(lambda: self.rightPanel.setCurrentIndex(3))
        self.leftPanel.searchB3.clicked.connect(lambda: self.rightPanel.setCurrentIndex(3))
        self.leftPanel.searchB4.clicked.connect(lambda: self.rightPanel.setCurrentIndex(3))