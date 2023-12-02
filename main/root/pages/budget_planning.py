##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QLabel, QStackedWidget, QTableView, QScrollArea, QSizePolicy, QAbstractScrollArea, QTableWidgetItem
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QModelIndex, QRect, QAbstractTableModel, Qt, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.pages.components.budget_planning import Budget_Plan 
from root.pages.components.budget_planning_spec import Budget_Breakdown 
from root.pages.components.budget_planning_lc_1 import Budget_Plan_LineChart 
########################################################################################
            
class Budget_Planning(QWidget):
    """
    Transaction page that Shows a table of all transactions that has occurred
    """
    def __init__(self, page, database: Database):
        super().__init__(page)
        self.setGeometry(QRect(0, 0, 1920, 1065))
        self.setObjectName("Budget_Planning")
        
        # self.db = Workspace()
        # self.notification = notification

        self.budget_planning = page
        self.database = database
        
        # Configure Transaction to be scrollable
        self.budget_p_main_scrollArea = QScrollArea(parent=self.budget_planning)
        self.budget_p_main_scrollArea.setGeometry(QRect(0, 0, 1920, 1090))
        sizePolicy_1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy_1.setHorizontalStretch(0)
        sizePolicy_1.setVerticalStretch(0)
        sizePolicy_1.setHeightForWidth(self.budget_p_main_scrollArea.sizePolicy().hasHeightForWidth())
        self.budget_p_main_scrollArea.setSizePolicy(sizePolicy_1)
        self.budget_p_main_scrollArea.setMaximumSize(QSize(1920, 1065))
        self.budget_p_main_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.budget_p_main_scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.budget_p_main_scrollArea.setWidgetResizable(True)
        self.budget_p_main_scrollArea.setObjectName("budget_p_main_scrollArea")

        
        self.budget_p_main_scrollAreaWidgetContents = QWidget()
        self.budget_p_main_scrollAreaWidgetContents.setEnabled(True)
        self.budget_p_main_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1905, 2750))
        sizePolicy_2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy_2.setHorizontalStretch(0)
        sizePolicy_2.setVerticalStretch(0)
        sizePolicy_2.setHeightForWidth(self.budget_p_main_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.budget_p_main_scrollAreaWidgetContents.setSizePolicy(sizePolicy_2)
        self.budget_p_main_scrollAreaWidgetContents.setMinimumSize(QSize(0, 2750))
        self.budget_p_main_scrollAreaWidgetContents.setMaximumSize(QSize(1920, 30000))
        self.budget_p_main_scrollAreaWidgetContents.setObjectName("budget_p_main_scrollAreaWidgetContents")
        
        self.budget_planning_label = QLabel(parent=self.budget_p_main_scrollAreaWidgetContents)
        self.budget_planning_label.setGeometry(QRect(40, 10, 231, 41))
        self.budget_planning_label.setStyleSheet("font: 700 22pt \"Nirmala UI\";")
        self.budget_planning_label.setObjectName("budget_planning_label")
        self.budget_planning_label.setText("Budget Planning")
        
        self.yearly_savings_label = QLabel(parent=self.budget_p_main_scrollAreaWidgetContents)
        self.yearly_savings_label.setGeometry(QRect(740, 1400, 271, 61))
        self.yearly_savings_label.setStyleSheet("font: 800 16pt \"Nirmala UI\";")
        self.yearly_savings_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yearly_savings_label.setWordWrap(True)
        self.yearly_savings_label.setText("Yearly Savings :")
        
        self.amount_yearly_savings_label = QLabel(parent=self.budget_p_main_scrollAreaWidgetContents)
        self.amount_yearly_savings_label.setGeometry(QRect(1060, 1400, 150, 60))
        self.amount_yearly_savings_label.setStyleSheet("font: 800 16pt \"Nirmala UI\";")
        self.amount_yearly_savings_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.amount_yearly_savings_label.setWordWrap(True)
        
        # Budget Planning widget
        self.budget_planning_plan = Budget_Plan(self.budget_p_main_scrollAreaWidgetContents, self.database)
        self.expenses_planned = self.budget_planning_plan.expenses_dict
        self.budget_planning_breakdown = Budget_Breakdown(self.budget_p_main_scrollAreaWidgetContents, 
                                                           self.budget_planning_plan.expenses_dict, 
                                                           self.database)
        self.bp_linechart = Budget_Plan_LineChart(self.budget_p_main_scrollAreaWidgetContents, self.budget_planning_breakdown.row_names)
        
        # Update and stats widget
        # year var. & dict stats var. pass to -> stats Widget
        
        
        # Chart widget
        # pass dict stats widget var. -> chart widget

        
        # Signals
        self.budget_planning_breakdown.confirm_pushButton.clicked.connect(self.project_earnings)
        # Update signal
        
        # Add account signal
        
        # Remove account signal
        
        # Chart signal
        
        self.budget_p_main_scrollArea.setWidget(self.budget_p_main_scrollAreaWidgetContents)
        
    def project_earnings(self):
        check = self.budget_planning_breakdown.actual_wage_check()
        
        if not check:
            return
        
        planned_m_wage = self.budget_planning_plan.monthly_wage_cost_label.text().replace("$ ", "")
        if planned_m_wage == "- -":
            return
        
        monthly_spend = self.budget_planning_plan.total_cost_label.text().replace("$ ", "")
        if monthly_spend == "- -":
            return
        
        self.budget_planning_breakdown.calc_wage_before_tax(planned_m_wage)
        self.budget_planning_breakdown.fill_table(monthly_spend)
        self.bp_linechart.fill_chart(self.budget_planning_breakdown.account_data_point)
        
        self.amount_yearly_savings_label.setText(f"$ {self.budget_planning_breakdown.account_data_point[-1]}")
        
        
        