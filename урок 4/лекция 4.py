# def summa_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)

# summa_numbers(5)   


# def summa_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(summa_numbers(5))


# def summa_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# a = summa_numbers(5)   
# print(summa_numbers(5))  



# def sum_str(*miya):
#     res = ' '
#     for i in miya:
#         res += i
#     return res

# print(sum_str('m', 'i', 'y', 'a'))



# import modul1
# print(modul1.f(1))

# from modul1 import f
# print(f(2.3))

# from modul1 import *
# print(f(1))

# import modul1
# print(modul1.f(1))

# import modul1 as m1
# print(m1.f(2.3))


# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n - 1) + fib(n -2)

# list = []
# for i in range(1,10):
#     list.append(fib(i))
# print(list)



# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1: ] if i <= pivot]
#         greater = [i for i in array[1: ] if i > pivot]
#         return quick_sort(less) +[pivot] + quick_sort(greater)
# print(quick_sort([10, 5, 2]))


# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#             while i < len(left):
#                 nums[k] = left[i]
#                 i += 1
#                 k += 1
            
#             while j < len(right):
#                 nums[k] = right[j]
#                 j += 1
#                 k += 1

# list = [1,2,3,4,5]
# merge_sort(list)
# print(list)

            

