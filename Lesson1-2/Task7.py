#Задача 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# Попытка приведения value к типу int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def check_conditions(conditions_list, count):
    count = try_to_int(count)
    if count == None or count <= 0:
        return
    for i in (True, False):
        conditions_list.append(i)
        if len(conditions_list) == count:
            left = False
            right = True
            for condition in conditions_list:
                left = left or condition
                right = right and not condition
            print(*conditions_list, '->', not left == right)
        else:
            check_conditions(conditions_list, count)
        conditions_list.pop()


while True:
    print('Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат')
    print('Для выхода оставьте поле пустым')
    s = input('Введите колличество значение: ')
    if s == '':
        exit()
    count = try_to_int(s)
    if count == None or count <= 0:
        print('Некорректный ввод! Повторите попытку')
        continue
    check_conditions([], count)
        
        