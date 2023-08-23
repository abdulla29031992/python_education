#  СПИСКИ

# # list_1 = []
# # list_1 = list()
# # print(list_1)

# list_1 = [1, 2, 3, 4,]
# # print(list_1)

# # list_1 = [1, 2, 3, 4,]  
# # print(*list_1)

# # for i in list_1 :
# #     print(i)

# # for i in list_1 :
# #     print(list_1)

# # print(len(list_1))

# print(list_1[0])
# print(list_1[-2])

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)


# list_1 = []
# print(list_1)
# for i in range(5) :
#     list_1.append(i)
#     print(list_1)


# list_1 = [1, 2, 3, 4]
# print(list_1)
# print(list_1.pop())
# print(list_1)


# list_1 = [1, 2, 3, 4]
# print(list_1)
# print(list_1.pop(0))
# print(list_1)

# list_1 = [1, 2, 3, 4]
# print(list_1)
# print(list_1.insert(4, 5))
# print(list_1)


# list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(list_1[0])
# print(list_1[-1])
# print(list_1[len(list_1)-1])
# print(list_1[:])
# print(list_1[:2])
# print(list_1[len(list_1)-2:])
# print(list_1[2:9])
# print(list_1[::6])


 #    КОРТЕЖ

# t = ()
# print(type(t))

# t = (1, )
# print(type(t))

# t = (1,3,5 )
# print(type(t))

# v = [1,8,9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v
# print(a,b,c)

# t =[1, 2, 3]
# for i in t :
#     print(i)

# t =[1, 2, 3]
# for i in range(len(t)) :
#     print(t[i])

# t = [1, 2, 3]
# print(t)
# t[0] = 2
# print(t)



#   СЛОВАРЬ

# d ={}
# d =dict()

# d['q'] = 'qwerty' 
# print(d)

# d['w'] = 'werty'
# print(d)

# print(d['q'])

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} 
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐

# del dictionary['left'] # удаление элемента
# print(dictionary)
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓  
# # right: →
# dictionary[985] = 8989
# print(dictionary)


# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary.items())
# for (k,v) in dictionary.items() :
#     print(k,v)




#    МНОЖЕСТВО

# colors = {'red', 'green', 'blue'} 
# print(colors) # {'red', 'green', 'blue'} 
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'} 
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'} 
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'} 
# colors.remove('red') # KeyError: 'red' 
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'} 
# colors.clear() # { }
# print(colors) # set()

# q = set()
# print(q)

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a) 
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

a = {1,2,3}

b = frozenset(a)
print(b)