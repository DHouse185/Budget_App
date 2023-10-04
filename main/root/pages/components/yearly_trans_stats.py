##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import calendar
import pandas as pd
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
from root.database import Database
from root.pages.components.ui.stats_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Yearly_Stats(Ui_Form):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.stats = QWidget(parent=parent)
        self.setupUi(self.stats)
        self.stats.setGeometry(QRect(0, 0, 390, 1650))
        
        self.database = database
        
        self.year = self.stats_Year_comboBox.currentText()
        
        if int(self.year) % 4 == 0:
            self.year_range = 366
        else:
            self.year_range = 365
            
        self.amount_Max_Days_label.setText(f"{self.year_range}")
        today_day = datetime.datetime.now()
        self.days_passed = today_day.timetuple()
        self.days_passed = self.days_passed.tm_yday
        self.amount_Days_Passed_label.setText(f"{self.days_passed}")
        
        self.transaction_df = self.database.start_up_transaction_data
        self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        self.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        
        print(self.transaction_df)
        
        self.year_starting_budg = self.database.starting_budget(self.year)
        self.amount_Starting_Budget_label.setText(f"${self.year_starting_budg[0][0]}")
        self.budget_for_year = self.database.budget_for_year(self.year)
        self.amount_Budget_For_Year_label.setText(f"${self.budget_for_year[0][0]}")
        self.total_spent = self.transaction_df.loc[self.transaction_df['Transaction Type'] == 'Expense', 'Amount'].sum() 
        self.amount_Total_Spent_label.setText(f"${self.total_spent}")
        self.planned_savings = self.database.savings_for_year(self.year)
        self.amount_Planned_Savings_label.setText(f"${self.planned_savings[0][0]}")
        self.left_in_budget_year = int(self.budget_for_year[0][0])-int(self.total_spent)
        self.amount_Left_in_Budget_label.setText(f"${self.left_in_budget_year}")
        
        # Set Earnings for months
        self.yearly_earnings = 0
        for idx, label in enumerate(self.month_earning_label_list):
            # Get first dy of the month
            date_1 = datetime.datetime(year=int(self.year), month=(idx + 1), day=1)
            first_date = f"{date_1.strftime('%Y-%m-%d')}"
            
            # Get last day of the month
            months_range = calendar.monthrange(int(self.year), (idx + 1))
            days_in_month = months_range[1]
            date_2 = datetime.datetime(year=int(self.year), month=(idx + 1), day=int(days_in_month))
            last_date = f"{date_2.strftime('%Y-%m-%d')}"
            
            # Get earnings
            earnings = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] >= first_date) & (self.transaction_df_no_date_idx['Date'] <= last_date)
                                               & (self.transaction_df_no_date_idx['Transaction Type'] == 'Income'), 'Amount'].sum() 
            label.setText(f"${earnings}")
            
            self.yearly_earnings += int(earnings)
        
        self.amount_Yearly_Earnings_label.setText(f"${self.yearly_earnings}")
        
        current_expense_balance = self.year_starting_budg[0][0] + self.yearly_earnings - self.total_spent
        self.amount_Current_Expense_Balance_label.setText(f"${current_expense_balance}")
        
        profit_loss = current_expense_balance - self.year_starting_budg[0][0]
        self.amount_Current_ProfitLoss_label.setText(f"{profit_loss}")
        
        balance_left_in_budg = current_expense_balance - int(self.budget_for_year[0][0])
        self.amount_Balance_Left_in_Budget_label.setText(f"${balance_left_in_budg}")
        
        earnings_for_year = self.database.earnings_for_year(self.year)
        balance_left_in_budg_salary = balance_left_in_budg + earnings_for_year[0][0] - self.yearly_earnings
        
        self.amount_Balance_Left_in_Budget_Salary_label.setText(f"${balance_left_in_budg_salary}")
        
        try:
            daily_exp_goal = round((self.budget_for_year[0][0] / self.year_range), 2)
            self.amount_Daily_Expense_Goal_label.setText(f"${daily_exp_goal}")

        except ZeroDivisionError:
            self.amount_Daily_Expense_Goal_label.setText(f"$0.00")
        
        try:    
            daily_avg_exp = round((self.total_spent / self.days_passed), 2)
            self.amount_Daily_Average_Expense_label.setText(f"${daily_avg_exp}")
        
        except ZeroDivisionError:
            self.amount_Daily_Average_Expense_label.setText(f"$0.00")
            
        current_savings = round((daily_exp_goal - daily_avg_exp), 2)
        self.amount_Current_Savings_Daily_label.setText(f"${current_savings}")
        
        try:
            new_daily_expense = round((((daily_exp_goal * self.year_range) / (self.year_range - self.days_passed)) - (((daily_avg_exp * self.year_range)) / (self.year_range - self.days_passed))), 2)
            self.amount_New_Daily_Expense_Planned_label.setText(f"${new_daily_expense}")
            
        except ZeroDivisionError:
            self.amount_New_Daily_Expense_Planned_label.setText("$0.00")
        
        weekly_exp_goal = daily_exp_goal * 7
        weekly_avg_exp = daily_avg_exp * 7
        predicted_yearly_expense = daily_avg_exp * self.year_range
        predicted_savings = current_savings * self.year_range
        
        self.amount_Weekly_Expense_Goal_label.setText(f"${weekly_exp_goal}")
        self.amount_Weekly_Average_Expense_label.setText(f"${weekly_avg_exp}")
        self.amount_Predicted_Yearly_Expense_label.setText(f"${predicted_yearly_expense}")
        self.amount_Predicted_Total_Savings_label.setText(f"${predicted_savings}")
        # self.tables_array = ['category_test', 'sub_category_test', 'account_test', 'category_type_test',
        #                      'accounting_type_test', 'month_test']
        # self.create_table_dict()
        