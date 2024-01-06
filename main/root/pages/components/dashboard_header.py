##########  Python IMPORTs  ############################################################
import typing
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
from root.pages.components.ui.Dashboard_header_widget import Ui_Dashboard_header_widget
from root.database import Database
import root.helper.root_variables as rvar
########################################################################################

class Header(Ui_Dashboard_header_widget):
    def __init__(self, parent, database: Database, year: int, month_ls: typing.List[QPushButton]):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> header_widget
        super().__init__()
        self.Dashboard_header_widget = QWidget(parent=parent)
        self.setupUi(self.Dashboard_header_widget)
        self.Dashboard_header_widget.setGeometry(QRect(0, 0, 1920, 130))
        
        self.database = database
        self.year = year
        self.month_abbrv = [abbr.text() for abbr in month_ls]
        self.month_list = [rvar.MONTHS_SHORT_DICT[month] for month in self.month_abbrv]
        self.month_list = sorted(self.month_list, key=lambda x: rvar.month_dict[x])
        self.month_num_list = [rvar.month_dict[month_name] for month_name in self.month_list]
        self.calc_category_year()
        
    def update_header(self, year, month_ls):
        self.year = year
        self.month_abbrv = [abbr.text() for abbr in month_ls]
        self.month_list = [rvar.MONTHS_SHORT_DICT[month] for month in self.month_abbrv]
        self.month_list = sorted(self.month_list, key=lambda x: rvar.month_dict[x])
        self.month_num_list = [rvar.month_dict[month_name] for month_name in self.month_list]
        
        self.calc_category_year()
        
    def calc_category_year(self):
        eating_out = sum(eat_out.amount for eat_out in self.database.app_data['transaction_data']['start_data'] if eat_out.year == self.year and eat_out.category == 'Food' and eat_out.month in self.month_num_list)
        grocery = sum(groc.amount for groc in self.database.app_data['transaction_data']['start_data'] if groc.year == self.year and groc.category == 'Grocery' and groc.month in self.month_num_list)
        transportation = sum(trans.amount for trans in self.database.app_data['transaction_data']['start_data'] if trans.year == self.year and trans.category == 'Transportation' and trans.month in self.month_num_list)
        free_expense = sum(free_exp.amount for free_exp in self.database.app_data['transaction_data']['start_data'] if free_exp.year == self.year and free_exp.category == 'Free Expense' and free_exp.month in self.month_num_list)
        investment = sum(inv.amount for inv in self.database.app_data['transaction_data']['start_data'] if inv.year == self.year and inv.category == 'Investment' and inv.month in self.month_num_list)
        bills = sum(bill.amount for bill in self.database.app_data['transaction_data']['start_data'] if bill.year == self.year and bill.category == 'Bills' and bill.month in self.month_num_list)
        support = sum(sup.amount for sup in self.database.app_data['transaction_data']['start_data'] if sup.year == self.year and sup.category == 'Support' and sup.month in self.month_num_list)
        
        self.eating_out_Spent_label.setText(f"${eating_out}")
        self.grocery_Spent_label.setText(f"${grocery}")
        self.transportation_Spent_label.setText(f"${transportation}")
        self.free_expense_Spent_label.setText(f"${free_expense}")
        self.investment_Spent_label.setText(f"${investment}")
        self.bills_Spent_label.setText(f"${bills}")
        self.support_Spent_label.setText(f"${support}")
        # self.bills_Spent_label_2.setText(f"")