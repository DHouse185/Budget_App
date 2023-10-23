##########  Python IMPORTs  ############################################################
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
########################################################################################

##########  Created files IMPORTS  #####################################################
from login_controls.login_interface import LoginWindow
from root.root_file import Root
########################################################################################

class Start:
    def __init__(self, log):
        app = QApplication(sys.argv)
        login = LoginWindow(log)
        
        if login.start:
            if not login.button_close_event:
                # For Debugging purposes
                print("entered")
                login.show()
        
            if login.exec() == 1:
                Form = QMainWindow()
                user_id = login.user_id
                self.initiate_program(log, user_id, Form)

            else:
                login.reject()
                
        # Stops application from closing upon initialization    
        sys.exit(app.exec()) 
            
    def initiate_program(self, log, user_id, Form):
        # For Debugging purposes
        print("success")
        root_h = Root(Form, log, user_id)