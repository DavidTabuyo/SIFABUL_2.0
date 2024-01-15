from PyQt5 import QtCore, QtGui, QtWidgets


class ChangePasswordUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setStyleSheet("QPushButton#pushButton {\n"
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
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(assets/img.jpg);\n"
"border-top-left-radius:50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(380, 70, 140, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.new_password_imp = QtWidgets.QLineEdit(self.widget)
        self.new_password_imp.setGeometry(QtCore.QRect(300, 230, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_password_imp.setFont(font)
        self.new_password_imp.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;\n"
"")
        self.new_password_imp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_imp.setObjectName("new_password_imp")
        self.accept_btn = QtWidgets.QPushButton(self.widget)
        self.accept_btn.setGeometry(QtCore.QRect(295, 310, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.accept_btn.setFont(font)
        self.accept_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.accept_btn.setObjectName("accept_btn")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(280, 70, 76, 71))
        self.label_6.setStyleSheet("\n"
"background-image: url(assets/sifabulchiquito.html);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.old_password_imp = QtWidgets.QLineEdit(self.widget)
        self.old_password_imp.setGeometry(QtCore.QRect(300, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.old_password_imp.setFont(font)
        self.old_password_imp.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;\n"
"")
        self.old_password_imp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_password_imp.setObjectName("old_password_imp")
        self.cancel_btn = QtWidgets.QPushButton(self.widget)
        self.cancel_btn.setGeometry(QtCore.QRect(390, 410, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_btn.setObjectName("cancel_btn")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.accept_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.accept_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.new_password_imp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_password_imp.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Cambiar</span></p><p><span style=\" font-size:16pt;\">Contraseña</span></p></body></html>"))
        self.new_password_imp.setPlaceholderText(_translate("MainWindow", " Contraseña Nueva"))
        self.accept_btn.setText(_translate("MainWindow", "Aceptar"))
        self.old_password_imp.setPlaceholderText(_translate("MainWindow", " Contraseña Vieja"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancelar"))
        


    """START OWN CODE 
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    """
    
    def showError(self, e):
            error_message = QtWidgets.QMessageBox()
            error_message.setIcon(QtWidgets.QMessageBox.Critical)
            error_message.setWindowTitle('Error')
            error_message.setText(str(e))
            error_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
            error_message.exec_()
    
    def change_correct(self):
        warning_message = QtWidgets.QMessageBox()
        warning_message.setIcon(QtWidgets.QMessageBox.Warning)
        warning_message.setWindowTitle('Aviso')
        warning_message.setText("Se ha cambiado la contraseña correctamente")
        warning_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        warning_message.exec_()

