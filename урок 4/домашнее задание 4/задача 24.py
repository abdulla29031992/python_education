# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# i ягод.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло a
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

berries = []
n = int(input("N> ")) # berries = list(map(int, input(f"Введите ягоды для {n} кустов > ").split()))
for i in range(n):
    berries.append(int(input(f"Куст {i+1}: ")))

max_sum = 0

for i in range(n):
    sum = berries[i]
    left = (i-1) % n # 0-1%5 = -1, 1-1%5 = 0, 2-1%5 = 1, 3-1%5 = 2, 4-1%5 = 3, 5-1%5 = 4. При n==5
    right = (i+1) % n
    sum += berries[left] + berries[right] 
    max_sum = max(max_sum, sum)

print(max_sum)