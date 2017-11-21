""" Left Panel for CTS """

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.Qt import Qt


class LeftPanel(QWidget):
    def __init__(self, parent):
        super(LeftPanel, self).__init__(parent)

        # set layout manager to Vertical Box layout
        self.layout = QVBoxLayout(self)
        # declare user picture label
        self.pic = QLabel(self)
        # set width and hight
        self.width = 85
        self.hight = 648
        # start initUI
        self.initUI()

    def initUI(self):
        # set LeftPanel size
        self.setFixedSize(self.width, self.hight)
        # set background color
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(palette)
        # set pic
        self.setpic("../img/unknown-user.png")
        # set pic size
        self.pic.setFixedSize(60, 60)
        # add pic to layout



    def setpic(self, path):
        """ set pic to the path image"""
        pixmap = QPixmap(path)
        pixmap.scaled(64, 64)
        self.pic.setPixmap(pixmap)
