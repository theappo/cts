from PyQt5.QtWidgets import QTabWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class TeamPage(QTabWidget):
    def __init__(self, parent=None):
        super(TeamPage, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, QTabWidget):
        QTabWidget.setObjectName("QTabWidget")
        QTabWidget.resize(784, 574)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
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
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignHCenter)
        QTabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.tab1)
        self.widget_2.setObjectName("widget_2")
        self.formLayout = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.pushButton = QtWidgets.QPushButton(self.tab1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.widget = QtWidgets.QWidget(self.tab1)
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.verticalLayout_2.addWidget(self.widget)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignHCenter)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget_3)
        QTabWidget.addTab(self.tab1, "")

        self.retranslateUi(QTabWidget)
        QTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(QTabWidget)

    def retranslateUi(self, QTabWidget):
        _translate = QtCore.QCoreApplication.translate
        QTabWidget.setWindowTitle(_translate("QTabWidget", "QTabWidget"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("QTabWidget", "Team Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("QTabWidget", "Member1"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("QTabWidget", "Member2"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("QTabWidget", "Member3"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("QTabWidget", "Member4"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("QTabWidget", "Member5"))
        self.pushButton_3.setText(_translate("QTabWidget", "Review this member"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("QTabWidget", "Project id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("QTabWidget", "Client"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("QTabWidget", "Price"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("QTabWidget", "Due date"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("QTabWidget", "Detail"))
        self.pushButton_4.setText(_translate("QTabWidget", "Submit Project"))
        QTabWidget.setTabText(QTabWidget.indexOf(self.tab), _translate("QTabWidget", "Team"))
        self.label_3.setText(_translate("QTabWidget", "Join a team"))
        self.pushButton.setText(_translate("QTabWidget", "Join"))
        self.label_4.setText(_translate("QTabWidget", "Create a team"))
        self.pushButton_5.setText(_translate("QTabWidget", "Create"))
        self.tableWidget_3.setSortingEnabled(True)
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("QTabWidget", "Project Name"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("QTabWidget", "Client"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("QTabWidget", "Price"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("QTabWidget", "Date"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("QTabWidget", "Detail"))
        QTabWidget.setTabText(QTabWidget.indexOf(self.tab1), _translate("QTabWidget", "Team"))