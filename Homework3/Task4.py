# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

from cast import try_to_int

# Преобразование десятичного числа в двоичное
def binary(num):
    if num in range(-1, 2):
        return num
    sign = -1 if num < 0 else 1
    num = abs(num)
    factor = 1
    result = 0
    while num > 0:
        result += num % 2 * factor
        factor = factor * 10
        num = num // 2
    return result * sign

print('Преобразование десятичного числа в двоичное')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите целое число: ')
    if s == '':
        exit()
    num = try_to_int(s)
    print(binary(num) if num != None else 'Некорректный ввод! Повторите попытку...')