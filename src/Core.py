""" CTS core system, program start from here """

import sys

sys.path.insert(0, "../gui")

from MainWindow import *
from LoginManager import *
from User import *
from Developer import *
from Client import *
from GateWay import *

from SystemInfo import *

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtCore


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
        # connect logout button
        self.mainWindow.leftPanel.out.triggered.connect(self.logout)
        # connect grand statistic button
        self.mainWindow.leftPanel.grandStat.triggered.connect(self.systemInfo)

    def setLeftPanel(self):
        if self.loginManager.currentUser == None:
            self.mainWindow.leftPanel.setpic("")
            self.mainWindow.leftPanel.controlPanel.setCurrentIndex(0)
            self.mainWindow.leftPanel.setFuncMenu(False)
        else:
            if type(self.loginManager.currentUser) is Developer:
                if self.loginManager.currentUser.get_transaction_history == ():
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(1)
                else:
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(2)
            elif type(self.loginManager.currentUser) is Client:
                if self.loginManager.currentUser.get_transaction_history == ():
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(3)
                else:
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(4)
            else:
                self.mainWindow.leftPanel.controlPanel.setCurrentIndex(5)

            self.mainWindow.leftPanel.setpic("../resources/pictures/" + self.loginManager.currentUser.user_id)
            self.mainWindow.leftPanel.setFuncMenu(True)

    def login(self):
        msg = self.loginManager.login(self.mainWindow.rightPanel.page0.loginID.text(),
                                      self.mainWindow.rightPanel.page0.loginPW.text())
        # set GUI
        if self.loginManager.currentUser != None:

            self.setLeftPanel()
            # TODO: login error, check ==
            if self.loginManager.currentUser.get_transaction_history == ():
                self.mainWindow.rightPanel.setCurrentIndex(1)
                print(1)
            else:
                self.mainWindow.rightPanel.setCurrentIndex(2)
                print(self.loginManager.currentUser.get_transaction_history())
        # show message
        QMessageBox.about(self.mainWindow, "Message", msg)

    def logout(self):
        self.loginManager.log_out()

        self.setLeftPanel()

        self.mainWindow.rightPanel.setCurrentIndex(0)

        self.mainWindow.rightPanel.page0.loginID.clear()
        self.mainWindow.rightPanel.page0.loginPW.clear()

        # show message
        QMessageBox.about(self.mainWindow, "Message", "You have successfully logged out!")

    def systemInfo(self):
        db = GateWay()

        info = SystemInfo(self.mainWindow)
        info.lcdNumber.display(db.get_dev_num())
        info.lcdNumber_2.display(db.get_client_num())


        info.setWindowFlags(QtCore.Qt.Window)
        info.show()


def main():
    cts = QApplication(sys.argv)
    core = Core()
    core.mainWindow.show()
    sys.exit(cts.exec_())


main()
