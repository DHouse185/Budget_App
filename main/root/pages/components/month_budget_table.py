##########  Python IMPORTs  ############################################################

import pandas as pd
from decimal import Decimal
import typing
import copy
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import Qt, QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.models import Category
from root.pages.components.ui.month_budget_plan_table import Ui_Form
########################################################################################

class Month_Budget_Table(Ui_Form):
    def __init__(self, parent, database: Database, year: str, account_id: int):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.table = QWidget(parent=parent)
        self.setupUi(self.table)
        self.table.setGeometry(QRect(0, 0, 1910, 640))
        
        self.database = database
        self.year = year
        self.columns_query: typing.List[Category] = [cat.category for cat in self.database.app_data['category']['start_data']]
        self.columns = self.columns_query.copy()

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
        # self.block_query = False
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

                results = next(
                    (getattr(cat_budg, column.lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] 
                     if cat_budg.year == self.year 
                     and cat_budg.month == rvar.month_dict[row] 
                     and ((account_id == 0) or (cat_budg.account_id == account_id))),
                    Decimal(0.00)
                    )
                item.setText(f"${results}")
                if account_id == 0:
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                self.budget_plan_tableWidget.setItem(j, i, item)
                
        self.itemchange = 0
        
    def adjust_budget(self, item: QTableWidgetItem, account_id):
        
        if self.itemchange == 0:
            self.itemchange = 1
            # Get the column and row of the changed item
            column = item.column()
            row = item.row()
            
            # Validate Input
            ret = QMessageBox.question(self.table, "Confirmation",
                                    f"Do you want to change the amount for {self.columns_query[column]} in {self.row_names[row]}?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)# if not self.block_query else QMessageBox.StandardButton.Yes
            
            # If user chooses to change amount
            if ret == QMessageBox.StandardButton.Yes:
                value = item.text()
                try:
                    value.replace('$', '')
                    value = float(value)
                    value = "{:.2f}".format(value)
                    
                except ValueError:
                    QMessageBox.information(self.table, "Value Error",
                                    f"{value} is not a valid number")
                    value = sum(
                        getattr(cat_budg, self.columns[column].lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] 
                        if cat_budg.year == self.year 
                        and cat_budg.month == rvar.month_dict[self.row_names[row]]
                        and ((account_id == 0) or (cat_budg.account_id == account_id))
                        )
                    item.setText(f"${value}")
                    self.itemchange = 0
                    
                    return
                    
            # If user chooses not to close application
            elif ret == QMessageBox.StandardButton.Cancel:
                value = sum(
                        getattr(cat_budg, self.columns[column].lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] 
                            if cat_budg.year == self.year 
                            and cat_budg.month == rvar.month_dict[self.row_names[row]]
                            and ((account_id == 0) or (cat_budg.account_id == account_id))
                        )
                
                item.setText(f"${value}")
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
            
            # Update month budget start data dictionary and placed in unsaved data waiting to be updated
            for month_budg in self.database.app_data['month_budget']['start_data']:
                if month_budg.year == self.year \
                and month_budg.month == rvar.month_dict[self.row_names[row]] \
                and month_budg.account_id == account_id:
                    setattr(month_budg, self.columns[column].lower(), Decimal(value))
                    self.database.app_data['unsaved_data']['UPDATE'].append(month_budg)
                    month_budg.update()
                    # Add change to update dictionary
                    break
            
            changing_columns = ['expected_ending_budget', 'left_amount', 'total']
            col_len = len(self.columns) - 1
            
            for i, column in enumerate(changing_columns):
                col = col_len - i
                altered_item = self.budget_plan_tableWidget.item(row, col)
                
                altered_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                results = next(
                    (getattr(cat_budg, column.lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] 
                     if cat_budg.year == self.year 
                     and cat_budg.month == rvar.month_dict[self.row_names[row]]
                     and ((account_id == 0) or (cat_budg.account_id == account_id))),
                    Decimal(0.00)
                    )
                altered_item.setText(f"${results}")
                
                altered_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            
            self.budget_plan_tableWidget.viewport().update()
            self.itemchange = 0
    
    def update_table(self, year: str, account_id: int):
        # self.block_query = True
        self.itemchange = 1
        self.year = int(year)
        
        # Update each item
        for i, column in enumerate(self.columns):
            for j, row in enumerate(self.row_names):
                item = self.budget_plan_tableWidget.item(j, i)
                
                # if i >= len(self.columns) - 3 or account_id == 0:
                item.setFlags(Qt.ItemFlag.ItemIsEditable)
                
                results = sum(
                    getattr(cat_budg, column.lower()) for cat_budg in self.database.app_data['month_budget']['start_data'] 
                     if cat_budg.year == self.year 
                     and cat_budg.month == rvar.month_dict[row] 
                     and ((account_id == 0) or (cat_budg.account_id == account_id))
                    )
                item.setText(f"${results}")
                
                if i >= len(self.columns) - 3  or account_id == 0:
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        
        self.itemchange = 0
        # self.block_query = False
                
