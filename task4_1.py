# Вычислить число ПИ c заданной точностью d
# *Пример:* 
# - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10

d = float(input('введите число d в диапазоне (10^-1 ≤ d ≤ 10^-10): '))
str_pi = '3.1415926535897'
if d <= 10**(-1) and d >= 10**(-10):
    str(d)
    print(str_pi[:len(str(d))])
else: print("Неверное значение!")