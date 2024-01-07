##########  Python IMPORTs  ############################################################
import pandas as pd
from typing import List
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice, QLegend
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.models import Account
# from pages.dashboard import Dashboard
########################################################################################

class Doughnut(QWidget):
    def __init__(self, parent, database: Database, year: int, month_ls: List[QPushButton]):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__(parent=parent)
        self.setGeometry(QRect(680, 130, 540, 540))
        self.setObjectName("doughnut_chart")
        
        self.database = database
        self.year = year
        self.month_abbrv = [abbr.text() for abbr in month_ls]
        self.month_list = [rvar.MONTHS_SHORT_DICT[month] for month in self.month_abbrv]
        self.month_list = sorted(self.month_list, key=lambda x: rvar.month_dict[x])
        self.month_num_list = [rvar.month_dict[month_name] for month_name in self.month_list]
        self.transaction_df: pd.DataFrame = self.database.app_data['transaction_dataframe']
        self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        self.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        year_df = self.transaction_df_no_date_idx[self.transaction_df_no_date_idx['Date'].apply(lambda x: x.year == self.year and x.month in self.month_num_list)]
        self.total_spent = year_df.loc[year_df['Transaction Type'] == 'Expense', 'Amount'].sum() if year_df.columns != [] else 0
        self.accounts: List[Account] = [acc.account for acc in self.database.app_data['account']['start_data']]
        
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
            account_spent = year_df.loc[(year_df['Account'] == f'{account}') & (year_df['Transaction Type'] == 'Expense'), 'Amount'].sum() 
            try:
                spent_ratio = round((account_spent / self.total_spent), 2)
                slice_ = QPieSlice(f'{account}', spent_ratio)
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
                slice_ = QPieSlice(f'{account}', 0)
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
                

        # label styling
        for idx, slice_ in enumerate(slices):
            if slice_.percentage() > 0.1:
                slice_.setLabelPosition(QPieSlice.LabelPosition.LabelInsideHorizontal)
                label = f"<p align='center'>{f'{slice_.label()}'}<br>{round(slice_.percentage()*100, 2)}%<br>${account_spent_list[idx]}</p>"
            elif slice_.percentage() <= 0.1 and slice_.percentage() > 0:
                label = f"<p align='center'>{f'{slice_.label()}'} ~1%</p>"
            elif slice_.percentage() == 0:
                label = ''
            else:
                label = f"<p align='center'>{f'{slice_.label()}'}<br>{round(slice_.percentage()*100, 2)}%</p>"
            slice_.setLabel(label)
            
                
        chart = QChart()
        # chart.setBackgroundBrush(QColor(30, 80, 30, 255))
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        chart.addSeries(self.series)
        chart.setTitle("Total Spend By Account")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)
        chart.legend().setMarkerShape(QLegend.MarkerShape.MarkerShapeCircle)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Create a layout to hold both the chart and the label
        layout = QVBoxLayout()
        layout.addWidget(chart_view)

        self.setLayout(layout)
        
    def chart_update(self, year: int, month_ls: List[QPushButton]):
        self.year = year
        self.transaction_df_no_date_idx = self.transaction_df.reset_index()
        self.transaction_df_no_date_idx['Date']= pd.to_datetime(self.transaction_df_no_date_idx['Date'])
        self.month_abbrv = [abbr.text() for abbr in month_ls]
        self.month_list = [rvar.MONTHS_SHORT_DICT[month] for month in self.month_abbrv]
        self.month_list = sorted(self.month_list, key=lambda x: rvar.month_dict[x])
        self.month_num_list = [rvar.month_dict[month_name] for month_name in self.month_list]
        year_df = self.transaction_df_no_date_idx[self.transaction_df_no_date_idx['Date'].apply(lambda x: x.year == self.year and x.month in self.month_num_list)]
        self.total_spent = year_df.loc[year_df['Transaction Type'] == 'Expense', 'Amount'].sum() if year_df.columns != [] else 0
        self.accounts: List[Account] = [acc.account for acc in self.database.app_data['account']['start_data']]
        
        self.series.clear()
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
            account_spent = year_df.loc[(year_df['Account'] == f'{account}') & (year_df['Transaction Type'] == 'Expense'), 'Amount'].sum() 
            try:
                spent_ratio = round((account_spent / self.total_spent), 2)
                slice_ = QPieSlice(f'{account}', spent_ratio)
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
                slice_ = QPieSlice(f'{account}', 0)
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
                

        # label styling
        for idx, slice_ in enumerate(slices):
            if slice_.percentage() > 0.1:
                slice_.setLabelPosition(QPieSlice.LabelPosition.LabelInsideHorizontal)
                label = f"<p align='center'>{f'{slice_.label()}'}<br>{round(slice_.percentage()*100, 2)}%<br>${account_spent_list[idx]}</p>"
                slice_.setLabel(label)
            elif slice_.percentage() <= 0.1 and slice_.percentage() > 0:
                label = f"<p align='center'>{f'{slice_.label()}'} ~1%</p>"
                slice_.setLabel(label)
            elif slice_.percentage() == 0:
                label = ''
                slice_.setLabel(label)
            else:
                label = f"<p align='center'>{f'{slice_.label()}'}<br>{round(slice_.percentage()*100, 2)}%</p>"
                slice_.setLabel(label)
