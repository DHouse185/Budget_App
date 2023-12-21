##########  Python IMPORTs  ############################################################
from typing import List, Tuple, Dict, Union
import random
from decimal import Decimal
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QWidget, QMessageBox, QVBoxLayout, QGridLayout, QLabel, QPushButton, QDoubleSpinBox, QLineEdit, QComboBox
from PyQt6.QtCore import QRect, QDateTime, QDate, QTime, Qt
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.database import Database
from root.models import Account
from root.models import Category_Type
from root.models import Sub_Category
from root.models import Category
from root.models import Accounting_Type
from root.models import Frequency
from root.models import Transaction
from root.models import Payback
from root.pages.components.ui.add_transaction_widget import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Popup_window(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, position, database: Database):
        super().__init__()
        # Create new widget for popup window
        self.setObjectName("Parameters_Window")
        self.resize(500, 300)
        self.setWindowTitle("Parameters")
        # self.pop_window.setStyleSheet(Path(r_var.DARK_MODE).read_text())
        self.setGeometry(QRect(position.x(), position.y() + 500, 500, 300))
        self.setStyleSheet(rvar.APP_STYLE)
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
        self.payback_data = database.app_data['payback']['old']
        ################### Test ######################################################
        test_payback_data = Payback((2, 'test', 'test', Decimal(50.00), Decimal(500.00)))
        self.payback_data.append(test_payback_data)
        ###############################################################################
        self.info_storage_list: List[Tuple[Union[QLabel, QComboBox, QDoubleSpinBox, QPushButton],
                                           Union[QLabel, QComboBox, QDoubleSpinBox, QPushButton]]] = list()
        self.new = False
        self.pay_to_payback = False
        self.name = 'None'
        self.payback_id = 1
        
        self.widgets = {
            'New': [
            {
                'Name'     : 'Name',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : 'Name',
                'column'   : 0,
                'row'      : 2
                },
            {
                'Name'     : 'Description',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : 'Description',
                'column'   : 0,
                'row'      : 3
                },
            {
                'Name'     : 'Payback Amount',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : 'Payback Amount',
                'column'   : 0,
                'row'      : 4
                },
            {
                'Name'     : 'Confirm',
                'widget'   : QPushButton,
                'width'    : 150,
                'indent'   : 10,
                'data_type': str,
                'label'    : 'Confirm',
                'column'   : 0,
                'row'      : 5,
                'function' : self.confirm_button
                },
            {
                'Name'    : 'Name_lineedit',
                'widget'   : QLineEdit,
                'width'    : 300,
                'indent'   : 10,
                'data_type': str,
                'column'   : 1,
                'row'      : 2,
                },
            {
                'Name'    : 'Description_lineedit',
                'widget'   : QLineEdit,
                'width'    : 300,
                'indent'   : 10,
                'data_type': str,
                'column'   : 1,
                'row'      : 3,
                },
            {
                'Name'    : 'payback_amount_doublespinbox',
                'widget'   : QDoubleSpinBox,
                'width'    : 150,
                'indent'   : 10,
                'data_type': Decimal,
                'max'      : 10000000.00,
                'column'   : 1,
                'row'      : 4,
                }
            ],
            'Payback' : [
            {
                'Name'     : 'Paid Back',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : 'Paid Back',
                'column'   : 0,
                'row'      : 2
                },
            {
                'Name'     : 'Payback Amount',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : 'Payback Amount',
                'column'   : 0,
                'row'      : 3
                },
            {
                'Name'     : 'Left',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : 'Left',
                'column'   : 0,
                'row'      : 4
                },
            {
                'Name'     : 'Confirm',
                'widget'   : QPushButton,
                'width'    : 110,
                'indent'   : 10,
                'data_type': str,
                'column'   : 0,
                'row'      : 5,
                'function' : self.confirm_button
                },
            {
                'Name'    : 'paid_back_label',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : self.paid_back,
                'column'   : 1,
                'row'      : 2,
                },
            {
                'Name'    : 'Payback Amount',
                'widget'   : QLabel,
                'width'    : 200,
                'indent'   : 10,
                'data_type': str,
                'label'    : self.pay_back_amount,
                'column'   : 1,
                'row'      : 3,
                },
            {
                'Name'    : 'Left_amount',
                'widget'   : QLabel,
                'width'    : 150,
                'indent'   : 10,
                'data_type': str,
                'label'    : self.payback_left_amount,
                'column'   : 1,
                'row'      : 4,
                },
            {
                'Name'    : 'Finished',
                'widget'   : QPushButton,
                'width'    : 110,
                'indent'   : 10,
                'data_type': str,
                'column'   : 1,
                'row'      : 5,
                'function' : self.finished_button
                }            
            ], 
            }
        # Add Label for Combobox of active Payback Transactions
        self.id_to_index_dict: Dict[int, int] = dict()
        self.active_payback_label = QLabel() 
        self.active_payback_label.setObjectName('Payback_Transaction')
        self.active_payback_label.setText('Payback Transaction')
        self.active_payback_label.setMaximumWidth(200)
        self.active_payback_label.setIndent(10)
        self.grid_frame.addWidget(self.active_payback_label, 0, 0)
        # Add combobox of active Payback Transactions
        self.active_payback_combobox = QComboBox()
        self.active_payback_combobox.setObjectName("transfer_To_comboBox")
        self.active_payback_combobox.addItem('')
        index_tracker = 1
        for payback in self.payback_data:
            if payback.payback_id == 1:
                pass
            else:
                self.active_payback_combobox.addItem(payback.payback_description)
                self.id_to_index_dict[index_tracker] = payback.payback_id
                index_tracker += 1
                
        self.grid_frame.addWidget(self.active_payback_combobox, 0, 1)
        # Push Buttons
        # NEW BUTTON
        self.new_pushButton = QPushButton()
        self.new_pushButton.setStyleSheet(rvar.BLUE_BUTTON_STYLE)
        self.new_pushButton.setObjectName("new_pushButton")
        self.new_pushButton.setMaximumWidth(110)
        self.new_pushButton.setText('New')
        self.grid_frame.addWidget(self.new_pushButton, 1, 0)
        # DISCARD BUTTON
        self.discard_pushButton = QPushButton()
        self.discard_pushButton.setStyleSheet(rvar.DISABLED_RED_BUTTON_STYLE)
        self.discard_pushButton.setObjectName("discard_pushButton")
        self.discard_pushButton.setMaximumWidth(110)
        self.discard_pushButton.setFixedWidth(110)
        self.discard_pushButton.setEnabled(False)
        self.discard_pushButton.setText('Discard')
        self.grid_frame.addWidget(self.discard_pushButton, 1, 1)
        # CONFIRM SIGNAL
        self.confirm_signal = QPushButton()
        self.confirm_signal.setObjectName("confirm_signal")
        # Functions for buttons
        self.new_pushButton.clicked.connect(self.new_payback)
        self.active_payback_combobox.currentIndexChanged.connect(self.old_payback)
        self.discard_pushButton.clicked.connect(self.discard)

    def paid_back(self) -> str:
        id = self.id_to_index_dict[self.active_payback_combobox.currentIndex()]
        paid_back: Decimal = next((pd_bk.paid_back_amount for pd_bk in self.payback_data if pd_bk.payback_id == id), None)
        return f'${paid_back}'
        
    def pay_back_amount(self) -> str:
        id = self.id_to_index_dict[self.active_payback_combobox.currentIndex()]
        paid_back: Decimal = next((pd_bk.payback_amount for pd_bk in self.payback_data if pd_bk.payback_id == id), None)
        return f'${paid_back}'
            
    def payback_left_amount(self) -> str:
        paid_back = Decimal(self.paid_back().replace('$', ''))
        pay_back_amount = Decimal(self.pay_back_amount().replace('$', ''))
        left: Decimal = paid_back - pay_back_amount
        return f'${left}'
        
    def discard(self):
        self.refresh()
        self.new = False
        self.pay_to_payback = False
        self.discard_pushButton.setEnabled(False)
        self.discard_pushButton.setStyleSheet(rvar.DISABLED_RED_BUTTON_STYLE)
        
    def confirm_button(self):
        if self.new == True:
            for widget_info in self.info_storage_list:
                if widget_info[0] == QDoubleSpinBox:
                    if widget_info[1].objectName() == 'payback_amount_doublespinbox':
                        self.payback_amount: Decimal = round(Decimal(widget_info[1].value()), 2)
                        validate = self.confirm_validate(widget_info[0], self.payback_amount)
                        if not validate:
                            del self.payback_amount
                            self.payback_id = 1
                            break
                elif widget_info[0] == QLineEdit:
                    if widget_info[1].objectName() == 'Name_lineedit':
                        self.name: str = widget_info[1].text()
                        validate = self.confirm_validate(widget_info[0], self.name)
                        if not validate:
                            self.name = 'None'
                            self.payback_id = 1
                            break
                    elif widget_info[1].objectName() == 'Description_lineedit':
                        self.payback_description: str = widget_info[1].text()
                        validate = self.confirm_validate(widget_info[0], self.payback_description)
                        if not validate:
                            del self.payback_description
                            self.payback_id = 1
                            break
                else:
                    pass
            if validate:
                self.payback_id = max([payback.payback_id for payback in self.payback_data]) + 1
                self.close()
                    
        elif self.pay_to_payback == True:
            validate = self.confirm_validate()
            if validate:
                self.payback_id = self.id_to_index_dict[self.active_payback_combobox.currentIndex()]
                self.name: str = next((payback.payback_name for payback in self.payback_data if payback.payback_id == self.payback_id), 'None')
                self.close()
            
    def confirm_validate(self, qwidget_message=None, object=None): 
        if self.new == True:
            if qwidget_message == QDoubleSpinBox:
                if object <= 0.00:
                    QMessageBox.information(self.popup_widget, "Error",
                                        "Please input a payback amount greater than 0 for your transaction",
                                        QMessageBox.StandardButton.Ok)
                    return False
                else:
                    return True
            if qwidget_message == QLineEdit:
                if object == '':
                    QMessageBox.information(self.popup_widget, "Error",
                                        "Please fill in the line edits for your transaction",
                                        QMessageBox.StandardButton.Ok)
                    return False
                else:
                    return True

        elif self.pay_to_payback == True:
            if self.id_to_index_dict[self.active_payback_combobox.currentIndex()] == '':
                QMessageBox.information(self.popup_widget, "Error",
                                    "Please select a payback account for your transaction",
                                    QMessageBox.StandardButton.Ok)
                return False
            else:
                return True

    def update_payback_dict(self, amount=None):
        if self.new == True:
            if self.payback_id == 1:
                pass
            else:
                payback_data = Payback((self.payback_id, self.name, self.payback_description, amount, self.payback_amount))
                self.payback_data.append(payback_data)
                self.refresh()
                # Add to Insert dictionary
                
        elif self.pay_to_payback == True:
            payback = next((py_bk for py_bk in self.payback_data if py_bk.payback_id == self.payback_id))
            payback.payback_amount += amount
            self.refresh()
            # Add to update dictionary
                        
    def finished_button(self):
        self.confirm_button()
        ... # Put remove on payback dictionary when completed
        
    def refresh(self):
        for widget_info in self.info_storage_list:
            widget = widget_info[1]
            widget.deleteLater()
            del widget
        self.name = 'None'
        self.payback_id = 1
        self.info_storage_list.clear()
    
    def old_payback(self):
        if self.active_payback_combobox.currentIndex() == 0:
            pass
        else:
            self.new = False
            self.pay_to_payback = True
            self.refresh()
            self.discard_pushButton.setEnabled(True)
            self.discard_pushButton.setStyleSheet(rvar.RED_BUTTON_STYLE)
            for widget_dict in self.widgets['Payback']:
                if widget_dict['widget'] == QLabel:
                    # Add Label for Combobox of active Payback Transactions
                    widget = QLabel() 
                    widget.setObjectName(widget_dict['Name'])
                    widget.setMaximumWidth(widget_dict['width'])
                    widget.setIndent(widget_dict['indent'])
                    self.grid_frame.addWidget(widget, widget_dict['row'], widget_dict['column'])
                    if widget_dict['column'] == 0:
                        widget.setText(widget_dict['label'])
                    elif widget_dict['column'] == 1:
                        widget.setText(widget_dict['label']())
                    self.info_storage_list.append((widget_dict['widget'], widget))
                        
                elif widget_dict['widget'] == QDoubleSpinBox:
                    widget = QDoubleSpinBox()
                    widget.setMaximum(widget_dict['max'])
                    widget.setSingleStep(0.01)
                    widget.setProperty("value", 0.00)
                    widget.setMaximumWidth(widget_dict['width'])
                    widget.setObjectName(widget_dict['Name'])
                    self.grid_frame.addWidget(widget, widget_dict['row'], widget_dict['column'])
                    self.info_storage_list.append((widget_dict['widget'], widget))
                    
                elif widget_dict['widget'] == QPushButton:
                    widget = QPushButton()
                    widget.setStyleSheet(rvar.GREEN_BUTTON_STYLE)
                    widget.setMaximumWidth(widget_dict['width'])
                    widget.setObjectName(widget_dict['Name'])
                    widget.setText(widget_dict['Name'])
                    if widget_dict['column'] == 0:
                        widget.setStyleSheet(rvar.GREEN_BUTTON_STYLE)
                    elif widget_dict['column'] == 1:
                        widget.setStyleSheet(rvar.RED_BUTTON_STYLE)
                    self.grid_frame.addWidget(widget, widget_dict['row'], widget_dict['column'])
                    widget.clicked.connect(widget_dict['function'])
                    self.info_storage_list.append((widget_dict['widget'], widget))
        
    def new_payback(self):
        self.new = True
        self.pay_to_payback = False
        self.refresh()
        self.discard_pushButton.setEnabled(True)
        self.discard_pushButton.setStyleSheet(rvar.RED_BUTTON_STYLE)
        for widget_dict in self.widgets['New']:
            if widget_dict['widget'] == QLabel:
                # Add Label for Combobox of active Payback Transactions
                widget = QLabel() 
                widget.setObjectName(widget_dict['Name'])
                widget.setText(widget_dict['label'])
                widget.setMaximumWidth(widget_dict['width'])
                widget.setIndent(widget_dict['indent'])
                self.grid_frame.addWidget(widget, widget_dict['row'], widget_dict['column'])
                self.info_storage_list.append((widget_dict['widget'], widget))
            
            elif widget_dict['widget'] == QDoubleSpinBox:
                widget = QDoubleSpinBox()
                widget.setMaximum(widget_dict['max'])
                widget.setSingleStep(0.01)
                widget.setProperty("value", 0.00)
                widget.setMaximumWidth(widget_dict['width'])
                widget.setObjectName(widget_dict['Name'])
                self.grid_frame.addWidget(widget, widget_dict['row'], widget_dict['column'])
                self.info_storage_list.append((widget_dict['widget'], widget))
                
            elif widget_dict['widget'] == QPushButton:
                widget = QPushButton()
                widget.setStyleSheet(rvar.GREEN_BUTTON_STYLE)
                widget.setMaximumWidth(widget_dict['width'])
                widget.setObjectName(widget_dict['Name'])
                widget.setText(widget_dict['Name'])
                self.grid_frame.addWidget(widget, widget_dict['row'], widget_dict['column'])
                widget.clicked.connect(widget_dict['function'])
                self.info_storage_list.append((widget_dict['widget'], widget))
                
            elif widget_dict['widget'] == QLineEdit:
                widget = QLineEdit()
                widget.setMaximumWidth(widget_dict['width'])
                widget.setObjectName(widget_dict['Name'])
                self.grid_frame.addWidget(widget, widget_dict['row'], widget_dict['column'])
                self.info_storage_list.append((widget_dict['widget'], widget))
         
