########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import calendar
import pandas as pd
import typing
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow,
                             QWidget,
                             QVBoxLayout,
                             QMessageBox,
                             QStackedWidget,
                             QWidget,
                             QGridLayout,
                             QLabel,
                             QTableWidgetItem,
                             QTableWidget,
                             QToolTip, QComboBox)
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice, QLegend, QBarCategoryAxis, QLineSeries, QValueAxis
from PyQt6.QtGui import QAction, QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QRect, QPointF, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
# from pages.dashboard import Dashboard
########################################################################################

class Budget_Plan_LineChart(QWidget):
    def __init__(self, parent, x_axis_names):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__(parent=parent)
        self.setGeometry(QRect(70, 940, 1700, 459))
        self.setObjectName("Budget_plan_Line_chart")
        self.x_axis_name = x_axis_names

        self.qline_norm = QLineSeries()
        self.qline_norm.setName("Portfolio Chart")
        self.qline_norm.setBrush(Qt.GlobalColor.green)
        self.qline_norm.setColor(Qt.GlobalColor.green)

        self.chart = QChart()
        self.chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.chart.addSeries(self.qline_norm)

        self.chart.setTitle(f"Budget Plan Outlook")

        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.x_axis_name)
        self._axis_x.setLabelsAngle(45)
        self.chart.addAxis(self._axis_x, Qt.AlignmentFlag.AlignBottom)

        self.qline_norm.attachAxis(self._axis_x)

        self._axis_x.setRange("Week 2", "Week 52")

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

        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Create a layout to hold both the chart and the label
        layout = QVBoxLayout()
        layout.addWidget(chart_view)

        self.setLayout(layout)

    def fill_chart(self, data_points):
        self.qline_norm.clear()
        max_amount = 0
        min_amount = 0

        for i in range(len(self.x_axis_name)):
            self.qline_norm.append(i, data_points[i])

            if data_points[i] < min_amount:
                min_amount = data_points[i]

            if data_points[i] > max_amount:
                max_amount = data_points[i]

        # Needs to be changed
        if min_amount <= 100:
            min_amount = 0
        else:
            min_amount -= 200

        max_amount += 100
        self._axis_y.setRange(min_amount, max_amount)