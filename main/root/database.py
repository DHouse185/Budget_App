##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
import calendar
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QRect
import psycopg2 as pg2
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
########################################################################################

class Database:
    def __init__(self, database_conn: pg2.connect):
        super().__init__()
        self.connection = database_conn
        self.cur = self.connection.cursor()
        self.create_tables()
        # self._dummy_data = self.dummy_data()
        self.month_budget_check()
        self.start_up_transaction_data = self.retrieve_initial_data()
        
    def create_tables(self):
        # Create category table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS category_test
                         (category_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         category VARCHAR(100) NOT NULL);""")
        self.connection.commit()
        
        # Create sub_category table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS sub_category_test
                         (sub_category_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         sub_category VARCHAR(100) NOT NULL);""")
        self.connection.commit()
        
        # Create account table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS account_test
                         (account_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         account VARCHAR(100) NOT NULL);""")
        self.connection.commit()
        
        # Create Category type table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS category_type_test
                         (category_type_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         category_type VARCHAR(100) NOT NULL);""")
        self.connection.commit()
        
        # Create category table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS accounting_type_test
                         (accounting_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         accounting VARCHAR(10) NOT NULL);""")
        self.connection.commit()
        
        # Create Months table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS month_test
                         (month_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         month VARCHAR(10) NOT NULL);""")
        self.connection.commit()
        # self.cur.execute("""INSERT INTO month_test (month) VALUES
        #                     ('January'),
        #                     ('February'),
        #                     ('March'),
        #                     ('April'),
        #                     ('May'),
        #                     ('June'),
        #                     ('July'),
        #                     ('August'),
        #                     ('September'),
        #                     ('October'),
        #                     ('November'),
        #                     ('December');""")
        # self.connection.commit()
        
        # create transaction table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS transaction_test
                         (transaction_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         transaction_date DATE NOT NULL,
                         transaction_name TEXT,
                         amount NUMERIC(13, 2) NOT NULL,
                         category_id INTEGER REFERENCES category_test(category_id),
                         sub_category_id INTEGER REFERENCES sub_category_test(sub_category_id),
                         account_id INTEGER REFERENCES account_test(account_id),
                         category_type_id INTEGER REFERENCES category_type_test(category_type_id),
                         month_id INTEGER REFERENCES month_test(month_id),
                         accounting_id INTEGER REFERENCES accounting_type_test(accounting_id));""")
        self.connection.commit()
        
        # Create monthly budget table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS month_budget_test
                         (month_year_id INTEGER UNIQUE NOT NULL PRIMARY KEY,
                         month_id INTEGER REFERENCES month_test(month_id) NOT NULL,
                         earnings NUMERIC(13, 2) NOT NULL,
                         food NUMERIC(13, 2) NOT NULL,
                         bills NUMERIC(13, 2) NOT NULL,
                         grocery NUMERIC(13, 2) NOT NULL,
                         transportation NUMERIC(13, 2) NOT NULL,
                         free_expense NUMERIC(13, 2) NOT NULL,
                         investment NUMERIC(13, 2) NOT NULL,
                         support NUMERIC(13, 2) NOT NULL,
                         goal NUMERIC(13, 2) NOT NULL,
                         starting_budget NUMERIC(13, 2) NOT NULL,
                         total NUMERIC(13, 2) GENERATED ALWAYS AS (food + bills + grocery + transportation + free_expense + investment + support) STORED NOT NULL,
                         left_amount NUMERIC(13, 2) GENERATED ALWAYS AS (earnings - (food + bills + grocery + transportation + free_expense + investment + support)) STORED NOT NULL,
                         expected_ending_budget NUMERIC(13, 2) GENERATED ALWAYS AS (starting_budget + earnings - (food + bills + grocery + transportation + free_expense + investment + support)) STORED NOT NULL);""")
        self.connection.commit()
        
        # Create dummmy data for month_budget_test
        # self.cur.execute("""INSERT INTO month_budget_test (month_year_id, 
        #                     month_id, earnings, food, bills, grocery,
        #                     transportation, free_expense, investment, support,
        #                     goal, starting_budget) VALUES
        #                     (12023, 1, 4631.45, 200, 2000, 150, 200, 1000, 250, 200, 150, 6000),
        #                     (22023, 2, 6600.00, 200, 2000, 150, 200, 1200, 250, 200, 150, 6000),
        #                     (32023, 3, 5001.45, 200, 2000, 150, 200, 1000, 250, 200, 150, 6000),
        #                     (42023, 4, 4501.27, 170, 2000, 150, 200, 1000, 250, 200, 150, 6000),
        #                     (52023, 5, 3531.15, 130, 2000, 150, 200, 600, 250, 200, 150, 8000);""")
        # self.connection.commit()
    
    def retrieve_initial_data(self) -> pd.DataFrame:
        """
        Gets initial transaction data to be utilized by the 
        appication upon start up.
        Returns: pd.dataframe
        """
        self.cur.execute("""SELECT transaction_test.transaction_date, account_test.account, transaction_test.transaction_name, 
                            transaction_test.amount, category_test.category, sub_category_test.sub_category,
                            category_type_test.category_type
                            FROM transaction_test
                            INNER JOIN account_test
                            ON account_test.account_id = transaction_test.account_id
                            INNER JOIN category_test
                            ON category_test.category_id = transaction_test.category_id
                            INNER JOIN sub_category_test
                            ON sub_category_test.sub_category_id = transaction_test.sub_category_id
                            INNER JOIN category_type_test
                            ON category_type_test.category_type_id = transaction_test.category_type_id
                            ORDER BY transaction_test.transaction_date;""")
        
        start_up_results = self.cur.fetchall()
        start_up_df = pd.DataFrame(start_up_results, columns=['Date', 'Account', 'Description', 'Amount', 'Category', 'SubCategory', 'Transaction Type'])
        #print(start_up_df)
        start_up_df = start_up_df.set_index('Date')
        #print(start_up_df)
        self.connection.commit()
        
        return start_up_df
    
    def single_data_request(self, table, column, row, criteria):
        self.cur.execute(f"""SELECT {table}.{column} FROM {table}
                         WHERE {row} = {criteria};""")
        
        query_results = self.cur.fetchall()
        #print(query_results)
        self.connection.commit()
        
        return query_results
    
    def all_data_request(self, table, column=None):
        if column is None:
            column = '*'
        self.cur.execute(f"""SELECT {column} FROM {table};""")
        
        query_results = self.cur.fetchall()
        #print(query_results)
        self.connection.commit()
        
        return query_results
    
    def sum_single_data_request(self, table, column, rows, criteria):
        self.cur.execute(f"""SELECT SUM({table}.{column})
                        FROM {table}
                        WHERE {rows} = {criteria};""")
        
        query_results = self.cur.fetchall()
        #print(query_results)
        self.connection.commit()
        
        return query_results
    
    def query_column(self, table, column):
        self.cur.execute(f"""SELECT {table}.{column} FROM {table};""")
        
        query_results = self.cur.fetchall()
        print(query_results)
        self.connection.commit()
        
        return query_results
        
    def month_budget_check(self, year=datetime.now().year):
        # if no data is entered in the database for month budget
        """
        Gets month budget data to be utilized by the 
        appication upon start up.
        Returns: pd.dataframe
        """
        #print(self)
        for month_int in rvar.month_dict.values():
            # print(year)
            # print(month_int)
            month_budget = self.retrieve_dashboard_month_progress(month_int, year)
            
            if not month_budget:
                month_budget_id = int((int(month_int) * 10000) + int(year))
                
                self.cur.execute(f"""INSERT INTO month_budget_test
                        (month_year_id, month_id, earnings, food, bills, grocery, transportation, free_expense,
                        investment, support, goal, starting_budget)
                        VALUES ({month_budget_id}, {month_int}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                        ;""")
        # self.cur.execute(f"""SELECT month_test.month, earnings, food, grocery, transportation, 
        #                  free_expense, investment, bills, support, goal, total, left_amount
        #                  FROM month_budget_test
        #                  INNER JOIN month_test
        #                  ON month_test.month_id = month_budget_test.month_id
        #                  WHERE month_year_id = {month_budget_id};""")
        
        # query_results = self.cur.fetchall()
        # print(query_results)
        self.connection.commit()
        
        return None
    
    @rfunc.query_print_results
    def retrieve_dashboard_month_progress(self, month: int, year: str) -> pd.DataFrame:
        """
        Gets month budget data to be utilized by the 
        appication upon start up.
        Returns: pd.dataframe
        """
        # print(f'self: {self}')
        # print(f'month: {month}')
        # print(f'year: {year}')
        month_budget_id = int((int(month) * 10000) + int(year))
        self.cur.execute(f"""SELECT month_test.month, earnings, food, grocery, transportation, 
                         free_expense, investment, bills, support, goal, total, left_amount
                         FROM month_budget_test
                         INNER JOIN month_test
                         ON month_test.month_id = month_budget_test.month_id
                         WHERE month_year_id = {month_budget_id};""")
        
        query_results = self.cur.fetchall()
        # print(query_results)
        self.connection.commit()
        
        return query_results
    
    def retrieve_dashboard_spent_progress(self, category_id: int, month: str, year: str) -> pd.DataFrame:
        """
        Gets month spent data to be utilized by the 
        appication upon start up.
        Returns: pd.dataframe
        """
        cat_id_num = rvar.category_dict[category_id]
        # print(f"cat_id_num:{cat_id_num}")
        
        # print(f'month: {month}')
        # print(f'month: {year}')
        month_budget_id = str((int(month) * 10000) + int(year))
        
        # Get first day of the month
        if int(month_budget_id) < 99999:
            
            date_1 = datetime(year=int(month_budget_id[1:]), month=int(month_budget_id[0:1]), day=1)
            first_date = f"{date_1.strftime('%Y-%m-%d')}"
            # print(f"first_date:{first_date}")
            
            # Get last day of the month
            months_range = calendar.monthrange(date_1.year, date_1.month)
            days_in_month = months_range[1]
            date_2 = datetime(year=int(month_budget_id[1:]), month=int(month_budget_id[0:1]), day=int(days_in_month))
            last_date = f"{date_2.strftime('%Y-%m-%d')}"
            # print(f"last_date:{last_date}")
        
        elif int(month_budget_id) > 99999:
            
            date_1 = datetime(year=int(month_budget_id[2:]), month=int(month_budget_id[0:2]), day=1)
            first_date = f"{date_1.strftime('%Y-%m-%d')}"
            # print(f"first_date:{first_date}")
            
            # Get last day of the month
            months_range = calendar.monthrange(date_1.year, date_1.month)
            days_in_month = months_range[1]
            date_2 = datetime(year=int(month_budget_id[2:]), month=int(month_budget_id[0:2]), day=int(days_in_month))
            last_date = f"{date_2.strftime('%Y-%m-%d')}"
            # print(f"last_date:{last_date}")
        
        self.cur.execute(f"""SELECT SUM(amount) FROM transaction_test
                         WHERE 
                         transaction_date BETWEEN SYMMETRIC '{first_date}' AND '{last_date}' 
                         AND category_id = {cat_id_num};""")
        
        query_results = self.cur.fetchall()
        self.connection.commit()
        
        if not query_results[0][0]:
            query_results = [(0,)]
        # query_array = np.array(query_results)
        # print(f"amount: {query_results}")
        
        return query_results
    
    def starting_budget(self, year: int):
        table = "month_budget_test"
        column = "starting_budget"
        row = "month_year_id"
        criteria = 10000 + int(year)
        
        results = self.single_data_request(table, column, row, criteria)
        
        return results
    
    def get_all_data_no_id(self, table: str):
        """
        'SELECT {CATEGORY} FROM {table} method
        """
        data_table = table
        table_category = rvar.table_dict[table]
        
        results = self.all_data_request(data_table, table_category)
        
        return results
    
    def get_all_data_w_id(self, table: str):
        """
        'SELECT * FROM table' method
        """
        data_table = table
        
        results = self.all_data_request(data_table)
        
        return results
    
    def budget_for_year(self, year):
        table = "month_budget_test"
        column = "total"
        rows = "month_year_id - month_id * 10000"
        
        results = self.sum_single_data_request(table, column, rows, year)
        
        return results
    
    def savings_for_year(self, year):
        table = "month_budget_test"
        column = "left_amount"
        rows = "month_year_id - month_id * 10000"
        
        results = self.sum_single_data_request(table, column, rows, year)
        
        return results
    
    def earnings_for_year(self, year):
        table = "month_budget_test"
        column = "earnings"
        rows = "month_year_id - month_id * 10000"
        
        results = self.sum_single_data_request(table, column, rows, year)
        
        return results
    
    
    def insert_transaction_data(self, transaction_list: list):
        """
        list: [transaction_date (2023-01-01), transaction_name, amount (10.00), category_id,
                sub_category_id, account_id, category_type_id, month_id, accounting_id]
        """
        self.cur.execute(f"""INSERT INTO transaction_test (transaction_date, transaction_name, 
                         amount, category_id, sub_category_id, account_id, category_type_id, 
                         month_id, accounting_id)
                         VALUES
                         ('{transaction_list[0]}', '{transaction_list[1]}', {transaction_list[2]}, 
                         {transaction_list[3]}, {transaction_list[4]}, {transaction_list[5]},
                         {transaction_list[6]}, {transaction_list[7]}, {transaction_list[8]});""")

        self.connection.commit()
        print('Transaction added')
    
    
    
    # def dummy_data(self) -> pd.DataFrame:
    #     """
    #     Gets initial transaction data to be utilized by the 
    #     appication upon start up.
    #     Returns: pd.dataframe
    #     """
    #     self.cur.execute("""SELECT * FROM transaction_data_test;""")
        
    #     start_up_results = self.cur.fetchall()
    #     start_up_df = pd.DataFrame(start_up_results, columns=['transaction_id', 'category_id', 'sub_category_id', 'account_id', 'category_type_id', 'month_id'])
    #     start_up_df.index = start_up_df['transaction_id']
    #     self.connection.commit()
        
    #     return start_up_df
