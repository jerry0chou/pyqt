# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuUi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 312)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setCheckable(False)
        self.openAction.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menu/pic/gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.openAction.setIcon(icon)
        self.openAction.setPriority(QtWidgets.QAction.NormalPriority)
        self.openAction.setObjectName("openAction")
        self.action_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/menu/pic/share.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_2.setIcon(icon1)
        self.action_2.setObjectName("action_2")
        self.saveAction = QtWidgets.QAction(MainWindow)
        self.saveAction.setObjectName("saveAction")
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.action_5 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/menu/pic/think.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_5.setIcon(icon2)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/menu/pic/windows.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_6.setIcon(icon3)
        self.action_6.setObjectName("action_6")
        self.menu.addAction(self.openAction)
        self.menu.addAction(self.saveAction)
        self.menu.addAction(self.exitAction)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.openAction.triggered.connect(MainWindow.open)
        self.saveAction.triggered.connect(MainWindow.save)
        self.exitAction.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "菜单栏"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "联系"))
        self.openAction.setText(_translate("MainWindow", "打开"))
        self.openAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_2.setText(_translate("MainWindow", "分享"))
        self.saveAction.setText(_translate("MainWindow", "保存"))
        self.exitAction.setText(_translate("MainWindow", "退出"))
        self.action_5.setText(_translate("MainWindow", "定位"))
        self.action_6.setText(_translate("MainWindow", "视窗"))

import icon_rc
