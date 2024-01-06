##########  Python IMPORTs  ############################################################
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
        
        for text in self.label_dict.keys():
           for label in self.label_check_list:
               if label in text:
                   self.new_label_dict[label.lower()] = self.label_dict[text]  
                
        for category in self.categories:
            category_title = category.replace('_', ' ')
            
            if category_title.lower() == 'total':
                category_budget = sum([cat_budg.total for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == self.year])
                self.new_label_dict['spend'].setText(f"${category_budget}")
                
            elif category_title.lower() == 'left amount':
                category_budget = sum([cat_budg.left_amount for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == self.year])
                self.new_label_dict['extra'].setText(f"${category_budget}")
                
            else:
                category_budget = sum([getattr(cat_budg, category.lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == self.year])
                self.new_label_dict[category_title.lower()].setText(f"${category_budget}")
        
    def change_year(self, year: str):
        self.year = year
        check = self.database.month_budget_check_stats(self.stats, self.year)
        
        if check:
            self.change_stats(self.year)
            
        else:
            QMessageBox.information(self.stats, "Update Fail",
                                """Previous year selection is still shown on the table and stats.\nData on the table has not been updated.""",
                                QMessageBox.StandardButton.Ok)    
            
        return check
  
    def change_stats(self, year):
        
        for category in self.categories:
            category_title = category.replace('_', ' ')
            
            if category_title.lower() == 'total':
                category_budget = sum([cat_budg.total for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == self.year])
                self.new_label_dict['spend'].setText(f"${category_budget}")
                
            elif category_title.lower() == 'left amount':
                category_budget = sum([cat_budg.left_amount for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == self.year])
                self.new_label_dict['extra'].setText(f"${category_budget}")
                
            else:
                category_budget = sum([getattr(cat_budg, category.lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] if cat_budg.year == self.year])
                self.new_label_dict[category_title.lower()].setText(f"${category_budget}")