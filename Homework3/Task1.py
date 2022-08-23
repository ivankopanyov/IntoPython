# Задача 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from cast import try_to_float_list

# Получение списка из элементов, стоящих на нечётной позиции в переданном списке
def get_items_odd_index_list(l):
    return [l[i] for i in range(len(l)) if i % 2 != 0]

print('Получение суммы элементов списка, стоящих на нечётной позиции')
print('Для выхода оставьте поле пустым')

while True:
     s = input('Введите элементы списка через пробел: ')
     if s == '':
         exit()
     nums_list = try_to_float_list(s.split())
     if nums_list == None or len(nums_list) == 0:
         print('Некорректный ввод! Повторите попытку...')
         continue
     nums_list = get_items_odd_index_list(nums_list)
     print(' + '.join(map('{0:g}'.format, nums_list)), ' = ' if len(nums_list) > 0 else '', '{0:g}'.format(sum(nums_list)), sep='')