import AI
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication,QWidget
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter
from PyQt5.QtCore import Qt
from PyQt6 import QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1001, 575)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 180, 541, 40))
        self.textEdit.setSizeIncrement(QtCore.QSize(59, 160))
        self.textEdit.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(50,50,50);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;                \n"
"border: 0px solid #094065;\n"
"font: 25 15pt \"Calibri\";")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 311, 71))
        self.label.setStyleSheet("image: url(Без именнеи.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;                \n"
"border: 0px solid #094065")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("nedvijimosti_ru_rgb-01.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 270, 261, 40))
        self.textEdit_2.setSizeIncrement(QtCore.QSize(59, 160))
        self.textEdit_2.setStyleSheet("color: rgb(50,50,50);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;                \n"
"border: 0px solid #094065;\n"
"font: 25 15pt \"Calibri\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(600, 180, 331, 221))
        self.textEdit_3.setSizeIncrement(QtCore.QSize(59, 160))
        self.textEdit_3.setStyleSheet("color: rgb(50,50,50);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;                \n"
"border: 0px solid #094065;\n"
"font: 25 15pt \"Calibri\";")
        self.textEdit_3.setObjectName("textEdit_3")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(0, -20, 1041, 681))
        self.label_2.setStyleSheet("background-image: url(#ffb685#eedb4f_1920_1080.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("#ffb685#eedb4f_1920_1080.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 330, 151, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 330, 151, 21))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(320, 270, 251, 40))
        self.textEdit_4.setSizeIncrement(QtCore.QSize(59, 160))
        self.textEdit_4.setStyleSheet("color: rgb(50,50,50);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;                \n"
"border: 0px solid #094065;\n"
"font: 25 15pt \"Calibri\";")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(30, 360, 261, 40))
        self.textEdit_5.setSizeIncrement(QtCore.QSize(59, 160))
        self.textEdit_5.setStyleSheet("color: rgb(50,50,50);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;                \n"
"border: 0px solid #094065;\n"
"font: 25 15pt \"Calibri\";")
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 151, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 240, 181, 21))
        self.label_7.setObjectName("label_7")
        self.textEdit_6 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(320, 360, 251, 40))
        self.textEdit_6.setSizeIncrement(QtCore.QSize(59, 160))
        self.textEdit_6.setStyleSheet("color: rgb(50,50,50);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;                \n"
"border: 0px solid #094065;\n"
"font: 25 15pt \"Calibri\";")
        self.textEdit_6.setObjectName("textEdit_6")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 440, 141, 41))
        self.pushButton.setStyleSheet("QPushButton{    background-color: rgb(70,70,70);	border-radius: 5px;                	border: 0px solid #094065;	color:white;}QPushButton:hover{	background-color: rgb(138, 138, 138);}")
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.textEdit_2.raise_()
        self.textEdit_3.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.textEdit_4.raise_()
        self.textEdit_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.textEdit_6.raise_()
        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.click)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4c4c4c;\">Район города</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4c4c4c;\">Этажность дома</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4c4c4c;\">Этаж</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4c4c4c;\">Площадь</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4c4c4c;\">Количество комнат</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
    def click(self):
        adress = self.textEdit.toPlainText().strip()
        square = self.textEdit_2.toPlainText().strip()
        count_rooms = self.textEdit_4.toPlainText().strip()
        floor = self.textEdit_5.toPlainText().strip()
        count_floor = self.textEdit_6.toPlainText().strip()
        print(count_rooms ,floor , count_floor, square)
        if (not count_rooms.isdigit() or not floor.isdigit() or not count_floor.isdigit() or not square.replace('.','').isdigit()):
            self.textEdit_3.setText('\n\n\n\n  введите корректные параметры')
            return
        square = float(square)
        count_rooms = int(count_rooms)
        floor = int(floor)
        count_floor= int(count_floor)
        distcrict = 1
        if(adress.strip().lower().startswith('с')):
            district = 3
        elif(adress.strip().lower().startswith('ж')):
            district = 2
        elif (adress.strip().lower().startswith('о')):
            district = 1
        else:
            self.textEdit_3.setText('\n\n\n\n  введите корректный район')
            return
        if (square > 250 or square < 10):
            self.textEdit_3.setText('\n\n\n\n  введите корректную площадь')
            return
        if (square > 250 or square < 10):
            self.textEdit_3.setText('\n\n\n\n  введите корректную площадь')
            return
        if (count_rooms > 5 or count_rooms < 1):
            self.textEdit_3.setText(('\n\n\n\n  введите корректное количество комнат'))
            return
        if (count_rooms > 5 or count_rooms < 0):
            self.textEdit_3.setText(('\n\n\n\n  введите корректное количество комнат'))
            return
        if (floor < -1 or floor > count_floor):
            self.textEdit_3.setText(('\n\n\n\n  введите корректный этаж'))
            print(floor,count_floor)
            return
        if (count_floor < 1):
            self.textEdit_3.setText(('\n\n\n\n  введите корректную этажность здания'))
            return
        res = f"\n\n\n\n                       {round((AI.estimation(int(floor),int(count_floor),int(count_rooms),district,float(square)))/1000000, 3)}   млн. руб."
        print(res)
        self.textEdit_3.setText(str(res))



