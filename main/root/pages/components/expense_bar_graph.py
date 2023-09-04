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
                             QLabel)
from PyQt6.QtCharts import (QBarCategoryAxis, 
                            QBarSeries, 
                            QBarSet, 
                            QChart, 
                            QChartView, 
                            QLineSeries, 
                            QValueAxis)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_vriables as rvar
# from pages.dashboard import Dashboard
########################################################################################

class Expense_Bar_Graph:
    def __init__(self, parent, database_conn):
        super().__init__()
        
        self.month_set = QBarSet("Month")
        
        self.month_set.append()
        
        self.bar_series = QBarSeries()
        self.bar_series.append(self.month_set)
        
        self.chart = QChart()
        self.chart.addSeries(self.bar_series)
        self.chart.setTitle