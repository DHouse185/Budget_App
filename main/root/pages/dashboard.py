##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget, QScrollArea, QSizePolicy, QAbstractScrollArea
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QRect, QSize, Qt
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.dashboard_header import Header 
from root.pages.components.button_content import ButtonContent 
from root.pages.components.top_5_expenses_db import Top_5 
from root.pages.components.month_progress import Month_progress
# from root.pages.components.expense_bar_graph import Expense_Bar_Graph
########################################################################################



class Dashboard(QWidget):
    """
    Dashboard page that contains and manage all components on the dashboard page
    """
    def __init__(self, page, database: Database):
        super().__init__(page)
        
        self.setGeometry(QRect(0, 0, 1920, 1103))
        self.setObjectName("Dashboard")
        # self.db = Workspace()
        
        # self.notification = notification
        self.dashboard_page = page
        self.database = database
        
        # Configure Dashboard to be scrollable
        self.dashboard_scrollArea = QScrollArea(parent=self.dashboard_page)
        self.dashboard_scrollArea.setGeometry(QRect(0, 0, 1920, 1065))
        sizePolicy_1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy_1.setHorizontalStretch(0)
        sizePolicy_1.setVerticalStretch(0)
        sizePolicy_1.setHeightForWidth(self.dashboard_scrollArea.sizePolicy().hasHeightForWidth())
        self.dashboard_scrollArea.setSizePolicy(sizePolicy_1)
        self.dashboard_scrollArea.setMaximumSize(QSize(1920, 1065))
        self.dashboard_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.dashboard_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.dashboard_scrollArea.setWidgetResizable(True)
        self.dashboard_scrollArea.setObjectName("Dashboard_scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1910, 1600))
        sizePolicy_2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_2.setHorizontalStretch(0)
        sizePolicy_2.setVerticalStretch(0)
        sizePolicy_2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy_2)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1600))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1920, 30000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.header = Header(self.scrollAreaWidgetContents) #, self.database)
        self.button_content = ButtonContent(self.scrollAreaWidgetContents)
        self.top_5 = Top_5(self.scrollAreaWidgetContents)
        self.month_progress = Month_progress(self.scrollAreaWidgetContents, self.database)
        # self.expense_bar_graph = Expense_Bar_Graph()
        
        self.dashboard_scrollArea.setWidget(self.scrollAreaWidgetContents)
            
