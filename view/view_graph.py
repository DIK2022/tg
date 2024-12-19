import sys

import pyqtgraph as pg
from PyQt6 import QtWidgets
from PyQt6.QtGui import QColor
from PyQt6 import QtCore

from UI.ui_GraphWindow import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__init_Tiele_Check_Box()
        self.__init_plotgraph()

    def __init_Tiele_Check_Box(self):
        '''
        Метод заполнения заголовков для чекбоксов
        :return:
        '''
        self.ui.cbMetod_1.setText("Метод 1")
        self.ui.cbMetod_2.setText("Метод 2")
        self.ui.cbMetod_3.setText("Метод 3")
        self.ui.cbMetod_4.setText("Метод 4")
        self.ui.cbMetod_5.setText("Метод 5")
        self.ui.cbMetod_6.setText("Метод 6")
        self.ui.cbMetod_7.setText("Метод 7")
        self.ui.cbMetod_8.setText("Метод 8")
        self.ui.cbMetod_9.setText("Метод 9")
        self.ui.cbMetod_10.setText("Метод 10")

    def __init_plotgraph(self):
        '''
        Метод инициализации полотна для графика.

        :return:
        '''
        self.plot_graph = pg.PlotWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.plot_graph)
        self.ui.graph_widget.setLayout(layout)
        self.plot_graph.setBackground("w")#Цвет полотна
        self.plot_graph.addLegend()#Вывод легенды на полотне
        self.plot_graph.showGrid(x=True, y=True)#Отрисовка координатной сетки
        self.plot_graph.setXRange(1, 100)  # Размер сетки по X
        self.plot_graph.setYRange(1, 100)  # Размер сетки по Y
        self.plot_graph.setTitle("Температура и Время", color="b", size="20pt")  # Заголовок полотна
        styles = {"color": "red", "font-size": "18px"}  # задаем стиль наименования
        self.plot_graph.setLabel("left", "Температура (°C)", **styles)  # наименование по оси y
        self.plot_graph.setLabel("bottom", "Время (мин.)", **styles)  # наименование по осит Z
        self.plot_graph.setBackground(QColor(100, 50, 254, 25))  # Задаем цвет полотна для отображения графика
        self.pen = pg.mkPen(color=(255, 0, 0), width=5, style=QtCore.Qt.PenStyle.DashLine)  # Задаем цвет линии графика

    def plot_line(self, name, axisX, axisY, pen, brus):
        '''
        Метод отрисовки линии графика
        :param name:наименование легенды
        :param axisX: массив значений по оси x
        :param axisY:массив значений по оси y
        :param pen:параметры линии
        :param brus:цвет маркера
        :return:
        '''
        self.plot_graph.plot(
            axisX,
            axisY,
            name=name,
            pen=pen,
            symbol="+",
            symbolSize=15,
            symbolBrush=brus
        )
