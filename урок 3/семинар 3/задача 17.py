# Задача 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

# print(len(set(input().split())))    
# print(len(set(input())) - 1)  

# sp = [1, 1, 2, 0, -1, 3, 4, 4]
# sp = set (sp)
# print(len(sp))


from random import randint


list = [randint(-10,10) for _ in range(10)]

#for i in range(10):
#    list.append(randint(-10,10))

print(list)

result = set(list)

print(len(result))

