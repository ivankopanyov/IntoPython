#Задача 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# Попытка приведения value к типу int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Проверка кратности числа
def is_multiple(value, multiple_value):
    if not try_to_int(value) or not try_to_int(multiple_value):
        return None
    return value % multiple_value == 0

print('Проверка, кратно ли число 5 и 10 или 15 но не 30')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите число: ')
    if s == '':
        exit()
    num = try_to_int(s)
    if num == None:
        print('Некорректный ввод! Повторите попытку')
        continue
    is_not = '' if (is_multiple(num, 5) and is_multiple(num, 10)) or (is_multiple(num, 15) and not is_multiple(num, 30)) else 'не '
    print(f'{is_not}кратно')
