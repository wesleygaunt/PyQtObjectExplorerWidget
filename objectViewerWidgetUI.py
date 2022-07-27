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
        self.verticalLayout = QtWidgets.QVBoxLayout(objectViewerWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.optionsLayout = QtWidgets.QFrame(objectViewerWidget)
        self.optionsLayout.setObjectName("optionsLayout")
        self.optionsLayout1 = QtWidgets.QHBoxLayout(self.optionsLayout)
        self.optionsLayout1.setContentsMargins(0, 0, 0, 6)
        self.optionsLayout1.setSpacing(0)
        self.optionsLayout1.setObjectName("optionsLayout1")
        self.upLevelToolButton = QtWidgets.QToolButton(self.optionsLayout)
        self.upLevelToolButton.setText("")
        self.upLevelToolButton.setAutoRaise(True)
        self.upLevelToolButton.setObjectName("upLevelToolButton")
        self.optionsLayout1.addWidget(self.upLevelToolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.optionsLayout1.addItem(spacerItem)
        self.optionsButton = QtWidgets.QToolButton(self.optionsLayout)
        self.optionsButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.optionsButton.setAutoRaise(True)
        self.optionsButton.setObjectName("optionsButton")
        self.optionsLayout1.addWidget(self.optionsButton)
        self.verticalLayout.addWidget(self.optionsLayout)
        self.treeView = QtWidgets.QTreeView(objectViewerWidget)
        font = QtGui.QFont()
        self.treeView.setFont(font)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.tableView = QtWidgets.QTableView(objectViewerWidget)
        font = QtGui.QFont()
        self.tableView.setFont(font)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setWordWrap(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView)

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

