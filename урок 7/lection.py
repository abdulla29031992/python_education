# def f(x):
#     return x*x
# a = f
# print(a(5))


# def f(x):
#     return x*x
# print(f(5))


# def cal1(a):
#     return a + a

# def cal2(a):
#     return a * a

# def math(op, x):
#     print(op(x))

# math(cal1, 5)
# math(cal2, 5)


# def cal1(a, b):
#     return a + b

# def cal2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(cal1, 5, 5)
# math(cal2, 5, 2)


# def math(op, x, y):
#      print(op(x, y))

# cal1 = lambda a, b : a + b

# math(cal1, 5, 5) 


# def math(op, x, y):
#     print(op(x, y))

# math(lambda a, b : a + b, 5, 5)


# TASK
# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример:12358152338 Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38] 
# out = []
# for i in data :
#     if i % 2 == 0: 
#         out.append((i, i ** 2))
# print(out)
    
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38] 
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)


