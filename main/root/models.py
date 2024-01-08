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
        
    def get_table(self):
        return 'transaction_'

    def insert_column(self):
        return '(transaction_date, transaction_name, amount, category_id, sub_category_id, account_id, category_type_id, \
month_id, accounting_id, frequency_id, payback_id) VALUES \
(%(date)s, %(name)s, %(amount)s, %(cate)s, %(sub_cate)s, %(acc)s, %(cate_typ)s, %(month)s, %(accing)s, %(freq)s, %(pay)s)'
            
    def insert_data(self, app_data) -> dict:
        values = {'date' : self.date,
                  'name' : self.description,
                  'amount' : self.amount,
                  'cate' : next(cate.id for cate in app_data['category']['start_data'] if cate.category == self.category),
                  'sub_cate' : next(cate.id for cate in app_data['sub_category']['start_data'] if cate.sub_category == self.sub_category),
                  'acc' : next(cate.id for cate in app_data['account']['start_data'] if cate.account == self.account),
                  'cate_typ' : next(cate.id for cate in app_data['category_type']['start_data'] if cate.category_type == self.category_type),
                  'month' : self.month,
                  'accing' : next(cate.id for cate in app_data['accounting_type']['start_data'] if cate.type == self.accounting_type),
                  'freq' : next(cate.id for cate in app_data['frequency']['start_data'] if cate.frequency == self.frequency),
                  'pay' : self.payback_id,}
        return values
    
    def delete_column(self): 
        return "WHERE transaction_id = %(transaction_id)s;"
    
    def delete_data(self, _):
        values = {'transaction_id': self.id}
        return values
        
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
        self.month_name = next(month for month, month_id in rvar.month_dict.items() if month_id == self.month)
        
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
    
    def update(self):
        self.total = self.food + self.bills + self.grocery + self.transportation + self.free_expense + self.investment + self.support
        self.left_amount = self.earnings + self.total
        self.expected_ending_budget = self.starting_budget + self.left_amount

    def get_table(self):
        return 'month_budget_'
    
    def insert_column(self):
        return '(month_year_id, month_id, earnings, food, bills, grocery, transportation, free_expense, investment,\
            support, goal, starting_budget) VALUES \
(%(month_year_id)s, %(month_id)s, %(earnings)s, %(food)s, %(bills)s, %(grocery)s, %(transportation)s, %(free_expense)s, %(investment)s, %(support)s, %(goal)s, %(starting_budget)s)'

    def insert_data(self, _) -> dict:
        values = {'month_year_id' : self.id,
                  'month_id' : self.month,
                  'earnings' : self.earnings,
                  'food' : self.food,
                  'bills' : self.bills,
                  'grocery' : self.grocery,
                  'transportation' : self.transportation,
                  'free_expense' : self.free_expense,
                  'investment' : self.investment,
                  'support' : self.support,
                  'goal' : self.goal,
                  'starting_budget' : self.starting_budget}
        return values
    
    def update_column(self):
        return '''SET month_id = %(month_id)s, 
    earnings = %(earnings)s, 
    food = %(food)s, 
    bills = %(bills)s, 
    grocery = %(grocery)s, 
    transportation = %(transportation)s, 
    free_expense = %(free_expense)s, 
    investment = %(investment)s, 
    support = %(support)s, 
    goal = %(goal)s, 
    starting_budget = %(starting_budget)s
    WHERE month_year_id = %(month_year_id)s;'''
        
    def update_data(self, _) -> dict:
        values = {'month_year_id' : self.id,
                  'month_id' : self.month,
                  'earnings' : self.earnings,
                  'food' : self.food,
                  'bills' : self.bills,
                  'grocery' : self.grocery,
                  'transportation' : self.transportation,
                  'free_expense' : self.free_expense,
                  'investment' : self.investment,
                  'support' : self.support,
                  'goal' : self.goal,
                  'starting_budget' : self.starting_budget}
        return values
    
class Accounting_Type:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.type = data[1]

    def get_table(self):
        return 'accounting_type_'
    
    def insert_column(self):
        return '(accounting)'
    
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...

class Sub_Category:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.sub_category = data[1]
        
    def get_table(self):
        return 'sub_category_'
    
    def insert_column(self):
        return '(sub_category, sub_category_id) VALUES (%(sub_category)s, %(sub_category_id)s)'
    
    def insert_data(self, _):
        values = {'sub_category' : self.sub_category,
                  'sub_category_id' : self.id}
        return values
        
    def update_column(self):
        return '''SET sub_category = %(sub_category)s, 
    WHERE sub_category_id = %(sub_category_id)s;'''
        
    def update_data(self, _):
        values = {'sub_category' : self.sub_category,
                  'sub_category_id' : self.id}
        return values