class Add_Transaction(Ui_Form):
    def __init__(self, parent, database: Database):
        # Create Transaction Addition widget for Transaction page
        # Mainwindow -> central widget -> StackWidget -> Transaction Page
        # -> Add Transaction
        super().__init__()
        self.add_trans_widget = QWidget(parent=parent)
        self.setupUi(self.add_trans_widget)
        self.add_trans_widget.setGeometry(QRect(415, 0, 1490, 400))
        position = self.payback_pushButton.pos()
        self.payback_popup = Popup_window(position=position, database=database)
        
        self.database = database
        self.tables_array = ['category_test', 'sub_category_test', 'account_test', 'category_type_test',
                             'accounting_type_test', 'month_test']
        self.create_table_dict()
        
        # Add Transfer to Accounts
        self.accounts: List[str] = [acc.account for acc in self.database.app_data['account']['old']]
        for _, account in enumerate(self.accounts):  
            self.transfer_To_comboBox.addItem(account)
            self.account_comboBox.addItem(account)
        # Add category type
        self.category_types: List[str] = [cat_type.category_type for cat_type in self.database.app_data['category_type']['old']]
        for _, category_type in enumerate(self.category_types):  
            self.category_Type_comboBox.addItem(category_type)
        # Add sub categories
        self.sub_categories: List[str] = [sub_cat_type.sub_category for sub_cat_type in self.database.app_data['sub_category']['old']]
        for _, sub_category in enumerate(self.sub_categories):  
            self.sub_Category_comboBox.addItem(sub_category)   
        # Add Categories
        self.categories: List[str] = [cat.category for cat in self.database.app_data['category']['old']]
        for _, category in enumerate(self.categories):  
            self.category_comboBox.addItem(category)
        # Add Accounting type
        self.accountings: List[str] = [acc_type.type for acc_type in self.database.app_data['accounting_type']['old']]
        for _, accounting in enumerate(self.accountings):  
            self.credit_Debit_comboBox.addItem(accounting)
        # Add Frequency
        self.frequencies: List[str] = [freq.frequency for freq in self.database.app_data['frequency']['old']]
        for _, frequency in enumerate(self.frequencies):  
            self.frequency_comboBox.addItem(frequency)
        
        self.category_Type_comboBox.currentTextChanged.connect(self.check_category_type)    
        self.discard_pushButton.clicked.connect(self.discard_check)
        self.payback_pushButton.clicked.connect(self.payback_window)
        
    def check_category_type(self, text):
        if text == 'Payback':
            self.enable_payback()
        else:
            self.disable_payback()
        
    def disable_payback(self):
        self.payback_pushButton.setEnabled(False)
        self.payback_pushButton.setStyleSheet(rvar.DISABLED_BLUE_BUTTON_STYLE)
        self.payback_popup.name = 'None'
        self.payback_popup.payback_id = 1
        self.payback_popup.refresh()
        
    def enable_payback(self):
        self.payback_pushButton.setEnabled(True)
        self.payback_pushButton.setStyleSheet(rvar.BLUE_BUTTON_STYLE)
        
    def payback_window(self):
        self.payback_popup.show()
    
    def payback_confirm(self):
        self.payback = self.payback_popup.payback_id
        self.payback_name = self.payback_popup.name
               
    def create_table_dict(self):
        self.accounts_dict = dict()
        self.category_type_dict = dict()
        self.sub_categories_dict = dict()
        self.categories_dict = dict()
        self.accountings_dict = dict()
        self.frequency_dict = dict()
        
        accounts: List[Account] = self.database.app_data['account']['old']
        ######## POTENTIALLY ADD TO DATABASE APP_DATA? ######################################## 
        for _, account in enumerate(accounts):  
            self.accounts_dict[account.account] = account.id
        # Add category type
        category_types: List[Category_Type] = self.database.app_data['category_type']['old']
        for _, category_type in enumerate(category_types):  
            self.category_type_dict[category_type.category_type] = category_type.id
        # Add sub categories
        sub_categories: List[Sub_Category] = self.database.app_data['sub_category']['old']
        for _, sub_category in enumerate(sub_categories):  
            self.sub_categories_dict[sub_category.sub_category] = sub_category.id
        # Add Categories
        categories: List[Category] = self.database.app_data['category']['old']
        for _, category in enumerate(categories):  
            self.categories_dict[category.category] = category.id
        # Add Accounting type
        accountings : List[Accounting_Type]= self.database.app_data['accounting_type']['old']
        for _, accounting in enumerate(accountings):  
            self.accountings_dict[accounting.type] = accounting.id
        # Add Frequency
        frequencies : List[Frequency]= self.database.app_data['frequency']['old']
        for _, frequency in enumerate(frequencies):  
            self.frequency_dict[frequency.frequency] = frequency.id
        ######## POTENTIALLY ADD TO DATABASE APP_DATA? ########################################
    
    def add_check(self):
        # Validate Input
        ret = QMessageBox.question(self.add_trans_widget, "Confirmation",
                                 "Do you want to add this transaction?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to exit the application
        if ret == QMessageBox.StandardButton.Yes:
            return self.add_transaction()
            
        # If user chooses not to close application
        elif ret == QMessageBox.StandardButton.Cancel:
            return False
            
        # Close event will be ignored if neither are selected
        else:
            QMessageBox.information(self.add_trans_widget, "Error",
                                 "Something went wrong. Transaction was not added",
                                 QMessageBox.StandardButton.Ok)
            return False
                        
    def add_transaction(self):
        account = self.account_comboBox.currentText()
        account_id = self.accounts_dict[account]
        
        # Grab Date
        date = self.date_dateEdit.dateTime()
        date_datetime = date.toPyDateTime().date()
        date_month = date.toString("MMMM")
        date_formatted = date.toString("yyyy-MM-dd")        
        month_id = rvar.month_dict[date_month]        
        description = self.description_lineEdit.text()
        amount = self.amount_doubleSpinBox.text()        
        accounting = self.credit_Debit_comboBox.currentText()
        accounting_id = self.accountings_dict[accounting]
        transfer_account = self.transfer_To_comboBox.currentText()
        payback = self.payback_popup.name
        payback_id = self.payback_popup.payback_id
        frequency = self.frequency_comboBox.currentText()
        self.payback = self.payback_popup.payback_id
        self.payback_name = self.payback_popup.name
        if transfer_account == 'None':
            pass
        else:
            transfer_account_id = self.accounts_dict[transfer_account]
        
        sub_category = self.sub_Category_comboBox.currentText()
        sub_category_id = self.sub_categories_dict[sub_category]
        
        category = self.category_comboBox.currentText()
        category_id = self.categories_dict[category]
        
        category_type = self.category_Type_comboBox.currentText()
        category_type_id = self.category_type_dict[category_type]
        
        max_id = max([trans.id for trans in self.database.app_data['transaction_data']['old']])
        trans_temp_id = random.randint((max_id + 1), (max_id + 10))
        
        transaction_list = [date_formatted, description, amount, category_id, sub_category_id, account_id, category_type_id, month_id, accounting_id]
        
        for _, check in enumerate(transaction_list):
            if check == '':
                QMessageBox.information(self.add_trans_widget, "Empty input",
                                 "One of the inputs is not valid for adding to transactions",
                                 QMessageBox.StandardButton.Ok)
                return False
            else:
                pass
        transaction = Transaction((max_id, date_datetime, account, description, round(Decimal(amount), 2), category, sub_category, category_type, payback, payback_id, frequency, accounting))
        self.database.app_data['transaction_data']['old'].append(transaction) # Change to 'unsaved' or 'new' later
        # Add Transaction to insert dictionary
        self.payback_popup.update_payback_dict(round(Decimal(amount), 2))
        df2 = {'ID': trans_temp_id, 'Account': account, 'Description': description, 'Amount': round(Decimal(amount), 2), 'Category': category, 'SubCategory': sub_category, 'Transaction Type': category_type}
        self.database.app_data['transaction_dataframe'].loc[date_datetime] = df2
        return True
        
    def discard_check(self):
        # Validate Input
        ret = QMessageBox.question(self.add_trans_widget, "Confirmation",
                                 "Do you want to clear this transaction?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        
        # If user chooses to exit the application
        if ret == QMessageBox.StandardButton.Yes:
            self.discard_transaction()
            
        # If user chooses not to close application
        elif ret == QMessageBox.StandardButton.Cancel:
            return 
            
        # Close event will be ignored if neither are selected
        else:
            QMessageBox.information(self.add_trans_widget, "Error",
                                 "Something went wrong. Progress not discarded",
                                 QMessageBox.StandardButton.Ok)
            return 
        
    def discard_transaction(self):
        self.account_comboBox.setCurrentIndex(0)
        self.date_dateEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.description_lineEdit.clear()
        self.amount_doubleSpinBox.setProperty("value", 0.00)      
        self.credit_Debit_comboBox.setCurrentIndex(0)
        self.transfer_To_comboBox.setCurrentIndex(0)
        self.sub_Category_comboBox.setCurrentIndex(0)
        self.category_comboBox.setCurrentIndex(0)
        self.category_Type_comboBox.setCurrentIndex(0)