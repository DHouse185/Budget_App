########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import calendar
import pandas as pd
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow, 
                             QWidget, 
                             QVBoxLayout,
                             QMessageBox, 
                             QStackedWidget, 
                             QWidget,
                             QGridLayout,
                             QLabel)
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice, QLegend, QBarCategoryAxis, QLineSeries, QValueAxis
from PyQt6.QtGui import QAction, QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QRect, QPointF
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
# from pages.dashboard import Dashboard
########################################################################################

class LineChart(QWidget):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__(parent=parent)
        self.setGeometry(QRect(0, 900, 681, 401))
        self.setObjectName("Line_chart")
        
        self.database = database
        self.transaction_df = self.database.start_up_transaction_data
        self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        self.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        
        # This is just for testing purposes
        self.year = 2023
        
        self.months_rng = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.categories = self.database.query_column('category_test', 'category')
        self.line_series_list = list()
        color_palatte = [Qt.GlobalColor.darkGreen, Qt.GlobalColor.darkRed, Qt.GlobalColor.darkBlue, 
                         Qt.GlobalColor.cyan, Qt.GlobalColor.blue, Qt.GlobalColor.gray, 
                         Qt.GlobalColor.lightGray, Qt.GlobalColor.yellow, Qt.GlobalColor.red,
                         Qt.GlobalColor.green, Qt.GlobalColor.darkYellow, Qt.GlobalColor.magenta,
                         Qt.GlobalColor.darkMagenta, Qt.GlobalColor.darkCyan,]
        palette_num = 0
        
        for category in self.categories:
            qline = QLineSeries()
            qline.setName(f"{category[0]}")
            self.line_series_list.append(qline)
            
        # print(f"Line Series List: \n...\n{self.line_series_list}")
        
        max_amount = 0
        min_amount = 0
        
        for idx, month_id in enumerate(rvar.month_dict.values()):
            # Get first day of the month
            date_1 = datetime.datetime(year=int(self.year), month=(month_id), day=1)
            first_date = f"{date_1.strftime('%Y-%m-%d')}"
            
            # Get last day of the month
            months_range = calendar.monthrange(int(self.year), (month_id))
            days_in_month = months_range[1]
            date_2 = datetime.datetime(year=int(self.year), month=(month_id), day=int(days_in_month))
            last_date = f"{date_2.strftime('%Y-%m-%d')}"
            
            for cat_num, line_serie in enumerate(self.line_series_list):
                # print(f"\nself.categories[cat_num]: {self.categories[cat_num]}")
                # print(f"\nself.categories[cat_num][0]: {self.categories[cat_num][0]}")
                # Get earnings
                exp_amount = self.transaction_df_no_date_idx.loc[(self.transaction_df_no_date_idx['Date'] >= first_date) 
                                                                 & (self.transaction_df_no_date_idx['Date'] <= last_date)
                                                                 & (self.transaction_df_no_date_idx['Transaction Type'] == 'Expense')
                                                                 & (self.transaction_df_no_date_idx['Category'] == f'{self.categories[cat_num][0]}'),
                                                                 'Amount'].sum() 
                line_serie.append(QPointF(idx, exp_amount))
                
                if idx == 0 and cat_num == 0:
                    min_amount = exp_amount
                
                if exp_amount < min_amount:
                    min_amount = exp_amount
                       
                if exp_amount > max_amount:
                    max_amount = exp_amount

        print(f"Line Series List: \n...\n{self.line_series_list}")
        
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        
        for line_series in self.line_series_list:
            if palette_num >= 14:
                    palette_num = 0
            line_series.setBrush(color_palatte[palette_num])
            line_series.setColor(color_palatte[palette_num])
            palette_num += 1
            self.chart.addSeries(line_series)
            
        self.chart.setTitle(f"Expense Chart per Category for {self.year}")
        
        # self.cat = list()
        # for cat in self.categories:
        #     self.cat.append(cat[0])
            
        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.months_rng)
        self.chart.addAxis(self._axis_x, Qt.AlignmentFlag.AlignBottom)
        
        for ls in self.line_series_list:
            ls.attachAxis(self._axis_x)

        self._axis_x.setRange("Jan", "Dec")
        
        self._axis_y = QValueAxis()
        self.chart.addAxis(self._axis_y, Qt.AlignmentFlag.AlignLeft)
        
        for ls2 in self.line_series_list:
            ls2.attachAxis(self._axis_y)

        # Needs to be changed
        if min_amount <= 50:
            min_amount = 0
        else:
            min_amount -= 50
        
        max_amount += 100
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
                