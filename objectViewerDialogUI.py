# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectViewerDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ObjectDialog(object):
    def setupUi(self, ObjectDialog):
        ObjectDialog.setObjectName("ObjectDialog")
        ObjectDialog.resize(500, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(ObjectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.objectViewerWidget = objectViewerWidget(ObjectDialog)
        self.objectViewerWidget.setObjectName("objectViewerWidget")
        self.verticalLayout.addWidget(self.objectViewerWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(ObjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ObjectDialog)
        self.buttonBox.accepted.connect(ObjectDialog.accept)
        self.buttonBox.rejected.connect(ObjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ObjectDialog)

    def retranslateUi(self, ObjectDialog):
        _translate = QtCore.QCoreApplication.translate
        ObjectDialog.setWindowTitle(_translate("ObjectDialog", "Dialog"))
from objectViewerWidget import objectViewerWidget
