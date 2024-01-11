##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget, QTableView, QScrollArea, QSizePolicy, QAbstractScrollArea
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QModelIndex, QRect, QAbstractTableModel, Qt, QSize, QSortFilterProxyModel
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.add_transaction import Add_Transaction 
from root.pages.components.yearly_trans_stats import Yearly_Stats 
########################################################################################

class FilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super(FilterProxyModel, self).__init__()

    def filterAcceptsRow(self, source_row, source_parent):
        # CUSTOMIZE LATER TO IMPLEMENT FILTERING LOGIC
        return True

class TableModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
        super(TableModel, self).__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        
    def rowCount(self, index):
        return self._data.shape[0]
    
    def columnCount(self, index):
        return self._data.shape[1]
    
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])
            
            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])        
    
    def resetData(self, updated_dataframe):
        self.beginResetModel()
        self._data = updated_dataframe
        self.endResetModel()
        
    def removeRow(self, row):
        self.beginRemoveRows(QModelIndex(), row, row)
        self._data = self._data.drop(self._data.index[row])
        self.endRemoveRows()
            
class Transactions(QWidget):
    """
    Transaction page that Shows a table of all transactions that has occurred
    """
    def __init__(self, page, database: Database):
        super().__init__(page)
        self.setGeometry(QRect(0, 0, 1920, 1065))
        self.setObjectName("Transaction")
        
        # self.db = Workspace()
        
        # self.notification = notification
        self.transaction_page = page
        self.database = database
        
        # Configure Transaction to be scrollable
        self.transaction_scrollArea = QScrollArea(parent=self.transaction_page)
        self.transaction_scrollArea.setGeometry(QRect(0, 0, 1920, 1090))
        sizePolicy_1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy_1.setHorizontalStretch(0)
        sizePolicy_1.setVerticalStretch(0)
        sizePolicy_1.setHeightForWidth(self.transaction_scrollArea.sizePolicy().hasHeightForWidth())
        self.transaction_scrollArea.setSizePolicy(sizePolicy_1)
        self.transaction_scrollArea.setMaximumSize(QSize(1920, 1065))
        self.transaction_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.transaction_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.transaction_scrollArea.setWidgetResizable(True)
        self.transaction_scrollArea.setObjectName("Transaction_scrollArea")
        
        # Transaction Scroll Area contents
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1910, 1670))
        sizePolicy_2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_2.setHorizontalStretch(0)
        sizePolicy_2.setVerticalStretch(0)
        sizePolicy_2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy_2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1670))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1920, 30000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Transaction Table
        self.transaction_table = QTableView(self.scrollAreaWidgetContents)
        self.transaction_table.setObjectName('transaction_table')
        self.transaction_table.setStyleSheet(rvar.DARK_MODE_TRANS_TABLE)
        self.transaction_table.setGeometry(QRect(415, 420, 1490, 1230))
        self.transaction_table.horizontalHeader().setDefaultSectionSize(175)

        # Add Transaction Widget
        self.transaction_addition = Add_Transaction(self.scrollAreaWidgetContents, self.database)
        self.transaction_stats = Yearly_Stats(self.scrollAreaWidgetContents, self.database)
        self.account_name = self.transaction_stats.stats_Account_comboBox.currentText()
        self.table_df = self.database.app_data['transaction_dataframe'].query("Account == @self.account_name") \
            if self.account_name != 'All' else self.database.app_data['transaction_dataframe']
        self.transaction_model = TableModel(self.table_df)
        self.transaction_table.setModel(self.transaction_model)
        filter_model = FilterProxyModel()
        filter_model.setSourceModel(self.transaction_model)
        # SET FILTER MODEL FOR THE TABLE VIEW
        self.transaction_table.setModel(filter_model)
        # Set the filter key column (the column on which filtering will be applied)
        filter_model.setFilterKeyColumn(-1)  # Set to -1 to filter on all columns
        self.transaction_addition.add_pushButton.clicked.connect(self.add_transaction_to_table)
        self.transaction_addition.remove_pushButton.clicked.connect(self.remove_selected_row)
        self.transaction_stats.stats_Account_comboBox.currentIndexChanged.connect(self.update_account)
        # self.expense_bar_graph = Expense_Bar_Graph()
        # Connect a signal (e.g., from a QLineEdit for user input) to update the filter
        # For example, a QLineEdit named filterLineEdit:
        # filterLineEdit.textChanged.connect(filter_model.setFilterRegExp)
        
        self.transaction_scrollArea.setWidget(self.scrollAreaWidgetContents)
        
    def update_account(self):
        self.account_name = self.transaction_stats.stats_Account_comboBox.currentText()
        updated_df = self.database.app_data['transaction_dataframe'].query("Account == @self.account_name") \
            if self.account_name != 'All' else self.database.app_data['transaction_dataframe']
        self.transaction_model.resetData(updated_df)
        self.transaction_stats.update_data()
        
    def update_page(self):
        self.transaction_addition.update_component()
        self.transaction_stats.stats_Account_comboBox.currentIndexChanged.disconnect(self.update_page)
        accounts_ls = [acc.account for acc in self.database.app_data['account']['start_data']]
        self.transaction_stats.stats_Account_comboBox.clear()
        self.transaction_stats.stats_Account_comboBox.addItem('All')
        self.transaction_stats.stats_Account_comboBox.addItems(accounts_ls)
        self.account_name = self.transaction_stats.stats_Account_comboBox.currentText()
        updated_df = self.database.app_data['transaction_dataframe'].query("Account == @self.account_name") \
            if self.account_name != 'All' else self.database.app_data['transaction_dataframe']
        self.transaction_model.resetData(updated_df)
        self.transaction_stats.update_data()
        self.transaction_stats.stats_Account_comboBox.currentIndexChanged.connect(self.update_page)
            
    def add_transaction_to_table(self):
        trans_conf = self.transaction_addition.add_check()
        if trans_conf:
            updated_df = self.database.app_data['transaction_dataframe']
            self.transaction_model.resetData(updated_df)
            self.transaction_stats.update_data()
            
            # Add new transaction to a place to be added to Postgres sql

    def remove_selected_row(self):
        # Get the selected row index
        selected_index = self.transaction_table.selectionModel().currentIndex()

        if selected_index.isValid():
            row = selected_index.row()
            # Confirm the removal
            
            # Retrieve information about the row
            row_data = {}
            for col in range(self.transaction_model.columnCount(QModelIndex())):
                col_name = str(self.transaction_model.headerData(col, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole))
                col_value = str(self.transaction_model.data(self.transaction_model.index(row, col), Qt.ItemDataRole.DisplayRole))
                row_data[col_name] = col_value
                
            ret = QMessageBox.question(self, 'Confirmation', f'Do you want to remove the selected transactions with ID #{row_data["ID"]}?\n\nRow Data:\n{row_data}',
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

            if ret == QMessageBox.StandardButton.Yes:
                # Utilizing the transaction ID# put in remove transaction dictionary. if in unsaved dictionary remove from that dictionary
                transaction_id = int(row_data["ID"])
                transaction = next((trans for trans in self.database.app_data['transaction_data']['start_data'] if trans.id == int(row_data["ID"])), None)
                if transaction is not None:
                    self.database.app_data['unsaved_data']['DELETE'].append(transaction)
                    self.database.app_data['transaction_data']['start_data'].remove(transaction)
                    # self.database.app_data['unsaved_data']['DELETE'] check for 'INSERT' occurance
                    if transaction in self.database.app_data['unsaved_data']['DELETE'] and transaction in self.database.app_data['unsaved_data']['INSERT']:
                        self.database.app_data['unsaved_data']['INSERT'].remove(transaction)
                        self.database.app_data['unsaved_data']['DELETE'].remove(transaction)

                # Remove the row from the model and DataFrame
                self.transaction_model.removeRow(row)
                
                # Remove the row from the DataFrame
                self.database.app_data['transaction_dataframe'] = self.database.app_data['transaction_dataframe'][self.database.app_data['transaction_dataframe']['ID'] != transaction_id]
                self.transaction_stats.update_data()

        
        