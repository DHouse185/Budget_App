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
from root.pages.components.ui.top_5_expense import Ui_top_5_expense
# from pages.dashboard import Dashboard
########################################################################################

class Top_5(Ui_top_5_expense):
    def __init__(self, parent): # , database):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> header_widget
        super().__init__()
        self.Dashboard_top_5 = QWidget(parent=parent)
        self.setupUi(self.Dashboard_top_5)
        self.Dashboard_top_5.setGeometry(QRect(680, 1020, 541, 281))