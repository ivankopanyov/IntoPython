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

def input_polynomial(file_name):
    while True:
        s = input('Введите колличество коэффициентов (k >= 2): ')
        if s == '':
            exit()
        k = try_to_int(s)
        if k == None or k < 2:
            print('Некорректный ввод! Повторите попытку...')
            continue
        p = Polynomial(*[randint(0, 100) for _ in range(k)])
        with open(file_name, 'w') as file:
            file.write(str(p))
        print(f'Многочлен {p} записан в файл {file_name}')
        break
0
print('Формирование многочлена и запись его в файл')
print('Для выхода оставьте поле пустым')

while True:
    file_name1 = 'file1.txt'
    file_name2 = 'file2.txt'
    input_polynomial(file_name1)
    input_polynomial(file_name2)
    with open(file_name1, 'r') as file:
        p1 = Polynomial(file.read())
    with open(file_name2, 'r') as file:
        p2 = Polynomial(file.read())
    result = p1 + p2
    result_file_name = 'result.txt'
    with open(result_file_name, 'w') as file:
        file.write(str(result))
    print(f'Многочлен {result} записан в файл {result_file_name}')