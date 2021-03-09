# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:34:12 2021

@author: Test
"""
from objectViewerDialogUI import Ui_ObjectDialog
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import Qt 

from collections import abc
import numbers

from objectViewerWidget import objectViewerWidget

        
class objectViewerDialog(QtWidgets.QDialog, Ui_ObjectDialog):
    #class attributes - act as constants

    def __init__(self, obj, parent=None):
        super(objectViewerDialog,self).__init__(parent)
        self.setupUi(self)
        self.objectViewerWidget.set_object_data(obj)
        #self.verticalLayout.addWidget(self.mainWidget)
        # Create an instance of the GUI
        #self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
