# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

from cast import try_to_int

# Получение ряда Фибоначчи от -num до num
def fibonacci(num):
    result = [0]
    a, b = 1, 1
    c, d = 1, -1
    for _ in range(1, num + 1):
        result.append(a)
        result.insert(0, c)
        a, b = b, a + b
        c, d = d, c - d
    return result

print('Получение ряда Фибоначчи')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите число: ')
    if s == '':
        exit()
    num = try_to_int(s)
    print(fibonacci(abs(num)) if num != None else 'Некорректный ввод! Повторите попытку...')