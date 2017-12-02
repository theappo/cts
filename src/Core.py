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
from Application import *

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
        # connect singup button
        self.mainWindow.rightPanel.page0.signUPB.clicked.connect(self.signUp)
        # connect grand statistic button
        self.mainWindow.leftPanel.grandStat.triggered.connect(self.systemInfo)

    def setLeftPanel(self):
        if self.loginManager.currentUser == None:
            self.mainWindow.leftPanel.setpic("")
            self.mainWindow.leftPanel.controlPanel.setCurrentIndex(0)
            self.mainWindow.leftPanel.setFuncMenu(False)
        else:
            if type(self.loginManager.currentUser) is Developer:
                if self.loginManager.currentUser.get_transaction_history() == ():
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(1)
                else:
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(2)
            elif type(self.loginManager.currentUser) is Client:
                if self.loginManager.currentUser.get_transaction_history() == ():
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(3)
                else:
                    self.mainWindow.leftPanel.controlPanel.setCurrentIndex(4)
            else:
                self.mainWindow.leftPanel.controlPanel.setCurrentIndex(5)

            self.mainWindow.leftPanel.setpic(self.loginManager.currentUser.user_id)
            self.mainWindow.leftPanel.setFuncMenu(True)

    def login(self):
        msg = self.loginManager.login(self.mainWindow.rightPanel.page0.loginID.text(),
                                      self.mainWindow.rightPanel.page0.loginPW.text())
        # set GUI
        if self.loginManager.currentUser != None:
            self.setLeftPanel()

            if self.loginManager.currentUser.get_transaction_history() == ():
                db = GateWay()
                # TODO, fix active client and devs
                # TODO, add one more dev
                topC = db.get_active_clients(3)
                topD = db.get_active_devs(3)

                self.mainWindow.rightPanel.setCurrentIndex(1)
                print(topD)
                # self.mainWindow.rightPanel.page1.setTopClient(topC[0][0], topC[1][0], topC[2][0])
                # self.mainWindow.rightPanel.page1.setTopDev(topD[0][0], topD[1][0], topD[2][0])
            else:
                self.mainWindow.rightPanel.setCurrentIndex(2)
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

    def signUp(self):
        db = GateWay()

        if len(self.mainWindow.rightPanel.page0.signUpID.text()) < 6:
            QMessageBox.about(self.mainWindow, "Sorry", "ID must have length 6 or more")
        elif db.user_exists(self.mainWindow.rightPanel.page0.signUpID.text()):
            QMessageBox.about(self.mainWindow, "Sorry", "This ID already taken by others, try to use somthing else")
        elif len(self.mainWindow.rightPanel.page0.signUpPW.text()) < 6:
            QMessageBox.about(self.mainWindow, "Sorry", "Password must have length 6 or more")
        else:
            applyPage = Application(self.mainWindow)
            applyPage.setWindowFlags(QtCore.Qt.Window)
            applyPage.pushButton.clicked.connect(
                lambda: self.createNewUser(self.mainWindow.rightPanel.page0.signUpID.text(),
                                           self.mainWindow.rightPanel.page0.signUpPW.text(),
                                           applyPage.radioButton.isChecked(),
                                           applyPage.lineEdit.text(),
                                           applyPage.lineEdit_2.text(),
                                           applyPage.lineEdit_6.text()))
            applyPage.show()

    # fill in information to apply to be a user
    def createNewUser(self, userID, userPW, userType, email, address, money):
        if email == None or address == None or money == None:
            QMessageBox.about(self.mainWindow, "Sorry", "You Must Filled In Every Detail, Please Try Again")
        elif not money.isInt():
            QMessageBox.about(self.mainWindow, "Sorry", "Invalid Deposit Amount")
        else:
            db = GateWay()

            # TODO: delete/blacklist a user? how about their money?
            if userType:
                db.add_user(userID, userPW, money, 1, email, address)
            else:
                db.add_user(userID, userPW, money, 2, email, address)

    def systemInfo(self):
        db = GateWay()

        info = SystemInfo(self.mainWindow)
        # set dev and client num
        info.lcdNumber.display(db.get_dev_num())
        info.lcdNumber_2.display(db.get_client_num())
        # get top user id
        info.setTop(db.get_active_clients(1)[0][0], db.get_active_devs(1)[0][0])

        info.setWindowFlags(QtCore.Qt.Window)
        info.show()


def main():
    cts = QApplication(sys.argv)
    core = Core()
    core.mainWindow.show()
    sys.exit(cts.exec_())


main()
