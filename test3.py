from io import BytesIO

import requests
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image

delta = (0.004, 0.003)
coor = (37.904043, 59.119361)


def get_image():
    global delta, coor
    longitude, lattitude = coor
    map_params = {
        "ll": ",".join([str(longitude), str(lattitude)]),
        "spn": ",".join([str(delta[0]), str(delta[1])]),
        "l": "map",
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(response.content)).save("ans.png")


def set_delta(v):
    global delta
    delta = (max(0.0004, delta[0] * v), max(0.0003, delta[1] * v))
    get_image()


def move(x, y):
    global coor, delta
    coor = (coor[0] + delta[0] * x, coor[1] + delta[1] * y)
    get_image()


class Map(QtWidgets.QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        uic.loadUi("map.ui", self)
        pixmap = QPixmap("ans.png")
        self.image.setPixmap(pixmap)

    def update(self):
        get_image()
        pixmap = QPixmap("ans.png")
        self.image.setPixmap(pixmap)

    def pgup(self):
        set_delta(0.75)
        self.update()

    def pgdown(self):
        set_delta(1.5)
        self.update()

    def up(self):
        self.move(-1, 0)
        self.update()

    def down(self):
        self.move(1, 0)
        self.update()

    def left(self):
        self.move(0, -1)
        self.update()

    def right(self):
        self.move(0, 1)
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    get_image()
    main = Map()
    main.show()
    sys.exit(app.exec())
