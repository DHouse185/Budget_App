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
    "Feb" : "February",
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
DISABLED_BLUE_BUTTON_STYLE = """QPushButton {
                                    background-color: #000277;
                                    border: 1px solid #a3a3a3;
                                    border-radius: 4px;
                                    color: #ffffff;
                                    padding: 5px;
                                    }"""                                            
RED_BUTTON_STYLE = """QPushButton {
                                    background-color: #c30000;
                                    border: 1px solid #4d4d4d;
                                    border-radius: 4px;
                                    color: #ffffff;
                                    padding: 5px;
                                    }
                        QPushButton:hover {
                                            background-color: #ff5a5a;
                                            border: 1px solid #5a5a5a;
                                            }
                        QPushButton:pressed {
                                            background-color: #8c0000;
                                            border: 1px solid #5a5a5a;
                                            }"""                                        
DISABLED_RED_BUTTON_STYLE = """QPushButton {
                                    background-color: #8c0000;
                                    border: 1px solid #5a5a5a;
                                    border-radius: 4px;
                                    color: #ffffff;
                                    padding: 5px;
                                    }"""
GREEN_BUTTON_STYLE = """QPushButton {
                                    background-color: #00aa00;
                                    border: 1px solid #4d4d4d;
                                    border-radius: 4px;
                                    color: #ffffff;
                                    padding: 5px;
                                    }
                        QPushButton:hover {
                                            background-color: #00ff00;
                                            border: 1px solid #5a5a5a;
                                            }
                        QPushButton:pressed {
                                            background-color: #007900;
                                            border: 1px solid #5a5a5a;
                                            }"""  
APP_STYLE = ("QWidget {\n"
"        background-color: #2c2c2c;\n"
"        color: #ffffff;\n"
"        border: none;\n"
"        font: 14pt \"Nirmala UI\";\n"
"}\n"
"QWidget#side_menu {\n"
"    background-color: #4e5564;\n"
"    color: #ffffff;\n"
"    border: 1px solid #4e5564;\n"
"    border-radius: 16px;\n"
"    font: 14pt \"Nirmala UI\";\n"
"}\n"
"QLabel#Dashboard_Title {\n"
"    background-color: none;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    font: 20pt \"Nirmala UI\";\n"
"}\n"
"QLabel#Eat_Out_Image {\n"
"    background-image: url(:/images/pngaaa.com-2384833.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QLabel#Grocery_Image {\n"
"    background-image: url(:/images/pngaaa.com-2138453.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QLabel#Transportation_Image {\n"
"    background-image: url(:/images/pngaaa.com-2182093.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QLabel#Free_Expense_Image {\n"
"    background-image: url(:/images/pngaaa.com-1261106.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QLabel#Bills_Image {\n"
"    background-image: url(:/images/pngaaa.com-1433501.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QLabel#Investment_Image {\n"
"    background-image: url(:/images/pngaaa.com-3584133.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QLabel#Support_Image {\n"
"    background-image: url(:/images/pngaaa.com-2914571.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QLabel#Goal_Image {\n"
"    background-image: url(:/images/pngaaa.com-848656.png);\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton {\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5a5a5a;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"QPushButton#side_menu_button:hover {\n"
"    background-image: url(:/button_image/Burger_button_hover.png);\n"
"    background-color: #5a5a5a;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"QPushButton#side_menu_button:pressed {\n"
"    background-image: url(:/button_image/Burger_button_click.png);\n"
"    background-color: #5a5a5a;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"QPushButton#remove_button_watchlist {\n"
"    background-color: #ff0000;\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#remove_button_watchlist:hover {\n"
"    background-color: #ff6c6c;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"QPushButton#remove_button_watchlist:pressed {\n"
"    background-color: #aa0000;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"QPushButton#Add_strategy {\n"
"    background-color: #00ad0e;\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#Add_strategy:hover {\n"
"    background-color: #67ff74;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"QPushButton#Add_strategy:pressed {\n"
"    background-color: #006408;\n"
"    border: 1px solid #a3a3a3;\n"
"}\n"
"QPushButton#Activation {\n"
"    background-color: #00ad0e;\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#Activation:hover {\n"
"    background-color: #67ff74;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"QPushButton#Activation:pressed {\n"
"    background-color: #006408;\n"
"    border: 1px solid #a3a3a3;\n"
"}\n"
"QPushButton#Blue_button {\n"
"    background-color: #0003bb;\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#Blue_button:hover {\n"
"    background-color: #4446d1;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"QPushButton#Blue_button:pressed {\n"
"    background-color: #000277;\n"
"    border: 1px solid #a3a3a3;\n"
"}\n"
"QPushButton#Yellow_button {\n"
"    background-color: #a5bd1e;\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#Yellow_button:hover {\n"
"    background-color: #e5ff54;\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"QPushButton#Yellow_button:pressed {\n"
"    background-color: #81960f;\n"
"    border: 1px solid #a3a3a3;\n"
"}\n"
"QCheckBox {\n"
"    color: #ffffff;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"    border-color: #ffffff;\n"
"    border-radius: 6px;\n"
"}\n"
"QTextEdit {\n"
"    background-color: #4d4d4d;\n"
"    border: 1px solid #4d4d4d;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"    border-color: #ffffff;\n"
"    border-radius: 20px;\n"
"}\n"
"QProgressBar {\n"
"    border: 1px solid #444444;\n"
"    border-radius: 7px;\n"
"    background-color: #2e2e2e;\n"
"    text-align: center;\n"
"    font-size: 10pt;\n"
"    color: white;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #3a3a3a;\n"
"    width: 5px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #3a3a3a;\n"
"    width: 10px;\n"
"    margin: 16px 0 16px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #444444;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: #3a3a3a;\n"
"    height: 10px;\n"
"    margin: 0px 16px 0 16px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #444444;\n"
"    border-radius: 5px;\n"
"}\n"
"QTabWidget {\n"
"    background-color: #2e2e2e;\n"
"    border: none;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: #2e2e2e;\n"
"    color: #b1b1b1;\n"
"    padding: 8px 20px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border: none;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: #3a3a3a;\n"
"    color: white;\n"
"}")
                                            
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