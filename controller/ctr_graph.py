class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # событие при нажатии на чекбокс
        self.view.ui.cbMetod_1.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_2.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_3.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_4.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_5.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_6.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_7.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_8.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_9.stateChanged.connect(self.onStateChanged)
        self.view.ui.cbMetod_10.stateChanged.connect(self.onStateChanged)

    def onStateChanged(self):
        '''
        Метод обработки нажатия чекбокса
        :return:
        '''
        self.__clear_line()#Вызываем метод очистки графика
        self.__state_check_box(self.view.ui.cbMetod_1, self.model.tm1,1)#проверяем состояние чекбокса cbMetod_1
        self.__state_check_box(self.view.ui.cbMetod_2, self.model.tm2, 2)#проверяем состояние чекбокса cbMetod_2
        self.__state_check_box(self.view.ui.cbMetod_3, self.model.tm3, 3)#проверяем состояние чекбокса cbMetod_3
        self.__state_check_box(self.view.ui.cbMetod_4, self.model.tm4, 4)#проверяем состояние чекбокса cbMetod_4
        self.__state_check_box(self.view.ui.cbMetod_5, self.model.tm5, 5)#проверяем состояние чекбокса cbMetod_5
        self.__state_check_box(self.view.ui.cbMetod_6, self.model.tm6, 6)#проверяем состояние чекбокса cbMetod_6
        self.__state_check_box(self.view.ui.cbMetod_7, self.model.tm7,7)#проверяем состояние чекбокса cbMetod_7
        self.__state_check_box(self.view.ui.cbMetod_8, self.model.tm8,8)#проверяем состояние чекбокса cbMetod_8
        self.__state_check_box(self.view.ui.cbMetod_9, self.model.tm9,9)#проверяем состояние чекбокса cbMetod_9
        self.__state_check_box(self.view.ui.cbMetod_10,self.model.tm10,10)#проверяем состояние чекбокса cbMetod_10

    def __state_check_box(self, check_box, tm, n):
        '''
        Метод проверки ссотояния чекбокса если check_box установлена галочка, отрисовываем график
        :param check_box: чекбокс над которым производятся действия
        :param tm: метод который выводится на графике
        :param n: номер метода для легенды
        :return:
        '''
        if check_box.isChecked():
            minutes = tm.getTime()
            temperature = tm.getTemperatur()
            self.view.plot_line(f"Температура с датчика №{n}", minutes, temperature, self.view.pen, "b")

    def __clear_line(self):
        '''
        Метод очистки холста отрисовки графиков
        :return:
        '''
        self.view.plot_graph.clear()

