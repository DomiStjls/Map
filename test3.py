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


class Map(QtWidgets.QMainWindow):
    def __init__(self):
        super(Map, self).__init__()

        self.setupUi(self)
        pixmap = QPixmap("ans.jpg")
        self.image.setPixmap(pixmap)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(0, 0, 600, 450))
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(610, 110, 351, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.i = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.i.setObjectName("i")
        self.horizontalLayout.addWidget(self.i)
        self.chb3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chb3.setObjectName("chb3")
        self.horizontalLayout.addWidget(self.chb3)
        self.chb2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chb2.setObjectName("chb2")
        self.horizontalLayout.addWidget(self.chb2)
        self.chb1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chb1.setObjectName("chb1")
        self.horizontalLayout.addWidget(self.chb1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        """
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        """
        self.find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.find.setObjectName("find")
        self.horizontalLayout_2.addWidget(self.find)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.adress = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.adress.setText("")
        self.adress.setObjectName("adress")
        self.verticalLayout.addWidget(self.adress)
        self.sbros = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sbros.setObjectName("sbros")
        self.verticalLayout.addWidget(self.sbros)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionup = QtWidgets.QAction(MainWindow)
        self.actionup.setObjectName("actionup")
        self.actiondown = QtWidgets.QAction(MainWindow)
        self.actiondown.setCheckable(True)
        self.actiondown.setObjectName("actiondown")
        self.actionleft = QtWidgets.QAction(MainWindow)
        self.actionleft.setObjectName("actionleft")
        self.actionright = QtWidgets.QAction(MainWindow)
        self.actionright.setObjectName("actionright")
        self.actionup_2 = QtWidgets.QAction(MainWindow)
        self.actionup_2.setObjectName("actionup_2")
        self.actiondown_2 = QtWidgets.QAction(MainWindow)
        self.actiondown_2.setObjectName("actiondown_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.i.setText(_translate("MainWindow", "индес"))
        self.chb3.setText(_translate("MainWindow", "схема"))
        self.chb2.setText(_translate("MainWindow", "гибрид"))
        self.chb1.setText(_translate("MainWindow", "спутник"))
        self.find.setText(_translate("MainWindow", "Найти"))
        self.sbros.setText(_translate("MainWindow", "Сброс поиска"))
        self.actionup.setText(_translate("MainWindow", "pgup"))
        self.actionup.setToolTip(_translate("MainWindow", "pgup"))
        self.actionup.setShortcut(_translate("MainWindow", "PgUp"))
        self.actiondown.setText(_translate("MainWindow", "pgdown"))
        self.actiondown.setToolTip(_translate("MainWindow", "pgdown"))
        self.actiondown.setShortcut(_translate("MainWindow", "PgDown"))
        self.actionleft.setText(_translate("MainWindow", "left"))
        self.actionleft.setShortcut(_translate("MainWindow", "Left"))
        self.actionright.setText(_translate("MainWindow", "right"))
        self.actionright.setShortcut(_translate("MainWindow", "Right"))
        self.actionup_2.setText(_translate("MainWindow", "up"))
        self.actionup_2.setToolTip(_translate("MainWindow", "up"))
        self.actionup_2.setShortcut(_translate("MainWindow", "Up"))
        self.actiondown_2.setText(_translate("MainWindow", "down"))
        self.actiondown_2.setShortcut(_translate("MainWindow", "Down"))
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_PageUp:
            set_delta(0.75)
            self.update()
        if e.key() == Qt.Key_PageDown:
            set_delta(1.5)
            self.update()
        if e.key() == Qt.Key_Down:
            self.move(-1, 0)
            self.update()
        if e.key() == Qt.Key_W:
            move(1, 0)
            self.update()
        if e.key() == Qt.Key_S:
            move(0, -1)
            self.update()
        if e.key() == Qt.Key_D:
            move(0, 1)
            self.update()
        if e.key() == Qt.Key_A:
            move(0, 1)
            self.update()

    def update(self):
        get_image()
        pixmap = QPixmap("ans.jpg")
        self.image.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    get_image()
    main = Map()
    main.show()
    sys.exit(app.exec_())
