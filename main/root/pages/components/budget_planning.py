##########  Python IMPORTs  ############################################################
from pathlib import Path
import os
import csv
from decimal import Decimal
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow, 
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
from PyQt6.QtGui import QAction, QRegularExpressionValidator
from PyQt6.QtCore import Qt, QRect, QSize, QRegularExpression
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.pages.components.ui.budget_planning_plan_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class _Window(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, position: QWidget, name: str = 'Window'):
        super().__init__()
        # Create new widget for popup window
        self.setObjectName("_Window")
        self.resize(500, 300)
        self.setWindowTitle(f"{name}")
        # self.pop_window.setStyleSheet(Path(r_var.DARK_MODE).read_text())
        self.setGeometry(QRect(position.x(), position.y() + 500, 500, 300))
        # self.setStyleSheet(rvar.APP_STYLE)
        # Add a widget to this pop_up window
        self.popup_widget = QWidget(self)
        self.popup_widget.setObjectName("pop_up_widget")
        self.popup_widget.setGeometry(QRect(10, 1, 490, 290))
        # Give it a vertical layout
        self.vertical_pop_up = QVBoxLayout(self.popup_widget)
        self.vertical_pop_up.setObjectName("Vertical_Layout_popup_window")
        self.vertical_pop_up.setSpacing(0)
        # Now add a grid to the Vertical layout
        self.grid_frame = QGridLayout()
        self.grid_frame.setObjectName("Grid_frame_popup")
        self.grid_frame.setSpacing(5)
        self.vertical_pop_up.addLayout(self.grid_frame)
        self.vertical_pop_up.setAlignment(Qt.AlignmentFlag.AlignTop)
        
