##########  Python IMPORTs  ############################################################
from typing import List
from decimal import Decimal
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QWidget, 
                             QVBoxLayout, 
                             QPushButton, 
                             QPushButton)
from PyQt6.QtCharts import (QBarCategoryAxis, 
                            QBarSeries, 
                            QBarSet, 
                            QChart, 
                            QChartView, 
                            QLineSeries, 
                            QValueAxis, QLegend)
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt, QRect
import numpy as np
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
########################################################################################

class Net_Income_Bar_Graph(QWidget):
    def __init__(self, parent: QWidget, database_conn: Database, month_ls: List[QPushButton], year: int): # WILL ADD CATEGORY OPTION LATER
        # WILL ADD TREND LINE LATER
        super().__init__(parent=parent)
        self.setGeometry(QRect(0, 510, 680, 390))
        self.setObjectName("Net_Income_Bar_Graph")
        self.transaction_data = database_conn.app_data['transaction_data']['start_data']
        self.year = year
        self.month_abbrv = [abbr.text() for abbr in month_ls]
        self.month_list = [rvar.MONTHS_SHORT_DICT[month] for month in self.month_abbrv]
        # SORT DATA BY MONTH
        self.month_list = sorted(self.month_list, key=lambda x: rvar.month_dict[x])
        self.month_abbrv.sort(key=lambda x: rvar.month_dict[rvar.MONTHS_SHORT_DICT[x]])
            # COLLECT DATA FOR BARGRAPH
        self.data: List[Decimal] = self.collect_data()
        self.month_set = QBarSet("Month")
        for value in self.data:
            self.month_set.append(value)
        self.month_set.setBrush(Qt.GlobalColor.cyan)
        self.month_set.setColor(Qt.GlobalColor.cyan)
        # ADD BARSET TO BARSERIES
        self.bar_series = QBarSeries()
        self.bar_series.append(self.month_set)
        # CREATE CHART AND CUSTOMIZE
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.chart.addSeries(self.bar_series)
        self.chart.setTitle('Net Income Bar Chart')
        self.chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)
        self.chart.legend().setMarkerShape(QLegend.MarkerShape.MarkerShapeCircle)
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.month_abbrv)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.bar_series.attachAxis(self.axis_x)
        self.axis_y = QValueAxis()
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.bar_series.attachAxis(self.axis_y)
        min_amount = 0
        max_amount = (Decimal(1000.00) + max(self.data))
        self.axis_y.setRange(min_amount, max_amount)
        # ADD CHART TO CHARTVIEW
        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        # Create a layout to hold both the chart and the label
        layout = QVBoxLayout()
        layout.addWidget(chart_view)
        self.setLayout(layout)
        
    def collect_data(self) -> List[Decimal]:
        expense_data: List[Decimal] = [sum([trans.amount for trans in self.transaction_data if trans.month == rvar.month_dict[month] and trans.accounting_type == 'Debit' and trans.year == self.year]) for month in self.month_list]
        income_data: List[Decimal] = [sum([trans.amount for trans in self.transaction_data if trans.month == rvar.month_dict[month] and trans.accounting_type == 'Credit' and trans.year == self.year]) for month in self.month_list]
        data: List[Decimal] = np.subtract(income_data, expense_data)
        return data
    
    def chart_update(self, month_ls: List[QPushButton], year: int):
        self.year = year
        self.bar_series.clear()
        self.month_abbrv = [abbr.text() for abbr in month_ls]
        self.month_list = [rvar.MONTHS_SHORT_DICT[month] for month in self.month_abbrv]
        # SORT DATA BY MONTH
        self.month_list = sorted(self.month_list, key=lambda x: rvar.month_dict[x])
        self.month_abbrv.sort(key=lambda x: rvar.month_dict[rvar.MONTHS_SHORT_DICT[x]])
        self.axis_x.clear()
        self.axis_x.append(self.month_abbrv)
        # COLLECT DATA FOR BARGRAPH
        self.data: List[Decimal] = self.collect_data()
        month_set = QBarSet("Month")
        for value in self.data:
            month_set.append(value)
        month_set.setBrush(Qt.GlobalColor.cyan)
        month_set.setColor(Qt.GlobalColor.cyan)        
        # ADD BARSET TO BARSERIES
        self.bar_series.append(month_set)
        min_amount = 0
        max_amount = (Decimal(1000.00) + max(self.data))
        self.axis_y.setRange(min_amount, max_amount)
