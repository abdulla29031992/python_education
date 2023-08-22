import random

def find_max_min_mass(count_watermelon) :
    max, min = 1, 20
    for i in range(count_watermelon) :
        mass = random.randrange(1, 21)
        print(mass, end = " ")
        if max < mass :
            mass = max
        if min > mass :
            min = mass
    else :
        print(end = "\n")
        return max, min
    
count_watermelon = int(input("Введите кол-во арбузов: "))

print(find_max_min_mass(count_watermelon))

