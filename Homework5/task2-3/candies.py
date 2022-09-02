from ui import UI
from game import *
import random

# Класс, описывающий игрока для игры в Конфеты
class CandiesPlayer(Player):

    # Метод для хода игрока. Возвращает введенное пользователем число
    def move(self, game):
        return self._ui.input_number(f"{self._name}, заберите от 1 до {game.max()} конфет включительно: ", 1, game.max())

# Класс, описывающий бота для игры в Конфеты
class CandiesBot(CandiesPlayer):

    # Метод для хода бота
    def move(self, game):
        total = game.total()
        max = game.max()

        if max == total:
            num = max
        else:
            n = int(total / (max + 1))
            num = random.randint(1, max) if total == max * n + n else total - (max * n + n)

        self._ui.output(f'{self._name} взял {num} конфет!')
        return num

# Класс, описывающий игру в Конфеты
class Candies(Game):

    # Максимально возможное колличество конфет, которое можно взять за один ход
    __max = 0

    # Текущее колличество конфет
    __total = 0

    # Начально колличество конфет. Хранится для сброса настроек игры
    __start_total = 0

    def __init__(self, player1: CandiesPlayer, player2: CandiesPlayer, ui: UI, max: int, total: int):
        super().__init__(player1, player2, ui)
        self.__max = max
        self.__total = total
        self.__start_total = total

    # Проверка состояния игры после каждого хода
    def _check(self, num: int, player: CandiesPlayer) -> str:
        if 1 > num > self.max():
            return self._ERROR
        self.__total -= num
        self._output_info()
        if self.__total <= 0:
            return self._WIN
        return self._NONE
    
    # Сброс настроек игры к начальным
    def _start_settings(self):
        self.__total = self.__start_total

    # Вывод информации для пользователя
    def _output_info(self):
        self._ui.output(f'Осталось конфет: {self.__total}')

    # Публичный метод, возвращает оставшееся колличество конфет 
    def total(self):
        return self.__total

    # Публичный метод, возвращает максимальное колличество конфет, которое можно взять за ход
    # Если __max больше __total, вернет __total
    def max(self):
        return self.__total if self.__total < self.__max else self.__max