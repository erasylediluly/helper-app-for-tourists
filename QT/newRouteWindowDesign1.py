# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newRouteWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 848)
        MainWindow.setStyleSheet("color:white;background: #202543;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(40, 500, 981, 141))
        self.listWidget_2.setStyleSheet("background:#202543;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 260, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;background-color: rgba(0,0,0,0%);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;background-color: rgba(0,0,0,0%);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 390, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;background-color: rgba(0,0,0,0%);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 440, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_5.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 30px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;background-color: rgba(0,0,0,0%);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #202543;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 730, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: white;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;color:black;border-radius:19px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(470, 20, 271, 31))
        self.comboBox_2.setStyleSheet("color:#ffffff;background:#845DB4;font-size:15px;font-family: Courier New;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 21, 141, 31))
        self.comboBox.setStyleSheet("color:#ffffff;background:#845DB4;font-size:15px;font-family: Courier New;")
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 30, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;background-color: rgba(0,0,0,0%);")
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(780, 20, 241, 31))
        self.textEdit.setStyleSheet("background:white;border-radius:15px;color:#000000;font-size:15px;font-family: Courier New;")
        self.textEdit.setObjectName("textEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 30, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_9.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;background-color: rgba(0,0,0,0%);")
        self.label_9.setObjectName("label_9")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(40, 90, 981, 151))
        self.listWidget.setStyleSheet("background:#202543;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 660, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(410, 660, 181, 31))
        self.textEdit_2.setStyleSheet("background:white;color:black;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 700, 181, 31))
        self.comboBox_3.setStyleSheet("color:#ffffff;background:#845DB4;font-size:15px;font-family: Courier New;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 700, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_10.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 750, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_11.setObjectName("label_11")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(360, 740, 181, 31))
        self.comboBox_4.setStyleSheet("color:#ffffff;background:#845DB4;font-size:15px;font-family: Courier New;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(870, 660, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background: #845DB4;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;border-radius:19px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(210, 260, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background:#202543;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(210, 330, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background:#202543;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(210, 390, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background:#202543;font-family: Courier New;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 34px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #FFFFFF;")
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(660, 270, 361, 201))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 411, 471))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(690, 230, 361, 561))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.label_15.raise_()
        self.label_6.raise_()
        self.listWidget_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.comboBox_2.raise_()
        self.comboBox.raise_()
        self.label_7.raise_()
        self.textEdit.raise_()
        self.label_9.raise_()
        self.listWidget.raise_()
        self.label.raise_()
        self.textEdit_2.raise_()
        self.comboBox_3.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.comboBox_4.raise_()
        self.pushButton_3.raise_()
        self.label_14.raise_()
        self.label_13.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1046, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Построить маршрут"))
        self.label_2.setText(_translate("MainWindow", "Название:"))
        self.label_3.setText(_translate("MainWindow", "Регион:"))
        self.label_4.setText(_translate("MainWindow", "Вид:"))
        self.label_5.setText(_translate("MainWindow", "Добавленные места:"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Построить маршрут >"))
        self.label_7.setText(_translate("MainWindow", "Область:"))
        self.label_9.setText(_translate("MainWindow", "Вид:"))
        self.label.setText(_translate("MainWindow", "Расход топлива на 100км:"))
        self.label_10.setText(_translate("MainWindow", "Вид топлива:"))
        self.label_11.setText(_translate("MainWindow", "Город отправления:"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))