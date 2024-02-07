from io import BytesIO

import requests
from PIL import Image

delta = (0.004, 0.003)
coor = (37.904043, 59.119361)
mode = "sat"


def get_image():
    global delta, coor, mode
    longitude, lattitude = coor
    map_params = {
        "ll": ",".join([str(longitude), str(lattitude)]),
        "spn": ",".join([str(delta[0]), str(delta[1])]),
        "l": mode,
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(response.content)).save("ans.jpg")


def set_delta(v):
    global delta
    delta = (max(0.002, delta[0] * v), max(0.0015, delta[1] * v))
    get_image()


def move(h, v):
    global coor
    coor = (coor[0] + delta[0] * h * 3, coor[1] + delta[1] * v * 2)
    get_image()


def change(*args):
    # смена вида карты схема=1\спутник=2\гибрид=3
    if args[0] == 1:
        mode = "map"
    elif args[0] == 2:
        mode = "sat"
    else:
        mode = "skl"


def find(*args):
    # поиск места + метка, которая сохраняется + должна возвращать полный адрес найдекного места + подается адрес и true/false надо ли искать индекс(если true надо)
    text, ind = args
    server = "https://search-maps.yandex.ru/v1/"
    search_params = {
        "apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
        "text": text,
        "lang": "ru_RU",
        "type": "biz",
        "ll": map(str, )
    }
    responce = requests.get(server, params=search_params)
    print(responce.json())


def delete_mark():
    # не очень понима., что должна делать функция, но по идее убирать последнюю метку
    pass


def take_cords(*args):
    global coor
    # по координатам в карте найти координаты на местности + True/False надо ли менять карту или просто отметить на существующей
    x, y = args
    x = x / 600 * delta[0] + coor[0]
    y = y / 450 * delta[1] + coor[1]
    return map(str, (y, x))
    pass
