########  Python IMPORTs  ############################################################
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget
from PyQt6.QtCharts import QChart, QChartView, QLegend, QBarCategoryAxis, QLineSeries, QValueAxis
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt, QRect, QPointF
########################################################################################

##########  Created files IMPORTS  #####################################################
########################################################################################

# class ChartView(QChartView):
#     def __init__(self, chart: QChart):
#         super().__init__(chart)
#         self.setMouseTracking(True)
#         self.point_text = ""
    
#     def mouseMoveEvent(self, event):
#         pos = event.pos()
#         chart = self.chart()
#         found_point = None
#         # point = QPointF()
#         # point.
#         if chart:
#             for series in chart.series():
#                 for point in series.points():
#                     point_pos = chart.mapToPosition(point)
#                     if (point_pos - pos).manhattanLength() < 5:  # Set a tolerance for the hover area
#                         found_point = point
#                         break
                    
#                     # if point_pos.toPoint() == pos.toPointF():
#                     #     QToolTip.showText(event.globalPos(), f"({point.x()}, {point.y()})")

#         if found_point:
#             self.point_text = f"({found_point.x()}, {found_point.y()})"
#         else:
#             self.point_text = ""

#     def viewportEvent(self, event):
#         if self.point_text:
#             QToolTip.showText(event.screenPos(), self.point_text)
#             return True  # Event has been handled
#         else:
#             QToolTip.hideText()
#             return False  # Event has been handled


class MB_LineChart(QWidget):
    def __init__(self, parent, budget_table: QTableWidget, year: str):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__(parent=parent)
        self.setGeometry(QRect(0, 640, 1030, 440))
        self.setObjectName("MB_Line_chart")
        
        col_len = budget_table.columnCount()
        
        # This is just for testing purposes
        
        self.months_rng = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        self.qline = QLineSeries()
        self.qline.setName("Expected Funds")
        self.qline.setBrush(Qt.GlobalColor.green)
        self.qline.setColor(Qt.GlobalColor.green)
        
        max_amount = 0
        min_amount = 0
        
        col_query = col_len - 1
        
        for row in range(len(self.months_rng)):
                
            series_item = budget_table.item(row, col_query)
            # For Debugging purposes
            # print(f"Series Item text Before Change: {series_item.text()}")
            data_point = series_item.text().replace('$', '')
            data_point = float(data_point)
            # For Debugging purposes
            # print('Data point results 1: ')
            # print(data_point)
            
            data_point = float("{:.2f}".format(data_point))
            # For Debugging purposes
            # print('Data point results 2: ')
            # print(data_point)
            
            # For Debugging purposes
            # print(f"Altered column: {col_query}")
            # print(f"Altered row: {row} ")
        
            self.qline.append(QPointF(row, data_point))
            
            if row == 0:
                min_amount = data_point
            
            if data_point < min_amount:
                min_amount = data_point
                    
            if data_point > max_amount:
                max_amount = data_point
        
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        self.chart.addSeries(self.qline)
        
        # points = self.qline.points()
        # for point in points:
        #     point_pos = self.chart.mapToPosition(point)
        #     if point_pos. == pos.toPoint():
        #         QToolTip.showText(event.globalPos(), f"({point.x()}, {point.y()})")
        
        self.chart.setTitle(f"Expected Finance for the Year {year}")
                    
        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self.months_rng)
        self.chart.addAxis(self._axis_x, Qt.AlignmentFlag.AlignBottom)
        
        self.qline.attachAxis(self._axis_x)

        self._axis_x.setRange("Jan", "Dec")
        
        self._axis_y = QValueAxis()
        self.chart.addAxis(self._axis_y, Qt.AlignmentFlag.AlignLeft)
        
        self.qline.attachAxis(self._axis_y)

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
        layout.addWidget(chart_view)

        self.setLayout(layout)
                
    def update_data(self, budget_table: QTableWidget):
        # Clear the current data
        self.qline.clear()
        max_amount = 0
        min_amount = 0
        
        col_len = budget_table.columnCount()
        col_query = col_len - 1
        
        for row in range(len(self.months_rng)):
                
            series_item = budget_table.item(row, col_query)
            # For Debugging purposes
            print(f"Series Item text Before Change: {series_item.text()}")
            data_point = series_item.text().replace('$', '')
            data_point = float(data_point)
            # For Debugging purposes
            print('Data point results 1: ')
            print(data_point)
            
            data_point = float("{:.2f}".format(data_point))
            # For Debugging purposes
            print('Data point results 2: ')
            print(data_point)
            
            # For Debugging purposes
            print(f"Altered column: {col_query}")
            print(f"Altered row: {row} ")
        
            self.qline.append(QPointF(row, data_point))
                    
            if row == 0:
                min_amount = data_point
            
            if data_point < min_amount:
                min_amount = data_point
                    
            if data_point > max_amount:
                max_amount = data_point
        
        # Needs to be changed
        if min_amount <= 200:
            min_amount = 0
        else:
            min_amount -= 200
        
        max_amount += 100
        self._axis_y.setRange(min_amount, max_amount)
