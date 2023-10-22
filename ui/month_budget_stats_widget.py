# Form implementation generated from reading ui file 'month_budget_stats_widget.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 430)
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
        self.reset_pushButton = QtWidgets.QPushButton(parent=Form)
        self.reset_pushButton.setGeometry(QtCore.QRect(350, 10, 180, 40))
        self.reset_pushButton.setStyleSheet("QPushButton {\n"
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
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.month_budget_year_comboBox_2 = QtWidgets.QComboBox(parent=Form)
        self.month_budget_year_comboBox_2.setGeometry(QtCore.QRect(0, 10, 121, 28))
        self.month_budget_year_comboBox_2.setStyleSheet("font: 14pt \"Nirmala UI\";")
        self.month_budget_year_comboBox_2.setObjectName("month_budget_year_comboBox_2")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.month_budget_year_comboBox_2.addItem("")
        self.update_pushButton = QtWidgets.QPushButton(parent=Form)
        self.update_pushButton.setGeometry(QtCore.QRect(140, 10, 180, 40))
        self.update_pushButton.setStyleSheet("QPushButton {\n"
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
        self.update_pushButton.setObjectName("update_pushButton")
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 60, 681, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.amount_total_earnings_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_earnings_label.setObjectName("amount_total_earnings_label")
        self.gridLayout_5.addWidget(self.amount_total_earnings_label, 0, 1, 1, 1)
        self.total_spend_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_spend_label.setObjectName("total_spend_label")
        self.gridLayout_5.addWidget(self.total_spend_label, 0, 2, 1, 1)
        self.amount_total_spend_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_spend_label.setObjectName("amount_total_spend_label")
        self.gridLayout_5.addWidget(self.amount_total_spend_label, 0, 3, 1, 1)
        self.total_food_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_food_label.setObjectName("total_food_label")
        self.gridLayout_5.addWidget(self.total_food_label, 1, 0, 1, 1)
        self.amount_total_food_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_food_label.setObjectName("amount_total_food_label")
        self.gridLayout_5.addWidget(self.amount_total_food_label, 1, 1, 1, 1)
        self.total_extra_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_extra_label.setObjectName("total_extra_label")
        self.gridLayout_5.addWidget(self.total_extra_label, 1, 2, 1, 1)
        self.amount_total_extra_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_extra_label.setObjectName("amount_total_extra_label")
        self.gridLayout_5.addWidget(self.amount_total_extra_label, 1, 3, 1, 1)
        self.total_bills_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_bills_label.setObjectName("total_bills_label")
        self.gridLayout_5.addWidget(self.total_bills_label, 2, 0, 1, 1)
        self.amount_total_bills_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_bills_label.setObjectName("amount_total_bills_label")
        self.gridLayout_5.addWidget(self.amount_total_bills_label, 2, 1, 1, 1)
        self.total_grocery_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_grocery_label.setObjectName("total_grocery_label")
        self.gridLayout_5.addWidget(self.total_grocery_label, 3, 0, 1, 1)
        self.amount_total_grocery_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_grocery_label.setObjectName("amount_total_grocery_label")
        self.gridLayout_5.addWidget(self.amount_total_grocery_label, 3, 1, 1, 1)
        self.total_transportation_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_transportation_label.setObjectName("total_transportation_label")
        self.gridLayout_5.addWidget(self.total_transportation_label, 4, 0, 1, 1)
        self.amount_total_transportation_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_transportation_label.setObjectName("amount_total_transportation_label")
        self.gridLayout_5.addWidget(self.amount_total_transportation_label, 4, 1, 1, 1)
        self.total_free_expense_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_free_expense_label.setObjectName("total_free_expense_label")
        self.gridLayout_5.addWidget(self.total_free_expense_label, 5, 0, 1, 1)
        self.amount_total_free_expense_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_free_expense_label.setObjectName("amount_total_free_expense_label")
        self.gridLayout_5.addWidget(self.amount_total_free_expense_label, 5, 1, 1, 1)
        self.total_investment_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_investment_label.setObjectName("total_investment_label")
        self.gridLayout_5.addWidget(self.total_investment_label, 6, 0, 1, 1)
        self.amount_total_investment_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_investment_label.setObjectName("amount_total_investment_label")
        self.gridLayout_5.addWidget(self.amount_total_investment_label, 6, 1, 1, 1)
        self.total_support_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_support_label.setObjectName("total_support_label")
        self.gridLayout_5.addWidget(self.total_support_label, 7, 0, 1, 1)
        self.amount_total_support_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.amount_total_support_label.setObjectName("amount_total_support_label")
        self.gridLayout_5.addWidget(self.amount_total_support_label, 7, 1, 1, 1)
        self.total_earnings_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.total_earnings_label.setObjectName("total_earnings_label")
        self.gridLayout_5.addWidget(self.total_earnings_label, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.reset_pushButton.setText(_translate("Form", "Reset"))
        self.month_budget_year_comboBox_2.setItemText(0, _translate("Form", "2023"))
        self.month_budget_year_comboBox_2.setItemText(1, _translate("Form", "2022"))
        self.month_budget_year_comboBox_2.setItemText(2, _translate("Form", "2021"))
        self.month_budget_year_comboBox_2.setItemText(3, _translate("Form", "2020"))
        self.month_budget_year_comboBox_2.setItemText(4, _translate("Form", "2019"))
        self.month_budget_year_comboBox_2.setItemText(5, _translate("Form", "2018"))
        self.month_budget_year_comboBox_2.setItemText(6, _translate("Form", "2017"))
        self.month_budget_year_comboBox_2.setItemText(7, _translate("Form", "2016"))
        self.month_budget_year_comboBox_2.setItemText(8, _translate("Form", "2015"))
        self.update_pushButton.setText(_translate("Form", "Update"))
        self.amount_total_earnings_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_spend_label.setText(_translate("Form", "Total Spend :"))
        self.amount_total_spend_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_food_label.setText(_translate("Form", "Total Food :"))
        self.amount_total_food_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_extra_label.setText(_translate("Form", "Total Extra :"))
        self.amount_total_extra_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_bills_label.setText(_translate("Form", "Total Bills :"))
        self.amount_total_bills_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_grocery_label.setText(_translate("Form", "Total Grocery :"))
        self.amount_total_grocery_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_transportation_label.setText(_translate("Form", "Total Transportation :"))
        self.amount_total_transportation_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_free_expense_label.setText(_translate("Form", "Total Free Expense :"))
        self.amount_total_free_expense_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_investment_label.setText(_translate("Form", "Total Investment :"))
        self.amount_total_investment_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_support_label.setText(_translate("Form", "Total Support :"))
        self.amount_total_support_label.setText(_translate("Form", "$1,555,555.55"))
        self.total_earnings_label.setText(_translate("Form", "Total Earnings :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())