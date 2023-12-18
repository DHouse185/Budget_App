##########  Python IMPORTs  ############################################################
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QPushButton, QPushButton
from PyQt6.QtCore import QRect
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
        self.year = rvar.CURRENT_YEAR
        self.year_button_list = list()
        self.selected_month_list = self.month_button_list.copy()
        
        for button in self.month_button_list:
            button.setStyleSheet(rvar.BLUE_BUTTON_STYLE)
            
        # MORE BUTTONS FOR YEARS
        row = 3
        column = 0
        for button in rvar.YEARS_LIST:
            column = 0 if column > 3 else column
            pushbutton = QPushButton(parent=self.button_Content_widget)
            pushbutton.setObjectName(f"pushButton_{button}")
            pushbutton.setText(f"{button}")
            if int(button) == rvar.CURRENT_YEAR:
                pushbutton.setStyleSheet(rvar.BLUE_BUTTON_STYLE)
            self.gridLayout.addWidget(pushbutton, row, column, 1, 1)
            self.year_button_list.append(pushbutton)
            column += 1
            row += 1 if column > 3 else 0
            
        self.button_list = self.selected_month_list + self.year_button_list
    
    def select(self, pushbutton: QPushButton):
        text = pushbutton.text()
        self.button_select(text, pushbutton)    
        
    def button_select(self, text: str, pushbutton: QPushButton):
        # ADD TO PARENT WIDGET UPDATE FUNCTIONS LATER #################################
        # CREATE DISTINCTION BETWEEN YEAR AND MONTH
        if text in self.month_list_str:
            self.adjust_month(pushbutton, text)
        elif text in rvar.YEARS_LIST:
            self.adjust_year(pushbutton, text)
    
    def adjust_month(self, pushbutton: QPushButton, text: str):
        if pushbutton in self.selected_month_list:
            pushbutton.setStyleSheet(rvar.NORMAL_BUTTON_STYLE)
            self.selected_month_list.remove(pushbutton)
        else:
            pushbutton.setStyleSheet(rvar.BLUE_BUTTON_STYLE)
            self.selected_month_list.append(pushbutton)
        # UTILIZE TEXT VARIABLE LATER TO ADJUST DATA ON DASHBOARD
        
    def adjust_year(self, pushbutton: QPushButton, text: str): 
        if self.year == int(text):
            return
        else:
            for button in self.year_button_list:
                button.setStyleSheet(rvar.NORMAL_BUTTON_STYLE)
            pushbutton.setStyleSheet(rvar.BLUE_BUTTON_STYLE)
            self.year = int(text)
            return
        