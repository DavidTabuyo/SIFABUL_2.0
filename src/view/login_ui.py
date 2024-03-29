from PyQt5 import QtCore, QtGui, QtWidgets


class loginUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon_path = "assets/sifabulchiquito.html"
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
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
        self.label_4.setGeometry(QtCore.QRect(350, 90, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.UserName = QtWidgets.QLineEdit(self.widget)
        self.UserName.setGeometry(QtCore.QRect(295, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px;\n"
                                    "")
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(295, 230, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px;\n"
                                    "")
        self.Password.setObjectName("Password")
        self.BotonOk = QtWidgets.QPushButton(self.widget)
        self.BotonOk.setGeometry(QtCore.QRect(295, 310, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BotonOk.setFont(font)
        self.BotonOk.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BotonOk.setObjectName("BotonOk")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(280, 70, 76, 71))
        self.label_6.setStyleSheet("\n"
                                   "background-image: url(assets/sifabulchiquito.html);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.btn_cancel = QtWidgets.QPushButton(self.widget)
        self.btn_cancel.setGeometry(QtCore.QRect(390, 410, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setObjectName("btn_cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(
            blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_4.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_6.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        icon_path = "assets/sifabulchiquito.html" 
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIFABUL"))
        self.label_4.setText(_translate("MainWindow", "Iniciar Sesión"))
        self.UserName.setPlaceholderText(_translate("MainWindow", " Usuario"))
        self.Password.setPlaceholderText(
            _translate("MainWindow", " Contraseña"))
        self.BotonOk.setText(_translate("MainWindow", "Aceptar"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancelar"))

        """START OWN CODE 
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    """

    def showError(self, e):
        mensaje_error = QtWidgets.QMessageBox()
        mensaje_error.setIcon(QtWidgets.QMessageBox.Critical)
        mensaje_error.setWindowTitle('Error')
        mensaje_error.setText(str(e))
        mensaje_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mensaje_error.exec_()
