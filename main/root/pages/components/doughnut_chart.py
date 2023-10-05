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
        self.setStyleSheet(self.widget_style())
        
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
            print(f'account: {account[0]}')
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

    def widget_style(self):
        style = """QWidget {  
                 background-color: #2c2c2c;  
                 color: #ffffff;  
                 border: none;  
                 font: 11pt \ Nirmala UI\ ;  
         }  
         QWidget#side_menu {  
             background-color: #4e5564;  
             color: #ffffff;  
             border: 1px solid #4e5564;  
             border-radius: 16px;  
             font: 14pt \ Nirmala UI\ ;  
         }  
         QLabel#Dashboard_Title {  
             background-color: none;  
             color: #ffffff;  
             border: none;  
             font: 20pt \ Nirmala UI\ ;  
         }  
         QLabel#Eat_Out_Image {  
             background-image: url(:/images/pngaaa.com-2384833.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QLabel#Grocery_Image {  
             background-image: url(:/images/pngaaa.com-2138453.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QLabel#Transportation_Image {  
             background-image: url(:/images/pngaaa.com-2182093.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QLabel#Free_Expense_Image {  
             background-image: url(:/images/pngaaa.com-1261106.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QLabel#Bills_Image {  
             background-image: url(:/images/pngaaa.com-1433501.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QLabel#Investment_Image {  
             background-image: url(:/images/pngaaa.com-3584133.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QLabel#Support_Image {  
             background-image: url(:/images/pngaaa.com-2914571.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QLabel#Goal_Image {  
             background-image: url(:/images/pngaaa.com-848656.png);  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QPushButton {  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QPushButton:hover {  
             background-color: #5a5a5a;  
             border: 1px solid #5a5a5a;  
         }  
         QPushButton#side_menu_button:hover {  
             background-image: url(:/button_image/Burger_button_hover.png);  
             background-color: #5a5a5a;  
             border: 1px solid #5a5a5a;  
         }  
         QPushButton#side_menu_button:pressed {  
             background-image: url(:/button_image/Burger_button_click.png);  
             background-color: #5a5a5a;  
             border: 1px solid #5a5a5a;  
         }  
         QPushButton#remove_button_watchlist {  
             background-color: #ff0000;  
             border: 1px solid #ffffff;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QPushButton#remove_button_watchlist:hover {  
             background-color: #ff6c6c;  
             border: 1px solid #ffffff;  
         }  
         QPushButton#remove_button_watchlist:pressed {  
             background-color: #aa0000;  
             border: 1px solid #ffffff;  
         }  
         QPushButton#Add_strategy {  
             background-color: #00ad0e;  
             border: 1px solid #ffffff;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QPushButton#Add_strategy:hover {  
             background-color: #67ff74;  
             border: 1px solid #ffffff;  
         }  
         QPushButton#Add_strategy:pressed {  
             background-color: #006408;  
             border: 1px solid #a3a3a3;  
         }  
         QPushButton#Activation {  
             background-color: #00ad0e;  
             border: 1px solid #ffffff;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QPushButton#Activation:hover {  
             background-color: #67ff74;  
             border: 1px solid #ffffff;  
         }  
         QPushButton#Activation:pressed {  
             background-color: #006408;  
             border: 1px solid #a3a3a3;  
         }  
         QPushButton#Blue_button {  
             background-color: #0003bb;  
             border: 1px solid #ffffff;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QPushButton#Blue_button:hover {  
             background-color: #4446d1;  
             border: 1px solid #ffffff;  
         }  
         QPushButton#Blue_button:pressed {  
             background-color: #000277;  
             border: 1px solid #a3a3a3;  
         }  
         QPushButton#Yellow_button {  
             background-color: #a5bd1e;  
             border: 1px solid #ffffff;  
             border-radius: 4px;  
             color: #ffffff;  
             padding: 5px;  
         }  
         QPushButton#Yellow_button:hover {  
             background-color: #e5ff54;  
             border: 1px solid #ffffff;  
         }  
         QPushButton#Yellow_button:pressed {  
             background-color: #81960f;  
             border: 1px solid #a3a3a3;  
         }  
         QCheckBox {  
             color: #ffffff;  
         }  
         QLineEdit {  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             color: #ffffff;  
             padding: 5px;  
             border-color: #ffffff;  
             border-radius: 6px;  
         }  
         QTextEdit {  
             background-color: #4d4d4d;  
             border: 1px solid #4d4d4d;  
             color: #ffffff;  
             padding: 5px;  
             border-color: #ffffff;  
             border-radius: 20px;  
         }  
         QProgressBar {  
             border: 1px solid #444444;  
             border-radius: 7px;  
             background-color: #2e2e2e;  
             text-align: center;  
             font-size: 10pt;  
             color: white;  
         }  
         QProgressBar::chunk {  
             background-color: #3a3a3a;  
             width: 5px;  
         }  
         QScrollBar:vertical {  
             border: none;  
             background-color: #3a3a3a;  
             width: 10px;  
             margin: 16px 0 16px 0;  
         }  
         QScrollBar::handle:vertical {  
             background-color: #444444;  
             border-radius: 5px;  
         }  
         QScrollBar:horizontal {  
             border: none;  
             background-color: #3a3a3a;  
             height: 10px;  
             margin: 0px 16px 0 16px;  
         }  
         QScrollBar::handle:horizontal {  
             background-color: #444444;  
             border-radius: 5px;  
         }  
         QTabWidget {  
             background-color: #2e2e2e;  
             border: none;  
         }  
         QTabBar::tab {  
             background-color: #2e2e2e;  
             color: #b1b1b1;  
             padding: 8px 20px;  
             border-top-left-radius: 5px;  
             border-top-right-radius: 5px;  
             border: none;  
         }  
         QTabBar::tab:selected, QTabBar::tab:hover {  
             background-color: #3a3a3a;  
             color: white;  
         }"""
        
        return style
