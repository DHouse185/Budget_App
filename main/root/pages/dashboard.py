##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import QMainWindow, QWidget, QMessageBox, QStackedWidget
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QRect
########################################################################################

##########  Created files IMPORTS  #####################################################
import helper.root_functions as rfunc
import helper.root_vriables as rvar
from pages.components.dashboard_header import Header 
########################################################################################



class Dashboard:
    """
    Dashboard page that contains and manage all components on the dashboard page
    """
    def __init__(self, page, database_conn):
        super().__init__()
        
        # self.db = Workspace()
        
        # self.notification = notification
        self.dashboard_page = page
        self.database_conn = database_conn
        
        self.header = Header(self.dashboard_page)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Create a widget that will contain all things related
        # to the Watchlist
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> watchlist_widget
        self.watchlist_widget = QWidget(self.dashboard_page)
        self.watchlist_widget.setObjectName(u"watchlist_widget")
        self.watchlist_widget.setGeometry(QRect(30, 130, 607, 706))
        
        # Command Frame will be the main layout of watchlist widget
        # Mainwindow -> central widget -> StackWidget -> Main Page
        # -> watchlist_widget -> _commands_frame
        self._commands_frame = QVBoxLayout(self.watchlist_widget) 
        self._commands_frame.setObjectName("Watchlist_Commands_frame")
        self._commands_frame.setSpacing(6)
        
        # This will be were all symbol ask and bid prices for a 
        # symbol will occur
        # Mainwindow -> central widget -> StackWidget -> Main Page
        # -> watchlist_widget -> _commands_frame -> watchlist_scrollArea
        # -> scrollAreaWidgetContents
        self.watchlist_scrollArea = QScrollArea()
        self.watchlist_scrollArea.setObjectName("Watchlist_scrollArea")
        self.watchlist_scrollArea.setWidgetResizable(True)
        self.watchlist_scrollArea.setMaximumSize(587, 620)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("watchlist_scrollAreaWidgetContents")
        
        # Creating a grid layout for headers, columns, and rows
        # Mainwindow -> central widget -> StackWidget -> Main Page
        # -> watchlist_widget -> _commands_frame -> watchlist_scrollArea
        # -> scrollAreaWidgetContents -> _headers_frame
        self._headers_frame = QGridLayout(self.scrollAreaWidgetContents)
        self._headers_frame.setObjectName("Watchlist_Headers_frame")
        self._headers_frame.setSpacing(0)
        self._headers_frame.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Applies an autocompleter when typing a pair in the LineEdit
        _binance_entry_autocompleter = QCompleter(self.binance_symbols)
        _binance_entry_autocompleter.popup().setStyleSheet("""background-color: #4d4d4d;
                                                           border: 2px solid #4d4d4d;
                                                           color: #ffffff;
                                                           padding: 5px;""")
        self._binance_entry.setCompleter(_binance_entry_autocompleter)
        
        # Enter button trigger to add symbol to watchlist
        self._binance_entry.returnPressed.connect(self._add_binance_symbol)
        
        # Applying widgets to _command frame. Order is important
        self._commands_frame.addWidget(self._binance_label)
        self._commands_frame.addWidget(self._binance_entry)
        self._commands_frame.addWidget(self.watchlist_scrollArea)
        
        # Creating headers for scrollAreaWidgetContents
        self._headers = ["symbol", "exchange", "bid", "ask", "remove"]
        
        # Create a list of QLabels for the number of headers 
        self._headers_labels = [QLabel() for _ in range(len(self._headers))]
        
        # Initiate body widget dictionary
        self.body_widgets = dict()
        
        # enumerate over QLabel list
        for idx, h in enumerate(self._headers_labels):
            
            # Give each header QLabel a setObjectName. Good for stylesheet
            h.setObjectName(f"label_{self._headers[idx]}")
            
            if self._headers[idx] == 'remove':
                h.setText("") # remove Qlabel isn't need initially
                
            else:
                h.setText(f"{self._headers[idx]}") # initiate headers text
                h.setMinimumWidth(200)
                
            self._headers_frame.addWidget(h, 0, idx) # remember, headers are in scroll area
            
        # Fill initiated dictionary with header dictionary     
        for h in self._headers:
            
            self.body_widgets[h] = dict()
            
            if h in ['bid', 'ask']:
                self.body_widgets[h + "_var"] = dict()
                
        # Important for where to add pair data in Scroll area
        # self._body_index = 0 is the header area    
        self._body_index = 1
        
        # saved_symbols = self.db.get("watchlist")
        # for s in saved_symbols:
        #     self._add_symbol(s['symbol'], s['exchange'])
        
        # Now we add the scrollAreaWidgetContents to watchlist_scrollArea
        self.watchlist_scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        # Push widgets up in watchlist_widget
        self._commands_frame.setAlignment(Qt.AlignmentFlag.AlignTop)