import sys

import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPen


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle('Желтый круг')
        self.start = False

        self.btn = QPushButton('Go', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.run)

    def paintEvent(self, e):
        if self.start % 2 == 1:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(242,241,4))
            n = random.randint(10, 40)
            print(n)
            qp.drawEllipse(random.randint(20, 280), random.randint(20, 280), n, n)
            qp.end()
            self.update()
        
    def run(self):
        self.start += 1
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
