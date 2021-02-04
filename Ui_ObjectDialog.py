# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ObjectDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ObjectDialog(object):
    def setupUi(self, ObjectDialog):
        ObjectDialog.setObjectName("ObjectDialog")
        ObjectDialog.resize(500, 600)
        self.gridLayout = QtWidgets.QGridLayout(ObjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.callablesCheckBox = QtWidgets.QCheckBox(ObjectDialog)
        self.callablesCheckBox.setObjectName("callablesCheckBox")
        self.gridLayout.addWidget(self.callablesCheckBox, 0, 0, 1, 1)
        self.specialsCheckBox = QtWidgets.QCheckBox(ObjectDialog)
        self.specialsCheckBox.setObjectName("specialsCheckBox")
        self.gridLayout.addWidget(self.specialsCheckBox, 0, 1, 1, 1)
        self.MainTable = QtWidgets.QTableWidget(ObjectDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(ObjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 5)
        self.privateCheckBox = QtWidgets.QCheckBox(ObjectDialog)
        self.privateCheckBox.setObjectName("privateCheckBox")
        self.gridLayout.addWidget(self.privateCheckBox, 0, 2, 1, 1)
        self.objectCheckBox = QtWidgets.QCheckBox(ObjectDialog)
        self.objectCheckBox.setObjectName("objectCheckBox")
        self.gridLayout.addWidget(self.objectCheckBox, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(420, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.typeLabel = QtWidgets.QLabel(ObjectDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout.addWidget(self.typeLabel, 1, 0, 1, 5)

        self.retranslateUi(ObjectDialog)
        self.buttonBox.accepted.connect(ObjectDialog.accept)
        self.buttonBox.rejected.connect(ObjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ObjectDialog)

    def retranslateUi(self, ObjectDialog):
        _translate = QtCore.QCoreApplication.translate
        ObjectDialog.setWindowTitle(_translate("ObjectDialog", "Dialog"))
        self.callablesCheckBox.setText(_translate("ObjectDialog", "Callables"))
        self.specialsCheckBox.setText(_translate("ObjectDialog", "__specials__ "))
        item = self.MainTable.horizontalHeaderItem(0)
        item.setText(_translate("ObjectDialog", "Name"))
        item = self.MainTable.horizontalHeaderItem(1)
        item.setText(_translate("ObjectDialog", "Type"))
        item = self.MainTable.horizontalHeaderItem(2)
        item.setText(_translate("ObjectDialog", "Value"))
        self.privateCheckBox.setText(_translate("ObjectDialog", "__private"))
        self.objectCheckBox.setText(_translate("ObjectDialog", "Object view"))
        self.typeLabel.setText(_translate("ObjectDialog", "Type: "))

