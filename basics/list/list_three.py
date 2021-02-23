"""
嵌套的列表推导式
将3*4的矩阵换成4*3的矩阵
"""

# 矩阵 matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 正常的逻辑操作
transposed = []
for i in range(4):
    line = []
    for row in matrix:
        line.append(row[i])
    transposed.append(line)

# 嵌套列表推导式有效
transposed = [[row[i] for row in matrix] for i in range(4)]
transposed = []
# 返回的是一个[<object>,...]
for i in range(4):
    transposed.append(row[i] for row in matrix)

# 内置函数处理数组
# transposed = basics(zip(*matrix))
transposed = list(transposed)
print(transposed)


# del 删除
wait_list = [1, 2, 3, 4, 5, 6, 7]
del wait_list[0]


print(wait_list)


# 字符串后面加上逗号，会被解析成元组 tuple
singleton = 'dada',

print(len(singleton))
print(singleton)