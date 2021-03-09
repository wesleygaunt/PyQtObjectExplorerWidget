# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from objectViewerDialog import objectViewerDialog

import datetime

#create a test class with some methods
class newClass():
    def __init__(self,value):
        self.value = value
    def newClassFunction(self,function_arg):
        print("I'm a function")
    def __private_function(self):
        print("I'm a private function")


#objects to test:
object_ = newClass(10)
date = datetime.datetime(2020,1,1)
float_ = 1.0
int_ = 1
complex_ = complex(1,1)
string_ = "Hello, World!"
dict_ = {"1_key": complex_,"2_key":"2_val","func":datetime.datetime.now}
list_ = [1,2,3]
tuple_ = ("1_tuple_val",2,3)
set_ = {"set1_item", "2", 5}


app = QtWidgets.QApplication([])
#provide the objects as arguments to the dialog to see it working
dialog = objectViewerDialog(dict_)
dialog.exec()