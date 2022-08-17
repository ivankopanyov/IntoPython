#Задача 2. Найти максимальное из пяти чисел

# Поиск элемента списка с максимальным значением
def find_max(nums):
    if type(nums) != list or len(nums) == 0 or not all([isinstance(item, float) for item in nums]):
        return None
    return max(nums)

# Попытка приведения value к типу float
def try_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Приведение строки к списку вещественных чисел
def str_to_float_list(s):
    if (type(s) != str):
        return None
    result = []
    for i in s.split():
        num = try_to_float(i)
        if num == None:
            return None
        result.append(num)
    return result

print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите 5 чисел через пробел: ')
    if s == '':
        exit()
    nums_list = str_to_float_list(s)
    if nums_list == None:
        print('Некорректный ввод! Повторите попытку...')
        continue
    if len(nums_list) != 5:
        print('Введено некорректное колличество чисел! Повторите попытку...')
        continue
    print(f"Максимальное значение {'{0:g}'.format(find_max(nums_list))}")