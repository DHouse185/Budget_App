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
from root.pages.components.portfolio_widget import Portfolio_Widget
from root.pages.components.portfolio_stats import Portfolio_Stats
from root.pages.components.portfolio_lc import Portfolio_LineChart
########################################################################################
            
class Portfolio(QWidget):
    """
    Transaction page that Shows a table of all transactions that has occurred
    """
    def __init__(self, page, database: Database):
        super().__init__(page)
        self.setGeometry(QRect(0, 0, 1920, 1065))
        self.setObjectName("Portfolio")
        
        # self.db = Workspace()
        # self.notification = notification

        self.portfolio_page = page
        self.database = database
        
        # Configure Transaction to be scrollable
        self.portfolio_main_scrollArea = QScrollArea(parent=self.portfolio_page)
        self.portfolio_main_scrollArea.setGeometry(QRect(0, 0, 1920, 1090))
        sizePolicy_1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy_1.setHorizontalStretch(0)
        sizePolicy_1.setVerticalStretch(0)
        sizePolicy_1.setHeightForWidth(self.portfolio_main_scrollArea.sizePolicy().hasHeightForWidth())
        self.portfolio_main_scrollArea.setSizePolicy(sizePolicy_1)
        self.portfolio_main_scrollArea.setMaximumSize(QSize(1920, 1065))
        self.portfolio_main_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.portfolio_main_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.portfolio_main_scrollArea.setWidgetResizable(True)
        self.portfolio_main_scrollArea.setObjectName("portfolio_main_scrollArea")
        
        self.portfolio_main_scrollAreaWidgetContents = QWidget()
        self.portfolio_main_scrollAreaWidgetContents.setEnabled(True)
        self.portfolio_main_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1905, 1500))
        sizePolicy_2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_2.setHorizontalStretch(0)
        sizePolicy_2.setVerticalStretch(0)
        sizePolicy_2.setHeightForWidth(self.portfolio_main_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.portfolio_main_scrollAreaWidgetContents.setSizePolicy(sizePolicy_2)
        self.portfolio_main_scrollAreaWidgetContents.setMinimumSize(QSize(0, 1500))
        self.portfolio_main_scrollAreaWidgetContents.setMaximumSize(QSize(1920, 30000))
        self.portfolio_main_scrollAreaWidgetContents.setObjectName("portfolio_main_scrollAreaWidgetContents")
        
        # Portfolio widget
        self.portfolio_wid = Portfolio_Widget(self.portfolio_main_scrollAreaWidgetContents, self.database)
        self.year = self.portfolio_wid.year
        self.account_dictionary = self.portfolio_wid.account_dict        
        
        # Update and stats widget
        # year var. & dict stats var. pass to -> stats Widget
        self.portfolio_stats = Portfolio_Stats(self.portfolio_main_scrollAreaWidgetContents, self.database, self.year, self.account_dictionary)
        
        # Chart widget
        # pass dict stats widget var. -> chart widget
        self.line_chart_wid = Portfolio_LineChart(self.portfolio_main_scrollAreaWidgetContents, 
                                    self.account_dictionary,
                                    self.year)
        
        # Signals
        self.portfolio_wid.stats_Year_comboBox.currentTextChanged.connect(self.update_year)
        
        # Evaluate signal
        
        # Update signal
        
        # Add account signal
        
        # Remove account signal
        
        # Chart signal
        
        self.portfolio_main_scrollArea.setWidget(self.portfolio_main_scrollAreaWidgetContents)
        
    def update_year(self):
        self.prev_year = self.year
        self.year = self.portfolio_wid.stats_Year_comboBox.currentText()
        self.portfolio_stats.year = self.year
        self.line_chart_wid.year = self.year
        
        self.portfolio_stats.eval_year()
        self.portfolio_wid.year_change(prev_year=self.prev_year, new_year=self.year)
    # def update_account(self):
    #     ...
    
    # def add_account(self):
    #     ...
    
    # def remove_account(self):
    #     ...
    
    # def charting(self):
    #     ...
            
            