# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 550, 500))
        self.widget.setStyleSheet(u"QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(38, 66, 50, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(49, 87, 66, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2 {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(85, 98, 112, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#push"
                        "Button_2:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(49, 87, 66, 255);\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(:/images/6ef95b76fbbac79716b698fb1bf38407.jpg);\n"
"border-top-left-radius:50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius:50px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 90, 140, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.UserName = QLineEdit(self.widget)
        self.UserName.setObjectName(u"UserName")
        self.UserName.setGeometry(QRect(295, 170, 190, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.UserName.setFont(font1)
        self.UserName.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;\n"
"")
        self.Password = QLineEdit(self.widget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(295, 230, 190, 40))
        self.Password.setFont(font1)
        self.Password.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;\n"
"")
        self.BotonOk = QPushButton(self.widget)
        self.BotonOk.setObjectName(u"BotonOk")
        self.BotonOk.setGeometry(QRect(295, 310, 190, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.BotonOk.setFont(font2)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(295, 360, 191, 16))
        self.label_5.setStyleSheet(u"color:rgba(0, 0, 0, 210);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 70, 76, 71))
        self.label_6.setStyleSheet(u"\n"
"background-image: url(:/images/sifabulchiquito.html);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.UserName.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Usuario", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Contrase\u00f1a", None))
        self.BotonOk.setText(QCoreApplication.translate("MainWindow", u"L o g I n", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Olvidaste tu contrase\u00f1a?", None))
        self.label_6.setText("")
    # retranslateUi

