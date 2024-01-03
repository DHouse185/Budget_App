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
from root.pages.components.ui.expense_planning import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################
        
class Expense_planning(Ui_Form):
    def __init__(self, parent, x_axis_names):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> top_5_expense
        super().__init__()
        self.expense_plan = QWidget(parent=parent)
        self.setupUi(self.expense_plan)
        self.expense_plan.setGeometry(QRect(0, 1460, 1900, 650))
        
        self.row_location = 1
        self.min_size = 400
        self._valid_float = QRegularExpressionValidator(QRegularExpression(r'^[+-]?\d*\.?\d+$'))
        
        self.expenses_dict = {
            "cost" : list(),
            "time_period" : list(),
            "name" : list()
        }
        
        self.checkbox_ls = list()
        #######################################
        self.confirm_pushButton.setEnabled(False) # Make true in parent widget function
        
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
        self._axis_x.setLabelsAngle(45)
        self._axis_x.setLabelsFont(QFont("Nirmala UI", 5, 1))
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

        chart_view = QChartView(self.chart, self.expense_plan)
        chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        chart_view.setGeometry(QRect(1000, 60, 881, 481))
        
        ##################################################################################
        # Signals                                                                        #
        ##################################################################################
        self.add_pushButton.clicked.connect(lambda: self.add_expense())
        self.minus_pushButton.clicked.connect(self.remove_expense)
        # self.confirm_pushButton.clicked.connect(self.confirm)    
    
    def remove_expense(self):
        removal_list = list()
        print(f"checkbox list: {self.checkbox_ls}")
        
        for expense in self.checkbox_ls:
            print(f"expense beg: {expense}")
            print(f"expense checked?: {expense[1].isChecked()}")
            if isinstance(expense[1], QCheckBox) and expense[1].isChecked():
                # parent_wid = expense[1].parent()
                
                # row_2 = self.grid_frame.indexOf(parent_wid) // self.grid_frame.columnCount()
                # col_2 = self.grid_frame.indexOf(parent_wid) % self.grid_frame.columnCount()
                                    
                for col_ in range(self.gridLayout.columnCount()):
                    del_widget_item = self.gridLayout.itemAtPosition(expense[0], col_)
                    if del_widget_item:
                        del_widget = del_widget_item.widget()
                        if del_widget:
                            self.gridLayout.removeWidget(del_widget)
                            del_widget.deleteLater()
                
                removal_list.append(expense)            
                
                name = [item for item in self.expenses_dict["name"] if item[0] == expense[0]]
                if name:
                    self.expenses_dict["name"].remove(name[0])
                    
                tp_dateEdit = [item for item in self.expenses_dict["time_period"] if item[0] == expense[0]]
                if tp_dateEdit:
                    self.expenses_dict["time_period"].remove(tp_dateEdit[0])
                    
                cost = [item for item in self.expenses_dict["cost"] if item[0] == expense[0]]
                if cost:
                    self.expenses_dict["cost"].remove(cost[0])
                                
        for removal in removal_list:
            self.checkbox_ls.remove(removal)
        
    def add_expense(self):
        column_location = 0
        row = self.row_location
        
        frame_1 = QFrame()
        frame_1.setStyleSheet("border: 1px solid #000000;")
        frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        frame_1.setFrameShadow(QFrame.Shadow.Raised)
        frame_1.setObjectName("frame_1")
        frame_1.setFixedSize(QSize(230, 50))
        frame_1_layout = QHBoxLayout(frame_1)
        
        checkbox = QCheckBox()
        checkbox.setGeometry(QRect(5, 5, 10, 40))
        checkbox.setObjectName("checkbox")
        checkbox.setStyleSheet("border: none;")
        frame_1_layout.addWidget(checkbox)
        
        self.checkbox_ls.append((row, checkbox))
        
        expense_name_lineEdit = QLineEdit()
        expense_name_lineEdit.setGeometry(QRect(20, 5, 200, 40))
        expense_name_lineEdit.setObjectName("expense_name_lineEdit")
        frame_1_layout.addWidget(expense_name_lineEdit)
        
        expense_name_lineEdit.returnPressed.connect(lambda: self.on_enter_pressed(frame_1, expense_name_lineEdit, row))
                
        self.gridLayout.addWidget(frame_1, self.row_location, column_location)
        column_location += 1
        
        frame_2 = QFrame()
        frame_2.setStyleSheet("border: 1px solid #000000;")
        frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        frame_2.setFrameShadow(QFrame.Shadow.Raised)
        frame_2.setObjectName("frame_2")
        frame_2.setFixedSize(QSize(230, 50))
        frame_2_layout = QHBoxLayout(frame_2)
        
        expense_cost_lineEdit = QLineEdit()
        expense_cost_lineEdit.setGeometry(QRect(10, 5, 210, 40))
        expense_cost_lineEdit.setObjectName("expense_cost_lineEdit")
        expense_cost_lineEdit.setValidator(self._valid_float)
        
        frame_2_layout.addWidget(expense_cost_lineEdit)
        
        self.gridLayout.addWidget(frame_2, self.row_location, column_location)
        column_location += 1
                                               
        cost_label = QLabel()
        cost_label.setFixedSize(QSize(230, 50))
        cost_label.setObjectName("cost_label")
        cost_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
                                 "color: #7300ff;\n"
                                 "border: 1px solid #000000;")
        cost_label.setText("$ - -")
        cost_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.gridLayout.addWidget(cost_label, self.row_location, column_location)
        column_location += 1
        current_year = datetime.datetime.now().year
        time_period_dateedit = QDateEdit()
        time_period_dateedit.setFixedSize(QSize(230, 50))
        time_period_dateedit.setObjectName("time_period_dateedit")
        time_period_dateedit.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
                                    "border: 1px solid #000000;")
        time_period_dateedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        time_period_dateedit.setMaximumDate(QDate(current_year, 12, 31))
        time_period_dateedit.setMinimumDate(QDate(current_year, 1, 1))
        time_period_dateedit.setDisplayFormat('MMM dd')
        self.expenses_dict["time_period"].append((row, time_period_dateedit))
        
        self.gridLayout.addWidget(time_period_dateedit, self.row_location, column_location)
        
        expense_cost_lineEdit.returnPressed.connect(lambda: self.on_enter_cost(frame_2, expense_cost_lineEdit, cost_label, row))
        
        self.row_location += 1
        
        if self.row_location > 7:
            self.min_size += 50
            self.scrollAreaWidgetContents.setMinimumSize(QSize(0, self.min_size))

        # After adding all the widgets, set the layout on the scroll area's widget content
        
    def on_enter_pressed(self, frame: QFrame, line_e: QLineEdit, row: int):
        # This function will be called when Enter is pressed in the QLineEdit
        # print("Enter key pressed")
        
        text = line_e.text()
        expense_name_label = QLabel(text=text)  # Set the parent of QLabel
        expense_name_label.setGeometry(QRect(20, 5, 200, 40))
        expense_name_label.setObjectName("expense_name_label")
        expense_name_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
                                        "color: #7300ff;\n"
                                        "border: 0;")  # Set border to 0
        expense_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add QLabel to the layout of the frame
        layout = frame.layout()
        if layout:
            layout.addWidget(expense_name_label)
        
        self.expenses_dict["name"].append((row, text))
            
        layout.removeWidget(line_e)
        
        line_e.deleteLater()
        
    def on_enter_cost(self, frame: QFrame, line_e: QLineEdit, cost_label: QLabel, row: int):
        # This function will be called when Enter is pressed in the QLineEdit
        
        text = line_e.text()
        text = "{:.2f}".format(float(text))
        cost_label.setText(f"$ {text}")
        
        cost_exist = [item for item in self.expenses_dict["cost"] if item[0] == row]
        
        if cost_exist == []:
            self.expenses_dict["cost"].append((row, float(text)))
        
        elif cost_exist != []:
            self.expenses_dict["cost"].remove(cost_exist[0])
            self.expenses_dict["cost"].append((row, float(text)))
        
                                               
    def fill_chart(self, data_points):
        # incomplete_cost = [(i, item) for i, item in enumerate(self.expenses_dict['cost']) if item[0] not in [x[0] for x in self.expenses_dict['time_period']]]
        incomplete_date = [(i, item) for i, item in enumerate(self.expenses_dict['time_period']) if item[0] not in [x[0] for x in self.expenses_dict['cost']]]
        
        if incomplete_date:
            # Display a QMessageBox with information about incomplete data
            message = "Incomplete data found!\n\Please fill in the missing data\n"
            QMessageBox.information(self.expense_plan, "Incomplete Data", message)
        else:
            expense_data_points = data_points.copy()
            time_period_list = self.expenses_dict['time_period']
            time_period_list = sorted(time_period_list, key=lambda x: x[0])
            cost_list = self.expenses_dict['cost']
            cost_list = sorted(cost_list, key=lambda x: x[0])
            # purchase_date_list = list()
            
            for index, cost_time in enumerate(time_period_list):
                cost_time_datetime = cost_time[1].dateTime()
                cost_time_datetime = cost_time_datetime.toPyDateTime()
                cost_time_week_number = cost_time_datetime.isocalendar()[1]
                data_point_index = int((cost_time_week_number - 1) / 2) # making it an integer keeps a two week period the same x-intercept point.
                for index_2, savings in enumerate(expense_data_points):
                    savings -= cost_list[index][1]
                    expense_data_points[index_2] = savings if index_2 >= data_point_index else expense_data_points[index_2]
                    
            self.new_year_save_amount_lable.setText(f'${round(expense_data_points[-1], 2)}')
            
            
            self.qline_norm.clear()
            max_amount = 0
            min_amount = 0

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
            
            self.expense_data_points = expense_data_points
