""" panel for system information """
import sys

from PyQt5.QtWidgets import QWidget, QTabWidget, QLCDNumber, QLabel, QFormLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QPixmap


class SystemInfo(QTabWidget):
    def __init__(self, width, hight, parent=None):
        super(SystemInfo, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        # add UserStatistic
        self.us = UserStatistic(self.width, self.hight)

        self.initUI()

    def initUI(self):
        # set Systeminfo size
        self.setFixedSize(self.width, self.hight)

        # add tabs
        self.addTab(self.us, "User Statistic")


class UserStatistic(QWidget):
    def __init__(self, width, hight, parent=None):
        super(UserStatistic, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        # LCD number
        self.developNum = QLCDNumber()
        self.clienNum = QLCDNumber()

        # user detail for the "most"
        self.developPic = QPixmap()
        self.clienPic = QPixmap
        self.developID = QLabel()
        self.clienID = QLabel()

        self.initUI()

    def initUI(self):



def main():
    cts = QApplication(sys.argv)
    mainWindow = SystemInfo(300, 200)
    mainWindow.show()
    sys.exit(cts.exec_())


main()
