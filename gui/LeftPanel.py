""" Left Panel for CTS """
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QToolButton, QMenu, QFormLayout, QAction, QStackedWidget
from PyQt5.QtGui import QPixmap, QPalette, QIcon, QColor
from PyQt5.QtCore import Qt, QSize, QObjectCleanupHandler


class LeftPanel(QWidget):
    def __init__(self, width, hight, parent=None):
        super(LeftPanel, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        # declare path string
        self.unknownUser = "../img/unknown-user.png"
        self.menuIcon = "../img/menu-icon.png"

        # declare user picture label
        self.pic = QLabel(self)
        self.pic.setScaledContents(True)

        # declare control panel
        self.controlPanel = QStackedWidget(self)
        # declare control button
        # for visitor and temp user
        self.homeB0 = QPushButton("Home")
        self.searchB0 = QPushButton("Search")
        # for develop has no transaction history
        self.homeB1 = QPushButton("Home")
        self.searchB1 = QPushButton("Search")
        self.currentProjectB1 = QPushButton("Current Project")
        self.submitProjectB1 = QPushButton("Submit Project")
        self.messageB1 = QPushButton("Message")
        self.historyB1 = QPushButton("History")
        self.manageTeam1 = QPushButton("Team Manager")
        # for develop has transaction history
        self.homeB2 = QPushButton("Home")
        self.searchB2 = QPushButton("Search")
        self.currentProjectB2 = QPushButton("Current Project")
        self.submitProjectB2 = QPushButton("Submit Project")
        self.messageB2 = QPushButton("Message")
        self.historyB2 = QPushButton("History")
        self.manageTeam2 = QPushButton("Team Manager")
        # for client has no transaction history
        self.homeB3 = QPushButton("Home")
        self.searchB3 = QPushButton("Search")
        self.currentProjectB3 = QPushButton("Current Project")
        self.postProjectB3 = QPushButton("Post New Project")
        self.messageB3 = QPushButton("Message")
        self.historyB3 = QPushButton("History")
        # for client has transaction history
        self.homeB4 = QPushButton("Home")
        self.searchB4 = QPushButton("Search")
        self.currentProjectB4 = QPushButton("Current Project")
        self.postProjectB4 = QPushButton("Post New Project")
        self.messageB4 = QPushButton("Message")
        self.historyB4 = QPushButton("History")
        # TODO: super user buttons

        # declare function button
        self.funcbutt = QToolButton(self)
        self.mu = QMenu()
        # declare action
        self.personalInfo = QAction("Personal Information")
        self.grandStat = QAction("Grand Statistic")
        self.out = QAction("Sign Out")

        # start initUI
        self.initUI()

    def initUI(self):
        # set LeftPanel size
        self.setFixedSize(self.width, self.hight)

        # set LeftPanel background color
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(40, 42, 45))
        self.setPalette(palette)

        # set pic
        self.setpic(self.unknownUser)
        # set pic size
        self.pic.setFixedSize(self.width - 20, self.width - 20)
        # add pic to LeftPanel
        self.pic.move(10, 10)

        # set stackWidget size
        self.controlPanel.setFixedSize(self.width, self.hight - 250)
        # add visitor page to controlPanel
        v = QWidget()
        vly = QFormLayout()
        vly.addRow(self.homeB0)
        vly.addRow(self.searchB0)
        v.setLayout(vly)
        self.controlPanel.addWidget(v)
        # add dev has no transaction to controlpanel
        dnt = QWidget()
        dntly = QFormLayout()
        dntly.addRow(self.homeB1)
        dntly.addRow(self.searchB1)
        dntly.addRow(self.currentProjectB1)
        dntly.addRow(self.submitProjectB1)
        dntly.addRow(self.messageB1)
        dntly.addRow(self.historyB1)
        dntly.addRow(self.manageTeam1)
        dnt.setLayout(dntly)
        self.controlPanel.addWidget(dnt)
        # add dev has transaction to controlPanel
        dt = QWidget()
        dtly = QFormLayout()
        dtly.addRow(self.homeB2)
        dtly.addRow(self.searchB2)
        dtly.addRow(self.currentProjectB2)
        dtly.addRow(self.submitProjectB2)
        dtly.addRow(self.messageB2)
        dtly.addRow(self.historyB2)
        dtly.addRow(self.manageTeam2)
        dt.setLayout(dtly)
        self.controlPanel.addWidget(dt)
        # add client has no transaction
        cnt = QWidget()
        cntly = QFormLayout()
        cntly.addRow(self.homeB3)
        cntly.addRow(self.searchB3)
        cntly.addRow(self.currentProjectB3)
        cntly.addRow(self.postProjectB3)
        cntly.addRow(self.messageB3)
        cntly.addRow(self.historyB3)
        cnt.setLayout(cntly)
        self.controlPanel.addWidget(cnt)
        # add client has transaction
        ct = QWidget()
        ctly = QFormLayout()
        ctly.addRow(self.homeB4)
        ctly.addRow(self.searchB4)
        ctly.addRow(self.currentProjectB4)
        ctly.addRow(self.postProjectB4)
        ctly.addRow(self.messageB4)
        ctly.addRow(self.historyB4)
        ct.setLayout(ctly)
        self.controlPanel.addWidget(ct)
        # TODO: add superUser
        # add controlPanel to LeftPanel
        self.controlPanel.setCurrentIndex(0)
        self.controlPanel.move(0, 180)

        # set funcbutt menu
        self.setFuncMenu(False)
        self.funcbutt.setPopupMode(QToolButton.InstantPopup)
        self.funcbutt.setMenu(self.mu)
        # set image for funcbutt
        self.funcbutt.setIcon(QIcon(self.menuIcon))
        self.funcbutt.setIconSize(QSize(60, 30))
        # add funcbutt to LeftPanel
        self.funcbutt.setFixedSize(61, 31)
        self.funcbutt.move(39, self.hight - 43)
        # connect menu event

    def setpic(self, user_id):
        """ set pic to the path image"""
        pixmap = QPixmap("../resources/pictures/" + user_id)
        # when path not found
        if (pixmap.isNull()):
            pixmap = QPixmap(self.unknownUser)
        # scaled and set
        pixmap.scaled(60, 60, Qt.KeepAspectRatio)
        self.pic.setPixmap(pixmap)

    def setFuncMenu(self, login):
        if login:
            self.mu.clear()
            self.mu.addAction(self.grandStat)
            self.mu.addAction(self.personalInfo)
            self.mu.addAction(self.out)
        else:
            self.mu.clear()
            self.mu.addAction(self.grandStat)