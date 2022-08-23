# Задача 11. Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

def get_multiply_list(length, multiply, start = 1):
    result = []
    for i in range(length):
        result.append(start)
        start *= multiply
    return result

print(*get_multiply_list(5, -3))