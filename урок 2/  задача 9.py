# Задача 9. По данному целому неотрицательному n вычислите значение
# n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

# count = 2
# sum = 1
# a = True

# while a:
# 	try:
# 		n = int(input("Введите n: "))
# 		if n >= 0:
# 			a = False
# 		else: print("Введите положительное целое число!")
# 	except:
# 		print("Введите положительное целое число!")

# if n == 0:
# 	print("0 ! = 1")
# 	exit()
# elif n == 1:
# 	print("1 ! = 1")
# 	exit()

def fact(n):
    i = 1
    result = 1
    while i < n:
        result *= i
        i += 1
    return result


# n = int(input('Введите число ->'))
# print(fact(n))

