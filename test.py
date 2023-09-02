# def recr(a, b):
#     if b == 1:
#         return a
#     return a*recr(a, b-1)


# a = int(input("A = "))
# b = int(input("B = "))
# print(recr(a, b))

def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a