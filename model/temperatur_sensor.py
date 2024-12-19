from random import randint

class TemperaturSensor:
    '''Класс датчика температуры'''
    _temperatur = None#Поле температуры
    _time = None#Поле временных отметок
    def __init__(self):
        self._time = [t for t in range(1, 100, 10)]
        self._temperatur = map(self.__temperatur, self._time)
        self._temperatur = list(self._temperatur)


    def __temperatur(self, t):
        '''
        Метод для генерации случайного значения для температуры
        :param t:
        :return:
        '''
        temperatur = randint(1, 100)
        return temperatur

    def getTemperatur(self):
        '''
        Метод выводит покфзания температуры
        :return:
        :name
        _temperatur
        :type
        list()
        '''
        return self._temperatur

    def getTime(self):
        '''
        Метод возвращает массив временных отметок
        :return:
        '''
        return self._time
