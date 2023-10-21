##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import calendar
import pandas as pd
########################
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
from root.pages.components.ui.calendar_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Calendar_Img(Ui_Form):
    def __init__(self, parent, database: Database, year: str, month: str):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.calendar = QWidget(parent=parent)
        self.setupUi(self.calendar)
        self.calendar.setGeometry(QRect(390, 0, 1520, 1841))
        
        self.database = database
        self.month = month
        self.month_int = rvar.month_dict[self.month]
        self.year = year
        self.month_title_label.setText(f"{self.month}")
        
        self.transaction_df = self.database.start_up_transaction_data
        self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        self.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        
        # Get first day of the month
        date_1 = datetime.datetime(year=int(self.year), month=(self.month_int), day=1)

        # Get first day weekday
        self.first_date_weekday = date_1.weekday()
        
        if self.first_date_weekday == 6:
            self.first_date_weekday = 0
        else:
            self.first_date_weekday += 1
            

        # Get last day of the month
        months_range = calendar.monthrange(int(self.year), (self.month_int))

        
        self.credit_list = []
        self.debit_list = [] 
        
        month_day = 1
        for label in range(len(self.date_label_list)):
            if label >= (months_range[1] + self.first_date_weekday):
                self.date_label_list[label].setText(f" ")
                self.credit_list.append(0)
                self.debit_list.append(0)
                
            elif label < self.first_date_weekday:
                self.date_label_list[label].setText(f" ")
                self.credit_list.append(0)
                self.debit_list.append(0)
                
            elif label < (months_range[1] + self.first_date_weekday):
                date = datetime.datetime(year=int(self.year), month=(self.month_int), day=month_day)
                date = f"{date.strftime('%Y-%m-%d')}"
                self.date_label_list[label].setText(f"{month_day}")
                
                credit = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] == date)
                                               & (self.transaction_df_no_date_idx['Transaction Type'] == 'Income'), 'Amount'].sum()
                space_1 = 24 - (len(str(credit)) * 2)
                self.date_credit_label_list[label].setText((("$                          ") + (f"{credit}".rjust(space_1, ' '))))
                
                self.credit_list.append(credit)
                
                debit = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] == date)
                                               & (self.transaction_df_no_date_idx['Transaction Type'] == 'Expense'), 'Amount'].sum()
                space_2 = 24 - (len(str(debit)) * 2)
                self.date_debit_label_list[label].setText((("$                          ") + (f"{debit}".rjust(space_2, ' '))))

                self.debit_list.append(debit)
                
                transactions = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] == date), 'Description']
                if transactions.empty:
                    self.date_expense_label_list[label].setText("-")
                else:
                    transaction_str = transactions.to_string(header=False, index=False).split('\n')
                    # print(f"transactions {label} before full string conversion:")
                    # print(transaction_str)
                    transaction_str = [''.join(ele.split('  ')) for ele in transaction_str]
                    # print(f"transactions {label} string conversion:")
                    # print(transaction_str)
                    self.date_expense_label_list[label].setText(", ".join( str(e) for e in transaction_str))
                    
                month_day += 1
                
            else:
                self.date_label_list[label].setText(f" ")
                self.credit_list.append(0)
                self.debit_list.append(0)
                
    def month_change(self, month: str):
        
        self.month = month
        self.month_int = rvar.month_dict[self.month]
        self.month_title_label.setText(f"{self.month}")
        
        # Get first day of the month
        date_1 = datetime.datetime(year=int(self.year), month=(self.month_int), day=1)

        # Get first day weekday
        self.first_date_weekday = date_1.weekday()
        
        if self.first_date_weekday == 6:
            self.first_date_weekday = 0
        else:
            self.first_date_weekday += 1

        # Get last day of the month
        months_range = calendar.monthrange(int(self.year), (self.month_int))
        
        self.credit_list = []
        self.debit_list = [] 
        
        month_day = 1
        for label in range(len(self.date_label_list)):
            if label >= (months_range[1] + self.first_date_weekday):
                self.date_label_list[label].setText(f" ")
                self.date_credit_label_list[label].setText("$                                              -")
                self.date_debit_label_list[label].setText("$                                              -")
                self.date_expense_label_list[label].setText("-")
                self.credit_list.append(0)
                self.debit_list.append(0)
                
            elif label < self.first_date_weekday:
                self.date_label_list[label].setText(f" ")
                self.date_credit_label_list[label].setText("$                                              -")
                self.date_debit_label_list[label].setText("$                                              -")
                self.date_expense_label_list[label].setText("-")
                self.credit_list.append(0)
                self.debit_list.append(0)
                
            elif label < (months_range[1] + self.first_date_weekday):
                date = datetime.datetime(year=int(self.year), month=(self.month_int), day=month_day)
                date = f"{date.strftime('%Y-%m-%d')}"
                self.date_label_list[label].setText(f"{month_day}")
                
                credit = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] == date)
                                               & (self.transaction_df_no_date_idx['Transaction Type'] == 'Income'), 'Amount'].sum()
                space_1 = 24 - (len(str(credit)) * 2)
                self.date_credit_label_list[label].setText((("$                          ") + (f"{credit}".rjust(space_1, ' '))))
                
                self.credit_list.append(credit)
                
                debit = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] == date)
                                               & (self.transaction_df_no_date_idx['Transaction Type'] == 'Expense'), 'Amount'].sum()
                space_2 = 24 - (len(str(debit)) * 2)
                self.date_debit_label_list[label].setText((("$                          ") + (f"{debit}".rjust(space_2, ' '))))

                self.debit_list.append(debit)
                
                transactions = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] == date), 'Description']
                if transactions.empty:
                    self.date_expense_label_list[label].setText("-")
                else:
                    transaction_str = transactions.to_string(header=False, index=False).split('\n')
                    # print(f"transactions {label} before full string conversion:")
                    # print(transaction_str)
                    transaction_str = [''.join(ele.split('  ')) for ele in transaction_str]
                    # print(f"transactions {label} string conversion:")
                    # print(transaction_str)
                    self.date_expense_label_list[label].setText(", ".join( str(e) for e in transaction_str))
                    
                month_day += 1
                
            else:
                self.date_label_list[label].setText(f" ")
                self.date_credit_label_list[label].setText("$                                              -")
                self.date_debit_label_list[label].setText("$                                              -")
                self.date_expense_label_list[label].setText("-")
                self.credit_list.append(0)
                self.debit_list.append(0)