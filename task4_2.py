#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def find_mult(num):
    multipliers = []
    div = 2
    while num > 1:
        while num % div == 0:
            multipliers.append(div)
            num //= div
        div += 1
    return multipliers

n = int(input('Введите число N: '))
multipliers_n = find_mult(n)

print(f'Список простых множителей числа N: {multipliers_n}')