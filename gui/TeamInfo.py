from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class TeamInfo(QWidget):
    def __init__(self, parent=None):
        super(TeamInfo, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(716, 780)
        self.verticalLayout = QtWidgets.QVBoxLayout(QWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(QWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(QWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.tableWidget_2)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget_2.setSortingEnabled(True)

        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "QWidget"))
        self.groupBox.setTitle(_translate("QWidget", "Team Reviews"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Devloper"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Reviewer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Review"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "Rating"))
        self.groupBox_2.setTitle(_translate("QWidget", "Team History"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("QWidget", "Team Formed"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("QWidget", "Menber1"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("QWidget", "Menber2"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("QWidget", "Menber3"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "Menber4"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("QWidget", "Menber5"))