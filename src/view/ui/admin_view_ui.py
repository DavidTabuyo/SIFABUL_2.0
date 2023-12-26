# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_view.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 311, 501))
        self.list_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.list_layout.setObjectName(u"list_layout")
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.edit_list_btn = QPushButton(self.centralwidget)
        self.edit_list_btn.setObjectName(u"edit_list_btn")
        self.edit_list_btn.setGeometry(QRect(40, 530, 75, 23))
        self.change_password_btn = QPushButton(self.centralwidget)
        self.change_password_btn.setObjectName(u"change_password_btn")
        self.change_password_btn.setGeometry(QRect(210, 570, 121, 23))
        self.send_notification_btn = QPushButton(self.centralwidget)
        self.send_notification_btn.setObjectName(u"send_notification_btn")
        self.send_notification_btn.setGeometry(QRect(570, 520, 121, 23))
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(370, 20, 401, 501))
        self.notifications_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.notifications_layout.setObjectName(u"notifications_layout")
        self.notifications_layout.setContentsMargins(0, 0, 0, 0)
        self.update_btn = QPushButton(self.centralwidget)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(490, 520, 75, 23))
        self.add_worker_btn = QPushButton(self.centralwidget)
        self.add_worker_btn.setObjectName(u"add_worker_btn")
        self.add_worker_btn.setGeometry(QRect(120, 530, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.edit_list_btn.setText(QCoreApplication.translate("MainWindow", u"Editar lista", None))
        self.change_password_btn.setText(QCoreApplication.translate("MainWindow", u"cambiar contrase\u00f1a", None))
        self.send_notification_btn.setText(QCoreApplication.translate("MainWindow", u"enviar notificacion", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"actualizar", None))
        self.add_worker_btn.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir becario", None))
    # retranslateUi

