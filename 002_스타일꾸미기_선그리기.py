import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QPen
from PyQt5.QtCore import Qt


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
        self.drawLine(paint)
        paint.end()

    def drawLine(self, paint):
        pen = QPen(Qt.blue, 4, Qt.SolidLine) # 선 기본설정
        paint.setPen(pen) # 연결을 시켜주는 것이다. paint를 셋 페인트에
        paint.drawLine(100, 40, 400, 40)

        pen.setStyle(Qt.DashLine)
        pen.setColor(Qt.yellow)
        paint.setPen(pen)
        paint.drawLine(100, 80, 400, 80)

        pen.setStyle(Qt.DashDotLine)
        pen.setColor(Qt.red)
        paint.setPen(pen)
        paint.drawLine(100, 120, 400, 120)

        pen.setStyle(Qt.DashDotDotLine)
        pen.setColor(Qt.darkMagenta)
        paint.setPen(pen)
        paint.drawLine(100, 160, 400, 160)

        pen.setStyle(Qt.DotLine)
        pen.setColor(Qt.darkGreen)
        paint.setPen(pen)
        paint.drawLine(100, 200, 400, 200)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([4, 4, 5, 4]) # 대쉬 # 공간 # 대쉬 # 공간
        pen.setColor(Qt.darkGray)
        pen.setWidth(8)
        paint.setPen(pen)
        paint.drawLine(100, 240, 400, 240)



app = QApplication(sys.argv)
exc = myapp()
app.exec_()

