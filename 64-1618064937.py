from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import os

app = QApplication([])
m = QWidget()
m.setWindowTitle('Easy Editor')

layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QVBoxLayout()
layout4 = QHBoxLayout()

Btn_file = QPushButton("Папка")
Btn_left = QPushButton('Лево')
Btn_right = QPushButton('Право')
Btn_mirror = QPushButton('Зеркало')
Btn_r = QPushButton('Резкость')
Btn_BW = QPushButton('Ч/Б')
Pic = QLabel('Картинка')
List = QListWidget()

layout1.addWidget(Btn_file)
layout1.addWidget(List)
layout2.addWidget(Btn_left)
layout2.addWidget(Btn_right)
layout2.addWidget(Btn_mirror)
layout2.addWidget(Btn_r)
layout2.addWidget(Btn_BW)
layout3.addWidget(Pic)
layout3.addLayout(layout2)
layout4.addLayout(layout1)
layout4.addLayout(layout3)

m.SetLayout(layout4)
m.show()
app.exec_()
