import random
from abc import ABC, abstractmethod
from ui import UI

# Абстрактный класс игрока
class Player(ABC):

    # Имя игрока
    _name = None

    # Интерфейс для ввода-вывода информации пользователю
    _ui = None

    def __init__(self, name: str, ui: UI):
        self._name = name
        self._ui = ui

    # Метод, возвращающий имя игрока
    def name(self) -> str:
        return self._name

    # Метод для хода игрока
    @abstractmethod
    def move(self, game) -> int:
        pass

class Game(ABC):

    # Константы для передаци состаяния игры
    _DRAW = 'draw'
    _WIN = 'win'
    _LOSE = 'lose'
    _NONE = 'none'
    _ERROR = 'error'

    # Текущие игроки
    _player1 = None
    _player2 = None

    # Интерфейс пользователя
    _ui = None

    def __init__(self, player1: Player, player2: Player, ui: UI):
        self._player1 = player1
        self._player2 = player2
        self._ui = ui

    # Метод, начинающий игру
    def start(self):
        if random.randint(0, 1) == 0:
            self._player1, self._player2 = self._player2, self._player1
        self._start_settings()
        self._process()

    # Процесс игры, вызываемый из метода start
    def _process(self):
        self._output_info()
        current = self._player1
        while True:
            while True:
                num = current.move(self)
                state = self._check(num, current)
                if state == self._ERROR:
                    self._ui.output('Некорректный ввод. Повторите попытку...')
                else:
                    break
            if state == self._WIN:
                self._ui.output(f'{current.name()} победил! Поздравляем!')
                return
            elif state == self._LOSE:
                self._ui.output(f'{current.name()} проиграл!')
                return
            elif state == self._DRAW:
                self._ui.output(f'Ничья!')
                return
            current = self._player1 if current != self._player1 else self._player2

    # Метода сброса настроек игры на стартовые
    @abstractmethod
    def _start_settings(self):
        pass

    # Метод применения хода игрока и проверка состояния игры
    @abstractmethod
    def _check(self, num: int, player: Player) -> str:
        pass

    # Метод вывода информации пользователю
    @abstractmethod
    def _output_info(self):
        pass