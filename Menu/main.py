# -*- coding:utf-8 -*-
# Author : JerryChu
from PyQt5.QtWidgets import QFileDialog

from Menu.MenuUi import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # 参考博客中建立的是Widget项目，因此哪里导入的是QWidget
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
    def open(self):
        textPath, textType = QFileDialog.getOpenFileName(self,
                                                       "打开图片",
                                                       "", # 起始目录
                                                       "*.txt;;All Files (*)")
        print(textPath,textType)
        f=open(textPath)
        data=f.read()
        f.close()
        print(data)

    def save(self):
        print("已经保存了保存。。")
app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())