""" a login and sign up tab widget"""

from PyQt5.QtWidgets import QTabWidget, QFormLayout, QLineEdit, QPushButton, QWidget


class LoginSignup(QTabWidget):
    def __init__(self, width, hight, parent=None):
        super(LoginSignup, self).__init__(parent)

        # set width and hight
        self.width = width
        self.hight = hight

        # TODO: forgot password?
        # declare page
        self.signUpPage = QWidget()
        self.loginPage = QWidget()

        # declare LineEdit
        self.signUpID = QLineEdit()
        self.signUpPW = QLineEdit()
        self.signUpPW.setEchoMode(QLineEdit.Password)
        self.loginID = QLineEdit()
        self.loginPW = QLineEdit()
        self.loginPW.setEchoMode(QLineEdit.Password)

        # declare check button
        self.signUPB = QPushButton("Sign Up", self.signUpPage)
        self.loginB = QPushButton("Login", self.loginPage)

        self.initUI()

    def initUI(self):
        # set LoginSignup size
        self.setFixedSize(self.width, self.hight)

        # set signUP dialog
        signUp = QFormLayout()
        signUp.addRow("User ID", self.signUpID)
        signUp.addRow("Password", self.signUpPW)

        # set login dialog
        login = QFormLayout()
        login.addRow("User ID", self.loginID)
        login.addRow("Password", self.loginPW)

        # add layout
        self.signUpPage.setLayout(signUp)
        self.loginPage.setLayout(login)

        # move signup and login button
        self.signUPB.move(self.width / 2 - 45, self.hight - 70)
        self.loginB.move(self.width / 2 - 45, self.hight - 70)

        # add tabs
        self.addTab(self.signUpPage, "Sign Up")
        self.addTab(self.loginPage, "Login")
