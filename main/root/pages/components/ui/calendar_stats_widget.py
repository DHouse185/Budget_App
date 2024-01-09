# Form implementation generated from reading ui file 'calendar_stats_widget.ui'
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
        self.amount_Balance_Left_in_Budget_Salary_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Balance_Left_in_Budget_Salary_Months_label.setGeometry(QtCore.QRect(209, 596, 173, 56))
        self.amount_Balance_Left_in_Budget_Salary_Months_label.setWordWrap(True)
        self.amount_Balance_Left_in_Budget_Salary_Months_label.setObjectName("amount_Balance_Left_in_Budget_Salary_Months_label")
        self.stats_Month_comboBox = QtWidgets.QComboBox(parent=Form)
        self.stats_Month_comboBox.setGeometry(QtCore.QRect(10, 7, 180, 28))
        self.stats_Month_comboBox.setStyleSheet("font: 14pt \"Nirmala UI\";")
        self.stats_Month_comboBox.setObjectName("stats_Month_comboBox")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.stats_Month_comboBox.addItem("")
        self.starting_Budget_Months_label = QtWidgets.QLabel(parent=Form)
        self.starting_Budget_Months_label.setGeometry(QtCore.QRect(10, 164, 193, 56))
        self.starting_Budget_Months_label.setObjectName("starting_Budget_Months_label")
        self.balance_Left_in_Budget_Months_label = QtWidgets.QLabel(parent=Form)
        self.balance_Left_in_Budget_Months_label.setGeometry(QtCore.QRect(10, 535, 193, 55))
        self.balance_Left_in_Budget_Months_label.setWordWrap(True)
        self.balance_Left_in_Budget_Months_label.setObjectName("balance_Left_in_Budget_Months_label")
        self.days_Passed_Months_label = QtWidgets.QLabel(parent=Form)
        self.days_Passed_Months_label.setGeometry(QtCore.QRect(10, 103, 193, 55))
        self.days_Passed_Months_label.setObjectName("days_Passed_Months_label")
        self.amount_Week_1_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_Week_1_Earning_label.setGeometry(QtCore.QRect(209, 720, 173, 55))
        self.amount_Week_1_Earning_label.setObjectName("amount_Week_1_Earning_label")
        self.planned_Savings_Months_label = QtWidgets.QLabel(parent=Form)
        self.planned_Savings_Months_label.setGeometry(QtCore.QRect(10, 658, 193, 56))
        self.planned_Savings_Months_label.setObjectName("planned_Savings_Months_label")
        self.amount_Balance_Left_in_Budget_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Balance_Left_in_Budget_Months_label.setGeometry(QtCore.QRect(209, 535, 173, 55))
        self.amount_Balance_Left_in_Budget_Months_label.setWordWrap(True)
        self.amount_Balance_Left_in_Budget_Months_label.setObjectName("amount_Balance_Left_in_Budget_Months_label")
        self.budget_For_Month_label = QtWidgets.QLabel(parent=Form)
        self.budget_For_Month_label.setGeometry(QtCore.QRect(10, 349, 193, 56))
        self.budget_For_Month_label.setObjectName("budget_For_Month_label")
        self.amount_Total_Spent_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Total_Spent_Months_label.setGeometry(QtCore.QRect(209, 411, 173, 56))
        self.amount_Total_Spent_Months_label.setObjectName("amount_Total_Spent_Months_label")
        self.amount_Current_Savings_Daily_label = QtWidgets.QLabel(parent=Form)
        self.amount_Current_Savings_Daily_label.setGeometry(QtCore.QRect(209, 1275, 173, 56))
        self.amount_Current_Savings_Daily_label.setObjectName("amount_Current_Savings_Daily_label")
        self.max_Days_Months_label = QtWidgets.QLabel(parent=Form)
        self.max_Days_Months_label.setGeometry(QtCore.QRect(10, 41, 193, 56))
        self.max_Days_Months_label.setObjectName("max_Days_Months_label")
        self.weekly_Expense_Goal_Months_label = QtWidgets.QLabel(parent=Form)
        self.weekly_Expense_Goal_Months_label.setGeometry(QtCore.QRect(10, 1398, 193, 56))
        self.weekly_Expense_Goal_Months_label.setWordWrap(True)
        self.weekly_Expense_Goal_Months_label.setObjectName("weekly_Expense_Goal_Months_label")
        self.predicted_Monthly_Expense_Months_label = QtWidgets.QLabel(parent=Form)
        self.predicted_Monthly_Expense_Months_label.setGeometry(QtCore.QRect(10, 1522, 193, 55))
        self.predicted_Monthly_Expense_Months_label.setWordWrap(True)
        self.predicted_Monthly_Expense_Months_label.setObjectName("predicted_Monthly_Expense_Months_label")
        self.amount_Planned_Savings_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Planned_Savings_Months_label.setGeometry(QtCore.QRect(209, 658, 173, 56))
        self.amount_Planned_Savings_Months_label.setObjectName("amount_Planned_Savings_Months_label")
        self.balance_Left_in_Budget_Salary_Months_label = QtWidgets.QLabel(parent=Form)
        self.balance_Left_in_Budget_Salary_Months_label.setGeometry(QtCore.QRect(10, 596, 193, 56))
        self.balance_Left_in_Budget_Salary_Months_label.setWordWrap(True)
        self.balance_Left_in_Budget_Salary_Months_label.setObjectName("balance_Left_in_Budget_Salary_Months_label")
        self.amount_Current_ProfitLoss_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Current_ProfitLoss_Months_label.setGeometry(QtCore.QRect(209, 288, 173, 55))
        self.amount_Current_ProfitLoss_Months_label.setObjectName("amount_Current_ProfitLoss_Months_label")
        self.amount_Budget_For_Month_label = QtWidgets.QLabel(parent=Form)
        self.amount_Budget_For_Month_label.setGeometry(QtCore.QRect(209, 349, 173, 56))
        self.amount_Budget_For_Month_label.setObjectName("amount_Budget_For_Month_label")
        self.current_ProfitLoss_Months_label = QtWidgets.QLabel(parent=Form)
        self.current_ProfitLoss_Months_label.setGeometry(QtCore.QRect(10, 288, 193, 55))
        self.current_ProfitLoss_Months_label.setObjectName("current_ProfitLoss_Months_label")
        self.amount_Yearly_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.amount_Yearly_Earnings_label.setGeometry(QtCore.QRect(209, 1090, 173, 55))
        self.amount_Yearly_Earnings_label.setObjectName("amount_Yearly_Earnings_label")
        self.amount_Daily_Expense_Goal_label = QtWidgets.QLabel(parent=Form)
        self.amount_Daily_Expense_Goal_label.setGeometry(QtCore.QRect(209, 1151, 173, 56))
        self.amount_Daily_Expense_Goal_label.setObjectName("amount_Daily_Expense_Goal_label")
        self.Week_3_Earning_label = QtWidgets.QLabel(parent=Form)
        self.Week_3_Earning_label.setGeometry(QtCore.QRect(10, 843, 193, 56))
        self.Week_3_Earning_label.setObjectName("Week_3_Earning_label")
        self.amount_Daily_Average_Expense_label = QtWidgets.QLabel(parent=Form)
        self.amount_Daily_Average_Expense_label.setGeometry(QtCore.QRect(209, 1213, 173, 56))
        self.amount_Daily_Average_Expense_label.setObjectName("amount_Daily_Average_Expense_label")
        self.Week_6_Earning_label = QtWidgets.QLabel(parent=Form)
        self.Week_6_Earning_label.setGeometry(QtCore.QRect(10, 1028, 193, 56))
        self.Week_6_Earning_label.setObjectName("Week_6_Earning_label")
        self.amount_Predicted_Total_Savings_label = QtWidgets.QLabel(parent=Form)
        self.amount_Predicted_Total_Savings_label.setGeometry(QtCore.QRect(209, 1583, 173, 56))
        self.amount_Predicted_Total_Savings_label.setWordWrap(True)
        self.amount_Predicted_Total_Savings_label.setObjectName("amount_Predicted_Total_Savings_label")
        self.weekly_Average_Expense_Months_label = QtWidgets.QLabel(parent=Form)
        self.weekly_Average_Expense_Months_label.setGeometry(QtCore.QRect(10, 1460, 193, 56))
        self.weekly_Average_Expense_Months_label.setWordWrap(True)
        self.weekly_Average_Expense_Months_label.setObjectName("weekly_Average_Expense_Months_label")
        self.monthly_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.monthly_Earnings_label.setGeometry(QtCore.QRect(10, 1090, 193, 55))
        self.monthly_Earnings_label.setObjectName("monthly_Earnings_label")
        self.Week_2_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.Week_2_Earnings_label.setGeometry(QtCore.QRect(10, 781, 193, 56))
        self.Week_2_Earnings_label.setObjectName("Week_2_Earnings_label")
        self.amount_Weekly_Expense_Goal_label = QtWidgets.QLabel(parent=Form)
        self.amount_Weekly_Expense_Goal_label.setGeometry(QtCore.QRect(209, 1398, 173, 56))
        self.amount_Weekly_Expense_Goal_label.setWordWrap(True)
        self.amount_Weekly_Expense_Goal_label.setObjectName("amount_Weekly_Expense_Goal_label")
        self.left_in_Budget_Months_label = QtWidgets.QLabel(parent=Form)
        self.left_in_Budget_Months_label.setGeometry(QtCore.QRect(10, 473, 193, 56))
        self.left_in_Budget_Months_label.setObjectName("left_in_Budget_Months_label")
        self.amount_Week_6_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_Week_6_Earning_label.setGeometry(QtCore.QRect(209, 1028, 173, 56))
        self.amount_Week_6_Earning_label.setObjectName("amount_Week_6_Earning_label")
        self.daily_Expense_Goal_Months_label = QtWidgets.QLabel(parent=Form)
        self.daily_Expense_Goal_Months_label.setGeometry(QtCore.QRect(10, 1151, 193, 56))
        self.daily_Expense_Goal_Months_label.setObjectName("daily_Expense_Goal_Months_label")
        self.amount_Starting_Budget_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Starting_Budget_Months_label.setGeometry(QtCore.QRect(209, 164, 173, 56))
        self.amount_Starting_Budget_Months_label.setObjectName("amount_Starting_Budget_Months_label")
        self.amount_Left_in_Budget_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Left_in_Budget_Months_label.setGeometry(QtCore.QRect(209, 473, 173, 56))
        self.amount_Left_in_Budget_Months_label.setObjectName("amount_Left_in_Budget_Months_label")
        self.current_Expense_Balance_Months_label = QtWidgets.QLabel(parent=Form)
        self.current_Expense_Balance_Months_label.setGeometry(QtCore.QRect(10, 226, 193, 56))
        self.current_Expense_Balance_Months_label.setWordWrap(True)
        self.current_Expense_Balance_Months_label.setObjectName("current_Expense_Balance_Months_label")
        self.Week_4_Earning_label = QtWidgets.QLabel(parent=Form)
        self.Week_4_Earning_label.setGeometry(QtCore.QRect(10, 905, 193, 55))
        self.Week_4_Earning_label.setObjectName("Week_4_Earning_label")
        self.amount_Week_4_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_Week_4_Earning_label.setGeometry(QtCore.QRect(209, 905, 173, 55))
        self.amount_Week_4_Earning_label.setObjectName("amount_Week_4_Earning_label")
        self.amount_Days_Passed_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Days_Passed_Months_label.setGeometry(QtCore.QRect(209, 103, 173, 55))
        self.amount_Days_Passed_Months_label.setObjectName("amount_Days_Passed_Months_label")
        self.total_Spent_Months_label = QtWidgets.QLabel(parent=Form)
        self.total_Spent_Months_label.setGeometry(QtCore.QRect(10, 411, 193, 56))
        self.total_Spent_Months_label.setObjectName("total_Spent_Months_label")
        self.amount_Current_Expense_Balance_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Current_Expense_Balance_Months_label.setGeometry(QtCore.QRect(209, 226, 173, 56))
        self.amount_Current_Expense_Balance_Months_label.setWordWrap(True)
        self.amount_Current_Expense_Balance_Months_label.setObjectName("amount_Current_Expense_Balance_Months_label")
        self.amount_Predicted_Monthly_Expense_label = QtWidgets.QLabel(parent=Form)
        self.amount_Predicted_Monthly_Expense_label.setGeometry(QtCore.QRect(209, 1522, 173, 55))
        self.amount_Predicted_Monthly_Expense_label.setWordWrap(True)
        self.amount_Predicted_Monthly_Expense_label.setObjectName("amount_Predicted_Monthly_Expense_label")
        self.Week_5_Earning_label = QtWidgets.QLabel(parent=Form)
        self.Week_5_Earning_label.setGeometry(QtCore.QRect(10, 966, 193, 56))
        self.Week_5_Earning_label.setObjectName("Week_5_Earning_label")
        self.Week_1_Earning_label = QtWidgets.QLabel(parent=Form)
        self.Week_1_Earning_label.setGeometry(QtCore.QRect(10, 720, 193, 55))
        self.Week_1_Earning_label.setObjectName("Week_1_Earning_label")
        self.amount_Week_2_Earnings_label = QtWidgets.QLabel(parent=Form)
        self.amount_Week_2_Earnings_label.setGeometry(QtCore.QRect(209, 781, 173, 56))
        self.amount_Week_2_Earnings_label.setObjectName("amount_Week_2_Earnings_label")
        self.amount_New_Daily_Expense_Planned_label = QtWidgets.QLabel(parent=Form)
        self.amount_New_Daily_Expense_Planned_label.setGeometry(QtCore.QRect(209, 1337, 173, 55))
        self.amount_New_Daily_Expense_Planned_label.setWordWrap(True)
        self.amount_New_Daily_Expense_Planned_label.setObjectName("amount_New_Daily_Expense_Planned_label")
        self.current_Savings_Daily_Months_label = QtWidgets.QLabel(parent=Form)
        self.current_Savings_Daily_Months_label.setGeometry(QtCore.QRect(10, 1275, 193, 56))
        self.current_Savings_Daily_Months_label.setObjectName("current_Savings_Daily_Months_label")
        self.daily_Average_Expense_Months_label = QtWidgets.QLabel(parent=Form)
        self.daily_Average_Expense_Months_label.setGeometry(QtCore.QRect(10, 1213, 193, 56))
        self.daily_Average_Expense_Months_label.setObjectName("daily_Average_Expense_Months_label")
        self.new_Daily_Expense_Planned_Months_label = QtWidgets.QLabel(parent=Form)
        self.new_Daily_Expense_Planned_Months_label.setGeometry(QtCore.QRect(10, 1337, 193, 55))
        self.new_Daily_Expense_Planned_Months_label.setWordWrap(True)
        self.new_Daily_Expense_Planned_Months_label.setObjectName("new_Daily_Expense_Planned_Months_label")
        self.amount_Max_Days_Months_label = QtWidgets.QLabel(parent=Form)
        self.amount_Max_Days_Months_label.setGeometry(QtCore.QRect(209, 41, 173, 56))
        self.amount_Max_Days_Months_label.setObjectName("amount_Max_Days_Months_label")
        self.predicted_Total_Savings_Months_label = QtWidgets.QLabel(parent=Form)
        self.predicted_Total_Savings_Months_label.setGeometry(QtCore.QRect(10, 1583, 193, 56))
        self.predicted_Total_Savings_Months_label.setWordWrap(True)
        self.predicted_Total_Savings_Months_label.setObjectName("predicted_Total_Savings_Months_label")
        self.amount_Week_5_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_Week_5_Earning_label.setGeometry(QtCore.QRect(209, 966, 173, 56))
        self.amount_Week_5_Earning_label.setObjectName("amount_Week_5_Earning_label")
        self.amount_Week_3_Earning_label = QtWidgets.QLabel(parent=Form)
        self.amount_Week_3_Earning_label.setGeometry(QtCore.QRect(209, 843, 173, 56))
        self.amount_Week_3_Earning_label.setObjectName("amount_Week_3_Earning_label")
        self.amount_Weekly_Average_Expense_label = QtWidgets.QLabel(parent=Form)
        self.amount_Weekly_Average_Expense_label.setGeometry(QtCore.QRect(209, 1460, 173, 56))
        self.amount_Weekly_Average_Expense_label.setWordWrap(True)
        self.amount_Weekly_Average_Expense_label.setObjectName("amount_Weekly_Average_Expense_label")
        self.stats_Year_comboBox = QtWidgets.QComboBox(parent=Form)
        self.stats_Year_comboBox.setGeometry(QtCore.QRect(200, 7, 180, 28))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.amount_Balance_Left_in_Budget_Salary_Months_label.setText(_translate("Form", "$ - "))
        self.stats_Month_comboBox.setItemText(0, _translate("Form", "January"))
        self.stats_Month_comboBox.setItemText(1, _translate("Form", "February"))
        self.stats_Month_comboBox.setItemText(2, _translate("Form", "March"))
        self.stats_Month_comboBox.setItemText(3, _translate("Form", "April"))
        self.stats_Month_comboBox.setItemText(4, _translate("Form", "May"))
        self.stats_Month_comboBox.setItemText(5, _translate("Form", "June"))
        self.stats_Month_comboBox.setItemText(6, _translate("Form", "July"))
        self.stats_Month_comboBox.setItemText(7, _translate("Form", "August"))
        self.stats_Month_comboBox.setItemText(8, _translate("Form", "September"))
        self.stats_Month_comboBox.setItemText(9, _translate("Form", "October"))
        self.stats_Month_comboBox.setItemText(10, _translate("Form", "November"))
        self.stats_Month_comboBox.setItemText(11, _translate("Form", "December"))
        self.starting_Budget_Months_label.setText(_translate("Form", "Starting Budget"))
        self.balance_Left_in_Budget_Months_label.setText(_translate("Form", "Balance After Budget Exp."))
        self.days_Passed_Months_label.setText(_translate("Form", "Days Passed"))
        self.amount_Week_1_Earning_label.setText(_translate("Form", "$ - "))
        self.planned_Savings_Months_label.setText(_translate("Form", "Planned Savings"))
        self.amount_Balance_Left_in_Budget_Months_label.setText(_translate("Form", "$ - "))
        self.budget_For_Month_label.setText(_translate("Form", "Budget For Month"))
        self.amount_Total_Spent_Months_label.setText(_translate("Form", "$ - "))
        self.amount_Current_Savings_Daily_label.setText(_translate("Form", "$ - "))
        self.max_Days_Months_label.setText(_translate("Form", "Max Days"))
        self.weekly_Expense_Goal_Months_label.setText(_translate("Form", "Weekly Expense Goal"))
        self.predicted_Monthly_Expense_Months_label.setText(_translate("Form", "Predicted Monthly Expense"))
        self.amount_Planned_Savings_Months_label.setText(_translate("Form", "$ - "))
        self.balance_Left_in_Budget_Salary_Months_label.setText(_translate("Form", "Balance after Budget Exp. +                           Expected Income"))
        self.amount_Current_ProfitLoss_Months_label.setText(_translate("Form", "$ - "))
        self.amount_Budget_For_Month_label.setText(_translate("Form", "$ - "))
        self.current_ProfitLoss_Months_label.setText(_translate("Form", "Current Profit/Loss"))
        self.amount_Yearly_Earnings_label.setText(_translate("Form", "$ - "))
        self.amount_Daily_Expense_Goal_label.setText(_translate("Form", "$ - "))
        self.Week_3_Earning_label.setText(_translate("Form", "Week 3 Earnings"))
        self.amount_Daily_Average_Expense_label.setText(_translate("Form", "$ - "))
        self.Week_6_Earning_label.setText(_translate("Form", "Week 6 Earnings"))
        self.amount_Predicted_Total_Savings_label.setText(_translate("Form", "$ - "))
        self.weekly_Average_Expense_Months_label.setText(_translate("Form", "Weekly Average Expense"))
        self.monthly_Earnings_label.setText(_translate("Form", "Monthly Earnings"))
        self.Week_2_Earnings_label.setText(_translate("Form", "Week 2 Earnings"))
        self.amount_Weekly_Expense_Goal_label.setText(_translate("Form", "$ - "))
        self.left_in_Budget_Months_label.setText(_translate("Form", "Left in Budget"))
        self.amount_Week_6_Earning_label.setText(_translate("Form", "$ - "))
        self.daily_Expense_Goal_Months_label.setText(_translate("Form", "Daily Expense Goal"))
        self.amount_Starting_Budget_Months_label.setText(_translate("Form", "$ - "))
        self.amount_Left_in_Budget_Months_label.setText(_translate("Form", "$ - "))
        self.current_Expense_Balance_Months_label.setText(_translate("Form", "Current Balance"))
        self.Week_4_Earning_label.setText(_translate("Form", "Week 4 Earnings"))
        self.amount_Week_4_Earning_label.setText(_translate("Form", "$ - "))
        self.amount_Days_Passed_Months_label.setText(_translate("Form", "$ - "))
        self.total_Spent_Months_label.setText(_translate("Form", "Total Spent"))
        self.amount_Current_Expense_Balance_Months_label.setText(_translate("Form", "$ - "))
        self.amount_Predicted_Monthly_Expense_label.setText(_translate("Form", "$ - "))
        self.Week_5_Earning_label.setText(_translate("Form", "Week 5 Earnings"))
        self.Week_1_Earning_label.setText(_translate("Form", "Week 1 Earnings"))
        self.amount_Week_2_Earnings_label.setText(_translate("Form", "$ - "))
        self.amount_New_Daily_Expense_Planned_label.setText(_translate("Form", "$ - "))
        self.current_Savings_Daily_Months_label.setText(_translate("Form", "Current Savings (Daily)"))
        self.daily_Average_Expense_Months_label.setText(_translate("Form", "Daily Average Expense"))
        self.new_Daily_Expense_Planned_Months_label.setText(_translate("Form", "New Daily Expense (Planned)"))
        self.amount_Max_Days_Months_label.setText(_translate("Form", "$ - "))
        self.predicted_Total_Savings_Months_label.setText(_translate("Form", "Predicted Total Savings"))
        self.amount_Week_5_Earning_label.setText(_translate("Form", "$ - "))
        self.amount_Week_3_Earning_label.setText(_translate("Form", "$ - "))
        self.amount_Weekly_Average_Expense_label.setText(_translate("Form", "$ - "))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
