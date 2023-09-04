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
import root.helper.root_vriables as rvar
# from pages.dashboard import Dashboard
########################################################################################

class Header:
    def __init__(self, parent, database):
        super().__init__()
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> header_widget
        self.header_widget = QWidget(parent)
        self.header_widget.setObjectName(u"Dashboard_header_widget")
        self.header_widget.setGeometry(QRect(0, 0, 1960, 250))
        
        # Header Title
        self.header_title_label = QLabel("Financial Dashboard", self.header_widget)
        self.header_title_label.setObjectName("Dashboard_Title")
        self.header_title_label.setGeometry(QRect(5, 2, 200, 100))
        
        # YTD label
        self.ytd_label = QLabel("Spend YTD: ", self.header_widget)
        self.ytd_label.setObjectName("YTD_Label")
        self.ytd_label.setGeometry(QRect(235, 52, 75, 100)) 
        
        self.category = ["Eating_Out","Grocery","Transportation","Free_Expense","Investment","Bills","Support", "Goal"]
        self.image = [QLabel(self.header_widget) for _ in range(len(self.category))]
        self.spent = [QLabel(self.header_widget) for _ in range(len(self.category))]
        self.labels = [QLabel(self.header_widget) for _ in range(len(self.category))]
        
        for idx, h in enumerate(self.image):
            i_width = 75
            i_height = 100
            i_atop = 12
            i_start_left = 340
            # name
            h.setObjectName(f"{self.category[idx]}_Image")
            # Postion and Shape 
            h.setGeometry(QRect(i_start_left, i_atop, i_width, i_height))
            i_start_left += 205
        
        for idx, h in enumerate(self.spent):
            s_width = 100
            s_height = 100
            s_atop = 12
            s_start_left = 415
            # name
            h.setObjectName(f"{self.category[idx]}_Spent")
            # Postion and Shape 
            h.setGeometry(QRect(s_start_left, s_atop, s_width, s_height))
            s_start_left += 205
            
        for idx, h in enumerate(self.labels):
            s_width = 175
            s_height = 100
            s_atop = 114
            s_start_left = 340
            # name
            h.setObjectName(f"{self.category[idx]}_Spent")
            h.setText(f"{self.category[idx].replace('_', ' ')}")
            # Postion and Shape 
            h.setGeometry(QRect(s_start_left, s_atop, s_width, s_height))
            s_start_left += 205
        