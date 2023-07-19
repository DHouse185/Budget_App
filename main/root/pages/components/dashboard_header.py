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
import helper.root_functions as rfunc
import helper.root_vriables as rvar
# from pages.dashboard import Dashboard
########################################################################################

class Header:
    def __init__(self, dashboard, database_conn):
        super().__init__()
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> header_widget
        self.header_widget = QWidget(dashboard)
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
        
        # Eating-out label
        self.eat_out_image = QLabel(self.header_widget)
        self.eat_out_image.setObjectName("Eat_Out_Image")
        self.eat_out_image.setGeometry(QRect(340, 12, 75, 100)) 
        # Eating-out Image
        self.eat_out_spent = QLabel(self.header_widget)
        self.eat_out_spent.setObjectName("Eat_Out_Spent")
        self.eat_out_spent.setGeometry(QRect(415, 12, 100, 100)) 
        # Eating-out spent
        self.eat_out_label = QLabel(self.header_widget)
        self.eat_out_label.setObjectName("Eat_Out_Label")
        self.eat_out_label.setGeometry(QRect(340, 114, 175, 100)) 
        
        # Grocery label
        self.grocery_image = QLabel(self.header_widget)
        self.grocery_image.setObjectName("Grocery_Image")
        self.grocery_image.setGeometry(QRect(545, 12, 75, 100))
        # Grocery Image
        self.grocery_spent = QLabel(self.header_widget)
        self.grocery_spent.setObjectName("Grocery_Spent")
        self.grocery_spent.setGeometry(QRect(590, 12, 100, 100)) 
        # Grocery spent
        self.grocery_label = QLabel(self.header_widget)
        self.grocery_label.setObjectName("Grocery_Label")
        self.grocery_label.setGeometry(QRect(545, 114, 175, 100)) 
        
        # Transportation label
        self.transportation_image = QLabel(self.header_widget)
        self.transportation_image.setObjectName("Transportation_Image")
        self.transportation_image.setGeometry(QRect(720, 12, 75, 100))
        # Transportation Image
        self.transportation_spent = QLabel(self.header_widget)
        self.transportation_spent.setObjectName("Transportation_Spent")
        self.transportation_spent.setGeometry(QRect(795, 12, 100, 100)) 
        # Transportation spent
        self.transportation_label = QLabel(self.header_widget)
        self.transportation_label.setObjectName("Transportation_Label")
        self.transportation_label.setGeometry(QRect(720, 114, 175, 100)) 
        
        # Free Expense label
        self.free_expense_image = QLabel(self.header_widget)
        self.free_expense_image.setObjectName("Free_Expense_Image")
        self.free_expense_image.setGeometry(QRect(925, 12, 75, 100))
        # Free Expense Image
        self.free_expense_spent = QLabel(self.header_widget)
        self.free_expense_spent.setObjectName("Free_Expense_Spent")
        self.free_expense_spent.setGeometry(QRect(1000, 12, 100, 100)) 
        # Free Expense spent
        self.free_expense_label = QLabel(self.header_widget)
        self.free_expense_label.setObjectName("Free_Expense_Label")
        self.free_expense_label.setGeometry(QRect(925, 114, 175, 100)) 
        
        # Bills label
        self.bills_image = QLabel(self.header_widget)
        self.bills_image.setObjectName("Bills_Image")
        self.bills_image.setGeometry(QRect(1130, 12, 75, 100))
        # Bills Image
        self.bills_spent = QLabel(self.header_widget)
        self.bills_spent.setObjectName("Bills_Spent")
        self.bills_spent.setGeometry(QRect(1205, 12, 100, 100)) 
        # Bills spent
        self.bills_label = QLabel(self.header_widget)
        self.bills_label.setObjectName("Bills_Label")
        self.bills_label.setGeometry(QRect(1130, 114, 175, 100)) 
        
        # Investment label
        self.investment_image = QLabel(self.header_widget)
        self.investment_image.setObjectName("Investment_Image")
        self.investment_image.setGeometry(QRect(1335, 12, 75, 100))
        # Investment Image
        self.investment_spent = QLabel(self.header_widget)
        self.investment_spent.setObjectName("Investment_Spent")
        self.investment_spent.setGeometry(QRect(1410, 12, 100, 100)) 
        # Investment spent
        self.investment_label = QLabel(self.header_widget)
        self.investment_label.setObjectName("Investment_Label")
        self.investment_label.setGeometry(QRect(1335, 114, 175, 100)) 
        
        # Support Label
        self.support_image = QLabel(self.header_widget)
        self.support_image.setObjectName("Support_Image")
        self.support_image.setGeometry(QRect(1540, 12, 75, 100))
        # Support Image
        self.support_spent = QLabel(self.header_widget)
        self.support_spent.setObjectName("Support_Spent")
        self.support_spent.setGeometry(QRect(1615, 12, 100, 100)) 
        # Support spent
        self.support_label = QLabel(self.header_widget)
        self.support_label.setObjectName("Support_Label")
        self.support_label.setGeometry(QRect(1540, 114, 175, 100)) 
        
        # Goal label
        self.goal_image = QLabel(self.header_widget)
        self.goal_image.setObjectName("Goal_Image")
        self.goal_image.setGeometry(QRect(1745, 12, 75, 100))
        # Goal Image
        self.goal_spent = QLabel(self.header_widget)
        self.goal_spent.setObjectName("Goal_Spent")
        self.goal_spent.setGeometry(QRect(1820, 12, 100, 100)) 
        # Goal spent
        self.goal_label = QLabel(self.header_widget)
        self.goal_label.setObjectName("Goal_Label")
        self.goal_label.setGeometry(QRect(1745, 114, 175, 100)) 
        