##########  Python IMPORTs  ############################################################
from collections import namedtuple
import typing 
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.components.ui.top_5_expense import Ui_top_5_expense
from root.database import Database
# from pages.dashboard import Dashboard
########################################################################################

class Top_5(Ui_top_5_expense):
    def __init__(self, parent, database: Database, year, month_ls: typing.List[QPushButton], account: str):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> top_5_expense
        super().__init__()
        self.Dashboard_top_5 = QWidget(parent=parent)
        self.setupUi(self.Dashboard_top_5)
        self.Dashboard_top_5.setGeometry(QRect(680, 1020, 541, 281))
        self.database = database
        self.top_5_update(year, month_ls, account)
        
    def top_5_update(self, year, month_ls: typing.List[QPushButton], account):
        self.year = year
        self.account = account
        self.month_abbrv = [abbr.text() for abbr in month_ls]
        self.month_list = [rvar.MONTHS_SHORT_DICT[month] for month in self.month_abbrv]
        self.month_list = sorted(self.month_list, key=lambda x: rvar.month_dict[x])
        self.month_num_list = [rvar.month_dict[month_name] for month_name in self.month_list]
        self.top_5_calc()
        
    def top_5_calc(self):    
        subcategory_totals = dict()
        sub_category_ls = [sub_c.sub_category for sub_c in self.database.app_data['sub_category']['start_data']]
        # Calculate the total amount for each subcategory
        for sub_category in sub_category_ls:
            subcategory_totals[sub_category] = sum([trans.amount for trans in self.database.app_data['transaction_data']['start_data'] if trans.sub_category == sub_category
                and trans.accounting_type != "Credit"
                and trans.year == self.year
                and trans.month in self.month_num_list
                and (self.account == 'All' or trans.account == self.account)])
            
        # Named tuple to store subcategory information
        SubcategoryInfo = namedtuple('SubcategoryInfo', ['name', 'total_amount'])
        
        # Create a list of named tuples for each subcategory
        subcategory_info_list = [SubcategoryInfo(name=sub, total_amount=subcategory_totals[sub]) for sub in subcategory_totals]
        self.database.app_data['sub_category_yearly_total'] = dict()
        self.database.app_data['sub_category_yearly_total']['start_data'] = subcategory_info_list

        # Get the top five subcategories based on total amount
        top_five_subcategories = sorted(subcategory_info_list, key=lambda x: x.total_amount, reverse=True)[:5] 
        
        # Capture the total amount for the top five subcategories
        ############### Salary will get caught in this. Remove potentially?############
        total_amount_top_five = sum(sub.total_amount for sub in top_five_subcategories) 
        ###############################################################################
        
        # TOP 1
        top_1_percent = round(float(top_five_subcategories[0].total_amount / total_amount_top_five), 2) * 100 if total_amount_top_five != 0 else 0
        top_1_percent = int(top_1_percent)
        self.top_1_progressBar.setProperty("value", top_1_percent)
        self.top_1_spent_label.setText(f"${top_five_subcategories[0].total_amount}")
        self.top_1_desc_label.setText(f"{top_five_subcategories[0].name}")
        
        # TOP 2
        top_2_percent = round(float(top_five_subcategories[1].total_amount / total_amount_top_five), 2) * 100 if total_amount_top_five != 0 else 0
        top_2_percent = int(top_2_percent)
        self.top_2_progressBar.setProperty("value", top_2_percent)
        self.top_2_spent_label.setText(f"${top_five_subcategories[1].total_amount}")
        self.top_2_desc_label.setText(f"{top_five_subcategories[1].name}")
        
        # TOP 3
        top_3_percent = round(float(top_five_subcategories[2].total_amount / total_amount_top_five), 2) * 100 if total_amount_top_five != 0 else 0
        top_3_percent = int(top_3_percent)
        self.top_3_progressBar.setProperty("value", top_3_percent)
        self.top_3_spent_label.setText(f"${top_five_subcategories[2].total_amount}")
        self.top_3_desc_label.setText(f"{top_five_subcategories[2].name}")
        
        # TOP 4
        top_4_percent = round(float(top_five_subcategories[3].total_amount / total_amount_top_five), 2) * 100 if total_amount_top_five != 0 else 0
        top_4_percent = int(top_4_percent)
        self.top_4_progressBar.setProperty("value", top_4_percent)
        self.top_4_spent_label.setText(f"${top_five_subcategories[3].total_amount}")
        self.top_4_desc_label.setText(f"{top_five_subcategories[3].name}")
        
        # TOP 5
        top_5_percent = round(float(top_five_subcategories[4].total_amount / total_amount_top_five), 2) * 100 if total_amount_top_five != 0 else 0
        top_5_percent = int(top_5_percent)
        self.top_5_progressBar.setProperty("value", top_5_percent)
        self.top_5_spent_label.setText(f"${top_five_subcategories[4].total_amount}")
        self.top_5_desc_label.setText(f"{top_five_subcategories[4].name}")