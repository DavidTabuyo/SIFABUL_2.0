from PyQt5 import QtCore, QtGui, QtWidgets


class AddWorkerUi(object):
    def setupUi(self, MainWindow, admin_id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 631, 500))
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
        self.label_3.setGeometry(QtCore.QRect(119, 50, 511, 361))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                   "border: 2px solid rgba(0, 0, 0, 0.7);\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(140, 70, 76, 71))
        self.label_6.setStyleSheet("\n"
                                   "background-image: url(assets/sifabulchiquito.html);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(240, 80, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_7.setObjectName("label_7")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(137, 155, 481, 241))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_10.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.admin_le = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.admin_le.setFont(font)
        self.admin_le.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                    "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                    "    border-radius: 5px;\n"
                                    "    color: rgba(0, 0, 0, 240);\n"
                                    "    padding: 5px;")
        self.admin_le.setPlaceholderText("")
        self.admin_le.setObjectName("admin_le")
        self.verticalLayout_2.addWidget(self.admin_le)
        self.name_le = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.name_le.setFont(font)
        self.name_le.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                   "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                   "    border-radius: 5px;\n"
                                   "    color: rgba(0, 0, 0, 240);\n"
                                   "    padding: 5px;")
        self.name_le.setPlaceholderText("")
        self.name_le.setObjectName("name_le")
        self.verticalLayout_2.addWidget(self.name_le)
        self.password_le = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.password_le.setFont(font)
        self.password_le.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                       "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                       "    border-radius: 5px;\n"
                                       "    color: rgba(0, 0, 0, 240);\n"
                                       "    padding: 5px;")
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setPlaceholderText("")
        self.password_le.setObjectName("password_le")
        self.verticalLayout_2.addWidget(self.password_le)
        self.confirm_password_le = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.confirm_password_le.setFont(font)
        self.confirm_password_le.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                               "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                               "    border-radius: 5px;\n"
                                               "    color: rgba(0, 0, 0, 240);\n"
                                               "    padding: 5px;")
        self.confirm_password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_le.setPlaceholderText("")
        self.confirm_password_le.setObjectName("confirm_password_le")
        self.verticalLayout_2.addWidget(self.confirm_password_le)
        self.name_le_2 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.name_le_2.setFont(font)
        self.name_le_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                     "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                     "    border-radius: 5px;\n"
                                     "    color: rgba(0, 0, 0, 240);\n"
                                     "    padding: 5px;")
        self.name_le_2.setPlaceholderText("")
        self.name_le_2.setObjectName("name_le_2")
        self.verticalLayout_2.addWidget(self.name_le_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btm_accept = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btm_accept.setFont(font)
        self.btm_accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btm_accept.setObjectName("btm_accept")
        self.horizontalLayout.addWidget(self.btm_accept)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.admin_le.setText(admin_id)
        self.admin_le.setDisabled(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        icon_path = "assets/sifabulchiquito.html" 
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIFABUL"))
        self.label_7.setText(_translate("MainWindow", "AÑADIR TRABAJADOR"))
        self.label_5.setText(_translate("MainWindow", "Admin:"))
        self.label_9.setText(_translate("MainWindow", "Nombre de usuario:"))
        self.label_8.setText(_translate("MainWindow", "Contraseña:"))
        self.label_4.setText(_translate("MainWindow", "Confirmar contraseña:"))
        self.label_10.setText(_translate("MainWindow", "Nombre:"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancelar"))
        self.btm_accept.setText(_translate("MainWindow", "Aceptar"))

        """START OWN CODE 
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    """

    def showError(self, e):
        mensaje_error = QtWidgets.QMessageBox()
        mensaje_error.setIcon(QtWidgets.QMessageBox.Critical)
        mensaje_error.setWindowTitle('Error')
        mensaje_error.setText(str(e))
        mensaje_error.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mensaje_error.exec()

    def change_correct(self):
        warning_message = QtWidgets.QMessageBox()
        warning_message.setIcon(QtWidgets.QMessageBox.Warning)
        warning_message.setWindowTitle('Aviso')
        warning_message.setText("Se ha creado un nuevo becario correctamente")
        warning_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        warning_message.exec_()
