# Import GUI file

import os
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication,QPushButton


import resources_rc
from User_Interface import *
# IMPORT Custom widgets

########################################################################


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        # QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("MotionPilot")

        self.ui.More_Menu_Widget.setHidden(True)
        self.ui.Information_Button.clicked.connect(self.show_center_menu)

        self.ui.Home_Button.clicked.connect(self.switch_to_homePage)
        self.ui.Manual_Button.clicked.connect(self.switch_to_ManualPage)
        self.ui.Library_Button.clicked.connect(self.switch_to_LibraryPage)

        self.ui.Information_Button.clicked.connect(self.switch_to_InformationPage)
        self.ui.Settings_Button.clicked.connect(self.switch_to_SettingsPage)

    def switch_to_homePage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(0)

    def switch_to_LibraryPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(2)

    def switch_to_ManualPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(1)

    def switch_to_InformationPage(self):
        self.ui.More_Menu_Stacked_Widget.setCurrentIndex(0)

    def switch_to_SettingsPage(self):
        self.ui.More_Menu_Stacked_Widget.setCurrentIndex(1)

    def show_center_menu(self):
        self.ui.More_Menu_Widget.setHidden(False)


        # Show window
        self.show()

# Execute App
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
