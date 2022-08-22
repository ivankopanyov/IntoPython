# Задача 16. Задать список из n чисел последовательности (1 + 1 / n) * n и вывести на экран их сумму

def list_sum(n):
    return sum([(1 + 1 / i) * i for i in range(1, n + 1)])

print(list_sum(1)) # 2
print(list_sum(2)) # 5
print(list_sum(3)) # 9