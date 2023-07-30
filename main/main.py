# This is the start of the budget platform.
# You should be able to manage your budget
# and analyze where your money is going. 
# This progran should also help with planning expesnses as well
# Good Luck! 
# Please do not edit this file

##########  Python IMPORTs  ############################################################
from PyQt6.QtWidgets import QApplication
import sys
########################################################################################

##########  Created files IMPORTS  #####################################################
import logger
from login_controls.login_interface import LoginWindow
#from root.root import Root
########################################################################################

# Set up logger
log = logger.main()
# log.debug()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    login = LoginWindow(log)
    
    if login.button_close_event == 0:
        login.show()
        
    if login.exec() == 1:
        user_id = login.user_id
        print("success")
        #root_h = Root(log, user_id)
        
    else:
        login.reject()
    
    # Stops application from closing upon initialization
    sys.exit(app.exec())
