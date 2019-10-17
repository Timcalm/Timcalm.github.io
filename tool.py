# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_tool(object):
    def setupUi(self, tool):
        tool.setObjectName("tool")
        tool.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(tool)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 380, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(230, 40, 291, 61))
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 190, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(180, 190, 311, 31))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 380, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(180, 260, 411, 91))
        self.listWidget_2.setObjectName("listWidget_2")
        tool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(tool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        tool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(tool)
        self.statusbar.setObjectName("statusbar")
        tool.setStatusBar(self.statusbar)

        self.retranslateUi(tool)
        QtCore.QMetaObject.connectSlotsByName(tool)

    def retranslateUi(self, tool):
        _translate = QtCore.QCoreApplication.translate
        tool.setWindowTitle(_translate("tool", "MainWindow"))
        self.pushButton.setText(_translate("tool", "识别"))
        self.toolButton.setText(_translate("tool", "男女声音识别"))
        self.pushButton_2.setText(_translate("tool", "浏览"))
        self.pushButton_3.setText(_translate("tool", "重置"))
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app    
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件    
    ui = Ui_tool()                          # ui是你创建的ui类的实例化对象    
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow    
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow    
    sys.exit(app.exec_())  
