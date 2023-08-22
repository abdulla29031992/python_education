
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