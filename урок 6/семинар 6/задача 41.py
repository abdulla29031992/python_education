# Задача 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.

import random

n = int(input())
list = [random.randint(0, 10) for i in range(n)]
print(list)

count = 0

for i in range(-1, len(list) - 1):
    if list[i] > list[i - 1] and list[i] + list[i + 1]:
        count += 1
print(count)

# запись в одну строку
# print(sum([1 for x in range(-1, len(list_1)-1) if list_1[x] > list_1[x+1] and list_1[x] > list_1[x-1]]))
# print(sum([1 for x in range(-1, len(list_1)-1) if list_1[x-1] < list_1[x] > list_1[x+1]]))