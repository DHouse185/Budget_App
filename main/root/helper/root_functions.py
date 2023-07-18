########## Python IMPORTs  #############################################################
import os
########################################################################################

########## Third Party Python IMPORTs  #################################################
from cryptography.fernet import Fernet
########################################################################################

##########  Created files IMPORTS  #####################################################

########################################################################################

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
    pg_directory = os.path.join("C:", "Users", "D'Andre House", "Codes", "PGA")
    try:    
        if os.path.exists(pg_directory):
            # Key
            k_file = open(pg_directory + '\k.txt')
            key = k_file.read()
            k_file.close()
            
            # Password
            p_file = open(pg_directory + '\w.txt')
            pwd = p_file.read()
            p_file.close()
            
            passwd = decrypt(pwd, key)
            
            return passwd
        else:
            Exception
            
    except Exception:
        print("Could not access files to access the database")