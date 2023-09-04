# Задача 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

import random

n = int(input())
list = [random.randint(0, 10) for i in range(n)]
print(list)

count = 0

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            count += 1

print(count)
