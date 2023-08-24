# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

lst = []
n = int(input("N> "))
for i in range(n):
    lst.append(int(input(f"{i+1}: ")))
x = int(input("X> "))
diff_min = abs(lst[0]-x)
num = lst[0]
for i in lst:
    if abs(i-x) < diff_min:
        diff_min = abs(i-x)
        num = i
print(num)