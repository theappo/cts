""" CTS core system, program start from here """

import sys
import datetime
import shutil

sys.path.insert(0, "../gui")

from MainWindow import *
from LoginManager import *
from SearchEngine import *
from ApplicationManager import *
from TeamManager import *
from User import *
from Developer import *
from Client import *
from GateWay import *

from SystemInfo import *
from Application import *
from Application2 import *
from UserInfo import *
from TeamInfo import *
from NewMessage import *
from Pd import *
from NotLow import *
from Rating import *

from shutil import copyfile

from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QFileDialog, QInputDialog, QLineEdit
from PyQt5 import QtCore


class Core():
    def __init__(self):
        self.db = GateWay()
        self.loginManager = LoginManager()
        self.searchEngine = SearchEngine()
        self.appManager = ApplicationManager()
        self.teamManager = TeamManager()
        self.mainWindow = MainWindow()

        self.applyPage = Application(self.mainWindow)
        self.applyPage.setWindowFlags(QtCore.Qt.Window)
        self.applyPage2 = Application2(self.mainWindow)
        self.applyPage2.setWindowFlags(QtCore.Qt.Window)

        self.userInfo = UserInfo(self.mainWindow)
        self.userInfo.setWindowFlags(QtCore.Qt.Window)
        self.teamInfo = TeamInfo(self.mainWindow)
        self.teamInfo.setWindowFlags(QtCore.Qt.Window)

        self.newMessage = NewMessage(self.mainWindow)
        self.newMessage.setWindowFlags(QtCore.Qt.Window)

        self.info = Pd(self.mainWindow)
        self.info.setWindowFlags(QtCore.Qt.Window)

        self.notlow = NotLow(self.mainWindow)
        self.notlow.setWindowFlags(QtCore.Qt.Window)

        self.rating = Rating()
        self.rating.setWindowFlags(QtCore.Qt.Window)

        # temp varibales
        self.pendingprojects = ()
        self.indiv_bid = ()
        self.team_bid = ()
        self.current_indiv_projects = ()
        self.current_team_projects = ()
        self.submited_indiv_projects = ()
        self.submited_team_projects = ()

        self.devCurrProj = ()
        self.needReview = ()
        self.bidProj = ()

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
        # connect personal information button
        self.mainWindow.leftPanel.personalInfo.triggered.connect(self.personalInfo)
        # connect Pd delete account button
        self.info.pushButton_4.clicked.connect(self.deleteAcount)
        # connect singup button
        self.mainWindow.rightPanel.page0.signUPB.clicked.connect(self.signUp)
        # connect applyPage confirm button
        self.applyPage.pushButton.clicked.connect(self.createNewUser)
        # connect applyPage2 confirm button
        self.applyPage2.pushButton_4.clicked.connect(self.moreDeatil)
        # connect searchPage search button
        self.mainWindow.rightPanel.page3.pushButton.clicked.connect(self.search)
        # connect searchPage user Detail button
        self.mainWindow.rightPanel.page3.pushButton_2.clicked.connect(self.viewUserInfo)
        # connect searchPage team Detail button
        self.mainWindow.rightPanel.page3.pushButton_3.clicked.connect(self.viewTeamInfo)
        # connect the message button to refresh message page
        self.mainWindow.leftPanel.messageB1.clicked.connect(self.refreshMessage)
        self.mainWindow.leftPanel.messageB2.clicked.connect(self.refreshMessage)
        self.mainWindow.leftPanel.messageB3.clicked.connect(self.refreshMessage)
        self.mainWindow.leftPanel.messageB4.clicked.connect(self.refreshMessage)
        # connect message Page refresh button
        self.mainWindow.rightPanel.page4.pushButton_2.clicked.connect(self.refreshMessage)
        # connect message Page new message button
        self.mainWindow.rightPanel.page4.pushButton_4.clicked.connect(self.showNewMessage)
        # connect newMessage send button
        self.newMessage.pushButton.clicked.connect(self.sendNewMessage)
        # connect client project button
        self.mainWindow.leftPanel.ProjectB3.clicked.connect(self.refreshClientProject)
        self.mainWindow.leftPanel.ProjectB4.clicked.connect(self.refreshClientProject)
        # connect client project table1
        self.mainWindow.rightPanel.page6.tableWidget.itemClicked.connect(self.setbidtables)
        # connect client select this developer button
        self.mainWindow.rightPanel.page6.pushButton_3.clicked.connect(self.choosedev)
        self.mainWindow.rightPanel.page6.pushButton_4.clicked.connect(self.chooseTeam)
        # connect client project post new project table
        self.mainWindow.rightPanel.page6.pushButton_2.clicked.connect(self.postNewProject)
        # connect client download button
        self.mainWindow.rightPanel.page6.pushButton_5.clicked.connect(self.clientReview)
        # connect rating buttion
        self.rating.pushButton.clicked.connect(self.lowrating)
        # connect developer project button
        self.mainWindow.leftPanel.ProjectB1.clicked.connect(self.refreshDevProject)
        self.mainWindow.leftPanel.ProjectB2.clicked.connect(self.refreshDevProject)
        # connect developer project page refresh button
        self.mainWindow.rightPanel.page7.pushButton_4.clicked.connect(self.refreshDevProject)
        # connect developer project page submit project button
        self.mainWindow.rightPanel.page7.pushButton.clicked.connect(self.submitProj)
        # connect developer project page review client button
        self.mainWindow.rightPanel.page7.pushButton_2.clicked.connect(self.devReview)
        # connect developer project page bid project button
        self.mainWindow.rightPanel.page7.pushButton_3.clicked.connect(self.palceBid)
        # connect developer project page bid team project button
        self.mainWindow.rightPanel.page7.pushButton_5.clicked.connect(self.palceteamBid)
        # connect history button
        self.mainWindow.leftPanel.historyB1.clicked.connect(self.refreshHistory)
        self.mainWindow.leftPanel.historyB2.clicked.connect(self.refreshHistory)
        self.mainWindow.leftPanel.historyB3.clicked.connect(self.refreshHistory)
        self.mainWindow.leftPanel.historyB4.clicked.connect(self.refreshHistory)
        # connect grand statistic button
        self.mainWindow.leftPanel.grandStat.triggered.connect(self.systemInfo)
        # connect superUser panel
        self.mainWindow.leftPanel.manage.clicked.connect(self.refreshManage)
        # connect superUser accept application button
        self.mainWindow.rightPanel.page8.pushButton.clicked.connect(self.acceptApp)
        # connect superUser reject application button
        self.mainWindow.rightPanel.page8.pushButton_2.clicked.connect(self.rejectApp)
        # connect superUser change review button
        self.mainWindow.rightPanel.page8.pushButton_7.clicked.connect(self.changeReview)
        # connect superUser add blacklist button
        self.mainWindow.rightPanel.page8.pushButton_3.clicked.connect(self.addToBlacklist)
        # connect superUser remove blacklist button
        self.mainWindow.rightPanel.page8.pushButton_4.clicked.connect(self.removeBlacklist)
        # connect superUser rest warning button
        self.mainWindow.rightPanel.page8.pushButton_5.clicked.connect(self.resetwarning)
        # connect team page
        self.mainWindow.leftPanel.manageTeam1.clicked.connect(self.refreshTeam)
        self.mainWindow.leftPanel.manageTeam2.clicked.connect(self.refreshTeam)
        # connect team current project table
        self.mainWindow.rightPanel.page9.tableWidget.itemClicked.connect(self.refreshteamcurrentprojct)
        # connect team page review button
        self.mainWindow.rightPanel.page9.pushButton_3.clicked.connect(self.devReview)
        # connect team page join team button
        self.mainWindow.rightPanel.page9.pushButton.clicked.connect(self.jointeam)
        # connect team page create team button
        self.mainWindow.rightPanel.page9.pushButton_5.clicked.connect(self.createteam)
        # connect team page submit project button
        self.mainWindow.rightPanel.page9.pushButton_4.clicked.connect(self.submitteamProj)

        # connect rating submit button
        self.rating.pushButton.clicked.connect(self.createReview)

    def setLeftPanel(self):
        if self.loginManager.currentUser == None:
            self.mainWindow.leftPanel.setpic("")
            self.mainWindow.leftPanel.controlPanel.setCurrentIndex(0)
            self.mainWindow.leftPanel.setFuncMenu(False)
        elif self.loginManager.currentUser.check_application():
            self.mainWindow.leftPanel.controlPanel.setCurrentIndex(6)
            self.mainWindow.leftPanel.setFuncMenu(True)
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

            if type(self.loginManager.currentUser) is SuperUser:
                self.refreshManage()
                self.mainWindow.rightPanel.setCurrentIndex(8)
            else:
                if self.loginManager.currentUser.get_transaction_history() == ():
                    topC = self.db.get_active_clients(3)
                    topD = self.db.get_active_devs(3)

                    self.mainWindow.rightPanel.setCurrentIndex(1)

                    self.mainWindow.rightPanel.page1.setTopClient(topC[0][0], topC[1][0], topC[2][0])
                    self.mainWindow.rightPanel.page1.setTopDev(topD[0][0], topD[1][0], topD[2][0])
                else:
                    self.mainWindow.rightPanel.setCurrentIndex(2)
                    self.mainWindow.rightPanel.page2.setUser(
                        self.db.get_similar_interests(self.loginManager.currentUser.user_id))

                if self.loginManager.currentUser.interests() == (
                        0, 0, 0, 0, 0, 0) and not self.loginManager.currentUser.check_application():
                    self.applyPage2.show()

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

        if len(self.mainWindow.rightPanel.page0.signUpID.text()) < 6:
            QMessageBox.about(self.mainWindow, "Sorry", "ID must have length 6 or more")
        elif self.db.user_exists(self.mainWindow.rightPanel.page0.signUpID.text()):
            QMessageBox.about(self.mainWindow, "Sorry", "This ID already taken by others, try to use somthing else")
        elif len(self.mainWindow.rightPanel.page0.signUpPW.text()) < 6:
            QMessageBox.about(self.mainWindow, "Sorry", "Password must have length 6 or more")
        elif self.db.check_blacklist(self.mainWindow.rightPanel.page0.signUpID.text()):
            # if this user was add into the blacklist a year ago, then his can login again
            if self.db.get_black_list(self.mainWindow.rightPanel.page0.signUpID.text())[1] < str(
                    datetime.date.today().replace(year=datetime.date.today().year - 1)):
                self.db.remove_blacklist(self.mainWindow.rightPanel.page0.signUpID.text())
                QMessageBox.about(self.mainWindow, "Message", "Welcome back! You are removed from blacklist")
            else:
                QMessageBox.about(self.mainWindow, "Error", "You are in blacklist")
        else:
            self.applyPage.show()

    # fill in information to apply to be a user
    def createNewUser(self):
        userID = self.mainWindow.rightPanel.page0.signUpID.text()
        userPW = self.mainWindow.rightPanel.page0.signUpPW.text()
        userType = int(self.applyPage.radioButton.isChecked()) + 1
        email = self.applyPage.lineEdit.text()
        address = self.applyPage.lineEdit_2.text()
        balance = self.applyPage.lineEdit_6.text()

        try:
            val = float(balance)
        except ValueError:
            QMessageBox.about(self.mainWindow, "Sorry", "Invalid Deposit Amount")

        if email == None or address == None or balance == None:
            QMessageBox.about(self.mainWindow, "Sorry", "You Must Filled In Every Detail, Please Try Again")
        else:

            self.db.add_user(userID, userPW, balance, userType, email, address)

            self.applyPage.close()

    def moreDeatil(self):
        if self.applyPage2.picpath != ('', ''):
            copyfile(self.applyPage2.picpath[0],
                     "../resources/pictures/" + self.loginManager.currentUser.user_id + ".png")
        if self.applyPage2.resumepath != ('', ''):
            copyfile(self.applyPage2.resumepath[0],
                     "../resources/resumes/" + self.loginManager.currentUser.user_id + ".pdf")
        if self.applyPage2.adpath != ('', ''):
            copyfile(self.applyPage2.adpath[0],
                     "../resources/AdInfo/" + self.loginManager.currentUser.user_id + ".pdf")

        IOS = int(self.applyPage2.checkBox.isChecked())
        Android = int(self.applyPage2.checkBox_2.isChecked())
        Desktop = int(self.applyPage2.checkBox_3.isChecked())
        Java = int(self.applyPage2.checkBox_4.isChecked())
        Python = int(self.applyPage2.checkBox_5.isChecked())
        Cpp = int(self.applyPage2.checkBox_6.isChecked())

        self.db.update_user_interests(self.loginManager.currentUser.user_id, Java, Python, Cpp, IOS, Android, Desktop)

        self.applyPage2.close()

    def search(self):
        self.searchEngine.search(self.mainWindow.rightPanel.page3.lineEdit.text())

        # clear all content
        self.mainWindow.rightPanel.page3.tableWidget.setRowCount(0)
        self.mainWindow.rightPanel.page3.tableWidget_2.setRowCount(0)
        self.mainWindow.rightPanel.page3.tableWidget_3.setRowCount(0)
        self.mainWindow.rightPanel.page3.tableWidget_4.setRowCount(0)

        # set user
        for user in self.searchEngine.users:
            rowPosition = self.mainWindow.rightPanel.page3.tableWidget.rowCount()
            self.mainWindow.rightPanel.page3.tableWidget.insertRow(rowPosition)
            self.mainWindow.rightPanel.page3.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(user.user_id))
            self.mainWindow.rightPanel.page3.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(user.type()))
            self.mainWindow.rightPanel.page3.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(user.rating())))

        for team in self.searchEngine.teams:
            memberlist = team.get_team_members()
            rowPosition = self.mainWindow.rightPanel.page3.tableWidget_2.rowCount()
            self.mainWindow.rightPanel.page3.tableWidget_2.insertRow(rowPosition)
            self.mainWindow.rightPanel.page3.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(team.team_id))
            self.mainWindow.rightPanel.page3.tableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(str(memberlist[0])))
            self.mainWindow.rightPanel.page3.tableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(str(memberlist[1])))
            self.mainWindow.rightPanel.page3.tableWidget_2.setItem(rowPosition, 3, QTableWidgetItem(str(memberlist[2])))
            self.mainWindow.rightPanel.page3.tableWidget_2.setItem(rowPosition, 4, QTableWidgetItem(str(memberlist[3])))
            self.mainWindow.rightPanel.page3.tableWidget_2.setItem(rowPosition, 5, QTableWidgetItem(str(memberlist[4])))

        for i in range(len(self.searchEngine.idprojs)):
            rowPosition = self.mainWindow.rightPanel.page3.tableWidget_3.rowCount()
            self.mainWindow.rightPanel.page3.tableWidget_3.insertRow(rowPosition)
            self.mainWindow.rightPanel.page3.tableWidget_3.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(self.searchEngine.idprojs[i][0]))
            self.mainWindow.rightPanel.page3.tableWidget_3.setItem(rowPosition, 1,
                                                                   QTableWidgetItem(self.searchEngine.idprojs[i][1]))
            self.mainWindow.rightPanel.page3.tableWidget_3.setItem(rowPosition, 2,
                                                                   QTableWidgetItem(self.searchEngine.idprojs[i][2]))
            self.mainWindow.rightPanel.page3.tableWidget_3.setItem(rowPosition, 3,
                                                                   QTableWidgetItem(self.searchEngine.idprojs[i][3]))
            self.mainWindow.rightPanel.page3.tableWidget_3.setItem(rowPosition, 4,
                                                                   QTableWidgetItem(
                                                                       str(self.searchEngine.idprojs[i][4])))

        for i in range(len((self.searchEngine.teamprojs))):
            rowPosition = self.mainWindow.rightPanel.page3.tableWidget_4.rowCount()
            self.mainWindow.rightPanel.page3.tableWidget_4.insertRow(rowPosition)
            self.mainWindow.rightPanel.page3.tableWidget_4.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(self.searchEngine.teamprojs[i][0]))
            self.mainWindow.rightPanel.page3.tableWidget_4.setItem(rowPosition, 1,
                                                                   QTableWidgetItem(self.searchEngine.teamprojs[i][1]))
            self.mainWindow.rightPanel.page3.tableWidget_4.setItem(rowPosition, 2,
                                                                   QTableWidgetItem(self.searchEngine.teamprojs[i][2]))
            self.mainWindow.rightPanel.page3.tableWidget_4.setItem(rowPosition, 3,
                                                                   QTableWidgetItem(self.searchEngine.teamprojs[i][3]))
            self.mainWindow.rightPanel.page3.tableWidget_4.setItem(rowPosition, 4,
                                                                   QTableWidgetItem(
                                                                       str(self.searchEngine.teamprojs[i][4])))

    def viewUserInfo(self):
        try:
            user = self.searchEngine.users[self.mainWindow.rightPanel.page3.tableWidget.currentItem().row()]

            self.userInfo.setpic(user.user_id)
            self.userInfo.lineEdit.setText(user.get_email())
            self.userInfo.lineEdit_2.setText(user.get_address())

            interest = user.interests()
            if interest[0]:
                self.userInfo.checkBox.setChecked(True)
            if interest[1]:
                self.userInfo.checkBox_2.setChecked(True)
            if interest[2]:
                self.userInfo.checkBox_3.setChecked(True)
            if interest[3]:
                self.userInfo.checkBox_4.setChecked(True)
            if interest[4]:
                self.userInfo.checkBox_5.setChecked(True)
            if interest[5]:
                self.userInfo.checkBox_6.setChecked(True)

            reviews = user.get_review()

            self.userInfo.tableWidget.setRowCount(0)

            for review in reviews:
                rowPosition = self.userInfo.tableWidget.rowCount()
                self.userInfo.tableWidget.insertRow(rowPosition)
                self.userInfo.tableWidget.setItem(rowPosition, 0,
                                                  QTableWidgetItem(review[0]))
                self.userInfo.tableWidget.setItem(rowPosition, 1,
                                                  QTableWidgetItem(str(review[4])))
                self.userInfo.tableWidget.setItem(rowPosition, 2,
                                                  QTableWidgetItem(review[1]))
                self.userInfo.tableWidget.setItem(rowPosition, 3,
                                                  QTableWidgetItem(review[3]))

            self.userInfo.show()
        except AttributeError:
            pass

    def viewTeamInfo(self):
        team = self.searchEngine.teams[self.mainWindow.rightPanel.page3.tableWidget_2.currentItem().row()]
        try:
            for project in team.get_history_projects():
                print(project)
                rowPosition = self.teamInfo.tableWidget.rowCount()
                self.teamInfo.tableWidget.insertRow(rowPosition)
                self.teamInfo.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(project[0]))
                self.teamInfo.tableWidget.setItem(rowPosition, 1, (QTableWidgetItem(project[1])))
                self.teamInfo.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(project[10]))
                self.teamInfo.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(project[8])))
                self.teamInfo.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(project[2]))
            self.teamInfo.show()
        except AttributeError:
            pass

    def refreshMessage(self):
        inbox = self.loginManager.currentUser.get_inbox_message()

        # clear all content
        self.mainWindow.rightPanel.page4.tableWidget.setRowCount(0)
        self.mainWindow.rightPanel.page4.tableWidget_2.setRowCount(0)

        for im in inbox:
            rowPosition = self.mainWindow.rightPanel.page4.tableWidget.rowCount()
            self.mainWindow.rightPanel.page4.tableWidget.insertRow(rowPosition)
            self.mainWindow.rightPanel.page4.tableWidget.setItem(rowPosition, 0,
                                                                 QTableWidgetItem(im[0]))
            self.mainWindow.rightPanel.page4.tableWidget.setItem(rowPosition, 1,
                                                                 QTableWidgetItem(str(im[2])))
            self.mainWindow.rightPanel.page4.tableWidget.setItem(rowPosition, 2,
                                                                 QTableWidgetItem(im[1]))

        sent = self.loginManager.currentUser.get_sent_message()

        for sm in sent:
            rowPosition = self.mainWindow.rightPanel.page4.tableWidget_2.rowCount()
            self.mainWindow.rightPanel.page4.tableWidget_2.insertRow(rowPosition)
            self.mainWindow.rightPanel.page4.tableWidget_2.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(sm[0]))
            self.mainWindow.rightPanel.page4.tableWidget_2.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(str(sm[2]))))
            self.mainWindow.rightPanel.page4.tableWidget_2.setItem(rowPosition, 2,
                                                                   QTableWidgetItem(sm[1]))

    def showNewMessage(self):
        self.newMessage.show()

    def sendNewMessage(self):
        if self.db.user_exists(self.newMessage.lineEdit.text()):
            self.loginManager.currentUser.new_message(self.newMessage.lineEdit.text(),
                                                      self.newMessage.textEdit.toPlainText())
            self.newMessage.close()
        else:
            QMessageBox.about(self.mainWindow, "Error", "User does not exists, please check")

    def refreshClientProject(self):
        # clear all content
        self.mainWindow.rightPanel.page6.tableWidget.setRowCount(0)
        self.mainWindow.rightPanel.page6.tableWidget_4.setRowCount(0)
        self.mainWindow.rightPanel.page6.tableWidget_5.setRowCount(0)

        self.pendingprojects = self.loginManager.currentUser.pending_projects()

        for project in self.pendingprojects:
            rowPosition = self.mainWindow.rightPanel.page6.tableWidget.rowCount()
            self.mainWindow.rightPanel.page6.tableWidget.insertRow(rowPosition)
            self.mainWindow.rightPanel.page6.tableWidget.setItem(rowPosition, 0,
                                                                 QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page6.tableWidget.setItem(rowPosition, 1,
                                                                 (QTableWidgetItem(project[2])))

        self.current_indiv_projects = self.loginManager.currentUser.current_indiv_projects()

        for project in self.current_indiv_projects:
            rowPosition = self.mainWindow.rightPanel.page6.tableWidget_4.rowCount()
            self.mainWindow.rightPanel.page6.tableWidget_4.insertRow(rowPosition)
            self.mainWindow.rightPanel.page6.tableWidget_4.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page6.tableWidget_4.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(project[8])))
            self.mainWindow.rightPanel.page6.tableWidget_4.setItem(rowPosition, 3,
                                                                   (QTableWidgetItem(project[2])))

        self.current_team_projects = self.loginManager.currentUser.current_team_projects()

        for project in self.current_team_projects:
            rowPosition = self.mainWindow.rightPanel.page6.tableWidget_4.rowCount()
            self.mainWindow.rightPanel.page6.tableWidget_4.insertRow(rowPosition)
            self.mainWindow.rightPanel.page6.tableWidget_4.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page6.tableWidget_4.setItem(rowPosition, 2,
                                                                   (QTableWidgetItem(project[8])))
            self.mainWindow.rightPanel.page6.tableWidget_4.setItem(rowPosition, 3,
                                                                   (QTableWidgetItem(project[2])))

        self.submited_indiv_projects = self.loginManager.currentUser.finished_indiv_projects()

        for project in self.submited_indiv_projects:
            rowPosition = self.mainWindow.rightPanel.page6.tableWidget_5.rowCount()
            self.mainWindow.rightPanel.page6.tableWidget_5.insertRow(rowPosition)
            self.mainWindow.rightPanel.page6.tableWidget_5.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page6.tableWidget_5.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(project[8])))
            self.mainWindow.rightPanel.page6.tableWidget_5.setItem(rowPosition, 3,
                                                                   (QTableWidgetItem(project[2])))

        self.submited_team_projects = self.loginManager.currentUser.finished_team_projects()
        for project in self.submited_team_projects:
            rowPosition = self.mainWindow.rightPanel.page6.tableWidget_5.rowCount()
            self.mainWindow.rightPanel.page6.tableWidget_5.insertRow(rowPosition)
            self.mainWindow.rightPanel.page6.tableWidget_5.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page6.tableWidget_5.setItem(rowPosition, 2,
                                                                   (QTableWidgetItem(project[8])))
            self.mainWindow.rightPanel.page6.tableWidget_5.setItem(rowPosition, 3,
                                                                   (QTableWidgetItem(project[2])))

    def refreshDevProject(self):
        self.mainWindow.rightPanel.page7.tableWidget.setRowCount(0)
        self.mainWindow.rightPanel.page7.tableWidget_2.setRowCount(0)
        self.mainWindow.rightPanel.page7.tableWidget_3.setRowCount(0)

        self.devCurrProj = self.loginManager.currentUser.current_indiv_projects()

        for project in self.devCurrProj:
            rowPosition = self.mainWindow.rightPanel.page7.tableWidget.rowCount()
            self.mainWindow.rightPanel.page7.tableWidget.insertRow(rowPosition)
            self.mainWindow.rightPanel.page7.tableWidget.setItem(rowPosition, 0,
                                                                 QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page7.tableWidget.setItem(rowPosition, 3,
                                                                 (QTableWidgetItem(project[2])))
            self.mainWindow.rightPanel.page7.tableWidget.setItem(rowPosition, 1,
                                                                 (QTableWidgetItem(str(project[9]))))
            self.mainWindow.rightPanel.page7.tableWidget.setItem(rowPosition, 2,
                                                                 (QTableWidgetItem(str(project[5]))))

        self.needReview = self.loginManager.currentUser.get_dev_pending_client_reviews()

        for case in self.needReview:
            rowPosition = self.mainWindow.rightPanel.page7.tableWidget_2.rowCount()
            self.mainWindow.rightPanel.page7.tableWidget_2.insertRow(rowPosition)
            self.mainWindow.rightPanel.page7.tableWidget_2.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(case[0]))
            self.mainWindow.rightPanel.page7.tableWidget_2.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(case[1])))

        self.bidProj = self.db.get_pending_projects()

        for project in self.bidProj:
            lowest = str(self.db.get_lowest_bid(project[0]))
            if lowest == "-1":
                lowest = "No bid yet"
            rowPosition = self.mainWindow.rightPanel.page7.tableWidget_3.rowCount()
            self.mainWindow.rightPanel.page7.tableWidget_3.insertRow(rowPosition)
            self.mainWindow.rightPanel.page7.tableWidget_3.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page7.tableWidget_3.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(project[1])))
            self.mainWindow.rightPanel.page7.tableWidget_3.setItem(rowPosition, 2,
                                                                   (QTableWidgetItem(str(project[4]))))
            self.mainWindow.rightPanel.page7.tableWidget_3.setItem(rowPosition, 3,
                                                                   (QTableWidgetItem(lowest)))

    def setbidtables(self):
        self.indiv_bid = self.db.get_individual_project_bids(
            self.pendingprojects[self.mainWindow.rightPanel.page6.tableWidget.currentItem().row()][0])

        self.team_bid = self.db.get_team_project_bids(
            self.pendingprojects[self.mainWindow.rightPanel.page6.tableWidget.currentItem().row()][0])

        # clear content
        self.mainWindow.rightPanel.page6.tableWidget_2.setRowCount(0)
        self.mainWindow.rightPanel.page6.tableWidget_3.setRowCount(0)

        for bid in self.indiv_bid:
            rowPosition = self.mainWindow.rightPanel.page6.tableWidget_2.rowCount()
            self.mainWindow.rightPanel.page6.tableWidget_2.insertRow(rowPosition)
            self.mainWindow.rightPanel.page6.tableWidget_2.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(bid[0]))
            self.mainWindow.rightPanel.page6.tableWidget_2.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(str(bid[1]))))

        for bid in self.team_bid:
            rowPosition = self.mainWindow.rightPanel.page6.tableWidget_3.rowCount()
            self.mainWindow.rightPanel.page6.tableWidget_3.insertRow(rowPosition)
            self.mainWindow.rightPanel.page6.tableWidget_3.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(bid[0]))
            self.mainWindow.rightPanel.page6.tableWidget_3.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(str(bid[1]))))

    def postNewProject(self):
        if self.db.project_id_exists(self.mainWindow.rightPanel.page6.lineEdit.text()):
            QMessageBox.about(self.mainWindow, "Sorry", "This ID already taken by others, try to use somthing else")
        else:
            self.db.create_new_project(self.mainWindow.rightPanel.page6.lineEdit.text(),
                                       self.loginManager.currentUser.user_id,
                                       self.mainWindow.rightPanel.page6.textEdit.toPlainText(),
                                       self.mainWindow.rightPanel.page6.dateEdit.date().toPyDate(),
                                       0,
                                       self.mainWindow.rightPanel.page6.dateEdit_2.date().toPyDate())
            self.refreshClientProject()
            QMessageBox.about(self.mainWindow, "New Project", "Done")

    def choosedev(self):
        try:
            dev = self.indiv_bid[self.mainWindow.rightPanel.page6.tableWidget_2.currentItem().row()][0]
            bid = self.indiv_bid[self.mainWindow.rightPanel.page6.tableWidget_2.currentItem().row()][1]
            project = self.pendingprojects[self.mainWindow.rightPanel.page6.tableWidget.currentItem().row()][0]
            self.db.choose_dev(project, dev, float(bid))
            try:
                lowest = self.db.get_lowest_bid(project)
                if lowest < bid:
                    self.notlow.show()
            except IndexError:
                pass
            self.refreshClientProject()
        except AttributeError:
            QMessageBox.about(self.mainWindow, "Error", "Please select a develop and project")

    def chooseTeam(self):
        try:
            team = self.team_bid[self.mainWindow.rightPanel.page6.tableWidget_3.currentItem().row()][0]
            bid = self.team_bid[self.mainWindow.rightPanel.page6.tableWidget_3.currentItem().row()][1]
            project = self.pendingprojects[self.mainWindow.rightPanel.page6.tableWidget.currentItem().row()][0]
            try:
                lowest = self.db.get_lowest_bid(project)
                if lowest < bid:
                    self.notlow.show()
            except IndexError:
                pass
            self.db.choose_team(project, team, float(bid))
            self.refreshClientProject()
        except AttributeError:
            QMessageBox.about(self.mainWindow, "Error", "Please select a team and project")

    def clientReview(self):
        download = QFileDialog.getSaveFileName(self.mainWindow, "Download Project", "", "exe (*.exe)")
        try:
            dev = self.submited_indiv_projects[
                self.mainWindow.rightPanel.page6.tableWidget_5.currentItem().row()][1]
            proj = self.submited_indiv_projects[
                    self.mainWindow.rightPanel.page6.tableWidget_5.currentItem().row()][0]
            if dev != None:
                copyfile("../resources/projects/" + proj + ".exe", download[0])
                self.rating.show()
            else:
                copyfile("../resources/projects/" + proj + ".exe", download[0])
                self.rating.show()
        except TypeError or FileNotFoundError:
            QMessageBox.about(self.mainWindow, "Error", "Project not yet uploaded")
        except IndexError:
            QMessageBox.about(self.mainWindow, "Error", "This is a test data! System crash!")
        except AttributeError:
            pass

    def createReview(self):
        rating = self.rating.comboBox.currentText()
        dev = self.submited_indiv_projects[
            self.mainWindow.rightPanel.page6.tableWidget_5.currentItem().row()][8]
        message = self.rating.textEdit.toPlainText()
        if dev == None:
            dev = self.submited_team_projects[
                self.mainWindow.rightPanel.page6.tableWidget_5.currentItem().row()][8]
            project = self.submited_team_projects[
                self.mainWindow.rightPanel.page6.tableWidget_5.currentItem().row()][0]
            self.loginManager.currentUser.create_team_project_review(project, dev, rating, message)
        else:
            project = self.submited_indiv_projects[
                self.mainWindow.rightPanel.page6.tableWidget_5.currentItem().row()][0]
            self.loginManager.currentUser.create_project_review(project, dev, rating, message)

        self.refreshClientProject()

    def devReview(self):
        self.rating.show()

    def lowrating(self):
        if int(self.rating.comboBox.currentText()) < 3 and len(self.rating.textEdit.toPlainText()) == 0:
            QMessageBox.about(self.mainWindow, "Error", "You must leave a review")
        else:
            self.rating.close()

    def palceBid(self):
        try:
            project = self.bidProj[self.mainWindow.rightPanel.page7.tableWidget_3.currentItem().row()][0]
            bid = self.mainWindow.rightPanel.page7.lineEdit.text()
            id = self.loginManager.currentUser.user_id
            try:
                self.db.place_individual_bid(project, id, float(bid))
                self.refreshDevProject()
            except AttributeError:
                QMessageBox.about(self.mainWindow, "Error", "You already bid on this project")
            except TypeError:
                QMessageBox.about(self.mainWindow, "Error", "Invalid bid price")
        except AttributeError:
            QMessageBox.about(self.mainWindow, "Error", "Place select a project")

    def palceteamBid(self):
        text, okPressed = QInputDialog.getText(self.mainWindow, "Team", "Team ID:", QLineEdit.Normal, "")

        if okPressed and text != '':
            project = self.bidProj[self.mainWindow.rightPanel.page7.tableWidget_3.currentItem().row()][0]
            bid = self.mainWindow.rightPanel.page7.lineEdit.text()
            id = str(text)
            try:
                self.db.place_team_bid(project, id, float(bid))
                self.refreshDevProject()
            except AttributeError:
                QMessageBox.about(self.mainWindow, "Error", "You already bid on this project")
            except TypeError:
                QMessageBox.about(self.mainWindow, "Error", "Invalid bid price")

    def submitProj(self):
        path = QFileDialog.getOpenFileName(self.mainWindow, "Submit Project", "", "exe (*.exe)")
        project = self.devCurrProj[self.mainWindow.rightPanel.page7.tableWidget.currentItem().row()][0]
        try:
            copyfile(path[0], "../resources/projects/" + project + ".exe")
            self.loginManager.currentUser.new_message(self.db.get_project_info(project)[1],
                                                      "Your project" + project + "is up")
            self.db.finish_individual_project(project)
            self.refreshDevProject()
        except AttributeError:
            QMessageBox.about(self.mainWindow, "Error", "Please select a project")
        except shutil.SameFileError:
            QMessageBox.about(self.mainWindow, "Error", "This Project already submited")
        except FileNotFoundError:
            QMessageBox.about(self.mainWindow, "Error", "Project not found")

    def submitteamProj(self):
        path = QFileDialog.getOpenFileName(self.mainWindow, "Submit Project", "", "exe (*.exe)")
        i = self.mainWindow.rightPanel.page9.tableWidget_2.currentItem().row()
        project = self.mainWindow.rightPanel.page9.tableWidget_2.itemAt(i, 0).text()
        try:
            copyfile(path[0], "../resources/projects/" + project + ".exe")
            self.loginManager.currentUser.new_message(self.db.get_project_info(project)[1],
                                                      "Your project" + project + "is up")
            self.db.finish_team_project(project)
            self.teamManager.read(self.loginManager.currentUser)
            self.refreshTeam()
        except AttributeError:
            QMessageBox.about(self.mainWindow, "Error", "Please select a project")
        except shutil.SameFileError:
            QMessageBox.about(self.mainWindow, "Error", "This Project already submited")
        except FileNotFoundError:
            QMessageBox.about(self.mainWindow, "Error", "Project not found")

    def refreshHistory(self):
        transactions = self.loginManager.currentUser.get_transaction_history()
        reviews = self.loginManager.currentUser.get_review()
        projects = self.loginManager.currentUser.finished_indiv_projects()

        # clear all content
        self.mainWindow.rightPanel.page5.tableWidget.setRowCount(0)
        self.mainWindow.rightPanel.page5.tableWidget_2.setRowCount(0)
        self.mainWindow.rightPanel.page5.tableWidget_3.setRowCount(0)

        # add all client team projects
        if type(self.loginManager.currentUser) is Client:
            team_projects = self.loginManager.currentUser.finished_team_projects()
        else:
            team_projects = ()

        for transaction in transactions:
            rowPosition = self.mainWindow.rightPanel.page5.tableWidget.rowCount()
            self.mainWindow.rightPanel.page5.tableWidget.insertRow(rowPosition)
            self.mainWindow.rightPanel.page5.tableWidget.setItem(rowPosition, 0,
                                                                 QTableWidgetItem(str(transaction[1])))
            self.mainWindow.rightPanel.page5.tableWidget.setItem(rowPosition, 1,
                                                                 (QTableWidgetItem(transaction[4])))
            self.mainWindow.rightPanel.page5.tableWidget.setItem(rowPosition, 2,
                                                                 QTableWidgetItem(transaction[3]))
            self.mainWindow.rightPanel.page5.tableWidget.setItem(rowPosition, 3,
                                                                 QTableWidgetItem(str(transaction[2])))

        for review in reviews:
            rowPosition = self.mainWindow.rightPanel.page5.tableWidget_2.rowCount()
            self.mainWindow.rightPanel.page5.tableWidget_2.insertRow(rowPosition)
            self.mainWindow.rightPanel.page5.tableWidget_2.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(review[0]))
            self.mainWindow.rightPanel.page5.tableWidget_2.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(review[1])))
            self.mainWindow.rightPanel.page5.tableWidget_2.setItem(rowPosition, 2,
                                                                   QTableWidgetItem(review[2]))
            self.mainWindow.rightPanel.page5.tableWidget_2.setItem(rowPosition, 3,
                                                                   QTableWidgetItem(str(review[4])))
            self.mainWindow.rightPanel.page5.tableWidget_2.setItem(rowPosition, 4,
                                                                   QTableWidgetItem(review[3]))

        for project in projects:
            rowPosition = self.mainWindow.rightPanel.page5.tableWidget_3.rowCount()
            self.mainWindow.rightPanel.page5.tableWidget_3.insertRow(rowPosition)
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(project[1])))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 2,
                                                                   QTableWidgetItem(project[8]))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 4,
                                                                   QTableWidgetItem(str(project[9])))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 5,
                                                                   QTableWidgetItem(str(project[5])))

        for project in team_projects:
            rowPosition = self.mainWindow.rightPanel.page5.tableWidget_3.rowCount()
            self.mainWindow.rightPanel.page5.tableWidget_3.insertRow(rowPosition)
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 0,
                                                                   QTableWidgetItem(project[0]))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 1,
                                                                   (QTableWidgetItem(project[1])))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 2,
                                                                   QTableWidgetItem(project[9]))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 4,
                                                                   QTableWidgetItem(str(project[11])))
            self.mainWindow.rightPanel.page5.tableWidget_3.setItem(rowPosition, 5,
                                                                   QTableWidgetItem(str(project[5])))

    def refreshManage(self):
        # clear all content
        self.mainWindow.rightPanel.page8.tableWidget.setRowCount(0)

        self.appManager.read()

        for app in self.appManager.apps:
            rowPosition = self.mainWindow.rightPanel.page8.tableWidget.rowCount()
            self.mainWindow.rightPanel.page8.tableWidget.insertRow(rowPosition)
            self.mainWindow.rightPanel.page8.tableWidget.setItem(rowPosition, 0,
                                                                 QTableWidgetItem(app.user_id))
            self.mainWindow.rightPanel.page8.tableWidget.setItem(rowPosition, 1,
                                                                 QTableWidgetItem(app.type()))
            self.mainWindow.rightPanel.page8.tableWidget.setItem(rowPosition, 2,
                                                                 QTableWidgetItem(app.get_email()))
            self.mainWindow.rightPanel.page8.tableWidget.setItem(rowPosition, 2,
                                                                 QTableWidgetItem(app.get_address()))

    def acceptApp(self):
        self.appManager.accept(self.mainWindow.rightPanel.page8.tableWidget.currentItem().row())
        self.refreshManage()

    def rejectApp(self):
        text, okPressed = QInputDialog.getText(self.mainWindow, "Reason", "Reason:", QLineEdit.Normal, "")

        if okPressed and text != '':
            self.appManager.reject(self.mainWindow.rightPanel.page8.tableWidget.currentItem().row(), str(text))
            self.refreshManage()

    def addToBlacklist(self):
        self.db.add_blacklist(self.mainWindow.rightPanel.page8.lineEdit.text(),
                              self.mainWindow.rightPanel.page8.lineEdit_4.text())

    def removeBlacklist(self):
        self.db.remove_blacklist(self.mainWindow.rightPanel.page8.lineEdit_5.text())

    def resetwarning(self):
        self.db.remove_warning(self.mainWindow.rightPanel.page8.lineEdit_6.text())

    def changeReview(self):
        projct = self.mainWindow.rightPanel.page8.lineEdit_7.text()
        rating = self.mainWindow.rightPanel.page8.lineEdit_3.text()
        cost = self.mainWindow.rightPanel.page8.lineEdit_8.text()

        self.db.settle_project_dispute(projct, rating, cost)

    def refreshTeam(self):
        # clear all content
        self.mainWindow.rightPanel.page9.tableWidget.setRowCount(0)

        self.teamManager.read(self.loginManager.currentUser)

        for team in self.teamManager.teams:
            member = team.get_team_members()
            rowPosition = self.mainWindow.rightPanel.page9.tableWidget.rowCount()
            self.mainWindow.rightPanel.page9.tableWidget.insertRow(rowPosition)
            self.mainWindow.rightPanel.page9.tableWidget.setItem(rowPosition, 0,
                                                                 QTableWidgetItem(str(team.team_id)))
            self.mainWindow.rightPanel.page9.tableWidget.setItem(rowPosition, 1,
                                                                 QTableWidgetItem(str(member[0])))
            self.mainWindow.rightPanel.page9.tableWidget.setItem(rowPosition, 2,
                                                                 QTableWidgetItem(str(member[1])))
            self.mainWindow.rightPanel.page9.tableWidget.setItem(rowPosition, 3,
                                                                 QTableWidgetItem(str(member[2])))
            self.mainWindow.rightPanel.page9.tableWidget.setItem(rowPosition, 4,
                                                                 QTableWidgetItem(str(member[3])))
            self.mainWindow.rightPanel.page9.tableWidget.setItem(rowPosition, 5,
                                                                 QTableWidgetItem(str(member[4])))

    def refreshteamcurrentprojct(self):
        try:
            self.mainWindow.rightPanel.page9.tableWidget_2.setRowCount(0)
            self.mainWindow.rightPanel.page9.tableWidget_3.setRowCount(0)

            i = self.mainWindow.rightPanel.page9.tableWidget.currentItem().row()

            for project in self.teamManager.current_project(i):
                rowPosition = self.mainWindow.rightPanel.page9.tableWidget_2.rowCount()
                self.mainWindow.rightPanel.page9.tableWidget_2.insertRow(rowPosition)
                self.mainWindow.rightPanel.page9.tableWidget_2.setItem(rowPosition, 0,
                                                                       QTableWidgetItem(project[0]))
                self.mainWindow.rightPanel.page9.tableWidget_2.setItem(rowPosition, 1,
                                                                       (QTableWidgetItem(project[1])))
                self.mainWindow.rightPanel.page9.tableWidget_2.setItem(rowPosition, 2,
                                                                       QTableWidgetItem(str(project[9])))
                self.mainWindow.rightPanel.page9.tableWidget_2.setItem(rowPosition, 3,
                                                                       QTableWidgetItem(str(project[5])))
                self.mainWindow.rightPanel.page9.tableWidget_2.setItem(rowPosition, 4,
                                                                       QTableWidgetItem(project[2]))

            for project in self.teamManager.finished_project(i):
                rowPosition = self.mainWindow.rightPanel.page9.tableWidget_3.rowCount()
                self.mainWindow.rightPanel.page9.tableWidget_3.insertRow(rowPosition)
                self.mainWindow.rightPanel.page9.tableWidget_3.setItem(rowPosition, 0,
                                                                       QTableWidgetItem(project[0]))
                self.mainWindow.rightPanel.page9.tableWidget_3.setItem(rowPosition, 1,
                                                                       (QTableWidgetItem(project[1])))
                self.mainWindow.rightPanel.page9.tableWidget_3.setItem(rowPosition, 2,
                                                                       QTableWidgetItem(str(project[11])))
                self.mainWindow.rightPanel.page9.tableWidget_3.setItem(rowPosition, 3,
                                                                       QTableWidgetItem(str(project[5])))
                self.mainWindow.rightPanel.page9.tableWidget_3.setItem(rowPosition, 4,
                                                                       QTableWidgetItem(project[2]))
        except IndexError:
            pass

    def jointeam(self):
        text, okPressed = QInputDialog.getText(self.mainWindow, "Password", "Password:", QLineEdit.Normal, "")

        if okPressed and text != '':
            teamID = self.mainWindow.rightPanel.page9.lineEdit.text()
            self.loginManager.currentUser.join_team(teamID)
            self.refreshTeam()
            QMessageBox.about(self.mainWindow, "Success", "Doen")

    def createteam(self):
        teamID = self.mainWindow.rightPanel.page9.lineEdit_2.text()
        if self.db.team_exists(teamID):
            QMessageBox.about(self.mainWindow, "Eroor", "This ID already taken by others, try to use somthing else")
        else:
            self.loginManager.currentUser.create_team(teamID)
            self.refreshTeam()

    def personalInfo(self):
        self.info.show()

    def deleteAcount(self):
        if len(self.loginManager.currentUser.current_indiv_projects()) == 0:
            try:
                self.loginManager.currentUser.new_message("SuperUser", self.info.textEdit.toPlainText())
                self.db.delete_account(self.loginManager.currentUser.user_id)
                self.info.close()
                self.logout()
            except ArithmeticError:
                pass
        else:
            QMessageBox.about(self.mainWindow, "Error",
                              "Unable to delete account, you still have unfinished projects")

    def systemInfo(self):
        info = SystemInfo(self.mainWindow)
        # set dev and client num
        info.lcdNumber.display(self.db.get_dev_num())
        info.lcdNumber_2.display(self.db.get_client_num())
        # get top user id
        info.setTop(self.db.get_active_clients(1)[0][0], self.db.get_active_devs(1)[0][0])

        info.setWindowFlags(QtCore.Qt.Window)
        info.show()


def main():
    cts = QApplication(sys.argv)
    core = Core()
    core.mainWindow.show()
    sys.exit(cts.exec_())


main()
