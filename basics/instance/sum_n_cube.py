"""
计算n个自然数的立方和
计算公式 13 + 23 + 33 + 43 + …….+ n3

实现要求：
输入 : n = 5
输出 : 225
公式 : 13 + 23 + 33 + 43 + 53 = 225
"""

# 立方公式
test = 2 ** 3
print(test)


def sum_n_cube():
    num = int(input("输入自然数。"))
    sum_list = [i ** 3 for i in range(1, num + 1)]
    print(sum(sum_list))


def answer(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum


if __name__ == '__main__':
    sum_n_cube()
    print(answer(3))
