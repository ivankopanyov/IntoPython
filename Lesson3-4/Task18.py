# Задача 18. Реализовать алгоритм перемешивания списка.

import random

# Перемешивание списка
def shuffle_list(value):
    if type(value) != list:
        return None
    if len(value) <= 1:
        return value
    for i in range(0, len(value) - 1):
        temp = value[i]
        rand_num = random.randint(i + 1, len(value) - 1)
        value[i] = value[rand_num]
        value[rand_num] = temp
    return value

print('Перемешивание списка')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите элементы списка через пробел: ')
    if s == '':
        exit()
    print(*shuffle_list(s.split()))