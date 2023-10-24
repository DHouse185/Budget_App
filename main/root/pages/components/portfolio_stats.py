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
from root.pages.components.ui.portfolio_stats_widget import Ui_Form
from root.database import Database
# from pages.dashboard import Dashboard
########################################################################################

class Portfolio_Stats(Ui_Form):
    def __init__(self, parent, database: Database, year, account_dict):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> top_5_expense
        super().__init__()
        self.portfolio_stats = QWidget(parent=parent)
        self.setupUi(self.portfolio_stats)
        self.portfolio_stats.setGeometry(QRect(950, 820, 960, 680))
        self.database = database
        self.year = year
        self.account_dict = account_dict
        
        self.name_ls = list()
        self.q_name_ls = list()
        
        for account in self.account_dict.values():
            name = account['name']
            q_name = account['query_name']
            id = account['account_id']
            
            if name == "Total":
                pass
            
            else:
                self.name_ls.append(name)
                self.q_name_ls.append((name, q_name, id))

        
        self.update_account_comboBox.addItems(self.name_ls)
        self.remove_account_comboBox.addItems(self.name_ls)
        
        self.eval_year()
        self.eval_month()
        
        self.update_confirm_pushButton.clicked.connect(self.update_check)
        self.add_confirm_pushButton.clicked.connect(self.add_account)
        self.remove_confirm_pushButton.clicked.connect(self.remove_account)
                    
    def eval_year(self): 
        for account in self.account_dict.values():
            if account['name'] == "Total":
                self.amount_total_label.setText(f"${account['year'][self.year]['sum']}") 
                self.amount_year_start_total_label.setText(f"${account['year'][self.year]['unfiltered_data'][0][1]}")
                
                average_change = round(account['year'][self.year]['average_change'], 2)
                if average_change > 0:
                    self.amount_avg_change_label.setText(f"{average_change} %")
                    self.amount_avg_change_label.setStyleSheet("color: #00aa00")
                
                else:
                    self.amount_avg_change_label.setText(f"{average_change} %")
                    self.amount_avg_change_label.setStyleSheet("color: #c30000")
                
                month_change = account['year'][self.year]['percent_change'][-1][1]
                if month_change > 0:
                    self.amount_last_month_change_label.setText(f"{month_change} %")
                    self.amount_last_month_change_label.setStyleSheet("color: #00aa00")
                
                else:
                    self.amount_last_month_change_label.setText(f"{month_change} %")
                    self.amount_last_month_change_label.setStyleSheet("color: #c30000")
                    
                expected_end = account['year'][self.year]['expected_data']
                
                if expected_end != []:
                    expected_end = round(expected_end[-1][1], 2)
                    self.amount_exp_end_label.setText(f"${expected_end}")
                    
                else:
                    expected_end = round(account['year'][self.year]['unfiltered_data'][-1][1], 2)
                    
                    self.amount_exp_end_label.setText(f"${expected_end}")   
                            
    def eval_month(self):
        eval_date = self.evaluate_Month_dateEdit_2.date()
        eval_month = eval_date.month() # This will never be 0 - 0 stands for Start
        eval_year = eval_date.year()
        
        if eval_year <= datetime.datetime.now().year:
            for account in self.account_dict.values():
                if account['name'] == "Total":
                    
                    start_amount = [item for item in account['year'][str(eval_year)]['unfiltered_data'] if item[0] == (eval_month - 1)]
                    
                    if start_amount == []:
                        self.amount_start_month_label.setText("N / A")
                    
                    else:
                        self.amount_start_month_label.setText(f"${start_amount[0][1]}") 

                    end_total = [item for item in account['year'][str(eval_year)]['unfiltered_data'] if item[0] == (eval_month)]
                    
                    if end_total == []:
                        self.amount_month_end_label.setText("N / A")
                    
                    else:
                        self.amount_month_end_label.setText(f"${end_total[0][1]}") 
                    
                    eval_month_change = [item for item in account['year'][str(eval_year)]['percent_change'] if item[0] == (eval_month)]
                    
                    if eval_month_change == []:
                        self.amount_month_change_label.setText("N / A")
                    
                    else:
                        self.amount_month_change_label.setText(f"{round(eval_month_change[0][1], 2)} %") 
                        
                        if eval_month_change[0][1] > 0:
                            self.amount_month_change_label.setStyleSheet("color: #00aa00")
                            
                        else:
                            self.amount_month_change_label.setStyleSheet("color: #c30000")
    
    def update_check(self):
        account_ = self.update_account_comboBox.currentText()
        # Get date
        update_date = self.update_month_dateEdit.date()
        update_month = update_date.month()
        update_year = update_date.year()
        
        # Validate Input
        ret = QMessageBox.question(self.portfolio_stats, "Confirmation",
                                f"Do you want to update the account {account_} for {update_month}/{update_year}?",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to change amount
        if ret == QMessageBox.StandardButton.Yes:
            if self.start_checkBox.isChecked() and update_month == 1:
                update_month = 0
                ret_2 = QMessageBox.question(self.portfolio_stats, "Year Start Amount",
                                f"The Start Checkbox is checked for the month of January. This will add the amount to the start column. " + \
                                    "This will be the value for the start of the year. Was this intended?",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                
                if ret_2 == QMessageBox.StandardButton.Yes:
                    self.update_account_amount()
                    QMessageBox.information(self.portfolio_stats, "Successfully updated",
                                "Successfully updated the account",
                                QMessageBox.StandardButton.Ok)
                    return
                
                elif ret_2 == QMessageBox.StandardButton.Cancel:
                    return
                
            else:
                self.update_account_amount()
                QMessageBox.information(self.portfolio_stats, "Successfully updated",
                                "Successfully updated the account",
                                QMessageBox.StandardButton.Ok)
                return
                                
    def update_account_amount(self):
        # get account
        account_ = self.update_account_comboBox.currentText()
        query_account = [item for item in self.q_name_ls if item[0] == account_]
        account_id = query_account[0][2]
        print(account_id)
        
        # get amount
        amount = self.update_amount_doubleSpinBox.value()
        
        # Get date
        update_date = self.update_month_dateEdit.date()
        update_month = update_date.month()
        update_year = update_date.year()
        
        if self.start_checkBox.isChecked() and update_month == 1:
            update_month = 0
            
        self.database.insert_account_data(update_year, update_month, account_id, amount)
        
        print("Successfully updated")
        
    def add_account(self):
        # get account
        account_ = self.account_name_lineEdit.text()

        print(account_)
        
        # get amount
        amount = self.add_account_doubleSpinBox.value()
        
        # Get date
        update_date = self.add_month_dateEdit.date()
        update_month = update_date.month()
        update_year = update_date.year()
        
        # Validate Input
        ret = QMessageBox.question(self.portfolio_stats, "Confirmation",
                                f"Do you want to add the account - {account_}?",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to change amount
        if ret == QMessageBox.StandardButton.Yes:
                
            add_ac = self.database.add_account(account_)
            
            if not add_ac:
                QMessageBox.information(self.portfolio_stats, "Error",
                                    "Can't add the account. It would seem that there is already an account with that name",
                                    QMessageBox.StandardButton.Ok)
                return
            
            elif add_ac:
                account_id_ = self.database.account_id_request(account_)
                account_id_ = account_id_[0][0]
                print(account_id_)
                self.database.insert_account_data(update_year, update_month, account_id_, amount)
                print("Successfully updated")
    
    def remove_account(self):
        account_ = self.remove_account_comboBox.currentText()
        
        # Validate Input
        ret = QMessageBox.question(self.portfolio_stats, "Confirmation",
                                f"Are you sure you want to delete the account - {account_}?" \
                                    + "\n Once it's remove, the data cannot be recovered.",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to change amount
        if ret == QMessageBox.StandardButton.Yes:
                ret_2 = QMessageBox.question(self.portfolio_stats, "Confirmation",
                                             "\n This is not recommended unless there are no transactions on this account" \
                                             + "or the account was added by accident.\n If a value is wrong in one of the months, just update the value." \
                                             + f"\nAre you sure? Account '{account_.upper()}' will be removed.",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                
                if ret_2 == QMessageBox.StandardButton.Yes:
                    query_account = [item for item in self.q_name_ls if item[0] == account_]
                    account_id = query_account[0][2]
                    
                    find_account = self.database.account_id_request(account_)
                    
                    if find_account == []:
                        QMessageBox.information(self.portfolio_stats, "Error",
                                    "Can't find the account. It would seem that the account is already removed",
                                    QMessageBox.StandardButton.Ok)
                        return
                    
                    elif find_account != []:
                        
                        self.database.remove_account(account_, account_id)
                        print("Successfully removed")        
        