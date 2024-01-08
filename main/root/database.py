##########  Python IMPORTs  ############################################################
from pathlib import Path
from datetime import datetime
import typing
import os
import csv
from contextlib import contextmanager
from decimal import Decimal
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
                         Goal, Frequency, States, States_Income_Taxes, Payback)
########################################################################################

class Database:
    def __init__(self, database_conn: pg2.connect, logger, user_id):
        super().__init__()
        self.connection = database_conn
        self.logger = logger
        self.user_id = user_id
        self.create_tables()
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
            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'category_{self.user_id}');")
            # Fetch the result
            table_exists_cat = cur.fetchone()[0]

            if table_exists_cat:
                self.logger.debug(f"The table 'category_{self.user_id}' exists.")

            else:
                self.logger.debug(f"The table 'category_{self.user_id}' does not exist.")

                # Create category table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS category_{self.user_id}
                                (category_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                category VARCHAR(100) NOT NULL);""")

                # Load and insert initial default data
                cat_csv = os.path.join(os.path.dirname(__file__), "default_data", "category.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(cat_csv):
                    pass

                else:
                    with open(cat_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'category'
                            category = row[1]

                            self.execute_update(f"INSERT INTO category_{self.user_id} (category) VALUES (%s);", (category,))

                    self.logger.debug(f"Initial default data inserted into 'category_{self.user_id}' table.")

            # SUB-CATEGORY TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'sub_category_{self.user_id}');")
            table_exists_sub_cat = cur.fetchone()[0]

            if table_exists_sub_cat:
                self.logger.debug(f"The table 'sub_category_{self.user_id}' exists.")

            else:
                # Create sub_category table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS sub_category_{self.user_id}
                                (sub_category_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                sub_category VARCHAR(100) NOT NULL);""")

                # Load and insert initial default data
                sub_cat_csv = os.path.join(os.path.dirname(__file__), "default_data", "sub_category.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(sub_cat_csv):
                    pass

                else:
                    with open(sub_cat_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'sub_category'
                            sub_category = row[1]

                            self.execute_update(f"INSERT INTO sub_category_{self.user_id} (sub_category) VALUES (%s);", (sub_category,))

                    self.logger.debug(f"Initial default data inserted into 'sub_category_{self.user_id}' table.")

            # ACCOUNT TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'account_{self.user_id}');")
            table_exists_acc = cur.fetchone()[0]

            if table_exists_acc:
                self.logger.debug(f"The table 'account_{self.user_id}' exists.")

            else:
                # Create account table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS account_{self.user_id}
                                (account_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                account VARCHAR(100) NOT NULL);""")

            # CATEGORY TYPE TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'category_type_{self.user_id}');")
            table_exists_cat_type = cur.fetchone()[0]

            if table_exists_cat_type:
                self.logger.debug(f"The table 'category_type_{self.user_id}' exists.")

            else:
                # Create Category type table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS category_type_{self.user_id}
                                (category_type_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                category_type VARCHAR(100) NOT NULL);""")

                # Load and insert initial default data
                cat_type_csv = os.path.join(os.path.dirname(__file__), "default_data", "category_type.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(cat_type_csv):
                    pass

                else:
                    with open(cat_type_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'category_type'
                            category_type = row[1]

                            self.execute_update(f"INSERT INTO category_type_{self.user_id} (category_type) VALUES (%s);", (category_type,))

                    self.logger.debug(f"Initial default data inserted into 'category_type_{self.user_id}' table.")

            # ACCOUNTING TYPE TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'accounting_type_{self.user_id}');")
            table_exists_acc_type = cur.fetchone()[0]

            if table_exists_acc_type:
                self.logger.debug(f"The table 'accounting_type_{self.user_id}' exists.")

            else:
                # Create category table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS accounting_type_{self.user_id}
                                (accounting_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                accounting VARCHAR(10) NOT NULL);""")

                # Load and insert initial default data
                acc_type_csv = os.path.join(os.path.dirname(__file__), "default_data", "accounting_type.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(acc_type_csv):
                    pass

                else:
                    with open(acc_type_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'accounting_type_{self.user_id}'
                            accounting_type = row[1]

                            self.execute_update(f"INSERT INTO accounting_type_{self.user_id} (accounting) VALUES (%s);", (accounting_type,))

                    self.logger.debug(f"Initial default data inserted into 'accounting_type_{self.user_id}' table.")

            # MONTH TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'month_{self.user_id}');")
            table_exists_mon = cur.fetchone()[0]

            if table_exists_mon:
                self.logger.debug(f"The table 'month_{self.user_id}' exists.")

            else:
                # Create Months table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS month_{self.user_id}
                                (month_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                month VARCHAR(10) NOT NULL);""")

                # Load and insert initial default data
                mon_csv = os.path.join(os.path.dirname(__file__), "default_data", "month.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(mon_csv):
                    pass

                else:
                    with open(mon_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'month_{self.user_id}'
                            month_ = row[1]

                            self.execute_update(f"INSERT INTO month_{self.user_id} (month) VALUES (%s);", (month_,))

                    self.logger.debug(f"Initial default data inserted into 'month_{self.user_id}' table.")

            # STATES TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'states_{self.user_id}');")
            table_exists_states = cur.fetchone()[0]

            if table_exists_states:
                self.logger.debug(f"The table 'states_{self.user_id}' exists.")

            else:
                # Create States table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS states_{self.user_id}
                                (state_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                state_name VARCHAR(100) NOT NULL,
                                state_abbreviation VARCHAR(2) NOT NULL);""")

                # Load and insert initial default data
                states_csv = os.path.join(os.path.dirname(__file__), "default_data", "states.csv")  # Update this with the path to your CSV file

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

                            self.execute_update(f"INSERT INTO states_{self.user_id} (state_name, state_abbreviation) VALUES (%s, %s);", (states_, states_abbr))

                    self.logger.debug(f"Initial default data inserted into 'states_{self.user_id}' table.")

            # STATES INCOME TAX TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'states_income_tax_{self.user_id}');")
            table_exists_states_inc = cur.fetchone()[0]

            if table_exists_states_inc:
                self.logger.debug(f"The table 'states_income_tax_{self.user_id}' exists.")

            else:
                # Create States Income tax table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS states_income_tax_{self.user_id}
                                (year INTEGER NOT NULL,
                                state_id INTEGER REFERENCES states_{self.user_id}(state_id),
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
                states_inc_csv = os.path.join(os.path.dirname(__file__), "default_data", "states_income_tax.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(states_inc_csv):
                    pass

                else:

                    with open(states_inc_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'states_income_tax_{self.user_id}'
                            year = row[0]
                            state_id = row[1] 
                            single_file_rate = row[2] if row[2] != 'NULL' else None
                            single_file_bracket = row[3] if row[3] != 'NULL' else None
                            married_file_rate = row[4] if row[4] != 'NULL' else None
                            married_file_bracket = row[5] if row[5] != 'NULL' else None
                            standard_duc_single = row[6] if row[6] != 'NULL' else None
                            standard_duc_couple = row[7] if row[7] != 'NULL' else None
                            personal_exmpt_single = row[8] if row[8] != 'NULL' else None
                            personal_exmpt_couple = row[9] if row[9] != 'NULL' else None
                            personal_exmpt_dependent = row[10] if row[10] != 'NULL' else None

                            self.execute_update(f"""INSERT INTO states_income_tax_{self.user_id}
                                        (year, state_id, single_filer_rates, single_filer_brackets,
                                        married_filing_jointly_rates, married_filing_jointly_brackets,
                                        standard_deduction_single, standard_deduction_couple,
                                        personal_exemption_single, personal_exemption_couple, personal_exemption_dependent)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (year, state_id, single_file_rate,
                                                                                                  single_file_bracket, married_file_rate,
                                                                                                  married_file_bracket, standard_duc_single,
                                                                                                  standard_duc_couple, personal_exmpt_single,
                                                                                                  personal_exmpt_couple, personal_exmpt_dependent))

                    self.logger.debug(f"Initial default data inserted into 'states_income_tax_{self.user_id}' table.")

            # FREQUENCY TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'frequency_{self.user_id}');")
            table_exists_freq = cur.fetchone()[0]

            if table_exists_freq:
                self.logger.debug(f"The table 'frequency_{self.user_id}' exists.")

            else:
                # Create frequency table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS frequency_{self.user_id}
                                (frequency_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                frequency VARCHAR(50) NOT NULL,
                                frequency_month INTEGER NOT NULL,
                                frequency_days INTEGER NOT NULL);""")

                # Load and insert initial default data
                freq_csv = os.path.join(os.path.dirname(__file__), "default_data", "frequency.csv")  # Update this with the path to your CSV file

                if not os.path.isfile(freq_csv):
                    pass

                else:

                    with open(freq_csv, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        next(csv_reader)  # Skip header if present

                        for row in csv_reader:
                            # Assuming the CSV file has one column for 'frequency_{self.user_id}'
                            frequency_ = row[1]
                            frequency_month = row[2]
                            frequency_days = row[3]

                            self.execute_update(f"INSERT INTO frequency_{self.user_id} (frequency, frequency_month, frequency_days) VALUES (%s, %s, %s);", (frequency_, frequency_month,
                                                                                                                                         frequency_days))

                    self.logger.debug(f"Initial default data inserted into 'frequency_{self.user_id}' table.")

            # PAYBACK TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'payback_{self.user_id}');")
            table_exists_pybk = cur.fetchone()[0]

            if table_exists_pybk:
                self.logger.debug(f"The table 'payback_{self.user_id}' exists.")

            else:
                # Create payback table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS payback_{self.user_id}
                                (payback_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                payback_name VARCHAR(100) NOT NULL,
                                payback_description VARCHAR(100) NOT NULL,
                                payback_amount NUMERIC(13, 2) NOT NULL,
                                paid_back_amount NUMERIC(13, 2) NOT NULL);""")

            # GOALS TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'goals_{self.user_id}');")
            table_exists_trans_freq = cur.fetchone()[0]

            if table_exists_trans_freq:
                self.logger.debug(f"The table 'goals_{self.user_id}' exists.")

            else:
                # Create goals table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS goals_{self.user_id}
                                (goal_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                goal_description VARCHAR(100) NOT NULL,
                                goal_account_id INTEGER REFERENCES account_{self.user_id}(account_id),
                                goal_asset VARCHAR(100),
                                goal_amount NUMERIC(13, 2),
                                goal_perc NUMERIC(13, 2),
                                goal_start_date DATE NOT NULL,
                                goal_end_date DATE NOT NULL,
                                goal_complete BOOLEAN NOT NULL);""")

            # TRANSACTION FREQUENCY TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'transaction_frequency_{self.user_id}');")
            table_exists_trans_freq = cur.fetchone()[0]

            if table_exists_trans_freq:
                self.logger.debug(f"The table 'transaction_frequency_{self.user_id}' exists.")

            else:
                # Create transaction frequency table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS transaction_frequency_{self.user_id}
                                (transaction_frequency_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                frequency_id INTEGER REFERENCES frequency_{self.user_id}(frequency_id),
                                start_date DATE NOT NULL,
                                amount NUMERIC(13, 2) NOT NULL,
                                category_id INTEGER REFERENCES category_{self.user_id}(category_id),
                                sub_category_id INTEGER REFERENCES sub_category_{self.user_id}(sub_category_id),
                                account_id INTEGER REFERENCES account_{self.user_id}(account_id),
                                category_type_id INTEGER REFERENCES category_type_{self.user_id}(category_type_id),
                                accounting_id INTEGER REFERENCES accounting_type_{self.user_id}(accounting_id),
                                payback_id INTEGER REFERENCES payback_{self.user_id}(payback_id));""")

            # TRANSACTION FREQUENCY RECEIPT TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'transaction_frequency_receipt_{self.user_id}');")
            table_exists_trans_freq_rec = cur.fetchone()[0]

            if table_exists_trans_freq_rec:
                self.logger.debug(f"The table 'transaction_frequency_receipt_{self.user_id}' exists.")

            else:
                # Create trnsaction frequency receipt table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS transaction_frequency_receipt_{self.user_id}
                                (transaction_frequency_receipt_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                transaction_frequency_id INTEGER REFERENCES frequency_{self.user_id}(frequency_id),
                                receipt_date DATE NOT NULL);""")

            # TRANSACTION TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'transaction_{self.user_id}');")
            table_exists_trans = cur.fetchone()[0]

            if table_exists_trans:
                self.logger.debug(f"The table 'transaction_{self.user_id}' exists.")

            else:
                self.logger.debug(f"The table 'transaction_{self.user_id}' does not exist.")

                # Create account table with months and values
                # create transaction table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS transaction_{self.user_id}
                                (transaction_id SERIAL UNIQUE NOT NULL PRIMARY KEY,
                                transaction_date DATE NOT NULL,
                                transaction_name TEXT,
                                amount NUMERIC(13, 2) NOT NULL,
                                category_id INTEGER REFERENCES category_{self.user_id}(category_id),
                                sub_category_id INTEGER REFERENCES sub_category_{self.user_id}(sub_category_id),
                                account_id INTEGER REFERENCES account_{self.user_id}(account_id),
                                category_type_id INTEGER REFERENCES category_type_{self.user_id}(category_type_id),
                                month_id INTEGER REFERENCES month_{self.user_id}(month_id),
                                accounting_id INTEGER REFERENCES accounting_type_{self.user_id}(accounting_id),
                                frequency_id INTEGER REFERENCES frequency_{self.user_id}(frequency_id),
                                payback_id INTEGER REFERENCES payback_{self.user_id}(payback_id));""")

                self.execute_update(f"""ALTER TABLE transaction_{self.user_id}
                                DROP CONSTRAINT transaction_{self.user_id}_account_id_fkey;

                                ALTER TABLE transaction_{self.user_id}
                                ADD CONSTRAINT transaction_{self.user_id}_account_id_fkey
                                FOREIGN KEY (account_id)
                                REFERENCES account_{self.user_id}(account_id)
                                ON DELETE CASCADE;"""
                                )

            # ACCOUNT MANAGEMENT TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'account_management_{self.user_id}');")
            table_exists_acc_man = cur.fetchone()[0]

            if table_exists_acc_man:
                self.logger.debug(f"The table 'account_management_{self.user_id}' exists.")

            else:
                self.logger.debug(f"The table 'account_management_{self.user_id}' does not exist.")

                # create portfolio management table
                # Will Need to correct table naming
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS account_management_{self.user_id}
                                (month_year_account_id INTEGER NOT NULL PRIMARY KEY,
                                month_year_id INTEGER NOT NULL,
                                month_id INTEGER REFERENCES month_{self.user_id}(month_id) NOT NULL,
                                account_id INTEGER REFERENCES account_{self.user_id}(account_id) NOT NULL,
                                amount NUMERIC(13, 2) NOT NULL);""")

                self.execute_update(f"""ALTER TABLE account_management_{self.user_id}
                                DROP CONSTRAINT account_management_{self.user_id}_account_id_fkey;

                                ALTER TABLE account_management_{self.user_id}
                                ADD CONSTRAINT account_management_{self.user_id}_account_id_fkey
                                FOREIGN KEY (account_id)
                                REFERENCES account_{self.user_id}(account_id)
                                ON DELETE CASCADE;"""
                                )

            # MONTHLY BUDGET TABLE

            cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'month_budget_{self.user_id}');")
            table_exists_mon_bdg = cur.fetchone()[0]

            if table_exists_mon_bdg:
                self.logger.debug(f"The table 'month_budget_{self.user_id}' exists.")

            else:
                # Create monthly budget table
                self.execute_update(f"""CREATE TABLE IF NOT EXISTS month_budget_{self.user_id}
                                (month_year_id INTEGER UNIQUE NOT NULL PRIMARY KEY,
                                month_id INTEGER REFERENCES month_{self.user_id}(month_id) NOT NULL,
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

        # APP TRANSACTION DATA
        self.app_data = dict()
        self.app_data['transaction_data'] = dict()
        self.app_data['unsaved_data'] = dict()
        self.app_data['unsaved_data']['INSERT'] = list()
        self.app_data['unsaved_data']['DELETE'] = list()
        self.app_data['unsaved_data']['UPDATE'] = list()
        self.app_data['transaction_data']['start_data'] = list()

        transaction_results = self.execute_query(f"""SELECT transaction_{self.user_id}.transaction_id, transaction_{self.user_id}.transaction_date, account_{self.user_id}.account,
                            transaction_{self.user_id}.transaction_name, transaction_{self.user_id}.amount, category_{self.user_id}.category,
                            sub_category_{self.user_id}.sub_category, category_type_{self.user_id}.category_type, payback_{self.user_id}.payback_name,
                            transaction_{self.user_id}.payback_id, frequency_{self.user_id}.frequency, accounting_type_{self.user_id}.accounting
                            FROM transaction_{self.user_id}
                            INNER JOIN account_{self.user_id}
                            ON account_{self.user_id}.account_id = transaction_{self.user_id}.account_id
                            INNER JOIN category_{self.user_id}
                            ON category_{self.user_id}.category_id = transaction_{self.user_id}.category_id
                            INNER JOIN sub_category_{self.user_id}
                            ON sub_category_{self.user_id}.sub_category_id = transaction_{self.user_id}.sub_category_id
                            INNER JOIN category_type_{self.user_id}
                            ON category_type_{self.user_id}.category_type_id = transaction_{self.user_id}.category_type_id
                            INNER JOIN payback_{self.user_id}
                            ON payback_{self.user_id}.payback_id = transaction_{self.user_id}.payback_id
                            INNER JOIN frequency_{self.user_id}
                            ON frequency_{self.user_id}.frequency_id = transaction_{self.user_id}.frequency_id
                            INNER JOIN accounting_type_{self.user_id}
                            ON accounting_type_{self.user_id}.accounting_id = transaction_{self.user_id}.accounting_id
                            ORDER BY transaction_{self.user_id}.transaction_date;""")

        for row in transaction_results:
            transaction_obj = Transaction(row)

            self.app_data['transaction_data']['start_data'].append(transaction_obj)

        self.connection.commit()

        # APP PANDAS DATAFRAME TRANSACTION DATA
        self.app_data['transaction_dataframe'] = dict()
        raw_df_data = list()

        for transaction in self.app_data['transaction_data']['start_data']:
            trans_data = (transaction.date, transaction.id, transaction.account, transaction.description, transaction.amount,
                            transaction.category, transaction.sub_category, transaction.category_type)

            raw_df_data.append(trans_data)

        self.app_data['transaction_dataframe'] = pd.DataFrame(raw_df_data, columns=['Date', 'ID', 'Account', 'Description', 'Amount', 'Category', 'SubCategory', 'Transaction Type'])
        self.app_data['transaction_dataframe'] = self.app_data['transaction_dataframe'].set_index('Date')
        self.app_data['transaction_dataframe'].sort_index(inplace=True, ascending=False)

        # APP MONTH BUDGET DATA
        self.app_data['month_budget'] = dict()
        self.app_data['month_budget']['start_data'] = list()

        month_budget_results = self.execute_query(f"""SELECT month_year_id, month_id, earnings,
                            food, bills, grocery,
                            transportation, free_expense, investment,
                            support, goal, starting_budget,
                            total, left_amount, expected_ending_budget
                            FROM month_budget_{self.user_id};""")

        for row in month_budget_results:
            month_budg_obj = Month_Budget(row)

            self.app_data['month_budget']['start_data'].append(month_budg_obj)

        self.connection.commit()

        # APP ACCOUNTING TYPE DATA
        self.app_data['accounting_type'] = dict()
        self.app_data['accounting_type']['start_data'] = list()

        accounting_type_results = self.execute_query(f"""SELECT accounting_id, accounting FROM accounting_type_{self.user_id};""")

        for row in accounting_type_results:
            account_type_obj = Accounting_Type(row)

            self.app_data['accounting_type']['start_data'].append(account_type_obj)

        self.connection.commit()

        # APP CATEGORY DATA
        self.app_data['category'] = dict()
        self.app_data['category']['start_data'] = list()

        category_results = self.execute_query(f"""SELECT category_id, category FROM category_{self.user_id};""")

        for row in category_results:
            cat_obj = Category(row)

            self.app_data['category']['start_data'].append(cat_obj)

        self.connection.commit()

        # APP SUB CATEGORY DATA
        self.app_data['sub_category'] = dict()
        self.app_data['sub_category']['start_data'] = list()

        sub_category_results = self.execute_query(f"""SELECT sub_category_id, sub_category FROM sub_category_{self.user_id};""")

        for row in sub_category_results:
            sub_cat_obj = Sub_Category(row)

            self.app_data['sub_category']['start_data'].append(sub_cat_obj)

        self.connection.commit()

        # APP ACCOUNT DATA
        self.app_data['account'] = dict()
        self.app_data['account']['start_data'] = list()

        account_results = self.execute_query(f"""SELECT account_id, account FROM account_{self.user_id};""")

        for row in account_results:
            account_obj = Account(row)

            self.app_data['account']['start_data'].append(account_obj)

        self.connection.commit()

        # APP CATEGORY TYPE DATA
        self.app_data['category_type'] = dict()
        self.app_data['category_type']['start_data'] = list()

        cate_type_results = self.execute_query(f"""SELECT category_type_id, category_type FROM category_type_{self.user_id};""")

        for row in cate_type_results:
            cat_type_obj = Category_Type(row)

            self.app_data['category_type']['start_data'].append(cat_type_obj)

        self.connection.commit()

        # APP MONTHS DATA
        self.app_data['months'] = dict()
        self.app_data['months']['start_data'] = list()

        month_results = self.execute_query(f"""SELECT month_id, month FROM month_{self.user_id};""")

        for row in month_results:
            month_obj = App_Month(row)

            self.app_data['months']['start_data'].append(month_obj)

        self.connection.commit()

        # APP ACCOUNT MANAGEMENT DATA
        self.app_data['account_management'] = dict()
        self.app_data['account_management']['start_data'] = list()

        account_manage_results = self.execute_query(f"""SELECT month_year_account_id, month_year_id, month_id, account_id, amount FROM account_management_{self.user_id};""")

        for row in account_manage_results:
            account_mangement_obj = Account_Management(row)

            self.app_data['account_management']['start_data'].append(account_mangement_obj)

        self.connection.commit()

        # APP GOAL DATA
        self.app_data['goals'] = dict()
        self.app_data['goals']['start_data'] = list()

        goal_results = self.execute_query(f"""SELECT goal_id, goal_description, goal_account_id, goal_asset, goal_amount,
                    goal_perc, goal_start_date, goal_end_date, goal_complete
                    FROM goals_{self.user_id};""")

        for row in goal_results:
            goal_obj = Goal(row)

            self.app_data['goals']['start_data'].append(goal_obj)

        self.connection.commit()
        
        # APP PAYBACK DATA
        self.app_data['payback'] = dict()
        self.app_data['payback']['start_data'] = list()

        payback_results = self.execute_query(f"""SELECT payback_id, payback_name, payback_description, payback_amount, paid_back_amount
                    FROM payback_{self.user_id};""")

        for row in payback_results:
            payback_obj = Payback(row)

            self.app_data['payback']['start_data'].append(payback_obj)

        self.connection.commit()

        # APP FREQUENCY DATA
        self.app_data['frequency'] = dict()
        self.app_data['frequency']['start_data'] = list()

        frequency_results = self.execute_query(f"""SELECT frequency_id, frequency, frequency_month, frequency_days FROM frequency_{self.user_id};""")

        for row in frequency_results:
            frequency_obj = Frequency(row)

            self.app_data['frequency']['start_data'].append(frequency_obj)

        self.connection.commit()
        
        # APP States DATA
        self.app_data['states'] = dict()
        self.app_data['states']['start_data'] = list()

        states_results = self.execute_query(f"""SELECT state_id, state_name, state_abbreviation FROM states_{self.user_id};""")

        for row in states_results:
            states_obj = States(row)

            self.app_data['states']['start_data'].append(states_obj)

        self.connection.commit()
        
        # APP STATE INCOME TAXES DATA
        self.app_data['state_income_tax'] = dict()
        self.app_data['state_income_tax']['start_data'] = list()

        state_income_tax_results = self.execute_query(f"""SELECT year, state_id, single_filer_rates,
                            single_filer_brackets, married_filing_jointly_rates, married_filing_jointly_brackets,
                            standard_deduction_single, standard_deduction_couple, personal_exemption_single,
                            personal_exemption_couple, personal_exemption_dependent
                            FROM states_income_tax_{self.user_id};""")

        for row in state_income_tax_results:
            state_inc_tax_obj = States_Income_Taxes(row)

            self.app_data['state_income_tax']['start_data'].append(state_inc_tax_obj)
        
        self.app_data['state_income_tax']['new'] = self.app_data['state_income_tax']['start_data']

        self.connection.commit()
        
        # EXTRA DATA RELATED TO APP
        
    def insert_data(self, constructor: str, model: typing.Union[Transaction, Month_Budget, Accounting_Type, Sub_Category,
                                                                Category, Account, Category_Type, App_Month, Account_Management,
                                                                Goal, Frequency, States, States_Income_Taxes, Payback]):
        values = model.insert_data(self.app_data)
        self.execute_update(constructor, values)
        
    def clear_unsave_data(self):
        for ls in self.app_data['unsaved_data'].keys():
            self.app_data['unsaved_data'][ls].clear()
        
    def delete_data(self, constructor: str, model: typing.Union[Transaction, Month_Budget, Accounting_Type, Sub_Category,
                                                                Category, Account, Category_Type, App_Month, Account_Management,
                                                                Goal, Frequency, States, States_Income_Taxes, Payback]):
        values = model.delete_data(self.app_data)
        self.execute_update(constructor, values)
    
    def update_data(self, constructor: str, model: typing.Union[Transaction, Month_Budget, Accounting_Type, Sub_Category,
                                                                Category, Account, Category_Type, App_Month, Account_Management,
                                                                Goal, Frequency, States, States_Income_Taxes, Payback]):
        values = model.update_data(self.app_data)
        self.execute_update(constructor, values)
            
    def month_budget_check_stats(self, parent, year: str):
        # if no data is entered in the database for month budget
        """
        Gets month budget data to be utilized by the
        application upon start up.
        Returns: pd.dataframe
        """
        #print(self)

        # Test 1
        m_int_list = [rvar.month_dict[m_int] for m_int in rvar.MONTHS_SHORT_DICT.values()]
        for month in m_int_list:
            month_budget = next(
                (
                    mon_budg for mon_budg in self.app_data['month_budget']['start_data'] if mon_budg.month == month and mon_budg.year == int(year)
                    ),
                False
                )
            if month_budget:
                break

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
                            month_info for month_info in self.app_data['month_budget']['start_data'] if month_info.month == month_int and month_info.year == year
                            ),
                        False
                        )

                    # Test 2
                    if not month_budget:

                        month_budget_id = int((int(month_int) * 10000) + int(year))

                        month_attr = [month_budget_id, month_int, Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00), Decimal(0.00)]
                        month_data = Month_Budget(month_attr)  ### REFERENCE ###
                        self.app_data['month_budget']['start_data'].append(month_data)
                        self.app_data['unsaved_data']['INSERT'].append(month_data)

                QMessageBox.information(parent, "Success",
                                f"Data has been successfully created for the year {year}.",
                                QMessageBox.StandardButton.Ok)

                return True

            # If user chooses not to add psuedo data
            elif ret == QMessageBox.StandardButton.Cancel:

                return False

        return True