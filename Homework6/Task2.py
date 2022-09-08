# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7] 
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

from random import randint

# Получение списка случайных чисел заданной длины в заданном диапазоне
def get_random_list(length: int, min: int, max: int) -> list:
    return [randint(min, max) for _ in range(length)]

# Получение возрастающую последовательность из списка, 
# содержащей максимальное количество элементов
def get_max_ascending_sequence(nums_list: list) -> list:
    sequence = [0] * len(nums_list)
    for i in range(len(nums_list)):
        for j in range(i):
            if nums_list[i] > nums_list[j] and sequence[j] > sequence[i]:
                sequence[i] = sequence[j]
        sequence[i] += 1
        
    i = sequence.index(max(sequence))
    result = [i]
    while sequence[i] != 1:
        j = i - 1
        while sequence[j] != sequence[i] - 1 or nums_list[j] >= nums_list[i]: 
            j -= 1
        i = j
        result.append(nums_list[i])
    return reversed(result)

def main() -> None:
    for _ in range(10):
        nums_list = get_random_list(randint(10, 20), 0, 100)
        result = get_max_ascending_sequence(nums_list)
        print(f'{" ".join(map(str, nums_list))}  =>  {" ".join(map(str, result))}')

if __name__ == '__main__':
    main()