# -*- coding:utf-8 -*-
# Author : JerryChu

import six
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements

from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QSplashScreen

from Image.ImageUi import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
import sys
import time

class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # 参考博客中建立的是Widget项目，因此哪里导入的是QWidget
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        #time.sleep(2)  # 启动界面睡眠
        QThread.sleep(2)

    def openImage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self,
                                                       "打开图片",
                                                       "",
                                                       " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(imgName)
        # 利用qlabel显示图片
        png = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)
    def nextImage(self):
        self.label.setStyleSheet("image: url(:/my_pic/pic/12.jpg);")
if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        splash= QSplashScreen(QPixmap(":/UI/pic/face.jpg")) # 启动界面
        splash.show()
        splash.showMessage("正在加载资源",Qt.AlignCenter,Qt.red) # 添加颜色 对齐
        QThread.sleep(2)
        splash.showMessage("正在初始化")
        QThread.sleep(2)
        app.processEvents() # 后台处理界面
        window = Mywindow()
        window.show()
        splash.finish(window) # 结束启动界面
        sys.exit(app.exec_())