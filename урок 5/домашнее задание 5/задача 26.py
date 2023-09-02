# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (35) A = 2; B = 3 -> 8

# variant 1

def recr(a, b):
    if b == 1:
        return a
    return a*recr(a, b-1)


a = int(input("A = "))
b = int(input("B = "))
print(recr(a, b))


#variant 2

def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a