# Import GUI file


import os
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Show window
        self.show()

# Execute App
if __name__ =="__main__":
    app = QApplication(sys.argv)
