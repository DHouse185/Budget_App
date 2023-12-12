########  Python IMPORTs  ############################################################
import typing
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox
from PyQt6.QtCharts import QChart, QChartView, QLegend, QBarCategoryAxis, QLineSeries, QValueAxis
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt, QRect, QPointF, QSize
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
# from pages.dashboard import Dashboard
########################################################################################

class Portfolio_LineChart(QWidget):
    def __init__(self, parent, dict: typing.Dict, year: str):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__(parent=parent)
        self.setGeometry(QRect(10, 820, 930, 680))
        self.setObjectName("Portfolio_Line_chart")
        
        self.account_dict = dict
        self.year = year
        
        self.account_comboBox = QComboBox(parent=self)
        self.account_comboBox.setGeometry(QRect(250, 5, 300, 45))
        self.account_comboBox.setMaximumSize(QSize(300, 45))
        self.account_comboBox.setObjectName("account_comboBox")
        
        self.name_ls = list()
                
        for account in self.account_dict.values():
            name = account['name']
                        
            self.name_ls.append(name)
        
        self.account_comboBox.addItems(self.name_ls)
        
        # This is just for testing purposes
        
        self.months_rng = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        self.account_name_box = self.account_comboBox.currentText()
        
        for account in self.account_dict.values():
            if account['name'] == self.account_name_box:
                self.account_name = account['query_name']
        
        self.qline_norm = QLineSeries()
        self.qline_norm.setName("Portfolio Chart")
        self.qline_norm.setBrush(Qt.GlobalColor.green)
        self.qline_norm.setColor(Qt.GlobalColor.green)
        
        self.qline_expected = QLineSeries()
        self.qline_expected.setName("Portfolio Expected Chart")
        self.qline_expected.setBrush(Qt.GlobalColor.magenta)
        self.qline_expected.setColor(Qt.GlobalColor.magenta)
        
        max_amount = 0
        min_amount = 0
                
        for point, value in enumerate(self.account_dict[self.account_name]['year'][self.year]['unfiltered_data']):
                
            # For Debugging purposes
            print(f"Series point Before Change: {value[0]}")
            print(f"Series value Before Change: {value[1]}")
            
            value_ad = float("{:.2f}".format(value[1]))
            
            # For Debugging purposes
            print(f'Data point value after format: {value_ad}')
                    
            self.qline_norm.append(QPointF(value[0], value_ad))
            
            if value[0] == 0 or point == 0:
                min_amount = value_ad
            
            if value_ad < min_amount:
                min_amount = value_ad
                    
            if value_ad > max_amount:
                max_amount = value_ad
                
        for point, value in enumerate(self.account_dict[self.account_name]['year'][self.year]['expected_data']):
            
            if point == 0 and value[0] != 0:
                value_ex_start = self.account_dict[self.account_name]['year'][self.year]['unfiltered_data'][-1]
                
                # For Debugging purposes
                print(f"Series Expected point 0 Before Change: {value_ex_start[0]}")
                print(f"Series Expected value 0 Before Change: {value_ex_start[1]}")
                
                value_ex_start_num = float("{:.2f}".format(value_ex_start[1]))
                
                # For Debugging purposes
                print(f'Data point Expected value 0 after format: {value_ex_start_num}')
                        
                self.qline_expected.append(QPointF(value_ex_start[0], value_ex_start_num))
                            
                if value_ex_start_num < min_amount:
                    min_amount = value_ex_start_num
                        
                if value_ex_start_num > max_amount:
                    max_amount = value_ex_start_num
                    
            # For Debugging purposes
            print(f"Series Expected point Before Change: {value[0]}")
            print(f"Series Expected value Before Change: {value[1]}")
            
            value_ad_ex = float("{:.2f}".format(value[1]))
            
            # For Debugging purposes
            print(f'Data point Expected value after format: {value_ad_ex}')
                    
            self.qline_expected.append(QPointF(value[0], value_ad_ex))
                        
            if value_ad_ex < min_amount:
                min_amount = value_ad_ex
                    
            if value_ad_ex > max_amount:
                max_amount = value_ad_ex
        
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.chart.addSeries(self.qline_norm)
        self.chart.addSeries(self.qline_expected)
        
        self.chart.setTitle(f"{self.account_name_box} for Year {self.year}")
                    
        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.months_rng)
        self.chart.addAxis(self._axis_x, Qt.AlignmentFlag.AlignBottom)
        
        self.qline_norm.attachAxis(self._axis_x)
        self.qline_expected.attachAxis(self._axis_x)

        self._axis_x.setRange("Jan", "Dec")
        
        self._axis_y = QValueAxis()
        self.chart.addAxis(self._axis_y, Qt.AlignmentFlag.AlignLeft)
        
        self.qline_norm.attachAxis(self._axis_y)
        self.qline_expected.attachAxis(self._axis_y)

        # Needs to be changed
        min_amount -= 100
        
        max_amount += 100
        self._axis_y.setRange(min_amount, max_amount)
        
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)
        self.chart.legend().setMarkerShape(QLegend.MarkerShape.MarkerShapeCircle)

        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Create a layout to hold both the chart and the label
        layout = QVBoxLayout()
        layout.addWidget(self.account_comboBox)
        layout.addWidget(chart_view)

        self.setLayout(layout)
        
        self.account_comboBox.currentTextChanged.connect(self.change_account)
                
    def change_account(self, text: str):
        # Clear the current data
        self.qline_norm.clear()
        self.qline_expected.clear()
        max_amount = 0
        min_amount = 0
        
        for account in self.account_dict.values():
            if account['name'] == text:
                self.account_name = account['query_name']
        
        for point, value in enumerate(self.account_dict[self.account_name]['year'][self.year]['unfiltered_data']):
                
            # For Debugging purposes
            print(f"Series point Before Change: {value[0]}")
            print(f"Series value Before Change: {value[1]}")
            
            value_ad = float("{:.2f}".format(value[1]))
            
            # For Debugging purposes
            print(f'Data point value after format: {value_ad}')
                    
            self.qline_norm.append(QPointF(value[0], value_ad))
            
            if value[0] == 0 or point == 0:
                min_amount = value_ad
            
            if value_ad < min_amount:
                min_amount = value_ad
                    
            if value_ad > max_amount:
                max_amount = value_ad
                
        for point, value in enumerate(self.account_dict[self.account_name]['year'][self.year]['expected_data']):
            
            if point == 0 and value[0] != 0:
                value_ex_start = self.account_dict[self.account_name]['year'][self.year]['unfiltered_data'][-1]
                
                # For Debugging purposes
                print(f"Series Expected point 0 Before Change: {value_ex_start[0]}")
                print(f"Series Expected value 0 Before Change: {value_ex_start[1]}")
                
                value_ex_start_num = float("{:.2f}".format(value_ex_start[1]))
                
                # For Debugging purposes
                print(f'Data point Expected value 0 after format: {value_ex_start_num}')
                        
                self.qline_expected.append(QPointF(value_ex_start[0], value_ex_start_num))
                            
                if value_ex_start_num < min_amount:
                    min_amount = value_ex_start_num
                        
                if value_ex_start_num > max_amount:
                    max_amount = value_ex_start_num
                    
            # For Debugging purposes
            print(f"Series Expected point Before Change: {value[0]}")
            print(f"Series Expected value Before Change: {value[1]}")
            
            value_ad_ex = float("{:.2f}".format(value[1]))
            
            # For Debugging purposes
            print(f'Data point Expected value after format: {value_ad_ex}')
                    
            self.qline_expected.append(QPointF(value[0], value_ad_ex))
                        
            if value_ad_ex < min_amount:
                min_amount = value_ad_ex
                    
            if value_ad_ex > max_amount:
                max_amount = value_ad_ex
        
        # Needs to be changed
        if min_amount <= 200:
            min_amount = 0
        else:
            min_amount -= 200
        
        max_amount += 100
        self._axis_y.setRange(min_amount, max_amount)
