# Form implementation generated from reading ui file 'button_content_widget.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6.QtWidgets import (QWidget, 
                             QGridLayout,
                             QApplication, 
                             QPushButton)
from PyQt6.QtCore import (QRect,
                          Qt, 
                          QMetaObject, 
                          QCoreApplication)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 351)
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
        self.button_Content_widget = QWidget(parent=Form)
        self.button_Content_widget.setGeometry(QRect(0, 0, 540, 351))
        self.button_Content_widget.setObjectName("button_Content_widget")
        self.gridLayout = QGridLayout(self.button_Content_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.jan_pushButton = QPushButton(parent=self.button_Content_widget)
        self.jan_pushButton.setObjectName("jan_pushButton")
        self.gridLayout.addWidget(self.jan_pushButton, 0, 0, 1, 1)
        self.feb_pushButton = QPushButton(parent=self.button_Content_widget)
        self.feb_pushButton.setObjectName("feb_pushButton")
        self.gridLayout.addWidget(self.feb_pushButton, 0, 1, 1, 1)
        self.mar_pushButton = QPushButton(parent=self.button_Content_widget)
        self.mar_pushButton.setObjectName("mar_pushButton")
        self.gridLayout.addWidget(self.mar_pushButton, 0, 2, 1, 1)
        self.apr_pushButton = QPushButton(parent=self.button_Content_widget)
        self.apr_pushButton.setObjectName("apr_pushButton")
        self.gridLayout.addWidget(self.apr_pushButton, 0, 3, 1, 1)
        self.may_pushButton_5 = QPushButton(parent=self.button_Content_widget)
        self.may_pushButton_5.setObjectName("may_pushButton_5")
        self.gridLayout.addWidget(self.may_pushButton_5, 1, 0, 1, 1)
        self.jun_pushButton_6 = QPushButton(parent=self.button_Content_widget)
        self.jun_pushButton_6.setObjectName("jun_pushButton_6")
        self.gridLayout.addWidget(self.jun_pushButton_6, 1, 1, 1, 1)
        self.jul_pushButton_7 = QPushButton(parent=self.button_Content_widget)
        self.jul_pushButton_7.setObjectName("jul_pushButton_7")
        self.gridLayout.addWidget(self.jul_pushButton_7, 1, 2, 1, 1)
        self.aug_pushButton_8 = QPushButton(parent=self.button_Content_widget)
        self.aug_pushButton_8.setObjectName("aug_pushButton_8")
        self.gridLayout.addWidget(self.aug_pushButton_8, 1, 3, 1, 1)
        self.sep_pushButton_9 = QPushButton(parent=self.button_Content_widget)
        self.sep_pushButton_9.setObjectName("sep_pushButton_9")
        self.gridLayout.addWidget(self.sep_pushButton_9, 2, 0, 1, 1)
        self.oct_pushButton_10 = QPushButton(parent=self.button_Content_widget)
        self.oct_pushButton_10.setObjectName("oct_pushButton_10")
        self.gridLayout.addWidget(self.oct_pushButton_10, 2, 1, 1, 1)
        self.nov_pushButton_11 = QPushButton(parent=self.button_Content_widget)
        self.nov_pushButton_11.setObjectName("nov_pushButton_11")
        self.gridLayout.addWidget(self.nov_pushButton_11, 2, 2, 1, 1)
        self.dec_pushButton_12 = QPushButton(parent=self.button_Content_widget)
        self.dec_pushButton_12.setObjectName("dec_pushButton_12")
        self.gridLayout.addWidget(self.dec_pushButton_12, 2, 3, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.jan_pushButton.setText(_translate("Form", "Jan"))
        self.feb_pushButton.setText(_translate("Form", "Feb"))
        self.mar_pushButton.setText(_translate("Form", "Mar"))
        self.apr_pushButton.setText(_translate("Form", "Apr"))
        self.may_pushButton_5.setText(_translate("Form", "May"))
        self.jun_pushButton_6.setText(_translate("Form", "Jun"))
        self.jul_pushButton_7.setText(_translate("Form", "Jul"))
        self.aug_pushButton_8.setText(_translate("Form", "Aug"))
        self.sep_pushButton_9.setText(_translate("Form", "Sep"))
        self.oct_pushButton_10.setText(_translate("Form", "Oct"))
        self.nov_pushButton_11.setText(_translate("Form", "Nov"))
        self.dec_pushButton_12.setText(_translate("Form", "Dec"))