##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import calendar
import pandas as pd
import decimal
import typing
import pprint
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow,
                             QWidget,
                             QMessageBox,
                             QStackedWidget,
                             QWidget,
                             QGridLayout,
                             QLabel,
                             QTableWidgetItem,
                             QScrollArea,
                             QComboBox)
from PyQt6.QtGui import QAction, QDoubleValidator
from PyQt6.QtCore import Qt, QRect, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
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
        default_years_list = ["2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015"]
        self.stats_Year_comboBox.addItems(default_years_list)
        self.stats_Year_comboBox.setCurrentIndex(0)

        # Get year
        self.year = self.stats_Year_comboBox.currentText()

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


        # Get account list
        account_ls = self.database.all_data_request("account_test")

        # For Debugging purposes
        # print(account_ls)

        self.account_dict = dict()

        for account in account_ls:
            self.account_dict[account[1]] = dict()
            self.account_dict[account[1]]["query_name"] = account[1]
            self.account_dict[account[1]]["name"] = account[1].replace("_", " ")
            self.account_dict[account[1]]["account_id"] = account[0]
            self.account_dict[account[1]]["year"] = dict()

        # For Debugging purposes
        # pp.pprint(self.account_dict)

        # Add total list to it
        self.account_dict["Total"] = dict()
        self.account_dict["Total"]["name"] = "Total"
        self.account_dict["Total"]["query_name"] = "Total"
        self.account_dict["Total"]["account_id"] = "total"
        self.account_dict["Total"]["year"] = dict()

        # Create dictionary with year dictionary for each account
        for account in self.account_dict.values():
            print(account)
            account["year"][self.year] = dict()
            account["year"][self.year]["year"] = int(self.year)
            account["year"][self.year]["data"] = list()
            account["year"][self.year]["percent_change"] = list()
            account["year"][self.year]["fill_in_data"] = list()
            account["year"][self.year]["fill_in_per_change"] = list()
            account["year"][self.year]["expected_data"] = list()
            account["year"][self.year]["average_change"] = 0
            account["year"][self.year]["sum"] = 0

            account["year"][str(int(self.year) -1)] = dict()
            account["year"][str(int(self.year) -1)]["year"] = int(self.year) -1
            account["year"][str(int(self.year) -1)]["data"] = list()
            account["year"][str(int(self.year) -1)]["percent_change"] = list()
            account["year"][str(int(self.year) -1)]["fill_in_data"] = list()
            account["year"][str(int(self.year) -1)]["fill_in_per_change"] = list()
            account["year"][str(int(self.year) -1)]["expected_data"] = list()
            account["year"][str(int(self.year) -1)]["average_change"] = 0
            account["year"][str(int(self.year) -1)]["sum"] = 0

        # pp.pprint(self.account_dict)  # Pretty print the data

        # Use year to get account data
        self.add_data()

        # For debugging purposes
        # pp.pprint(self.account_dict)  # Pretty print the data

        self.percent_change()

        # For debugging purposes
        # pp.pprint(self.account_dict)  # Pretty print the data

        # Update self.scrollAreaWidgetContents minimum height if needed
        account_num = len(self.account_dict)
        if account_num > 14:
            self.scrollAreaWidgetContents.setMinimumSize(QSize(2750, int(account_num * 57.86)))

        # Add account label widgets and data labels to scrollAreaWidgetContents
        self.add_account_name_widgets()
        self.add_account_data_label()


        # For debugging purposes
        # pp.pprint(self.account_dict)  # Pretty print the data

        self.portfolio_scrollArea.setWidget(self.scrollAreaWidgetContents)


    def add_data(self):
        # Use year to get account data
        # Add data to account dictionary list
        # Don't forget to update total list
        # Will Turn into function

        for year in range((int(self.year) - 1), (int(self.year) + 1), 1):

            for month in range(len(self.months_ls)):

                if year == datetime.datetime.now().year and month > datetime.datetime.now().month:
                    break
                sum_total = 0

                for account in self.account_dict.values():

                    if account["name"] == "Total":
                        account["year"][str(year)]["data"].append((month, sum_total))

                    else:
                        amount = self.database.portfolio_month_amount(account["year"][str(year)]["year"],
                                                            month,
                                                            account["account_id"])

                        # If data is found for the requested month
                        if amount != []:
                            amount = amount[0][0]
                            account["year"][str(year)]["data"].append((month, amount))
                            sum_total += amount

                        # If data is not found for the requested month
                        else:
                            # If the "not found" data is not the beginning of January
                            if (month - 1) >= 0:
                                # If there is data already filled into the "data" list for the previous month
                                for data_point in account["year"][str(year)]["data"]:
                                    # We make sure we are getting the right previous month
                                    if data_point[0] == (month - 1):
                                        amount = data_point[1]
                                        account["year"][str(year)]["fill_in_data"].append((month, amount))
                                        sum_total += amount

                                # If there is no data filled into the "data" list for the previous month
                                if amount == []:
                                    # We check if previous month data is available in "filled_in_data" list
                                    for data_point in account["year"][str(year)]["fill_in_data"]:
                                        # We make sure we are getting the right previous month from "filled_in_data"
                                        if data_point[0] == (month - 1):
                                            amount = data_point[1]
                                            account["year"][str(year)]["fill_in_data"].append((month, amount))
                                            sum_total += amount

                                    # If no data is found in "filled_in_data" list either, we just fill it in with 0
                                    if amount == []:
                                        account["year"][str(year)]["fill_in_data"].append((month, 0))

                            # If the "not found" data is the beginning of January
                            else:
                                amount = self.database.portfolio_month_amount(account["year"][str(year)]["year"] - 1,
                                                            12,
                                                            account["account_id"])

                                # If data was found in the previous year's December end
                                if amount != []:
                                    amount = amount[0][0]
                                    account["year"][str(year)]["fill_in_data"].append((month, amount))
                                    sum_total += amount

                                # If data was not found in the previous year's December end
                                else:
                                    # Check previous year's December end Fill in data
                                    account["year"][str(year)]["fill_in_data"].append((month, 0))

        # print(len(self.account_dict))

    def percent_change(self):

        for account in self.account_dict.values():
            for year in account["year"].values():
                data_only_list = year["data"]
                fill_in_only_list = year["fill_in_data"]
                percent_ls = list()
                fill_in_perc_ls = list()
                chronological_list = data_only_list + fill_in_only_list
                chronological_list = sorted(chronological_list, key=lambda x: x[0])
                year["sum"] = chronological_list[-1][1]

                for month in range(len(self.months_ls)):
                    if month == 0:
                        pass
                    elif year["year"] == datetime.datetime.now().year and month > datetime.datetime.now().month:
                        try:
                            average = sum(item[1] for item in percent_ls) / len(percent_ls)

                        except ZeroDivisionError:
                            average = 0

                        if chronological_list[-1][0] == (month -1):
                            print(chronological_list[-1][0])
                            print(average)
                            year["expected_data"].append((month, (float(chronological_list[-1][1]) * (1 + average))))
                        else:
                            year["expected_data"].append((month, ((year["expected_data"][-1][1]) * (1 + average))))

                    else:

                        # Find the tuple with the specified first element
                        result_1 = [item for item in data_only_list if item[0] == month]
                        # print(result_1)

                        if not result_1:
                            result_1 = float([item for item in fill_in_only_list if item[0] == month][0][1])
                            result_2 = [item for item in data_only_list if item[0] == (month - 1)]

                            if not result_2:
                                try:
                                    result_2 = float([item for item in fill_in_only_list if item[0] == (month - 1)][0][1])
                                    percent_change = float((result_1 - result_2) / abs(result_2)) * 100

                                    fill_in_perc_ls.append((month, percent_change))

                                except ZeroDivisionError:
                                    percent_change = float((result_1 - result_2) / (abs(result_2) + 1)) * 100

                                    fill_in_perc_ls.append((month, percent_change))

                            else:
                                try:
                                    percent_change = float((result_1 - float(result_2[0][1])) / abs(float(result_2[0][1]))) * 100

                                    fill_in_perc_ls.append((month, percent_change))

                                except ZeroDivisionError:
                                    percent_change = float((result_1 - float(result_2[0][1])) / (abs(float(result_2[0][1])) +1)) * 100

                                    fill_in_perc_ls.append((month, percent_change))

                        else:
                            result_1 = float(result_1[0][1])
                            result_2 = [item for item in data_only_list if item[0] == (month - 1)]

                            if not result_2:
                                try:
                                    result_2 = float([item for item in fill_in_only_list if item[0] == (month - 1)][0][1])
                                    percent_change = float((result_1 - result_2) / abs(result_2))

                                    percent_ls.append((month, percent_change))

                                except ZeroDivisionError:
                                    percent_change = float((result_1 - result_2) / (abs(result_2) + 1))

                                    percent_ls.append((month, percent_change))
                            else:
                                try:
                                    percent_change = float((result_1 - float(result_2[0][1])) / abs(float(result_2[0][1])))
                                    percent_ls.append((month, percent_change))

                                except ZeroDivisionError:
                                    percent_change = float((result_1 - float(result_2[0][1])) / (abs(float(result_2[0][1])) + 1))
                                    percent_ls.append((month, percent_change))

                year["percent_change"] = percent_ls
                year["fill_in_per_change"] = fill_in_perc_ls
                year["unfiltered_data"] = chronological_list
                try:
                    year["average_change"] = sum(item[1] for item in percent_ls) / len(percent_ls) # Calculate the average

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
                    account_label_y_start += param["y_space"]

    def add_account_data_label(self):
        value_label_x_start = 270
        value_label_y_start = 80

        # Use account dictionary to create labels and their locations dynamically
        for account in self.account_dict.values():
            # Loop through each account
            for year in account["year"].values():
                # loop through each year dictionary in each account dictionary
                year["data_label"] = [QLabel() for _ in range(len(year["unfiltered_data"]))]
                
                unfiltered_data = year["unfiltered_data"]
                norm_data = year["data"]
                fill_data = year["fill_in_data"]
                
                for un_data in unfiltered_data:
                    # Loop through all of the data that has been sorted chronologically
                    month = un_data[0] # get the month of the data point
                    
                    text = [item for item in norm_data if item[0] == month] # make sure we are getting the input data
                    
                    if not text: # input data not available for month
                        text = [item for item in fill_data if item[0] == month]
                        text = str(text[0][1])
                        year["data_label"][month].setAlignment(Qt.AlignmentFlag.AlignCenter)
                        year["data_label"][month].setStyleSheet("font-weight: bold;") # Visually indicate that data is made up
                        year["data_label"][month].setText(f"${text}")
                        
                        if str(year["year"]) == self.year: # make it visible 
                            year["data_label"][month].setParent(self.scrollAreaWidgetContents)
                        
                        for param in self.widget_parameters:
                            if param["code_name"] == "value":
                                year["data_label"][month].setGeometry(QRect(value_label_x_start, value_label_y_start, param["width"], param["height"]))
                                value_label_x_start += param["x_space"]
                        
                    else: # if input data is available for month
                        text = str(text[0][1])
                        year["data_label"][month].setAlignment(Qt.AlignmentFlag.AlignCenter)
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


