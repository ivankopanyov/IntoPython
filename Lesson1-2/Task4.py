#Задача 4. Показать первую цифру дробной части числа

# Попытка приведения value к типу float
def try_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Получение первой цифры дробной части числа
def get_first_fract_number(num):
    num = try_to_float(num)
    if num == None:
        return None
    return str(num).split('.')[1][0]

print('Получение первой цифры дробной части числа')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите число: ')
    if s == '':
        exit()
    result = get_first_fract_number(s)
    print(result if result != None else 'Некорректный ввод! Повторите попытку')