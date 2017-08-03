# -*- coding:utf-8 -*-
# Author : JerryChu
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit

from Dialog.myDialog import myDialog
from Dialog.myDialogUi import Ui_Dialog
from Dialog.dialogUi  import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
    # 基本对话框
    def infoButton_clicked(self):
        my_button=QMessageBox.information(self,'信息','提示信息',)
        print(my_button,'info')

    def quesButton_clicked(self):
        my_button=QMessageBox.question(self,'问题','是否保存')
        print(my_button,'question')

    def warningButton_clicked(self):
        my_button=QMessageBox.warning(self,'警告','文字编码不同')
        print(my_button,'warning')

    def criticalButton_clicked(self):
        my_button = QMessageBox.critical(self, '严重警告', '出大事了')
        print(my_button, 'critical')

    # 标准对话框
    def getStringButton_clicked(self):
        my_str,isOK=QInputDialog.getText(self,'字符串','请在此输入')
        print(my_str,isOK)

    def getIntButton_clicked(self):
        val, isOK = QInputDialog.getInt(self, '整形', '请在此输入',10,0,20,1)
        print(val, isOK)
        self.lcdNumber.setProperty("intValue", val)

    def getComboButton_clicked(self):
        fruit=['苹果','梨子','香蕉']
        my_str, isOK = QInputDialog.getItem(self, '水果', '请在此输入',fruit)
        print(my_str, isOK)

    # 自定义对话框
    def showMyDialog(self):
        # super(Ui_Dialog, self).__init__()
        # self.setupUi(self)
        dialog=Ui_Dialog()
        super(Ui_Dialog, dialog).__init__()
        print('hello')
        my_dialog=myDialog()
        my_dialog.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())