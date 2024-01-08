##########  Python IMPORTs  ############################################################
from typing import Optional
from decimal import Decimal
import datetime
import calendar
import pandas as pd
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRect
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
        self.update_data()
        self.stats_Year_comboBox.currentIndexChanged.connect(self.update_data)

    def update_data(self):
        self.year = int(self.stats_Year_comboBox.currentText())
        
        if self.year % 4 == 0:
            self.year_range = 366
        else:
            self.year_range = 365
            
        self.amount_Max_Days_label.setText(f"{self.year_range}")
        today_day = datetime.datetime.now()
        if today_day.year == self.year:
            self.days_passed = (today_day.timetuple()).tm_yday
        elif today_day.year > self.year:
            self.days_passed = self.year_range
        elif today_day.year < self.year:
            self.days_passed = 0
        self.amount_Days_Passed_label.setText(f"{self.days_passed}")
        
        self.transaction_df: pd.DataFrame = self.database.app_data['transaction_dataframe']
        self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        self.transaction_df_no_date_idx['Date'] = pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        
        self.year_starting_budg: Optional[Decimal] = next(
            (
                start_budg.starting_budget for start_budg in self.database.app_data["month_budget"]["start_data"] 
                if start_budg.month == 1 and start_budg.year == self.year
                ),
            Decimal(0.00)
            )
        self.amount_Starting_Budget_label.setText(f"${self.year_starting_budg}")
        self.budget_for_year: Decimal = sum(
            [
                year_budg.total for year_budg in self.database.app_data["month_budget"]["start_data"] 
                if year_budg.year == self.year
                ]
            )
        self.amount_Budget_For_Year_label.setText(f"${self.budget_for_year}")
        self.year_df = self.transaction_df_no_date_idx[self.transaction_df_no_date_idx['Date'].apply(lambda x: x.year == self.year)]
        self.total_spent = self.year_df.loc[self.year_df['Transaction Type'] == 'Expense', 'Amount'].sum() if (not self.year_df.columns.empty) and (not self.year_df.empty) else Decimal(0) # I believe this is used somewhere else in the code. Perhaps move to App_Database
        self.amount_Total_Spent_label.setText(f"${self.total_spent}")
        self.planned_savings: Decimal = sum(
            [
                plan_sav.left_amount for plan_sav in self.database.app_data["month_budget"]["start_data"] 
                if plan_sav.year == self.year
                ]
            )
        self.amount_Planned_Savings_label.setText(f"${self.planned_savings}")
        self.left_in_budget_year = self.budget_for_year-self.total_spent
        self.amount_Left_in_Budget_label.setText(f"${self.left_in_budget_year}")
        
        # Set Earnings for months
        self.yearly_earnings = 0
        for idx, label in enumerate(self.month_earning_label_list):
            # Get first day of the month
            first_date = (datetime.datetime(year=self.year, month=(idx + 1), day=1)).strftime('%Y-%m-%d')
            
            # Get last day of the month
            days_in_month = (calendar.monthrange(self.year, (idx + 1)))[1]
            last_date = (datetime.datetime(year=self.year, month=(idx + 1), day=int(days_in_month))).strftime('%Y-%m-%d')
            
            # Get earnings
            earnings = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] >= first_date) & (self.transaction_df_no_date_idx['Date'] <= last_date)
                                               & (self.transaction_df_no_date_idx['Transaction Type'] == 'Income'), 'Amount'].sum() 
            label.setText(f"${earnings}")
            
            self.yearly_earnings += earnings # Probably used this somewhere in the code too. Add to App Data later
        
        self.amount_Yearly_Earnings_label.setText(f"${self.yearly_earnings}")
        
        current_expense_balance = self.year_starting_budg + self.yearly_earnings - self.total_spent
        self.amount_Current_Expense_Balance_label.setText(f"${current_expense_balance}")
        
        profit_loss = current_expense_balance - self.year_starting_budg
        self.amount_Current_ProfitLoss_label.setText(f"{profit_loss}")
        
        balance_left_in_budg = current_expense_balance - self.budget_for_year
        self.amount_Balance_Left_in_Budget_label.setText(f"${balance_left_in_budg}")
        
        earnings_for_year: Decimal = sum(
            [
                year_earn.earnings for year_earn in self.database.app_data["month_budget"]["start_data"] 
                if year_earn.year == self.year
                ]
            )
        balance_left_in_budg_salary = balance_left_in_budg + earnings_for_year - self.yearly_earnings
        
        self.amount_Balance_Left_in_Budget_Salary_label.setText(f"${balance_left_in_budg_salary}")
        
        daily_exp_goal = Decimal(round((self.budget_for_year / self.year_range), 2)) if self.year_range != 0 else Decimal(0.00)
        self.amount_Daily_Expense_Goal_label.setText(f"${daily_exp_goal}")
        
        daily_avg_exp = Decimal(round((self.total_spent / self.days_passed), 2)) if self.days_passed != 0 else Decimal(0.00)
        self.amount_Daily_Average_Expense_label.setText(f"${daily_avg_exp}")
            
        current_savings = round((daily_exp_goal - daily_avg_exp), 2)
        self.amount_Current_Savings_Daily_label.setText(f"${current_savings}")
        
        new_daily_expense = round((((daily_exp_goal * self.year_range) / (self.year_range - self.days_passed)) - (((daily_avg_exp * self.year_range)) \
            / (self.year_range - self.days_passed))), 2) if (self.year_range - self.days_passed) != 0 else Decimal(0.00)
        self.amount_New_Daily_Expense_Planned_label.setText(f"${new_daily_expense}")
        
        weekly_exp_goal = daily_exp_goal * 7
        weekly_avg_exp = daily_avg_exp * 7
        predicted_yearly_expense = daily_avg_exp * self.year_range
        predicted_savings = current_savings * self.year_range
        
        self.amount_Weekly_Expense_Goal_label.setText(f"${weekly_exp_goal}")
        self.amount_Weekly_Average_Expense_label.setText(f"${weekly_avg_exp}")
        self.amount_Predicted_Yearly_Expense_label.setText(f"${predicted_yearly_expense}")
        self.amount_Predicted_Total_Savings_label.setText(f"${predicted_savings}")