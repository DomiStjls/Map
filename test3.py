from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys

class Map(QtWidgets.QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        uic.loadUi("map.ui", self)
        pixmap = QPixmap("ans.png")
        self.image.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Map()
    main.show()
    sys.exit(app.exec_())
