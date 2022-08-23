# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
from cast import try_to_float_list

# Получение произведения пар чисел списка
def sum_inverse_indexes_items(nums_list):
    return [nums_list[i] * nums_list[-(i + 1)] for i in range(math.ceil(len(nums_list) / 2))]

print('Получение произведения пар чисел списка')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите элементы списка через пробел: ')
    if s == '':
        exit()
    nums_list = try_to_float_list(s.split())
    if nums_list == None or len(nums_list) == 0:
        print('Некорректный ввод! Повторите попытку...')
        continue
    print(*list(map('{0:g}'.format, sum_inverse_indexes_items(nums_list))))