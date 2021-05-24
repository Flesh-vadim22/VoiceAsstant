from PyQt5 import QtCore, QtGui, QtWidgets


class MainView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 850, 450))
        self.main_frame.setStyleSheet("QFrame{\n"
"    background-color: #1B1D23;\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.menu_frame = QtWidgets.QFrame(self.main_frame)
        self.menu_frame.setGeometry(QtCore.QRect(0, 0, 850, 40))
        self.menu_frame.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"	border-radius:15px;\n"
"	margin-top:3px"
"}")
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.close_app_btn = QtWidgets.QPushButton(self.menu_frame)
        self.close_app_btn.setGeometry(QtCore.QRect(795, 5, 45, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        self.close_app_btn.setFont(font)
        self.close_app_btn.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.close_app_btn.setObjectName("close_app_btn")
        self.hide_app_btn = QtWidgets.QPushButton(self.menu_frame)
        self.hide_app_btn.setGeometry(QtCore.QRect(740, 5, 45, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hide_app_btn.sizePolicy().hasHeightForWidth())
        self.hide_app_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(10)
        self.hide_app_btn.setFont(font)
        self.hide_app_btn.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.hide_app_btn.setObjectName("hide_app_btn")
        self.chat_frame = QtWidgets.QFrame(self.main_frame)
        self.chat_frame.setGeometry(QtCore.QRect(10, 40, 425, 310))
        self.chat_frame.setStyleSheet("")
        self.chat_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chat_frame.setObjectName("chat_frame")

        self.chat_list = QtWidgets.QListWidget(self.chat_frame)
        self.chat_list.setGeometry(QtCore.QRect(0, 5, 425, 300))
        self.chat_list.setStyleSheet("color: white;\n"
"border-radius: 20px;\n"
"background-color: #2C313C;\n"
"")
        self.chat_list.setObjectName("chat_list")

        self.assistant_frame = QtWidgets.QFrame(self.main_frame)
        self.assistant_frame.setGeometry(QtCore.QRect(445, 45, 400, 380))
        self.assistant_frame.setStyleSheet("border-radius: 20px; \n"
                                           "background-color: #2C313C;")
        self.assistant_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.assistant_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.assistant_frame.setObjectName("assistant_frame")

        self.assistant_label = QtWidgets.QLabel(self.assistant_frame)
        self.assistant_label.setGeometry(QtCore.QRect(100, 20, 190, 290))
        self.assistant_label.setStyleSheet("border-radius: 20px;\n"
"background-color: #2C313C;\n"
"background-size:cover;\n"
"background-repeat:none;")
        self.assistant_label.setText("")
        self.assistant_label.setObjectName("assistant_label")

        self.user_frame = QtWidgets.QFrame(self.main_frame)
        self.user_frame.setGeometry(QtCore.QRect(10, 350, 425, 80))
        self.user_frame.setStyleSheet("")
        self.user_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_frame.setObjectName("user_frame")
#         self.user_edit = QtWidgets.QLineEdit(self.user_frame)
#         self.user_edit.setGeometry(QtCore.QRect(0, 0, 425, 40))
#         self.user_edit.setStyleSheet("QLineEdit{\n"
# "    border-radius: 10px;\n"
# "}")
#         self.user_edit.setObjectName("user_edit")
        self.send_btn = QtWidgets.QPushButton(self.user_frame)
        self.send_btn.setGeometry(QtCore.QRect(0, 0, 425, 35))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.send_btn.setFont(font)
        self.send_btn.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.send_btn.setObjectName("send_btn")


        self.stop_btn = QtWidgets.QPushButton(self.user_frame)
        self.stop_btn.hide()
        self.stop_btn.setGeometry(QtCore.QRect(0, 0, 425, 35))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setBold(True)
        font.setWeight(75)
        self.stop_btn.setFont(font)

        self.stop_btn.setStyleSheet("QPushButton{\n"
                                    "    color: white;\n"
                                    "    border-radius: 7px;\n"
                                    "    background-color: #595F76;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "    background-color: #50566E;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color: #434965;\n"
                                    "}")
        self.stop_btn.setObjectName("stop_btn")

        self.clear_btn = QtWidgets.QPushButton(self.user_frame)
        self.clear_btn.setGeometry(QtCore.QRect(0, 40, 425, 35))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.clear_btn.setObjectName("clear_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice_Assistant"))
        self.close_app_btn.setText(_translate("MainWindow", "X"))
        self.hide_app_btn.setText(_translate("MainWindow", "_"))
        self.send_btn.setText(_translate("MainWindow", "Начать разговор"))
        self.stop_btn.setText(_translate("MainWindow", "Остановить разговор"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить диалог"))
