# Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

import random

# Класс, описывающий арифметическое выражение
class ArithmeticExpression:

    # Строка, содержащая арифметическое выражение экземпляра класса
    __exp: str = None

    # Строка, содержащая результат вычисления арифметического выражения экземпляра класса
    __result: str = None

    # Инициализация объекта класса арифмитеческого выражения
    # На вход принимает строку с арифметическим выражением
    def __init__(self, exp: str) -> None:
        if type(exp) != str:
            raise TypeError

        if len(exp) < 3:
            raise ValueError

        try:
            self.__calc_exp(exp)
        except ZeroDivisionError:
            self.__result = "ZeroDivisionError"
        except TypeError or ValueError:
            raise
        self.__exp = exp

    # Возвращает строку, содержащую арифметическое выражение экземпляра класса
    def exp(self) -> str:
        return self.__exp

    # Возвращает строку, содержащую результат вычисления арифметического выражения экземпляра класса
    def result(self) -> str:
        return self.__result

    # Метод вычисления арифметического выражения экземпляра класса
    # Сначала производит вычисление внутри скобок
    def __calc_exp(self, exp: str) -> str:
        exp = exp.replace('- ', '+ -')
        while True:
            start = None
            stop = None
            for n in range(len(exp)):

                if exp[n] == '(':
                    if n == len(exp) - 1:
                        raise ValueError
                    start = n

                if exp[n] == ')':
                    if start == None:
                        raise ValueError
                    stop = n + 1
                    break

            if start == None:
                break
            else:
                try:
                    result = ArithmeticExpression.__calc_subexp(exp[start + 1:stop - 1])
                except ZeroDivisionError:
                    raise
                exp = exp.replace(exp[start:stop], result)
        try:
            self.__result = ArithmeticExpression.__calc_subexp(exp)
        except ZeroDivisionError:
            raise

    # Метод вычисления переданного арифметического выражения
    def __calc_subexp(exp: str) -> str:
        values_list = exp.split()
        for i in (True, False):
            try:
                ArithmeticExpression.__calc(values_list, i)
            except ZeroDivisionError:
                    raise

        return ' '.join(values_list)

    # Метод, определяющий текущий оператор
    def __calc(values_list: list, is_mult_or_div: bool) -> None:
        while True:
            found = False
            for i in range(len(values_list)):
                try:
                    found = ArithmeticExpression.__mult_div(values_list, i) if is_mult_or_div else ArithmeticExpression.__add_sub(values_list, i)
                except ZeroDivisionError:
                    raise
                if found:
                    break
            if not found:
                break
    
    # Метод умножения и деления элементов списка
    def __mult_div(values_list: list, index: int) -> bool:
        if values_list[index] == '*' or values_list[index] == '/':
            ArithmeticExpression.__adjustment_items(values_list, index)
            if values_list[index] == '*':
                result = float(values_list[index - 1]) * float(values_list[index + 1])
            else:
                try:
                    result = float(values_list[index - 1]) / float(values_list[index + 1])
                except ZeroDivisionError:
                    raise
            ArithmeticExpression.__process_list(values_list, index, result)
            return True
        return False
    
    # Метод сложения и вычитания элементов списка
    def __add_sub(values_list: list, index: int) -> bool:
        if values_list[index] == '+' or values_list[index] == '-':
            ArithmeticExpression.__adjustment_items(values_list, index)
            if values_list[index] == '+':
                result = float(values_list[index - 1]) + float(values_list[index + 1])
            else:
                result = float(values_list[index - 1]) + float(values_list[index + 1])
            ArithmeticExpression.__process_list(values_list, index, result)
            return True
        return False

    # Метод обработки невалидных элементов списка
    def __adjustment_items(values_list: list, index: int) -> None:
        values_list[index - 1] = values_list[index - 1].replace('--', '')
        values_list[index + 1] = values_list[index + 1].replace('--', '')

    # Метод обработки результат операции и удаления операндов
    def __process_list(values_list: list, index: int, value: float) -> None:
        values_list[index] = '{0:g}'.format(round(value, 2))
        values_list.pop(index + 1)
        values_list.pop(index - 1)

    # Метод генерации случайного арифметического выражения
    # Принимает колличество элементов выражения, максимально допустимое значение элемента 
    # и возможность включения в выражение вещественных чисел
    def random(numbers_count: int, max: int, only_int: bool = True) -> str:

        if numbers_count < 2 or max <= 0:
            raise ValueError

        operators = '+-*/'

        is_parenthes = False
        parentheses_count = 0
        numbers = [random.randint(-max, max) + (round(random.random(), 2) if not only_int else 0) for _ in range(numbers_count)]
        result = ''

        for i in range(len(numbers)):
            n = numbers[i]
            while True:
                operator = operators[random.randint(0, len(operators) - 1)]
                if operator != '/' or n != 0:
                    break

            n = '{0:g}'.format(n)

            if i < len(numbers) - 1 and random.randint(0, 3) == 0:
                n = f"{'-' if random.randint(0, 1) == 0 else ''}({n}"
                parentheses_count += 1
                is_parenthes = True

            if not is_parenthes and parentheses_count > 0 and random.randint(0, 1) == 0:
                n = f'{n})'
                parentheses_count -= 1
            
            is_parenthes = False

            result = f"{result} {operator} {n}"

        result = result.strip() \
            .replace('- -', '+ ') \
            .replace('- +', '- ') \
            .replace('+ -', '- ') \
            .replace('+ +', '+ ') \
            .replace('-0 ', '0 ') \
            .strip('+') \
            .strip('*') \
            .strip('/') \
            .strip()

        while parentheses_count > 0:
            result += ')'
            parentheses_count -= 1

        if result[0] == '-' and result[1] == ' ':
            result = result[0] + result[2:]

        return result

def main() -> None:
    for _ in range(10):
        exp_str = ArithmeticExpression.random(random.randint(3, 10), 10, random.randint(0, 1))
        exp = ArithmeticExpression(exp_str)
        print(f'{exp.exp()} = {exp.result()}')

    while True:
        exp_str = input('Введите арифметическое выражение (разделяйте знаки пробелом): ')
        try: 
            exp = ArithmeticExpression(exp_str)
        except ValueError or TypeError:
            print('Некорректный ввод. Повторите попытку...')
            continue

        print(f'{exp.exp()} = {exp.result()}')

if __name__ == '__main__':
    main()