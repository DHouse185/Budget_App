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
        
        self.budget_array = [self.month_col_label, self.month_col_Income_label, self.month_col_Eating_Out_label, 
                        self.month_col_Groceries_label, self.month_col_Transportation_label, 
                        self.month_col_Free_Expense_label, self.month_col_Investment_label, 
                        self.month_col_Bills_label, self.month_col_Support_label, self.month_col_Goal_label, 
                        self.month_col_Sum_Total_label, self.month_col_Profit_Loss_label]
        self.spent_array = [self.spent_col_Income_label, self.spent_col_Eating_Out_label,
                       self.spent_col_Groceries_label, self.spent_col_Transportation_label,
                       self.spent_col_Free_Expense_label, self.spent_col_Investment_label,
                       self.spent_col_Bills_label, self.spent_col_Support_label, self.spent_col_Goal_label,
                       self.spent_col_Sum_Total_label, self.spent_col_Profit_Loss_label]
        self.left_array = [self.left_col_Income_label, self.left_col_Eating_Out_label,
                      self.left_col_Groceries_label, self.left_col_Transportation_label, 
                      self.left_col_Free_Expense_label, self.left_col_Investment_label,
                      self.left_col_Bills_label, self.left_col_Support_label, self.left_col_Goal_label,
                      self.left_col_Sum_Total_label]
        self.progressbar_array = [self.income_progressBar, self.eating_Out_progressBar, 
                             self.groceries_progressBar, self.transportation_progressBar, self.free_Expense_progressBar,
                             self.investment_progressBar, self.bills_progressBar, self.support_progressBar, 
                             self.goal_progressBar, self.sum_Total_progressBar]
        self.columns_array = ["month_year_id", "month_id", "earnings", "food","bills","grocery","transportation","free_expense","investment","support","goal"]
        
        self.month_progress_comboBox.currentTextChanged.connect(self.select_month_year)
        self.Stats_Year_comboBox.currentTextChanged.connect(self.select_month_year)
        try:
            # Fill data for budget section
            cb_month = rvar.month_dict[self.month_progress_comboBox.currentText()]
            print(f"cb_month: {cb_month}")
            self.budget_data = self.database.retrieve_dashboard_month_progress(
                cb_month,
                self.Stats_Year_comboBox.currentText()
                )
            print(self.budget_data)
            for idx, label in enumerate(self.budget_array):
                text = self.budget_data[0][idx]
                if idx == 0:
                    label.setText(f"{str(text)}")
                else: 
                    label.setText(f"${str(text)}")
            
            # Fill data for spent section
            self.category_array = ["Earnings", "Food", "Bills", "Grocery", "Transportation","Free Expense", "Investment", "Support", "Goal"]
            spent_sum = 0
            for idx, label in enumerate(self.spent_array):
                if idx <= 7:
                    self.spent_data = self.database.retrieve_dashboard_spent_progress(
                        self.category_array[idx],
                        cb_month,
                        self.Stats_Year_comboBox.currentText())
                    print(self.spent_data)
                    text = self.spent_data[0][0]
                    label.setText(f"${str(text)}")
                    spent_sum += round(float(text), 2)
                    if idx == 0:
                        earnings = round(float(text), 2)
                        spent_sum -= round(float(text), 2)
                    
                elif idx == 8:
                    label.setText(f"$0.00")
                    spent_sum += 0
                    
                elif idx == 9:
                    label.setText(f"${str(spent_sum)}")
                    
                elif idx == 10:
                    pr_loss = round(earnings - spent_sum, 2)
                    label.setText(f"${str(pr_loss)}")
                    
            # Fill data for left section
            for idx, label in enumerate(self.left_array):
                budget_amount = round(float(self.budget_array[idx + 1].text().split('$')[1]), 2)
                spent_amount = round(float(self.spent_array[idx].text().split('$')[1]), 2)
                left_amount = round(budget_amount - spent_amount, 2)
                label.setText(f"${str(left_amount)}")
                
            # Configure progress bar
            for idx, progress in enumerate(self.progressbar_array):
                budget_amount = round(float(self.budget_array[idx + 1].text().split('$')[1]), 2)
                spent_amount = round(float(self.spent_array[idx].text().split('$')[1]), 2)
                progress_calc = int((spent_amount / budget_amount) * 100)
                if progress_calc > 100:
                    progress_calc = 100
                progress.setValue(progress_calc)
                
        except IndexError:
            print("No data for this timeframe: list index out of range")
            
    def select_month_year(self):
        """
        When another year or month is selected
        """
        try:
            # Fill data for budget section
            cb_month = rvar.month_dict[self.month_progress_comboBox.currentText()]
            print(f"cb_month: {cb_month}")
            self.budget_data = self.database.retrieve_dashboard_month_progress(
                cb_month,
                self.Stats_Year_comboBox.currentText()
                )
            print(self.budget_data)
            for idx, label in enumerate(self.budget_array):
                text = self.budget_data[0][idx]
                if idx == 0:
                    label.setText(f"{str(text)}")
                else: 
                    label.setText(f"${str(text)}")
            
            # Fill data for spent section
            self.category_array = ["Earnings", "Food", "Bills", "Grocery", "Transportation","Free Expense", "Investment", "Support", "Goal"]
            spent_sum = 0
            for idx, label in enumerate(self.spent_array):
                if idx <= 7:
                    self.spent_data = self.database.retrieve_dashboard_spent_progress(
                        self.category_array[idx],
                        cb_month,
                        self.Stats_Year_comboBox.currentText())
                    print(self.spent_data)
                    text = self.spent_data[0][0]
                    label.setText(f"${str(text)}")
                    spent_sum += round(float(text), 2)
                    if idx == 0:
                        earnings = round(float(text), 2)
                        spent_sum -= round(float(text), 2)
                    
                elif idx == 8:
                    label.setText(f"$0.00")
                    spent_sum += 0
                    
                elif idx == 9:
                    label.setText(f"${str(spent_sum)}")
                    
                elif idx == 10:
                    pr_loss = round(earnings - spent_sum, 2)
                    label.setText(f"${str(pr_loss)}")
                    
            # Fill data for left section
            for idx, label in enumerate(self.left_array):
                budget_amount = round(float(self.budget_array[idx + 1].text().split('$')[1]), 2)
                spent_amount = round(float(self.spent_array[idx].text().split('$')[1]), 2)
                left_amount = round(budget_amount - spent_amount, 2)
                label.setText(f"${str(left_amount)}")
                
            # Configure progress bar
            for idx, progress in enumerate(self.progressbar_array):
                budget_amount = round(float(self.budget_array[idx + 1].text().split('$')[1]), 2)
                spent_amount = round(float(self.spent_array[idx].text().split('$')[1]), 2)
                progress_calc = int((spent_amount / budget_amount) * 100)
                if progress_calc > 100:
                    progress_calc = 100
                progress.setValue(progress_calc)
        
        except IndexError:
            print("No data for this timeframe: list index out of range")
            
    def update_data(self):
        ... 