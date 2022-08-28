# Задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

from random import randint
from polynomial import Polynomial

def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print('Формирование многочлена и запись его в файл')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите колличество коэффициентов (k >= 2): ')
    if s == '':
        exit()
    k = try_to_int(s)
    if k == None or k < 2:
        print('Некорректный ввод! Повторите попытку...')
        continue
    p = Polynomial(*[randint(0, 100) for _ in range(k)])
    file_name = 'file.txt'
    with open(file_name, 'w') as file:
        file.write(str(p))
    print(f'Многочлен {p} записан в файл {file_name}')