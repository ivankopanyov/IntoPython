#Задача 10. Найти расстояние между двумя точками пространства

# Попытка приведения value к типу float
def try_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Ввод пользователем числа
def input_number(title):
    while True:
        s = input(title)
        if s == '':
            exit()
        num = try_to_float(s)
        if num != None:
            return num
        print("Некорректный ввод! Повторите попытку...")

# Получение расстояния между двумя точками пространства
def get_distance(X1, Y1, Z1, X2, Y2, Z2):
    if (type(X1) != int and type(X1) != float) or (type(Y1) != int and type(Y1) != float) or (type(Z1) != int and type(Z1) != float) or (type(X2) != int and type(X2) != float) or (type(Y2) != int and type(Y2) != float) or (type(Z2) != int and type(Z2) != float):
        return None
    return ((X1 - X2) ** 2 + (Y1 - Y2) ** 2 + (Z1 - Z2) ** 2)**0.5

print('Получение расстояния между двумя точками пространства')
print('Для выхода оставьте поле пустым')

while True:
    X1 = input_number('X1 = ')
    Y1 = input_number('Y1 = ')
    Z1 = input_number('Z1 = ')
    X2 = input_number('X2 = ')
    Y2 = input_number('Y2 = ')
    Z2 = input_number('Z2 = ')

    print(f'D = {get_distance(X1, Y1, Z1, X2, Y2, Z2)}')
