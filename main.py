# Вычислить число c заданной точностью d

import math
d = str(0.0001)
if "." in d:
    x = len(d.split(".")[1].rstrip("0"))

numberPi = math.pi
print(round(numberPi, x))


# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

N = int(input())
x = 2
while N > 1:
    if N % x == 0:
        N = N/x
        print(x)
    else:
        x = x + 1

# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [2, 3, 4, 6, 2, 1]

new_list  =[]

for i in list:
    if i not in new_list:
        new_list.append(i)

print('Уникальные элементы:', new_list)






