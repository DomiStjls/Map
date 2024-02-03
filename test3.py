from io import BytesIO

import requests
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image


def get_image(coor, delta):
    lattitude, longitude = coor.split(" ")
    map_params = {
        "ll": ",".join([longitude, lattitude]),
        "spn": ",".join([delta, delta]),
        "l": "sat"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).save("ans.jpg")


class Map(QtWidgets.QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        uic.loadUi("map.ui", self)
        pixmap = QPixmap("ans.jpg")
        self.image.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    get_image("59.119361 37.904043", "0.005")
    main = Map()
    main.show()
    sys.exit(app.exec_())
