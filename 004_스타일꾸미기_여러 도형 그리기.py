import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
import random


class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,500,500)
        self.setWindowTitle('도형그리기')
        self.show()

    def paintEvent(self, event):
        paint = QPainter() # 그림판 같은 역할을 하는 모듈입니다.
        paint.begin(self) # paint가 실행할 동작은 begin과 end사이에 위치해야함.
        self.drawFigure(paint)
        paint.end()

    def drawFigure(self, paint):
        paint.setBrush(QColor(10, 255, 40)) # 이 색깔로 직사각형 도형을 채운다.
        paint.setPen(QPen(QColor(Qt.red))) # 직사각형 둘레 선 색깔이다.
        paint.drawRect(20, 30, 100, 100) # 사각형으로 출력

        paint.setBrush(QColor(10, 255, 40)) # 이 색깔로 직사각형 도형을 채운다.
        paint.setPen(QPen(QColor(Qt.red))) # 직사각형 둘레 선 색깔이다.
        paint.drawRoundedRect(150, 20, 100, 100, 30, 30) # 마지막 뒤에 있는 30, 30은 직사각형의 모퉁이 수치다. 많이 올리면 둥그렇게 된다.

        paint.setBrush(QBrush(Qt.CrossPattern)) # 선이 크로스 형태로 그어진다.
        paint.setPen(QPen(QColor(Qt.red))) # 직사각형 둘레 선 색깔이다.
        paint.drawRoundedRect(300, 100, 100, 100, 30, 30)

        paint.setBrush(QColor(Qt.darkGreen)) # 이 색깔로 직사각형 도형을 채운다.
        paint.setPen(QPen(QColor(Qt.red), 2, Qt.DotLine)) # 직사각형 둘레 선 색깔이다.
        paint.drawEllipse(150, 200, 180, 180) 





app = QApplication(sys.argv)
exc = myapp()
app.exec_()