# """

        
#         self.graphicsView = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
#         self.graphicsView.setGeometry(QtCore.QRect(0, 130, 681, 381))
#         self.graphicsView.setStyleSheet("background-color: rgb(48, 0, 0);")
#         self.graphicsView.setObjectName("graphicsView")
#         self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
#         self.graphicsView_2.setGeometry(QtCore.QRect(0, 510, 681, 391))
#         self.graphicsView_2.setStyleSheet("background-color: rgb(30, 30, 30);")
#         self.graphicsView_2.setObjectName("graphicsView_2")
#         self.graphicsView_3 = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
#         self.graphicsView_3.setGeometry(QtCore.QRect(0, 900, 681, 401))
#         self.graphicsView_3.setStyleSheet("background-color: rgb(8, 0, 118);")
#         self.graphicsView_3.setObjectName("graphicsView_3")
#         self.graphicsView_4 = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
#         self.graphicsView_4.setGeometry(QtCore.QRect(1220, 130, 690, 821))
#         self.graphicsView_4.setStyleSheet("background-color: rgb(48, 0, 0);")
#         self.graphicsView_4.setObjectName("graphicsView_4")
#         self.graphicsView_5 = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
#         self.graphicsView_5.setGeometry(QtCore.QRect(680, 130, 540, 540))
#         self.graphicsView_5.setStyleSheet("background-color: rgb(0, 39, 33);")
#         self.graphicsView_5.setObjectName("graphicsView_5")
        
        
#         self.graphicsView_6 = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
#         self.graphicsView_6.setGeometry(QtCore.QRect(1220, 950, 690, 351))
#         self.graphicsView_6.setStyleSheet("background-color: rgb(8, 0, 118);")
#         self.graphicsView_6.setObjectName("graphicsView_6")
        
        
#         self.Month_progress_widget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
#         self.Month_progress_widget.setGeometry(QtCore.QRect(0, 1310, 1910, 251))
#         self.Month_progress_widget.setStyleSheet("")
#         self.Month_progress_widget.setObjectName("Month_progress_widget")
#         self.gridLayout_2 = QtWidgets.QGridLayout(self.Month_progress_widget)
#         self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.gridLayout_2.setObjectName("gridLayout_2")
#         self.Month_progress_comboBox = QtWidgets.QComboBox(parent=self.Month_progress_widget)
#         self.Month_progress_comboBox.setObjectName("Month_progress_comboBox")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.Month_progress_comboBox.addItem("")
#         self.gridLayout_2.addWidget(self.Month_progress_comboBox, 0, 0, 1, 2)
#         self.month_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.month_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.month_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.month_progress_label.setObjectName("month_progress_label")
#         self.gridLayout_2.addWidget(self.month_progress_label, 1, 0, 1, 1)
#         self.Income_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Income_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Income_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Income_progress_label.setObjectName("Income_progress_label")
#         self.gridLayout_2.addWidget(self.Income_progress_label, 1, 1, 1, 1)
#         self.Eating_out_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Eating_out_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Eating_out_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Eating_out_progress_label.setObjectName("Eating_out_progress_label")
#         self.gridLayout_2.addWidget(self.Eating_out_progress_label, 1, 2, 1, 1)
#         self.Groceries_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Groceries_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Groceries_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Groceries_progress_label.setObjectName("Groceries_progress_label")
#         self.gridLayout_2.addWidget(self.Groceries_progress_label, 1, 3, 1, 1)
#         self.Transportation_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Transportation_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Transportation_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Transportation_progress_label.setObjectName("Transportation_progress_label")
#         self.gridLayout_2.addWidget(self.Transportation_progress_label, 1, 4, 1, 1)
#         self.Free_expense_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Free_expense_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Free_expense_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Free_expense_progress_label.setObjectName("Free_expense_progress_label")
#         self.gridLayout_2.addWidget(self.Free_expense_progress_label, 1, 5, 1, 1)
#         self.Investment_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Investment_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Investment_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Investment_progress_label.setObjectName("Investment_progress_label")
#         self.gridLayout_2.addWidget(self.Investment_progress_label, 1, 6, 1, 1)
#         self.Bill_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Bill_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Bill_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Bill_progress_label.setObjectName("Bill_progress_label")
#         self.gridLayout_2.addWidget(self.Bill_progress_label, 1, 7, 1, 1)
#         self.Support_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Support_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Support_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Support_progress_label.setObjectName("Support_progress_label")
#         self.gridLayout_2.addWidget(self.Support_progress_label, 1, 8, 1, 1)
#         self.Goal_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Goal_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Goal_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Goal_progress_label.setObjectName("Goal_progress_label")
#         self.gridLayout_2.addWidget(self.Goal_progress_label, 1, 9, 1, 1)
#         self.Sum_Total_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Sum_Total_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Sum_Total_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Sum_Total_progress_label.setObjectName("Sum_Total_progress_label")
#         self.gridLayout_2.addWidget(self.Sum_Total_progress_label, 1, 10, 1, 1)
#         self.Profit_Loss_progress_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Profit_Loss_progress_label.setStyleSheet("background-color: rgb(85, 222, 0);\n"
# "color: rgb(0, 0, 0);\n"
# "font: 16pt\n"
# "")
#         self.Profit_Loss_progress_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.Profit_Loss_progress_label.setObjectName("Profit_Loss_progress_label")
#         self.gridLayout_2.addWidget(self.Profit_Loss_progress_label, 1, 11, 1, 1)
#         self.Month_col_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_label.setMinimumSize(QtCore.QSize(100, 0))
#         self.Month_col_label.setObjectName("Month_col_label")
#         self.gridLayout_2.addWidget(self.Month_col_label, 2, 0, 1, 1)
#         self.Month_col_Income_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Income_label.setObjectName("Month_col_Income_label")
#         self.gridLayout_2.addWidget(self.Month_col_Income_label, 2, 1, 1, 1)
#         self.Month_col_Eating_Out_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Eating_Out_label.setObjectName("Month_col_Eating_Out_label")
#         self.gridLayout_2.addWidget(self.Month_col_Eating_Out_label, 2, 2, 1, 1)
#         self.Month_col_Groceries_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Groceries_label.setObjectName("Month_col_Groceries_label")
#         self.gridLayout_2.addWidget(self.Month_col_Groceries_label, 2, 3, 1, 1)
#         self.Month_col_Transportation_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Transportation_label.setObjectName("Month_col_Transportation_label")
#         self.gridLayout_2.addWidget(self.Month_col_Transportation_label, 2, 4, 1, 1)
#         self.Month_col_Free_Expense_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Free_Expense_label.setObjectName("Month_col_Free_Expense_label")
#         self.gridLayout_2.addWidget(self.Month_col_Free_Expense_label, 2, 5, 1, 1)
#         self.Month_col_Investment_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Investment_label.setObjectName("Month_col_Investment_label")
#         self.gridLayout_2.addWidget(self.Month_col_Investment_label, 2, 6, 1, 1)
#         self.Month_col_Bills_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Bills_label.setObjectName("Month_col_Bills_label")
#         self.gridLayout_2.addWidget(self.Month_col_Bills_label, 2, 7, 1, 1)
#         self.Month_col_Support_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Support_label.setObjectName("Month_col_Support_label")
#         self.gridLayout_2.addWidget(self.Month_col_Support_label, 2, 8, 1, 1)
#         self.Month_col_Goal_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Goal_label.setObjectName("Month_col_Goal_label")
#         self.gridLayout_2.addWidget(self.Month_col_Goal_label, 2, 9, 1, 1)
#         self.Month_col_Sum_Total_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Sum_Total_label.setObjectName("Month_col_Sum_Total_label")
#         self.gridLayout_2.addWidget(self.Month_col_Sum_Total_label, 2, 10, 1, 1)
#         self.Month_col_Profit_Loss_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Month_col_Profit_Loss_label.setObjectName("Month_col_Profit_Loss_label")
#         self.gridLayout_2.addWidget(self.Month_col_Profit_Loss_label, 2, 11, 1, 1)
#         self.Spent_col_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_label.setObjectName("Spent_col_label")
#         self.gridLayout_2.addWidget(self.Spent_col_label, 3, 0, 1, 1)
#         self.Spent_col_Income_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Income_label.setObjectName("Spent_col_Income_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Income_label, 3, 1, 1, 1)
#         self.Spent_col_Eating_Out_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Eating_Out_label.setObjectName("Spent_col_Eating_Out_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Eating_Out_label, 3, 2, 1, 1)
#         self.Spent_col_Groceries_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Groceries_label.setObjectName("Spent_col_Groceries_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Groceries_label, 3, 3, 1, 1)
#         self.Spent_col_Transportation_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Transportation_label.setObjectName("Spent_col_Transportation_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Transportation_label, 3, 4, 1, 1)
#         self.Spent_col_Free_Expense_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Free_Expense_label.setObjectName("Spent_col_Free_Expense_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Free_Expense_label, 3, 5, 1, 1)
#         self.Spent_col_Investment_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Investment_label.setObjectName("Spent_col_Investment_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Investment_label, 3, 6, 1, 1)
#         self.Spent_col_Bills_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Bills_label.setObjectName("Spent_col_Bills_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Bills_label, 3, 7, 1, 1)
#         self.Spent_col_Support_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Support_label.setObjectName("Spent_col_Support_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Support_label, 3, 8, 1, 1)
#         self.Spent_col_Goal_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Goal_label.setObjectName("Spent_col_Goal_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Goal_label, 3, 9, 1, 1)
#         self.Spent_col_Sum_Total_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Sum_Total_label.setObjectName("Spent_col_Sum_Total_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Sum_Total_label, 3, 10, 1, 1)
#         self.Spent_col_Profit_Loss_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Spent_col_Profit_Loss_label.setObjectName("Spent_col_Profit_Loss_label")
#         self.gridLayout_2.addWidget(self.Spent_col_Profit_Loss_label, 3, 11, 1, 1)
#         self.Left_col_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_label.setObjectName("Left_col_label")
#         self.gridLayout_2.addWidget(self.Left_col_label, 4, 0, 1, 1)
#         self.Left_col_Income_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Income_label.setObjectName("Left_col_Income_label")
#         self.gridLayout_2.addWidget(self.Left_col_Income_label, 4, 1, 1, 1)
#         self.Left_col_Eating_Out_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Eating_Out_label.setObjectName("Left_col_Eating_Out_label")
#         self.gridLayout_2.addWidget(self.Left_col_Eating_Out_label, 4, 2, 1, 1)
#         self.Left_col_Groceries_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Groceries_label.setObjectName("Left_col_Groceries_label")
#         self.gridLayout_2.addWidget(self.Left_col_Groceries_label, 4, 3, 1, 1)
#         self.Left_col_Transportation_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Transportation_label.setObjectName("Left_col_Transportation_label")
#         self.gridLayout_2.addWidget(self.Left_col_Transportation_label, 4, 4, 1, 1)
#         self.Left_col_Free_Expense_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Free_Expense_label.setObjectName("Left_col_Free_Expense_label")
#         self.gridLayout_2.addWidget(self.Left_col_Free_Expense_label, 4, 5, 1, 1)
#         self.Left_col_Investment_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Investment_label.setObjectName("Left_col_Investment_label")
#         self.gridLayout_2.addWidget(self.Left_col_Investment_label, 4, 6, 1, 1)
#         self.Left_col_Bills_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Bills_label.setObjectName("Left_col_Bills_label")
#         self.gridLayout_2.addWidget(self.Left_col_Bills_label, 4, 7, 1, 1)
#         self.Left_col_Support_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Support_label.setObjectName("Left_col_Support_label")
#         self.gridLayout_2.addWidget(self.Left_col_Support_label, 4, 8, 1, 1)
#         self.Left_col_Support_label_2 = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Support_label_2.setObjectName("Left_col_Support_label_2")
#         self.gridLayout_2.addWidget(self.Left_col_Support_label_2, 4, 9, 1, 1)
#         self.Left_col_Sum_Total_label = QtWidgets.QLabel(parent=self.Month_progress_widget)
#         self.Left_col_Sum_Total_label.setObjectName("Left_col_Sum_Total_label")
#         self.gridLayout_2.addWidget(self.Left_col_Sum_Total_label, 4, 10, 1, 1)
#         self.Income_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Income_progressBar.setProperty("value", 24)
#         self.Income_progressBar.setObjectName("Income_progressBar")
#         self.gridLayout_2.addWidget(self.Income_progressBar, 5, 1, 1, 1)
#         self.Eating_Out_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Eating_Out_progressBar.setProperty("value", 24)
#         self.Eating_Out_progressBar.setObjectName("Eating_Out_progressBar")
#         self.gridLayout_2.addWidget(self.Eating_Out_progressBar, 5, 2, 1, 1)
#         self.Groceries_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Groceries_progressBar.setProperty("value", 24)
#         self.Groceries_progressBar.setObjectName("Groceries_progressBar")
#         self.gridLayout_2.addWidget(self.Groceries_progressBar, 5, 3, 1, 1)
#         self.Transportation_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Transportation_progressBar.setProperty("value", 24)
#         self.Transportation_progressBar.setObjectName("Transportation_progressBar")
#         self.gridLayout_2.addWidget(self.Transportation_progressBar, 5, 4, 1, 1)
#         self.Free_Expense_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Free_Expense_progressBar.setProperty("value", 24)
#         self.Free_Expense_progressBar.setObjectName("Free_Expense_progressBar")
#         self.gridLayout_2.addWidget(self.Free_Expense_progressBar, 5, 5, 1, 1)
#         self.Investment_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Investment_progressBar.setProperty("value", 24)
#         self.Investment_progressBar.setObjectName("Investment_progressBar")
#         self.gridLayout_2.addWidget(self.Investment_progressBar, 5, 6, 1, 1)
#         self.Bills_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Bills_progressBar.setProperty("value", 24)
#         self.Bills_progressBar.setObjectName("Bills_progressBar")
#         self.gridLayout_2.addWidget(self.Bills_progressBar, 5, 7, 1, 1)
#         self.Support_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Support_progressBar.setProperty("value", 24)
#         self.Support_progressBar.setObjectName("Support_progressBar")
#         self.gridLayout_2.addWidget(self.Support_progressBar, 5, 8, 1, 1)
#         self.Goal_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Goal_progressBar.setProperty("value", 24)
#         self.Goal_progressBar.setObjectName("Goal_progressBar")
#         self.gridLayout_2.addWidget(self.Goal_progressBar, 5, 9, 1, 1)
#         self.Sum_Total_progressBar = QtWidgets.QProgressBar(parent=self.Month_progress_widget)
#         self.Sum_Total_progressBar.setProperty("value", 24)
#         self.Sum_Total_progressBar.setObjectName("Sum_Total_progressBar")
#         self.gridLayout_2.addWidget(self.Sum_Total_progressBar, 5, 10, 1, 1)
#         self.Dashboard_scrollArea.setWidget(self.scrollAreaWidgetContents)
#         Budget_StackedWidget.addWidget(self.Dashboard_page)
# """ 
        