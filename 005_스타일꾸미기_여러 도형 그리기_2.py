import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPolygon
from PyQt5.QtCore import Qt, QPoint
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
        self.다각형(paint)
        paint.end()

    def 다각형(self, paint):
        점 = [
            QPoint(10, 10),
            QPoint(20, 30),
            QPoint(130, 120),
            QPoint(260, 140),
            QPoint(360, 160),
            QPoint(320, 280),
            QPoint(220, 270),
            QPoint(200, 195),
        ]

        다각형 = QPolygon(점)
        paint.setPen(QPen(Qt.red, 10))
        paint.drawPolygon(다각형)

        점 = [
            QPoint(320, 260),
            QPoint(300, 180),
            QPoint(120, 290),
            QPoint(200, 295),
        ]

        다각형_둘 = QPolygon(점)
        paint.setPen(QPen(Qt.blue, 10))
        paint.drawPolygon(다각형_둘)

        # 호, 현, 파이
        # (x, y, width, height, start-angle, span-angle) span-angle는 몇도를 표시할거냐 라는거다.
        paint.setPen(QPen(Qt.black, 5))
        paint.drawArc(100, 300, 100, 100, 0*16, 180*16) # 16은 상관이 없다.
        paint.drawText(100, 450, '180도')

        paint.setPen(QPen(Qt.red, 5))
        paint.drawChord(250, 300, 100, 100, 270*16, 60*16)
        paint.drawText(250, 450, '60도')

        paint.setPen(QPen(Qt.blue, 5))
        paint.drawPie(400, 300, 100, 100, 90*16, 180*16)
        paint.drawText(400, 450, '180도')




app = QApplication(sys.argv)
exc = myapp()
app.exec_()

