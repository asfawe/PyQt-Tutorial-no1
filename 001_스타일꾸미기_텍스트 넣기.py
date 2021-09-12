import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.text = 'Hello Weniv World!!'
        self.setGeometry(150,300,250,500)
        self.setWindowTitle('QPainter')
        self.show()

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self) # paint가 실행할 동작은 begin과 end사이에 위치해야함.
        self.drawText(event, paint)
        paint.end()

    def drawText(self, event, paint):
        paint.setPen(QColor(10,10,10))
        paint.setFont(QFont('Decorative', 10))
        paint.drawText(130, 100, 'hello world!!') # paint.drawText는 위치를 정하는것이다.
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)

app = QApplication(sys.argv)
exc = myapp()
app.exec_()

