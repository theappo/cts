""" a panel that dispaly user information """

from subprocess import Popen

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class UserInfo(QWidget):
    def __init__(self, parent=None):
        super(UserInfo, self).__init__(parent)

        self.user_id = None

        self.setupUi(self)

    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(576, 646)
        self.verticalLayout = QtWidgets.QVBoxLayout(QWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(QWidget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_7 = QtWidgets.QWidget(QWidget)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_7.setObjectName("widget_7")
        self.formLayout = QtWidgets.QFormLayout(self.widget_7)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_7)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget_7)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget = QtWidgets.QWidget(QWidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_6)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget_6)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget_5)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_4.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget_5)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_4.addWidget(self.checkBox_6)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget)
        self.tableWidget = QtWidgets.QTableWidget(QWidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout.addWidget(self.tableWidget)

        self.label.setFixedSize(100, 100)
        self.label.setScaledContents(True)

        self.lineEdit.setMinimumWidth(400)
        self.lineEdit_2.setMinimumWidth(400)

        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "QWidget"))
        self.label.setText(_translate("QWidget", "TextLabel"))
        self.pushButton_2.setText(_translate("QWidget", "View Resume"))
        self.pushButton.setText(_translate("QWidget", "View Addition Info"))
        self.label_2.setText(_translate("QWidget", "Email:"))
        self.label_3.setText(_translate("QWidget", "Adress:"))
        self.checkBox.setText(_translate("QWidget", "IOS"))
        self.checkBox_2.setText(_translate("QWidget", "Java"))
        self.checkBox_3.setText(_translate("QWidget", "Android"))
        self.checkBox_4.setText(_translate("QWidget", "Python"))
        self.checkBox_5.setText(_translate("QWidget", "DesktopApp"))
        self.checkBox_6.setText(_translate("QWidget", "CPP"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Project ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Project Rating"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Reviewer"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "Project Review"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "Project Detail"))

        # connect button
        self.pushButton_2.clicked.connect(self.viewresume)

    def setpic(self, user_id):
        self.user_id = user_id
        """ set pic to the path image"""
        pixmap = QPixmap("../resources/pictures/" + self.user_id)
        # when path not found
        if (pixmap.isNull()):
            pixmap = QPixmap("../img/unknown-user.png")
        # scaled and set
        pixmap.scaled(60, 60, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    def viewresume(self):
        download = QFileDialog.getSaveFileName(self.mainWindow, "Download Project", "", "pdf (*.pdf)")

        try:
            copyfile("../resources/resumes/" + self.user_id + ".pdf", download[0])
        except TypeError:
            QMessageBox.about(self, "Error", "This user not yet has a resume")
