# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from cast import try_to_float_list

# Получение списка дробных частей элементов списка вещественных чисел
def get_fract_list(nums_list):
    return [float(f"0.{str(i).split('.')[1]}") for i in nums_list]

print('Получение разницы между максимальным и минимальным значением дробной части элементов')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите вещественные числа через пробел: ')
    if s == '':
        exit()
    nums_list = try_to_float_list(s.split())
    if nums_list == None or len(nums_list) == 0:
        print('Некорректный ввод! Повторите попытку...')
        continue
    fract_list = get_fract_list(nums_list)
    max = max(fract_list)
    min = min(fract_list)
    print(f"{max} - {min} = {'{0:g}'.format(max - min)}")