##########  Python IMPORTs  ############################################################
from PyQt6.QtWidgets import QApplication
import sys
########################################################################################

##########  Created files IMPORTS  #####################################################
import logger
from login_controls.login_interface import LoginWindow
from root.root import Root
########################################################################################
# Set up logger
log = logger.main()

class Start:
    def __init__(self):
        
        login = LoginWindow(log)
        
        if login.start:
            if not login.button_close_event:
                print("entered")
                login.show()
        
            if login.exec() == 1:
                user_id = login.user_id
                print("success")
                root_h = Root(log, user_id)

            else:
                login.reject()
            
    