# Задача No49. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
# по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
# зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины 
# полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные 
# выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти 
# и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# varaint 1
# def find_farthest_orbit(orbits):
#     s_orbits = list(map(lambda x: x[0]*x[1]*3.14 if x[0]!=x[1] else -1,orbits))
#     max_indx = s_orbits.index(max(s_orbits))
#     return orbits[max_indx]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
# print(*find_farthest_orbit(orbits))



# variant 2
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# find_farthest_orbit = lambda x,y: 3.14*x*y
# s_max=0
# best_planet = list()
# for x,y in orbits:
#     if x!=y:
#         s_planet=find_farthest_orbit (x,y)
#         if s_planet>s_max:
#             s_max=s_planet
#             best_planet.clear()
#             best_planet.append((x,y))
# print (s_max, best_planet)



# variant 3
# import math

# def find_farthest_orbit(list_of_orbits):
# #S = pi*a*b
# #a и b - длины полуосей эллипса
#     S = list(map(lambda x : math.pi*x[0]*x[1] if x[0] != x[1] else 0, list_of_orbits))
#     return S.index(max(S))


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits), orbits[find_farthest_orbit(orbits)])




