# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n =  int(input('enter the number: '))
stop = 0
p = 2
for i in range(n) :
    if stop != 1 :
        p = p ** i
        if p <= n :
            print(p, end = " ")
            p = 2
            
    