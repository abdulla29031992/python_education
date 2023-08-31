# Задача No35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 
# Output: yes

# variant 1
# def Prime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n

# print(Prime(2))



#  variant 2

# def check_num(n, i):

#     if i > n - 1:
#         return "yes"
#     elif n % i == 0:
#         return 'no'
    
#     return check_num(n, i + 1)
    
# # num = int(input("Input num: "))
# num = 1

# print(check_num(num, 5))