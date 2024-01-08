# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_password_view.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

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
        self.widget.setCursor(QCursor(Qt.ArrowCursor))
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
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(:/assets/img.jpg);\n"
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
        self.label_4.setGeometry(QRect(380, 70, 140, 81))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.new_password_imp = QLineEdit(self.widget)
        self.new_password_imp.setObjectName(u"new_password_imp")
        self.new_password_imp.setGeometry(QRect(300, 230, 190, 40))
        font1 = QFont()
        font1.setPointSize(10)
        self.new_password_imp.setFont(font1)
        self.new_password_imp.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;\n"
"")
        self.new_password_imp.setEchoMode(QLineEdit.Password)
        self.accept_btn = QPushButton(self.widget)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setGeometry(QRect(295, 310, 190, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.accept_btn.setFont(font2)
        self.accept_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 70, 76, 71))
        self.label_6.setStyleSheet(u"\n"
"background-image: url(:assets/sifabulchiquito.html);")
        self.old_password_imp = QLineEdit(self.widget)
        self.old_password_imp.setObjectName(u"old_password_imp")
        self.old_password_imp.setGeometry(QRect(300, 170, 190, 40))
        self.old_password_imp.setFont(font1)
        self.old_password_imp.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;\n"
"")
        self.old_password_imp.setEchoMode(QLineEdit.Password)
        self.cancel_btn = QPushButton(self.widget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(390, 410, 100, 35))
        self.cancel_btn.setFont(font2)
        self.cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Cambiar</span></p><p><span style=\" font-size:16pt;\">Contrase\u00f1a</span></p></body></html>", None))
        self.new_password_imp.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Contrase\u00f1a Nueva", None))
        self.accept_btn.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_6.setText("")
        self.old_password_imp.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Contrase\u00f1a Vieja", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

