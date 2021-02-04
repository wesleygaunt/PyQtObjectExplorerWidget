# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:34:12 2021

@author: Test
"""
from Ui_ObjectDialog import Ui_ObjectDialog
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import Qt 

from collections import abc
import numbers
        
class ObjectExplorerDialog(QtWidgets.QDialog, Ui_ObjectDialog):
    #class attributes - act as constants
    OBJECT_TYPE = 0
    COLLECTION_TYPE = 1
    STRING_TYPE = 2
    NUMBER_TYPE = 3
    BOOL_TYPE = 4
    
    def __init__(self, obj, parent=None):
        super(ObjectExplorerDialog,self).__init__(parent)
        
        # Create an instance of the GUI
        #self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI

        self.setupUi(self)
        self.obj = obj
        
        
        
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Object Explorer - " + str(type(self.obj).__name__))
        self.typeLabel.setText(str(type(self.obj)))
        
        
        self.callablesCheckBox.stateChanged.connect(self.callables_state_changed)
        self.specialsCheckBox.stateChanged.connect(self.specials_state_changed)
        self.objectCheckBox.stateChanged.connect(self.object_view_state_change)
        self.privateCheckBox.stateChanged.connect(self.private_state_changed)
        self.MainTable.itemChanged.connect(self.itemChanged)
        
        self.specials_populate = False
        self.callables_populate = False
        self.private_populate = False
    
        
        if(isinstance(self.obj, (abc.Collection,str,numbers.Number,bool))):
            self.objectCheckBox.setVisible(True)
            self.callablesCheckBox.setEnabled(False)
            self.specialsCheckBox.setEnabled(False)
            self.privateCheckBox.setEnabled(False)
            self.view_as_object = False


            if(isinstance(self.obj, abc.Collection) and not isinstance(self.obj, str)):
                #collections
                self.obj_type = self.COLLECTION_TYPE
             
            #self.objectCheckBox.setChecked(True) #this will trigger collections state change and populate table
            elif(isinstance(self.obj,str)):
                #strings
                self.obj_type = self.STRING_TYPE
            
            elif(isinstance(self.obj,numbers.Number) and not isinstance(self.obj, bool)):
                #numerics
                self.obj_type = self.NUMBER_TYPE
            
            elif(isinstance(self.obj,bool)):
                #bools
                self.obj_type = self.BOOL_TYPE

        else:
            self.objectCheckBox.setVisible(False) #set hidden by default
            self.callablesCheckBox.setEnabled(True)
            self.specialsCheckBox.setEnabled(True)
            self.privateCheckBox.setEnabled(True)
            self.view_as_object = True
            self.obj_type = self.OBJECT_TYPE
 
        self.populate_table()
        

    def private_state_changed(self,state):
        if state == QtCore.Qt.Checked:
            self.private_populate = True
        else:
            self.private_populate = False
        
        self.populate_table()
        
    def callables_state_changed(self,state):
        if state == QtCore.Qt.Checked:
            self.callables_populate = True
        else:
            self.callables_populate = False
        
        self.populate_table()
        
    def specials_state_changed(self,state):
        if state == QtCore.Qt.Checked:
            self.specials_populate = True
        else:
            self.specials_populate = False
        
        self.populate_table()
    
    def object_view_state_change(self,state):
        if state == QtCore.Qt.Checked: #if checked, view as normal
            self.view_as_object = True
            self.callablesCheckBox.setEnabled(True)
            self.specialsCheckBox.setEnabled(True)
            self.privateCheckBox.setEnabled(True)
            
        else:
            self.view_as_object = False
            self.callablesCheckBox.setEnabled(False)
            self.specialsCheckBox.setEnabled(False)
            self.privateCheckBox.setEnabled(False)
        self.populate_table()
                   

    def itemChanged(self,item):
        row = item.row()
        column = item.column()
    
    def populate_table(self):
        self.MainTable.clear()   
        
        #create a dictionary which has the keys as the attribute names and the 
        if(self.view_as_object):
            items = self.get_object_attributes(self.obj, callables = self.callables_populate, specials = self.specials_populate, privates=self.private_populate)
        elif(self.obj_type == self.COLLECTION_TYPE):
            items = self.get_collection_items(self.obj)
        elif(self.obj_type == self.STRING_TYPE or self.obj_type == self.NUMBER_TYPE or self.obj_type == self.BOOL_TYPE):
            items = {1:str(self.obj)}
            
        rows = len(items)
        self.MainTable.setRowCount(rows)
        self.MainTable.setColumnCount(3)
        current_row = 0
        for key in items:
            
            value = items[key]       
                        
            key_item = QtWidgets.QTableWidgetItem(key)
            key_item.setFlags(key_item.flags() ^ Qt.ItemIsEditable) #make uneditable
            type_item = QtWidgets.QTableWidgetItem(str(type(value).__name__))  #https://stackoverflow.com/questions/75440/how-do-i-get-the-string-with-name-of-a-class
            type_item.setFlags(type_item.flags() ^ Qt.ItemIsEditable)
            value_item = QtWidgets.QTableWidgetItem(str(value))
            value_item.setFlags(value_item.flags() ^ Qt.ItemIsEditable)


            self.MainTable.setItem(current_row,0, key_item)
            self.MainTable.setItem(current_row,1, type_item) 
            self.MainTable.setItem(current_row,2, value_item)

            current_row = current_row + 1

        if(self.view_as_object == False):
            if(self.obj_type == self.COLLECTION_TYPE):
                if(isinstance(self.obj,abc.MutableMapping)):
                    self.MainTable.setHorizontalHeaderLabels(['Key','Type','Value'])
        
                elif(isinstance(self.obj,(abc.Sequence))):
                    self.MainTable.setHorizontalHeaderLabels(['Index','Type','Value'])
                    
                elif(isinstance(self.obj,abc.Set)):
                    #self.MainTable.setHorizontalHeaderLabels(['','Type','Value'])
                    if(self.MainTable.columnCount() != 2):
                        self.MainTable.removeColumn(0) #not indexed        else:
                        self.MainTable.setHorizontalHeaderLabels(['Type','Value'])
            elif(self.obj_type == self.STRING_TYPE or self.obj_type == self.NUMBER_TYPE or self.obj_type == self.BOOL_TYPE):
                if(self.MainTable.columnCount() != 1):
                    self.MainTable.removeColumn(0) #not indexed        else:
                    self.MainTable.removeColumn(0)
                    self.MainTable.setHorizontalHeaderLabels(['Value'])
                
        else:
            self.MainTable.setHorizontalHeaderLabels(['Name','Type','Value']) 
            
    def special(self,attr_name):
        #tests if the attribute is a special (ie magic, dunder etc) attribute
        if(attr_name.startswith('__') and attr_name.endswith('__')):
            return True
        else: return False
        
    def private(self,obj, attr_name):
        #tests if the attribute is private
        obj_name = type(obj).__name__
        if(attr_name.startswith('_' + obj_name + '__')):
            return True
        else: return False
        
    def get_collection_items(self,collection):
        if(isinstance(collection, abc.Mapping)): 
            items =  collection
                
        elif(isinstance(collection, abc.Sequence)): 
            #lists and tuples
            item_keys = range(0,len(collection))
            items = {str(item_key) : collection[item_key] for item_key in item_keys}
        elif(isinstance(collection,abc.Set)):
            #sets
            item_keys = range(0,len(collection))
            zip_items = zip(item_keys,collection)
            items = {str(item_key) : item for item_key, item in zip_items}
        else:
            print("unknown collection type")
            return
        return items
        
        
    def get_object_attributes(self, obj, callables = True, specials = True, privates = True):  
        item_keys = dir(obj)
        items = {item_key: getattr(obj, item_key) for item_key in item_keys}
        for item_key, item in items.copy().items():
            if(callable(item) and callables == False):
                del items[item_key]
            elif(self.special(item_key) and specials == False):
                del items[item_key]
            elif(self.private(obj, item_key) and privates == False):
                del items[item_key]
        return items


