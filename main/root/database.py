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
        #self._dummy_data = self.dummy_data()
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
        print(start_up_df)
        start_up_df = start_up_df.set_index('Date')
        print(start_up_df)
        self.connection.commit()
        
        return start_up_df
    
    def retrieve_dashboard_month_progress(self, month: int, year: str) -> pd.DataFrame:
        """
        Gets month budget data to be utilized by the 
        appication upon start up.
        Returns: pd.dataframe
        """
        print(f'month: {month}')
        month_budget_id = int((int(month) * 10000) + int(year))
        self.cur.execute(f"""SELECT month_test.month, earnings, food, grocery, transportation, 
                         free_expense, investment, bills, support, goal, total, left_amount
                         FROM month_budget_test
                         INNER JOIN month_test
                         ON month_test.month_id = month_budget_test.month_id
                         WHERE month_year_id = {month_budget_id};""")
        
        query_results = self.cur.fetchall()
        print(query_results)
        self.connection.commit()
        
        return query_results
    
    def retrieve_dashboard_spent_progress(self, category_id: int, month: str, year: str) -> pd.DataFrame:
        """
        Gets month spent data to be utilized by the 
        appication upon start up.
        Returns: pd.dataframe
        """
        cat_id_num = rvar.category_dict[category_id]
        print(f"cat_id_num:{cat_id_num}")
        
        print(f'month: {month}')
        print(f'month: {year}')
        month_budget_id = str((int(month) * 10000) + int(year))
        
        # Get first day of the month
        date_1 = datetime(year=int(month_budget_id[1:]), month=int(month_budget_id[0:1]), day=1)
        first_date = f"{date_1.strftime('%Y-%m-%d')}"
        print(f"first_date:{first_date}")
        
        # Get last day of the month
        months_range = calendar.monthrange(date_1.year, date_1.month)
        days_in_month = months_range[1]
        date_2 = datetime(year=int(month_budget_id[1:]), month=int(month_budget_id[0:1]), day=int(days_in_month))
        last_date = f"{date_2.strftime('%Y-%m-%d')}"
        print(f"last_date:{last_date}")
        
        self.cur.execute(f"""SELECT SUM(amount) FROM transaction_test
                         WHERE 
                         transaction_date BETWEEN SYMMETRIC '{first_date}' AND '{last_date}' 
                         AND category_id = {cat_id_num};""")
        
        query_results = self.cur.fetchall()
        # query_array = np.array(query_results)
        print(f"amount: {query_results}")
        self.connection.commit()
        
        return query_results
    
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
