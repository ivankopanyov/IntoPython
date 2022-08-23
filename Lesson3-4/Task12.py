# Задача 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def get_dictonary(count):
    values = [i * 3 + 1 for i in range(1, count + 1)]
    return { key + 1 : values[key] for key in range(len(values))}

print(get_dictonary(6))