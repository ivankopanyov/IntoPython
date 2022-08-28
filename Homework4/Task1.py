# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Получение списка простых множителей введенного числа
def get_prime_factors(value):
    value = try_to_int(value)
    if type(value) == None or value <= 0:
        return None
    if value in range(1, 4):
        return [1, value]
    result = []
    d = 2
    while d * d <= value:
        if value % d == 0:
            result.append(d)
            value //= d
        else:
            d += 1
    if value > 1:
        result.append(value)
    if (len(result) == 1):
        result.insert(0, 1)
    return result

print('Составление списка простых множителей введенного числа')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите натуральное число: ')
    if s == '':
        exit()
    prime_factors = get_prime_factors(s)
    print(f"{' x '.join(map(str, prime_factors))} = {s}" if prime_factors != None else 'Некорректный ввод! Повторите попытку...')