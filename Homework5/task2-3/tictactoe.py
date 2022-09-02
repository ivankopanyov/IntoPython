from game import *
import random

# Класс, описывающий игрока в крестики-нолики
class TicTacToePlayer(Player):

    # Символ для хода игрока
    _sign = None

    # Метод изменения символа игрока
    def set_sign(self, value: str):
        self._sign = value

    # Метод, возвращающий символ игрока
    def sign(self):
        return self._sign

    # Метод хода игрока
    def move(self, game):
        while True:
            field = game.field()
            num = self._input_number(field) - 1
            if field[num] != TicTacToe.EMPTY:
                self._output_error_message()
                continue
            self._output()
            return num

    # Метод, возвращающий число, введенное пользователем
    def _input_number(self, field: list) -> int:
        return self._ui.input_number(f"{self._name}, укажите номер пустого поля: ", 1, len(field))

    # Метод для вывода сообщения для пользователя
    # Реализуется в наследнике
    def _output(self):
        pass

    # Вывод сообщения об ошибке
    def _output_error_message(self):
        self._ui.output('Этот ход уже был! Повторите попытку...')

# Класс, описывающий бота для игры в крестики-нолики
class TicTacToeBot(TicTacToePlayer):

    # Метод, рассчитывающий ход бота
    def _input_number(self, field: list) -> int:
        vs_sign = TicTacToe.CROSS if self.sign() != TicTacToe.CROSS else TicTacToe.ZERO
        moves = [(self.sign(), 2), (vs_sign, 2), (self.sign(), 1), (vs_sign, 1)]
        for move in moves:
            result = self.__find_cell(move[0], move[1], field)
            if result != None:
                return result + 1

        return random.randint(1, len(field))

    # Проверка игрового поля
    def __find_cell(self, sign, sign_count, field):
        empties = []
        for line in TicTacToe.LINES:
            counter = 0
            temp_empties = []
            for i in line:
                if field[i] == TicTacToe.EMPTY:
                    temp_empties.append(i)
                if field[i] == sign:
                    counter += 1
            if counter >= sign_count and temp_empties != None:
                empties += temp_empties
        return None if len(empties) == 0 else empties[random.randint(0, len(empties) - 1)]

    # Метод для вывода сообщения для пользователя
    def _output(self):
        self._ui.output(f'{self.name()} сделал ход!')

    # Вывод сообщения об ошибке
    # Реализуется в базовом классе
    def _output_error_message(self):
        pass

# Класс, описывающий игру в крестики нолики
class TicTacToe(Game):

    # Константы, содержащие символы для вывода в игровое поле
    EMPTY = ' '
    CROSS = 'X'
    ZERO = '0'

    # Индексы линий игровогополя для проверки
    LINES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    # Список, хранящий состояние клеток игрового поля
    __field = None

    # Проверка состояния игры после каждого хода игрока
    def _check(self, num: int, player: TicTacToePlayer) -> str:
        if not num in range(0, 9) or self.__field[num] != self.EMPTY:
            return self._ERROR

        self.__field[num] = player.sign()

        self._output_info()

        for line in self.LINES:
            last = None
            for i in line:
                if self.__field[i] == self.EMPTY:
                    last = None
                    break
                if  self.__field[i] == self.EMPTY or last == None:
                    last = self.__field[i]
                else:
                    if last != self.__field[i]:
                        last = None
                        break
            if last != None:
                return self._WIN
        
        if not self.EMPTY in self.__field:
            return self._DRAW

        return self._NONE

    # Сброс настроек к стартовым
    def _start_settings(self):
        self._player1.set_sign(self.CROSS)
        self._player2.set_sign(self.ZERO)
        self.__field = [self.EMPTY for _ in range(9)]

    # Вывод информации для пользователя
    def _output_info(self):
        self._ui.output_field(self.__field)

    # Метод возвращающий копию списка, хранящего состояние клеток игрового поля
    def field(self):
        return self.__field.copy()