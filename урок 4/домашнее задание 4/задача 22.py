# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


n = int(input("N> "))
m = int(input("M> "))
numbers_n = set(list(map(int, input(f"Множество {n} элементов > ").split())))
numbers_m = set(list(map(int, input(f"Множество {m} элементов > ").split())))

for i in numbers_n:
    if i in numbers_m:
        print (i)
