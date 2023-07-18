# This is were the main program is managed

########## Python IMPORTs  #############################################################
import os
########################################################################################

##########  Python IMPORTs  ############################################################
from PyQt6.QtWidgets import QMainWindow
import sys
import psycopg2 as pg2
########################################################################################

##########  Created files IMPORTS  #####################################################
import helper.root_functions as rfunc
import helper.root_vriables as rvar
from budget import Budget
########################################################################################

class Root:
    def __init__(self, logger, user_id):
        self.user_id = user_id
        pwd = rfunc.pwd_retrieval()
        
        self.conn = pg2.connect(database='Budget', user='postgres', password=pwd)
        logger.debug("Connecting to database successful")
        
        self.Form = QMainWindow()
        self.ui = Budget(self.Form, 
                       logger,
                       self.conn)
        self.Form.show()
        
        
