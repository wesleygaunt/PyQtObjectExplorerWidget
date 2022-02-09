# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'objectViewerWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_objectViewerWidget(object):
    def setupUi(self, objectViewerWidget):
        objectViewerWidget.setObjectName("objectViewerWidget")
        objectViewerWidget.resize(900, 542)
        self.gridLayout = QtWidgets.QGridLayout(objectViewerWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.upLevelToolButton = QtWidgets.QToolButton(objectViewerWidget)
        self.upLevelToolButton.setText("")
        self.upLevelToolButton.setAutoRaise(True)
        self.upLevelToolButton.setObjectName("upLevelToolButton")
        self.gridLayout.addWidget(self.upLevelToolButton, 0, 0, 1, 1)
        self.optionsButton = QtWidgets.QToolButton(objectViewerWidget)
        self.optionsButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.optionsButton.setAutoRaise(True)
        self.optionsButton.setObjectName("optionsButton")
        self.gridLayout.addWidget(self.optionsButton, 0, 2, 1, 1)
        self.tableView = QtWidgets.QTableView(objectViewerWidget)
        font = QtGui.QFont()
        self.tableView.setFont(font)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setWordWrap(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableView, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.treeView = QtWidgets.QTreeView(objectViewerWidget)
        font = QtGui.QFont()
        self.treeView.setFont(font)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 2, 0, 1, 3)

        self.retranslateUi(objectViewerWidget)
        QtCore.QMetaObject.connectSlotsByName(objectViewerWidget)

    def retranslateUi(self, objectViewerWidget):
        _translate = QtCore.QCoreApplication.translate
        objectViewerWidget.setWindowTitle(_translate("objectViewerWidget", "Form"))
        self.optionsButton.setText(_translate("objectViewerWidget", "Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    objectViewerWidget = QtWidgets.QWidget()
    ui = Ui_objectViewerWidget()
    ui.setupUi(objectViewerWidget)
    objectViewerWidget.show()
    sys.exit(app.exec_())

