# Import GUI file

import os
import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QMainWindow, QApplication,QPushButton,QButtonGroup, QSizeGrip
from PyQt6.QtGui import QIcon


import resources_rc
from User_Interface import *
# IMPORT Custom widgets


#Code for connecting another window
import Tray_rc
from Tray import Ui_MainWindow as Ui_MinimizeTray
########################################################################


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        # QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Set the window icon
        self.setWindowIcon(QIcon('SystemTray\logo.png'))
        
        self.switch_to_homePage()
        self.initialize_ui()
        
        # Hide the title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Make the window draggable (
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.dragPosition = None

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
        self.ui.Custom_Button.clicked.connect(self.switch_to_CustomPage)

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
       
        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.ui.Information_Button)
        self.button_group.addButton(self.ui.Settings_Button)
        self.button_group.setExclusive(True)

        # Connect minimize to tray  button
        self.ui.Minimize_To_Tray_Button.clicked.connect(self.open_min_window)
        self.min_window = None
        
        QSizeGrip(self.ui.frame_4)

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    def initialize_ui(self):
        self.resize(800, 540)
        self.setWindowTitle("MotionPilot")

    def switch_to_StaticGestures(self):
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button1.setChecked(True)

    def switch_to_DynamicGestures(self):
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(1)
        self.ui.Dynamic_Button2.setChecked(True)
    def Remove_Button_Check(self):

        self.ui.More_Menu_Widget.setHidden(True)
        # Disable auto-exclusive temporarily
        self.button_group.setExclusive(False)

        # Uncheck the buttons
        self.ui.Information_Button.setChecked(False)
        self.ui.Settings_Button.setChecked(False)
        
        # Re-enable auto-exclusive
        self.button_group.setExclusive(True)
        self.ui.Main_Body_Widget.setFocus()

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
        self.ui.Custom_Button.setChecked(False)

    def switch_to_LibraryPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(2)
        self.ui.Library_Stacked_Widget.setCurrentIndex(1)
        self.ui.Applications_Stacked_Widget.setCurrentIndex(0)
        self.ui.Gestures_Button.setChecked(False)
        self.ui.Application_Button.setChecked(True)
        self.ui.Manual_Button.setChecked(False)
        self.ui.Custom_Button.setChecked(False)

    def switch_to_ManualPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(1)
        self.ui.Manual_Stacked_Widget.setCurrentIndex(1)
        self.ui.ManualMode_Button.setChecked(False)
        self.ui.AutoMode_Button.setChecked(True)
        self.ui.Custom_Button.setChecked(False)

    def switch_to_CustomPage(self):

        self.ui.Manual_Button.setChecked(False)
        self.ui.Manual_Button_Container.setHidden(True)
        self.ui.Manual_Button.setChecked(False)
        self.ui.Library_Button_Container.setHidden(True)

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

    #Code to window Draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            if self.dragPosition is not None:
                self.move(event.globalPosition().toPoint() - self.dragPosition)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = None
            event.accept()
  


#Code to connect another window
    def open_min_window(self):
        if self.min_window is None:
            self.min_window = MinimizeWindow()

        self.min_window.show_page_one()
        self.min_window.show()
        self.close()
        # Show window




#code of minimized window(system tray)
class MinimizeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MinimizeTray()
        self.ui.setupUi(self)

        # Hide the title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Make the window draggable (
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.dragPosition = None
        
        # Connect buttons to their respective slots
        self.ui.Close.clicked.connect(self.close)
        # Connect buttons to their respective slots
        self.ui.Maximize.clicked.connect(self.open_main_window)
        self.main_window = None
        
    
    # Set the window icon
        self.setWindowIcon(QIcon('SystemTray\logo.png'))

    
    #Code to connect another window
    def open_main_window(self):
        if self.main_window is None:
            self.main_window = MainWindow()

        self.main_window.show()
        self.close()
        # Show window
        
    #Move to the currentIndex4 widget page 
    def show_page_one(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    #Code to window Draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            if self.dragPosition is not None:
                self.move(event.globalPosition().toPoint() - self.dragPosition)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = None
            event.accept()
  

# Execute App
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
