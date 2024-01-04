##########  Python IMPORTs  ############################################################
from pathlib import Path
import os
import csv
from decimal import Decimal
import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QDateEdit, 
                             QWidget, 
                             QMessageBox, 
                             QPushButton, 
                             QWidget,
                             QGridLayout,
                             QLabel,
                             QFrame,
                             QLineEdit,
                             QVBoxLayout,
                             QCheckBox,
                             QHBoxLayout,
                             QInputDialog)
from PyQt6.QtGui import QPainter, QRegularExpressionValidator, QFont
from PyQt6.QtCharts import QChart, QChartView, QLegend, QBarCategoryAxis, QLineSeries, QValueAxis
from PyQt6.QtCore import Qt, QRect, QSize, QRegularExpression, QDate
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.components.ui.outside_expense_plan import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################
        
class Outside_Expense(Ui_Form):
    def __init__(self, parent, x_axis_names):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> top_5_expense
        super().__init__()
        self.outside_expense_plan = QWidget(parent=parent)
        self.setupUi(self.outside_expense_plan)
        self.outside_expense_plan.setGeometry(QRect(0, 2130, 1881, 621))
        
        self.record_list = list()
        self.record_list.append([])
        self.record_index = 0
        
        #######################################
        self.evaluate_pushButton.setEnabled(False) # Make true in parent widget function
        self.undo_pushButton.setEnabled(False) 
        self.redo_pushButton.setEnabled(False)
        
        ##################################################################################
        # Chart                                                                          #
        ##################################################################################
        self.x_axis_name = x_axis_names

        self.qline_norm = QLineSeries()
        self.qline_norm.setName("Portfolio Chart")
        self.qline_norm.setBrush(Qt.GlobalColor.green)
        self.qline_norm.setColor(Qt.GlobalColor.green)

        self.chart = QChart()
        self.chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.chart.addSeries(self.qline_norm)

        self.chart.setTitle(f"Budget Plan Outlook w/Annual Expenses")

        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.x_axis_name)
        self._axis_x.setLabelsAngle(20)
        self._axis_x.setLabelsFont(QFont("Nirmala UI", 7, 1))
        self.chart.addAxis(self._axis_x, Qt.AlignmentFlag.AlignBottom)

        self.qline_norm.attachAxis(self._axis_x)

        self._axis_x.setRange("W2", "W52")

        self._axis_y = QValueAxis()
        self.chart.addAxis(self._axis_y, Qt.AlignmentFlag.AlignLeft)

        self.qline_norm.attachAxis(self._axis_y)

        # Needs to be changed
        min_amount = 0
        max_amount = 100
        self._axis_y.setRange(min_amount, max_amount)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)
        self.chart.legend().setMarkerShape(QLegend.MarkerShape.MarkerShapeCircle)

        chart_view = QChartView(self.chart, self.outside_expense_plan)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        chart_view.setGeometry(QRect(500, 80, 881, 521))
        
        ##################################################################################
        # Signals                                                                        #
        ##################################################################################
        self.undo_pushButton.clicked.connect(self.undo)
        self.redo_pushButton.clicked.connect(self.redo)
    
    def evaluate_expense(self, data_points):
        expense_data_points = data_points.copy()
        time_period = self.date_dateEdit.dateTime()
        time_period = time_period.toPyDateTime()
        time_week_number = time_period.isocalendar()[1]
        data_point_index = int((time_week_number - 1) / 2)
        cost = self.amount_doubleSpinBox.value()
        for index, savings in enumerate(expense_data_points):
            savings -= cost
            expense_data_points[index] = savings if index >= data_point_index else expense_data_points[index]
                
        self.new_yearly_savings_amount_label.setText(f'${round(expense_data_points[-1], 2)}')
        self.record_list.append(expense_data_points.copy())
        self.record_index += 1
        
        if self.record_index <= 0 or self.record_index > len(self.record_list):
            print("Invalid index.")
        else:
            self.record_list[:] = self.record_list[:self.record_index + 1]
            self.undo_pushButton.setEnabled(True)
            self.redo_pushButton.setEnabled(True)
        
        self.fill_chart(expense_data_points)
        
    def undo(self):
        self.record_index -= 1
        if self.record_index < 0:
            self.record_index = 0
            self.undo_pushButton.setEnabled(False)
        else:
            data = self.record_list[self.record_index]
            self.fill_chart(data)
            
    def redo(self):
        if self.record_index >= len(self.record_list):
            self.undo_pushButton.setEnabled(False)
            pass
        else:
            self.record_index += 1
            data = self.record_list[self.record_index]
            self.fill_chart(data)
            if self.record_index >= len(self.record_list - 1):
                self.undo_pushButton.setEnabled(False)
        
    def fill_chart(self, expense_data_points):    
        self.qline_norm.clear()
        max_amount = 0
        min_amount = 0
        if expense_data_points != []:
            for i in range(len(self.x_axis_name)):
                self.qline_norm.append(i, expense_data_points[i])

                if expense_data_points[i] < min_amount:
                    min_amount = expense_data_points[i]

                if expense_data_points[i] > max_amount:
                    max_amount = expense_data_points[i]

        # Needs to be changed
        if min_amount <= 100:
            min_amount = 0
        else:
            min_amount -= 200

        max_amount += 100
        self._axis_y.setRange(min_amount, max_amount)