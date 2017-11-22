""" Left Panel for CTS """

from PyQt5.QtWidgets import *


class RightPanel(QStackedWidget):
    def __init__(self, width, hight, parent=None):
        super(RightPanel, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        self.initUI()

    def initUI(self):
        # set RightPanel size
        self.setFixedSize(self.width, self.hight)
