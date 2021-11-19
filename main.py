from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint
import sys


class YellowCircle(QMainWindow):
    def __init__(self):
        self.do_paint = False
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        diametr = randint(10, 90)
        qp.drawEllipse(randint(10, 450), randint(10, 380), diametr, diametr)


def my_excepthook(type, value, traceback):
    print('Unhandled error:', type, value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yc = YellowCircle()
    yc.show()
    sys.excepthook = my_excepthook
    sys.exit(app.exec_())
