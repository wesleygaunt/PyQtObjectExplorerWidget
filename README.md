# PythonObjectExplorerDialog
 Provides a simple object explorer dialog using PyQt 5 with support for collections and arbitary objects. Uses abstract base classes to display inherited collections correctly. Currently read-only, but will add support for changing values in a later commit.
 
## Usage
 ```python
app = QtWidgets.QApplication([])
dialog = ObjectExplorerDialog(object_)
dialog.exec()
```
Will produce the following dialog. The object attributes can be filtered using the checkboxes along the top of the dialog.

![IMAGE0](https://user-images.githubusercontent.com/47778261/106953308-23b0aa80-672a-11eb-9985-2333936f5c99.png)

## Screenshots
Viewing a Dictionary as a collection:

![IMAGE1](https://user-images.githubusercontent.com/47778261/106952513-1d6dfe80-6729-11eb-98e6-635ab5524834.png)

The same dictionary as an object, which can be changed by selecting 'Object View'

![IMAGE2](https://user-images.githubusercontent.com/47778261/106952962-bac93280-6729-11eb-9811-20bb5ed78283.png)

String:

![IMAGE3](https://user-images.githubusercontent.com/47778261/106952799-7b9ae180-6729-11eb-8c1a-b231d68fc337.png)

## Future work
I plan to make the dialog recursive so attributes can also be viewed in the dialog, and also add in editability for the built in types; strings, numerics and booleans.
