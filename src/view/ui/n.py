# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\send_notification_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.send_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_btn.setGeometry(QtCore.QRect(380, 250, 75, 23))
        self.send_btn.setObjectName("send_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(140, 250, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 10, 522, 222))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_edit = QtWidgets.QLineEdit(self.widget)
        self.title_edit.setObjectName("title_edit")
        self.verticalLayout.addWidget(self.title_edit)
        self.body_edit = QtWidgets.QPlainTextEdit(self.widget)
        self.body_edit.setObjectName("body_edit")
        self.verticalLayout.addWidget(self.body_edit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.worker_list = QtWidgets.QListWidget(self.widget)
        self.worker_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.worker_list.setViewMode(QtWidgets.QListView.IconMode)
        self.worker_list.setObjectName("worker_list")
        self.horizontalLayout.addWidget(self.worker_list)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_btn.setText(_translate("MainWindow", "Enviar"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancelar"))
