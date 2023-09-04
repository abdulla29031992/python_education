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


#  variant 2

# import random

#n = int(input("Введите размер массива: "))
#array = [random.randint(0,4) for _ in range(5)]

# print(array := [1, 2, 3, 2, 3, 2, 2, 2, 3,3])
# print(sum([array.count(x)//2 for x in set(array)]))
