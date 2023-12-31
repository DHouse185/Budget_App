##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget, QTableView, QScrollArea, QSizePolicy, QAbstractScrollArea
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QModelIndex, QRect, QAbstractTableModel, Qt, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.add_transaction import Add_Transaction 
from root.pages.components.yearly_trans_stats import Yearly_Stats 
########################################################################################


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
        self.transaction_table.horizontalHeader().setDefaultSectionSize(200)
        self.transaction_model = TableModel(self.database.start_up_transaction_data)
        self.transaction_table.setModel(self.transaction_model)
        
        # Add Transaction Widget
        self.transaction_addition = Add_Transaction(self.scrollAreaWidgetContents, self.database)
        # Add Transaction Stats
        self.transaction_stats = Yearly_Stats(self.scrollAreaWidgetContents, self.database)
        # self.expense_bar_graph = Expense_Bar_Graph()
        
        self.transaction_scrollArea.setWidget(self.scrollAreaWidgetContents)

        
        