# Задача 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def contains_count(line, entry):
    return line.count(entry)

print(contains_count('AA', 'A'))
