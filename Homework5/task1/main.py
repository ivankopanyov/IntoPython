# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from os.path import *
import random

# Функция генерации строк для обработки
def generate_str(entry):
    symbols = [chr(i) for i in range(1072, 1104)] + [chr(i) for i in range(1040, 1072)]
    lines = []
    for _ in range(random.randint(5, 10)):
        line = []
        for _ in range(random.randint(5, 10)):
            word = ''.join([symbols[random.randint(0, len(symbols) - 1)] for _ in range(random.randint(3, 10))])
            if random.randint(0, 1) == 0:
                pos = random.randint(0, len(word))
                word = word[:pos] + entry + word[pos + 1:]
            line.append(word)
        lines.append(' '.join(line))
    return '\n'.join(lines)

# Функция удаления слова из строки, которое содержит переданное вхождение
def remove_words(line, entry, ignore_case = True):
    if ignore_case:
        entry = entry.lower()
    return ' '.join([word for word in line.split() if not entry in (word.lower() if ignore_case else word)])

# Функция построчного измения файла через переданную функцию f
def file_handle(f, source_file, result_file):
    with open(source_file, 'r', encoding='utf-8') as source:
        with open(result_file, 'a', encoding='utf-8') as result:
            for line in source:
                result.write(f"{f(line)}\n")

if __name__ == '__main__':

    entry = 'абв'

    folder = join('Homework5', 'task1')
    source = 'source.txt'
    result = 'result.txt'

    # Записываем в исходный файл сгенерированные строки
    source_path = join(folder, source)
    with open(source_path, 'w', encoding='utf-8') as file:
        file.write(generate_str(entry))

    # Очищаем файл для записи результата
    result_path = join(folder, result)
    with open(result_path, 'w', encoding='utf-8') as file:
        file.write('')

    file_handle(lambda s: remove_words(s, entry) , source_path, result_path)
    print(f'Результат успешно записан в файл {result}')