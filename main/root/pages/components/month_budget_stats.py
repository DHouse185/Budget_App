##########  Python IMPORTs  ############################################################
from decimal import Decimal
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.ui.month_budget_stats_widget import Ui_Form
########################################################################################

class Month_Budget_Stats(Ui_Form):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.stats = QWidget(parent=parent)
        self.setupUi(self.stats)
        self.stats.setGeometry(QRect(1050, 650, 690, 430))
        
        self.database = database        
        self.year = int(self.month_budget_year_comboBox.currentText())
        self.categories = [cat.category for cat in self.database.app_data['category']['start_data']]
        self.categories.remove('Payment')
        self.categories.append('total')
        self.categories.append('left_amount')
        self.categories = ['_'.join(ele.split(' ')) for ele in self.categories]
        self.label_check_list = [''.join(ele.text().split('Total ')) for ele in self.label_list]
        self.label_check_list = [''.join(ele.split(' :')) for ele in self.label_check_list]
        self.new_label_dict = dict()
        self.add_account()
        account_nm = self.select_account_comboBox.currentText()
        if account_nm == 'All':
            account_id = 0
        else:
            account_id = next(acc.id for acc in self.database.app_data['account']['start_data'] if acc.account == account_nm)
            
        for text in self.label_dict.keys():
           for label in self.label_check_list:
               if label in text:
                   self.new_label_dict[label.lower()] = self.label_dict[text]  
                
        self.change_stats(self.year, account_id)
    
    def add_account(self):
        account_ls = list()
        self.select_account_comboBox.clear()
        for account in self.database.app_data['account']['start_data']:
            account_ls.append(account.account)
            
        self.select_account_comboBox.addItem('All')    
        self.select_account_comboBox.addItems(account_ls)
            
    def change_year(self, year: str):
        self.year = year
        account_nm = self.select_account_comboBox.currentText()
        if account_nm == 'All':
            account_id = 0
            check = True
        else:
            account_id = next(acc.id for acc in self.database.app_data['account']['start_data'] if acc.account == account_nm)
            check = self.database.month_budget_check_stats(self.stats, self.year, account_id)
        
        if check:
            self.change_stats(self.year, account_id)
            
        else:
            QMessageBox.information(self.stats, "Update Fail",
                                """Previous year selection is still shown on the table and stats.\nData on the table has not been updated.""",
                                QMessageBox.StandardButton.Ok)    
            
        return check
  
    def change_stats(self, year, account_id):
        if account_id == 0:
           for category in self.categories:
            category_title = category.replace('_', ' ')
            
            if category_title.lower() == 'total':
                category_budget = sum([cat_budg.total for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == int(self.year)])
                self.new_label_dict['spend'].setText(f"${category_budget}")
                
            elif category_title.lower() == 'left amount':
                category_budget = sum([cat_budg.left_amount for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == int(self.year)])
                self.new_label_dict['extra'].setText(f"${category_budget}")
                
            else:
                category_budget = sum([getattr(cat_budg, category.lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == int(self.year)])
                self.new_label_dict[category_title.lower()].setText(f"${category_budget}") 
                
        else:
            for category in self.categories:
                category_title = category.replace('_', ' ')
                
                if category_title.lower() == 'total':
                    category_budget = sum([Decimal(cat_budg.total) for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == int(self.year)])
                    self.new_label_dict['spend'].setText(f"${category_budget}")
                    
                elif category_title.lower() == 'left amount':
                    category_budget = sum([Decimal(cat_budg.left_amount) for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == int(self.year) and cat_budg.account_id == account_id])
                    self.new_label_dict['extra'].setText(f"${category_budget}")
                    
                else:
                    category_budget = sum([Decimal(getattr(cat_budg, category.lower())) for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == int(self.year) and cat_budg.account_id == account_id])
                    self.new_label_dict[category_title.lower()].setText(f"${category_budget}")