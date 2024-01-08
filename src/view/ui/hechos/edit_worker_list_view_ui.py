# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_worker_list_view.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

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
                        "Button_3 {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(38, 66, 50, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(49, 87, 66, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_4 {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
""
                        "QPushButton#pushButton_4:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(38, 66, 50, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(49, 87, 66, 255);\n"
"}")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(119, 50, 400, 375))
        self.label_3.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border: 2px solid rgba(0, 0, 0, 0.7);\n"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 176, 161, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.username_le = QLineEdit(self.widget)
        self.username_le.setObjectName(u"username_le")
        self.username_le.setGeometry(QRect(320, 228, 170, 30))
        font1 = QFont()
        font1.setPointSize(8)
        self.username_le.setFont(font1)
        self.username_le.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"    border: 2px solid rgba(46, 82, 101, 200);\n"
"    border-radius: 5px;\n"
"    color: rgba(0, 0, 0, 240);\n"
"    padding: 5px;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 330, 120, 35))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 70, 76, 71))
        self.label_6.setStyleSheet(u"\n"
"background-image: url(:/assets/sifabulchiquito.html);")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 380, 100, 35))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 222, 81, 40))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.workers_cb = QComboBox(self.widget)
        self.workers_cb.setObjectName(u"workers_cb")
        self.workers_cb.setGeometry(QRect(320, 183, 170, 30))
        self.workers_cb.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"    border: 2px solid rgba(46, 82, 101, 200);\n"
"    border-radius: 5px;\n"
"    color: rgba(0, 0, 0, 240);\n"
"    padding: 5px;")
        self.change_password_btn = QPushButton(self.widget)
        self.change_password_btn.setObjectName(u"change_password_btn")
        self.change_password_btn.setGeometry(QRect(150, 280, 171, 27))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.change_password_btn.setFont(font2)
        self.change_password_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_user_btn = QPushButton(self.widget)
        self.delete_user_btn.setObjectName(u"delete_user_btn")
        self.delete_user_btn.setGeometry(QRect(330, 280, 160, 27))
        self.delete_user_btn.setFont(font2)
        self.delete_user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 80, 261, 81))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Elige un Usuario:", None))
        self.username_le.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_6.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.change_password_btn.setText(QCoreApplication.translate("MainWindow", u"Cambiar contrase\u00f1a", None))
        self.delete_user_btn.setText(QCoreApplication.translate("MainWindow", u"Eliminar Usuario", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"EDITAR TRABAJADOR", None))
    # retranslateUi

