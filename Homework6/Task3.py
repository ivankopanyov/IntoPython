# Вычислить число  c заданной точностью d
# Подумать, что если точность вычисления до 1000 знаков после запятой

from decimal import *

# Вычисление числа пи с помощью формулы Чудновского
def get_pi(length: int) -> Decimal:
    getcontext().prec = length
    length /= 14
    const = 13591409
    pi = Decimal(const)
    k = Decimal(1)
    counter = 1
    while counter < length:
        k *= -Decimal((6 * counter - 5) * (2 * counter - 1) * (6 * counter - 1)) \
            / Decimal(counter * counter * counter * 10939058860032000)
        value = k * (const + 545140134 * counter)
        pi += value
        counter += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** -1
    return pi

def main() -> None:
    while True:
        try:
            count = int(input("Укажите колличетво знаков (минимум 3): "))
            if count < 3:
                raise ValueError
        except ValueError:
            print("Некорректный ввод. Повторите попытку...")
            continue

        print(f'Pi = {get_pi(count)}')

if __name__ == "__main__":
    main()