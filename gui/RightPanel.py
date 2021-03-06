""" Left Panel for CTS """

from PyQt5.QtWidgets import QStackedWidget, QHBoxLayout, QWidget

from LoginSignup import *
from Top3 import *
from Interest import *
from SearchPage import *
from Messages import *
from History import *
from ClientProjs import *
from DevProjs import *
from SystemManager import *
from TeamPage import *


class RightPanel(QStackedWidget):
    def __init__(self, width, hight, parent=None):
        super(RightPanel, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        # declare page
        self.page0 = LoginSignup(300, 170)
        self.page1 = Top3()
        self.page2 = Interest()
        self.page3 = SearchPage()
        self.page4 = Messages()
        self.page5 = History()
        self.page6 = ClientProjs()
        self.page7 = DevProjs()
        self.page8 = SystemManager()
        self.page9 = TeamPage()

        self.initUI()

    def initUI(self):
        # set RightPanel size
        self.setFixedSize(self.width, self.hight)

        # add login page
        loginPage = QWidget()
        loginlayout = QHBoxLayout()
        loginlayout.addWidget(self.page0)
        loginPage.setLayout(loginlayout)
        self.addWidget(loginPage)

        # add top3 page
        self.addWidget(self.page1)

        # add interest page
        self.addWidget(self.page2)

        # add search page
        self.addWidget(self.page3)

        # add message page
        self.addWidget(self.page4)

        # add history page
        self.addWidget(self.page5)

        # add projects page for client
        self.addWidget(self.page6)

        # add projects page for developer
        self.addWidget(self.page7)

        # add SystemManager Page for super user
        self.addWidget(self.page8)

        # add team page
        self.addWidget(self.page9)