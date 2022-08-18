#Задача 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

# Проверка приведения value к типу float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Получение положения точки на координатной плоскости
def get_point_position(x, y):
    if (type(x) != int and type(x) != float) or (type(y) != int and type(y) != float):
        return None

    if x == 0 and y == 0:
        return 'Центр'
    elif x == 0 and y < 0:
        return 'Ось Y между четвертями III и IV'
    elif x == 0 and y > 0:
        return 'Ось Y между четвертями I и II'
    elif x > 0 and y == 0:
        return 'Ось X между четвертями I и IV'
    elif x < 0 and y == 0:
        return 'Ось X между четвертями II и III'
    elif x > 0 and y > 0:
        return 'Четверть I'
    elif x < 0 and y > 0:
        return 'Четверть II'
    elif x < 0 and y < 0:
        return 'Четверть III'
    else:
        return 'Четверть IV'

# Ввод пользователем числа
def input_number(title):
    while True:
        s = input(title)
        if s == '':
            exit()
        if is_float(s):
            return float(s)
        print("Некорректный ввод! Повторите попытку...")
        

print('Получение положения точки на координатной плоскости')
print('Для выхода оставьте поле пустым')

while True:
    x = input_number('X = ')
    y = input_number('Y = ')

    print(f'Положение: {get_point_position(x, y)}')
