# Задача 17. Задать список из N элементов, заполненных числами из [-N, N]. 
#            Найти произведение элементов на указанных позициях. 
#            Позиции хранятся в файле file.txt в одной строке одно число.

import random

def get_random_list(n):
    return [random.randint(-n, n) for _ in range(n)]

def read_list(file_name):
    with open(file_name, 'r') as file:
        return [int(line) for line in file]

def calc_multiply_items(indexes, values):
    result = 1
    for item in [values[i] for i in indexes]:
        result *= item
    return result

file_name = r'C:\Users\kopanev_iv\Desktop\IntoPython\Lesson3-4\file.txt'
print(calc_multiply_items(read_list(file_name), get_random_list(10)))
