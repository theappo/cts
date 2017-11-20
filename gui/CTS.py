""" MainWinow for cts """

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Coding Turk System')
		self.setGeometry(100, 80, 1024, 648)
		self.setCentralWidget(QWidget())
		self.show()	

def main():
    
    cts = QApplication(sys.argv)
    # set GUI style
    cts.setStyle('Macintosh')
    mainWindow = MainWindow()
    sys.exit(cts.exec_())

main()