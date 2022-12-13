# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k(до 6 степени).*
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('k = '))

import random
indexList = []
for i in range(k + 1):
    indexList.append(random.randint(0, 100))
print(indexList)

equasion = [] 

i = 0
while k > -1:
    if k == 0:
        equasion.append(str(indexList[i]))
        k -= 1
    elif k == 1:
        equasion.append(str(indexList[i]))
        equasion.append('*x') 
        equasion.append('+')
        k -= 1
        i +=1
    else:
        equasion.append(str(indexList[i]))
        equasion.append('*x^') 
        equasion.append(str(k))
        equasion.append('+')
        k -= 1
        i +=1

print("".join(equasion))

with open('task4_4result.txt', 'w') as file:
    file.write("".join(equasion))