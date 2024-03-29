from PyQt5 import QtCore, QtGui, QtWidgets

from services.summary_graph import summary_display


class WorkerUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1397, 859)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1351, 831))
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
                                  "}\n"
                                  "")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(29, 0, 1311, 821))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                   "border: 2px solid rgba(0, 0, 0, 0.7);\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(360, 210, 291, 531))
        self.widget_2.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:0.5 #f5f5f5, stop:1 #ffffff);\n"
                                    "border: 2px solid rgba(46, 82, 101, 100);\n"
                                    "border-radius: 5px;\n"
                                    "")
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutFichajes = QtWidgets.QVBoxLayout()
        self.layoutFichajes.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.layoutFichajes.setContentsMargins(10, 10, 10, 10)
        self.layoutFichajes.setSpacing(10)
        self.layoutFichajes.setObjectName("layoutFichajes")
        self.verticalLayout.addLayout(self.layoutFichajes)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(680, 210, 611, 531))
        self.widget_3.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:0.5 #f5f5f5, stop:1 #ffffff);\n"
                                    "border: 2px solid rgba(46, 82, 101, 100);\n"
                                    "border-radius: 5px;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # Crear un QScrollArea
        scroll_area = QtWidgets.QScrollArea(self.widget_3)
        scroll_area.setGeometry(0, 0, 611, 531)
        scroll_area.setWidgetResizable(True)

        # Crear un QWidget para contener el layout de notificaciones
        scroll_content = QtWidgets.QWidget(scroll_area)
        scroll_area.setWidget(scroll_content)

        # Crear un QVBoxLayout para el layout de notificaciones
        self.notifications_layout = QtWidgets.QVBoxLayout(scroll_content)
        self.notifications_layout.setContentsMargins(0, 0, 0, 0)
        self.notifications_layout.setObjectName("notifications_layout")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(30, 0, 281, 821))
        self.widget_4.setStyleSheet("background-color: #2c313c\n"
                                    "")
        self.widget_4.setObjectName("widget_4")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.BtnChangePassword = QtWidgets.QPushButton(self.widget_4)
        self.BtnChangePassword.setGeometry(QtCore.QRect(50, 660, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BtnChangePassword.setFont(font)
        self.BtnChangePassword.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnChangePassword.setStyleSheet("QPushButton#BtnChangePassword {\n"
                                             "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
                                             "    color: rgba(255, 255, 255, 210);\n"
                                             "    border-radius: 5px;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#BtnChangePassword:hover {\n"
                                             "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#BtnChangePassword:pressed {\n"
                                             "    padding-left: 5px;\n"
                                             "    padding-top: 5px;\n"
                                             "    background-color: rgba(38, 66, 50, 255);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton#BtnChangePassword:pressed {\n"
                                             "    padding-left: 5px;\n"
                                             "    padding-top: 5px;\n"
                                             "    background-color: rgba(49, 87, 66, 255);\n"
                                             "}")
        self.BtnChangePassword.setObjectName("BtnChangePassword")
        self.BtnResumen = QtWidgets.QPushButton(self.widget_4)
        self.BtnResumen.setGeometry(QtCore.QRect(50, 610, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BtnResumen.setFont(font)
        self.BtnResumen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnResumen.setStyleSheet("QPushButton#BtnResumen {\n"
                                      "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
                                      "    color: rgba(255, 255, 255, 210);\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#BtnResumen:hover {\n"
                                      "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#BtnResumen:pressed {\n"
                                      "    padding-left: 5px;\n"
                                      "    padding-top: 5px;\n"
                                      "    background-color: rgba(38, 66, 50, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#BtnResumen:pressed {\n"
                                      "    padding-left: 5px;\n"
                                      "    padding-top: 5px;\n"
                                      "    background-color: rgba(49, 87, 66, 255);\n"
                                      "}")
        self.BtnResumen.setObjectName("BtnResumen")
        self.close_btn = QtWidgets.QPushButton(self.widget_4)
        self.close_btn.setGeometry(QtCore.QRect(50, 740, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_btn.setFont(font)
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setStyleSheet("QPushButton#close_btn {\n"
                                     "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
                                     "    color: rgba(255, 255, 255, 210);\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#close_btn:hover {\n"
                                     "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#close_btn:pressed {\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-top: 5px;\n"
                                     "    background-color: rgba(38, 66, 50, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#close_btn:pressed {\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-top: 5px;\n"
                                     "    background-color: rgba(49, 87, 66, 255);\n"
                                     "}")
        self.close_btn.setObjectName("close_btn")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(30, 550, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(440, 140, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(890, 140, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(280, -110, 511, 241))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(
            "background-image: url(assets/sifabul.html);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.BtnFichar = QtWidgets.QPushButton(self.widget)
        self.BtnFichar.setGeometry(QtCore.QRect(360, 750, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BtnFichar.setFont(font)
        self.BtnFichar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnFichar.setStyleSheet("QPushButton#BtnFichar{\n"
                                     "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
                                     "    color: rgba(255, 255, 255, 210);\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#BtnFichar:hover {\n"
                                     "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#BtnFichar:pressed {\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-top: 5px;\n"
                                     "    background-color: rgba(38, 66, 50, 255);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton#BtnFichar:pressed {\n"
                                     "    padding-left: 5px;\n"
                                     "    padding-top: 5px;\n"
                                     "    background-color: rgba(49, 87, 66, 255);\n"
                                     "}")
        self.BtnFichar.setObjectName("BtnFichar")
        self.refresh_btn = QtWidgets.QPushButton(self.widget)
        self.refresh_btn.setGeometry(QtCore.QRect(680, 750, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_btn.setStyleSheet("QPushButton#refresh_btn {\n"
                                       "image: url(assets/refresh-icon-white-0.png);\n"
                                       "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
                                       "    color: rgba(255, 255, 255, 210);\n"
                                       "    border-radius: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#refresh_btn:hover {\n"
                                       "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#refresh_btn:pressed {\n"
                                       "    padding-left: 5px;\n"
                                       "    padding-top: 5px;\n"
                                       "    background-color: rgba(38, 66, 50, 255);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton#refresh_btn:pressed {\n"
                                       "    padding-left: 5px;\n"
                                       "    padding-top: 5px;\n"
                                       "    background-color: rgba(49, 87, 66, 255);\n"
                                       "}")
        self.refresh_btn.setText("")
        self.refresh_btn.setObjectName("refresh_btn")
        self.delete_btn = QtWidgets.QPushButton(self.widget)
        self.delete_btn.setGeometry(QtCore.QRect(737, 750, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setStyleSheet("QPushButton#delete_btn {\n"
                                      # Ajusta la imagen según tus necesidades
                                      "    image: url(assets/trash_icon.png);\n"
                                      "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
                                      "    color: rgba(255, 255, 255, 210);\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#delete_btn:hover {\n"
                                      "    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#delete_btn:pressed {\n"
                                      "    padding-left: 5px;\n"
                                      "    padding-top: 5px;\n"
                                      "    background-color: rgba(38, 66, 50, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton#delete_btn:pressed {\n"
                                      "    padding-left: 5px;\n"
                                      "    padding-top: 5px;\n"
                                      "    background-color: rgba(49, 87, 66, 255);\n"
                                      "}")
        self.delete_btn.setText("")
        self.delete_btn.setObjectName("delete_btn")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        icon_path = "assets/sifabulchiquito.html" 
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIFABUL"))
        self.label_7.setText(_translate("MainWindow", "TRABAJADOR"))
        self.BtnChangePassword.setText(
            _translate("MainWindow", "Cambiar Contraseña"))
        self.BtnResumen.setText(_translate("MainWindow", "Ver resumen"))
        self.close_btn.setText(_translate("MainWindow", "CERRAR SESION"))
        self.label_12.setText(_translate("MainWindow", "Opciones"))
        self.label_9.setText(_translate("MainWindow", "Fichajes"))
        self.label_10.setText(_translate("MainWindow", "Notificaciones"))
        self.BtnFichar.setText(_translate("MainWindow", "Fichar"))

    """START OWN CODE 
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    """

    def addChecks(self, checks):
        for object in checks:
            label = QtWidgets.QLabel(object.time)
            self.layoutFichajes.addWidget(label)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                QtWidgets.QSizePolicy.Expanding)
            if object.is_entry:
                label.setStyleSheet(
                    'background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet(
                    'background-color: red;font-size: 20px;border-radius: 10px;')

    def clear_layout(self, layout):
        # Borrar todos los widgets en el layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        if layout == self.layoutFichajes:
            check_label = QtWidgets.QLabel()
            check_label.setText('Fichajes')
            check_label.setAlignment(QtCore.Qt.AlignCenter)
            check_label.setStyleSheet(
                "QLabel {"
                "   font-family: Decorative;"
                "   font-size: 20px;"
                "   color: black;"
                "   background-color: #FFB6C1;"
                "}"
            )
            layout.addWidget(check_label)

    def showError(self, e):
        error_message = QtWidgets.QMessageBox()
        error_message.setIcon(QtWidgets.QMessageBox.Critical)
        error_message.setWindowTitle('Error')
        error_message.setText(str(e))
        error_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        error_message.exec_()

    def addNotifications(self, notList):
        for i in notList:
            if not i.seen:
                label = QtWidgets.QLabel(i.get_output())
                self.notifications_layout.addWidget(label)
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setSizePolicy(
                    QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                label.setStyleSheet(
                    'background-color: #2c313c; color: white; font-size: 20px; border-radius: 10px;')
                label.setFixedWidth(605)
                label.setWordWrap(True)

    def show_summary(self, weeks):
        summary_display(weeks)

    def set_user(self, username: str):
        self.label_7.setText(username)

    def show_label(self):
        not_label = QtWidgets.QLabel()
        not_label.setText('NO HAY NOTIFICACIONES')
        not_label.setAlignment(QtCore.Qt.AlignCenter)
        not_label.setStyleSheet(
            "QLabel {"
            "   font-family: Decorative;"
            "   font-size: 20px;"
            "   color: black;"
            "   background-color: #FFB6C1;"
            "}")
        self.notifications_layout.addWidget(not_label)
