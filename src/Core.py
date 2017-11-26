""" CTS core system, program start from here """

import sys
sys.path.insert(0, "../gui")

from MainWindow import *

from PyQt5.QtWidgets import QApplication

def core():
    def __init__(self):
        self.currentUser = None



def main():
    cts = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    # disable resize
    mainWindow.setFixedSize(1024, 648)
    sys.exit(cts.exec_())


main()