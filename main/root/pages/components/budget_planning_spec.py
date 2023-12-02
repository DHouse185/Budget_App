##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow, 
                             QWidget, 
                             QMessageBox, 
                             QStackedWidget, 
                             QWidget,
                             QGridLayout,
                             QLabel,
                             QFrame,
                             QLineEdit,
                             QVBoxLayout,
                             QCheckBox,
                             QHBoxLayout,
                             QTableWidget,
                             QTableWidgetItem)
from PyQt6.QtGui import QAction, QRegularExpressionValidator, QFont
from PyQt6.QtCore import Qt, QRect, QSize, QRegularExpression
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.components.ui.budget_planning_breakdown_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Budget_Breakdown(Ui_Form):
    def __init__(self, parent, expense_dict, database):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> top_5_expense
        super().__init__()
        self.budget_plan_plan = QWidget(parent=parent)
        self.setupUi(self.budget_plan_plan)
        self.budget_plan_plan.setGeometry(QRect(990, 100, 910, 855))
        self.expenses_dict = expense_dict
        self.database = database
        
        self._valid_float = QRegularExpressionValidator(QRegularExpression(r'^[+-]?\d*\.?\d+$'))
        self.average_actualy_m_wage_lineEdit.setValidator(self._valid_float)
        self.current_savings_lineEdit.setValidator(self._valid_float)
        
        states = self.database.retrieve_states()
        self.states_ls = list()
        for state in states:
            self.states_ls.append(state[0])
        states = states[0]
        self.state_comboBox.addItems(self.states_ls)
        self.amount_fica_label.setText("7.65 %")
        
        self.budget_track_financial()
        self.create_table_items()
    
    def calc_wage_before_tax(self, monthly_wage: str):
        # check = self.actual_wage_check()
        
        # if not check:
        #     return check
                
        # planned_m_wage = monthly_wage.replace("$ ", "")
        # if planned_m_wage == "- -":
        #     return False
        planned_m_wage = monthly_wage
        
        self.mp_at = round((float(self.average_actualy_m_wage_lineEdit.text())), 2) - float(planned_m_wage) 
        self.mp_at = "{:.2f}".format(self.mp_at)
        self.amount_monthly_plan_at_label.setText(f"$ {self.mp_at}")
        
    def actual_wage_check(self):
        entered_wage = self.average_actualy_m_wage_lineEdit.text()
        
        if entered_wage == "":
            self.average_actualy_m_wage_lineEdit.setStyleSheet("border-color: rgb(255, 0, 0);")
            return False
        
        elif entered_wage != "":
            return True 
        
    def budget_track_financial(self):
        self.budget_track_tableWidget = QTableWidget(self.budget_plan_plan)
        self.budget_track_tableWidget.setGeometry(QRect(40, 580, 560, 270))
        self.budget_track_tableWidget.setAutoFillBackground(False)
        self.budget_track_tableWidget.setStyleSheet("QTableView {\n"
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
        self.budget_track_tableWidget.setAlternatingRowColors(True)
        self.budget_track_tableWidget.setObjectName("budget_track_tableWidget")
        self.create_table_items()
    
    def create_table_items(self):
        # self.budget_plan_tableWidget.setColumnCount(11)
        self.row_names = ["Week 2", "Week 4", "Week 6", "Week 8",
                          "Week 10", "Week 12", "Week 14", "Week 16",
                          "Week 18", "Week 20", "Week 22", "Week 24",
                          "Week 26", "Week 28", "Week 30", "Week 32",
                          "Week 34", "Week 36", "Week 38", "Week 40",
                          "Week 42", "Week 44", "Week 46", "Week 48",
                          "Week 50", "Week 52",
                          ]
        self.column_names = ["Total Earnings", "Earnings", "State Taxes", "Federal Taxes", "FICA", "After Taxes", "Total After Taxes", "Bi-Weekly Spending", "Savings"]
        
        self.budget_track_tableWidget.setRowCount(len(self.row_names))
        self.budget_track_tableWidget.setColumnCount(len(self.column_names))
        
        for v_item in range(len(self.row_names)):
            item = QTableWidgetItem()
            item.setFont(QFont("Nirmala UI", 10, 1))
            item.setText(f"{self.row_names[v_item]}")
            self.budget_track_tableWidget.setVerticalHeaderItem(v_item, item)
            
        for h_item in range(len(self.column_names)):
            item = QTableWidgetItem()
            item.setFont(QFont("Nirmala UI", 8, 1))
            item.setText(f"{self.column_names[h_item]}")
            self.budget_track_tableWidget.setHorizontalHeaderItem(h_item, item)
            
        self.budget_track_tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.budget_track_tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.budget_track_tableWidget.verticalHeader().setMinimumSectionSize(35)
    
    def delete_table_items(self):
        self.budget_track_tableWidget.setRowCount(0)
        self.budget_track_tableWidget.setColumnCount(0)
            
    def fill_table(self, total):
        check = self.actual_wage_check()
        
        if check:
            savings = self.current_savings_lineEdit.text()
            if savings == "":
                savings = 0
            self.delete_table_items()
            self.create_table_items()
            
            monthly_spend = round(float(total), 2)
            entered_wage = round(float(self.average_actualy_m_wage_lineEdit.text()), 2)
            total_earned = 0
            total_after_tax = 0
            savings = round(float(savings), 2)
            state = self.state_comboBox.currentText()
            state_tax_data = self.database.get_state_tax_bracket(state)
            federal_tax_data = [(0.1, 0), (0.12, 11001), (0.22, 44726), (0.24, 95376),
                                (0.32, 182101), (0.35, 231251), (0.37, 578126)]
            fica_tax_data = [(0.0765, 0)]
            self.account_data_point = list()
            
            for row in range(self.budget_track_tableWidget.rowCount()):
                item_2 = QTableWidgetItem()
                item_2.setFlags(Qt.ItemFlag.ItemIsEnabled)
                results_2 = round(entered_wage / 2, 2)
                item_2.setText(f"${'{:.2f}'.format(results_2)}")
                self.budget_track_tableWidget.setItem(row, 1, item_2)
                
                item_1 = QTableWidgetItem()
                item_1.setFlags(Qt.ItemFlag.ItemIsEnabled)
                total_earned += results_2
                item_1.setText(f"${'{:.2f}'.format(total_earned)}")
                self.budget_track_tableWidget.setItem(row, 0, item_1)
                
                item_3 = QTableWidgetItem()
                item_3.setFlags(Qt.ItemFlag.ItemIsEnabled)
                rate_1 = float(self.calculate_number(total_earned, state_tax_data))
                self.state_rate = '{:2f}'.format(rate_1 * 100)
                result_3 = round(entered_wage / 2, 2) * rate_1
                item_3.setText(f"${'{:.2f}'.format(result_3)}")
                self.budget_track_tableWidget.setItem(row, 2, item_3)
                
                item_4 = QTableWidgetItem()
                item_4.setFlags(Qt.ItemFlag.ItemIsEnabled)
                rate_2 = float(self.calculate_number(total_earned, federal_tax_data))
                self.federal_rate = '{:2f}'.format(rate_2 * 100)
                result_4 = round(entered_wage / 2, 2) * rate_2
                item_4.setText(f"${'{:.2f}'.format(result_4)}")
                self.budget_track_tableWidget.setItem(row, 3, item_4)
                
                item_5 = QTableWidgetItem()
                item_5.setFlags(Qt.ItemFlag.ItemIsEnabled)
                rate_3 = float(self.calculate_number(total_earned, fica_tax_data))
                self.fica_rate = rate_3 * 100
                result_5 = round(entered_wage / 2, 2) * rate_3
                item_5.setText(f"${'{:.2f}'.format(result_5)}")
                self.budget_track_tableWidget.setItem(row, 4, item_5)
                
                item_6 = QTableWidgetItem()
                item_6.setFlags(Qt.ItemFlag.ItemIsEnabled)
                result_6 = round(entered_wage / 2, 2) - (result_3 + result_4 + result_5)
                item_6.setText(f"${'{:.2f}'.format(result_6)}")
                self.budget_track_tableWidget.setItem(row, 5, item_6)
                
                item_7 = QTableWidgetItem()
                item_7.setFlags(Qt.ItemFlag.ItemIsEnabled)
                total_after_tax += result_6
                item_7.setText(f"${'{:.2f}'.format(total_after_tax)}")
                self.budget_track_tableWidget.setItem(row, 6, item_7)
                
                item_8 = QTableWidgetItem()
                item_8.setFlags(Qt.ItemFlag.ItemIsEnabled)
                result_7 = round(float(monthly_spend) / 2, 2)
                item_8.setText(f"${'{:.2f}'.format(result_7)}")
                self.budget_track_tableWidget.setItem(row, 7, item_8)
                
                item_9 = QTableWidgetItem()
                item_9.setFlags(Qt.ItemFlag.ItemIsEnabled)
                savings += result_6 - result_7 
                item_9.setText(f"${'{:.2f}'.format(savings)}")
                self.budget_track_tableWidget.setItem(row, 8, item_9)
                
                self.account_data_point.append(savings)
        
        self.amount_yearly_before_tax_label.setText(f"$ {'{:.2f}'.format(total_earned)}")
        self.amount_yearly_wage_after_tax_label.setText(f"$ {'{:.2f}'.format(total_after_tax)}")
        self.state_tax_amount_label.setText(f"{self.state_rate} %")
        self.amount_federal_tax_label.setText(f"{self.federal_rate} %")
        
        if total_earned != 0 and total_after_tax != 0:
            
            effective_tax = round(((total_earned - total_after_tax) / total_earned), 2) * 100
            self.amount_yearly_effective_tax.setText(f"{'{:.2f}'.format(effective_tax)} %")
        else:
            self.amount_yearly_effective_tax.setText("0 %")
            
    def calculate_number(self, value, rate_ranges):
        # Sort the rate_ranges by the lower bounds in descending order
        if rate_ranges != []:
            rate_ranges = sorted(rate_ranges, key=lambda x: x[1], reverse=True)

        for rate, lower_bound in rate_ranges:
            if value >= lower_bound:
                return rate

        # If value doesn't match any range, return a default rate
        return 0  # Or any other default calculation