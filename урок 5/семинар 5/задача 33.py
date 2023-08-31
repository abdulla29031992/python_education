# Задача No33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

# def max_change_min():
#     a = [0]
#     count = int(input('Кол-во оценок: '))
#     a = a * count
#     for j in range(len(a)):
#         num = int(input('Оценка: '))
#         a[j] = num
#     print('Исходник:',a)
#     for i in range(len(a)):
#         if a[i] > 3:
#             a[i] = 1
#     print('Коррекция: ',a)

# max_change_min()

def Change_Array(array, max_array, min_array):
    for i in range(len(array)):
        if array[i] == max_array:
            array[i] = min_array
    return array



array = [1, 3, 3, 3, 4]
max_array = max(array)
min_array = min(array)
print(Change_Array(array, max_array, min_array))