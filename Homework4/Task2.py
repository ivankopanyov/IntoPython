# Задача 2. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Получение списка неповторяющихся элементов переданного списка
def get_unique_items_list(nums_list):
    if type(nums_list) != list:
        return None
    if len(nums_list) in range(2):
        return nums_list
    result = []
    r = range(len(nums_list))
    for i in r:
        unique = True
        for j in r:
            if i != j and nums_list[i] == nums_list[j]:
                unique = False
                break
        if unique:
            result.append(nums_list[i])
    return result

print('Составление списка неповторяющихся элементов введенного списка')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите элементы списка через пробел: ')
    if s == '':
        exit()
    print(*get_unique_items_list(s.split()))