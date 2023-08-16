# Задача 6
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

number = int(input("введите шестизначный номер: "))

number1 = number // 1000
number2 = number % 1000

n1 = number1 % 10
n2 = number1 // 100
n3 = (number1 // 10) % 10
NewNumber1 = n1 + n2 + n3

a1 = number2 % 10
a2 = number2 // 100
a3 = (number2 // 10) % 10
NewNumber2 = a1 + a2 + a3

if (NewNumber1 == NewNumber2) :
    print("yes")
else :
    print("no")
    

