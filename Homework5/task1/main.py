# Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from os.path import *

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

    folder = join('Homework5', 'task1')
    source = 'source.txt'
    result = 'result.txt'

    # Проверяем наличие файла с ресурсом
    source_path = join(folder, source)
    if not exists(source_path):
        print(f'Файл {source} не найден!')
        exit()

    # Очищаем файл для записи результата
    result_path = join(folder, result)
    if exists(result_path):
        with open(result_path, 'w') as file:
            file.write('')

    file_handle(lambda s: remove_words(s, 'абв') , source_path, result_path)
    print(f'Результат успешно записан в файл {result}')