from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QTextEdit
from PyQt5 import uic
import sys
import random as k
import string

class PasswordGenratore(QMainWindow):
    def __init__(self):
        super(PasswordGenratore, self).__init__()


        # load uifile
        uic.loadUi("untitled.ui",self)


        #define widgets
        self.label = self.findChild(QLabel, "password")
        self.button = self.findChild(QPushButton, "btn")
        self.input = self.findChild(QTextEdit, "count")

        self.button.clicked.connect(self.genrate)
        self.label.setText(f'Hello There')

        #showing app
        self.show()


    def genrate(self):
        data = list(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation)
        count = int(self.input.toPlainText())
        print(count)
        self.label.setText("")
        self.input.setPlainText("")
        password = []
        for i in range(count):
            password.append(k.choice(data))
        k.shuffle(password)
        print(password)
        print(type(password))
        value = ""
        value = value.join(password)
        print(value)
        print(type(value))
        # for element in password:
        #     value += password
        self.label.setText(f'{value}')

#initialisation

app = QApplication(sys.argv)
windoe = PasswordGenratore()
app.exec_()




