########## Python IMPORTs  #############################################################
import os
import sys
########################################################################################

########## Third Party Python IMPORTs  #################################################
from PyQt6.QtWidgets import QMessageBox
import psycopg2 as pg2
########################################################################################

##########  Created files IMPORTS  #####################################################
from login_controls.utils.cryptography_helper import Login_Cryptography 
# UIs
from login_controls.gui.login import Login
from login_controls.gui.create_account import Create_Account
########################################################################################

class LoginWindow(Login):
    """
    This handles the login window functionality
    from the pyuic6 generated login.ui
    
    Ultimately returns: accept()
    
    else: None
    
    Thread: Main Thread
    """
    def __init__(self, logger):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login Window")
        self.log = logger
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_create_account.clicked.connect(self._creating_account)
        self.start = False
        
        self._initializer()
        
    
    def _initializer(self):
        try:
            # 1. Initiate Login_Cryptography 
            self._crypto = Login_Cryptography()
            
            pg_directory = os.path.join("C:\\Users", "D'Andre House", "Codes", "PGA")
            
            if os.path.exists(pg_directory):
                # Key
                k_file = open(pg_directory + '\k.txt')
                key = ''.join(k_file.readlines())
                key = bytes(key, 'utf-8')
                k_file.close()
                
                # Password
                p_file = open(pg_directory + '\w.txt')
                pwd = ''.join(p_file.readlines())
                pwd = bytes(pwd, 'utf-8')
                p_file.close()
                
                self.passwd = self._crypto.decrypt(pwd, key)
            else:
                print(f"could not find file directory {pg_directory}")
                Exception
            
            # 2. This connects to Log_connect database
            self.conn = pg2.connect(database='Budget_USER', user='postgres', password=self.passwd)
            
            # 3. Creates Table if it does not exist
            self.cur = self.conn.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS login 
                                       (user_id SERIAL UNIQUE PRIMARY KEY, 
                                       username_key BYTEA NOT NULL, 
                                       username BYTEA UNIQUE NOT NULL, 
                                       budget_password BYTEA NOT NULL, 
                                       budget_password_key BYTEA NOT NULL)""")
            self.conn.commit()
    
            # 4. Gets database login data
            self.cur.execute("SELECT username_key, username, budget_password_key, budget_password, user_id FROM login")
            # Remember for this list username is 0 element, password is 1 element
            self._sql_login_data = self.cur.fetchall()
            self.conn.commit()
            self.lineEdit_username.setText('DHouse185')
                        
            self.closeEvent = self.close_Event
            
            if not self._sql_login_data:
                button = QMessageBox.question(self, "No Login Information",
                                    "Welcome! There does not seem to be any login information."
                                    + " This must be your first time using the application.\n\n"
                                    + "Please create a new account."
                                    + " Clicking close will exit the program", 
                                    QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
                
                if button == QMessageBox.StandardButton.Ok:
                    self._creating_account()
                elif button == QMessageBox.StandardButton.Close:
                    self.conn.close()
                    # signals to login_handler to close application
                    self.button_close_event = True
                    sys.exit()
            
            if self._sql_login_data:
                self.start = True
                # application will not close as long as this is 0
                self.button_close_event = False
                    
        except Exception as e:
            self.log.error("An error occurred")
            self.log.error(e)
    
    def close_Event(self, event):
        """
        Custom close event handler\n
        closes:\n
        Main Application\n
        Binance US websocket
        """
        self.conn.close()
        event.accept()
        self.destroy()
        if self.exec() != 1:
            sys.exit()
    
    def login(self):
        """"
        Emmitted when Login button is clicked
        Will check if username or password exist
        """
        try:
            for element in self._sql_login_data:
                if self.lineEdit_username.text() == self._crypto.decrypt(bytes(element[1]), bytes(element[0])): 
                    if self.lineEdit_password.text() == self._crypto.decrypt(bytes(element[3]), bytes(element[2])):
                        self.user_id = element[4]
                        self.accept()
                        self.conn.close() # Will connect to a different database in budget program
                    else:
                        QMessageBox.warning(self, "Wrong username or password",
                                    "Either the username or password is incorrect")
                else: 
                    QMessageBox.warning(self, "Wrong username or password",
                                        "Either the username or password is incorrect")
        except Exception as e:
            self.log.error(e)
            
    def _creating_account(self):
        """
        From the LoginWindow class Create Account Window is called
        """
        self.account_creation = CreateAccount(self.conn, self.log, self)
        self.account_creation.show()
            
class CreateAccount(Create_Account):
    """
    This Window allows the user to create a new account
    with a new password.
    
    Thread: Main Thread
    """
    def __init__(self, sql_connect, logger, login: LoginWindow):
        super().__init__()
        self.setupUi(self)
        self.closeEvent = self.close_Event
        self.sql_connection = sql_connect
        self.log = logger
        self.login = login
        self._initializer()
        self.pushButton_create.clicked.connect(self.create_account)
    
    def _initializer(self):
        # 1. Initiate Login_Cryptography 
        self._crypto = Login_Cryptography()
        self.setWindowTitle("Create Account")
        self.move(self.pos().x() + 500, self.pos().y() + 200)
        
    def create_account(self):
        """
        Checks and validates user's input for creating a new account.
        If valid returns new username and password to database
        """
        try:
            username = self.lineEdit_username.text() 
            password = self.lineEdit_password.text()
            confirm_password = self.lineEdit_password_2.text()
            
            if username == "":
                # Prevent user from entering blank username 
                QMessageBox.warning(self, "Error",
                                    "Username Cannot Be Empty!")
            elif password == "" or confirm_password == "":
                # Prevent user from entering blank password 
                QMessageBox.warning(self, "Error",
                                    "Password Cannot Be Empty!")
            elif password != confirm_password:
                # Prevent user from misstyping intended password 
                QMessageBox.warning(self, "Error",
                                    "Confirmation Password does not match Pasword!")
            else: 
                username_key, username = self._crypto.encrypt_it(username)
                password_key, password = self._crypto.encrypt_it(password)
                # Inserting encryption and their key to sql database
                save_user_pass_query = """INSERT INTO login (username_key, username, budget_password_key, budget_password)
                    VALUES (%s, %s, %s, %s)""" 
                binary_tuple = (username_key, username, password_key, password,)
                self.cur = self.sql_connection.cursor()
                self.cur.execute(save_user_pass_query, binary_tuple)
                
                # Commit Change
                self.sql_connection.commit()
                q_button = QMessageBox.information(self, "Account Created",
                                    """Welcome! Account has been successfully created!\n
                                    Please reload the application.""", 
                                    QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                if q_button.Ok:
                    self.close()
                    
        except Exception as e:
            self.log.error(e)
            
    def close_Event(self, event):
        """
        Custom close event handler\n
        closes:\n
        Main Application\n
        Binance US websocket
        """
        self.sql_connection.close()
        event.accept()
        self.destroy()