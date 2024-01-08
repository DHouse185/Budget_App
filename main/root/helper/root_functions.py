########## Python IMPORTs  #############################################################
import os
import typing
from datetime import datetime
########################################################################################

########## Third Party Python IMPORTs  #################################################
from cryptography.fernet import Fernet
from PyQt6.QtWidgets import QWidget, QMessageBox
########################################################################################

##########  Created files IMPORTS  #####################################################
from root.models import (Transaction, Month_Budget, Accounting_Type, Sub_Category,
                         Category, Account, Category_Type, App_Month, Account_Management,
                         Goal, Frequency, States, States_Income_Taxes, Payback)
import root.helper.root_variables as rvar
########################################################################################

def unsave_message(parent: QWidget, unsaved_data_list: typing.List) -> bool:
    for changes in unsaved_data_list.values():
        if changes != []:
            unsaved_detected = True
            break
        else:
            unsaved_detected = False
             
    if unsaved_detected:
        message = 'The following data has not been saved yet. Would you like to save it?\n'
        for change_type in unsaved_data_list.keys():
            if change_type == 'INSERT':
                for model_type in unsaved_data_list[change_type]:
                    if model_type.__class__ == Transaction:
                        message += "\n".join([f"Add Transaction {model_type.description} - Amount: {model_type.amount} Account: {model_type.account} Date: {model_type.date} Type: {model_type.accounting_type}\n" ])
                    if model_type.__class__ == Month_Budget:
                        message += "\n".join([f"Add Monthly Budget data for {model_type.month_name} {model_type.year}\n"])
                    if model_type.__class__ == Account:
                        message += "\n".join([f"Add Account {model_type.account}\n"])
                    if model_type.__class__ == Account_Management:
                        message += "\n".join([f"Add Account data for {model_type.account_name} in {next((key for key, value in rvar.month_dict.items() if value == model_type.month_id), 'Year Starting Amount')} for the year {model_type.year}: Amount - {model_type.amount}\n"])
                    if model_type.__class__ == Category:
                        message += "\n".join([f"Add Category {model_type.category}\n"])
                    if model_type.__class__ == Sub_Category:
                        message += "\n".join([f"Add Sub Category {model_type.sub_category}\n"])                                                
            elif change_type == 'DELETE':
                for model_type in unsaved_data_list[change_type]:
                    if model_type.__class__ == Transaction:
                        message += "\n".join([f"Delete Transaction {model_type.description} - Amount: {model_type.amount} Account: {model_type.account} Date: {model_type.date} Type: {model_type.accounting_type}\n" ])
                    if model_type.__class__ == Month_Budget:
                        message += "\n".join([f"Delete Monthly Budget data for {model_type.month_name} {model_type.year}\n"])
                    if model_type.__class__ == Account:
                        message += "\n".join([f"Delete Account {model_type.account}\n"])
                    if model_type.__class__ == Account_Management:
                        message += "\n".join([f"Delete Account data for {model_type.account_name} in {next((key for key, value in rvar.month_dict.items() if value == model_type.month_id), 'Year Starting Amount')} for the year {model_type.year}: Amount - {model_type.amount}\n"])
                    if model_type.__class__ == Category:
                        message += "\n".join([f"Delete Category {model_type.category}\n"])
                    if model_type.__class__ == Sub_Category:
                        message += "\n".join([f"Delete Sub Category {model_type.sub_category}\n"])                                                                        
            elif change_type == 'UPDATE':
                for model_type in unsaved_data_list[change_type]:
                    if model_type.__class__ == Month_Budget:
                        message += "\n".join([f"Update Monthly Budget data for {model_type.month_name} {model_type.year}\n"])
                    if model_type.__class__ == Transaction:
                        message += "\n".join([f"Update Transaction {model_type.description} - Amount: {model_type.amount} Account: {model_type.account} Date: {model_type.date} Type: {model_type.accounting_type}\n" ])
                    if model_type.__class__ == Account:
                        message += "\n".join([f"Update Account {model_type.account}\n"])
                    if model_type.__class__ == Account_Management:
                        message += "\n".join([f"Update Account data for {model_type.account_name} in {next((key for key, value in rvar.month_dict.items() if value == model_type.month_id), 'Year Starting Amount')} for the year {model_type.year}: Amount - {model_type.amount}\n"])
                    if model_type.__class__ == Category:
                        message += "\n".join([f"Update Category {model_type.category}\n"])
                    if model_type.__class__ == Sub_Category:
                        message += "\n".join([f"Update Sub Category {model_type.sub_category}\n"])                                                                        

        ret = QMessageBox.question(parent, "Unsaved Data", message, QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if ret == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
        
def decrypt(text, key):
        """"
        Description: This program will read the key and encrypted pwd generated
        by GenerateEncryptedKey program. Can be executed multiple time.
        """
        ### 1. read encrypted pwd and convert into byte
        encpwdbyt = text
        ### 2. read key and convert into byte
        refKeybyt = key
        ### 3. use the key and encrypt pwd
        keytouse = Fernet(refKeybyt)
        myPass = (keytouse.decrypt(encpwdbyt))
        
        return str(myPass.decode('utf-8'))
        
def encrypt_it(text: str):
    """
    Encrypts a string that was passed to this function
    
    Returns: key -> string
                encryption -> string
    """
    from cryptography.fernet import Fernet
    ### 1. generate key and write it in a file
    key = Fernet.generate_key()
    ### 2. encrypt the password and write it in a file
    refKey = Fernet(key)
    mypwdbyt = bytes(text, 'utf-8') # convert into byte
    encryptedPWD = refKey.encrypt(mypwdbyt)
    ### 3. return key and encrypted password
    return key, encryptedPWD

def pwd_retrieval() -> str:
    pg_directory = os.path.join("C:\\Users", "D'Andre House", "Codes", "PGA")
    try:    
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
            
            passwd = decrypt(pwd, key)
            
            return passwd
        else:
            Exception
            
    except Exception:
        # For Debugging purposes
        print("Could not access files to access the database")
        
def number_of_days(date_1: datetime, date_2: datetime):  
        return (date_2 - date_1).days 
    
def query_print_results(query_function):
    def commit(*args, **kwargs):
        query_results = query_function(*args, **kwargs)
        
        # For Debugging purposes        
        #print(query_results)
                
        return query_results
                
    return commit