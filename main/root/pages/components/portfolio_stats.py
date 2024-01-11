##########  Python IMPORTs  ############################################################
import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.components.ui.portfolio_stats_widget import Ui_Form
from root.database import Database
from root.models import Account_Management, Account
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
        self.update_component(account_dict, year)
        
        self.update_confirm_pushButton.clicked.connect(self.update_check)
        self.add_confirm_pushButton.clicked.connect(self.add_account)
        self.remove_confirm_pushButton.clicked.connect(self.remove_account)
        self.evaluate_Month_dateEdit_2.dateChanged.connect(self.eval_month)
        
    def update_component(self, account_dict, year):
        self.year = year
        self.account_dict = account_dict
        self.add_accounts()
        self.eval_year()
        self.eval_month()
            
    def add_accounts(self):
        self.name_ls = list()
        self.q_name_ls = list()
        self.update_account_comboBox.clear()
        self.remove_account_comboBox.clear()
        for account in self.account_dict.values():
            name = account['name']
            q_name = account['query_name']
            id = account['account_id']
            # NEED TO CHANGE TO MAKE CONCISE
            if name == "Total":
                pass
            
            else:
                self.name_ls.append(name)
                self.q_name_ls.append((name, q_name, id))

        self.update_account_comboBox.addItems(self.name_ls)
        self.remove_account_comboBox.addItems(self.name_ls)
                    
    def eval_year(self): 
        account = next(account for account in self.account_dict.values() if account['name'] == "Total")
        self.amount_total_label.setText(f"${'{:.2f}'.format(account['year'][self.year]['sum'])}") 
        self.amount_year_start_total_label.setText(f"${'{:.2f}'.format(account['year'][self.year]['unfiltered_data'][0][1])}")
        average_change = round(account['year'][self.year]['average_change'], 2)
        
        if average_change > 0:
            self.amount_avg_change_label.setText(f"{'{:.2f}'.format(average_change)} %")
            self.amount_avg_change_label.setStyleSheet("color: #00aa00")
        
        else:
            self.amount_avg_change_label.setText(f"{'{:.2f}'.format(average_change)} %")
            self.amount_avg_change_label.setStyleSheet("color: #c30000")
        
        month_change = account['year'][self.year]['percent_change'][-1][1]
        if month_change > 0:
            self.amount_last_month_change_label.setText(f"{'{:.2f}'.format(month_change)} %")
            self.amount_last_month_change_label.setStyleSheet("color: #00aa00")
        
        else:
            self.amount_last_month_change_label.setText(f"{'{:.2f}'.format(month_change)} %")
            self.amount_last_month_change_label.setStyleSheet("color: #c30000")
            
        expected_end = account['year'][self.year]['expected_data']
        if expected_end != []:
            expected_end = round(expected_end[-1][1], 2)
            self.amount_exp_end_label.setText(f"${'{:.2f}'.format(expected_end)}")
            
        else:
            expected_end = round(account['year'][self.year]['unfiltered_data'][-1][1], 2)
            
            self.amount_exp_end_label.setText(f"${'{:.2f}'.format(expected_end)}")   
            
    def eval_month(self):
        eval_date = self.evaluate_Month_dateEdit_2.date()
        eval_month = eval_date.month() # This will never be 0 | 0 stands for Start
        eval_year = eval_date.year()
        
        if eval_year <= datetime.datetime.now().year:
            account = next(account for account in self.account_dict.values() if account['name'] == "Total")       
            start_amount = next((item[1] for item in account['year'][str(eval_year)]['unfiltered_data'] if item[0] == (eval_month - 1)), "N / A")
            self.amount_start_month_label.setText(f"${'{:.2f}'.format(start_amount)}")
            end_total = next((item[1] for item in account['year'][str(eval_year)]['unfiltered_data'] if item[0] == (eval_month)), "N / A")
            self.amount_month_end_label.setText(f"${'{:.2f}'.format(end_total)}") 
            eval_month_change = next((item[1] for item in account['year'][str(eval_year)]['percent_change'] if item[0] == (eval_month)), "N / A")
            self.amount_month_change_label.setText(f"{'{:.2f}'.format(round(eval_month_change, 2))} %") 
                
            if eval_month_change > 0:
                self.amount_month_change_label.setStyleSheet("color: #00aa00")
                
            else:
                self.amount_month_change_label.setStyleSheet("color: #c30000")
    
    def update_check(self):
        account_ = self.update_account_comboBox.currentText()
        if account_ == '':
            return
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
        query_account = next(item for item in self.q_name_ls if item[0] == account_)
        account_id = query_account[2]
        # print(account_id)
        
        # get amount
        amount = self.update_amount_doubleSpinBox.value()
        
        # Get date
        update_date = self.update_month_dateEdit.date()
        update_month = update_date.month()
        update_year = update_date.year()
        
        if self.start_checkBox.isChecked() and update_month == 1:
            update_month = 0
            
        # self.database.insert_account_data(update_year, update_month, account_id, amount)
        
        account = next(
            (
                acc for acc in self.database.app_data['account_management']['start_data'] if acc.year == update_year
                and acc.month_id == update_month
                and acc.account_id == account_id
             ),
            None)
        if account is not None:
            setattr(account, 'amount', amount)  
            setattr(account, 'account_name', account_)  
            self.database.app_data['unsaved_data']['UPDATE'].append(account)
        else:
            acc_man = Account_Management(
                    (
                        (1000000 * account_id) + (10000 * update_month) + int(update_year),
                        (10000 * int(update_month)) + int(update_year),
                        update_month,
                        account_id,
                        amount
                                    )
                    )
            acc_man.get_accout_name(account_)
            self.database.app_data['account_management']['start_data'].append(acc_man)
            self.database.app_data['unsaved_data']['INSERT'].append(acc_man)
        # print("Successfully updated")
        
    def add_account(self):
        # get account
        account_ = self.account_name_lineEdit.text()        
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
            _ac = next((acc.account for acc in self.database.app_data['account']['start_data'] if acc.account == account_), None)
            
            if _ac is not None:
                QMessageBox.information(self.portfolio_stats, "Error",
                                    "Can't add the account. It would seem that there is already an account with that name",
                                    QMessageBox.StandardButton.Ok)
                return
            
            else:
                account_id = max(([id.id for id in self.database.app_data['account']['start_data']]), default=0) + 1    
                self.database.app_data['account']['start_data'].append(Account((account_id, account_)))
                self.database.app_data['unsaved_data']['INSERT'].append(Account((account_id, account_)))
                # account_id_ = self.database.account_id_request(account_)
                # account_id_ = account_id_[0][0]

                # self.database.insert_account_data(update_year, update_month, account_id, amount)
                account = next(
                    (
                        acc for acc in self.database.app_data['account_management']['start_data'] if acc.year == update_year
                        and acc.month_id == update_month
                        and acc.account_id == account_id
                        ),
                    None
                    )
                if account is not None:
                    setattr(account, 'amount', amount)  
                    setattr(account, 'account_name', account_) 
                    self.database.app_data['unsaved_data']['UPDATE'].append(account)
                else:
                    acc_man = Account_Management(
                            (
                                (1000000 * account_id) + (10000 * update_month) + int(update_year),
                                (10000 * int(update_month)) + int(update_year),
                                update_month,
                                account_id,
                                amount
                                            )
                            )
                    acc_man.get_accout_name(account_)
                    self.database.app_data['account_management']['start_data'].append(acc_man)
                    self.database.app_data['unsaved_data']['INSERT'].append(acc_man)
                     # print("Successfully updated")

    
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
                    
                    # find_account = self.database.account_id_request(account_)
                    find_account = next((id for id in self.database.app_data['account']['start_data'] if id.account == account_ and id.id == account_id), None)
                    
                    if find_account is None:
                        QMessageBox.information(self.portfolio_stats, "Error",
                                    "Can't find the account. It would seem that the account is already removed",
                                    QMessageBox.StandardButton.Ok)
                        return

                    self.database.app_data['unsaved_data']['DELETE'].append(find_account)
                    self.database.app_data['account']['start_data'].remove(find_account)
                    if find_account in self.database.app_data['unsaved_data']['DELETE'] and find_account in self.database.app_data['unsaved_data']['INSERT']:
                        self.database.app_data['unsaved_data']['INSERT'].remove(find_account)
                        self.database.app_data['unsaved_data']['DELETE'].remove(find_account)
    
        