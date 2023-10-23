##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget, QTableView, QScrollArea, QSizePolicy, QAbstractScrollArea, QTableWidgetItem
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QModelIndex, QRect, QAbstractTableModel, Qt, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.month_budget_table import Month_Budget_Table 
from root.pages.components.month_budget_stats import Month_Budget_Stats 
from root.pages.components.monthly_budget_lc import MB_LineChart 
########################################################################################
            
class Monthly_Budget(QWidget):
    """
    Transaction page that Shows a table of all transactions that has occurred
    """
    def __init__(self, page, database: Database):
        super().__init__(page)
        self.setGeometry(QRect(0, 0, 1920, 1065))
        self.setObjectName("Calendar")
        
        # self.db = Workspace()
        
        # self.notification = notification

        self.monthly_budget_page = page
        self.database = database
        
        # Configure Transaction to be scrollable
        self.monthly_budget_scrollArea = QScrollArea(parent=self.monthly_budget_page)
        self.monthly_budget_scrollArea.setGeometry(QRect(0, 0, 1920, 1090))
        sizePolicy_1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy_1.setHorizontalStretch(0)
        sizePolicy_1.setVerticalStretch(0)
        sizePolicy_1.setHeightForWidth(self.monthly_budget_scrollArea.sizePolicy().hasHeightForWidth())
        self.monthly_budget_scrollArea.setSizePolicy(sizePolicy_1)
        self.monthly_budget_scrollArea.setMaximumSize(QSize(1920, 1065))
        self.monthly_budget_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.monthly_budget_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.monthly_budget_scrollArea.setWidgetResizable(True)
        self.monthly_budget_scrollArea.setObjectName("Monthly_Budget_scrollArea")
        
        # Monthly Budget Scroll Area contents
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1910, 1090))
        sizePolicy_2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_2.setHorizontalStretch(0)
        sizePolicy_2.setVerticalStretch(0)
        sizePolicy_2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy_2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1100))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1920, 30000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Add Calendar Widget
        self.month_budget_statistics = Month_Budget_Stats(self.scrollAreaWidgetContents, self.database)
        self.data_year = self.month_budget_statistics.year
        self.month_budget_tbl = Month_Budget_Table(self.scrollAreaWidgetContents, self.database, self.data_year)
        self.line_chart_wid = MB_LineChart(self.scrollAreaWidgetContents, 
                                           self.month_budget_tbl.budget_plan_tableWidget,
                                           self.data_year)
        
        self.monthly_budget_scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.month_budget_statistics.month_budget_year_comboBox.currentTextChanged.connect(self.year_change)
        self.month_budget_tbl.budget_plan_tableWidget.itemChanged.connect(self.update_data)
        
    def year_change(self, year: str):
        self.data_year = year
        check = self.month_budget_statistics.change_year(self.data_year)

        if not check:
            return
        
        else:
            self.month_budget_tbl.update_table(self.data_year)
            self.month_budget_tbl.budget_plan_tableWidget.viewport().update()
            
    def update_data(self, item: QTableWidgetItem):
        self.month_budget_tbl.adjust_budget(item)
        self.month_budget_statistics.change_stats(self.data_year)
        self.line_chart_wid.update_data(self.month_budget_tbl.budget_plan_tableWidget)
        