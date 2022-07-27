# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:15:41 2021

@author: Test
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from objectViewerWidgetUI import Ui_objectViewerWidget
from datetime import datetime

from PyQt5.QtCore import Qt 

from collections import abc
import numbers
import pandas as pd

OBJECT_DATA_ROLE = Qt.UserRole + 0

class objectViewerWidget(QtWidgets.QWidget, Ui_objectViewerWidget):
    #class attributes - act as constants
    OBJECT_TYPE = 0
    COLLECTION_TYPE = 1
    PANDAS_TYPE = 2
    
    def __init__(self, 
                 
                 *args, 
                 **kwargs):
        super(objectViewerWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        if(self.parent() == None):
            self.layout().setContentsMargins(9,9,9,9)
        
        self.treeModel = QtGui.QStandardItemModel()
        self.tableModel = QtGui.QStandardItemModel()
        
        self.stack = []
        

        
        
        self.treeView.setModel(self.treeModel)
        self.tableView.setModel(self.tableModel)
        
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.treeView.activated.connect(self.__treeView_item_entered)
        self.tableView.activated.connect(self.__tableView_item_entered)
        
        self.tableView.hide()
        self.treeView.hide()
        self.optionsButton.hide()

        
        self.specials_populate = False
        self.callables_populate = False
        self.private_populate = False
        self.show_primitive_members = False
        
        
        
        
        self.optionmenu = QtWidgets.QMenu(self)
        
        self.callable_action = self.optionmenu.addAction('Callable members')
        self.callable_action.setCheckable(True)
        self.callable_action.setChecked(self.callables_populate)
        self.callable_action.toggled.connect(self.__callables_state_changed)
        
        self.special_action = self.optionmenu.addAction('__special__ members')
        self.special_action.setCheckable(True)
        self.special_action.setChecked(self.specials_populate)
        self.special_action.toggled.connect(self.__specials_state_changed)
        
        self.private_action = self.optionmenu.addAction('__private members')
        self.private_action.setCheckable(True)
        self.private_action.setChecked(self.private_populate)
        self.private_action.toggled.connect(self.__private_state_changed)
        
        self.primitive_action = self.optionmenu.addAction('primitive members')
        self.primitive_action.setCheckable(True)
        self.primitive_action.setChecked(self.show_primitive_members)
        self.primitive_action.toggled.connect(self.__primitive_state_changed)
        
        upIcon = QtGui.QIcon("icons\\upLevel_icon_16px.png")
        self.upLevelToolButton.clicked.connect(self.__up_level)
        self.upLevelToolButton.setIcon(upIcon)
        
        self.optionsButton.setMenu(self.optionmenu)
        
        self.child_widgets = []
        
        
        # icon = QtGui.QIcon("icons/upLevel_icon_16px.png")
        # self.upLevelButton.setIcon(icon)
       


    def set_object_data(self,
        obj, name,
        open_children = True,
        open_child_in_same_widget = False, 
        callables_populate = False,
        specials_populate = False,  
        private_populate = False,
        show_primitive_members = False,
        hide_options = False):
        
        if type(obj) == None:
            return
        
        self.obj = obj
        self.name = name
        self.setWindowTitle(self.name)
        self.optionsButton.show()
        if((type(self.obj) == pd.DataFrame) or (type(self.obj) == pd.Series)):
            #print("pandas type")
            self.obj_type = self.PANDAS_TYPE
            self.tableView.show()
            self.treeView.hide()
            self.optionsButton.setEnabled(False)
        elif(isinstance(self.obj, abc.Collection) and not isinstance(self.obj, str)):
            self.obj_type = self.COLLECTION_TYPE
            self.tableView.show()
            self.treeView.hide()
            self.optionsButton.setEnabled(False)
        else:
            self.obj_type = self.OBJECT_TYPE
            self.tableView.hide()
            self.treeView.show()
            self.optionsButton.setEnabled(True)      
        
        
        
        if(hide_options == True):
            self.optionsLayout.hide()
            open_child_in_same_widget = False
        else:
            self.optionsLayout.show()
            pass
        
        if((self.stack == []) or (open_child_in_same_widget == False) or (open_children == False)):
            self.upLevelToolButton.hide()
        else:
            self.upLevelToolButton.show()
        
        self.open_children = open_children
        self.open_child_in_same_widget = open_child_in_same_widget
        self.specials_populate = specials_populate
        self.callables_populate = callables_populate
        self.private_populate = private_populate
        self.show_primitive_members = show_primitive_members
        self.hide_options = hide_options
        
        self.callable_action.setChecked(self.callables_populate)
        self.special_action.setChecked(self.specials_populate)
        self.private_action.setChecked(self.private_populate)
        self.primitive_action.setChecked(self.show_primitive_members)

              
        self.__populate()
    


            
    def __private_state_changed(self,state):
        self.private_populate =  state       
        self.__populate()
        
    def __callables_state_changed(self,state):
        self.callables_populate = state        
        self.__populate()
        
    def __specials_state_changed(self,state):
        self.specials_populate = state        
        self.__populate()
        
    def __primitive_state_changed(self,state):
        self.show_primitive_members = state        
        self.__populate()
        
    def __populate(self):     
        if(self.obj_type == self.OBJECT_TYPE):
            self.__populate_tree()
        elif(self.obj_type == self.COLLECTION_TYPE):
            self.__populate_table()
        elif(self.obj_type == self.PANDAS_TYPE):
            self.__populate_pandas()
        return
        
    def __populate_tree(self):      
        self.treeModel.clear()
        self.treeModel.setHorizontalHeaderLabels(['Name','Type','Size','Value','Path'])
        
        self.treeView.header().resizeSection(0,118)
        self.treeView.header().resizeSection(1,75)
        self.treeView.header().resizeSection(2,39)
        self.treeView.header().resizeSection(3,221)
        #self.treeView.header().resizeSection(4,126)
        
        rootItem = self.treeModel.invisibleRootItem()
        child_row = self.__recursive_add_item(self.obj, self.name, self.name, False)        
        rootItem.appendRow(child_row) #add all data to tree
        self.treeView.expand(child_row[0].index()) #expands to first level
        
    
    def __recursive_add_item(self, obj_to_add, name, path, special):
        
        nameItem = QtGui.QStandardItem(name)
        nameItem.setData(obj_to_add, OBJECT_DATA_ROLE)
        typeItem = QtGui.QStandardItem(str(type(obj_to_add).__name__))
        
        try:
            size = str(len(obj_to_add))
        except:
            size = "1"
        sizeItem = QtGui.QStandardItem(size)
        valueItem = QtGui.QStandardItem(str(obj_to_add))

        pathItem = QtGui.QStandardItem(path)
        
        #by default all items are generic objects
        items = self.__get_object_attributes(obj_to_add, callables = self.callables_populate, specials = self.specials_populate, privates=self.private_populate)
        type_ = 'OBJECT'
        icon = QtGui.QIcon("icons//object_icon_12px.png")
        
        if(callable(obj_to_add)):
            icon = QtGui.QIcon("icons//method_icon_12px.png")
        elif(type(obj_to_add) == bool):
            icon = QtGui.QIcon("icons//bool_icon_12px.png")
        elif(type(obj_to_add) == str):
            icon = QtGui.QIcon("icons//string_icon_12px.png")
        elif(type(obj_to_add) == int):
            icon = QtGui.QIcon("icons//int_float_icon_12px.png")
        elif(type(obj_to_add) == float):
            icon = QtGui.QIcon("icons//float_icon_12px.png")
        elif(type(obj_to_add) == datetime):
            icon = QtGui.QIcon("icons//datetime_icon_12px.png")
        elif((type(obj_to_add) == pd.DataFrame) or (type(obj_to_add) == pd.Series)):
            icon = QtGui.QIcon("icons//dataframe_icon_12px.png")  
        elif(isinstance(obj_to_add, abc.Collection) and not isinstance(obj_to_add, str)):
            #this is a collection type, need to get the items
            items = self.__get_collection_items(obj_to_add) 
            if(isinstance(obj_to_add, abc.Mapping)):
                #dicts and mappings
                type_ = 'MAPPING'
                icon = QtGui.QIcon("icons//dict_icon_12px.png")
            elif(isinstance(obj_to_add, abc.Sequence)): 
                #lists and tuples
                type_ = 'SEQUENCE'
                icon = QtGui.QIcon("icons//list_icon_12px.png")
            elif(isinstance(obj_to_add,abc.Set)):
                type_ = 'SEQUENCE'
                icon = QtGui.QIcon("icons//list_icon_12px.png")
            else:
                type_ = 'SEQUENCE'
                icon = QtGui.QIcon("icons//list_icon_12px.png")

            
        typeItem.setIcon(icon)  
        
        if(special):
            #this is a special item, so do not do recursion for it
            return [nameItem, typeItem, sizeItem, valueItem, pathItem]
        elif(callable(obj_to_add)):
            #this is callable, no need for recursion
            return [nameItem, typeItem, sizeItem, valueItem, pathItem]
        elif(name == 'denominator' or name == 'numerator' or name == 'real' or name =='imag'):
            return [nameItem, typeItem, sizeItem, valueItem, pathItem]
        elif(str(type(obj_to_add).__name__) == 'DataFrame'):
            return [nameItem, typeItem, sizeItem, valueItem, pathItem]
        elif(type(obj_to_add) == datetime):
            return [nameItem, typeItem, sizeItem, valueItem, pathItem]
        elif((self.show_primitive_members == False) and (type(obj_to_add) == str or type(obj_to_add) == int or type(obj_to_add) == float or type(obj_to_add) == bool)):
            return [nameItem, typeItem, sizeItem, valueItem, pathItem]

        
        else:
            # print(name)
            # print(str(type(obj_to_add).__name__))
            for key in items:
                #print("key : " + str(key))
                item = items[key]
                if(self.__special(key) == True):
                    #print("no recusion for: " + str(key))
                    special_child = True
                else:
                    #print("recusion for: " + str(key))
                    special_child = False
    
                if(type_ == 'MAPPING'):
                    child_row = self.__recursive_add_item(item, '\'' + str(key) + '\'', path + '[\'' + str(key) + '\']', special_child)
                elif(type_ == 'SEQUENCE'):
                    child_row = self.__recursive_add_item(item, '[' + str(key) + ']', path + '[' + str(key) + ']',special_child)
                elif(type_ == 'OBJECT'):
                    child_row = self.__recursive_add_item(item, str(key), path + '.' + str(key), special_child)
    
                    
                nameItem.appendRow(child_row)
                
            return [nameItem, typeItem, sizeItem, valueItem, pathItem]
        
    def __populate_pandas(self):
        self.tableModel.clear()
        
        index_column = [str(item) for item in list(self.obj.index)]
        if (type(self.obj) == pd.Series):
            columns = [self.obj.name] #just one column
            column = [QtGui.QStandardItem(str(value)) for value in list(self.obj)] 
            self.tableModel.appendColumn(column)
        else: #is a dataframe
            columns = (list(self.obj.columns))
            for col_name in self.obj:
                column = [QtGui.QStandardItem(str(value)) for value in list(self.obj[col_name])]            
                self.tableModel.appendColumn(column)
        
        self.tableModel.setHorizontalHeaderLabels(columns)
        self.tableView.verticalHeader().setVisible(True)
        self.tableModel.setVerticalHeaderLabels(index_column)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        return
        
    
    def __populate_table(self):
                
        self.tableModel.clear()   
        
        items = self.__get_collection_items(self.obj)

            
        for key in items:
            value = items[key] 
            
            
            keyItem = QtGui.QStandardItem(key)
            keyItem.setData(value, OBJECT_DATA_ROLE)
            typeItem = QtGui.QStandardItem(str(type(value).__name__))  #https://stackoverflow.com/questions/75440/how-do-i-get-the-string-with-name-of-a-class
            try:
                size = str(len(value))
            except:
                size = "1"
            sizeItem = QtGui.QStandardItem(size)
            valueItem = QtGui.QStandardItem(str(value))
            
            row = [keyItem, typeItem, sizeItem, valueItem]
            self.tableModel.appendRow(row)

        self.tableView.horizontalHeader().resizeSection(2,39)

        if(isinstance(self.obj,abc.MutableMapping)):
            #dict
            self.tableModel.setHorizontalHeaderLabels(['Key','Type','Size','Value'])
        elif(isinstance(self.obj,(abc.Sequence))):
            #lists and tuples
            self.tableModel.setHorizontalHeaderLabels(['Index','Type','Size','Value'])
        elif(isinstance(self.obj,abc.Set)):
            #sets
            self.tableModel.setHorizontalHeaderLabels(['Index (not indexable)','Type','Size','Value'])
            # self.tableModel.removeColumn(0) #not indexed        else:
            # self.tableModel.setHorizontalHeaderLabels(['Type','Size','Value'])
            
            
            
    def __special(self,attr_name):
        #tests if the attribute is a special (ie magic, dunder etc) attribute
        if(attr_name.startswith('__') and attr_name.endswith('__')):
            return True
        else: return False
        
    def __private(self,obj, attr_name):
        #tests if the attribute is private
        obj_name = type(obj).__name__
        if(attr_name.startswith('_' + obj_name + '__')):
            return True
        else: 
            return False
        
    def __get_collection_items(self,collection):
        #return the items in dict form
        #print("get_collection_items : " + str(collection))
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
            #unknown collection type
            return
        
        return items
        
        
    def __get_object_attributes(self, obj, callables = True, specials = True, privates = True):  
        item_keys = dir(obj)
        items = {item_key: getattr(obj, item_key) for item_key in item_keys}
        for item_key, item in items.copy().items():
            if(callable(item) and callables == False):
                del items[item_key]
            elif(self.__special(item_key) and specials == False):
                del items[item_key]
            elif(self.__private(obj, item_key) and privates == False):
                del items[item_key]
        return items
    
    
    def __treeView_item_entered(self, index):
        #print(str(index))
        
        #print("row: " + str(self.treeModel.itemFromIndex(index).row()) + ", col: " + str(self.treeModel.itemFromIndex(index).column()))
        row = self.treeModel.itemFromIndex(index).row()
        childDataItem = index.sibling(row,0)
        pathItem = index.sibling(row, 4)
        
        child_name = pathItem.data()

        if(child_name != self.name):
            self.__show_child_widget(childDataItem, child_name)           
        else:
            return
        
    def __tableView_item_entered(self,index):
        row = self.tableModel.itemFromIndex(index).row()
        #print(row)
        childDataItem = index.sibling(row,0)
        #print(childDataItem.data())
        child_key = childDataItem.data()
        
        
        if(isinstance(self.obj, abc.Mapping)):
            child_name = self.name + '[\'' + child_key + '\']'
           
        elif(isinstance(self.obj, abc.Sequence)): 
            #lists and tuples
            child_name = self.name + '[' + child_key + ']'
        elif(isinstance(self.obj,abc.Set)):
            #sets
            child_name = self.name + '[' + child_key + ']'
        else:
            #unknown collection type
            return
        
        self.__show_child_widget(childDataItem, child_name)    
        # pathItem = index.sibling(row, 4)
        
        # child_name = pathItem.data()
        

    
    def __show_child_widget(self, childDataItem, child_name):
        if(self.open_children == True):
            child_object = childDataItem.data(OBJECT_DATA_ROLE)     
            if(type(child_object) == None):
                return
            if(self.open_child_in_same_widget):
                self.upLevelToolButton.setEnabled(True)
                self.stack.append((self.obj, self.name)) #add to the stack
                self.set_object_data(child_object, child_name, self.open_children, self.open_child_in_same_widget, self.callables_populate, self.specials_populate,self.private_populate, self.show_primitive_members,self.hide_options)
                
            else:
                pos = self.pos()
                pos.setX(pos.x() + 30)
                pos.setY(pos.y() + 30)
                
                childObjectViewerWidget = objectViewerWidget()
                childObjectViewerWidget.set_object_data(child_object, child_name, self.open_children, self.open_child_in_same_widget, self.callables_populate, self.specials_populate,self.private_populate, self.show_primitive_members,self.hide_options)
                childObjectViewerWidget.move(pos)
                childObjectViewerWidget.show()
                
                self.child_widgets.append(childObjectViewerWidget)
        else:
            pass
            
    def __up_level(self):
        parent_object, parent_name = self.stack.pop()
        self.set_object_data(parent_object, parent_name, self.open_children, self.open_child_in_same_widget, self.callables_populate, self.specials_populate,self.private_populate, self.show_primitive_members,self.hide_options)
        
    def closeEvent(self, event):
        for widget in self.child_widgets:
            try:
                widget.close()
            except:
                pass
        super(objectViewerWidget, self).closeEvent(event)
    