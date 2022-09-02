from abc import ABC, abstractmethod

# Абстракция для класса ввода-вывода информации для пользователя
class UI(ABC):

    # Функция ввода строки пользователем
    @abstractmethod
    def input_str(self, message: str, not_empty: bool) -> str:
        pass
    
    # Функция ввода целого числа пользователем в переданном диапазоне
    @abstractmethod
    def input_number(self, message: str, min: int, max: int) -> int:
        pass

    # Функция вывода сообщения пользователю
    @abstractmethod
    def output(self, message: str):
        pass

# Имплементация абстракции ввода-вывода информации для пользователя через консоль
class ConsoleUI(UI):

    # Функция ввода строки пользователем в консоли
    def input_str(self, message: str, not_empty: bool):
        while True:
            s = input(message).strip()
            if not_empty and s == '':
                print('Вводимое значение не должно быть пустым! Повторите попытку...')
            else:
                return s

    # Функция ввода целого числа пользователем в переданном диапазоне в консоли
    def input_number(self, message: str, min: int = None, max: int = None):
        while True:
            try:
                num = int(input(message))
            except ValueError:
                print('Некорректный ввод! Повторите попытку...')
                continue

            if (min != None and num < min) or (max != None and num > max):
                print('Нарушен диапазон допустимых значений! Повторите попытку...')
            else:
                return num

    # Функция вывода сообщения пользователю в консоль
    def output(self, message: str):
        print(message)