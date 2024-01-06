# This is were the main program is managed

########## Python IMPORTs  #############################################################
#import os
########################################################################################

##########  Python IMPORTs  ############################################################
from PyQt6.QtWidgets import QMainWindow
#import sys
import psycopg2 as pg2
from psycopg2 import sql
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.budget import Budget
########################################################################################

class Root:
    def __init__(self, Form: QMainWindow, logger, user_id):
        self.user_id = user_id
        pwd = rfunc.pwd_retrieval()
        
        self.create_database_if_not_exists('Budget_App', pwd)
        self.conn = pg2.connect(database='Budget_App', user='postgres', password=pwd)
        logger.debug("Connecting to database successful")
        
        self.ui = Budget(Form, 
                       logger,
                       self.conn,
                       self.user_id)
        Form.show()
        
    def create_database_if_not_exists(database_name, password):
        # Connect to the default PostgreSQL database
        conn = pg2.connect(user='postgres', password=password)
        conn.autocommit = True

        # Check if the database already exists
        with conn.cursor() as cursor:
            cursor.execute(
                sql.SQL("SELECT 1 FROM pg_database WHERE datname = {}").format(sql.Identifier(database_name))
            )
            exists = cursor.fetchone()

            if not exists:
                # Create the database if it doesn't exist
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))

        # Close the connection to the default database
        conn.close()