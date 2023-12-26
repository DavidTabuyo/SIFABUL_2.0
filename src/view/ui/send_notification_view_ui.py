# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'send_notification_view.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(612, 295)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.send_btn = QPushButton(self.centralwidget)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setGeometry(QRect(380, 250, 75, 23))
        self.cancel_btn = QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(140, 250, 75, 23))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 10, 522, 222))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_edit = QLineEdit(self.widget)
        self.title_edit.setObjectName(u"title_edit")

        self.verticalLayout.addWidget(self.title_edit)

        self.body_edit = QPlainTextEdit(self.widget)
        self.body_edit.setObjectName(u"body_edit")

        self.verticalLayout.addWidget(self.body_edit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.worker_list = QListWidget(self.widget)
        self.worker_list.setObjectName(u"worker_list")
        self.worker_list.setSelectionMode(QAbstractItemView.MultiSelection)
        self.worker_list.setViewMode(QListView.IconMode)

        self.horizontalLayout.addWidget(self.worker_list)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

