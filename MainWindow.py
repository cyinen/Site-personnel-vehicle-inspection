# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QDir
from PIL import Image
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QWidget

from callCamera import Camera
from detector import Detector
import cv2 as cv
import time


class Ui_mainWindow(QWidget):
    startWork = pyqtSignal()
    dectSignal = pyqtSignal(str)

    def __init__(self):
        super(Ui_mainWindow, self).__init__()

        self.camera = Camera()
        self.cameraThread = QThread()
        self.camera.moveToThread(self.cameraThread)

        self.detector = Detector()
        self.detectorThread = QThread()
        self.detector.moveToThread(self.detectorThread)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setFixedSize(1328, 827)
        # mainWindow.resize(1328, 827)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 10, 361, 21))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(880, 300, 271, 341))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")


        self.checkBox_Logs = QtWidgets.QCheckBox(self.widget)
        self.checkBox_Logs.setObjectName("checkBox_Logs")
        self.verticalLayout.addWidget(self.checkBox_Logs)

        self.checkBox_Vegicle = QtWidgets.QCheckBox(self.widget)
        self.checkBox_Vegicle.setObjectName("checkBox_Vegicle")
        self.verticalLayout.addWidget(self.checkBox_Vegicle)
        self.checkBox_Clothes = QtWidgets.QCheckBox(self.widget)
        self.checkBox_Clothes.setObjectName("checkBox_Clothes")
        self.verticalLayout.addWidget(self.checkBox_Clothes)
        self.checkBox_Hat = QtWidgets.QCheckBox(self.widget)
        self.checkBox_Hat.setObjectName("checkBox_Hat")
        self.verticalLayout.addWidget(self.checkBox_Hat)
        self.checkBox_Person = QtWidgets.QCheckBox(self.widget)
        self.checkBox_Person.setObjectName("checkBox_Person")
        self.verticalLayout.addWidget(self.checkBox_Person)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_Start = QtWidgets.QPushButton(self.widget)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.verticalLayout_2.addWidget(self.pushButton_Start)
        self.pushButton_Stop = QtWidgets.QPushButton(self.widget)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.verticalLayout_2.addWidget(self.pushButton_Stop)

        self.pushButton_Vehicle = QtWidgets.QPushButton(self.widget)
        self.pushButton_Vehicle.setObjectName("pushButton_Vehicle")
        self.verticalLayout_2.addWidget(self.pushButton_Vehicle)

        self.pushButton_Test = QtWidgets.QPushButton(self.widget)
        self.pushButton_Test.setObjectName("pushButton_Test")
        self.verticalLayout_2.addWidget(self.pushButton_Test)

        self.pushButton_Exit = QtWidgets.QPushButton(self.widget)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.verticalLayout_2.addWidget(self.pushButton_Exit)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label_Display = QtWidgets.QLabel(self.centralwidget)
        self.label_Display.setGeometry(QtCore.QRect(20, 80, 630, 431))
        self.label_Display.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_Display.setObjectName("label_Display")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 560, 630, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextState = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextState.setGeometry(QtCore.QRect(880, 90, 271, 181))
        self.plainTextState.setObjectName("plainTextState")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1328, 35))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "基于Jeston Nano的嵌入式工地监测系统"))
        self.checkBox_Logs.setText("保存日志")
        self.checkBox_Vegicle.setText(_translate("mainWindow", "车辆监测"))
        self.checkBox_Clothes.setText(_translate("mainWindow", "反光衣监测"))
        self.checkBox_Hat.setText(_translate("mainWindow", "安全帽监测"))
        self.checkBox_Person.setText(_translate("mainWindow", "人员监测"))
        self.pushButton_Start.setText(_translate("mainWindow", "开始监测"))
        self.pushButton_Stop.setText(_translate("mainWindow", "停止监测"))
        self.pushButton_Test.setText(_translate("mainWindow", "测试模式"))
        self.pushButton_Vehicle.setText("车辆检测")
        self.pushButton_Exit.setText("退出")
        self.label_Display.setText(_translate("mainWindow", "监控区域"))
        self.label_Display.setStyleSheet("QLabel{border:2px solid rgb(126,139,146);}")

        self.checkBox_Vegicle.setChecked(True)
        self.checkBox_Hat.setChecked(True)
        self.checkBox_Person.setChecked(True)
        self.checkBox_Clothes.setChecked(True)

        self.pushButton_Exit.clicked.connect(mainWindow.close)
        img = Image.open("background.png")
        size = self.label_Display.size()
        size = (size.width(), size.height())
        img = img.resize(size)
        img = img.toqpixmap()
        self.label_Display.setPixmap(img)
        self.initSignasAndSolts()

    def initSignasAndSolts(self):
        self.pushButton_Start.clicked.connect(self.start)
        self.pushButton_Stop.clicked.connect(self.stop)
        self.startWork.connect(self.camera.doMyWork)
        self.camera.sendImg.connect(self.display)
        self.pushButton_Test.clicked.connect(self.test)
        self.detector.sendImg.connect(self.display)

        self.dectSignal.connect(self.detector.dectetVideo)

        self.pushButton_Vehicle.clicked.connect(self.dectVehicle)

    def checkStates(self):
        self.plainTextState.setPlainText("")
        if self.checkBox_Vegicle.isChecked():
            self.plainTextState.appendPlainText("正在进行车辆监测...")
        if self.checkBox_Hat.isChecked():
            self.plainTextState.appendPlainText("正在进行安全帽监测...")
        if self.checkBox_Clothes.isChecked():
            self.plainTextState.appendPlainText("正在进行反光服监测...")
        if self.checkBox_Person.isChecked():
            self.plainTextState.appendPlainText("正在进行人员监测...")

    def start(self):
        self.checkStates()
        self.openCamera()

    def stop(self):
        self.closeCamera()

    def openCamera(self):
        if self.cameraThread.isRunning():
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '摄像头已经打开啦!')
            msg_box.exec_()
            return
        else:
            self.camera.setFlag(True)
            self.cameraThread.start()
            self.startWork.emit()
            print("打开摄像头")
        return

    def closeCamera(self):
        if self.cameraThread.isRunning():
            self.camera.setFlag(False)
            self.cameraThread.quit()
            self.cameraThread.wait()
            print("关闭摄像头")
        else:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '摄像头还没打开呢!\n先去打开摄像头吧！')
            msg_box.exec_()
            return

    def display(self, img):
        self.label_Display.setPixmap(img[0])
        daytime = time.strftime("%Y-%m-%d-%H-%M-%s", time.localtime())

        outstr = img[1]
        person = outstr.find("person")
        hat = outstr.find("hat")
        reflective_clothes = outstr.find("reflective_clothes")
        if person > 0 and hat < 0 or reflective_clothes < 0:
            self.plainTextEdit.appendPlainText("[{}有工人没有按规定着装:]".format(daytime))
            if self.checkBox_Logs.isChecked():
                img[0].save("./违章人员/" + daytime + ".jpg")
            else:
                pass
        else:
            self.plainTextEdit.appendPlainText("[{}:]".format(daytime))
        self.plainTextEdit.appendPlainText(img[1])

    def test(self):
        
        if self.detectorThread.isRunning():
            self.pushButton_Test.setText("测试模式")
            self.detector.setFlag(True)
            self.detectorThread.quit()
            self.detectorThread.wait()
            self.pushButton_Start.clicked.disconnect(self.dectetVideo)
            self.pushButton_Stop.clicked.disconnect(self.dectetImg)
            self.pushButton_Start.setText("开始监测")
            self.pushButton_Stop.setText("停止监测")
            self.pushButton_Start.clicked.connect(self.start)
            self.pushButton_Stop.clicked.connect(self.stop)
            self.plainTextState.setPlainText("测试模式已关闭...")
        else:
            self.pushButton_Test.setText("关闭测试模式")
            self.detectorThread.start()
            self.pushButton_Start.setText("检测视频")
            self.pushButton_Stop.setText("检测图片")

            self.pushButton_Stop.clicked.disconnect(self.stop)
            self.pushButton_Start.clicked.disconnect(self.start)

            self.pushButton_Start.clicked.connect(self.dectetVideo)
            self.pushButton_Stop.clicked.connect(self.dectetImg)
            self.plainTextState.setPlainText("测试模式已开启...")

    def dectetVideo(self):
        self.detector.setFlag(False)
        self.plainTextState.appendPlainText("正在进行视频监测...")
        print("选择文件夹")
        # 实例化QFileDialog
        dig = QFileDialog()
        filenames = dig.getOpenFileName(self, '选择测试图片', './', 'Image files (*.jpg *.gif *.png *.jpeg *.mp4)')
        if filenames[0] == '':
            return
        print(filenames[0])
        self.dectSignal.emit(filenames[0])

    def dectetImg(self):
        self.plainTextState.appendPlainText("正在进行图片监测...")
        print("选择文件夹")
        # 实例化QFileDialog
        dig = QFileDialog()
        filenames = dig.getOpenFileName(self, '选择测试图片', './', 'Image files (*.jpg *.gif *.png *.jpeg *.mp4)')
        if filenames[0] == '':
            return

        img = cv.imread(filenames[0])
        size = self.label_Display.size()
        img = cv.resize(img, (size.width(), size.height()))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        img, out = self.detector.dectetImg(img)
        img = Image.fromarray(img)
        img = img.toqpixmap()
        self.label_Display.setPixmap(img)
        self.plainTextEdit.appendPlainText(out)
        self.plainTextState.setPlainText("图片测试结束...")
        return
    
    def dectVehicle(self):
        self.plainTextState.appendPlainText("正在进行车辆监测...")
        print("选择文件夹")
        # 实例化QFileDialog
        dig = QFileDialog()
        filenames = dig.getOpenFileName(self, '选择测试图片', './', 'Image files (*.jpg *.gif *.png *.jpeg *.mp4)')
        if filenames[0] == '':
            return
        img = cv.imread(filenames[0])
        size = self.label_Display.size()
        img = cv.resize(img, (size.width(), size.height()))

        img, out = self.detector.dectVehicle(img)
        img = Image.fromarray(img)
        img = img.toqpixmap()
        self.label_Display.setPixmap(img)
        
        self.plainTextEdit.appendPlainText("The car is "+out)
        self.plainTextState.setPlainText("车辆检测结束...")

