#Задача 3. Вывести на экран числа от -N до N

# Попытка приведения value к типу int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Вывод чисел на экран
def output_range(value):
    value = try_to_int(value)
    if value == None:
        return False
    if value == 0:
        print(value)
    else:
        value = abs(value)
        print(*range(-value, value), value)
    return True

print('Вывод на экран чисел от -N до N')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите число: ')
    if s == '':
        exit()
    if not output_range(s):
        print('Некорректный ввод! Повторите попытку')