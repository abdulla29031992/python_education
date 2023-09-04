# import random

# n = int(input())
# lst1=[random.randint(0,10) for i in range(n)]
# print(lst1)

# m = int(input())
# lst2=[random.randint(0,10) for i in range(m)]
# print(lst2)

# lst3=[]
# for i in lst1:
#     if i not in lst2:
#         lst3.append(i)

# print(lst3) 




# import random

# n = int(input())
# lst = [random.randint(0, 10) for i in range(n)]
# print(lst)

# count = 0
# for i in range(1, len(lst)-1):
#     if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
#         count += 1
# print(count)



# import random

# n = int(input())
# list = [random.randint(0, 10) for i in range(n)]
# print(list)

# count = 0

# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i] == list[j]:
#             count += 1
# print(count)


# k = int(input())

# if k < pow(10, 5):
#     for n in range(1, k):
#         m = 0
#         sum2 = 0
#         for i in range(1, n//2+1):
#             if n % i == 0:
#                 m += i
#         for j in range(1, m//2+1):
#             if m % j == 0:
#                 sum2 += j
#         if sum2 == n and m > n:
#             print(n, m)