#Задача 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

# Попытка приведения value к типу int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Получение диапазона координат по номеру четверти
def get_coor(num):
    num = try_to_int(num)
    if num == None or num not in range(1, 5):
        return None
    ranges = ['X > 0, Y > 0', 'X < 0, Y > 0', 'X < 0, Y < 0', 'X > 0, Y < 0']
    return ranges[num - 1]

print('Получение диапазона координат по номеру четверти')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите номер четверти: ')
    if s == '':
        exit()
    result = get_coor(s)
    print('Некорректный ввод! Повторите попытку' if result == None else result)