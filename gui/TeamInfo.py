from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class TeamInfo(QWidget):
    def __init__(self, parent=None):
        super(TeamInfo, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(716, 389)
        self.verticalLayout = QtWidgets.QVBoxLayout(QWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(QWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
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
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.groupBox)

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
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("QWidget", "Detail"))