# Form implementation generated from reading ui file 'stats_widget.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 1650)
        Form.setStyleSheet("QWidget {\n"
"        background-color: #2c2c2c;\n"
"        color: #ffffff;\n"
"        border: none;\n"
"        font: 11pt \"Nirmala UI\";\n"
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
        self.amount_June_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_June_Earning_label.setGeometry(QtCore.QRect(263, 870, 119, 43))
        self.amount_June_Earning_label.setObjectName("amount_June_Earning_label")
        self.balance_Left_in_Budget_label = QtWidgets.QLabel(parent=Form)
        self.balance_Left_in_Budget_label.setGeometry(QtCore.QRect(10, 481, 247, 43))
        self.balance_Left_in_Budget_label.setWordWrap(True)
        self.balance_Left_in_Budget_label.setObjectName("balance_Left_in_Budget_label")
        self.amount_Starting_Budget_label = QtWidgets.QLabel(parent=Form)
        self.amount_Starting_Budget_label.setGeometry(QtCore.QRect(263, 141, 119, 43))
        self.amount_Starting_Budget_label.setObjectName("amount_Starting_Budget_label")
        self.current_ProfitLoss_label = QtWidgets.QLabel(parent=Form)
        self.current_ProfitLoss_label.setGeometry(QtCore.QRect(10, 238, 247, 43))
        self.current_ProfitLoss_label.setObjectName("current_ProfitLoss_label")
        self.amount_Current_ProfitLoss_label = QtWidgets.QLabel(parent=Form)
        self.amount_Current_ProfitLoss_label.setGeometry(QtCore.QRect(263, 238, 119, 43))
        self.amount_Current_ProfitLoss_label.setObjectName("amount_Current_ProfitLoss_label")
        self.amount_Daily_Average_Expense_label = QtWidgets.QLabel(parent=Form)
        self.amount_Daily_Average_Expense_label.setGeometry(QtCore.QRect(263, 1308, 119, 42))
        self.amount_Daily_Average_Expense_label.setObjectName("amount_Daily_Average_Expense_label")
        self.november_Earning_label = QtWidgets.QLabel(parent=Form)
        self.november_Earning_label.setGeometry(QtCore.QRect(10, 1113, 247, 43))
        self.november_Earning_label.setObjectName("november_Earning_label")
        self.amount_New_Daily_Expense_Planned_label = QtWidgets.QLabel(parent=Form)
        self.amount_New_Daily_Expense_Planned_label.setGeometry(QtCore.QRect(263, 1405, 119, 43))
        self.amount_New_Daily_Expense_Planned_label.setWordWrap(True)
        self.amount_New_Daily_Expense_Planned_label.setObjectName("amount_New_Daily_Expense_Planned_label")
        self.balance_Left_in_Budget_Salary_label = QtWidgets.QLabel(parent=Form)
        self.balance_Left_in_Budget_Salary_label.setGeometry(QtCore.QRect(10, 530, 247, 43))
        self.balance_Left_in_Budget_Salary_label.setWordWrap(True)
        self.balance_Left_in_Budget_Salary_label.setObjectName("balance_Left_in_Budget_Salary_label")
        self.september_Earning_label = QtWidgets.QLabel(parent=Form)
        self.september_Earning_label.setGeometry(QtCore.QRect(10, 1016, 247, 43))
        self.september_Earning_label.setObjectName("september_Earning_label")
        self.weekly_Expense_Goal_label = QtWidgets.QLabel(parent=Form)
        self.weekly_Expense_Goal_label.setGeometry(QtCore.QRect(10, 1454, 247, 42))
        self.weekly_Expense_Goal_label.setWordWrap(True)
        self.weekly_Expense_Goal_label.setObjectName("weekly_Expense_Goal_label")
        self.march_Earning_label = QtWidgets.QLabel(parent=Form)
        self.march_Earning_label.setGeometry(QtCore.QRect(10, 724, 247, 43))
        self.march_Earning_label.setObjectName("march_Earning_label")
        self.stats_Year_comboBox = QtWidgets.QComboBox(parent=Form)
        self.stats_Year_comboBox.setGeometry(QtCore.QRect(10, 10, 372, 28))
        self.stats_Year_comboBox.setStyleSheet("font: 14pt \"Nirmala UI\";")
        self.stats_Year_comboBox.setObjectName("stats_Year_comboBox")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.stats_Year_comboBox.addItem("")
        self.amount_Left_in_Budget_label = QtWidgets.QLabel(parent=Form)
        self.amount_Left_in_Budget_label.setGeometry(QtCore.QRect(263, 433, 119, 42))
        self.amount_Left_in_Budget_label.setObjectName("amount_Left_in_Budget_label")
        self.amount_January_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_January_Earning_label.setGeometry(QtCore.QRect(263, 627, 119, 43))
        self.amount_January_Earning_label.setObjectName("amount_January_Earning_label")
        self.amount_May_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_May_Earning_label.setGeometry(QtCore.QRect(263, 822, 119, 42))
        self.amount_May_Earning_label.setObjectName("amount_May_Earning_label")
        self.max_Days_label = QtWidgets.QLabel(parent=Form)
        self.max_Days_label.setGeometry(QtCore.QRect(10, 44, 247, 43))
        self.max_Days_label.setObjectName("max_Days_label")
        self.daily_Average_Expense_label = QtWidgets.QLabel(parent=Form)
        self.daily_Average_Expense_label.setGeometry(QtCore.QRect(10, 1308, 247, 42))
        self.daily_Average_Expense_label.setObjectName("daily_Average_Expense_label")
        self.planned_Savings_label = QtWidgets.QLabel(parent=Form)
        self.planned_Savings_label.setGeometry(QtCore.QRect(10, 579, 247, 42))
        self.planned_Savings_label.setObjectName("planned_Savings_label")
        self.amount_Current_Expense_Balance_label = QtWidgets.QLabel(parent=Form)
        self.amount_Current_Expense_Balance_label.setGeometry(QtCore.QRect(263, 190, 119, 42))
        self.amount_Current_Expense_Balance_label.setWordWrap(True)
        self.amount_Current_Expense_Balance_label.setObjectName("amount_Current_Expense_Balance_label")
        self.current_Expense_Balance_label = QtWidgets.QLabel(parent=Form)
        self.current_Expense_Balance_label.setGeometry(QtCore.QRect(10, 190, 247, 42))
        self.current_Expense_Balance_label.setWordWrap(True)
        self.current_Expense_Balance_label.setObjectName("current_Expense_Balance_label")
        self.amount_Budget_For_Year_label = QtWidgets.QLabel(parent=Form)
        self.amount_Budget_For_Year_label.setGeometry(QtCore.QRect(263, 287, 119, 43))
        self.amount_Budget_For_Year_label.setObjectName("amount_Budget_For_Year_label")
        self.amount_Balance_Left_in_Budget_label = QtWidgets.QLabel(parent=Form)
        self.amount_Balance_Left_in_Budget_label.setGeometry(QtCore.QRect(263, 481, 119, 43))
        self.amount_Balance_Left_in_Budget_label.setWordWrap(True)
        self.amount_Balance_Left_in_Budget_label.setObjectName("amount_Balance_Left_in_Budget_label")
        self.amount_April_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_April_Earning_label.setGeometry(QtCore.QRect(263, 773, 119, 43))
        self.amount_April_Earning_label.setObjectName("amount_April_Earning_label")
        self.july_Earning_label = QtWidgets.QLabel(parent=Form)
        self.july_Earning_label.setGeometry(QtCore.QRect(10, 919, 247, 43))
        self.july_Earning_label.setObjectName("july_Earning_label")
        self.amount_Predicted_Yearly_Expense_label = QtWidgets.QLabel(parent=Form)
        self.amount_Predicted_Yearly_Expense_label.setGeometry(QtCore.QRect(263, 1551, 119, 42))
        self.amount_Predicted_Yearly_Expense_label.setWordWrap(True)
        self.amount_Predicted_Yearly_Expense_label.setObjectName("amount_Predicted_Yearly_Expense_label")
        self.left_in_Budget_label = QtWidgets.QLabel(parent=Form)
        self.left_in_Budget_label.setGeometry(QtCore.QRect(10, 433, 247, 42))
        self.left_in_Budget_label.setObjectName("left_in_Budget_label")
        self.weekly_Average_Expense_label = QtWidgets.QLabel(parent=Form)
        self.weekly_Average_Expense_label.setGeometry(QtCore.QRect(10, 1502, 247, 43))
        self.weekly_Average_Expense_label.setWordWrap(True)
        self.weekly_Average_Expense_label.setObjectName("weekly_Average_Expense_label")
        self.budget_For_Year_label = QtWidgets.QLabel(parent=Form)
        self.budget_For_Year_label.setGeometry(QtCore.QRect(10, 287, 247, 43))
        self.budget_For_Year_label.setObjectName("budget_For_Year_label")
        self.amount_Total_Spent_label = QtWidgets.QLabel(parent=Form)
        self.amount_Total_Spent_label.setGeometry(QtCore.QRect(263, 336, 119, 42))
        self.amount_Total_Spent_label.setObjectName("amount_Total_Spent_label")
        self.amount_February_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.amount_February_Earnings_label.setGeometry(QtCore.QRect(263, 676, 119, 42))
        self.amount_February_Earnings_label.setObjectName("amount_February_Earnings_label")
        self.amount_October_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_October_Earning_label.setGeometry(QtCore.QRect(263, 1065, 119, 42))
        self.amount_October_Earning_label.setObjectName("amount_October_Earning_label")
        self.daily_Expense_Goal_label = QtWidgets.QLabel(parent=Form)
        self.daily_Expense_Goal_label.setGeometry(QtCore.QRect(10, 1259, 247, 43))
        self.daily_Expense_Goal_label.setObjectName("daily_Expense_Goal_label")
        self.august_Earning_label = QtWidgets.QLabel(parent=Form)
        self.august_Earning_label.setGeometry(QtCore.QRect(10, 968, 247, 42))
        self.august_Earning_label.setObjectName("august_Earning_label")
        self.amount_August_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_August_Earning_label.setGeometry(QtCore.QRect(263, 968, 119, 42))
        self.amount_August_Earning_label.setObjectName("amount_August_Earning_label")
        self.amount_Yearly_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.amount_Yearly_Earnings_label.setGeometry(QtCore.QRect(263, 1211, 119, 42))
        self.amount_Yearly_Earnings_label.setObjectName("amount_Yearly_Earnings_label")
        self.december_Earning_label = QtWidgets.QLabel(parent=Form)
        self.december_Earning_label.setGeometry(QtCore.QRect(10, 1162, 247, 43))
        self.december_Earning_label.setObjectName("december_Earning_label")
        self.amount_Planned_Savings_label = QtWidgets.QLabel(parent=Form)
        self.amount_Planned_Savings_label.setGeometry(QtCore.QRect(263, 579, 119, 42))
        self.amount_Planned_Savings_label.setObjectName("amount_Planned_Savings_label")
        self.february_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.february_Earnings_label.setGeometry(QtCore.QRect(10, 676, 247, 42))
        self.february_Earnings_label.setObjectName("february_Earnings_label")
        self.october_Earning_label = QtWidgets.QLabel(parent=Form)
        self.october_Earning_label.setGeometry(QtCore.QRect(10, 1065, 247, 42))
        self.october_Earning_label.setObjectName("october_Earning_label")
        self.predicted_Yearly_Expense_label = QtWidgets.QLabel(parent=Form)
        self.predicted_Yearly_Expense_label.setGeometry(QtCore.QRect(10, 1551, 247, 42))
        self.predicted_Yearly_Expense_label.setWordWrap(True)
        self.predicted_Yearly_Expense_label.setObjectName("predicted_Yearly_Expense_label")
        self.amount_Days_Passed_label = QtWidgets.QLabel(parent=Form)
        self.amount_Days_Passed_label.setGeometry(QtCore.QRect(263, 93, 119, 42))
        self.amount_Days_Passed_label.setObjectName("amount_Days_Passed_label")
        self.amount_Weekly_Average_Expense_label = QtWidgets.QLabel(parent=Form)
        self.amount_Weekly_Average_Expense_label.setGeometry(QtCore.QRect(263, 1502, 119, 43))
        self.amount_Weekly_Average_Expense_label.setWordWrap(True)
        self.amount_Weekly_Average_Expense_label.setObjectName("amount_Weekly_Average_Expense_label")
        self.april_Earning_label = QtWidgets.QLabel(parent=Form)
        self.april_Earning_label.setGeometry(QtCore.QRect(10, 773, 247, 43))
        self.april_Earning_label.setObjectName("april_Earning_label")
        self.amount_Balance_Left_in_Budget_Salary_label = QtWidgets.QLabel(parent=Form)
        self.amount_Balance_Left_in_Budget_Salary_label.setGeometry(QtCore.QRect(263, 530, 119, 43))
        self.amount_Balance_Left_in_Budget_Salary_label.setWordWrap(True)
        self.amount_Balance_Left_in_Budget_Salary_label.setObjectName("amount_Balance_Left_in_Budget_Salary_label")
        self.amount_Max_Days_label = QtWidgets.QLabel(parent=Form)
        self.amount_Max_Days_label.setGeometry(QtCore.QRect(263, 44, 119, 43))
        self.amount_Max_Days_label.setObjectName("amount_Max_Days_label")
        self.amount_Weekly_Expense_Goal_label = QtWidgets.QLabel(parent=Form)
        self.amount_Weekly_Expense_Goal_label.setGeometry(QtCore.QRect(263, 1454, 119, 42))
        self.amount_Weekly_Expense_Goal_label.setWordWrap(True)
        self.amount_Weekly_Expense_Goal_label.setObjectName("amount_Weekly_Expense_Goal_label")
        self.amount_Predicted_Total_Savings_label = QtWidgets.QLabel(parent=Form)
        self.amount_Predicted_Total_Savings_label.setGeometry(QtCore.QRect(263, 1599, 119, 43))
        self.amount_Predicted_Total_Savings_label.setWordWrap(True)
        self.amount_Predicted_Total_Savings_label.setObjectName("amount_Predicted_Total_Savings_label")
        self.amount_Left_To_Spend_label = QtWidgets.QLabel(parent=Form)
        self.amount_Left_To_Spend_label.setGeometry(QtCore.QRect(263, 384, 119, 43))
        self.amount_Left_To_Spend_label.setObjectName("amount_Left_To_Spend_label")
        self.predicted_Total_Savings_label = QtWidgets.QLabel(parent=Form)
        self.predicted_Total_Savings_label.setGeometry(QtCore.QRect(10, 1599, 247, 43))
        self.predicted_Total_Savings_label.setWordWrap(True)
        self.predicted_Total_Savings_label.setObjectName("predicted_Total_Savings_label")
        self.total_Spent_label = QtWidgets.QLabel(parent=Form)
        self.total_Spent_label.setGeometry(QtCore.QRect(10, 336, 247, 42))
        self.total_Spent_label.setObjectName("total_Spent_label")
        self.new_Daily_Expense_Planned_label = QtWidgets.QLabel(parent=Form)
        self.new_Daily_Expense_Planned_label.setGeometry(QtCore.QRect(10, 1405, 247, 43))
        self.new_Daily_Expense_Planned_label.setWordWrap(True)
        self.new_Daily_Expense_Planned_label.setObjectName("new_Daily_Expense_Planned_label")
        self.amount_July_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_July_Earning_label.setGeometry(QtCore.QRect(263, 919, 119, 43))
        self.amount_July_Earning_label.setObjectName("amount_July_Earning_label")
        self.amount_Daily_Expense_Goal_label = QtWidgets.QLabel(parent=Form)
        self.amount_Daily_Expense_Goal_label.setGeometry(QtCore.QRect(263, 1259, 119, 43))
        self.amount_Daily_Expense_Goal_label.setObjectName("amount_Daily_Expense_Goal_label")
        self.may_Earning_label = QtWidgets.QLabel(parent=Form)
        self.may_Earning_label.setGeometry(QtCore.QRect(10, 822, 247, 42))
        self.may_Earning_label.setObjectName("may_Earning_label")
        self.starting_Budget_label = QtWidgets.QLabel(parent=Form)
        self.starting_Budget_label.setGeometry(QtCore.QRect(10, 141, 247, 43))
        self.starting_Budget_label.setObjectName("starting_Budget_label")
        self.amount_September_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_September_Earning_label.setGeometry(QtCore.QRect(263, 1016, 119, 43))
        self.amount_September_Earning_label.setObjectName("amount_September_Earning_label")
        self.left_To_Spend_label = QtWidgets.QLabel(parent=Form)
        self.left_To_Spend_label.setGeometry(QtCore.QRect(10, 384, 247, 43))
        self.left_To_Spend_label.setObjectName("left_To_Spend_label")
        self.january_Earning_label = QtWidgets.QLabel(parent=Form)
        self.january_Earning_label.setGeometry(QtCore.QRect(10, 627, 247, 43))
        self.january_Earning_label.setObjectName("january_Earning_label")
        self.days_Passed_label = QtWidgets.QLabel(parent=Form)
        self.days_Passed_label.setGeometry(QtCore.QRect(10, 93, 247, 42))
        self.days_Passed_label.setObjectName("days_Passed_label")
        self.amount_December_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_December_Earning_label.setGeometry(QtCore.QRect(263, 1162, 119, 43))
        self.amount_December_Earning_label.setObjectName("amount_December_Earning_label")
        self.amount_March_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_March_Earning_label.setGeometry(QtCore.QRect(263, 724, 119, 43))
        self.amount_March_Earning_label.setObjectName("amount_March_Earning_label")
        self.yearly_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.yearly_Earnings_label.setGeometry(QtCore.QRect(10, 1211, 247, 42))
        self.yearly_Earnings_label.setObjectName("yearly_Earnings_label")
        self.june_Earning_label = QtWidgets.QLabel(parent=Form)
        self.june_Earning_label.setGeometry(QtCore.QRect(10, 870, 247, 43))
        self.june_Earning_label.setObjectName("june_Earning_label")
        self.amount_November_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_November_Earning_label.setGeometry(QtCore.QRect(263, 1113, 119, 43))
        self.amount_November_Earning_label.setObjectName("amount_November_Earning_label")
        self.amount_Current_Savings_Daily_label = QtWidgets.QLabel(parent=Form)
        self.amount_Current_Savings_Daily_label.setGeometry(QtCore.QRect(263, 1356, 119, 43))
        self.amount_Current_Savings_Daily_label.setObjectName("amount_Current_Savings_Daily_label")
        self.current_Savings_Daily_label = QtWidgets.QLabel(parent=Form)
        self.current_Savings_Daily_label.setGeometry(QtCore.QRect(10, 1356, 247, 43))
        self.current_Savings_Daily_label.setObjectName("current_Savings_Daily_label")
        self.month_earning_label_list = [self.amount_January_Earning_label, self.amount_February_Earnings_label,  self.amount_March_Earning_label,
                                         self.amount_April_Earning_label, self.amount_May_Earning_label, self.amount_June_Earning_label,
                                         self.amount_July_Earning_label, self.amount_August_Earning_label, self.amount_September_Earning_label,
                                         self.amount_October_Earning_label, self.amount_November_Earning_label, self.amount_December_Earning_label]
        
        # self.amount_Starting_Budget_label.setText(_translate("Form", "$0.00"))
        # self.amount_Current_ProfitLoss_label.setText(_translate("Form", "$0.00"))
        # self.amount_New_Daily_Expense_Planned_label.setText(_translate("Form", "$0.00"))
        # self.amount_Left_in_Budget_label.setText(_translate("Form", "$0.00"))
        # self.amount_Current_Expense_Balance_label.setText(_translate("Form", "$0.00"))
        # self.amount_Budget_For_Year_label.setText(_translate("Form", "$0.00"))
        # self.amount_Balance_Left_in_Budget_label.setText(_translate("Form", "$0.00"))
        # self.amount_Predicted_Yearly_Expense_label.setText(_translate("Form", "$0.00"))
        # self.left_in_Budget_label.setText(_translate("Form", "Left in Budget"))
        # self.amount_Total_Spent_label.setText(_translate("Form", "$0.00"))
        # self.amount_Yearly_Earnings_label.setText(_translate("Form", "$0.00"))
        # self.amount_Planned_Savings_label.setText(_translate("Form", "$0.00"))
        # self.amount_Days_Passed_label.setText(_translate("Form", "$0.00"))
        # self.amount_Weekly_Average_Expense_label.setText(_translate("Form", "$0.00"))
        # self.amount_Balance_Left_in_Budget_Salary_label.setText(_translate("Form", "$0.00"))
        # self.amount_Max_Days_label.setText(_translate("Form", "$0.00"))
        # self.amount_Weekly_Expense_Goal_label.setText(_translate("Form", "$0.00"))
        # self.amount_Predicted_Total_Savings_label.setText(_translate("Form", "$0.00"))
        # self.amount_Left_To_Spend_label.setText(_translate("Form", "$0.00"))
        # self.total_Spent_label.setText(_translate("Form", "Total Spent"))
        # self.amount_July_Earning_label.setText(_translate("Form", "$0.00"))
        # self.amount_Daily_Expense_Goal_label.setText(_translate("Form", "$0.00"))
        # self.amount_Current_Savings_Daily_label.setText(_translate("Form", "$0.00"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.amount_June_Earning_label.setText(_translate("Form", "$0.00"))
        self.balance_Left_in_Budget_label.setText(_translate("Form", "Balance - Left in Budget"))
        self.amount_Starting_Budget_label.setText(_translate("Form", "$0.00"))
        self.current_ProfitLoss_label.setText(_translate("Form", "Current Profit/Loss"))
        self.amount_Current_ProfitLoss_label.setText(_translate("Form", "$0.00"))
        self.amount_Daily_Average_Expense_label.setText(_translate("Form", "$0.00"))
        self.november_Earning_label.setText(_translate("Form", "November Earnings"))
        self.amount_New_Daily_Expense_Planned_label.setText(_translate("Form", "$0.00"))
        self.balance_Left_in_Budget_Salary_label.setText(_translate("Form", "Balance - Left in Budget + Left Salary"))
        self.september_Earning_label.setText(_translate("Form", "September Earnings"))
        self.weekly_Expense_Goal_label.setText(_translate("Form", "Weekly Expense Goal"))
        self.march_Earning_label.setText(_translate("Form", "March Earnings"))
        self.stats_Year_comboBox.setItemText(0, _translate("Form", "2024"))
        self.stats_Year_comboBox.setItemText(1, _translate("Form", "2023"))
        self.stats_Year_comboBox.setItemText(2, _translate("Form", "2022"))
        self.stats_Year_comboBox.setItemText(3, _translate("Form", "2021"))
        self.stats_Year_comboBox.setItemText(4, _translate("Form", "2020"))
        self.stats_Year_comboBox.setItemText(5, _translate("Form", "2019"))
        self.stats_Year_comboBox.setItemText(6, _translate("Form", "2018"))
        self.stats_Year_comboBox.setItemText(7, _translate("Form", "2017"))
        self.stats_Year_comboBox.setItemText(8, _translate("Form", "2016"))
        self.stats_Year_comboBox.setItemText(9, _translate("Form", "2015"))
        self.amount_Left_in_Budget_label.setText(_translate("Form", "$0.00"))
        self.amount_January_Earning_label.setText(_translate("Form", "$0.00"))
        self.amount_May_Earning_label.setText(_translate("Form", "$0.00"))
        self.max_Days_label.setText(_translate("Form", "Max Days"))
        self.daily_Average_Expense_label.setText(_translate("Form", "Daily Average Expense"))
        self.planned_Savings_label.setText(_translate("Form", "Planned Savings"))
        self.amount_Current_Expense_Balance_label.setText(_translate("Form", "$0.00"))
        self.current_Expense_Balance_label.setText(_translate("Form", "Current Expense Balance"))
        self.amount_Budget_For_Year_label.setText(_translate("Form", "$0.00"))
        self.amount_Balance_Left_in_Budget_label.setText(_translate("Form", "$0.00"))
        self.amount_April_Earning_label.setText(_translate("Form", "$0.00"))
        self.july_Earning_label.setText(_translate("Form", "July Earnings"))
        self.amount_Predicted_Yearly_Expense_label.setText(_translate("Form", "$0.00"))
        self.left_in_Budget_label.setText(_translate("Form", "Left in Budget"))
        self.weekly_Average_Expense_label.setText(_translate("Form", "Weekly Average Expense"))
        self.budget_For_Year_label.setText(_translate("Form", "Budget For Year"))
        self.amount_Total_Spent_label.setText(_translate("Form", "To Be Worked On"))
        self.amount_February_Earnings_label.setText(_translate("Form", "$0.00"))
        self.amount_October_Earning_label.setText(_translate("Form", "$0.00"))
        self.daily_Expense_Goal_label.setText(_translate("Form", "Daily Expense Goal"))
        self.august_Earning_label.setText(_translate("Form", "August Earnings"))
        self.amount_August_Earning_label.setText(_translate("Form", "$0.00"))
        self.amount_Yearly_Earnings_label.setText(_translate("Form", "$0.00"))
        self.december_Earning_label.setText(_translate("Form", "December Earnings"))
        self.amount_Planned_Savings_label.setText(_translate("Form", "$0.00"))
        self.february_Earnings_label.setText(_translate("Form", "February Earnings"))
        self.october_Earning_label.setText(_translate("Form", "October Earnings"))
        self.predicted_Yearly_Expense_label.setText(_translate("Form", "Predicted Yearly Expense"))
        self.amount_Days_Passed_label.setText(_translate("Form", "$0.00"))
        self.amount_Weekly_Average_Expense_label.setText(_translate("Form", "$0.00"))
        self.april_Earning_label.setText(_translate("Form", "April Earnings"))
        self.amount_Balance_Left_in_Budget_Salary_label.setText(_translate("Form", "$0.00"))
        self.amount_Max_Days_label.setText(_translate("Form", "$0.00"))
        self.amount_Weekly_Expense_Goal_label.setText(_translate("Form", "$0.00"))
        self.amount_Predicted_Total_Savings_label.setText(_translate("Form", "$0.00"))
        self.amount_Left_To_Spend_label.setText(_translate("Form", "$0.00"))
        self.predicted_Total_Savings_label.setText(_translate("Form", "Predicted Total Savings"))
        self.total_Spent_label.setText(_translate("Form", "Total Spent"))
        self.new_Daily_Expense_Planned_label.setText(_translate("Form", "New Daily Expense (Planned)"))
        self.amount_July_Earning_label.setText(_translate("Form", "$0.00"))
        self.amount_Daily_Expense_Goal_label.setText(_translate("Form", "$0.00"))
        self.may_Earning_label.setText(_translate("Form", "May Earnings"))
        self.starting_Budget_label.setText(_translate("Form", "Starting Budget"))
        self.amount_September_Earning_label.setText(_translate("Form", "$0.00"))
        self.left_To_Spend_label.setText(_translate("Form", "Left To Spend"))
        self.january_Earning_label.setText(_translate("Form", "January Earnings"))
        self.days_Passed_label.setText(_translate("Form", "Days Passed"))
        self.amount_December_Earning_label.setText(_translate("Form", "$0.00"))
        self.amount_March_Earning_label.setText(_translate("Form", "$0.00"))
        self.yearly_Earnings_label.setText(_translate("Form", "Yearly Earnings"))
        self.june_Earning_label.setText(_translate("Form", "June Earnings"))
        self.amount_November_Earning_label.setText(_translate("Form", "$0.00"))
        self.amount_Current_Savings_Daily_label.setText(_translate("Form", "$0.00"))
        self.current_Savings_Daily_label.setText(_translate("Form", "Current Savings (Daily)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
