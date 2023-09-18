##########  Python IMPORTs  ############################################################
from pathlib import Path
########################################################################################

##########  Python THIRD PARTY IMPORTs  ################################################
from PyQt6.QtWidgets import (QMainWindow, 
                             QWidget, 
                             QMessageBox, 
                             QStackedWidget, 
                             QWidget,
                             QGridLayout,
                             QLabel,
                             QGraphicsOpacityEffect)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import (Qt, 
                          QPoint, 
                          QRect,
                          QEasingCurve, 
                          QPropertyAnimation, 
                          QParallelAnimationGroup, 
                          QSequentialAnimationGroup)
########################################################################################

##########  Created files IMPORTS  #####################################################
import root.helper.root_functions as rfunc
import root.helper.root_variables as rvar
from root.component.ui.side_menu import Ui_Form
# from pages.dashboard import Dashboard
########################################################################################

class Side_Menu(Ui_Form):
    def __init__(self, parent): # , database):
        # Create header widget for Dashboard
        # Mainwindow -> central widget -> StackWidget -> Dashboard Page
        # -> header_widget
        super().__init__()
        self.side_menu_widget = QWidget(parent=parent)
        self.setupUi(self.side_menu_widget)
        self.side_menu_widget.setGeometry(QRect(-300, 50, 300, 1030))
        self.effect = QGraphicsOpacityEffect(self.side_menu_widget)
        self.side_menu_widget.setGraphicsEffect(self.effect)
        
         # Appearing animation movement
        self.show_animation = QPropertyAnimation(self.side_menu_widget, b"pos")
        self.show_animation.setEndValue(QPoint(-30, 50))
        self.show_animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.show_animation.setDuration(1000)  # time in ms
        
        # Appearing animation opacity
        self.show_opacity_animation = QPropertyAnimation(self.effect, b"opacity")
        self.show_opacity_animation.setStartValue(0)
        self.show_opacity_animation.setEndValue(1)
        self.show_opacity_animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.show_opacity_animation.setDuration(1000)
        
        # Grouping appearing animation together to occur simultaneously
        self.anim_group_appear = QParallelAnimationGroup()
        self.anim_group_appear.addAnimation(self.show_animation)
        self.anim_group_appear.addAnimation(self.show_opacity_animation)
        
        # Disappering animation movement
        self.disappear_animation = QPropertyAnimation(self.side_menu_widget, b"pos")
        self.disappear_animation.setEndValue(QPoint(-300, 50))
        self.disappear_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.disappear_animation.setDuration(1200)  # time in ms
        
        # Disappering animation opacity
        self.disappear_opacity_animation = QPropertyAnimation(self.effect, b"opacity")
        self.disappear_opacity_animation.setStartValue(1)
        self.disappear_opacity_animation.setEndValue(0)
        self.disappear_opacity_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.disappear_opacity_animation.setDuration(1200)
        
        # Grouping disappearing animation together to occur simultaneously
        self.anim_group_disappear = QParallelAnimationGroup()
        self.anim_group_disappear.addAnimation(self.disappear_animation)
        self.anim_group_disappear.addAnimation(self.disappear_opacity_animation)
        
    def appear(self):
        self.anim_group_appear.start()
        
    def disappear(self):
        self.anim_group_disappear.start()