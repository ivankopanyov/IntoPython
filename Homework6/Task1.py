# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

from random import randint

# Создание файла со списком чисел
def generate_file(file_name: str) -> None:
    nums_list = get_nums_list(randint(1, 10), randint(3, 10))
    nums_list.pop(randint(1, len(nums_list) - 2))
    with open(file_name, 'w') as file:
        file.write(' '.join(list(map(str, nums_list))))

# Создание списка возрастающей последовательности чисел заданной длины 
# с заданным значением первого элемента
def get_nums_list(start_value: int, length: int) -> list:
    return [i + start_value for i in range(length)]

# Поиск пропущенного элемента в возрастающей последовательности
def get_pass_in_list(nums_list: list) -> int:
    for i in range(1, len(nums_list)):
        if nums_list[i] - 1 != nums_list[i - 1]:
            return nums_list[i] - 1

# Получение списка чисел из файла
def get_nums_list_from_file(file_name: str) -> list:
    with open(file_name, 'r') as file:
        return list(map(int, file.read().split()))

def main() -> None:
    file_name = "source.txt"
    for _ in range(10):
        generate_file(file_name)
        nums_list = get_nums_list_from_file(file_name)
        result = get_pass_in_list(nums_list)
        print(f"{' '.join(map(str, nums_list))}  ->  {result}")

if __name__ == '__main__':
    main()