# account_dict = {'Roth-IRA': { 'account_id': 6,
#                 'account_label': { 'name': <PyQt6.QtWidgets.QLabel object at 0x00000219B80A2E50>},
#                 'name': 'Roth-IRA',
#                 'query_name': 'Roth-IRA',
#                 'year': { '2022': { 'average_change': 0,
#                                     'data': [],
#                                     'data_label': [ <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDE50>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDEE0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDF70>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE040>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE0D0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE160>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE1F0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE280>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE310>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE3A0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE430>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE4C0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BE550>],
#                                     'expected_data': [],
#                                     'fill_in_data': [ (0, 0),
#                                                       (1, 0),
#                                                       (2, 0),
#                                                       (3, 0),
#                                                       (4, 0),
#                                                       (5, 0),
#                                                       (6, 0),
#                                                       (7, 0),
#                                                       (8, 0),
#                                                       (9, 0),
#                                                       (10, 0),
#                                                       (11, 0),
#                                                       (12, 0)],
#                                     'fill_in_per_change': [ (1, 0.0),
#                                                             (2, 0.0),
#                                                             (3, 0.0),
#                                                             (4, 0.0),
#                                                             (5, 0.0),
#                                                             (6, 0.0),
#                                                             (7, 0.0),
#                                                             (8, 0.0),
#                                                             (9, 0.0),
#                                                             (10, 0.0),
#                                                             (11, 0.0),
#                                                             (12, 0.0)],
#                                     'percent_change': [],
#                                     'sum': 0,
#                                     'unfiltered_data': [ (0, 0),
#                                                          (1, 0),
#                                                          (2, 0),
#                                                          (3, 0),
#                                                          (4, 0),
#                                                          (5, 0),
#                                                          (6, 0),
#                                                          (7, 0),
#                                                          (8, 0),
#                                                          (9, 0),
#                                                          (10, 0),
#                                                          (11, 0),
#                                                          (12, 0)],
#                                     'year': 2022},
#                           '2023': { 'average_change': 0,
#                                     'data': [],
#                                     'data_label': [ <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD820>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD8B0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD940>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD9D0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDA60>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDAF0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDB80>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDC10>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDCA0>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDD30>,
#                                                     <PyQt6.QtWidgets.QLabel object at 0x00000219B80BDDC0>],
#                                     'expected_data': [(11, 0.0), (12, 0.0)],
#                                     'fill_in_data': [ (0, 0),
#                                                       (1, 0),
#                                                       (2, 0),
#                                                       (3, 0),
#                                                       (4, 0),
#                                                       (5, 0),
#                                                       (6, 0),
#                                                       (7, 0),
#                                                       (8, 0),
#                                                       (9, 0),
#                                                       (10, 0)],
#                                     'fill_in_per_change': [ (1, 0.0),
#                                                             (2, 0.0),
#                                                             (3, 0.0),
#                                                             (4, 0.0),
#                                                             (5, 0.0),
#                                                             (6, 0.0),
#                                                             (7, 0.0),
#                                                             (8, 0.0),
#                                                             (9, 0.0),
#                                                             (10, 0.0)],
#                                     'percent_change': [],
#                                     'sum': 0,
#                                     'unfiltered_data': [ (0, 0),
#                                                          (1, 0),
#                                                          (2, 0),
#                                                          (3, 0),
#                                                          (4, 0),
#                                                          (5, 0),
#                                                          (6, 0),
#                                                          (7, 0),
#                                                          (8, 0),
#                                                          (9, 0),
#                                                          (10, 0)],
#                                     'year': 2023}}},
#   'Stocks Account': { 'account_id': 5,
#                       'account_label': { 'name': <PyQt6.QtWidgets.QLabel object at 0x00000219B80A2DC0>},
#                       'name': 'Stocks Account',
#                       'query_name': 'Stocks Account',
#                       'year': { '2022': { 'average_change': 0,
#                                           'data': [],
#                                           'data_label': [ <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD0D0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD160>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD1F0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD280>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD310>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD3A0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD430>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD4C0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD550>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD5E0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD670>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD700>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD790>],
#                                           'expected_data': [],
#                                           'fill_in_data': [ (0, 0),
#                                                             (1, 0),
#                                                             (2, 0),
#                                                             (3, 0),
#                                                             (4, 0),
#                                                             (5, 0),
#                                                             (6, 0),
#                                                             (7, 0),
#                                                             (8, 0),
#                                                             (9, 0),
#                                                             (10, 0),
#                                                             (11, 0),
#                                                             (12, 0)],
#                                           'fill_in_per_change': [ (1, 0.0),
#                                                                   (2, 0.0),
#                                                                   (3, 0.0),
#                                                                   (4, 0.0),
#                                                                   (5, 0.0),
#                                                                   (6, 0.0),
#                                                                   (7, 0.0),
#                                                                   (8, 0.0),
#                                                                   (9, 0.0),
#                                                                   (10, 0.0),
#                                                                   (11, 0.0),
#                                                                   (12, 0.0)],
#                                           'percent_change': [],
#                                           'sum': 0,
#                                           'unfiltered_data': [ (0, 0),
#                                                                (1, 0),
#                                                                (2, 0),
#                                                                (3, 0),
#                                                                (4, 0),
#                                                                (5, 0),
#                                                                (6, 0),
#                                                                (7, 0),
#                                                                (8, 0),
#                                                                (9, 0),
#                                                                (10, 0),
#                                                                (11, 0),
#                                                                (12, 0)],
#                                           'year': 2022},
#                                 '2023': { 'average_change': 0,
#                                           'data': [],
#                                           'data_label': [ <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBA60>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBAF0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBB80>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBC10>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBCA0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBD30>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBDC0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBE50>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBEE0>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BBF70>,
#                                                           <PyQt6.QtWidgets.QLabel object at 0x00000219B80BD040>],
#                                           'expected_data': [ (11, 0.0),
#                                                              (12, 0.0)],
#                                           'fill_in_data': [ (0, 0),
#                                                             (1, 0),
#                                                             (2, 0),
#                                                             (3, 0),
#                                                             (4, 0),
#                                                             (5, 0),
#                                                             (6, 0),
#                                                             (7, 0),
#                                                             (8, 0),
#                                                             (9, 0),
#                                                             (10, 0)],
#                                           'fill_in_per_change': [ (1, 0.0),
#                                                                   (2, 0.0),
#                                                                   (3, 0.0),
#                                                                   (4, 0.0),
#                                                                   (5, 0.0),
#                                                                   (6, 0.0),
#                                                                   (7, 0.0),
#                                                                   (8, 0.0),
#                                                                   (9, 0.0),
#                                                                   (10, 0.0)],
#                                           'percent_change': [],
#                                           'sum': 0,
#                                           'unfiltered_data': [ (0, 0),
#                                                                (1, 0),
#                                                                (2, 0),
#                                                                (3, 0),
#                                                                (4, 0),
#                                                                (5, 0),
#                                                                (6, 0),
#                                                                (7, 0),
#                                                                (8, 0),
#                                                                (9, 0),
#                                                                (10, 0)],
#                                           'year': 2023}}},
#   'Total': { 'account_id': 'total',
#              'account_label': { 'name': <PyQt6.QtWidgets.QLabel object at 0x00000219B80B5280>},
#              'name': 'Total',
#              'query_name': 'Total',
#              'year': { '2022': { 'average_change': 0.0,
#                                  'data': [ (0, 0),
#                                            (1, 0),
#                                            (2, 0),
#                                            (3, 0),
#                                            (4, 0),
#                                            (5, 0),
#                                            (6, 0),
#                                            (7, 0),
#                                            (8, 0),
#                                            (9, 0),
#                                            (10, 0),
#                                            (11, 0),
#                                            (12, 0)],
#                                  'data_label': [ <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8E50>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8EE0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8F70>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C9040>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C90D0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C9160>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C91F0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C9280>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C9310>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C93A0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C9430>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C94C0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C9550>],
#                                  'expected_data': [],
#                                  'fill_in_data': [],
#                                  'fill_in_per_change': [],
#                                  'percent_change': [ (1, 0.0),
#                                                      (2, 0.0),
#                                                      (3, 0.0),
#                                                      (4, 0.0),
#                                                      (5, 0.0),
#                                                      (6, 0.0),
#                                                      (7, 0.0),
#                                                      (8, 0.0),
#                                                      (9, 0.0),
#                                                      (10, 0.0),
#                                                      (11, 0.0),
#                                                      (12, 0.0)],
#                                  'sum': 0,
#                                  'unfiltered_data': [ (0, 0),
#                                                       (1, 0),
#                                                       (2, 0),
#                                                       (3, 0),
#                                                       (4, 0),
#                                                       (5, 0),
#                                                       (6, 0),
#                                                       (7, 0),
#                                                       (8, 0),
#                                                       (9, 0),
#                                                       (10, 0),
#                                                       (11, 0),
#                                                       (12, 0)],
#                                  'year': 2022},
#                        '2023': { 'average_change': 0.0,
#                                  'data': [ (0, Decimal('5000.00')),
#                                            (1, Decimal('5000.00')),
#                                            (2, Decimal('5000.00')),
#                                            (3, Decimal('5000.00')),
#                                            (4, Decimal('5000.00')),
#                                            (5, Decimal('5000.00')),
#                                            (6, Decimal('5000.00')),
#                                            (7, Decimal('5000.00')),
#                                            (8, Decimal('5000.00')),
#                                            (9, Decimal('5000.00')),
#                                            (10, Decimal('5000.00'))],
#                                  'data_label': [ <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8820>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C88B0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8940>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C89D0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8A60>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8AF0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8B80>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8C10>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8CA0>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8D30>,
#                                                  <PyQt6.QtWidgets.QLabel object at 0x00000219B80C8DC0>],
#                                  'expected_data': [(11, 5000.0), (12, 5000.0)],
#                                  'fill_in_data': [],
#                                  'fill_in_per_change': [],
#                                  'percent_change': [ (1, 0.0),
#                                                      (2, 0.0),
#                                                      (3, 0.0),
#                                                      (4, 0.0),
#                                                      (5, 0.0),
#                                                      (6, 0.0),
#                                                      (7, 0.0),
#                                                      (8, 0.0),
#                                                      (9, 0.0),
#                                                      (10, 0.0)],
#                                  'sum': Decimal('5000.00'),
#                                  'unfiltered_data': [ (0, Decimal('5000.00')),
#                                                       (1, Decimal('5000.00')),
#                                                       (2, Decimal('5000.00')),
#                                                       (3, Decimal('5000.00')),
#                                                       (4, Decimal('5000.00')),
#                                                       (5, Decimal('5000.00')),
#                                                       (6, Decimal('5000.00')),
#                                                       (7, Decimal('5000.00')),
#                                                       (8, Decimal('5000.00')),
#                                                       (9, Decimal('5000.00')),
#                                                       (10, Decimal('5000.00'))],
#                                  'year': 2023}}}}