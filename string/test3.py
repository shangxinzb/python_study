def reverseWords(input):
    # 字符串分隔
    inputWords = input.split(" ")

    # 字符串翻转
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

print(__name__)
# print (__dict__)
print(__doc__)
print(__file__)
print(__package__)
# print (__path__)

tup = ()

tup1 = (20, 21)

print(tup)
print(tup1)

param = {21.1, 'fdfsd', True}

print(param)

b = set("dfs")
print(b)
