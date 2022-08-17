#Задача 1. По двум заданным числам проверить является ли одно квадратом второго

# Проверка, является ли n_sqrt квадратом n
def is_sqrt(n, n_sqrt):
    if (type(n) == int or type(n) == float) and (type(n_sqrt) == int or type(n_sqrt) == float):
        return n ** 2 == n_sqrt
    return False

# Проверка приведения value к типу float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Ввод пользователем числа
def input_number(title):
    while True:
        s = input(title)
        if s == '':
            exit()
        if is_float(s):
            return float(s)
        print("Некорректный ввод! Повторите попытку...")
        

print('Проверка, является ли одно число квадратом второго')
print('Для выхода оставьте поле пустым')

while True:
    n = input_number('Введите число: ')
    n_sqrt = input_number('Введите квадрат числа: ')

    is_not = '' if is_sqrt(n, n_sqrt) else 'не '
    print(f"{'{0:g}'.format(n_sqrt)} {is_not}является квадратом {'{0:g}'.format(n)}")
