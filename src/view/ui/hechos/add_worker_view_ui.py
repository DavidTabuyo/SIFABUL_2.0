# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_worker_view.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 631, 500))
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
        self.label_3.setGeometry(QRect(119, 50, 451, 361))
        self.label_3.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border: 2px solid rgba(0, 0, 0, 0.7);\n"
"")
        self.name_le = QLineEdit(self.widget)
        self.name_le.setObjectName(u"name_le")
        self.name_le.setGeometry(QRect(339, 210, 211, 30))
        font = QFont()
        font.setPointSize(8)
        self.name_le.setFont(font)
        self.name_le.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"    border: 2px solid rgba(46, 82, 101, 200);\n"
"    border-radius: 5px;\n"
"    color: rgba(0, 0, 0, 240);\n"
"    padding: 5px;")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 70, 76, 71))
        self.label_6.setStyleSheet(u"\n"
"background-image: url(assets/sifabulchiquito.html);")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(240, 80, 261, 81))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.admin_le = QLineEdit(self.widget)
        self.admin_le.setObjectName(u"admin_le")
        self.admin_le.setGeometry(QRect(339, 170, 211, 30))
        self.admin_le.setFont(font)
        self.admin_le.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"    border: 2px solid rgba(46, 82, 101, 200);\n"
"    border-radius: 5px;\n"
"    color: rgba(0, 0, 0, 240);\n"
"    padding: 5px;")
        self.password_le = QLineEdit(self.widget)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setGeometry(QRect(339, 250, 211, 30))
        self.password_le.setFont(font)
        self.password_le.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"    border: 2px solid rgba(46, 82, 101, 200);\n"
"    border-radius: 5px;\n"
"    color: rgba(0, 0, 0, 240);\n"
"    padding: 5px;")
        self.password_le.setEchoMode(QLineEdit.Password)
        self.confirm_password_le = QLineEdit(self.widget)
        self.confirm_password_le.setObjectName(u"confirm_password_le")
        self.confirm_password_le.setGeometry(QRect(340, 290, 211, 30))
        self.confirm_password_le.setFont(font)
        self.confirm_password_le.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"    border: 2px solid rgba(46, 82, 101, 200);\n"
"    border-radius: 5px;\n"
"    color: rgba(0, 0, 0, 240);\n"
"    padding: 5px;")
        self.confirm_password_le.setEchoMode(QLineEdit.Password)
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(130, 360, 421, 28))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_cancel = QPushButton(self.widget1)
        self.btn_cancel.setObjectName(u"btn_cancel")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.btn_cancel.setFont(font2)
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btm_accept = QPushButton(self.widget1)
        self.btm_accept.setObjectName(u"btm_accept")
        self.btm_accept.setFont(font2)
        self.btm_accept.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btm_accept)

        self.widget2 = QWidget(self.widget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(137, 165, 431, 161))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color:rgba(0, 0, 0, 200);")

        self.verticalLayout.addWidget(self.label_5)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color:rgba(0, 0, 0, 200);")

        self.verticalLayout.addWidget(self.label_9)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color:rgba(0, 0, 0, 200);")

        self.verticalLayout.addWidget(self.label_8)

        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.label_4.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.name_le.setPlaceholderText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A\u00d1ADIR TRABAJADOR", None))
        self.admin_le.setPlaceholderText("")
        self.password_le.setPlaceholderText("")
        self.confirm_password_le.setPlaceholderText("")
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.btm_accept.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Admin:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Confirmar contrase\u00f1a:", None))
    # retranslateUi

