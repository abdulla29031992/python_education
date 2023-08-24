lst = []
n = int(input("N> "))
for i in range(n):
    lst.append(int(input(f"{i+1}: ")))
x = int(input("X> "))
print("Count X>",lst.count(x))

# count=0 вариант подсчета перебором
# for i in lst:
#     if i==x:
#         count+=1
# print(count)