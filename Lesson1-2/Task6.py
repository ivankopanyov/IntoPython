#Задача 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

# Попытка приведения value к типу int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Получение дня недели по индексу
def get_day_of_week(index):
    index = try_to_int(index)
    if index == None or index not in range(1, 8):
        return None
    days_of_week = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье'
    ]
    return days_of_week[index - 1]

# Определение, является ли день недели выходным
def is_weekend(index):
    index = try_to_int(index)
    if index == None or index not in range(1, 8):
        return None
    return index == 6 or index == 7

print('Вывод дня недели по его индексу')
print('Для выхода оставьте поле пустым')

while True:
    s = input('Введите индекс дня недели: ')
    if s == '':
        exit()
    day_of_week = get_day_of_week(s)
    if day_of_week == None:
        print('Некорректный ввод! Повторите попытку')
        continue
    print(day_of_week, '-', 'выходной' if is_weekend(s) else 'рабочий', 'день')