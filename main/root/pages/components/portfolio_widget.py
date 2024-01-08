##########  Python IMPORTs  ############################################################
import datetime
import pandas as pd
from decimal import Decimal
import typing
import pprint
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QLabel, QScrollArea, QComboBox
from PyQt6.QtCore import Qt, QRect, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.models import Account
from root.database import Database
########################################################################################
pp = pprint.PrettyPrinter(indent=2)  # Create a PrettyPrinter object with an indentation of 4 spaces

class Portfolio_Widget(QWidget):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__(parent=parent)

        self.setGeometry(QRect(0, 0, 1910, 810))
        self.setObjectName("portfolio_widget")

        # Scroll Area
        self.portfolio_scrollArea = QScrollArea(parent=self)
        self.portfolio_scrollArea.setGeometry(QRect(0, 0, 1900, 810))
        self.portfolio_scrollArea.setMinimumSize(QSize(0, 0))
        self.portfolio_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.portfolio_scrollArea.setWidgetResizable(True)
        self.portfolio_scrollArea.setObjectName("portfolio_scrollArea")
        # Scroll area content
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 2750, 810))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(2750, 810))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 167715))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # Set up Database
        self.database = database
        # Year combobox
        self.stats_Year_comboBox = QComboBox(parent=self.scrollAreaWidgetContents)
        self.stats_Year_comboBox.setGeometry(QRect(10, 30, 240, 30))
        self.stats_Year_comboBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.stats_Year_comboBox.setStyleSheet("font: 14pt \"Nirmala UI\";")
        self.stats_Year_comboBox.setObjectName("stats_Year_comboBox")
        # Default years
        self.default_years_list = ["2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015"] # Place somewhere in Databse?
        self.stats_Year_comboBox.addItems(self.default_years_list)
        self.stats_Year_comboBox.setCurrentIndex(0)
        # Get year
        self.widget_parameters = [
            {"code_name": "month", "widget": QLabel, "data_type": str, "height": 45, "width": 185, "x_space": 190, "y_space": 50},
            {"code_name": "value", "widget": QLabel, "data_type": str, "height": 45, "width": 185, "x_space": 190, "y_space": 50},
            {"code_name": "account", "widget": QLabel, "data_type": str, "height": 30, "width": 240, "x": 10, "y_space": 50}
            ]
        # Months Labels - List
        self.months_ls = ["Start", "January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November", "December"]
        
        # Dynamically create month labels and their location
        self.months_labels = [QLabel(parent=self.scrollAreaWidgetContents) for _ in range(len(self.months_ls))]
        month_label_x_start = 270
        for idx, label in enumerate(self.months_labels):
            label.setText(self.months_ls[idx])
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            for param in self.widget_parameters:
                if param["code_name"] == "month":
                    label.setGeometry(QRect(month_label_x_start, 30, param["width"], param["height"]))
                    month_label_x_start += param["x_space"]
        self.initialize_signal = 0
        self.update_component()
        self.portfolio_scrollArea.setWidget(self.scrollAreaWidgetContents)
    
    def remove_accountName_labels(self):
        # Use account dictionary to create labels and their locations dynamically
        for account in self.account_dict.values():
            if account.get('account_label') is not None:
                account["account_label"]["name"].setParent(None)
                del account["account_label"]["name"]
        
    def update_component(self):
        # Get account list
        self.year = self.stats_Year_comboBox.currentText()
        account_ls: typing.List[Account] = self.database.app_data['account']['start_data']
        if self.initialize_signal:
            self.remove_accountName_labels() 
        self.account_dict = dict()
        for account in account_ls:
            self.account_dict[account.account] = dict()
            self.account_dict[account.account]["query_name"] = account.account
            self.account_dict[account.account]["name"] = account.account.replace("_", " ")
            self.account_dict[account.account]["account_id"] = account.id
            self.account_dict[account.account]["year"] = dict()

        # Add total list to it
        self.account_dict["Total"] = dict()
        self.account_dict["Total"]["name"] = "Total"
        self.account_dict["Total"]["query_name"] = "Total"
        self.account_dict["Total"]["account_id"] = "total"
        self.account_dict["Total"]["year"] = dict()

        # Create dictionary with year dictionary for each account
        for account in self.account_dict.values():
            for year in self.default_years_list:
                account["year"][year] = dict()
                account["year"][year]["year"] = int(year)
                account["year"][year]["data"] = list()
                account["year"][year]["percent_change"] = list()
                account["year"][year]["fill_in_data"] = list()
                account["year"][year]["fill_in_per_change"] = list()
                account["year"][year]["expected_data"] = list()
                account["year"][year]["average_change"] = 0
                account["year"][year]["sum"] = 0

        # Use year to get account data
        self.add_data()
        self.percent_change()
        # Update self.scrollAreaWidgetContents minimum height if needed
        account_num = len(self.account_dict)
        if account_num > 14:
            self.scrollAreaWidgetContents.setMinimumSize(QSize(2750, int(account_num * 57.86)))
        # Add account label widgets and data labels to scrollAreaWidgetContents
        self.add_account_name_widgets()
        self.add_account_data_label()
        self.initialize_signal = 1
           
    def add_data(self):
        # Use year to get account data
        # Add data to account dictionary list
        # Don't forget to update total list

        for year in self.default_years_list:
            year = int(year)
            for month in range(len(self.months_ls)):
                if year == datetime.datetime.now().year and month > datetime.datetime.now().month: # break when it's current year and month
                    break
                sum_total = 0

                for account in self.account_dict.values():
                    if account["name"] == "Total":
                        account["year"][str(year)]["data"].append((month, sum_total))
                    else:
                        amount = self.get_account_amount(year, month, account)
                        sum_total = self.update_account_data(account, year, month, amount, sum_total)                      

    def get_account_amount(self, year, month, account):
        return next(
            (mon_amount.amount for mon_amount in self.database.app_data['account_management']['start_data']
            if mon_amount.month_id == month and mon_amount.account_id == account["account_id"] 
            and mon_amount.year == account["year"][str(year)]["year"]),
            None
        )

    def update_account_data(self, account, year, month, amount, sum_total):
        if amount is not None:
            account["year"][str(year)]["data"].append((month, amount))
            sum_total += Decimal(amount)
        else:
            # If data is not found for the requested month
            sum_total = self.fill_in_data(account, year, month, sum_total)
        return sum_total

    def fill_in_data(self, account, year, month, sum_total):
        # If the "not found" data is not the beginning of January
        if (month - 1) >= 0:
            sum_total = self.fill_in_from_previous_month(account, year, month, sum_total)
        else:
            # If the "not found" data is the beginning of January
            sum_total = self.fill_in_from_previous_year(account, year, month, sum_total)
        return sum_total

    def fill_in_from_previous_month(self, account, year, month, sum_total):
        for data_point in account["year"][str(year)]["data"]:
            # If there is data already filled into the "data" list for the previous month
            if data_point[0] == (month - 1):
                # We make sure we are getting the right previous month
                amount = data_point[1]
                account["year"][str(year)]["fill_in_data"].append((month, amount))
                sum_total += Decimal(amount)
                break
        # If there is no data filled into the "data" list for the previous month
        else:
            # We check if previous month data is available in "filled_in_data" list
            for data_point in account["year"][str(year)]["fill_in_data"]:
                # We make sure we are getting the right previous month from "filled_in_data
                if data_point[0] == (month - 1):
                    amount = data_point[1]
                    account["year"][str(year)]["fill_in_data"].append((month, amount))
                    sum_total += Decimal(amount)
                    break
            # If no data is found in "filled_in_data" list either, we just fill it in with 0
            else:
                account["year"][str(year)]["fill_in_data"].append((month, 0))
        return sum_total

    def fill_in_from_previous_year(self, account, year, month, sum_total):
        amount = next(
            (mon_amount.amount for mon_amount in self.database.app_data['account_management']['start_data']
            if mon_amount.month_id == 12 and mon_amount.account_id == account["account_id"] 
            and mon_amount.year == (account["year"][str(year)]["year"] - 1)),
            None
        )
        # If data was found in the previous year's December end
        if amount is not None:
            account["year"][str(year)]["fill_in_data"].append((month, amount))
            sum_total += Decimal(amount)
        # If data was not found in the previous year's December end
        else:
            # Check previous year's December end Fill in data
            account["year"][str(year)]["fill_in_data"].append((month, 0))
        return sum_total
    
    def percent_change(self):
        for account in self.account_dict.values():
            for year in account["year"].values():
                data_only_list = year["data"]
                fill_in_only_list = year["fill_in_data"]
                percent_ls = []
                fill_in_perc_ls = []
                chronological_list = sorted(data_only_list + fill_in_only_list, key=lambda x: x[0])
                year["sum"] = chronological_list[-1][1]

                for month in range(1, len(self.months_ls)):
                    if year["year"] == datetime.datetime.now().year and month > datetime.datetime.now().month:
                        try:
                            average = sum(item[1] for item in percent_ls) / len(percent_ls)
                        except ZeroDivisionError:
                            average = 0

                        last_month = chronological_list[-1][0]
                        prev_value = chronological_list[-1][1] if last_month == (month - 1) else year["expected_data"][-1][1]

                        year["expected_data"].append((month, prev_value * (1 + average)))
                    else:
                        result_1 = next((item[1] for item in data_only_list if item[0] == month), None)
                        result_2 = next((item[1] for item in data_only_list if item[0] == (month - 1)), None)

                        if result_1 is None:
                            result_1 = next((item[1] for item in fill_in_only_list if item[0] == month), None)

                            if result_2 is None:
                                result_2 = next((item[1] for item in fill_in_only_list if item[0] == (month - 1)), None)

                                try:
                                    percent_change = (result_1 - result_2) / abs(result_2) * 100 if (result_2 != 0) and (result_2 is not None) else Decimal(0.00) # CHECK AGAIN DURING DEBUGGING
                                except ZeroDivisionError:
                                    percent_change = (result_1 - result_2) / (abs(result_2) + 1) * 100

                                fill_in_perc_ls.append((month, percent_change))
                            else:
                                try:
                                    percent_change = (result_1 - result_2) / abs(result_2) * 100 if (result_2 is not None) and (result_2 != 0) and (result_1 is not None) else Decimal(0.00)
                                    percent_ls.append((month, Decimal(percent_change)))
                                
                                except ZeroDivisionError:
                                    percent_ls.append((month, Decimal(0.00)))
                        else:
                            try:    
                                percent_change = (float(result_1) - float(result_2)) / abs(float(result_2)) * 100 if (result_2 is not None) and (result_2 != 0) and (result_1 is not None) else Decimal(0.00)
                                percent_ls.append((month, round(Decimal(percent_change), 2)))
                            
                            except ZeroDivisionError:
                                percent_ls.append((month, Decimal(0.00)))

                year["percent_change"] = percent_ls
                year["fill_in_per_change"] = fill_in_perc_ls
                year["unfiltered_data"] = chronological_list

                try:
                    year["average_change"] = round(sum(item[1] for item in percent_ls) / len(percent_ls), 2)
                except ZeroDivisionError:
                    year["average_change"] = 0

    def add_account_name_widgets(self):
        account_label_x_start = 10
        account_label_y_start = 80

        # Use account dictionary to create labels and their locations dynamically
        for account in self.account_dict.values():
            account["account_label"] = dict()
            account["account_label"]["name"] = QLabel(parent=self.scrollAreaWidgetContents)
            account["account_label"]["name"].setText(f'{account["name"]} :')
            account["account_label"]["name"].setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

            for param in self.widget_parameters:
                if param["code_name"] == "account":
                    account["account_label"]["name"].setGeometry(QRect(account_label_x_start, account_label_y_start, param["width"], param["height"]))
                    account["account_label"]["name"].setVisible(True)
                    account_label_y_start += param["y_space"]

    def add_account_data_label(self):
        value_label_x_start = 270
        value_label_y_start = 80

        # Use account dictionary to create labels and their locations dynamically
        for account in self.account_dict.values():
            # Loop through each account
            for year in account["year"].values():
                # loop through each year dictionary in each account dictionary
                if year.get('data_label') is not None:
                    for label in year["data_label"]:
                        label.setParent(None)
                        del label
                year["data_label"] = [QLabel() for _ in range(len(year["unfiltered_data"]))]
                
                unfiltered_data = year["unfiltered_data"]
                norm_data = year["data"]
                fill_data = year["fill_in_data"]
                
                for un_data in unfiltered_data:
                    # Loop through all of the data that has been sorted chronologically
                    month = un_data[0] # get the month of the data point
                    text, fill = next(((item[1], False) for item in norm_data if item[0] == month), next(((item[1], True) for item in fill_data if item[0] == month), (Decimal(0.00), True)))
                    year["data_label"][month].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    if fill: # input data not available for month
                        year["data_label"][month].setStyleSheet("font-weight: bold;") # Visually indicate that data is made up
                    year["data_label"][month].setText(f"${text}")
                        
                    if str(year["year"]) == self.year: # make it visible 
                        year["data_label"][month].setParent(self.scrollAreaWidgetContents)
                        
                    for param in self.widget_parameters:
                        if param["code_name"] == "value":
                            year["data_label"][month].setGeometry(QRect(value_label_x_start, value_label_y_start, param["width"], param["height"]))
                            value_label_x_start += param["x_space"]
                
                value_label_x_start = 270
            
            for v_param in self.widget_parameters:
                if v_param["code_name"] == "value":
                    value_label_y_start += v_param["y_space"]
                    
    def year_change(self, prev_year, new_year):
        self.remove_prev_year_labels(prev_year=prev_year)
        for account in self.account_dict.values():
            account_year = account["year"][f'{new_year}']
            for data_label in account_year['data_label']:
                data_label.setParent(self.scrollAreaWidgetContents)
                data_label.setVisible(True)  # Show labels for the newly selected year
        
    def remove_prev_year_labels(self, prev_year):
        for account in self.account_dict.values():
            account_year = account["year"][f'{prev_year}']
            for data_label in account_year['data_label']:
                data_label.setParent(None)
                data_label.setVisible(False)  # Hide labels for the previous year
                        