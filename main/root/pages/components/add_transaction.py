##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
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
from root.database import Database
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
        self.accounts = self.database.get_all_data_no_id('account_test')
        
        for _, account in enumerate(self.accounts):  
            self.transfer_To_comboBox.addItem(account[0])
            self.account_comboBox.addItem(account[0])
            
        # Add category type
        self.category_types = self.database.get_all_data_no_id('category_type_test')
        
        for _, category_type in enumerate(self.category_types):  
            self.category_Type_comboBox.addItem(category_type[0])
            
        # Add sub categories
        self.sub_categories = self.database.get_all_data_no_id('sub_category_test')
        
        for _, sub_category in enumerate(self.sub_categories):  
            self.sub_Category_comboBox.addItem(sub_category[0])
            
        # Add Categories
        self.categories = self.database.get_all_data_no_id('category_test')
        
        for _, category in enumerate(self.categories):  
            self.category_comboBox.addItem(category[0])
            
        # Add Accounting type
        self.accountings = self.database.get_all_data_no_id('accounting_type_test')
        
        for _, accounting in enumerate(self.accountings):  
            self.credit_Debit_comboBox.addItem(accounting[0])
            
        self.add_pushButton.clicked.connect(self.add_transaction)
           
    def create_table_dict(self):
        self.accounts_dict = dict()
        self.category_type_dict = dict()
        self.sub_categories_dict = dict()
        self.categories_dict = dict()
        self.accountings_dict = dict()
        
        accounts = self.database.get_all_data_w_id('account_test')
        
        for _, account in enumerate(accounts):  
            self.accounts_dict[account[1]] = account[0]
            print(f"""raw : {accounts}
                  [0] before: {accounts[0]}
                  element[0] : {account[0]}
                  element[1] : {account[1]}""")
            print(self.accounts_dict)
            
        # Add category type
        category_types = self.database.get_all_data_w_id('category_type_test')
        
        for _, category_type in enumerate(category_types):  
            self.category_type_dict[category_type[1]] = category_type[0]
            
        # Add sub categories
        sub_categories = self.database.get_all_data_w_id('sub_category_test')
        
        for _, sub_category in enumerate(sub_categories):  
            self.sub_categories_dict[sub_category[1]] = sub_category[0]
            
        # Add Categories
        categories = self.database.get_all_data_w_id('category_test')
        
        for _, category in enumerate(categories):  
            self.categories_dict[category[1]] = category[0]
            
        # Add Accounting type
        accountings = self.database.get_all_data_w_id('accounting_type_test')
        
        for _, accounting in enumerate(accountings):  
            self.accountings_dict[accounting[1]] = accounting[0]
            
    def add_transaction(self):
        
        # Validate Input
        ret = QMessageBox.question(self.add_trans_widget, "Confirmation",
                                 "Do you want to add this transaction?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to exit the application
        if ret == QMessageBox.StandardButton.Yes:
            pass
            
        # If user chooses not to close application
        elif ret == QMessageBox.StandardButton.Cancel:
            return
            
        # Close event will be ignored if neither are selected
        else:
            QMessageBox.information(self.add_trans_widget, "Error",
                                 "Something went wrong. Transaction was not added",
                                 QMessageBox.StandardButton.Ok)
            return
        
        account = self.account_comboBox.currentText()
        account_id = self.accounts_dict[account]
        
        # Grab Date
        date = self.date_dateEdit.dateTime()
        date_month = date.toString("MMMM")
        date_formatted = date.toString("yyyy-MM-dd")
        
        print(date_month)
        month_id = rvar.month_dict[date_month]
        print(month_id)
        
        description = self.description_lineEdit.text()
        
        amount = self.amount_doubleSpinBox.text()        
        
        accounting = self.credit_Debit_comboBox.currentText()
        accounting_id = self.accountings_dict[accounting]
        
        transfer_account = self.transfer_To_comboBox.currentText()
        
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
        
        transaction_list = [date_formatted, description, amount, category_id, sub_category_id, account_id, category_type_id, month_id, accounting_id]
        
        for _, check in enumerate(transaction_list):
            if check == '':
                QMessageBox.information(self.add_trans_widget, "Empty input",
                                 "One of the inputs is not valid for adding to transactions",
                                 QMessageBox.StandardButton.Ok)
                return
            else:
                pass
                
        print(transaction_list)
        self.database.insert_transaction_data(transaction_list)