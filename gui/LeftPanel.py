""" Left Panel for CTS """

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QToolButton, QMenu, QFormLayout
from PyQt5.QtGui import QPixmap, QPalette, QIcon, QColor
from PyQt5.QtCore import Qt, QSize, QObjectCleanupHandler


class LeftPanel(QWidget):
    def __init__(self, parent):
        super(LeftPanel, self).__init__(parent)

        # set width and hight
        self.width = 140
        self.hight = 648

        # declare path string
        self.unknownUser = "../img/unknown-user.png"
        self.menuIcon = "../img/menu-icon.png"

        # declare user picture label
        self.pic = QLabel(self)
        self.pic.setScaledContents(True)

        # declare control panel
        self.controlPanel = QWidget(self)
        # declare control button
        self.homeB = QPushButton("Home")
        self.searchB = QPushButton("Search")
        self.currentProjectB = QPushButton("Current Project")
        self.submitProjectB = QPushButton("Submit Project")
        self.manageTeam = QPushButton("Team Manager")
        self.postProjectB = QPushButton("Post New Project")
        self.messageB = QPushButton("Message")
        self.historyB = QPushButton("History")
        # TODO: super user buttons
        # declare button list
        self.vblist = [self.homeB, self.searchB]
        self.dblist = [self.homeB, self.searchB, self.currentProjectB, self.submitProjectB, self.messageB,
                       self.historyB, self.manageTeam]
        self.cblist = [self.homeB, self.searchB, self.currentProjectB, self.postProjectB, self.messageB,
                       self.historyB]
        self.sublist = []

        # declare function button
        self.funcbutt = QToolButton(self)

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
        self.pic.setFixedSize(120, 120)
        # add pic to LeftPanel
        self.pic.move(10, 10)

        # set stackWidget size
        self.controlPanel.setFixedSize(self.width, self.hight - 250)
        # add controlPanel to LeftPanel
        self.setControlPanel(0)
        self.controlPanel.move(0, 180)

        # menu for funcbutt
        funcmenu = QMenu()
        funcmenu.addAction("Personal Information")
        funcmenu.addAction("System Statistic")
        funcmenu.addAction("Sign Out")
        # set funcbutt menu
        self.funcbutt.setMenu(funcmenu)
        self.funcbutt.setPopupMode(QToolButton.InstantPopup)
        # set image for funcbutt
        self.funcbutt.setIcon(QIcon(self.menuIcon))
        self.funcbutt.setIconSize(QSize(60, 30))
        # add funcbutt to LeftPanel
        self.funcbutt.setFixedSize(61, 31)
        self.funcbutt.move(39, 605)

    def setpic(self, path):
        """ set pic to the path image"""
        pixmap = QPixmap(path)
        # when path not found
        if (pixmap.isNull()):
            pixmap = QPixmap(self.unknowUser)
        # scaled and set
        pixmap.scaled(60, 60, Qt.KeepAspectRatio)
        self.pic.setPixmap(pixmap)

    def setControlPanel(self, i):
        """set controlPanle widget index"""
        layout = QFormLayout()

        if (i == 0):
            for button in self.vblist:
                layout.addRow(button)
        if (i == 1):
            for button in self.dblist:
                layout.addRow(button)
        if (i == 2):
            for button in self.cblist:
                layout.addRow(button)
        if (i == 3):
            for button in self.sublist:
                layout.addRow(button)

        # delete and add layout to controlPanel
        QObjectCleanupHandler().add(self.controlPanel.layout())
        self.controlPanel.setLayout(layout)

    def ControlPanelSignal(self):