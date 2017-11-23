""" Left Panel for CTS """

import LoginSignup

from PyQt5.QtWidgets import QStackedWidget, QHBoxLayout, QWidget
from LoginSignup import *


class RightPanel(QStackedWidget):
    def __init__(self, width, hight, parent=None):
        super(RightPanel, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        # declare page
        self.login = LoginSignup(300, 170)

        self.initUI()

    def initUI(self):
        # set RightPanel size
        self.setFixedSize(self.width, self.hight)

        # add login page
        loginPage = QWidget()
        loginlayout = QHBoxLayout()
        loginlayout.addWidget(self.login)
        loginPage.setLayout(loginlayout)
        self.addWidget(loginPage)

