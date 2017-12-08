from PyQt5.QtWidgets import QTabWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class NotLow(QTabWidget):
    def __init__(self, parent=None):
        super(NotLow, self).__init__(parent)

        self.setupUi(self)

    def setupUi(self, QTabWidget):
        QTabWidget.setObjectName("QTabWidget")
        QTabWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(QTabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(QTabWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.widget = QtWidgets.QWidget(QTabWidget)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.verticalLayout.addWidget(self.widget)
        self.pushButton = QtWidgets.QPushButton(QTabWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(QTabWidget)
        QtCore.QMetaObject.connectSlotsByName(QTabWidget)

    def retranslateUi(self, QTabWidget):
        _translate = QtCore.QCoreApplication.translate
        QTabWidget.setWindowTitle(_translate("QTabWidget", "QTabWidget"))
        self.label_2.setText(_translate("QTabWidget", "Please expain why you want to chose this developer / team?"))
        self.label.setText(_translate("QTabWidget", "Reason"))
        self.pushButton.setText(_translate("QTabWidget", "Submit"))