# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ImageROI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 3, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_1)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_12.addWidget(self.label_2, 0, 0, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout_12.addWidget(self.lcdNumber_2, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem1, 0, 3, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout_12.addWidget(self.lcdNumber_3, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_12.addWidget(self.label_3, 0, 4, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout_12.addWidget(self.lcdNumber_4, 0, 6, 1, 1)
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.gridLayout_12.addWidget(self.lcdNumber_1, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_1)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_1.setMaximumSize(QtCore.QSize(200, 30))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_8.addWidget(self.pushButton_1, 1, 4, 1, 2)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_8.addWidget(self.graphicsView, 4, 0, 1, 6)
        self.label_1 = QtWidgets.QLabel(self.frame_2)
        self.label_1.setObjectName("label_1")
        self.gridLayout_8.addWidget(self.label_1, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem3, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
        self.pushButton_3.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "Start Corner (X,Y)"))
        self.label_3.setText(_translate("MainWindow", "End Corner(X,Y)"))
        self.label_4.setText(_translate("MainWindow", "All Images are saved in their original diamensions"))
        self.pushButton_1.setText(_translate("MainWindow", "View Original Image"))
        self.label_1.setText(_translate("MainWindow", "0,0"))

import icons_ImageCrop_rc
