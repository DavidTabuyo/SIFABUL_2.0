from PyQt5 import QtCore, QtGui, QtWidgets

from model.worker import Worker


class EditWorkerListUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.label_3.setGeometry(QtCore.QRect(119, 50, 400, 375))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                   "border: 2px solid rgba(0, 0, 0, 0.7);\n"
                                   "")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(150, 176, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.username_le = QtWidgets.QLineEdit(self.widget)
        self.username_le.setGeometry(QtCore.QRect(320, 228, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.username_le.setFont(font)
        self.username_le.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                       "    border: 2px solid rgba(46, 82, 101, 200);\n"
                                       "    border-radius: 5px;\n"
                                       "    color: rgba(0, 0, 0, 240);\n"
                                       "    padding: 5px;")
        self.username_le.setPlaceholderText("")
        self.username_le.setObjectName("username_le")
        self.accept_btn = QtWidgets.QPushButton(self.widget)
        self.accept_btn.setGeometry(QtCore.QRect(260, 330, 120, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.accept_btn.setFont(font)
        self.accept_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.accept_btn.setObjectName("accept_btn")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(140, 70, 76, 71))
        self.label_6.setStyleSheet("\n"
                                   "background-image: url(assets/sifabulchiquito.html);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.cancel_btn = QtWidgets.QPushButton(self.widget)
        self.cancel_btn.setGeometry(QtCore.QRect(130, 380, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_btn.setObjectName("cancel_btn")
        self.label_5 = QtWidgets.QLabel(self.widget)
        # Ajustado el ancho de la etiqueta
        self.label_5.setGeometry(QtCore.QRect(150, 228, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_5.setObjectName("label_5")
        self.workers_cb = QtWidgets.QComboBox(self.widget)
        self.workers_cb.setGeometry(QtCore.QRect(320, 183, 170, 30))
        self.workers_cb.setStyleSheet("background-color: white;\n"  # Cambiado a fondo blanco
                                      "border: 2px solid rgba(46, 82, 101, 200);\n"
                                      "border-radius: 5px;\n"
                                      "color: black;\n"  # Cambiado a letras negras
                                      "padding: 5px;")
        # Set item delegate to handle combobox text color
        self.workers_cb.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.workers_cb.setObjectName("workers_cb")

        self.change_password_btn = QtWidgets.QPushButton(self.widget)
        self.change_password_btn.setGeometry(QtCore.QRect(150, 280, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.change_password_btn.setFont(font)
        self.change_password_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_password_btn.setObjectName("change_password_btn")
        self.delete_user_btn = QtWidgets.QPushButton(self.widget)
        self.delete_user_btn.setGeometry(QtCore.QRect(330, 280, 160, 27))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.delete_user_btn.setFont(font)
        self.delete_user_btn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_user_btn.setObjectName("delete_user_btn")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(230, 80, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.label_7.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_5.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_4.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.change_password_btn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.delete_user_btn.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_6.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        icon_path = "assets/sifabulchiquito.html" 
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SIFABUL"))
        self.label_4.setText(_translate("MainWindow", "Elige un Usuario:"))
        self.accept_btn.setText(_translate("MainWindow", "Aceptar"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancelar"))
        self.label_5.setText(_translate("MainWindow", "Nuevo nombre:"))
        self.change_password_btn.setText(
            _translate("MainWindow", "Cambiar contraseña"))
        self.delete_user_btn.setText(
            _translate("MainWindow", "Eliminar Usuario"))
        self.label_7.setText(_translate("MainWindow", "EDITAR TRABAJADOR"))

        """START OWN CODE 
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    """

    def show_workers(self, workers: list[Worker]):
        id_list = [worker.worker_id for worker in workers]
        self.workers_cb.addItems(id_list)

    def showError(self, e: str):
        error_message = QtWidgets.QMessageBox()
        error_message.setIcon(QtWidgets.QMessageBox.Critical)
        error_message.setWindowTitle('Error')
        error_message.setText(str(e))
        error_message.setStandardButtons(QtWidgets.QMessageBox.Ok)
        error_message.exec_()

    def get_selected_worker(self) -> str:
        return self.workers_cb.currentText()
