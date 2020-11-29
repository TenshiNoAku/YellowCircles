import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *

SCREEN_SIZE = [500, 500]
# Задаём длину стороны и количество углов
SIDE_LENGTH = 200
SIDES_COUNT = 5


class DrawStar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 1

    def ys(self, y):
        return SCREEN_SIZE[1] // 1 - y

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        s = random.randint(50, 250)
        qp.drawEllipse(SCREEN_SIZE[0] // 2 - s // 2, SCREEN_SIZE[1] // 2 - s // 2, s, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
