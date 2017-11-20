""" Left Panel for CTS """

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class LeftPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonList = []
        self.lay = QVBoxLayout()
        self.button1 = QPushButton("Button 1")
        self.buttonList = []

    def leftPanelUI(self):
        self.buttonList.append(self.button1)
        for button in self.buttonList:
            self.lay.addWidget(button)


def main():
    cts = QApplication(sys.argv)
    mainWindow = LeftPanel()
    mainWindow.show()
    sys.exit(cts.exec_())


main()
