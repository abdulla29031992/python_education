# Задача 1: 
#  За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

n = int(input('введите какое колличестыо киллометров должна проехать машина за один день: '))
m = int(input('введите какое колличество киллометров должна проехать: '))
d = m // n
ost = m % n
print(d + bool(ost))

