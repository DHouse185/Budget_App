##########  Python IMPORTs  ############################################################
from pathlib import Path
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
from root.pages.components.ui.month_progress_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Month_progress(Ui_Form):
    def __init__(self, parent, database):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> top_5_expense
        super().__init__()
        self.month_progress = QWidget(parent=parent)
        self.setupUi(self.month_progress)
        self.month_progress.setGeometry(QRect(0, 1310, 1910, 251))
        self.database = database
        
        budget_array = [self.month_col_label, self.month_col_Income_label, self.month_col_Eating_Out_label, 
                        self.month_col_Groceries_label, self.month_col_Transportation_label, 
                        self.month_col_Free_Expense_label, self.month_col_Investment_label, 
                        self.month_col_Bills_label, self.month_col_Support_label, self.month_col_Goal_label, 
                        self.month_col_Sum_Total_label, self.month_col_Profit_Loss_label]
        spent_array = [self.spent_col_label, self.spent_col_Income_label, self.spent_col_Eating_Out_label,
                       self.spent_col_Groceries_label, self.spent_col_Transportation_label,
                       self.spent_col_Free_Expense_label, self.spent_col_Investment_label,
                       self.spent_col_Bills_label, self.spent_col_Support_label, self.spent_col_Goal_label,
                       self.spent_col_Sum_Total_label, self.spent_col_Profit_Loss_label]
        left_array = [self.left_col_label, self.left_col_Income_label, self.left_col_Eating_Out_label,
                      self.left_col_Groceries_label, self.left_col_Transportation_label, 
                      self.left_col_Free_Expense_label, self.left_col_Investment_label,
                      self.left_col_Bills_label, self.left_col_Support_label, self.left_col_Goal_label,
                      self.left_col_Sum_Total_label]
        progressbar_array = [self.income_progressBar, self.eating_Out_progressBar, 
                             self.groceries_progressBar, self.transportation_progressBar, self.free_Expense_progressBar,
                             self.investment_progressBar, self.bills_progressBar, self.support_progressBar, 
                             self.goal_progressBar, self.sum_Total_progressBar]
        cb_month = rvar.month_dict[self.month_progress_comboBox.currentText()]
        print(f"cb_month: {cb_month}")
        self.data = self.database.retrieve_dashboard_month_progress(cb_month,
                                                                    self.Stats_Year_comboBox.currentText())
        print(self.data)
        for idx, label in enumerate(budget_array):
            text = self.data[0][idx]
            label.setText(f"${str(text)}")