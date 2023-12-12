##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
import calendar
import os
import csv
from contextlib import contextmanager
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
from root.models import (Transaction, Month_Budget, Accounting_Type, Sub_Category,
                         Category, Account, Category_Type, App_Month, Account_Management,
                         Goal, Frequency, States, States_Income_Taxes)
########################################################################################

class Database:
    def __init__(self, database_conn: pg2.connect, logger):
        super().__init__()
        self.connection = database_conn
        self.logger = logger
        self.create_tables()
        self.month_budget_check()
        self.initial_data()

    @contextmanager
    def cursor(self):
        with self.connection.cursor() as cur:
            yield cur

    def execute_query(self, query, values=None):
        with self.cursor() as cur:
            cur.execute(query, values)
            return cur.fetchall()

    def execute_update(self, query, values=None):
        with self.cursor() as cur:
            cur.execute(query, values)
            self.connection.commit()

    def create_tables(self):
        with self.cursor() as cur:

            # CATEGORY TABLE

            # Check if the table exists by querying the information schema
            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'category_test');")
            # Fetch the result
            table_exists_cat = cur.fetchone()[0]

            if table_exists_cat:
                self.logger.debug(f"The table 'category_test' exists.")

            else:
                self.logger.debug(f"The table 'category_test' does not exist.")

                # Create category table
                self.execute_update("""CREATE TABLE IF NOT EXISTS category_test
                                (category_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                category VARCHAR(100) NOT NULL);""")

                # Load and insert initial default data
                cat_csv = os.path.join(os.path.dirname(__file__), "default_data", "category_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(cat_csv):
                    pass

                else:
                    with open(cat_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'category'
                            category = row[1]

                            self.execute_update("INSERT INTO category_test (category) VALUES (%s);", (category,))

                    self.logger.debug("Initial default data inserted into 'category_test' table.")

            # SUB-CATEGORY TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'sub_category_test');")
            table_exists_sub_cat = cur.fetchone()[0]

            if table_exists_sub_cat:
                self.logger.debug(f"The table 'sub_category_test' exists.")

            else:
                # Create sub_category table
                self.execute_update("""CREATE TABLE IF NOT EXISTS sub_category_test
                                (sub_category_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                sub_category VARCHAR(100) NOT NULL);""")

                # Load and insert initial default data
                sub_cat_csv = os.path.join(os.path.dirname(__file__), "default_data", "sub_category_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(sub_cat_csv):
                    pass

                else:
                    with open(sub_cat_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'sub_category'
                            sub_category = row[1]

                            self.execute_update("INSERT INTO sub_category_test (sub_category) VALUES (%s);", (sub_category,))

                    self.logger.debug("Initial default data inserted into 'sub_category_test' table.")

            # ACCOUNT TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'account_test');")
            table_exists_acc = cur.fetchone()[0]

            if table_exists_acc:
                self.logger.debug(f"The table 'account_test' exists.")

            else:
                # Create account table
                self.execute_update("""CREATE TABLE IF NOT EXISTS account_test
                                (account_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                account VARCHAR(100) NOT NULL);""")

            # CATEGORY TYPE TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'category_type_test');")
            table_exists_cat_type = cur.fetchone()[0]

            if table_exists_cat_type:
                self.logger.debug(f"The table 'category_type_test' exists.")

            else:
                # Create Category type table
                self.execute_update("""CREATE TABLE IF NOT EXISTS category_type_test
                                (category_type_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                category_type VARCHAR(100) NOT NULL);""")

                # Load and insert initial default data
                cat_type_csv = os.path.join(os.path.dirname(__file__), "default_data", "category_type_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(cat_type_csv):
                    pass

                else:
                    with open(cat_type_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'category_type'
                            category_type = row[1]

                            self.execute_update("INSERT INTO category_type_test (category_type) VALUES (%s);", (category_type,))

                    self.logger.debug("Initial default data inserted into 'category_type_test' table.")

            # ACCOUNTING TYPE TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'accounting_type_test');")
            table_exists_acc_type = cur.fetchone()[0]

            if table_exists_acc_type:
                self.logger.debug(f"The table 'accounting_type_test' exists.")

            else:
                # Create category table
                self.execute_update("""CREATE TABLE IF NOT EXISTS accounting_type_test
                                (accounting_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                accounting VARCHAR(10) NOT NULL);""")

                # Load and insert initial default data
                acc_type_csv = os.path.join(os.path.dirname(__file__), "default_data", "accounting_type_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(acc_type_csv):
                    pass

                else:
                    with open(acc_type_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'accounting_type_test'
                            accounting_type = row[1]

                            self.execute_update("INSERT INTO accounting_type_test (accounting) VALUES (%s);", (accounting_type,))

                    self.logger.debug("Initial default data inserted into 'accounting_type_test' table.")

            # MONTH TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'month_test');")
            table_exists_mon = cur.fetchone()[0]

            if table_exists_mon:
                self.logger.debug(f"The table 'month_test' exists.")

            else:
                # Create Months table
                self.execute_update("""CREATE TABLE IF NOT EXISTS month_test
                                (month_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                month VARCHAR(10) NOT NULL);""")

                # Load and insert initial default data
                mon_csv = os.path.join(os.path.dirname(__file__), "default_data", "month_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(mon_csv):
                    pass

                else:
                    with open(mon_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'month_test'
                            month_ = row[1]

                            self.execute_update("INSERT INTO month_test (month) VALUES (%s);", (month_,))

                    self.logger.debug("Initial default data inserted into 'month_test' table.")

            # STATES TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'states_test');")
            table_exists_states = cur.fetchone()[0]

            if table_exists_states:
                self.logger.debug(f"The table 'states_test' exists.")

            else:
                # Create States table
                self.execute_update("""CREATE TABLE IF NOT EXISTS states_test
                                (state_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                state_name VARCHAR(100) NOT NULL,
                                state_abbreviation VARCHAR(2) NOT NULL);""")

                # Load and insert initial default data
                states_csv = os.path.join(os.path.dirname(__file__), "default_data", "states_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(states_csv):
                    pass

                else:
                    with open(states_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'states_csv'
                            states_ = row[1]
                            states_abbr = row[2]

                            self.execute_update("INSERT INTO states_test (state_name, state_abbreviation) VALUES (%s, %s);", (states_, states_abbr))

                    self.logger.debug("Initial default data inserted into 'states_test' table.")

            # STATES INCOME TAX TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'states_income_tax_test');")
            table_exists_states_inc = cur.fetchone()[0]

            if table_exists_states_inc:
                self.logger.debug(f"The table 'states_income_tax_test' exists.")

            else:
                # Create States Income tax table
                self.execute_update("""CREATE TABLE IF NOT EXISTS states_income_tax_test
                                (year INTEGER NOT NULL,
                                state_id INTEGER REFERENCES states_test(state_id),
                                single_filer_rates NUMERIC (6, 5),
                                single_filer_brackets INTEGER,
                                married_filing_jointly_rates NUMERIC (6, 5),
                                married_filing_jointly_brackets INTEGER,
                                standard_deduction_single INTEGER,
                                standard_deduction_couple INTEGER,
                                personal_exemption_single INTEGER,
                                personal_exemption_couple INTEGER,
                                personal_exemption_dependent INTEGER);""")


                # Load and insert initial default data
                states_inc_csv = os.path.join(os.path.dirname(__file__), "default_data", "states_income_tax_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(states_inc_csv):
                    pass

                else:

                    with open(states_inc_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'states_income_tax_test'
                            year = row[0]
                            state_id = row[1]
                            single_file_rate = row[2]
                            single_file_bracket = row[3]
                            married_file_rate = row[4]
                            married_file_bracket = row[5]
                            standard_duc_single = row[6]
                            standard_duc_couple = row[7]
                            personal_exmpt_single = row[8]
                            personal_exmpt_couple = row[9]
                            personal_exmpt_dependent = row[10]

                            self.execute_update("""INSERT INTO states_income_tax_test
                                        (year, state_id, single_filer_rates, single_filer_brackets,
                                        married_filing_jointly_rates, married_filing_jointly_brackets,
                                        standard_deduction_single, standard_deduction_couple,
                                        personal_exemption_single, personal_exemption_couple, personal_exemption_dependent)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (year, state_id, single_file_rate,
                                                                                                  single_file_bracket, married_file_rate,
                                                                                                  married_file_bracket, standard_duc_single,
                                                                                                  standard_duc_couple, personal_exmpt_single,
                                                                                                  personal_exmpt_couple, personal_exmpt_dependent))

                    self.logger.debug("Initial default data inserted into 'states_income_tax_test' table.")

            # FREQUENCY TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'frequency_test');")
            table_exists_freq = cur.fetchone()[0]

            if table_exists_freq:
                self.logger.debug(f"The table 'frequency_test' exists.")

            else:
                # Create frequency table
                self.execute_update("""CREATE TABLE IF NOT EXISTS frequency_test
                                (frequency_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                frequency VARCHAR(50) NOT NULL,
                                frequency_month INTEGER NOT NULL,
                                frequency_days INTEGER NOT NULL);""")

                # Load and insert initial default data
                freq_csv = os.path.join(os.path.dirname(__file__), "default_data", "frequency_test.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(freq_csv):
                    pass

                else:

                    with open(freq_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'frequency_test'
                            frequency_ = row[1]
                            frequency_month = row[2]
                            frequency_days = row[3]

                            self.execute_update("INSERT INTO frequency_test (frequency, frequency_month, frequency_days) VALUES (%s, %s, %s);", (frequency_, frequency_month,
                                                                                                                                         frequency_days))

                    self.logger.debug("Initial default data inserted into 'frequency_test' table.")

            # PAYBACK TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'payback_test');")
            table_exists_pybk = cur.fetchone()[0]

            if table_exists_pybk:
                self.logger.debug(f"The table 'payback_test' exists.")

            else:
                # Create payback table
                self.execute_update("""CREATE TABLE IF NOT EXISTS payback_test
                                (payback_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                payback_name VARCHAR(100) NOT NULL,
                                payback_description VARCHAR(100) NOT NULL,
                                payback_amount INTEGER NOT NULL,
                                paid_back_amount INTEGER NOT NULL);""")

            # GOALS TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'goals_test');")
            table_exists_trans_freq = cur.fetchone()[0]

            if table_exists_trans_freq:
                self.logger.debug(f"The table 'goals_test' exists.")

            else:
                # Create goals table
                self.execute_update("""CREATE TABLE IF NOT EXISTS goals_test
                                (goal_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                goal_description VARCHAR(100) NOT NULL,
                                goal_account_id INTEGER REFERENCES account_test(account_id),
                                goal_asset VARCHAR(100),
                                goal_amount NUMERIC(13, 2),
                                goal_perc NUMERIC(13, 2),
                                goal_start_date DATE NOT NULL,
                                goal_end_date DATE NOT NULL,
                                goal_complete BOOLEAN NOT NULL);""")

            # TRANSACTION FREQUENCY TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'transaction_frequency_test');")
            table_exists_trans_freq = cur.fetchone()[0]

            if table_exists_trans_freq:
                self.logger.debug(f"The table 'transaction_frequency_test' exists.")

            else:
                # Create transaction frequency table
                self.execute_update("""CREATE TABLE IF NOT EXISTS transaction_frequency_test
                                (transaction_frequency_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                frequency_id INTEGER REFERENCES frequency_test(frequency_id),
                                start_date DATE NOT NULL,
                                amount NUMERIC(13, 2) NOT NULL,
                                category_id INTEGER REFERENCES category_test(category_id),
                                sub_category_id INTEGER REFERENCES sub_category_test(sub_category_id),
                                account_id INTEGER REFERENCES account_test(account_id),
                                category_type_id INTEGER REFERENCES category_type_test(category_type_id),
                                accounting_id INTEGER REFERENCES accounting_type_test(accounting_id),
                                payback_id INTEGER REFERENCES payback_test(payback_id));""")

            # TRANSACTION FREQUENCY RECEIPT TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'transaction_frequency_receipt_test');")
            table_exists_trans_freq_rec = cur.fetchone()[0]

            if table_exists_trans_freq_rec:
                self.logger.debug(f"The table 'transaction_frequency_receipt_test' exists.")

            else:
                # Create trnsaction frequency receipt table
                self.execute_update("""CREATE TABLE IF NOT EXISTS transaction_frequency_receipt_test
                                (transaction_frequency_receipt_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                transaction_frequency_id INTEGER REFERENCES frequency_test(frequency_id),
                                receipt_date DATE NOT NULL);""")

            # TRANSACTION TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'transaction_test');")
            table_exists_trans = cur.fetchone()[0]

            if table_exists_trans:
                print(f"The table 'transaction_test' exists.")

            else:
                print(f"The table 'transaction_test' does not exist.")

                # Create account table with months and values
                # create transaction table
                self.execute_update("""CREATE TABLE IF NOT EXISTS transaction_test
                                (transaction_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                transaction_date DATE NOT NULL,
                                transaction_name TEXT,
                                amount NUMERIC(13, 2) NOT NULL,
                                category_id INTEGER REFERENCES category_test(category_id),
                                sub_category_id INTEGER REFERENCES sub_category_test(sub_category_id),
                                account_id INTEGER REFERENCES account_test(account_id),
                                category_type_id INTEGER REFERENCES category_type_test(category_type_id),
                                month_id INTEGER REFERENCES month_test(month_id),
                                accounting_id INTEGER REFERENCES accounting_type_test(accounting_id),
                                frequency_id INTEGER REFERENCES frequency_test(frequency_id),
                                payback_id INTEGER REFERENCES payback_test(payback_id));""")

                self.execute_update("""ALTER TABLE transaction_test
                                DROP CONSTRAINT transaction_test_account_id_fkey;

                                ALTER TABLE transaction_test
                                ADD CONSTRAINT transaction_test_account_id_fkey
                                FOREIGN KEY (account_id)
                                REFERENCES account_test(account_id)
                                ON DELETE CASCADE;"""
                                )

            # ACCOUNT MANAGEMENT TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'account_management_test');")
            table_exists_acc_man = cur.fetchone()[0]

            if table_exists_acc_man:
                print(f"The table 'account_management_test' exists.")

            else:
                print(f"The table 'account_management_test' does not exist.")

                # create portfolio management table
                # Will Need to correct table naming
                self.execute_update("""CREATE TABLE IF NOT EXISTS account_management_test
                                (month_year_account_id INTEGER NOT NULL PRIMARY KEY,
                                month_year_id INTEGER NOT NULL,
                                month_id INTEGER REFERENCES month_test(month_id) NOT NULL,
                                account_id INTEGER REFERENCES account_test(account_id) NOT NULL,
                                amount NUMERIC(13, 2) NOT NULL);""")

                self.execute_update("""ALTER TABLE account_management_test
                                DROP CONSTRAINT account_management_test_account_id_fkey;

                                ALTER TABLE account_management_test
                                ADD CONSTRAINT account_management_test_account_id_fkey
                                FOREIGN KEY (account_id)
                                REFERENCES account_test(account_id)
                                ON DELETE CASCADE;"""
                                )

            # MONTHLY BUDGET TABLE

            cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'month_budget_test');")
            table_exists_mon_bdg = cur.fetchone()[0]

            if table_exists_mon_bdg:
                print(f"The table 'month_budget_test' exists.")

            else:
                # Create monthly budget table
                self.execute_update("""CREATE TABLE IF NOT EXISTS month_budget_test
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

    def initial_data(self) -> None:
        """
        Gets initial transaction data to be utilized by the
        appication upon start up.
        Returns: pd.dataframe
        """
        with self.cursor() as cur:

            # APP TRANSACTION DATA

            self.app_data = dict()
            self.app_data['transaction_data'] = dict()
            self.app_data['transaction_data']['old'] = list()

            transaction_results = self.execute_query("""SELECT transaction_test.transaction_id, transaction_test.transaction_date, account_test.account,
                                transaction_test.transaction_name, transaction_test.amount, category_test.category,
                                sub_category_test.sub_category, category_type_test.category_type, payback_test.payback_name,
                                transaction_test.payback_id, frequency_test.frequency, accounting_type_test.accounting
                                FROM transaction_test
                                INNER JOIN account_test
                                ON account_test.account_id = transaction_test.account_id
                                INNER JOIN category_test
                                ON category_test.category_id = transaction_test.category_id
                                INNER JOIN sub_category_test
                                ON sub_category_test.sub_category_id = transaction_test.sub_category_id
                                INNER JOIN category_type_test
                                ON category_type_test.category_type_id = transaction_test.category_type_id
                                INNER JOIN payback_test
                                ON payback_test.payback_id = transaction_test.payback_id
                                INNER JOIN frequency_test
                                ON frequency_test.frequency_id = transaction_test.frequency_id
                                INNER JOIN accounting_type_test
                                ON accounting_type_test.accounting_id = transaction_test.accounting_id
                                ORDER BY transaction_test.transaction_date;""")

            for row in transaction_results:
                transaction_obj = Transaction(row)

                self.app_data['transaction_data']['old'].append(transaction_obj)

            self.connection.commit()

            print(self.app_data['transaction_data']['old'])

            # APP PANDAS DATAFRAME TRANSACTION DATA

            self.app_data['transaction_dataframe'] = dict()
            raw_df_data = list()

            for transaction in self.app_data['transaction_data']['old']:
                trans_data = (transaction.date, transaction.account, transaction.description, transaction.amount,
                              transaction.category, transaction.sub_category, transaction.category_type)

                raw_df_data.append(trans_data)

            self.app_data['transaction_dataframe'] = pd.DataFrame(raw_df_data, columns=['Date', 'Account', 'Description', 'Amount', 'Category', 'SubCategory', 'Transaction Type'])
            self.app_data['transaction_dataframe'] = self.app_data['transaction_dataframe'].set_index('Date')

            # print(self.app_data['transaction_dataframe'])

            # APP MONTH BUDGET DATA

            self.app_data['month_budget'] = dict()
            self.app_data['month_budget']['old'] = list()

            month_budget_results = self.execute_query("""SELECT month_year_id, month_id, earnings,
                                food, bills, grocery,
                                transportation, free_expense, investment,
                                support, goal, starting_budget,
                                total, left_amount, expected_ending_budget
                                FROM month_budget_test;""")

            for row in month_budget_results:
                month_budg_obj = Month_Budget(row)

                self.app_data['month_budget']['old'].append(month_budg_obj)

            self.app_data['month_budget']['new'] = self.app_data['month_budget']['old']

            self.connection.commit()

            # print(self.app_data['month_budget']['old'])

            # APP ACCOUNTING TYPE DATA

            self.app_data['accounting_type'] = dict()
            self.app_data['accounting_type']['old'] = list()

            accounting_type_results = self.execute_query("""SELECT accounting_id, accounting FROM accounting_type_test;""")

            for row in accounting_type_results:
                account_type_obj = Accounting_Type(row)

                self.app_data['accounting_type']['old'].append(account_type_obj)

            self.connection.commit()

            # print(self.app_data['accounting_type']['old'])

            # APP CATEGORY DATA

            self.app_data['category'] = dict()
            self.app_data['category']['old'] = list()

            category_results = self.execute_query("""SELECT category_id, category FROM category_test;""")

            for row in category_results:
                cat_obj = Category(row)

                self.app_data['category']['old'].append(cat_obj)

            self.connection.commit()

            # print(self.app_data['category']['old'])

            # APP SUB CATEGORY DATA

            self.app_data['sub_category'] = dict()
            self.app_data['sub_category']['old'] = list()

            sub_category_results = self.execute_query("""SELECT sub_category_id, sub_category FROM sub_category_test;""")

            for row in sub_category_results:
                sub_cat_obj = Sub_Category(row)

                self.app_data['sub_category']['old'].append(sub_cat_obj)

            self.connection.commit()

            # print(self.app_data['sub_category']['old'])

            # APP ACCOUNT DATA

            self.app_data['account'] = dict()
            self.app_data['account']['old'] = list()

            account_results = self.execute_query("""SELECT account_id, account FROM account_test;""")

            for row in account_results:
                account_obj = Account(row)

                self.app_data['account']['old'].append(account_obj)

            self.connection.commit()

            # print(self.app_data['account']['old'])

            # APP CATEGORY TYPE DATA

            self.app_data['category_type'] = dict()
            self.app_data['category_type']['old'] = list()

            cate_type_results = self.execute_query("""SELECT category_type_id, category_type FROM category_type_test;""")

            for row in cate_type_results:
                cat_type_obj = Category_Type(row)

                self.app_data['category_type']['old'].append(cat_type_obj)

            self.connection.commit()

            # print(self.app_data['category_type']['old'])

            # APP MONTHS DATA

            self.app_data['months'] = dict()
            self.app_data['months']['old'] = list()

            month_results = self.execute_query("""SELECT month_id, month FROM month_test;""")

            for row in month_results:
                month_obj = App_Month(row)

                self.app_data['months']['old'].append(month_obj)

            self.connection.commit()

            # print(self.app_data['months']['old'])

            # APP ACCOUNT MANAGEMENT DATA

            self.app_data['account_management'] = dict()
            self.app_data['account_management']['old'] = list()

            account_manage_results = self.execute_query("""SELECT month_year_account_id, month_year_id, month_id, account_id, amount FROM account_management_test;""")

            for row in account_manage_results:
                account_mangement_obj = Account_Management(row)

                self.app_data['account_management']['old'].append(account_mangement_obj)

            self.connection.commit()

            # print(self.app_data['account_management']['old'])

            # APP GOAL DATA

            self.app_data['goals'] = dict()
            self.app_data['goals']['old'] = list()

            goal_results = self.execute_query("""SELECT goals_id, goal_description, goal_account_id, goal_asset, goal_amount,
                        goal_perc, goal_start_date, goal_end_date, goal_complete
                        FROM goals_test;""")

            for row in goal_results:
                goal_obj = Goal(row)

                self.app_data['goals']['old'].append(goal_obj)

            self.connection.commit()

            # print(self.app_data['goals']['old'])

            # APP FREQUENCY DATA

            self.app_data['frequency'] = dict()
            self.app_data['frequency']['old'] = list()

            frequency_results = self.execute_query("""SELECT frequency_id, frequency, frequency_month, frequency_days FROM frequency_test;""")

            for row in frequency_results:
                frequency_obj = Frequency(row)

                self.app_data['frequency']['old'].append(frequency_obj)

            self.connection.commit()

            # print(self.app_data['frequency']['old'])
            
            # APP States DATA

            self.app_data['states'] = dict()
            self.app_data['states']['old'] = list()

            states_results = self.execute_query("""SELECT state_id, state_name, state_abbreviation FROM states_test;""")

            for row in states_results:
                states_obj = States(row)

                self.app_data['states']['old'].append(states_obj)

            self.connection.commit()

            # print(self.app_data['states']['old'])
            
            # APP STATE INCOME TAXES DATA

            self.app_data['state_income_tax'] = dict()
            self.app_data['state_income_tax']['old'] = list()

            state_income_tax_results = self.execute_query("""SELECT year, state_id, single_filer_rates,
                                single_filer_brackets, married_filing_jointly_rates, married_filing_jointly_brackets,
                                standard_deduction_single, standard_deduction_couple, personal_exemption_single,
                                personal_exemption_couple, personal_exemption_dependent
                                FROM states_income_tax_test;""")

            for row in state_income_tax_results:
                state_inc_tax_obj = States_Income_Taxes(row)

                self.app_data['state_income_tax']['old'].append(state_inc_tax_obj)

            self.app_data['state_income_tax']['new'] = self.app_data['state_income_tax']['old']

            self.connection.commit()

            # print(self.app_data['state_income_tax']['old'])

    def single_data_request(self, table, column, row, criteria):
        """SELECT {table}.{column} FROM {table}
            WHERE {row} = {criteria};"""

        self.cur.execute(f"""SELECT {table}.{column} FROM {table}
                         WHERE {row} = {criteria};""")

        query_results = self.cur.fetchall()
        #print(query_results)
        self.connection.commit()

        return query_results

    def single_data_request_2(self, table, column, row, criteria, row_2, criteria_2):
        """SELECT {table}.{column} FROM {table}
            WHERE {row} = {criteria}
            AND {row_2} = {criteria_2};"""

        self.cur.execute(f"""SELECT {table}.{column} FROM {table}
                         WHERE {row} = {criteria}
                         AND {row_2} = {criteria_2};""")

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

    def all_data_request_w_criteria(self, table, row, criteria):
        """SELECT {table}.{column} FROM {table}
            WHERE {row} = {criteria};"""

        self.cur.execute(f"""SELECT * FROM {table}
                         WHERE {row} = {criteria};""")

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
        # print(query_results)
        self.connection.commit()

        return query_results

    def update_value(self, table, column, row, criteria, value):
        """UPDATE {table}
            SET {column} = {value}
            WHERE {row} = {criteria};"""

        self.cur.execute(f"""UPDATE {table} SET {column} = {value}
                         WHERE {row} = {criteria};""")

        self.connection.commit()

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

    def month_budget_check_stats(self, parent, year: str):
        # if no data is entered in the database for month budget
        """
        Gets month budget data to be utilized by the
        appication upon start up.
        Returns: pd.dataframe
        """
        #print(self)

        # Test 1
        m_int = rvar.month_dict["January"]
        month_budget = next(
            (
                jan_budg for jan_budg in self.app_data['month_budget']['old'] if jan_budg.month == m_int and jan_budg.year == year
                ),
            False
            )

        if not month_budget:
            # Validate Input
            ret = QMessageBox.question(parent, "No Data Available",
                                    f"There seems to be no data available for the year {year}. Do you want to make template data for this year?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            # If User decides to add psuedo data
            if ret == QMessageBox.StandardButton.Yes:

                for month_int in rvar.month_dict.values():

                    month_budget = next(
                        (
                            month_info for month_info in self.app_data['month_budget']['old'] if month_info.month == m_int and month_info.year == year
                            ),
                        False
                        )

                    # Test 2
                    if not month_budget:

                        month_budget_id = int((int(month_int) * 10000) + int(year))


                        ##### ADD TO CODE LATER #########################################################################
                        # self.execute_query(f"""INSERT INTO month_budget_test
                        #         (month_year_id, month_id, earnings, food, bills, grocery, transportation, free_expense,
                        #         investment, support, goal, starting_budget)
                        #         VALUES ({month_budget_id}, {month_int}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                        #         ;""")
                        month_attr = [month_budget_id, month_int, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
                        month_data = Month_Budget(month_attr)
                        self.app_data['month_budget']['new'].append(month_data)

                QMessageBox.information(parent, "Success",
                                f"Data has been successfully created for the year {year}.",
                                QMessageBox.StandardButton.Ok)

                return True

            # If user chooses not to add psuedo data
            elif ret == QMessageBox.StandardButton.Cancel:

                return False

        # query_results = self.cur.fetchall()
        # print(query_results)
        return True

    # def category_budget(self, year: int, month: int, column: str):
    #     table = "month_budget_test"
    #     row = "month_year_id"
    #     criteria = (10000 * month) + int(year)

    #     results = self.single_data_request(table, column, row, criteria)

    #     return results

    # def starting_budget(self, year: int):
    #     table = "month_budget_test"
    #     column = "starting_budget"
    #     row = "month_year_id"
    #     criteria = 10000 + int(year)

    #     results = self.single_data_request(table, column, row, criteria)

    #     return results

    # def starting_budget_month(self, year: int, month: int):
    #     table = "month_budget_test"
    #     column = "starting_budget"
    #     row = "month_year_id"
    #     criteria = (10000 * month) + int(year)

    #     results = self.single_data_request(table, column, row, criteria)

    #     return results

    # def change_budget(self, year: int, month: int, column: str, value: str):
    #     table = "month_budget_test"
    #     row = "month_year_id"
    #     criteria = (10000 * month) + int(year)

    #     self.update_value(table, column, row, criteria, value)

    # def month_budget(self, year: int, month: int):
    #     table = "month_budget_test"
    #     column = "total"
    #     row = "month_year_id"
    #     criteria = (10000 * month) + int(year)

    #     results = self.single_data_request(table, column, row, criteria)

    #     return results

    # def savings_for_month(self, year: int, month: int):
    #     table = "month_budget_test"
    #     column = "left_amount"
    #     row = "month_year_id"
    #     criteria = (10000 * month) + int(year)

    #     results = self.single_data_request(table, column, row, criteria)

    #     return results

    # def earnings_for_month(self, year: int, month: int):
    #     table = "month_budget_test"
    #     column = "earnings"
    #     row = "month_year_id"
    #     criteria = (10000 * month) + int(year)

    #     results = self.single_data_request(table, column, row, criteria)

    #     return results

    def portfolio_month_amount(self, year: int, month: int, account_id: int):
        table = "account_management_test"
        column = "amount"
        row = "month_year_account_id"
        criteria = (1000000 * account_id) + (10000 * month) + int(year)
        row_2 = "account_id"
        criteria_2 = account_id

        results = self.single_data_request_2(table, column, row, criteria, row_2, criteria_2)

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

    def budget_for_year_table(self, year: int):
        """
        SELECT * FROM table
        WHERE month_year_id - month_id = year
        """
        data_table = "month_budget_test"
        rows = "month_year_id - month_id * 10000"

        results = self.all_data_request_w_criteria(data_table, rows, year)

        return results

    # def budget_for_year(self, year):
    #     table = "month_budget_test"
    #     column = "total"
    #     rows = "month_year_id - month_id * 10000"

    #     results = self.sum_single_data_request(table, column, rows, year)

    #     return results

    def savings_for_year(self, year):
        table = "month_budget_test"
        column = "left_amount"
        rows = "month_year_id - month_id * 10000"

        results = self.sum_single_data_request(table, column, rows, year)

        return results

    # def earnings_for_year(self, year):
    #     table = "month_budget_test"
    #     column = "earnings"
    #     rows = "month_year_id - month_id * 10000"

    #     results = self.sum_single_data_request(table, column, rows, year)

    #     return results

    def category_budget_for_year(self, year, column):
        table = "month_budget_test"
        rows = "month_year_id - month_id * 10000"

        results = self.sum_single_data_request(table, column, rows, year)

        return results

    def insert_transaction_data(self, transaction_list: list):
        """
        list: [transaction_date (2023-01-01), transaction_name, amount (10.00), category_id,
                sub_category_id, account_id, category_type_id, month_id, accounting_id]
        """
        with self.cursor() as cur:
            self.execute_update(f"""INSERT INTO transaction_test (transaction_date, transaction_name,
                            amount, category_id, sub_category_id, account_id, category_type_id,
                            month_id, accounting_id)
                            VALUES
                            ('{transaction_list[0]}', '{transaction_list[1]}', {transaction_list[2]},
                            {transaction_list[3]}, {transaction_list[4]}, {transaction_list[5]},
                            {transaction_list[6]}, {transaction_list[7]}, {transaction_list[8]});""")

            # For Debugging purposes
            print('Transaction added')

    # def insert_account_data(self, year, month, account_id, amount):
    #     """
    #     month_year_id = (10000 * int(month)) + int(year)
    #     self.cur.execute(f'INSERT INTO account_management_test
    #                      (month_year_account_id, month_year_id, month_id, account_id, amount)
    #                      VALUES
    #                      ('{month_year_id}', '{month}', {account_id}, {amount});')
    #     """
    #     month_year_id = (10000 * int(month)) + int(year)
    #     month_year_account_id = (1000000 * account_id) + (10000 * month) + int(year)

    #     if month == 0:
    #         month = 1

    #     self.cur.execute(f"""SELECT * FROM account_management_test
    #                              WHERE month_year_account_id = {month_year_account_id}
    #                              AND month_year_id = {month_year_id}
    #                              AND account_id = {int(account_id)}
    #                              AND month_id = {int(month)};""")

    #     query = self.cur.fetchall()

    #     print(f"query: {query}")
    #     self.connection.commit()

    #     if query == []:
    #         self.cur.execute(f"""INSERT INTO account_management_test
    #                         (month_year_account_id, month_year_id, month_id, account_id, amount)
    #                         VALUES
    #                         ({month_year_account_id}, {month_year_id}, {month}, {account_id}, {amount});""")

    #         self.connection.commit()

    #         # For Debugging purposes
    #         print('Account data added')

    #     if query != []:
    #         self.cur.execute(f"""UPDATE account_management_test SET amount = {amount}
    #                          WHERE month_year_account_id = {month_year_account_id}
    #                          AND month_year_id = {month_year_id}
    #                          AND account_id = {account_id}
    #                          AND month_id = {month};""")

    #         self.connection.commit()

    #         # For Debugging purposes
    #         print('Account data updated')

    # def add_account(self, account_name: str):
    #     table = "account_test"

    #     self.cur.execute(f"""SELECT * FROM {table}
    #                       WHERE account = '{account_name}';""")

    #     query = self.cur.fetchall()
    #     self.connection.commit()

    #     if query == []:
    #         self.cur.execute(f"""INSERT INTO {table}
    #                         (account)
    #                         VALUES ('{account_name}');""")

    #         self.connection.commit()

    #         # For Debugging purposes
    #         print('Account added')
    #         return True

    #     if query != []:
    #         return False

    # def account_id_request(self, account_name: str):
    #     table = "account_test"
    #     column = "account_id"
    #     row = "account"
    #     criteria = f"'{account_name}'"

    #     results = self.single_data_request(table, column, row, criteria)

    #     return results

    # def remove_account(self, account_name: str, account_id: str):

    #     self.cur.execute(f"""DELETE FROM account_test
    #                      WHERE account = '{account_name}'
    #                      AND account_id = {account_id};""")

    #     self.connection.commit()

    # def retrieve_states(self):
    #     table = "states_test"
    #     column = "state_name"

    #     result = self.query_column(table, column)

    #     return result

    # def get_state_tax_bracket(self, state):

    #     self.cur.execute(f"""SELECT states_income_tax_test.single_filer_rates, states_income_tax_test.single_filer_brackets
    #                      FROM states_income_tax_test
    #                      INNER JOIN states_test
    #                      ON states_income_tax_test.state_id = states_test.state_id
    #                      WHERE states_test.state_name = '{state}';""")

    #     query_results = self.cur.fetchall()
    #     # print(query_results)
    #     self.connection.commit()

    #     return query_results


    # """SELECT states_income_tax_test.single_filer_rates, states_income_tax_test.single_filer_brackets,
    #                      states_income_tax_test.standard_deduction_single
    #                      FROM states_income_tax_test
    #                      INNER JOIN states_test
    #                      ON states_income_tax_test.state_id = states_test.state_id
    #                      WHERE states_test.state_name = '{state}';""
