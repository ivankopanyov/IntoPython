# Задача 15. Написать программу получающую набор произведений чисел от 1 до N.

# Попытка приведения value к типу int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Вычисление факториала
def calc_factorial(n):
    if n == 0:
        return 1
    return calc_factorial(n-1) * n

# Вычисление факториалов всех чисел в диапазоне от 1 до value
def get_multiply_list(value):
    value = try_to_int(value)
    if value == None:
        return None
    if value in range(-1, 2):
        return [abs(value)]
    return list(map(calc_factorial, range(1, abs(value) + 1)))

print('Вычисление факториалов всех чисел в диапазоне от 1 до указанного числа')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите число: ')
    if s == '':
        exit()
    result = get_multiply_list(s)
    if result == None:
        print('Некорректный ввод! Повторите попытку...')
    else:
        print(*result)