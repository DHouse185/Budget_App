##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget, QScrollArea, QPushButton
from PyQt6.QtGui import QAction
from PyQt6.QtCore import (Qt, 
                          QPoint, 
                          QRect,
                          QEasingCurve, 
                          QPropertyAnimation, 
                          QParallelAnimationGroup, 
                          QSequentialAnimationGroup)
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.dashboard import Dashboard
from root.pages.transactions import Transactions
from root.pages.calendar import Calendar
from root.pages.monthly_budget import Monthly_Budget
from root.pages.portfolio import Portfolio
from root.pages.budget_planning import Budget_Planning
from root.database import Database
from root.component.side_menu_widget import Side_Menu
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
        
        # Create Side Menu and place in Main Window
        self.side_menu = Side_Menu(self.centralwidget)
        self.side_menu.side_menu_widget.raise_()
        
        # Prepare page swap button
        self.side_menu_button = QPushButton(self.centralwidget)
        self.side_menu_button.setObjectName("side_menu_button")
        self.side_menu_button.setGeometry(QRect(10, 40, 50, 50))
        # indicator for side menu button position
        # 0 means off. 1 means active
        self.side_menu_position = 0
        
        # Create animations for the program
        self.animation_creation()
        
        # Database
        self.database = Database(self.conn, self.logger)
        
        # Dashboard: -> Main Page
        self.dashboard = Dashboard(self.dashboard_page, self.database)
        
        # Dashbord -> Calendar Page
        self.calendar = Calendar(self.calendar_page, self.database)
        
        # Transaction -> Transactions Page
        self.transaction = Transactions(self.transaction_page, self.database)
        
        # Monthly Budget -> Monthly Budget Page
        self.monthly_budget = Monthly_Budget(self.monthly_budget_page, self.database)
        
        # Monthly Budget -> Portfolio Page
        self.portfolio = Portfolio(self.portfolio_page, self.database)
        
        # Monthly Budget -> Portfolio Page
        self.budget_planning = Budget_Planning(self.budget_planning_page, self.database)
        
        # Triggers and events
        self.side_menu_button.clicked.connect(self.side_menu_trigger)
        self.side_menu.dashboard_pushButton.clicked.connect(self.change_to_dashboard_page)
        self.side_menu.calendar_pushButton.clicked.connect(self.change_to_calendar_page)
        self.side_menu.transaction_pushButton.clicked.connect(self.change_to_transaction_page)
        self.side_menu.monthly_budget_pushButton.clicked.connect(self.change_to_monthly_budget_page)
        self.side_menu.portfolio_pushButton.clicked.connect(self.change_to_portfolio_page)
        self.side_menu.budget_planning_pushButton.clicked.connect(self.change_to_budget_planning_page)
    
    
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
            self.transaction.transaction_addition.payback_popup.destroy()
            self.destroy()
            
        # If user chooses not to close application
        elif ret == QMessageBox.StandardButton.Cancel:
            event.ignore()
            
        # Close event will be ignored if neither are selected
        else:
            event.ignore()
            
    def update(self):
        ...
        
    def animation_creation(self):
        """"
        initialize so animations are already prepared for 
        interface trigger function\n
        return: void
        """
       
        # side menu button animation showing menu
        self.sm_button_show = QPropertyAnimation(self.side_menu_button, b"pos")
        self.sm_button_show.setEndValue(QPoint(280, 40))
        self.sm_button_show.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.sm_button_show.setDuration(1000)  # time in ms
        
        # side menu button animation closing menu
        self.sm_button_close = QPropertyAnimation(self.side_menu_button, b"pos")
        self.sm_button_close.setEndValue(QPoint(10, 40))
        self.sm_button_close.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.sm_button_close.setDuration(1200)  # time in ms
        
        # Close side menu animation
        self.close_group_animation = QParallelAnimationGroup()
        self.close_group_animation.addAnimation(self.side_menu.anim_group_disappear)
        self.close_group_animation.addAnimation(self.sm_button_close)
        
        # Open side menu animation
        self.show_group_animation = QParallelAnimationGroup()
        self.show_group_animation.addAnimation(self.side_menu.anim_group_appear)
        self.show_group_animation.addAnimation(self.sm_button_show)
        
    def side_menu_trigger(self):
        if not self.side_menu_position:
            self.show_group_animation.start()
            self.side_menu_position = 1
            return
        
        elif self.side_menu_position:
            self.close_group_animation.start()
            self.side_menu_position = 0
            return
        
        else:
            self.side_menu_position = 0
            return
        
    def change_to_dashboard_page(self):
        self.stackedWidget.setCurrentWidget(self.dashboard_page)
        self.side_menu_trigger()
        return
     
    def change_to_calendar_page(self):
        self.stackedWidget.setCurrentWidget(self.calendar_page)
        self.side_menu_trigger()
        return        
    
    def change_to_transaction_page(self):
        self.stackedWidget.setCurrentWidget(self.transaction_page)
        self.side_menu_trigger()
        return  
    
    def change_to_monthly_budget_page(self):
        self.stackedWidget.setCurrentWidget(self.monthly_budget_page)
        self.side_menu_trigger()
        return    
    
    def change_to_portfolio_page(self):
        self.stackedWidget.setCurrentWidget(self.portfolio_page)
        self.side_menu_trigger()
        return        
    
    def change_to_budget_planning_page(self):
        self.stackedWidget.setCurrentWidget(self.budget_planning_page)
        self.side_menu_trigger()
        return    