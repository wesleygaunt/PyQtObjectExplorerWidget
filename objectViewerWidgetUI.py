# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectViewerWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_objectViewerWidget(object):
    def setupUi(self, objectViewerWidget):
        objectViewerWidget.setObjectName("objectViewerWidget")
        objectViewerWidget.resize(636, 497)
        self.gridLayout = QtWidgets.QGridLayout(objectViewerWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.privateCheckBox = QtWidgets.QCheckBox(objectViewerWidget)
        self.privateCheckBox.setObjectName("privateCheckBox")
        self.gridLayout.addWidget(self.privateCheckBox, 0, 2, 1, 1)
        self.specialsCheckBox = QtWidgets.QCheckBox(objectViewerWidget)
        self.specialsCheckBox.setObjectName("specialsCheckBox")
        self.gridLayout.addWidget(self.specialsCheckBox, 0, 1, 1, 1)
        self.MainTable = QtWidgets.QTableWidget(objectViewerWidget)
        self.MainTable.setObjectName("MainTable")
        self.MainTable.setColumnCount(3)
        self.MainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, item)
        self.MainTable.horizontalHeader().setVisible(True)
        self.MainTable.horizontalHeader().setStretchLastSection(True)
        self.MainTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.MainTable, 2, 0, 1, 5)
        self.callablesCheckBox = QtWidgets.QCheckBox(objectViewerWidget)
        self.callablesCheckBox.setObjectName("callablesCheckBox")
        self.gridLayout.addWidget(self.callablesCheckBox, 0, 0, 1, 1)
        self.objectCheckBox = QtWidgets.QCheckBox(objectViewerWidget)
        self.objectCheckBox.setObjectName("objectCheckBox")
        self.gridLayout.addWidget(self.objectCheckBox, 0, 4, 1, 1)
        self.typeLabel = QtWidgets.QLabel(objectViewerWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout.addWidget(self.typeLabel, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)

        self.retranslateUi(objectViewerWidget)
        QtCore.QMetaObject.connectSlotsByName(objectViewerWidget)

    def retranslateUi(self, objectViewerWidget):
        _translate = QtCore.QCoreApplication.translate
        objectViewerWidget.setWindowTitle(_translate("objectViewerWidget", "Form"))
        self.privateCheckBox.setText(_translate("objectViewerWidget", "__private"))
        self.specialsCheckBox.setText(_translate("objectViewerWidget", "__specials__ "))
        item = self.MainTable.horizontalHeaderItem(0)
        item.setText(_translate("objectViewerWidget", "Name"))
        item = self.MainTable.horizontalHeaderItem(1)
        item.setText(_translate("objectViewerWidget", "Type"))
        item = self.MainTable.horizontalHeaderItem(2)
        item.setText(_translate("objectViewerWidget", "Value"))
        self.callablesCheckBox.setText(_translate("objectViewerWidget", "Callables"))
        self.objectCheckBox.setText(_translate("objectViewerWidget", "Object view"))
        self.typeLabel.setText(_translate("objectViewerWidget", "Type: "))
