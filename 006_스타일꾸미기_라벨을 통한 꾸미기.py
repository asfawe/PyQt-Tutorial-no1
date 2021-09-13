import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap



class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        licat = QLabel()
        pie = QLabel()
        sun = QLabel()

        licat.setStyleSheet(
            "border-style: solid;" # dorder(보덜)(테두리를 두르다. 라는 뜻이다.)테두리-스타일을 정해준다. 선은 그냥 일반선으로 solid솔리드로 사용을 하였다.
            "border-width: 3px;" # 테두리 선에 두깨 설정
            "border-color: red;" # 테두리 선에 색깔 설정
            "border-radius: 3px;" # 둥근 테두리를 만단다. 픽셀을 올릴수록.
            "image: url(img/weniv-licat.png)" # 이미지를 가져온다.
        )
        pie.setStyleSheet(
            "border-style: double;"
            "border-width: 5px;"
            "border-color: blue;"
            "background-color: #87CEFA;"
            "image: url(img/weniv-pie.png)"
        )
        sun.setStyleSheet(
            "border-style: dot-dot-dash;"
            "border-width: 5px;"
            "border-color: green;"
            "border-radius: 3px;"
            "background-color: beige;"
            "image: url(img/weniv-sun.png)"
        )

        hbox = QHBoxLayout()
        hbox.addWidget(licat)
        hbox.addWidget(pie)
        hbox.addWidget(sun)

        self.setLayout(hbox)

        self.setGeometry(400,400,500,400)
        self.setWindowTitle('라벨을 통한 꾸미기')
        self.show()

    




app = QApplication(sys.argv)
exc = myapp()
app.exec_()

