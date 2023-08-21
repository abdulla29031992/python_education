# sp = [55, 111, True, "sssss", [55,77,88] ]

# for i in range(len(sp)):
#     print(sp[i], end = " ")

# print(end = "\n")
# for el in sp:
#     print(el, end = " ")

# print(end = "\n")
# for item in enumerate(sp):
#     print(item)

# from random import randint
# import time

# def show_test(upper: int) -> str :
#     print(randint(1,upper))
#     print(time.time() )
#     return 1234


# print(show_test(100))


def search_possition_number_in_Fibbonachi(number):
    num_fib = [0,1]
    while number > num_fib[-1] :
        new_num_fib = num_fib[-1]+num_fib[-2]
        num_fib.append(new_num_fib)
    if num_fib[-1] == number:
        return len(num_fib)
    return -1



try: 
    number = int(input("Введите число: "))

    print(f"Позиция числа {number} в последовательности Фиббоначи ---> {search_possition_number_in_Fibbonachi(number)}")
except:
    print("Ввели неверные данные")