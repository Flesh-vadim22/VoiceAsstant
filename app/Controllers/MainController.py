import datetime
import pyttsx3
import app.Models.DataModel
import speech_recognition as sr
from PyQt5 import QtCore, QtWidgets
import os
from app.Views.MainView import MainView


engine = pyttsx3.init()

class MainController(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = MainView()
        # self.ui.assistant_label.setStyleSheet("background-image: face1.png)")
        self.answer = app.Models.DataModel.DataModel()
        self.ui.setupUi(self)
        self.ui.assistant_label.setText("<center><img src='file:///" + os.getcwd() + "/src/face1.png'></center>")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.ui.hide_app_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.close_app_btn.clicked.connect(lambda: self.close())
        self.ui.clear_btn.clicked.connect(lambda: self.ui.chat_list.clear())
        self.ui.send_btn.clicked.connect(self.start_conversation)
        self.ui.stop_btn.clicked.connect(self.stop_conversation)
        self.stop = False
        self.repeat_start = False
# перемезение окна приложения, т.к. стандартные элементы убраны
    def center(self):
        frame_geometry = self.frameGeometry()
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center)
        self.move(frame_geometry.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
# воспроизведение речи ассистента
    def speak(self, text):
        engine.say(text)
        engine.runAndWait()
        engine.stop()



    # распознавание речи пользователя
    def recordAudio(self, phrase='Говорите: '):
        recognize = sr.Recognizer()
        with sr.Microphone() as source:
            recognize.adjust_for_ambient_noise(source)
            self.send_message(phrase, user=False)
            self.speak(phrase)
            audio = recognize.listen(source)
        try:
            data = recognize.recognize_google(audio, language='ru-RU').lower()
            self.send_message(phrase)
        except sr.UnknownValueError:
            error = "Извините,но я вас не понимаю"
            self.ui.assistant_label.setText("<center><img src='file:///" + os.getcwd() + "/src/face3.png'></center>")
            self.send_message(error, user=False)
            self.speak(error)
            return None
        except sr.RequestError as e:
            error = "Не удалось запросить результаты у службы распознавания речи Google"
            self.ui.assistant_label.setText("<center><img src='file:///" + os.getcwd() + "/src/face3.png'></center>")
            self.speak(error)
            self.send_message(error, user=False)
            return None
        return data
    # def send_message_user(self, text):
    #     item = QtWidgets.QListWidgetItem()
    #     item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
    #     item.setText('Вы' + ': ' + text)
    #     self.ui.chat_list.addItem(item)

    def send_message(self, text, user=True):
        item = QtWidgets.QListWidgetItem()
        if user == True:
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            item.setText('Вы' + ': ' + text)
        else:
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            item.setText('Каралис' + ': ' + text)
        self.ui.chat_list.addItem(item)

    # def send_message_assistant(self, answer):
    #     item = QtWidgets.QListWidgetItem()
    #     item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    #     item.setText('Каралис' + ': ' + answer)
    #     self.ui.chat_list.addItem(item)

    # выявление времени суток пользователя
    def getTimeOfDay(self):
        getTime = int(datetime.datetime.now().hour)
        if getTime >= 0 and getTime < 6:
            text = 'Доброе ночи'
            self.send_message(text, user=False)
            self.speak(text)
        elif getTime >= 6 and getTime < 12:
            text = 'Доброе утро'
            self.send_message(text, user=False)
            self.speak(text)
        elif getTime >= 12 and getTime < 18:
            text = 'Добрый день'
            self.send_message(text, user=False)
            self.speak(text)
        elif getTime >= 18 and getTime != 0:
            text = 'Добрый вечер!'
            self.send_message(text, user=False)
            self.speak(text)
    def stop_conversation(self):
        engine.endLoop()
        self.ui.assistant_label.setText("<center><img src='file:///" + os.getcwd() + "/src/face1.png'></center>")
        self.stop = True
        self.ui.stop_btn.hide()
        self.ui.send_btn.show()

    def start_conversation(self):
        if self.repeat_start == False:
            start_text = 'Мое почтение, меня зовут Каралис.\n' \
                         ' Могу ли я вам чем-нибудь помочь?'
            self.getTimeOfDay()
            self.send_message(start_text, user=False)
            self.speak(start_text)

        self.repeat_start = True
        self.stop = False
        self.ui.stop_btn.show()
        self.ui.send_btn.hide()
        while self.stop == False:
            statement = self.recordAudio()
            if statement == None: continue
            # self.send_message_assistant(statement)
            # self.speak(statement)
            answer, action = self.answer.get_answer(statement)
            if type(action) is str:
                self.send_message(action, user=False)
                self.speak(action)
            self.ui.assistant_label.setText("<center><img src='file:///" + os.getcwd() + "/src/face2.png'></center>")
            self.send_message(answer, user=False)
            self.speak(answer)
            if action == True:
                self.ui.assistant_label.setText("<center><img src='file:///" + os.getcwd() + "/src/face1.png'></center>")
                self.stop = True
                self.ui.send_btn.show()
                self.ui.stop_btn.hide()
                break
            if engine._inLoop:
                engine.endLoop()