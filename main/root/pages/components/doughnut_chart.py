##########  Python IMPORTs  ############################################################
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
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice, QLegend
from PyQt6.QtGui import QAction, QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
# from pages.dashboard import Dashboard
########################################################################################

class Doughnut(QWidget):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__(parent=parent)
        self.setGeometry(QRect(680, 130, 540, 540))
        self.setObjectName("doughnut_chart")
        
        self.database = database
        self.transaction_df = self.database.start_up_transaction_data
        
        self.total_spent = self.transaction_df.loc[self.transaction_df['Transaction Type'] == 'Expense', 'Amount'].sum() 
        self.accounts = self.database.query_column('account_test', 'account')
        self.accounts = self.accounts
        
        self.series = QPieSeries()
        color_palatte = [Qt.GlobalColor.darkGreen, Qt.GlobalColor.green, Qt.GlobalColor.blue, Qt.GlobalColor.darkBlue, 
                         Qt.GlobalColor.cyan, Qt.GlobalColor.darkCyan, Qt.GlobalColor.gray, 
                         Qt.GlobalColor.lightGray, Qt.GlobalColor.yellow, Qt.GlobalColor.darkYellow,]
        palette_num = 0
        # Set the hole size
        self.series.setHoleSize(0.15)
        slices = list()
        account_spent_list = list()
        for account in self.accounts:
            # print(f'account: {account[0]}')
            account_spent = self.transaction_df.loc[(self.transaction_df['Account'] == f'{account[0]}') & (self.transaction_df['Transaction Type'] == 'Expense'), 'Amount'].sum() 
            try:
                spent_ratio = round((account_spent / self.total_spent), 2)
                slice_ = QPieSlice(f'{account[0]}', spent_ratio)
                slice_.setExploded()
                slice_.setLabelVisible()
                slice_.setPen(QPen(Qt.GlobalColor.darkGreen, 2))
                # slice_.setLabelArmLengthFactor(0.2)
                
                if palette_num > 9:
                    palette_num = 0
                slice_.setBrush(color_palatte[palette_num])
                palette_num += 1
                slices.append(slice_)
                account_spent_list.append(account_spent)
                self.series.append(slice_)      

            except ZeroDivisionError:
                slice_ = QPieSlice(f'{account[0]}', 0)
                slice_.setExploded()
                slice_.setLabelVisible()
                slice_.setPen(QPen(Qt.darkGreen, 2))
                # slice_.setLabelArmLengthFactor(0.2)
                
                if palette_num > 9:
                    palette_num = 0
                slice_.setBrush(color_palatte[palette_num])
                palette_num += 1
                slices.append(slice_)
                account_spent_list.append(account_spent)
                self.series.append(slice_)
                

        # label styling
        for idx, slice_ in enumerate(slices):
            if slice_.percentage() > 0.05:
                slice_.setLabelPosition(QPieSlice.LabelPosition.LabelInsideHorizontal)
                label = f"<p align='center'>{f'{slice_.label()}'}<br>{round(slice_.percentage()*100, 2)}%<br>${account_spent_list[idx]}</p>"
            elif slice_.percentage() <= 0.01:
                label = f"<p align='center'>{f'{slice_.label()}'} ~1%</p>"
            else:
                label = f"<p align='center'>{f'{slice_.label()}'}<br>{round(slice_.percentage()*100, 2)}%</p>"
            slice_.setLabel(label)
            
                
        chart = QChart()
        # chart.setBackgroundBrush(QColor(30, 80, 30, 255))
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        chart.addSeries(self.series)
        chart.setTitle("Total Spend By Account")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)
        chart.legend().setMarkerShape(QLegend.MarkerShape.MarkerShapeCircle)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Create a layout to hold both the chart and the label
        layout = QVBoxLayout()
        layout.addWidget(chart_view)

        self.setLayout(layout)
