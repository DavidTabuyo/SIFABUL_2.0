# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worker_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class WorkerUi(object):
    def setupUi(self, BECARIO):
        BECARIO.setObjectName("BECARIO")
        BECARIO.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(BECARIO)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 60, 251, 501))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutFichajes = QtWidgets.QVBoxLayout()
        self.layoutFichajes.setObjectName("layoutFichajes")
        self.verticalLayout.addLayout(self.layoutFichajes)
        self.BtnFichar = QtWidgets.QPushButton(self.layoutWidget)
        self.BtnFichar.setObjectName("BtnFichar")
        self.verticalLayout.addWidget(self.BtnFichar)
        self.btnChangePassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnChangePassword.setGeometry(QtCore.QRect(10, 20, 151, 23))
        self.btnChangePassword.setObjectName("btnChangePassword")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 70, 160, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.notifications_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.notifications_layout.setContentsMargins(0, 0, 0, 0)
        self.notifications_layout.setObjectName("notifications_layout")
        self.btnResumen = QtWidgets.QPushButton(self.centralwidget)
        self.btnResumen.setGeometry(QtCore.QRect(180, 20, 247, 23))
        self.btnResumen.setObjectName("btnResumen")
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(560, 40, 131, 23))
        self.refresh_btn.setObjectName("refresh_btn")
        BECARIO.setCentralWidget(self.centralwidget)

        self.retranslateUi(BECARIO)
        QtCore.QMetaObject.connectSlotsByName(BECARIO)

    def retranslateUi(self, BECARIO):
        _translate = QtCore.QCoreApplication.translate
        BECARIO.setWindowTitle(_translate("BECARIO", "MainWindow"))
        self.BtnFichar.setText(_translate("BECARIO", "FICHAR"))
        self.btnChangePassword.setText(_translate("BECARIO", "CAMBIAR CONTRASEÑA"))
        self.btnResumen.setText(_translate("BECARIO", "VER RESUMEN"))
        self.refresh_btn.setText(_translate("BECARIO", "Recargar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BECARIO = QtWidgets.QMainWindow()
    ui = Ui_BECARIO()
    ui.setupUi(BECARIO)
    BECARIO.show()
    sys.exit(app.exec_())
