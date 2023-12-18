##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import pandas as pd
import os
########################################################################################

root_util_directory = os.path.dirname(__file__)
DARK_MODE = os.path.join(root_util_directory, "style", "darkmode_style.qss")
CURRENT_DATE = datetime.datetime.now()
CURRENT_YEAR = CURRENT_DATE.year
CURRENT_MONTH = CURRENT_DATE.month
CURRENT_DAY = CURRENT_DATE.day
DARK_MODE_TRANS_TABLE = ("""QTableView {\n
                         alternate-background-color: #9f9f9f;\n
                        }\n
                         QTableView QHeaderView {\n
                            border-bottom: 2px solid white;\n
                        }\n
                        QTableView QHeaderView::section {\n
                            color: #ffffff;\n
                            background: #000000;\n
                            border: 2px;\n
                        }\n
                        QTableView QTableCornerButton::section {\n
                            color: #ffffff;\n
                            background: #000000;\n
                            border-bottom: 2px solid white;\n
                        }""")
MONTHS_SHORT_DICT = {
    "Jan" : "January",
    "Feb" : "Februry",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
NORMAL_BUTTON_STYLE = """QPushButton {
                                        background-color: #4d4d4d;
                                        border: 1px solid #4d4d4d;
                                        border-radius: 4px;
                                        color: #ffffff;
                                        padding: 5px;
                                        }
                        QPushButton:hover {
                                            background-color: #5a5a5a;
                                            border: 1px solid #5a5a5a;
                                            }"""
BLUE_BUTTON_STYLE = """QPushButton {
                                    background-color: #0003bb;
                                    border: 1px solid #ffffff;
                                    border-radius: 4px;
                                    color: #ffffff;
                                    padding: 5px;
                                    }
                        QPushButton:hover {
                                            background-color: #4446d1;
                                            border: 1px solid #ffffff;
                                            }
                        QPushButton:pressed {
                                                background-color: #000277;
                                                border: 1px solid #a3a3a3;
                                            }"""
month_dict ={
    'January'  : 1,
    'February' : 2,
    'March'    : 3,
    'April'    : 4,
    'May'      : 5,
    'June'     : 6,
    'July'     : 7,
    'August'   : 8,
    'September': 9,
    'October'  : 10,
    'November' : 11,
    'December' : 12,
}
category_dict = {
    'Food'           : 1,
    'Bills'          : 2,
    'Grocery'        : 3,
    'Free Expense'   : 4,
    'Earnings'       : 5,
    'Transportation' : 6,
    'Investment'     : 7,
    'Support'        : 8,
    'Payment'        : 9,
}
table_dict ={
    'category_test'        : 'category', 
    'sub_category_test'    : 'sub_category',
    'account_test'         : 'account',
    'category_type_test'   : 'category_type',
    'accounting_type_test' : 'accounting',
    'month_test'           : 'month',
}
YEARS_LIST = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', ]