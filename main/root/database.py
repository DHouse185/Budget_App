##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QRect
import psycopg2 as pg2
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_vriables as rvar
import root.utils.resources # Do not remove. Needed for images
########################################################################################

class Database:
    def __init__(self, database_conn: pg2.connect):
        super().__init__()
        self.connection = database_conn
        self.cur = self.connection.cursor()
        self.create_tables()
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
        
        # Create Months table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS month_test
                         (month_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         month VARCHAR(10) NOT NULL);""")
        self.connection.commit()
        
        # create transaction table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS transaction_test
                         (transaction_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                         transaction_date DATE NOT NULL,
                         transaction_name TEXT,
                         amount NUMERICAL(13, 2) NOT NULL);""")
        self.connection.commit()
        
        # create transaction data table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS transaction_data_test
                         (transaction_id INTEGER REFERENCES transaction_test(transaction_id),
                         category_id INTEGER REFERENCES category_test(category_id),
                         sub_category_id INTEGER REFERENCES sub_category_test(sub_category_id),
                         account_id INTEGER REFERENCES account_test(account_id),
                         category_type_id INTEGER REFERENCES category_type_test(category_type_id),
                         month_id INTEGER REFERENCES month_test(month_id)
                         );""")
        self.connection.commit()
        
    def retrieve_initial_data(self) -> pd.DataFrame:
        """
        Gets initial transaction data to be utilized by the 
        appication upon start up.
        Returns: pd.dataframe
        """
        self.cur.execute("""SELECT transaction_test.transaction_date, account_test.account, transaction_test.transaction_name, 
                            transaction_test.amount, category_test.category, sub_category_test.subcategory,
                            category_type_test.category_type
                            FROM transaction_test
                            INNER JOIN transaction_data_test
                            ON transaction_test.transaction_id = transaction_data_test.transaction_id
                            INNER JOIN account_test
                            ON account_test.account_id = transaction_data_test.account_id
                            INNER JOIN category_test
                            ON category_test.category_id = transaction_data_test.category_id
                            INNER JOIN sub_category_test
                            ON sub_category_test.sub_category_id = transaction_data_test.sub_category_id
                            INNER JOIN category_type_test
                            ON category_type_test.category_type_id = transaction_data_test.category_type_id
                            ORDER BY transaction_test.transaction_date;""")
        
        start_up_results = self.cur.fetchall()
        start_up_df = pd.DataFrame(start_up_results, columns=['Date', 'Account', 'Description', 'Amount', 'Category', 'SubCategory', 'Transaction Type'])
        start_up_df.index = start_up_df['Date']
        self.connection.commit()
        
        return start_up_df