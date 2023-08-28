# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# variant 1

# lst = []
# n = int(input("N> "))
# for i in range(n):
#     lst.append(int(input(f"{i+1}: ")))
# x = int(input("X> "))
# diff_min = abs(lst[0]-x)
# num = lst[0]
# for i in lst:
#     if abs(i-x) < diff_min:
#         diff_min = abs(i-x)
#         num = i
# print(num)


#  variant 2
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

