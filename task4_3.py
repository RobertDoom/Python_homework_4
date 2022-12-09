# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

lst_1 = list(map(int, input('Введите элементы списка через пробел: ').split()))
print(lst_1)
lst_2 = list()
for i in range(len(lst_1)):
    if int(lst_1[i]) not in lst_2:
        lst_2.append(lst_1[i])
print(lst_2)