class Category:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.category = data[1]
        
    def get_table(self):
        return 'category_'
    
    def insert_column(self):
        return '(category) VALUES %(category)s'
    
    def insert_data(self, _):
        values = {'category' : self.category
                  }
        return values
        
    def update_column(self):
        return '''SET category = %(category)s, 
    WHERE category_id = %(category_id)s;'''
        
    def update_data(self, _):
        values = {'category' : self.category,
                  'category_id' : self.id}
        return values

class Account:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.account = data[1]
        
    def get_table(self):
        return 'account_'
    
    def insert_column(self):
        return '(account_id, account) VALUES (%(account_id)s, %(account)s);'
    
    def insert_data(self, _) -> None:
        values = {'account': self.account,
                  'account_id': self.id}
        return values
        
    def update_column(self) -> None:
        return 'SET account = %(account)s WHERE account_id = %(account_id)s;'
        
    def update_data(self, _) -> None:
        values = {'account_id' : self.id,
                  'account' : self.account
                  }
        return values

    def delete_column(self): 
        return "WHERE account_id = %(account_id)s;"
    
    def delete_data(self, _):
        values = {'account_id': self.id}
        return values

class Category_Type:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.category_type = data[1]
        
    def get_table(self):
        return 'category_type_'
    
    def insert_column(self):
        return '(category_type)'
    
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...

class App_Month:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.month = data[1]
        
    def get_table(self):
        return 'month_'
    
    def insert_column(self):
        return '(month)'
    
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...

class Account_Management:
    
    def __init__(self, data: tuple):
        self.id = data[0]
        self.month_year_id = data[1]
        self.month_id = data[2]
        self.account_id = data[3]
        self.amount = data[4]
        self.year = self.month_year_id - (self.month_id * 10000)
        self.account_name = None
        
        if self.year < 0:
            self.month_id = 0
            self.year = self.month_year_id
            
    def get_accout_name(self, acc_name):
        self.account_name = acc_name
           
    def get_table(self):
        return 'account_management_'
    
    def insert_column(self):
        return '(month_year_account_id, month_year_id, month_id, account_id, amount) VALUES (%(month_year_account_id)s, %(month_year_id)s, %(month_id)s, %(account_id)s, %(amount)s);'
    
    def insert_data(self, _) -> None:
        values = {'month_year_account_id': self.id,
                  'month_year_id': self.month_year_id,
                  'month_id': self.month_id,
                  'account_id': self.account_id,
                  'amount': self.amount,
            }
        return values
        
    def update_column(self) -> None:
        return '''SET month_year_id = %(month_year_id)s, 
    month_id = %(month_id)s, 
    account_id = %(account_id)s, 
    amount = %(amount)s
    WHERE month_year_account_id = %(month_year_account_id)s;'''
        
    def update_data(self, _) -> None:
        values = {'month_year_account_id': self.id,
                  'month_year_id': self.month_year_id,
                  'month_id': self.month_id,
                  'account_id': self.account_id,
                  'amount': self.amount,
            }
        return values

    def delete_column(self): 
        return "WHERE month_year_account_id = %(month_year_account_id)s;"
    
    def delete_data(self, _):
        values = {'month_year_account_id': self.id}
        return values

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
        
    def get_table(self):
        return 'goals_'
    
    def insert_column(self):
        return '(goal_description, goal_account_id, goal_asset, goal_amount, goal_perc, goal_start_date, goal_end_date, goal_complete)'
    
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...

class Frequency:

    def __init__(self, data: tuple):
        self.id = data[0]
        self.frequency = data[1]
        self.month = data[2]
        self.days = data[3]
        
    def get_table(self):
        return 'frequency_'
    
    def insert_column(self):
        return '(frequency, frequency_month, frequency_days)'
    
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...

class Payback:
    
    def __init__(self, data: tuple):
        self.payback_id = data[0]
        self.payback_name = data[1]
        self.payback_description = data[2]
        self.payback_amount = data[3]
        self.paid_back_amount = data[4]

    def get_table(self):
        return 'payback_'
    
    def insert_column(self):
        return '(payback_name, payback_description, payback_amount, paid_back_amount)'
    
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...

class States:
    def __init__(self, data: tuple):
        self.state_id = data[0]
        self.state_name = data[1]
        self.state_abbreviation = data[2]
        
    def get_table(self):
        return 'states_'
    
    def insert_column(self):
        return '(state_name, state_abbreviation)'
    
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...

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

    def get_table(self):
        return 'states_income_tax_'
    
    def insert_column(self):
        return '(year, state_id, single_filer_rates, single_filer_brackets, married_filing_jointly_rates, \
            married_filing_jointly_brackets, standard_deduction_single, standard_deduction_couple, \
                personal_exemption_single, personal_exemption_couple, personal_exemption_dependent)'
                
    def insert_data(self, _) -> None:
        ...
        
    def update_column(self) -> None:
        ...
        
    def update_data(self, _) -> None:
        ...