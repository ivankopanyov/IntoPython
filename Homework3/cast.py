# Безопасное приведение типов

# Попытка приведения переданного значения к типу int
def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# Попытка приведения переданного значения к типу float
def try_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Попытка приведения всех элементов переданного списка к типу float
# Если не удалось привести хотя бы один элемент, вернет None
def try_to_float_list(nums_list):
    if type(nums_list) != list:
        return None
    result = []
    for i in nums_list:
        num = try_to_float(i)
        if num == None:
            return None
        result.append(num)
    return result