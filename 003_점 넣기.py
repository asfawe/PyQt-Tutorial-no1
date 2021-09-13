import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt
import random


class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('QPainter')
        self.show()

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self) # paint가 실행할 동작은 begin과 end사이에 위치해야함.
        self.drawRandomPoint(paint)
        paint.end()

    def drawRandomPoint(self, paint):
        pen = QPen()

        colors = [Qt.red, Qt.blue, Qt.green]

        size = self.size() # 창 크기를 구함.
        print(f'높이와 넓이 : {size.height()}, {size.width()}')
        
        for _ in range(1000):
            pen.setColor(QColor(random.choice(colors)))
            pen.setWidth(random.randint(1, 20)) # 1부터 20까지 랜덤에 숫자 하나를 정해준다.
            paint.setPen(pen)

            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)

            paint.drawPoint(x,y)





app = QApplication(sys.argv)
exc = myapp()
app.exec_()

