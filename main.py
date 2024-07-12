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

        self.switch_to_homePage()
        self.initialize_ui()

        self.ui.Restore_Button.clicked.connect(self.restore_or_maximize_window)
        self.ui.Home_Button.setChecked(True)

        # self.ui.verticalSpacer_7.setHidden(True)
        self.ui.Library_Button_Container.setHidden(True)
        self.ui.Manual_Button_Container.setHidden(True)
        self.ui.More_Menu_Widget.setHidden(True)



        self.ui.Library_Button.clicked.connect(self.show_Library_Button_Container)
        self.ui.Manual_Button.clicked.connect(self.show_Manual_Button_Container)
        self.ui.Information_Button.clicked.connect(self.show_center_menu)
        self.ui.Settings_Button.clicked.connect(self.show_center_menu)

        self.ui.More_Menu_close_Button.clicked.connect(self.More_Menu_Remover)

        self.ui.Home_Button.clicked.connect(self.switch_to_homePage)
        self.ui.Manual_Button.clicked.connect(self.switch_to_ManualPage)
        self.ui.Library_Button.clicked.connect(self.switch_to_LibraryPage)

        self.ui.Information_Button.clicked.connect(self.switch_to_InformationPage)
        self.ui.Settings_Button.clicked.connect(self.switch_to_SettingsPage)

        self.ui.Application_Button.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.Gestures_Button.clicked.connect(self.switch_to_GesturesPage)

        self.ui.AutoMode_Button.clicked.connect(self.switch_to_AutoModePage)
        self.ui.ManualMode_Button.clicked.connect(self.switch_to_ManualModePage)

        self.ui.UTube_Button.clicked.connect(self.switch_to_Page4)
        self.ui.Vlc_Button.clicked.connect(self.switch_to_Page1)
        self.ui.Zoom_Button.clicked.connect(self.switch_to_Page3)
        self.ui.System_Button.clicked.connect(self.switch_to_Page5)
        self.ui.Reading_Button.clicked.connect(self.switch_to_Page6)
        self.ui.Powerpoint_Button.clicked.connect(self.switch_to_Page2)

        self.ui.BackButton1.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton2.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton3.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton4.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton5.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton7.clicked.connect(self.switch_to_ApplicationsPage)

        self.ui.Static_Button2.setCheckable(True)
        self.ui.Static_Button1.setCheckable(True)
        self.ui.Dynamic_Button2.setCheckable(True)
        self.ui.Dynamic_Button1.setCheckable(True)

        self.ui.Static_Button2.clicked.connect(self.switch_to_StaticGestures)
        self.ui.Static_Button1.clicked.connect(self.switch_to_StaticGestures)
        self.ui.Dynamic_Button2.clicked.connect(self.switch_to_DynamicGestures)
        self.ui.Dynamic_Button1.clicked.connect(self.switch_to_DynamicGestures)

        self.ui.Start_Button.clicked.connect(self.switch_to_Start_Application)
        self.ui.Stop_Button.clicked.connect(self.switch_to_Stop_Application)

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    def initialize_ui(self):
        self.resize(710, 540)
        self.setWindowTitle("MotionPilot")

    def switch_to_StaticGestures(self):
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button1.setChecked(True)

    def switch_to_DynamicGestures(self):
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(1)
        self.ui.Dynamic_Button2.setChecked(True)
    def Remove_Button_Check(self):

        self.ui.More_Menu_Widget.setHidden(True)
        self.ui.Information_Button.setChecked(False)
        self.ui.Settings_Button.setChecked(False)

    def More_Menu_Remover(self):
        self.Remove_Button_Check()
        self.initialize_ui()
    def switch_to_Start_Application(self):
        self.ui.Start_Stacked_Widget.setCurrentIndex(1)

    def switch_to_Stop_Application(self):
        self.ui.Start_Stacked_Widget.setCurrentIndex(0)

    def switch_to_homePage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(0)
        self.ui.Start_Stacked_Widget.setCurrentIndex(0)
        self.ui.Manual_Button_Container.setHidden(True)
        self.ui.Library_Button_Container.setHidden(True)
        self.ui.Manual_Button.setChecked(False)

    def switch_to_LibraryPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(2)
        self.ui.Library_Stacked_Widget.setCurrentIndex(1)
        self.ui.Applications_Stacked_Widget.setCurrentIndex(0)
        self.ui.Gestures_Button.setChecked(False)
        self.ui.Application_Button.setChecked(True)
        self.ui.Manual_Button.setChecked(False)

    def switch_to_ManualPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(1)
        self.ui.Manual_Stacked_Widget.setCurrentIndex(1)
        self.ui.ManualMode_Button.setChecked(False)
        self.ui.AutoMode_Button.setChecked(True)

    def switch_to_InformationPage(self):
        self.ui.More_Menu_Stacked_Widget.setCurrentIndex(0)

    def switch_to_SettingsPage(self):
        self.ui.More_Menu_Stacked_Widget.setCurrentIndex(1)

    def switch_to_ApplicationsPage(self):
        self.ui.Library_Stacked_Widget.setCurrentIndex(1)
        self.ui.Applications_Stacked_Widget.setCurrentIndex(0)


    def switch_to_GesturesPage(self):
        self.ui.Library_Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button1.setChecked(True)

    def switch_to_AutoModePage(self):
        self.ui.Manual_Stacked_Widget.setCurrentIndex(1)

    def switch_to_ManualModePage(self):
        self.ui.Manual_Stacked_Widget.setCurrentIndex(0)

    def switch_to_Page1(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(1)

    def switch_to_Page2(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(2)

    def switch_to_Page3(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(3)

    def switch_to_Page4(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(4)

    def switch_to_Page5(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(5)

    def switch_to_Page6(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(6)



    def show_center_menu(self):
        self.ui.More_Menu_Widget.setHidden(False)

    def show_Library_Button_Container(self):
        # self.ui.verticalSpacer_7.setHidden(False)
        self.ui.Library_Button_Container.setHidden(False)
        self.ui.Manual_Button_Container.setHidden(True)

    def show_Manual_Button_Container(self):
        self.ui.Manual_Button_Container.setHidden(False)
        self.ui.Library_Button_Container.setHidden(True)


        # Show window
        self.show()

# Execute App
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
