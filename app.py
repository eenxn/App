from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
from PyQt6.QtCore import Qt
import sys

# def clicked():
#     global n
#     print(n)
#     n+=1

# n =1

# app = QApplication(sys.argv)
# #print(sys.argv)
# window = QWidget()
# window.setWindowTitle("Petkub")
# label = QLabel("Petkub", parent= window)
# layout1 = QVBoxLayout()
# btn_1 = QPushButton("Petkub1", parent= window)
# btn_2 = QPushButton("Petkub2", parent= window)
# layout1.addWidget(btn_1)
# layout1.addWidget(label)
# label.setAlignment(Qt.AlignmentFlag.AlignCenter)
# layout1.addWidget(btn_2)
# window.setLayout(layout1)

# btn_1.clicked.connect(clicked)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.resize(600,600)

btn_1 = QPushButton("Petkub1")
btn_2 = QPushButton("Petkub2")
widget_1 = QWidget()
layout_1_v = QVBoxLayout()
layout_1_v.addWidget(btn_1)
layout_1_v.addWidget(btn_2)
layout_1_v.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
widget_1.setLayout(layout_1_v)

btn_3 = QPushButton("Petkub3")
btn_4 = QPushButton("Petkub4")
widget_2 = QWidget()
layout_2_v = QVBoxLayout()
layout_2_v.addWidget(btn_3)
layout_2_v.addWidget(btn_4)
layout_2_v.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
widget_2.setLayout(layout_2_v)

layout_v = QVBoxLayout()
layout_v.addWidget(widget_1)
layout_v.addWidget(widget_2)

central_widget.setLayout(layout_v)

window.show()
sys.exit(app.exec())