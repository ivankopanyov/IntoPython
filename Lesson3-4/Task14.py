# Задача 14. Подсчитать сумму цифр в вещественном числе

# Попытка приведения value к типу float
def try_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Вычисление суммы всех цифр вещественного числа
def calc_sum_nums_of_float(value):
    value = try_to_float(value)
    if type(value) != float:
        return None
    nums = str(value).replace('.', '')
    return sum(list(map(int, nums)))

print('Вычисление суммы всех цифр вещественного числа')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите вещественное число: ')
    if s == '':
        exit()
    result = calc_sum_nums_of_float(s)
    print('Некорректный ввод! Повторите попытку...' if result == None else f'Результат: {result}')