from io import BytesIO

import requests
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtCore import Qt
from PIL import Image

delta = 0.005
coor = (59.119361, 37.904043)


def get_image():
    global delta, coor
    lattitude, longitude = coor
    map_params = {
        "ll": ",".join([str(longitude), str(lattitude)]),
        "spn": ",".join([str(delta), str(delta)]),
        "l": "sat",
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(response.content)).save("ans.jpg")


def set_delta(v):
    global delta
    delta = max(0.002, delta * v)
    get_image()


def move(h, v):
    pass


def change(*args):  # смена вида карты схема=1\спутник=2\гибрид=3
    pass


def find(*args):  # поиск места + метка, которая сохраняется + должна возвращать полный адрес найдекного места + подается адрес и true/false надо ли искать индекс(если true надо)
    pass
def delete_mark(): # не очень понима., что должна делать функция, но по идее убирать последнюю метку
    pass
