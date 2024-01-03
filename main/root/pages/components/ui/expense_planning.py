# Form implementation generated from reading ui file 'expense_planning.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1901, 652)
        Form.setStyleSheet("QWidget {\n"
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
        self.expense_planning_widget = QtWidgets.QWidget(parent=Form)
        self.expense_planning_widget.setGeometry(QtCore.QRect(0, 0, 1901, 651))
        self.expense_planning_widget.setObjectName("budget_planning_widget_2")
        self.expense_planning_label = QtWidgets.QLabel(parent=self.expense_planning_widget)
        self.expense_planning_label.setGeometry(QtCore.QRect(20, 10, 251, 41))
        self.expense_planning_label.setStyleSheet("font: 700 22pt \"Nirmala UI\";")
        self.expense_planning_label.setObjectName("budget_planning_label_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.expense_planning_widget)
        self.scrollArea.setGeometry(QtCore.QRect(30, 60, 955, 440))
        self.scrollArea.setMinimumSize(QtCore.QSize(955, 440))
        self.scrollArea.setMaximumSize(QtCore.QSize(943, 440))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1, 945, 450))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 450))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents_7")
        self.layoutWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 1, 941, 431))
        self.layoutWidget.setObjectName("layoutWidget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout_13")
        self.gridLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.annual_expense_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.annual_expense_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.annual_expense_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
"color: #7300ff;\n"
"border: 2.5px solid #000000;")
        self.annual_expense_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.annual_expense_label.setObjectName("Expenses_label_3")
        self.gridLayout.addWidget(self.annual_expense_label, 0, 0, 1, 1)
        self.time_period_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.time_period_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.time_period_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
"color: #7300ff;\n"
"border: 2.5px solid #000000;")
        self.time_period_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.time_period_label.setObjectName("percentage_label_3")
        self.gridLayout.addWidget(self.time_period_label, 0, 3, 1, 1)
        self.cost_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.cost_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.cost_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
"color: #7300ff;\n"
"border: 2.5px solid #000000;")
        self.cost_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cost_label.setObjectName("cost_label_3")
        self.gridLayout.addWidget(self.cost_label, 0, 2, 1, 1)
        self.input_cost_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.input_cost_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_cost_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
"color: #7300ff;\n"
"border: 2.5px solid #000000;")
        self.input_cost_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_cost_label.setObjectName("input_label_3")
        self.gridLayout.addWidget(self.input_cost_label, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.monthly_review_tableView_3 = QtWidgets.QTableView(parent=self.expense_planning_widget)
        # self.monthly_review_tableView_3.setGeometry(QtCore.QRect(1000, 60, 881, 421))
        # self.monthly_review_tableView_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        # self.monthly_review_tableView_3.setObjectName("monthly_review_tableView_3")
        self.new_year_save_lable = QtWidgets.QLabel(parent=self.expense_planning_widget)
        self.new_year_save_lable.setGeometry(QtCore.QRect(730, 580, 271, 61))
        self.new_year_save_lable.setStyleSheet("font: 800 16pt \"Nirmala UI\";")
        self.new_year_save_lable.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.new_year_save_lable.setWordWrap(True)
        self.new_year_save_lable.setObjectName("average_actualy_m_wage_label_23")
        self.new_year_save_amount_lable = QtWidgets.QLabel(parent=self.expense_planning_widget)
        self.new_year_save_amount_lable.setGeometry(QtCore.QRect(1050, 580, 150, 60))
        self.new_year_save_amount_lable.setStyleSheet("font: 800 16pt \"Nirmala UI\";")
        self.new_year_save_amount_lable.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.new_year_save_amount_lable.setWordWrap(True)
        self.new_year_save_amount_lable.setObjectName("average_actualy_m_wage_label_24")
        self.add_pushButton = QtWidgets.QPushButton(parent=self.expense_planning_widget)
        self.add_pushButton.setGeometry(QtCore.QRect(95, 508, 100, 35))
        self.add_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #00aa00;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00ff00;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #007900;\n"
"    border: 1px solid #5a5a5a;\n"
"}")
        self.add_pushButton.setObjectName("add_pushButton_5")
        self.minus_pushButton = QtWidgets.QPushButton(parent=self.expense_planning_widget)
        self.minus_pushButton.setGeometry(QtCore.QRect(325, 508, 100, 35))
        self.minus_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #c30000;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ff5a5a;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #8c0000;\n"
"    border: 1px solid #5a5a5a;\n"
"}")
        self.minus_pushButton.setObjectName("minus_pushButton_6")
        self.confirm_pushButton = QtWidgets.QPushButton(parent=self.expense_planning_widget)
        self.confirm_pushButton.setGeometry(QtCore.QRect(555, 508, 100, 35))
        self.confirm_pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #00aa00;\n"
"    border: 1px solid #4d4d4d;\n"
"    border-radius: 4px;\n"
"    color: #ffffff;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00ff00;\n"
"    border: 1px solid #5a5a5a;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #007900;\n"
"    border: 1px solid #5a5a5a;\n"
"}")
        self.confirm_pushButton.setObjectName("add_pushButton_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.expense_planning_label.setText(_translate("Form", "Expense Planning"))
        self.annual_expense_label.setText(_translate("Form", "Annual Expenses"))
        self.time_period_label.setText(_translate("Form", "Time period"))
        self.cost_label.setText(_translate("Form", "Cost"))
        self.input_cost_label.setText(_translate("Form", "Cost"))
        self.new_year_save_lable.setText(_translate("Form", "New Yearly Savings :"))
        self.new_year_save_amount_lable.setText(_translate("Form", "$ - -"))
        self.add_pushButton.setText(_translate("Form", "+"))
        self.minus_pushButton.setText(_translate("Form", "-"))
        self.confirm_pushButton.setText(_translate("Form", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())