class Budget_Plan(Ui_Form):
    def __init__(self, parent, database):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> top_5_expense
        super().__init__()
        self.budget_plan_plan = QWidget(parent=parent)
        self.setupUi(self.budget_plan_plan)
        self.budget_plan_plan.setGeometry(QRect(40, 100, 970, 835))
        
        self.database = database
        
        self.row_location = 0
        self.min_size = 400
        self._valid_float = QRegularExpressionValidator(QRegularExpression(r'^[+-]?\d*\.?\d+$'))
        
        self.expenses_dict = {
            "cost" : list(),
            "percent" : list(),
            "name" : list()
        }
        
        self.checkbox_ls = list()
        
        self.grid_frame = QGridLayout(self.scrollAreaWidgetContents_2)
        self.grid_frame.setObjectName("grid_frame")
        self.grid_frame.setSpacing(5)
        self.grid_frame.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.load_window = _Window(position=self.load_pushButton, name="Load Window")
        
        self.add_pushButton.clicked.connect(lambda: self.add_expense())
        self.minus_pushButton.clicked.connect(self.remove_expense)
        self.load_pushButton.clicked.connect(self.load_signal)
        self.Save_pushButton.clicked.connect(self.save_file)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
    
    
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
                                    
                for col_ in range(self.grid_frame.columnCount()):
                    del_widget_item = self.grid_frame.itemAtPosition(expense[0], col_)
                    if del_widget_item:
                        del_widget = del_widget_item.widget()
                        if del_widget:
                            self.grid_frame.removeWidget(del_widget)
                            del_widget.deleteLater()
                
                removal_list.append(expense)            
                
                name = [item for item in self.expenses_dict["name"] if item[0] == expense[0]]
                if name:
                    self.expenses_dict["name"].remove(name[0])
                    
                percent = [item for item in self.expenses_dict["percent"] if item[0] == expense[0]]
                if percent:
                    self.expenses_dict["percent"].remove(percent[0])
                    
                cost = [item for item in self.expenses_dict["cost"] if item[0] == expense[0]]
                if cost:
                    self.expenses_dict["cost"].remove(cost[0])
                
                sum_cost = sum(item[1] for item in self.expenses_dict["cost"])    
                for cost_ in self.expenses_dict["cost"]:
                    for percent_lab in self.expenses_dict["percent"]:
                        if cost_[0] == percent_lab[0]:
                            percent = (cost_[1] / sum_cost) * 100    
                            percent = "{:.2f}".format(float(percent))
                            percent_lab[1].setText(f"{percent} %")
                            
                self.total_adjust()
                
        for removal in removal_list:
            self.checkbox_ls.remove(removal)
        
    def add_expense(self, load_expense='', load_cost=''):
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
        if load_expense != '':
            expense_name_lineEdit.setText(load_expense)
        frame_1_layout.addWidget(expense_name_lineEdit)
        
        expense_name_lineEdit.returnPressed.connect(lambda: self.on_enter_pressed(frame_1, expense_name_lineEdit, row))
                
        self.grid_frame.addWidget(frame_1, self.row_location, column_location)
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
        if load_cost is not None:
            expense_cost_lineEdit.setText(load_cost)
        
        frame_2_layout.addWidget(expense_cost_lineEdit)
        
        self.grid_frame.addWidget(frame_2, self.row_location, column_location)
        column_location += 1
                                               
        cost_label = QLabel()
        cost_label.setFixedSize(QSize(230, 50))
        cost_label.setObjectName("cost_label")
        cost_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
                                 "color: #7300ff;\n"
                                 "border: 1px solid #000000;")
        cost_label.setText("$ - -")
        cost_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.grid_frame.addWidget(cost_label, self.row_location, column_location)
        column_location += 1

        percent_label = QLabel()
        percent_label.setFixedSize(QSize(230, 50))
        percent_label.setObjectName("percent_label")
        percent_label.setStyleSheet("font: 18pt \"Nirmala UI\";\n"
                                    "color: #7300ff;\n"
                                    "border: 1px solid #000000;")
        percent_label.setText("- - %")
        percent_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grid_frame.addWidget(percent_label, self.row_location, column_location)
        
        expense_cost_lineEdit.returnPressed.connect(lambda: self.on_enter_cost(frame_2, expense_cost_lineEdit, cost_label, percent_label, row))
        
        self.row_location += 1
        
        if self.row_location > 7:
            self.min_size += 50
            self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, self.min_size))

        if load_cost and load_expense:
            expense_cost_lineEdit.returnPressed.emit()
            expense_name_lineEdit.returnPressed.emit()
        # After adding all the widgets, set the layout on the scroll area's widget content
        
    def on_enter_pressed(self, frame: QFrame, line_e: QLineEdit, row: int):
        # This function will be called when Enter is pressed in the QLineEdit
        print("Enter key pressed")
        
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
        
    def on_enter_cost(self, frame: QFrame, line_e: QLineEdit, cost_label: QLabel, percent_label: QLabel, row: int):
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
        
        self.percent_adjust(float(text), percent_label, row)
        self.total_adjust()
        
    def percent_adjust(self, cost: float, percent_label: QLabel, row: int):
        self.expenses_dict["percent"].append((row, percent_label))
        
        sum_cost = sum(item[1] for item in self.expenses_dict["cost"])
        
        for cost in self.expenses_dict["cost"]:
            for percent_lab in self.expenses_dict["percent"]:
                if cost[0] == percent_lab[0]:
                    percent = (cost[1] / sum_cost) * 100    
                    percent = "{:.2f}".format(float(percent))
                    percent_lab[1].setText(f"{percent} %")
                    
    def total_adjust(self):
        sum_cost = sum(item[1] for item in self.expenses_dict["cost"])
        self.total_cost_label.setText(f"$ {sum_cost}")
        
        monthly_wage = "{:.2f}".format(sum_cost / 0.70)
        self.monthly_wage_cost_label.setText(f"$ {monthly_wage}")
        
        bi_weekly = "{:.2f}".format(float(monthly_wage) / 2.0)
        self.bi_weekly_wage_cost_label.setText(f"$ {bi_weekly}")
        
        hourly_wage = "{:.2f}".format(float(bi_weekly) / 80.0)
        self.hourly_wage_cost_label.setText(f"$ {hourly_wage}")
                   
    def load_signal(self):
        # Load window with saved plans
        self.load_window.setStyleSheet(rvar.APP_STYLE)
        self.load_window.show()
        self.fill_load_window(self.load_window) # Get file names
            
    def fill_load_window(self, load_window: QWidget):
        plan_folder = os.path.join(os.path.dirname(__file__), "budget_planning")
        raw_file_list = os.listdir(plan_folder)
        file_list = [file for file in raw_file_list if file.endswith('.bplan')]
        if file_list != []:
            column = 0
            row = 0
            for file_name in file_list:
                if column > 1:
                    column = 0
                    row += 1
                else:
                    button = QPushButton()
                    button.setStyleSheet(rvar.NORMAL_BUTTON_STYLE)
                    button.setObjectName("new_pushButton")
                    button.setMaximumWidth(250)
                    button.setText(f'{file_name}')
                    button.clicked.connect(lambda _, file_nm=file_name: self.load_plan(file_nm))
                    load_window.grid_frame.addWidget(button, row, column)
                    column += 1
        else:
            QMessageBox.information(load_window, "No Save Data", "Can't load data as there is no save data available. Please create and save one to do this action",
                                    QMessageBox.StandardButton.Ok)
            load_window.close()             
    
    def load_file(self, file_name) -> str:
        return os.path.join(os.path.dirname(__file__), "budget_planning", file_name)
    
    def load_plan(self, file_name):
        file = self.load_file(str(file_name))
        with open(file, 'r', encoding='utf-8-sig') as bplan_file:
            bplan_reader = csv.reader(bplan_file)
            for row in bplan_reader:
                # Assuming the CSV file has one column for 'category'
                category = str(row[0])
                cost = str(row[1])
                self.add_expense(load_expense=category, load_cost=cost)
                
    def save_file(self):
        ret = QMessageBox.question(self.budget_plan_plan, "Confirmation",
                                 "Do you want to save the budget plan that is here?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if ret == QMessageBox.StandardButton.Yes:
            ...
            # Have user make a file name
            file_name, ok_pressed = QInputDialog.getText(None, 'File Name', 'Please type a name for the file:')

            # Check if the user pressed OK
            if ok_pressed:
                ...
                # Check if file name exist
                check = self.file_check(file_name)
                if not check:
                    self.saving_file(file_name=file_name)
                else:
                    QMessageBox.information(self.budget_plan_plan, "Error",
                                 f"The file name {file_name}.bplan already exist.\n\nPlease try again",)
                    return
                # Save all components to file
                # self.grid_frame.columnCount()
            else:
                return
            
        else:
            return
    
    def file_check(self, file_name):
        file_dir = os.path.join(os.path.dirname(__file__), "budget_planning", f'{file_name}.bplan')
        check = os.path.exists(file_dir)
        if file_name == '':
            check = True
        return check
    
    def saving_file(self, file_name):
        # Check if both 'name' and 'cost' are present for each index
        incomplete_cost = [(i, item) for i, item in enumerate(self.expenses_dict['name']) if i not in [x[0] for x in self.expenses_dict['cost']]]
        incomplete_name = [(i, item) for i, item in enumerate(self.expenses_dict['cost']) if i not in [x[0] for x in self.expenses_dict['name']]]

        if incomplete_cost:
            # Display a QMessageBox with information about incomplete data
            message = "Incomplete data found!\n\nRows with incomplete cost:\n"
            message += "\n".join([f"Row {index + 1}: {name}" for index, (row, name) in incomplete_cost])
            QMessageBox.information(self.budget_plan_plan, "Incomplete Cost", message)
        elif incomplete_name:
            # Display a QMessageBox with information about incomplete data
            message = "Incomplete data found!\n\nRows with incomplete name:\n"
            message += "\n".join([f"Row {index + 1}: {name}" for index, (row, name) in incomplete_name])
            QMessageBox.information(self.budget_plan_plan, "Incomplete Name", message)
        else:
            # Create and write to the CSV file
            file_dir = os.path.join(os.path.dirname(__file__), "budget_planning", f'{file_name}.bplan')
            with open(f'{file_dir}', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                expense_list = self.expenses_dict['name']
                expense_list = sorted(expense_list, key=lambda x: x[0])
                cost_list = self.expenses_dict['cost']
                cost_list = sorted(cost_list, key=lambda x: x[0])
                
                # Write data
                for index, (name_index, _) in enumerate(self.expenses_dict['name']):
                    cost_index, cost_value = cost_list[index]
                    # print(cost_index, name_index, cost_value, self.expenses_dict['name'][name_index][1])
                    csv_writer.writerow([self.expenses_dict['name'][name_index][1], cost_value])

            QMessageBox.information(self.budget_plan_plan, "File Created", f"BPLAN file '{file_name}'.bplan created successfully!")
        
        