##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import calendar
import pandas as pd
import decimal
import typing
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow, 
                             QWidget, 
                             QMessageBox, 
                             QStackedWidget, 
                             QWidget,
                             QGridLayout,
                             QLabel,
                             QTableWidgetItem)
from PyQt6.QtGui import QAction, QDoubleValidator
from PyQt6.QtCore import Qt, QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.ui.month_budget_plan_table import Ui_Form
########################################################################################

class Month_Budget_Table(Ui_Form):
    def __init__(self, parent, database: Database, year: str):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.table = QWidget(parent=parent)
        self.setupUi(self.table)
        self.table.setGeometry(QRect(0, 0, 1910, 640))
        
        self.database = database
        # self.transaction_df = self.database.start_up_transaction_data
        # self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        # self.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        
        self.year = year
        columns_query = self.database.query_column("category_test", "category")
        self.columns = list()
        self.columns_query = list()
        
        for column in columns_query:
            self.columns.append(column[0])
            self.columns_query.append(column[0])

        self.columns.remove('Payment')
        self.columns.append('starting_budget')
        self.columns.append('total')
        self.columns.append('left_amount')
        self.columns.append('expected_ending_budget')
        self.columns = ['_'.join(ele.split(' ')) for ele in self.columns]
        
        self.columns_query.remove('Payment')
        self.columns_query.append('Starting Budget')
        self.columns_query.append('Total')
        self.columns_query.append('Left Amount')
        self.columns_query.append('Expected Ending Budget')
        
        self.budget_plan_tableWidget.setColumnCount((len(self.columns)))
        self.budget_plan_tableWidget.setWordWrap(True)
        
        # self.table_column_data = list()
        
        # Create columns
        for idx, column in enumerate(self.columns_query):
            item = QTableWidgetItem()
            self.budget_plan_tableWidget.setHorizontalHeaderItem(idx, item)
            self.budget_plan_tableWidget.horizontalHeaderItem(idx).setText(column)
                    
        for i, column in enumerate(self.columns):
            for j, row in enumerate(self.row_names):
                item = QTableWidgetItem()
                if i >= len(self.columns) - 3:
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                # item = self.budget_plan_tableWidget.item(j, i)
                results = self.database.category_budget(self.year, rvar.month_dict[row], column)
                print('results: ')
                print(results[0][0])
                item.setText(f"${results[0][0]}")
                self.budget_plan_tableWidget.setItem(j, i, item)
                
        self.itemchange = 0
        # self.budget_plan_tableWidget.itemChanged.connect(self.adjust_budget)
        # budget_plan_results = self.database.budget_for_year_table(self.year)
        # print(f"budget_plan_results: {budget_plan_results}")
        # self.budget_plan_df = pd.DataFrame(budget_plan_results) #, columns=['Date', 'Account', 'Description', 'Amount', 'Category', 'SubCategory', 'Transaction Type'])
        # #print(start_up_df)
        # print(f"self.budget_plan_df: {self.budget_plan_df}")
        
    def adjust_budget(self, item: QTableWidgetItem):
        if self.itemchange == 0:
            self.itemchange = 1
            # Get the column and row of the changed item
            column = item.column()
            row = item.row()
            
            # Validate Input
            ret = QMessageBox.question(self.table, "Confirmation",
                                    f"Do you want to change the amount for {self.columns_query[column]} in {self.row_names[row]}?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            
            # If user chooses to change amount
            if ret == QMessageBox.StandardButton.Yes:
                value = item.text()
                try:
                    value = float(value)
                    value = "{:.2f}".format(value)
                    
                except ValueError:
                    QMessageBox.information(self.table, "Value Error",
                                    f"{value} is not a valid number")
                    value = self.database.category_budget(self.year, rvar.month_dict[self.row_names[row]], self.columns[column])
                    value = value[0][0]
                    print(f"Value after Error: {value}")
                    item.setText(f"${value}")
                    print(f"Changed cell at column {column}, row {row} to {value}")
                    self.itemchange = 0
                    
                    return
                    
            # If user chooses not to close application
            elif ret == QMessageBox.StandardButton.Cancel:
                # results = self.database.category_budget(self.year, rvar.month_dict[self.row_names[row]], self.columns[column])
                # value = results[0][0]
                value = self.database.category_budget(self.year, rvar.month_dict[self.row_names[row]], self.columns[column])
                value = value[0][0]
                
                print(f"Cancelled change -- value changed to {value}")
                item.setText(f"${value}")
                print(f"Changed cell at column {column}, row {row} to {value}")
                self.itemchange = 0
                
                return

            # Close event will be ignored if neither are selected
            else:
                QMessageBox.information(self.table, "Error",
                                    "Something went wrong. Transaction was not added",
                                    QMessageBox.StandardButton.Ok)
                
                self.itemchange = 0
                return
            
            item.setText(f"${value}")
            print(f"Changed cell at column {column}, row {row} to {value}")
            
            self.database.change_budget(self.year, rvar.month_dict[self.row_names[row]], self.columns[column], str(value))
            print("Database updated")
            
            changing_columns = ['expected_ending_budget', 'left_amount', 'total']
            col_len = len(self.columns) - 1
            
            for i, column in enumerate(changing_columns):
                col = col_len - i
                altered_item = self.budget_plan_tableWidget.item(row, col)
                print(f"Altered Item text Before Change: {altered_item.text()}")
                
                altered_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                results = self.database.category_budget(self.year, rvar.month_dict[self.row_names[row]], column)
                print('results: ')
                print(results[0][0])
                altered_item.setText(f"${results[0][0]}")
                
                # Print statements for debugging:
                print(f"Altered column: {col}")
                print(f"Altered row: {row} ")
                altered_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                print(f"Altered Item text: {altered_item.text()}")
            
            self.budget_plan_tableWidget.viewport().update()
            self.itemchange = 0
    
    def update_table(self, year: str):
        self.itemchange = 1
        self.year = year
        
        # Update each item
        for i, column in enumerate(self.columns):
            for j, row in enumerate(self.row_names):
                item = self.budget_plan_tableWidget.item(j, i)
                
                if i >= len(self.columns) - 3:
                    item.setFlags(Qt.ItemFlag.ItemIsEditable)
                
                results = self.database.category_budget(self.year, rvar.month_dict[row], column)
                print('results: ')
                print(results[0][0])
                item.setText(f"${results[0][0]}")
                
                if i >= len(self.columns) - 3:
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        
        self.itemchange = 0
                
#####################

# EXAMPLE

#####################

# self._base_params_data_collect = [
#             {"code_name": "exchange", "widget": QComboBox, "data_type": str, "values": r_var.EXCHANGES, "width": 200},
#             {"code_name": "pairs", "widget": QComboBox, "data_type": str, "values": self.binance_symbols, "width": 150},
#             {"code_name": "timeframe", "widget": QComboBox, "data_type": str, "values": r_var.TIME_FRAMES, "width": 150},
#             {"code_name": "from_time", "widget": QDateEdit, "data_type": QDate, "width": 150},
#             {"code_name": "to_time", "widget": QDateEdit, "data_type": QDate, "width": 150},
#         ]