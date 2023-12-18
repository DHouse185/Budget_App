##########  Python IMPORTs  ############################################################
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
from root.pages.components.ui.Dashboard_header_widget import Ui_Dashboard_header_widget
from root.database import Database
########################################################################################

class Header(Ui_Dashboard_header_widget):
    def __init__(self, parent, database: Database, year):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> header_widget
        super().__init__()
        self.Dashboard_header_widget = QWidget(parent=parent)
        self.setupUi(self.Dashboard_header_widget)
        self.Dashboard_header_widget.setGeometry(QRect(0, 0, 1920, 130))
        
        self.database = database
        self.year = year
        
        # Calculate Categories Year Total
        
        eating_out = sum(eat_out.amount for eat_out in self.database.app_data['transaction_data']['old'] if eat_out.year == self.year and eat_out.category == 'Food')
        grocery = sum(groc.amount for groc in self.database.app_data['transaction_data']['old'] if groc.year == self.year and groc.category == 'Grocery')
        transportation = sum(trans.amount for trans in self.database.app_data['transaction_data']['old'] if trans.year == self.year and trans.category == 'Transportation')
        free_expense = sum(free_exp.amount for free_exp in self.database.app_data['transaction_data']['old'] if free_exp.year == self.year and free_exp.category == 'Free Expense')
        investment = sum(inv.amount for inv in self.database.app_data['transaction_data']['old'] if inv.year == self.year and inv.category == 'Investment')
        bills = sum(bill.amount for bill in self.database.app_data['transaction_data']['old'] if bill.year == self.year and bill.category == 'Bills')
        support = sum(sup.amount for sup in self.database.app_data['transaction_data']['old'] if sup.year == self.year and sup.category == 'Support')
        
        self.eating_out_Spent_label.setText(f"${eating_out}")
        self.grocery_Spent_label.setText(f"${grocery}")
        self.transportation_Spent_label.setText(f"${transportation}")
        self.free_expense_Spent_label.setText(f"${free_expense}")
        self.investment_Spent_label.setText(f"${investment}")
        self.bills_Spent_label.setText(f"${bills}")
        self.support_Spent_label.setText(f"${support}")
        # self.bills_Spent_label_2.setText(f"")
        
        # YEAR CHANGE UPDATE FUNCTION...
        
        # MONTH CHANGE UPDATE FUNCTION...