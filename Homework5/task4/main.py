# Задание 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from os.path import *
import random

# Функция генерации строк для обработки
def generate_str():
    indexes = [(97, 122), (65, 90), (48, 57), (1072, 1103), (1040, 1071)]
    symbols = []
    for i in indexes:
        symbols += [chr(i) for i in range(i[0], i[1] + 1)]
    symbols += [' ', '.', ',']
    result = ''
    for _ in range(random.randint(5, 10)):
        line = ''
        for _ in range(random.randint(5, 10)):
            symbol = symbols[random.randint(0, len(symbols) - 1)]
            line += ''.join([symbol for _ in range(random.randint(1, 20))])
        result += line + '\n'
    return result

# Функция RLE кодирования
def rle_encode(data):
    data = data.replace('"', "'")

    if len(data) == 0:
        return data

    count = 0
    symbol = None
    result = ''
    
    for i in data:
        if symbol == None:
            symbol = i
            count += 1
            continue
        if i == symbol:
            count += 1
            continue
        if count > 1:
            result += str(count)
        result += f'"{symbol}"' if symbol.isdigit() else symbol
        symbol = i
        count = 1

    if count > 1:
        result += str(count)
    result += f'"{symbol}"' if symbol.isdigit() else symbol

    return result

# Функция RLE декодирования
def rle_decode(data: str):
    result = ''
    count = ''
    in_mark = False

    for i in data:

        if i == '"':
            in_mark = not in_mark
            continue

        if in_mark or not i.isdigit():
            result += ''.join([i for _ in range((int(count) if len(count) > 0 else 1))])
            count = ''
            continue

        count += i
    
    return result

def main():

    folder = join('Homework5', 'task4')
    source = 'source.txt'
    encode = 'encode.txt'
    decode = 'decode.txt'

    # Записываем в исходный файл сгенерированные строки
    source_path = join(folder, source)
    with open(source_path, 'w', encoding='utf-8') as file:
        file.write(generate_str())

    # Записываем в файл закодированнное содержание исходного файла
    encode_path = join(folder, encode)
    with open(source_path, 'r', encoding='utf-8') as source_file:
        with open(encode_path, 'w', encoding='utf-8') as encode_file:
            encode_file.write(rle_encode(source_file.read()))
            
    print(f'Результат кодирования успешно записан в файл {encode}')

    # Записываем в файл закодированнное содержание исходного файла
    decode_path = join(folder, decode)
    with open(encode_path, 'r', encoding='utf-8') as encode_file:
        with open(decode_path, 'w', encoding='utf-8') as decode_file:
            decode_file.write(rle_decode(encode_file.read()))
            
    print(f'Результат декодирования успешно записан в файл {decode}')

if __name__ == '__main__':
    main()