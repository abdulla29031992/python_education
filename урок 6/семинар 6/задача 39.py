# Задача 39. Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# import random

# n = int(input())
# lst1=[random.randint(0,10) for i in range(n)]
# print(lst1)

# m = int(input())
# lst2=[random.randint(0,10) for i in range(m)]
# print(lst2)

# lst3=[]
# for i in lst1:
#     if i not in lst2:
#         lst3.append(i)

# print(lst3) 


# varuiant 2

# from random import randint

# list1_length = int(input('Введите число элементов первого массива ->'))
# list2_length = int(input('Введите число элементов первого массива ->'))

# sp = [randint(1,10) for x in range(list1_length)]
# sp2 = [randint(1,10) for x in range(list2_length)]

# print(sp)
# print(sp2)

# print ([x for x in sp if x not in sp2 ])