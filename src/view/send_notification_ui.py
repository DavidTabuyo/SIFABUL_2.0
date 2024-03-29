from PyQt5 import QtCore, QtGui, QtWidgets


class SendNotificationUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 631, 500))
        self.widget.setStyleSheet("QPushButton#send_btn {\n"
                                  "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
                                  "    color: rgba(255, 255, 255, 210);\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#send_btn:hover {\n"
                                  "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#send_btn:pressed {\n"
                                  "    padding-left: 5px;\n"
                                  "    padding-top: 5px;\n"
                                  "    background-color: rgba(38, 66, 50, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#send_btn:pressed {\n"
                                  "    padding-left: 5px;\n"
                                  "    padding-top: 5px;\n"
                                  "    background-color: rgba(49, 87, 66, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#cancel_btn {\n"
                                  "    background-color: rgba(0, 0, 0, 0);\n"
                                  "    color: rgba(85, 98, 112, 255);\n"
                                  "    border-radius: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#cancel_btn:hover {\n"
                                  "    color: rgba(131, 96, 53, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton#pushButton_3 {\n"
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
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(49, 0, 561, 471))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                   "border: 2px solid rgba(0, 0, 0, 0.7);\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(90, 40, 76, 71))
        self.label_6.setStyleSheet("\n"
                                   "background-image: url(assets/sifabulchiquito.html);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.cancel_btn = QtWidgets.QPushButton(self.widget)
        self.cancel_btn.setGeometry(QtCore.QRect(70, 420, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_btn.setObjectName("cancel_btn")
        self.send_btn = QtWidgets.QPushButton(self.widget)
        self.send_btn.setGeometry(QtCore.QRect(427, 412, 167, 44))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.send_btn.setFont(font)
        self.send_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_btn.setObjectName("send_btn")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(170, 40, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.title_edit = QtWidgets.QLineEdit(self.widget)
        self.title_edit.setGeometry(QtCore.QRect(100, 170, 451, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.title_edit.setFont(font)
        self.title_edit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                      "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                      "    border-radius: 5px;\n"
                                      "    color: rgba(0, 0, 0, 240);\n"
                                      "    padding: 5px;")
        self.title_edit.setText("")
        self.title_edit.setObjectName("title_edit")
        self.body_edit = QtWidgets.QLineEdit(self.widget)
        self.body_edit.setGeometry(QtCore.QRect(100, 210, 451, 171))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.body_edit.setFont(font)
        self.body_edit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                     "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                     "    border-radius: 5px;\n"
                                     "    color: rgba(0, 0, 0, 240);\n"
                                     "    padding: 5px;")
        self.body_edit.setText("")
        self.body_edit.setObjectName("body_edit")
        self.select_worker_cb = QtWidgets.QLineEdit(self.widget)
        self.select_worker_cb.setGeometry(QtCore.QRect(100, 130, 451, 30))
        self.select_worker_cb.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                            "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                            "    border-radius: 5px;\n"
                                            "    color: rgba(0, 0, 0, 240);\n"
                                            "    padding: 5px;")
        self.select_worker_cb.setObjectName("select_worker_cb")
        self.select_worker_cb.setPlaceholderText(
            "Inserte los destinatarios separados por ;")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        icon_path = "assets/sifabulchiquito.html" 
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIFABUL"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancelar"))
        self.send_btn.setText(_translate("MainWindow", "Enviar"))
        self.label_7.setText(_translate("MainWindow", "ENVIAR NOTIFICACIÓN"))
        self.title_edit.setPlaceholderText(_translate("MainWindow", "ASUNTO"))
        self.body_edit.setPlaceholderText(
            _translate("MainWindow", "ESCRIBE UN MENSAJE"))

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

    def send_advise(self):
        warning_message = QtWidgets.QMessageBox()
        warning_message.setIcon(QtWidgets.QMessageBox.Warning)
        warning_message.setWindowTitle('Aviso')
        warning_message.setText("Se ha enviado la notificación correctamente")
        warning_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        warning_message.exec_()
