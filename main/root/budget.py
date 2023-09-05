##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget, QScrollArea
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.dashboard import Dashboard
# from root.pages.transactions import Transactions
from root.database import Database
import root.utils.resources # Do not remove. Needed for images
########################################################################################

class Budget(QWidget):
    def __init__(self,
                 MainWindow: QMainWindow,
                 logger,
                 database):
        super().__init__(MainWindow)
        
        # initiate logger in this class
        self.logger = logger
        self.conn = database
        
        # Prepare MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1118)
        MainWindow.setWindowTitle("Budget")
        
        # Gives Mainwindow dark mode style
        MainWindow.setStyleSheet(Path(rvar.DARK_MODE).read_text())
        
        # Replace QMainWindow closeEvent with one of our own
        MainWindow.closeEvent = self.closeEvent
        MainWindow.setMaximumSize(1920, 1128)
        
        # Begin the main parent widget of the main window
        # Mainwindow -> central widget
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 25, 1920, 1103))
        
        # Menu Bar
        # Mainwindow -> Menu Bar
        # Apply menu bar to MainWindow
        self.menu_bar = MainWindow.menuBar()
        self.menu_bar.setGeometry(QRect(0, 0, 1920, 15))
        
        # Create action for menu bar
        self.actionSave_Workspace = QAction(MainWindow)
        self.actionSave_Workspace.setObjectName(u"actionSave_Workspace")
        self.actionSave_Workspace.setText("Save Workspace")
        
        # Action of "Save Workspace" in menu bar
        #               self.actionSave_Workspace.triggered.connect(self._save_workspace)
        
        # On the menu bar there will be a menu called "Workspace"
        workspace_menu = self.menu_bar.addMenu('&Workspace')
        #           workspace_menu.addAction(self.actionSave_Workspace)
        
        # Prepare Pages (i.e. Stack Widgets) for Main Window
        # Mainwindow -> central widget -> StackWidget
        self.stackedWidget = QStackedWidget(self.centralwidget)
        #   self.stackedWidget.stackUnder(self.notification)
        self.stackedWidget.setObjectName(u"Main_stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1920, 1103))
        
        # Starting Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"Dashboard_page")
        self.stackedWidget.addWidget(self.dashboard_page)
        
        # Calendar Page
        # Mainwindow -> central widget -> StackWidget -> Calendar Page
        self.calendar_page = QWidget()
        self.calendar_page.setObjectName(u"Calendar_page")
        self.stackedWidget.addWidget(self.calendar_page)
        
        # Transactions Page
        # Mainwindow -> central widget -> StackWidget -> Transactions Page
        self.transaction_page = QWidget()
        self.transaction_page.setObjectName(u"Transactions_page")
        self.stackedWidget.addWidget(self.transaction_page)
        
        # Monthly Budget Snapshot Page
        # Mainwindow -> central widget -> StackWidget -> Monthly Budget Snapshot Page
        self.monthly_budget_page = QWidget()
        self.monthly_budget_page.setObjectName(u"Monthly_Budget_page")
        self.stackedWidget.addWidget(self.monthly_budget_page)
        
        # Portfolio Page
        # Mainwindow -> central widget -> StackWidget -> Portfolio Page
        self.portfolio_page = QWidget()
        self.portfolio_page.setObjectName(u"Portfolio_page")
        self.stackedWidget.addWidget(self.portfolio_page)
        
        # Budget Planning Page
        # Mainwindow -> central widget -> StackWidget -> Budget Planning Page
        self.budget_planning_page = QWidget()
        self.budget_planning_page.setObjectName(u"Budget_Planning_page")
        self.stackedWidget.addWidget(self.budget_planning_page)
        
        # Spending Planning Page
        # Mainwindow -> central widget -> StackWidget -> Spending Planning Page
        self.spending_planning_page = QWidget()
        self.spending_planning_page.setObjectName(u"Spending_Planning_page")
        self.stackedWidget.addWidget(self.spending_planning_page)
        
        # Make the main page the main page upon initializing
        self.stackedWidget.setCurrentWidget(self.dashboard_page)
        
        # Database
        # self.database = Database(self.conn)
        
        # Dashboard: -> Main Page
        self.dashboard = Dashboard(self.dashboard_page) #, self.database)
        
        # Transaction -> Transactions Page
        # self.transaction = Transactions(self.transaction_page, self.database)
    
    
    def closeEvent(self, event):
        """
        Custom close event handler\n
        closes:\n
        Main Application\n
        Binance US websocket
        """
        ret = QMessageBox.question(self, "Confirmation",
                                 "Do you really want to exit the application?",
                                 QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to exit the application
        if ret == QMessageBox.StandardButton.Close:
            self.conn.close()
            event.accept()
            self.destroy()
            
        # If user chooses not to close application
        elif ret == QMessageBox.StandardButton.Cancel:
            event.ignore()
            
        # Close event will be ignored if neither are selected
        else:
            event.ignore()
            
    def update(self):
        ...