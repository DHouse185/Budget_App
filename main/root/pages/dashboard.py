##########  Python IMPORTs  ############################################################
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QScrollArea, QSizePolicy, QAbstractScrollArea
from PyQt6.QtCore import QRect, QSize, Qt
import datetime
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.dashboard_header import Header 
from root.pages.components.button_content import ButtonContent 
from root.pages.components.top_5_expenses_db import Top_5 
from root.pages.components.month_progress import Month_progress
from root.pages.components.doughnut_chart import Doughnut
from root.pages.components.line_chart import LineChart
from root.pages.components.expense_bar_graph import Expense_Bar_Graph
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

        self.button_content = ButtonContent(self.scrollAreaWidgetContents)
        self.year = self.button_content.year 
        self.month_list = self.button_content.selected_month_list
        self.header = Header(self.scrollAreaWidgetContents, self.database, self.year)
        self.top_5 = Top_5(self.scrollAreaWidgetContents, self.database, self.year)
        self.month_progress = Month_progress(self.scrollAreaWidgetContents, self.database)
        self.spend_doughnut_chart = Doughnut(self.scrollAreaWidgetContents, self.database)
        self.spend_line_chart = LineChart(self.scrollAreaWidgetContents, self.database)
        self.expense_bar_graph = Expense_Bar_Graph(self.scrollAreaWidgetContents, self.database, self.month_list, self.year)
        # self.net_income = Net_Income_Bar_Graph()
        # self.waterfall_chrt = Water_Fall_Chart()
        # self.tree_map = Tree_Map()
        
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
        
        
#         self.graphicsView_6 = QtWidgets.QGraphicsView(parent=self.scrollAreaWidgetContents)
#         self.graphicsView_6.setGeometry(QtCore.QRect(1220, 950, 690, 351))
#         self.graphicsView_6.setStyleSheet("background-color: rgb(8, 0, 118);")
#         self.graphicsView_6.setObjectName("graphicsView_6")

# """ 
        