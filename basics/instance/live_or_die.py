"""
约瑟夫生死者
描述：
30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
"""

# 创建一个人类集合
people = {}
# 有30个人，每人都有一个编号，赋值1代表在船上
for x in range(1, 31):
    people[x] = 1

# print(people)
# 报数
check = 0
# 编号
serial_number = 1
# 下船人数
down_ship = 0

while serial_number <= 31:
    if serial_number == 31:
        # 到31，说明要从头开始了
        serial_number = 1
    elif down_ship == 15:
        # 输出还在船上人的编号
        # join只能将字符串序列转换成新的字符串，数字是不行的！
        lived_people = [str(serial_num) for serial_num, life in people.items() if life == 1]
        print("还在船上的编号有：", "、".join(list(lived_people)))
        # 15个人下船后，游戏结束
        break
    else:
        # 等于0时说明下船了
        if people[serial_number] == 0:
            # 编号+1，下一位
            serial_number += 1
            continue
        else:
            # 报数+1
            check += 1
            # 报数到9时
            if check == 9:
                # 当前编号人下船
                people[serial_number] = 0
                # 报数重新开始计算
                check = 0
                print("{}号下船了".format(serial_number))
                # 下船人+1
                down_ship += 1
            else:
                # 编号+1，下一位
                serial_number += 1
                continue


# print("还在船上人的编号", "号，".split(lived_people))

# lived_people = [serial_num for serial_num, life in people.items() if life == 1]
        # print(lived_people)