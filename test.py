# def print_operation_table(operation, n, m):
#     table = []
#     for i in range(1, n + 1):
#         line = []
#         for j in range(1, m + 1):
#             line.append(operation(i,j))
#         table.append(line)

#     for row in table:
#         print(("{: <7}"*m).format(*row))

#     print("Искомый элемент> ", operation(n,m))

# x, y = map(int, input("Введите 2 значения через пробел: ").split())
# print_operation_table(lambda x, y: x * y, x, y)



# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])

# print_operation_table(lambda x, y: x * y)

def print_operation_table(operation, num_rows = 6, num_colums = 6):
    a = [[operation(i, j) for j in range(1, num_colums + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)




