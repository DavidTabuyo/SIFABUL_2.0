from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
from datetime import datetime, timedelta

from model.notification import Notification


class AdminUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1397, 876)
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
        self.workers_layout = QtWidgets.QVBoxLayout()
        self.workers_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.workers_layout.setContentsMargins(10, 10, 10, 10)
        self.workers_layout.setSpacing(10)
        self.workers_layout.setObjectName("workers_layout")
        self.verticalLayout.addLayout(self.workers_layout)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(680, 210, 581, 531))
        self.widget_3.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:0.5 #f5f5f5, stop:1 #ffffff);\n"
"border: 2px solid rgba(46, 82, 101, 100);\n"
"border-radius: 5px;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 581, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.notifications_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
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
        self.BtnChangePassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.edit_list_btn = QtWidgets.QPushButton(self.widget_4)
        self.edit_list_btn.setGeometry(QtCore.QRect(50, 560, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edit_list_btn.setFont(font)
        self.edit_list_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_list_btn.setStyleSheet("QPushButton#edit_list_btn {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#edit_list_btn:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
"}\n"
"\n"
"QPushButton#edit_list_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(38, 66, 50, 255);\n"
"}\n"
"\n"
"QPushButton#edit_list_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(49, 87, 66, 255);\n"
"}")
        self.edit_list_btn.setObjectName("edit_list_btn")
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
        self.label_12.setGeometry(QtCore.QRect(30, 500, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:white;")
        self.label_12.setObjectName("label_12")
        self.send_notification_btn = QtWidgets.QPushButton(self.widget_4)
        self.send_notification_btn.setGeometry(QtCore.QRect(50, 610, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.send_notification_btn.setFont(font)
        self.send_notification_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_notification_btn.setStyleSheet("QPushButton#send_notification_btn {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#send_notification_btn:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
"}\n"
"\n"
"QPushButton#send_notification_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(38, 66, 50, 255);\n"
"}\n"
"\n"
"QPushButton#send_notification_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(49, 87, 66, 255);\n"
"}")
        self.send_notification_btn.setObjectName("send_notification_btn")
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
        self.label_11.setStyleSheet("background-image: url(assets/sifabul.html);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.add_worker_btn = QtWidgets.QPushButton(self.widget)
        self.add_worker_btn.setGeometry(QtCore.QRect(360, 750, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_worker_btn.setFont(font)
        self.add_worker_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_worker_btn.setStyleSheet("QPushButton#add_worker_btn{\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(49, 87, 66, 219), stop: 1 rgba(25, 42, 35, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#add_worker_btn:hover {\n"
"    background-color: qlineargradient(spread: pad, x1: 0, y1: 0.505682, x2: 1, y2: 0.477, stop: 0 rgba(38, 66, 50, 219), stop: 1 rgba(19, 31, 26, 226));\n"
"}\n"
"\n"
"QPushButton#add_worker_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(38, 66, 50, 255);\n"
"}\n"
"\n"
"QPushButton#add_worker_btn:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(49, 87, 66, 255);\n"
"}")
        self.scroll_area = QtWidgets.QScrollArea(self.widget_3)
        self.scroll_area.setGeometry(QtCore.QRect(0, 0, 581, 531))
        self.scroll_area.setWidgetResizable(True)

        # Create a widget to contain the notifications layout
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_widget)

        # Set notifications_layout as the layout for the scroll widget
        self.notifications_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
        self.notifications_layout.setContentsMargins(0, 0, 0, 0)
        self.notifications_layout.setObjectName("notifications_layout")
        self.add_worker_btn.setObjectName("add_worker_btn")
        self.refresh_btn = QtWidgets.QPushButton(self.widget)
        self.refresh_btn.setGeometry(QtCore.QRect(680, 750, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_btn.setStyleSheet("QPushButton#refresh_btn {\n"
"    image: url(assets/refresh-icon-white-0.png);\n"
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
        "    image: url(assets/trash_icon.png);\n"  # Ajusta la imagen según tus necesidades
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Administrador"))
        self.BtnChangePassword.setText(_translate("MainWindow", "Cambiar Contraseña"))
        self.edit_list_btn.setText(_translate("MainWindow", "Editar trabajadores"))
        self.close_btn.setText(_translate("MainWindow", "CERRAR SESION"))
        self.label_12.setText(_translate("MainWindow", "Opciones"))
        self.send_notification_btn.setText(_translate("MainWindow", "Enviar notificacion"))
        self.label_9.setText(_translate("MainWindow", "Becarios"))
        self.label_10.setText(_translate("MainWindow", "Notificaciones"))
        self.add_worker_btn.setText(_translate("MainWindow", "Añadir becario"))


    """START OWN CODE 
    ---------------------------------------------------------------------------------------------------------------------------------------------------
    """

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                
    def show_notifications(self, notList:list[Notification]):
        for i in notList:
            label = QtWidgets.QLabel(i.get_output())
            self.notifications_layout.addWidget(label)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            #if all workers has seen the notificarion
            if 1:#i.is_seen:
                label.setStyleSheet('background-color: green;font-size: 20px;border-radius: 10px;')
            else:
                label.setStyleSheet('background-color: red;font-size: 20px;border-radius: 10px;')
        
        
    def show_summary(self,weeks):
        # Ordenar las semanas por fecha
        weeks.sort(key=lambda x: datetime.strptime(x.monday, "%Y-%m-%d"))

        # Tomar las 10 últimas semanas
        last_10_weeks = weeks[-10:]

        # Crear listas de fechas, horas trabajadas y colores
        fechas = [(datetime.strptime(week.monday, "%Y-%m-%d") + timedelta(days=7)).strftime("%Y-%m-%d") for week in last_10_weeks]
        horas_trabajadas = [week.get_total_hours() for week in last_10_weeks]
        colores = ['red' if hour < 10 else 'green' for hour in horas_trabajadas]

        # Crear el gráfico de barras
        plt.figure(figsize=(10, 6))
        bars = plt.bar(fechas, horas_trabajadas, color=colores, label='Horas trabajadas')

        # Línea roja de puntos en y=10
        plt.axhline(y=10, color='r', linestyle='--', label='_nolegend_')

        # Mostrar el número de horas en formato "hh h mm min" en cada barra
        for bar, week in zip(bars, last_10_weeks):
            height = bar.get_height()
            formatted_total = week.get_formatted_total()
            plt.text(bar.get_x() + bar.get_width() / 2, height, formatted_total, ha='center', va='bottom')

        # Personalizar el gráfico
        plt.title('Resumen semanal')
        plt.ylabel('Horas trabajadas')
        plt.xticks(rotation=45, ha='right')  # Rotar las fechas en el eje x
        plt.ylim(0, 12)  # Rango del eje y hasta 12 horas
        plt.legend()

        # Mostrar el gráfico
        plt.tight_layout()
        plt.show(block=False)
        
    def set_user(self, username:str):
        self.label_7.setText(username)

                    
    