# Класс, описывающий многочлен.
class Polynomial:

    # Список коэффициентов многочлена.
    __coefs = None

    # Инициализация объекта многочлена.
    # В качестве аргументов принимает перечисление коэффециентов либо строку в формате многочлена.
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == str:
            self.__parse(args[0])
            return
        if len(args) < 2:
            raise ValueError('')
        args = list(args)
        is_zero = True
        for i in range(len(args)):
            num = self.__try_to_float(args[i])
            if num == None:
                raise ValueError('')
            if i != 0 and args[i] != 0:
                is_zero = False
            args[i] = num
        if is_zero:
            raise ValueError('')
        self.__coefs = list(args)

    # Парсинг переданной строки для получения списка коэффициентов многочлена.
    def __parse(self, value):
        value = value.replace(' ', '') \
                        .split('=')[0] \
                        .replace('*', '') \
                        .replace('-x', '-1x') \
                        .replace('+x', '+1x') \
                        .replace('+', '|+') \
                        .replace('-', '|-')
        if len(value) == 0:
            raise ValueError('')

        if value[0] == 'x':
            value = f'1{value}'

        value = value.split('|')

        if value[0] == '':
            value.pop(0)

        if len(value) == 0 or not 'x' in value[0]:
            raise ValueError('')

        result = []

        if 'x' in value[-1]:
            result.append(0.0)
        else:
            temp = self.__try_to_float(value[-1])
            if type(temp) != float:
                raise ValueError('')
            result.append(temp)
            value.pop(-1)

        if not 'x' in value[-1]:
            raise ValueError('')

        if not '^' in value[-1]:
            temp = self.__try_to_float(value[-1].split('x')[0])
            if type(temp) != float:
                raise ValueError('')
            result.append(temp)
            value.pop(-1)

        if len(value) == 0:
            self.__coefs = result
            return

        for i in reversed(range(len(value))):
            temp = value[i].split('x^')
            if len(temp) != 2:
                raise ValueError('')
            num = self.__try_to_float(temp[0])
            degree = self.__try_to_float(temp[1])
            if type(num) != float or type(degree) != float:
                raise ValueError('')
            for _ in range(int(degree) - len(result)):
                result.append(0.0)
            result.append(num)

        self.__coefs = result

    # Возвращает копию списка коэффециентов многочлена.
    def coefs(self):
        return self.__coefs.copy()

    # Переопределение оператора сложения многочленов.
    # Возвращает строку с результатом, где 'x' второго многочлена заменен на 'у'.
    def __add__(self, other):
        if type(other) != Polynomial:
            raise TypeError('')
        self_coefs = self.coefs()
        other_coefs = other.coefs()
        last = self_coefs[0] + other_coefs[0]
        self_coefs[0] = 0.0
        other_coefs[0] = 0.0
        str_self = str(Polynomial(*self_coefs)).split(' = ')[0]
        str_other = str(Polynomial(*other_coefs)).split(' = ')[0].replace('x', 'y')
        result = f"{str_self}{' + ' if other_coefs[-1] >= 0 else ''}{str_other}"
        if last != 0:
            result += f" {'+' if last > 0 else '-'} {'{0:g}'.format(abs(last))}"
        return f'{result} = 0'
    
    # Приведение многочлена к типу строки.
    def __str__(self):
        result = ''
        for i in range(len(self.__coefs)):
            if self.__coefs[i] == 0:
                continue
            temp = ' - ' if self.__coefs[i] < 0 else ' + '
            value = abs(self.__coefs[i])
            if value != 1 or i == 0:
                temp += '{0:g}'.format(value)
            if value != 1 and i > 0:
                temp += '*'
            if i > 0:
                temp += 'x'
            if i >= 2:
                temp += f'^{i}'
            result = f'{temp}{result}'
        if result[1] == '+':
            result = result.replace(' + ', '', 1)
        return f"{result} = 0"

    # Попытка приведения value к типу float
    def __try_to_float(self, value):
        try:
            return float(value)
        except ValueError:
            return None