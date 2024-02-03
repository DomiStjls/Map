from io import BytesIO

import requests
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image

delta = 0.005
coor = (59.119361, 37.904043)


def get_image():
    global delta, coor
    lattitude, longitude = coor
    map_params = {
        "ll": ",".join([str(longitude), str(lattitude)]),
        "spn": ",".join([str(delta), str(delta)]),
        "l": "sat"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).save("ans.jpg")


def set_delta(v):
    global delta
    delta = max(0.002, delta * v)
    get_image()


class Map(QtWidgets.QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        uic.loadUi("map.ui", self)
        pixmap = QPixmap("ans.jpg")
        self.image.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    set_delta(1.5)
    get_image()
    main = Map()
    main.show()
    sys.exit(app.exec_())
