# Form implementation generated from reading ui file 'Budget_plan.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1740, 640)
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
        self.budget_plan_tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.budget_plan_tableWidget.setGeometry(QtCore.QRect(0, 0, 1900, 640))
        self.budget_plan_tableWidget.setAutoFillBackground(False)
        self.budget_plan_tableWidget.setStyleSheet("QTableView {\n"
"    alternate-background-color: #9f9f9f;\n"
"}\n"
"QTableView QHeaderView {\n"
"    border-bottom: 2px solid white;\n"
"}\n"
"QTableView QHeaderView::section {\n"
"    color: #ffffff;\n"
"    background: #000000;\n"
"    border: 2px;\n"
"}\n"
"QTableView QTableCornerButton::section {\n"
"    color: #ffffff;\n"
"    background: #000000;\n"
"    border-bottom: 2px solid white;\n"
"}")
        self.budget_plan_tableWidget.setAlternatingRowColors(True)
        self.budget_plan_tableWidget.setObjectName("budget_plan_tableWidget")
        # self.budget_plan_tableWidget.setColumnCount(11)
        self.row_names = list()
        self.budget_plan_tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.budget_plan_tableWidget.setVerticalHeaderItem(11, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(8, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(9, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.budget_plan_tableWidget.setHorizontalHeaderItem(10, item)
        self.budget_plan_tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.budget_plan_tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.budget_plan_tableWidget.verticalHeader().setMinimumSectionSize(50)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.budget_plan_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "January"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "February"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "March"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "April"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "May"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "June"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "July"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "August"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "September"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "October"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Form", "November"))
        self.row_names.append(item.text())
        item = self.budget_plan_tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Form", "December"))
        self.row_names.append(item.text())
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("Form", "Earnings"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("Form", "Food"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("Form", "Bills"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(3)
        # item.setText(_translate("Form", "Grocery"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("Form", "Transportation"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(5)
        # item.setText(_translate("Form", "Free Expense"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(6)
        # item.setText(_translate("Form", "Investment"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(7)
        # item.setText(_translate("Form", "Support"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(8)
        # item.setText(_translate("Form", "Starting Budget"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(9)
        # item.setText(_translate("Form", "Total"))
        # item = self.budget_plan_tableWidget.horizontalHeaderItem(10)
        # item.setText(_translate("Form", "Left Amount"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())