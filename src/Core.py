""" CTS core system, program start from here """

import sys

sys.path.insert(0, "../gui")

from MainWindow import *
from LoginManager import *
from User import *
from Developer import *
from Client import *

from PyQt5.QtWidgets import QApplication, QMessageBox


class Core():
    def __init__(self):
        self.loginManager = LoginManager()
        self.mainWindow = MainWindow()

        self.setup()

    def setup(self):
        # set size of mainWindow
        self.mainWindow.setFixedSize(1024, 648)
        # init leftpanel button
        self.setLeftPanel()

        # connect login button
        self.mainWindow.rightPanel.page0.loginB.clicked.connect(self.login)

    def setLeftPanel(self):
        if self.loginManager.currentUser == None:
            self.mainWindow.leftPanel.setControlPanel(0)
        elif type(self.loginManager.currentUser) is Developer:
            if self.loginManager.currentUser.get_transaction_history == ():
                self.mainWindow.leftPanel.setControlPanel(1)
            else:
                self.mainWindow.leftPanel.setControlPanel(2)
        elif type(self.loginManager.currentUser) is Client:
            if self.loginManager.currentUser.get_transaction_history == ():
                self.mainWindow.leftPanel.setControlPanel(3)
            else:
                self.mainWindow.leftPanel.setControlPanel(4)
        else:
            self.mainWindow.leftPanel.setControlPanel(5)

    def login(self):
        msg = self.loginManager.login(self.mainWindow.rightPanel.page0.loginID.text(),
                                      self.mainWindow.rightPanel.page0.loginPW.text())
        # set GUI
        if self.loginManager.currentUser != None:

            self.mainWindow.leftPanel.setpic("../resources/pictures/" + self.loginManager.currentUser.user_id)

            self.setLeftPanel()

            if self.loginManager.currentUser.get_transaction_history == ():
                self.mainWindow.rightPanel.setCurrentIndex(1)
            else:
                self.mainWindow.rightPanel.setCurrentIndex(2)
        # show message
        QMessageBox.about(self.mainWindow, "Message", msg)


def main():
    cts = QApplication(sys.argv)
    core = Core()
    core.mainWindow.show()
    sys.exit(cts.exec_())


main()
