##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import calendar
import pandas as pd
import decimal
import typing
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
from root.pages.components.ui.calendar_stats_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Calendar_Stats(Ui_Form):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.stats = QWidget(parent=parent)
        self.setupUi(self.stats)
        self.stats.setGeometry(QRect(0, 0, 390, 1650))
        
        self.database = database
        self.transaction_df = self.database.start_up_transaction_data
        self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        self.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        
        self.year = self.stats_Year_comboBox.currentText()
        self.month = self.stats_Month_comboBox.currentText()
        self.month_int = rvar.month_dict[self.month]
        months_range = calendar.monthrange(int(self.year), (self.month_int))
        self.month_range = months_range[1]
            
        self.amount_Max_Days_Months_label.setText(f"{self.month_range}")
        
        today_day = datetime.datetime.now()
        # Get first day of the month
        date_1 = datetime.datetime(year=int(self.year), month=(self.month_int), day=1)
        # first_date = f"{date_1.strftime('%Y-%m-%d')}"
        if today_day <= date_1:
            self.amount_Days_Passed_Months_label.setText("0")
            self.days_passed = 0
            
        elif today_day.month == date_1.month and today_day.year == date_1.year:
            self.amount_Days_Passed_Months_label.setText(f"{today_day.day}")
            self.days_passed = today_day.day
            
        elif today_day > date_1:
            self.amount_Days_Passed_Months_label.setText(f"{self.month_range}")
            self.days_passed = self.month_range
        
        self.month_starting_budg = self.database.starting_budget_month(self.year, self.month_int)
        self.amount_Starting_Budget_Months_label.setText(f"${self.month_starting_budg[0][0]}")
        self.budget_for_month = self.database.month_budget(self.year, self.month_int)
        self.amount_Budget_For_Month_label.setText(f"${self.budget_for_month[0][0]}")
        self.planned_savings = self.database.savings_for_month(self.year, self.month_int)
        self.amount_Planned_Savings_Months_label.setText(f"${self.planned_savings[0][0]}")
        self.earnings_for_month = self.database.earnings_for_month(self.year, self.month_int)
        
        try:
            self.daily_exp_goal = round((self.budget_for_month[0][0] / self.month_range), 2)
            self.amount_Daily_Expense_Goal_label.setText(f"${self.daily_exp_goal}")

        except ZeroDivisionError:
            self.amount_Daily_Expense_Goal_label.setText(f"$0.00")
            
        self.weekly_exp_goal = self.daily_exp_goal * 7
        self.amount_Weekly_Expense_Goal_label.setText(f"${self.weekly_exp_goal}")
        
    def init_2(self, credit_list: typing.List, debit_list: typing.List):
        self.stats_credit_list = credit_list
        self.stats_debit_list = debit_list
        self.total_spent = sum(self.stats_debit_list)        
        self.amount_Total_Spent_Months_label.setText(f"${self.total_spent}")
        self.left_in_budget_month = round(self.budget_for_month[0][0] - self.total_spent, 2)
        self.amount_Left_in_Budget_Months_label.setText(f"${self.left_in_budget_month}")
        
        # Weeks earnings
        self.amount_Week_1_Earning_label.setText(f"${round(sum(self.stats_credit_list[0:7]), 2)}") 
        self.amount_Week_2_Earnings_label.setText(f"${round(sum(self.stats_credit_list[7:14]), 2)}") 
        self.amount_Week_3_Earning_label.setText(f"${round(sum(self.stats_credit_list[14:21]), 2)}") 
        self.amount_Week_4_Earning_label.setText(f"${round(sum(self.stats_credit_list[21:28]), 2)}") 
        self.amount_Week_5_Earning_label.setText(f"${round(sum(self.stats_credit_list[28:35]), 2)}") 
        self.amount_Week_6_Earning_label.setText(f"${round(sum(self.stats_credit_list[35:]), 2)}") 
        self.monthly_earnings = round(sum(self.stats_credit_list), 2)
        self.amount_Yearly_Earnings_label.setText(f"${self.monthly_earnings}")

        self.current_expense_balance = self.month_starting_budg[0][0] + self.monthly_earnings - self.total_spent
        self.amount_Current_Expense_Balance_Months_label.setText(f"${self.current_expense_balance}")
        
        self.profit_loss = self.current_expense_balance - self.month_starting_budg[0][0]
        self.amount_Current_ProfitLoss_Months_label.setText(f"${self.profit_loss}")
        
        self.balance_left_in_budg = self.current_expense_balance - int(self.budget_for_month[0][0])
        self.amount_Balance_Left_in_Budget_Months_label.setText(f"${self.balance_left_in_budg}")
        
        self.balance_left_in_budg_salary = self.balance_left_in_budg + self.earnings_for_month[0][0] - self.monthly_earnings
        self.amount_Balance_Left_in_Budget_Salary_Months_label.setText(f"${self.balance_left_in_budg_salary}")
        
        try:    
            self.daily_avg_exp = round((self.total_spent / self.days_passed), 2)
            self.amount_Daily_Average_Expense_label.setText(f"${self.daily_avg_exp}")
        
        except ZeroDivisionError:
            self.amount_Daily_Average_Expense_label.setText(f"$0.00")
            
        self.current_savings = round((self.daily_exp_goal - self.daily_avg_exp), 2)
        self.amount_Current_Savings_Daily_label.setText(f"${self.current_savings}")
        
        try:
            self.new_daily_expense = round((((self.daily_exp_goal * self.month_range) / (self.month_range - self.days_passed)) - (((self.daily_avg_exp * self.month_range)) / (self.month_range - self.days_passed))), 2)
            self.amount_New_Daily_Expense_Planned_label.setText(f"${self.new_daily_expense}")
            
        except ZeroDivisionError:
            self.amount_New_Daily_Expense_Planned_label.setText("$0.00")
        
        weekly_avg_exp = self.daily_avg_exp * 7
        predicted_yearly_expense = self.daily_avg_exp * self.month_range
        predicted_savings = self.current_savings * self.month_range
        
        self.amount_Weekly_Average_Expense_label.setText(f"${weekly_avg_exp}")
        self.amount_Predicted_Monthly_Expense_label.setText(f"${predicted_yearly_expense}")
        self.amount_Predicted_Total_Savings_label.setText(f"${predicted_savings}")
    
    def month_change_1(self):
                
        self.month = self.stats_Month_comboBox.currentText()
        self.month_int = rvar.month_dict[self.month]
        months_range = calendar.monthrange(int(self.year), (self.month_int))
        self.month_range = months_range[1]
            
        self.amount_Max_Days_Months_label.setText(f"{self.month_range}")
        
        today_day = datetime.datetime.now()
        # Get first day of the month
        date_1 = datetime.datetime(year=int(self.year), month=(self.month_int), day=1)
        # first_date = f"{date_1.strftime('%Y-%m-%d')}"
        if today_day <= date_1:
            self.amount_Days_Passed_Months_label.setText("0")
            self.days_passed = 0
            
        elif today_day.month == date_1.month and today_day.year == date_1.year:
            self.amount_Days_Passed_Months_label.setText(f"{today_day.day}")
            self.days_passed = today_day.day
            
        elif today_day > date_1:
            self.amount_Days_Passed_Months_label.setText(f"{self.month_range}")
            self.days_passed = self.month_range
        
        self.month_starting_budg = self.database.starting_budget_month(self.year, self.month_int)
        self.amount_Starting_Budget_Months_label.setText(f"${self.month_starting_budg[0][0]}")
        self.budget_for_month = self.database.month_budget(self.year, self.month_int)
        self.amount_Budget_For_Month_label.setText(f"${self.budget_for_month[0][0]}")
        self.planned_savings = self.database.savings_for_month(self.year, self.month_int)
        self.amount_Planned_Savings_Months_label.setText(f"${self.planned_savings[0][0]}")
        self.earnings_for_month = self.database.earnings_for_month(self.year, self.month_int)
        
        try:
            self.daily_exp_goal = round((self.budget_for_month[0][0] / self.month_range), 2)
            self.amount_Daily_Expense_Goal_label.setText(f"${self.daily_exp_goal}")

        except ZeroDivisionError:
            self.amount_Daily_Expense_Goal_label.setText(f"$0.00")
            
        self.weekly_exp_goal = self.daily_exp_goal * 7
        self.amount_Weekly_Expense_Goal_label.setText(f"${self.weekly_exp_goal}")
    
    def month_change_2(self, credit_list: typing.List, debit_list: typing.List):
        self.stats_credit_list = credit_list
        self.stats_debit_list = debit_list
        self.total_spent = sum(self.stats_debit_list)        
        self.amount_Total_Spent_Months_label.setText(f"${self.total_spent}")
        self.left_in_budget_month = round(self.budget_for_month[0][0] - self.total_spent, 2)
        self.amount_Left_in_Budget_Months_label.setText(f"${self.left_in_budget_month}")
        
        # Weeks earnings
        self.amount_Week_1_Earning_label.setText(f"${round(sum(self.stats_credit_list[0:7]), 2)}") 
        self.amount_Week_2_Earnings_label.setText(f"${round(sum(self.stats_credit_list[7:14]), 2)}") 
        self.amount_Week_3_Earning_label.setText(f"${round(sum(self.stats_credit_list[14:21]), 2)}") 
        self.amount_Week_4_Earning_label.setText(f"${round(sum(self.stats_credit_list[21:28]), 2)}") 
        self.amount_Week_5_Earning_label.setText(f"${round(sum(self.stats_credit_list[28:35]), 2)}") 
        self.amount_Week_6_Earning_label.setText(f"${round(sum(self.stats_credit_list[35:]), 2)}") 
        self.monthly_earnings = round(sum(self.stats_credit_list), 2)
        self.amount_Yearly_Earnings_label.setText(f"${self.monthly_earnings}")

        self.current_expense_balance = self.month_starting_budg[0][0] + self.monthly_earnings - self.total_spent
        self.amount_Current_Expense_Balance_Months_label.setText(f"${self.current_expense_balance}")
        
        self.profit_loss = self.current_expense_balance - self.month_starting_budg[0][0]
        self.amount_Current_ProfitLoss_Months_label.setText(f"${self.profit_loss}")
        
        self.balance_left_in_budg = self.current_expense_balance - int(self.budget_for_month[0][0])
        self.amount_Balance_Left_in_Budget_Months_label.setText(f"${self.balance_left_in_budg}")
        
        self.balance_left_in_budg_salary = self.balance_left_in_budg + self.earnings_for_month[0][0] - self.monthly_earnings
        self.amount_Balance_Left_in_Budget_Salary_Months_label.setText(f"${self.balance_left_in_budg_salary}")
        
        try:    
            self.daily_avg_exp = round((self.total_spent / self.days_passed), 2)
            self.amount_Daily_Average_Expense_label.setText(f"${self.daily_avg_exp}")
        
        except ZeroDivisionError:
            self.amount_Daily_Average_Expense_label.setText(f"$0.00")
        
        # print(f"self.daily_exp_goal : {self.daily_exp_goal.__class__}")
        # print(f"self.daily_avg_exp : {self.daily_avg_exp.__class__}")
        # print(f"self.total_spent : {self.total_spent.__class__}")
        # print(f"self.stats_debit_list : \n{self.stats_debit_list}")
            
        self.current_savings = round((self.daily_exp_goal - decimal.Decimal(self.daily_avg_exp)), 2)
        self.amount_Current_Savings_Daily_label.setText(f"${self.current_savings}")
        
        try:
            if decimal.Decimal(self.month_range - self.days_passed) == 0:
                ZeroDivisionError
            else:
                self.new_daily_expense = round((((decimal.Decimal(self.daily_exp_goal) * decimal.Decimal(self.month_range)) / (decimal.Decimal(self.month_range - self.days_passed))) - (((decimal.Decimal(self.daily_avg_exp * self.month_range))) / (decimal.Decimal(self.month_range - self.days_passed)))), 2)
                self.amount_New_Daily_Expense_Planned_label.setText(f"${self.new_daily_expense}")
            
        except ZeroDivisionError:
            self.amount_New_Daily_Expense_Planned_label.setText("$0.00")
        
        weekly_avg_exp = self.daily_avg_exp * 7
        predicted_yearly_expense = self.daily_avg_exp * self.month_range
        predicted_savings = self.current_savings * self.month_range
        
        self.amount_Weekly_Average_Expense_label.setText(f"${weekly_avg_exp}")
        self.amount_Predicted_Monthly_Expense_label.setText(f"${predicted_yearly_expense}")
        self.amount_Predicted_Total_Savings_label.setText(f"${predicted_savings}")