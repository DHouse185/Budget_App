##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget, QTableView, QScrollArea
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QModelIndex, QRect, QAbstractTableModel, Qt
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.dashboard_header import Header 
########################################################################################

class TableModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame):
        super(TableModel, self).__init__()
        self._data = data
        
    def get_data(self, index, role):
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

class TransactionTable(QWidget):
    def __init__(self, dataframe: pd.DataFrame, parent: QWidget):
        super().__init__(parent)
        self.setGeometry(QRect(763, 5, 1152, 852))
        self.setObjectName("Transaction_Table_Widget")
        
        # Configure Transaction to be scrollable
        self.scrollarea = QScrollArea(self) 
        self.scrollarea.setObjectName("Transaction_scrollArea")
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.height(852)
        self.scrollarea.width(1152)
        self.scrollarea.setMaximumSize(1920, 1065)
        
        self.scrollareacontent = QWidget()
        
        self.dataframe = dataframe
        
        self.table = QTableView(self.scrollareacontent)
        
        self.model = TableModel(self.dataframe)
        self.table.setModel(self.model)

class Transaction_Stats(QWidget):
    def __init__(self, dataframe: pd.DataFrame, parent: QWidget):
        super().__init__(parent)
        self.setGeometry(QRect(5, 5, 738, 532))
        self.setObjectName("Transaction_Stat_Table_Widget")
        self.dataframe = dataframe
        
        current_date = datetime.now()
        current_year = current_date.year
        
        todays_days = rfunc.number_of_days(datetime(current_year, 1, 1), current_date)

        expense_series = np.where(self.dataframe['Transaction Type'] == 'Expense', int(self.dataframe['Amount']), 0)
        income_series = np.where(self.dataframe['Transaction Type'] == 'Income', int(self.dataframe['Amount']), 0)
        
        data = pd.DataFrame(
            [
                [str(current_year)]
                [round(np.sum(expense_series), 2)],
                [round(np.sum(income_series), 2)],
                [round((np.sum(expense_series))/(todays_days), 2)],
                [round((np.sum(expense_series)/(todays_days))*7, 2)],
                [round((np.sum(expense_series)/(todays_days))*365, 2)],
                [round((np.sum(income_series))/(todays_days), 2)],
                [round((np.sum(income_series)/(todays_days))*7, 2)],
                [round((np.sum(income_series)/(todays_days))*14, 2)],
                [round((np.sum(income_series)/(todays_days))*365, 2)]    
            ],
        columns=["Stats"], 
        index=["Year", "Total Spent", "Total Income", "Daily Average Expense", "Weekly Average Expense",
               "Predicted Total Expense", "Daily Average Income", "Weekly Average Income", "Bi-Weekly Average Income", "Predicted Yearly Income"])
        
        self.table = QTableView(self)
        
        self.model = TableModel(self.dataframe)
        self.table.setModel(self.model)

class Transactions(QWidget):
    """
    Transaction page that Shows a table of all transactions that has occurred
    """
    def __init__(self, page, database: Database):
        super().__init__(page)
        self.setGeometry(QRect(0, 0, 1920, 1065))
        self.setObjectName("Dashboard")
        
        # self.db = Workspace()
        
        # self.notification = notification
        
        # Configure Transaction to be scrollable
        self.scrollarea = QScrollArea(self) 
        self.scrollarea.setObjectName("Transaction_scrollArea")
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.height(1065)
        self.scrollarea.width(1920)
        self.scrollarea.setMaximumSize(1920, 1065)
        
        self.scrollareacontent = QWidget()

        self.transaction_page = page
        self.database = database
        
        self.transaction_df = database.start_up_transaction_data
        
        self.transaction_table = TransactionTable(self.transaction_df, self.scrollareacontent)
        self.transaction_stats = Transaction_Stats(self.transaction_df, self.scrollareacontent)
        
        
        self.scrollarea.setWidget(self.scrollareacontent)
        