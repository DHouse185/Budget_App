##########  Python IMPORTs  ############################################################
import datetime
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
import numpy as np
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
########################################################################################

class Transaction:
    """
        Storage for data on a Transaction
        data\n
        Ex. Data - \n
        number: 1\n
        date: 2023-01-20\n
        account: 'Chase_Checking'\n
        description: Clothes\n
        amount: 50.00\n
        category: Free Expense\n
        sub_category: Walmart\n
        category_type: Expense\n
        payback: False\n
        payback_id: 0\n
        frequency: Once\n
        month: 1\n
        year: 2023\n
        accounting_type: debit
        """

    def __init__(self, data: tuple):
        self.id = data[0]
        self.date: datetime.date = data[1]
        self.account = data[2]
        self.description = data[3]
        self.amount = data[4]
        self.category = data[5]
        self.sub_category = data[6]
        self.category_type = data[7]
        self.payback = data[8]
        self.payback_id = data[9]
        self.frequency = data[10]
        self.accounting_type = data[11]
        self.month = self.date.month
        self.year = self.date.year
        
class Month_Budget:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.month = data[1]
        self.earnings = data[2]
        self.food = data[3]
        self.bills = data[4]
        self.grocery = data[5]
        self.transportation = data[6]
        self.free_expense = data[7]
        self.investment = data[8]
        self.support = data[9]
        self.goal = data[10]
        self.starting_budget = data[11]
        self.total = data[12]
        self.left_amount = data[13]
        self.expected_ending_budget = data[14]
        self.year = self.id - (self.month * 10000)
        self.month_name = [month for month, month_id in rvar.month_dict.items() if month_id == self.month]
        
        self.dashbord_list = [self.month_name, self.earnings, self.food, self.grocery, self.transportation,
                              self.free_expense, self.investment, self.bills, self.support, self.goal,
                              self.total, self.left_amount]
        
        self.category_mapping = {
            'earnings'       : 'earnings',
            'food'           : 'food',
            'bills'          : 'bills',
            'grocery'        : 'grocery',
            'transportation' : 'transportation',
            'investment'     : 'investment',
            'support'        : 'support',
            'goal'           : 'goal',
            'free expense'   : 'free_expense'
        }
        
class Accounting_Type:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.type = data[1]
        
class Sub_Category:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.sub_category = data[1]
        
class Category:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.category = data[1]
        
class Account:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.account = data[1]
        
class Category_Type:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.category_type = data[1]
        
class App_Month:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.month = data[1]
        
class Account_Management:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.month_year_id = data[1]
        self.month_id = data[2]
        self.account_id = data[3]
        self.amount = data[4]
        self.year = self.month_year_id - (self.month_id * 10000)
        
        if self.year < 0:
            self.month_id = 0
            self.year = self.month_year_id
        
class Goal:

    def __init__(self, data: tuple):
        self.id = data[0]
        self.name = data[1]
        self.account_id = data[2]
        self.asset = data[3]
        self.amount = data[4]
        self.percent = data[5]
        self.start_date = data[6]
        self.end_date = data[7]
        self.complete = data[8]
        
class Frequency:

    def __init__(self, data: tuple):
        self.id = data[0]
        self.frequency = data[1]
        self.month = data[2]
        self.days = data[3]

class States:
    def __init__(self, data: tuple):
        self.state_id = data[0]
        self.state_name = data[1]
        self.state_abbreviation = data[2]
        
class States_Income_Taxes:
    def __init__(self, data: tuple):
        self.year = data[0]
        self.state_id = data[1]
        self.single_filer_rates = data[2]
        self.single_filer_brackets = data[3]
        self.married_filing_jointly_rates = data[4]
        self.married_filing_jointly_brackets = data[5]
        self.standard_deduction_single = data[6]
        self.standard_deduction_couple = data[7]
        self.personal_exemption_single = data[8]
        self.personal_exemption_couple = data[9]
        self.personal_exemption_dependent = data[10]
