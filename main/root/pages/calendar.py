##########  Python IMPORTs  ############################################################
import pandas as pd
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QScrollArea, QSizePolicy, QAbstractScrollArea
from PyQt6.QtCore import QRect, Qt, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.calendar_info import Calendar_Img 
from root.pages.components.calendar_stats import Calendar_Stats 
########################################################################################
            
class Calendar(QWidget):
    """
    Transaction page that Shows a table of all transactions that has occurred
    """
    def __init__(self, page, database: Database):
        super().__init__(page)
        self.setGeometry(QRect(0, 0, 1920, 1065))
        self.setObjectName("Calendar")
        
        # self.db = Workspace()
        
        # self.notification = notification

        self.calendar_page = page
        self.database = database
        
        # Configure Transaction to be scrollable
        self.calendar_scrollArea = QScrollArea(parent=self.calendar_page)
        self.calendar_scrollArea.setGeometry(QRect(0, 0, 1920, 1090))
        sizePolicy_1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy_1.setHorizontalStretch(0)
        sizePolicy_1.setVerticalStretch(0)
        sizePolicy_1.setHeightForWidth(self.calendar_scrollArea.sizePolicy().hasHeightForWidth())
        self.calendar_scrollArea.setSizePolicy(sizePolicy_1)
        self.calendar_scrollArea.setMaximumSize(QSize(1920, 1065))
        self.calendar_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.calendar_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.calendar_scrollArea.setWidgetResizable(True)
        self.calendar_scrollArea.setObjectName("Calendar_scrollArea")
        
        # Transaction Scroll Area contents
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1910, 1845))
        sizePolicy_2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_2.setHorizontalStretch(0)
        sizePolicy_2.setVerticalStretch(0)
        sizePolicy_2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy_2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1845))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1920, 30000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Add Calendar Widget
        self.calendar_stats = Calendar_Stats(self.scrollAreaWidgetContents, self.database)
        self.year = self.calendar_stats.year
        self.month = self.calendar_stats.month
        self.calendar_img = Calendar_Img(self.scrollAreaWidgetContents, self.database, self.year, self.month)
        self.calendar_stats.init_2(self.calendar_img.credit_list, self.calendar_img.debit_list)
        
        self.calendar_scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.calendar_stats.stats_Month_comboBox.currentTextChanged.connect(self.month_change)
        self.calendar_stats.stats_Year_comboBox.currentTextChanged.connect(self.year_change)
        
    def month_change(self):
        self.calendar_stats.month_change_1()
        self.month = self.calendar_stats.month
        self.calendar_img.month_change(self.month)
        self.calendar_stats.month_change_2(self.calendar_img.credit_list, self.calendar_img.debit_list)
    
    def year_change(self):
        self.calendar_stats.year = self.calendar_stats.stats_Year_comboBox.currentText()
        self.calendar_img.year = self.calendar_stats.stats_Year_comboBox.currentText()
        self.calendar_stats.month_change_1()
        self.month = self.calendar_stats.month
        self.calendar_img.month_change(self.month)
        self.calendar_stats.month_change_2(self.calendar_img.credit_list, self.calendar_img.debit_list)
        
    def update_page(self):
        self.calendar_img.transaction_df: pd.DataFrame = self.database.app_data['transaction_dataframe']
        self.calendar_img.transaction_df_no_date_idx = self.calendar_img.transaction_df.reset_index()
        self.calendar_img.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        self.year_change()