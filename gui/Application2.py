from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Application2(QWidget):
    def __init__(self, parent=None):
        super(Application2, self).__init__(parent)

        self.picpath = ('', '')
        self.resumepath = ('', '')
        self.adpath = ('', '')

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 538)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Welcome To CTS!"))
        self.groupBox.setTitle(_translate("Form", "Before continuing, please tell us more about you:"))
        self.pushButton_2.setText(_translate("Form", "Upload Picture"))
        self.pushButton.setText(_translate("Form", "Upload Resume"))
        self.pushButton_3.setText(_translate("Form", "Sample work / Business credential"))
        self.groupBox_2.setTitle(_translate("Form", "Tell us about you interst:"))
        self.checkBox.setText(_translate("Form", "IOS"))
        self.checkBox_2.setText(_translate("Form", "Android"))
        self.checkBox_3.setText(_translate("Form", "DesktopApp"))
        self.checkBox_4.setText(_translate("Form", "Java"))
        self.checkBox_5.setText(_translate("Form", "Python"))
        self.checkBox_6.setText(_translate("Form", "Cpp"))
        self.pushButton_4.setText(_translate("Form", "Confirm"))

        # connect buttion
        self.pushButton_2.clicked.connect(self.uploadpic)
        self.pushButton.clicked.connect(self.uploadresume)
        self.pushButton_3.clicked.connect(self.uploadmore)

    def uploadpic(self):
        self.picpath = QFileDialog.getOpenFileName(self, "Upload Picture", "", "Images (*.png)")

    def uploadresume(self):
        self.resumepath = QFileDialog.getOpenFileName(self, "Upload Resume", "", "PDF (*.pdf)")

    def uploadmore(self):
        self.adpath = QFileDialog.getOpenFileName(self, "Upload Simple Work or Business Credential", "",
                                                      "PDF (*.pdf)")
