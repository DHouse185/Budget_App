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
from root.pages.components.ui.Dashboard_header_widget import Ui_Dashboard_header_widget
# from pages.dashboard import Dashboard
########################################################################################

class Header(Ui_Dashboard_header_widget):
    def __init__(self, parent): # , database):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> header_widget
        super().__init__()
        self.Dashboard_header_widget = QWidget(parent=parent)
        self.setupUi(self.Dashboard_header_widget)
        self.Dashboard_header_widget.setGeometry(QRect(0, 0, 1920, 130))