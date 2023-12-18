##########  Python IMPORTs  ############################################################
from typing import List
import random
from decimal import Decimal
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import QRect, QDateTime, QDate, QTime
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.models import Account
from root.models import Category_Type
from root.models import Sub_Category
from root.models import Category
from root.models import Accounting_Type
from root.models import Frequency
from root.models import Transaction
from root.pages.components.ui.add_transaction_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Add_Transaction(Ui_Form):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.add_trans_widget = QWidget(parent=parent)
        self.setupUi(self.add_trans_widget)
        self.add_trans_widget.setGeometry(QRect(415, 0, 1490, 400))
        
        self.database = database
        self.tables_array = ['category_test', 'sub_category_test', 'account_test', 'category_type_test',
                             'accounting_type_test', 'month_test']
        self.create_table_dict()
        
        # Add Transfer to Accounts
        self.accounts: List[str] = [acc.account for acc in self.database.app_data['account']['old']]
        for _, account in enumerate(self.accounts):  
            self.transfer_To_comboBox.addItem(account)
            self.account_comboBox.addItem(account)
        # Add category type
        self.category_types: List[str] = [cat_type.category_type for cat_type in self.database.app_data['category_type']['old']]
        for _, category_type in enumerate(self.category_types):  
            self.category_Type_comboBox.addItem(category_type)
        # Add sub categories
        self.sub_categories: List[str] = [sub_cat_type.sub_category for sub_cat_type in self.database.app_data['sub_category']['old']]
        for _, sub_category in enumerate(self.sub_categories):  
            self.sub_Category_comboBox.addItem(sub_category)
            
        ######### FOR DEBUGGING #################################    
        # for index in range(self.category_comboBox.count()):
            # item_text = self.category_comboBox.itemText(index)
            # print(item_text)    
            
        # Add Categories
        self.categories: List[str] = [cat.category for cat in self.database.app_data['category']['old']]
        for _, category in enumerate(self.categories):  
            self.category_comboBox.addItem(category)
        # Add Accounting type
        self.accountings: List[str] = [acc_type.type for acc_type in self.database.app_data['accounting_type']['old']]
        for _, accounting in enumerate(self.accountings):  
            self.credit_Debit_comboBox.addItem(accounting)
        # Add Frequency
        self.frequencies: List[str] = [freq.frequency for freq in self.database.app_data['frequency']['old']]
        for _, frequency in enumerate(self.frequencies):  
            self.frequency_comboBox.addItem(frequency)
            
        self.discard_pushButton.clicked.connect(self.discard_check)
           
    def create_table_dict(self):
        self.accounts_dict = dict()
        self.category_type_dict = dict()
        self.sub_categories_dict = dict()
        self.categories_dict = dict()
        self.accountings_dict = dict()
        self.frequency_dict = dict()
        
        accounts: List[Account] = self.database.app_data['account']['old']
        ######## POTENTIALLY ADD TO DATABASE APP_DATA? ######################################## 
        for _, account in enumerate(accounts):  
            self.accounts_dict[account.account] = account.id
        # Add category type
        category_types: List[Category_Type] = self.database.app_data['category_type']['old']
        for _, category_type in enumerate(category_types):  
            self.category_type_dict[category_type.category_type] = category_type.id
        # Add sub categories
        sub_categories: List[Sub_Category] = self.database.app_data['sub_category']['old']
        for _, sub_category in enumerate(sub_categories):  
            self.sub_categories_dict[sub_category.sub_category] = sub_category.id
        # Add Categories
        categories: List[Category] = self.database.app_data['category']['old']
        for _, category in enumerate(categories):  
            self.categories_dict[category.category] = category.id
        # Add Accounting type
        accountings : List[Accounting_Type]= self.database.app_data['accounting_type']['old']
        for _, accounting in enumerate(accountings):  
            self.accountings_dict[accounting.type] = accounting.id
        # Add Frequency
        frequencies : List[Frequency]= self.database.app_data['frequency']['old']
        for _, frequency in enumerate(frequencies):  
            self.frequency_dict[frequency.frequency] = frequency.id
        ######## POTENTIALLY ADD TO DATABASE APP_DATA? ########################################
    
    def add_check(self):
        # Validate Input
        ret = QMessageBox.question(self.add_trans_widget, "Confirmation",
                                 "Do you want to add this transaction?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to exit the application
        if ret == QMessageBox.StandardButton.Yes:
            return self.add_transaction()
            
        # If user chooses not to close application
        elif ret == QMessageBox.StandardButton.Cancel:
            return False
            
        # Close event will be ignored if neither are selected
        else:
            QMessageBox.information(self.add_trans_widget, "Error",
                                 "Something went wrong. Transaction was not added",
                                 QMessageBox.StandardButton.Ok)
            return False
                        
    def add_transaction(self):
        account = self.account_comboBox.currentText()
        account_id = self.accounts_dict[account]
        
        # Grab Date
        date = self.date_dateEdit.dateTime()
        date_datetime = date.toPyDateTime().date()
        date_month = date.toString("MMMM")
        date_formatted = date.toString("yyyy-MM-dd")        
        month_id = rvar.month_dict[date_month]        
        description = self.description_lineEdit.text()
        amount = self.amount_doubleSpinBox.text()        
        accounting = self.credit_Debit_comboBox.currentText()
        accounting_id = self.accountings_dict[accounting]
        transfer_account = self.transfer_To_comboBox.currentText()
        payback = 'None' # Fix Later
        payback_id = 1 # Fix Later
        frequency = self.frequency_comboBox.currentText()
        
        if transfer_account == 'None':
            pass
        else:
            transfer_account_id = self.accounts_dict[transfer_account]
        
        sub_category = self.sub_Category_comboBox.currentText()
        sub_category_id = self.sub_categories_dict[sub_category]
        
        category = self.category_comboBox.currentText()
        category_id = self.categories_dict[category]
        
        category_type = self.category_Type_comboBox.currentText()
        category_type_id = self.category_type_dict[category_type]
        
        max_id = max([trans.id for trans in self.database.app_data['transaction_data']['old']])
        trans_temp_id = random.randint((max_id + 1), (max_id + 10))
        
        transaction_list = [date_formatted, description, amount, category_id, sub_category_id, account_id, category_type_id, month_id, accounting_id]
        
        for _, check in enumerate(transaction_list):
            if check == '':
                QMessageBox.information(self.add_trans_widget, "Empty input",
                                 "One of the inputs is not valid for adding to transactions",
                                 QMessageBox.StandardButton.Ok)
                return False
            else:
                pass
        transaction = Transaction((max_id, date_datetime, account, description, Decimal(amount), category, sub_category, category_type, payback, payback_id, frequency, accounting))
        self.database.app_data['transaction_data']['old'].append(transaction) # Change to 'unsaved' or 'new' later
        df2 = {'ID': trans_temp_id, 'Account': account, 'Description': description, 'Amount': Decimal(amount), 'Category': category, 'SubCategory': sub_category, 'Transaction Type': category_type}
        self.database.app_data['transaction_dataframe'].loc[date_datetime] = df2
        ############## WILL NEED TO UPDATE #####################        
        # print(transaction_list)
        # self.database.insert_transaction_data(transaction_list)
        ########################################################
        return True
        
    def discard_check(self):
        # Validate Input
        ret = QMessageBox.question(self.add_trans_widget, "Confirmation",
                                 "Do you want to clear this transaction?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to exit the application
        if ret == QMessageBox.StandardButton.Yes:
            self.discard_transaction()
            
        # If user chooses not to close application
        elif ret == QMessageBox.StandardButton.Cancel:
            return 
            
        # Close event will be ignored if neither are selected
        else:
            QMessageBox.information(self.add_trans_widget, "Error",
                                 "Something went wrong. Progress not discarded",
                                 QMessageBox.StandardButton.Ok)
            return 
        
    def discard_transaction(self):
        self.account_comboBox.setCurrentIndex(0)
        self.date_dateEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.description_lineEdit.clear()
        self.amount_doubleSpinBox.setProperty("value", 0.00)      
        self.credit_Debit_comboBox.setCurrentIndex(0)
        self.transfer_To_comboBox.setCurrentIndex(0)
        self.sub_Category_comboBox.setCurrentIndex(0)
        self.category_comboBox.setCurrentIndex(0)
        self.category_Type_comboBox.setCurrentIndex(0)