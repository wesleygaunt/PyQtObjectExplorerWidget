# PythonObjectExplorerDialog
 Provides a simple object explorer dialog using PyQt 5 with support for collections and arbitary objects. Uses abstract base classes to display inherited collections correctly. Currently read-only, but will add support for changing values in a later commit.
 
##Usage
 ```python
app = QtWidgets.QApplication([])
dialog = ObjectExplorerDialog(object_)
dialog.exec()
```
##Screenshots
Add screenshots here.