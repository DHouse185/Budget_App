##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow, 
                             QWidget, 
                             QMessageBox, 
                             QStackedWidget, 
                             QWidget,
                             QGridLayout,
                             QLabel)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.components.ui.button_content_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class ButtonContent(Ui_Form):
    def __init__(self, parent): # , database):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> ButtonContent
        super().__init__()
        self.dash_button_content_widget = QWidget(parent=parent)
        self.setupUi(self.dash_button_content_widget)
        self.dash_button_content_widget.setGeometry(QRect(680, 670, 540, 351))