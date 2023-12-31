# Задача No51. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и 
# вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
# print(‘same’) else:
# print(‘different’)


# variant 1

values = [0, 2, 10, 6]
same_by = list(filter(lambda a: True if a % 2 == 0 else False, values))
if len(values) == len(same_by):
    print('same')
else:
    print('different')


# variant 2

def same_by(characteristic, objects):
    S = set(list(map(characteristic, objects)))
    if len(S) <= 1:
        return True
    else:
        return False

values = [0, 2, 10, 6] 
 
if same_by(lambda x: x % 2, values): 
    print('same')
else:
    print('different')