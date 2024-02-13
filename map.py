from io import BytesIO

import requests
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt
from PIL import Image
from q import get_image, set_delta, change, move, find, delete_mark, take_cords


class Map(QtWidgets.QMainWindow):
    def __init__(self):
        super(Map, self).__init__()

        self.setupUi(self)
        pixmap = QPixmap("ans.png")
        self.image.setPixmap(pixmap)
        self.group = QButtonGroup()
        self.group.buttonClicked.connect(self.change_fon)
        self.group.addButton(self.chb1)
        self.group.addButton(self.chb2)
        self.group.addButton(self.chb3)
        self.i.clicked.connect(self.show_index)
        self.print_index = False
        self.change_pos = True
        self.setMouseTracking(True)
        self.centralWidget().setMouseTracking(True)
        self.image.setMouseTracking(True)
        self.image.installEventFilter(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
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
        self.i = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.i.setObjectName("i")
        self.horizontalLayout.addWidget(self.i)
        self.chb3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.chb3.setObjectName("chb3")
        self.horizontalLayout.addWidget(self.chb3)
        self.chb2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.chb2.setObjectName("chb2")
        self.horizontalLayout.addWidget(self.chb2)
        self.chb1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.chb1.setObjectName("chb1")

        self.chb1.setChecked(True)
        self.chb2.setChecked(False)
        self.chb3.setChecked(False)
        self.i.setChecked(False)

        self.horizontalLayout.addWidget(self.chb1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.LineEdit.setObjectName("LineEdit")
        self.horizontalLayout_2.addWidget(self.LineEdit)
        self.find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.find.setObjectName("find")

        self.find.clicked.connect(self.find_place)

        self.horizontalLayout_2.addWidget(self.find)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.adress = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.adress.setText("")
        self.adress.setObjectName("adress")
        self.verticalLayout.addWidget(self.adress)
        self.sbros = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sbros.setObjectName("sbros")

        self.sbros.clicked.connect(self.delete_res)

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
        self.i.setText(_translate("MainWindow", "показывать ли индекс"))
        self.chb3.setText(_translate("MainWindow", "схема"))
        self.chb2.setText(_translate("MainWindow", "гибрид"))
        self.chb1.setText(_translate("MainWindow", "спутник"))
        self.chbs = [self.chb3, self.chb2, self.chb1]
        self.find.setText(_translate("MainWindow", "Найти"))
        self.sbros.setText(_translate("MainWindow", "Сброс поиска"))

    def eventFilter(self, obj, event):
        if obj == self.image and event.type() == event.MouseMove:
            self.statusbar.showMessage(f"{event.x()}, {event.y()}")
            m = list(take_cords(event.x(), event.y()))
            self.statusbar.showMessage(f"{m[0]}, {m[1]}")
        return super().eventFilter(obj, event)

    def mousePressEvent(self, e):
        if e.button() == Qt.RightButton and (e.x() < 600 and e.y() < 450):
            pass
        if e.button() == Qt.LeftButton and (e.x() < 600 and e.y() < 450):
            t = find(", ".join(take_cords(e.x(), e.y())), self.print_index, self.change_pos)
            self.adress.setText(t)
            self.update()

    def show_index(self):
        self.print_index = self.i.isChecked()
        self.find_place()

    def delete_res(self):
        self.LineEdit.setText("")
        self.adress.setText("")
        delete_mark()
        self.update()

    def find_place(self, change_pos=True):
        text = self.LineEdit.text()
        if text != "":
            t = find(text, self.print_index, change_pos)
            self.adress.setText(t)
            self.update()

    def change_fon(self, b):
        for button in self.group.buttons():
            if button is not b:
                button.setChecked(False)
        # print(self.chbs.index(b) + 1)
        change(self.chbs.index(b) + 1)
        self.find_place()
        self.update()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_PageUp:
            set_delta(0.75)
            self.update()
        if e.key() == Qt.Key_PageDown:
            set_delta(1.5)
            self.update()
        if e.key() == Qt.Key_Down:
            move(0, -1)
            self.update()
        if e.key() == Qt.Key_Up:
            move(0, 1)
            self.update()
        if e.key() == Qt.Key_Left:
            move(-1, 0)
            self.update()
        if e.key() == Qt.Key_Right:
            move(1, 0)
            self.update()
        """
        if e.key() == Qt.Key_W:
            move(0, 1)
            self.update()
        if e.key() == Qt.Key_S:
            move(0, -1)
            self.update()
        if e.key() == Qt.Key_D:
            move(1, 0)
            self.update()
        if e.key() == Qt.Key_A:
            move(-1, 0)
            self.update()
            """

    """
    def mouseMoveEvent(self,e):
        if e.x() < 600 and e.y() < 450:
            self.statusbar.setStatusTip(f"{e.x()}, {e.y()}")
            """

    def update(self):
        get_image()
        pixmap = QPixmap("ans.png")
        self.image.setPixmap(pixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    get_image()
    main = Map()
    main.show()
    sys.exit(app.exec_())
