##########  Python IMPORTs  ############################################################
from pathlib import Path
import datetime
import pandas as pd
import os
########################################################################################

root_util_directory = os.path.dirname(__file__)
DARK_MODE = os.path.join(root_util_directory, "style", "darkmode_style.qss")
DARK_MODE_TRANS_TABLE = ("""QTableView {\n
                         alternate-background-color: #9f9f9f;\n
                        }\n
                         QTableView QHeaderView {\n
                            border-bottom: 2px solid white;\n
                        }\n
                        QTableView QHeaderView::section {\n
                            color: #ffffff;\n
                            background: #000000;\n
                            border: 2px;\n
                        }\n
                        QTableView QTableCornerButton::section {\n
                            color: #ffffff;\n
                            background: #000000;\n
                            border-bottom: 2px solid white;\n
                        }""")
month_dict ={
    'January'  : 1,
    'February' : 2,
    'March'    : 3,
    'April'    : 4,
    'May'      : 5,
    'June'     : 6,
    'July'     : 7,
    'August'   : 8,
    'September': 9,
    'October'  : 10,
    'November' : 11,
    'December' : 12,
}