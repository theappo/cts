""" Left Panel for CTS """

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QToolButton, QMenu, QStackedWidget
from PyQt5.QtGui import QPixmap, QImage, QPalette, QIcon, QColor
from PyQt5.QtCore import Qt, QSize


class LeftPanel(QWidget):
    def __init__(self, parent):
        super(LeftPanel, self).__init__(parent)

        # set width and hight
        self.width = 86
        self.hight = 648

        # declare user picture label
        self.pic = QLabel(self)
        self.pic.setScaledContents(True)

        # declare contorl panel
        self.cp = QStackedWidget(self)

        # declare function button
        self.funcbutt = QToolButton(self)

        # start initUI
        self.initUI()

    def initUI(self):
        # set LeftPanel size
        self.setFixedSize(self.width, self.hight)

        # set background color
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(40,42,45))
        self.setPalette(palette)

        # set pic
        self.setpic("../img/unknown-user.png")
        # set pic size
        self.pic.setFixedSize(60, 60)
        # add pic to leftpanel
        self.pic.move(13, 13)

        # menu for funcbutt
        funcmenu = QMenu()
        funcmenu.addAction("System Statistic")
        funcmenu.addAction("Sign Out")
        # set funcbutt menu
        self.funcbutt.setMenu(funcmenu)
        self.funcbutt.setPopupMode(QToolButton.InstantPopup)
        # set image for funcbutt
        self.funcbutt.setIcon(QIcon("../img/menu-icon.png"))
        self.funcbutt.setIconSize(QSize(60, 30))
        # add funcbutt to leftpanel
        self.funcbutt.setFixedSize(61, 31)
        self.funcbutt.move(12, 610)

    def setpic(self, path):
        """ set pic to the path image"""
        if (path == None):
            pixmap = QPixmap("../img/unknown-user.png")
        else:
            pixmap = QPixmap(path)
        pixmap.scaled(60, 60)
        self.pic.setPixmap(pixmap)
