# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from objectViewerDialog import objectViewerDialog
from objectViewerWidget import objectViewerWidget


import datetime

#create a test class with some methods
class newClass():
    def __init__(self,value):
        self.name = "Car"
        self.length = value
        self.height = 5
        self.__secret = 'I\'m a secret, don\'t tell anyone!'
    def newClassFunction(self,function_arg):
        print("I'm a function")
    def __private_function(self):
        print("I'm a private function")


#objects to test:
object_ = newClass(10)
date = datetime.datetime(2020,1,1)
float_ = 2.0
int_ = 1
complex_ = complex(1,1)
string_ = "Hello, World!"
list1 = ["hello","world",3]
list2 = [1,2, list1]

dict_ = {"None": None,"complex number":complex_, "list":list2, 'number' : 5.3}

tuple_ = ("1_tuple_val",2,3)
set_ = {"set1_item", "2"}
object_.dimensions = list2
object_.bool = True


app = QtWidgets.QApplication([])
widget = objectViewerWidget()
widget.set_object_data(object_, 
                       'object_',
                        open_children=False,
                        open_child_in_same_widget=False,
                        callables_populate = False,
                        specials_populate = False,  
                        private_populate = False,
                        show_primitive_members = False,
                        hide_options = True)

widget.show()
app.exec()

# app = QtWidgets.QApplication([])
# widget2 = objectViewerWidget()
# widget2.set_object_data(widget, 'widget')
# widget2.show()
# app.exec()



# app = QtWidgets.QApplication([])
# widget2 = objectViewerWidget()
# widget2.set_object_data(widget, 'widget',True)
# widget2.show()
# app.exec()
