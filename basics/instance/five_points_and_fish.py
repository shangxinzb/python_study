""""
五人分鱼
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
"""


def once():
    fish = 1
    while True:
        total, enough = fish, True
        for people in range(1, 6):
            if (total - 1) % 5 == 0:
                print(total)
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print("fish have {}".format(fish))
            break
        fish += 1


def main():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(f'总共有{fish}条鱼')
            break
        fish += 1


def twice():
    fish = 1
    while True:
        total_fish = fish
        enough = False
        for _ in range(5):
            if total_fish % 5 == 1:
                total_fish = total_fish - ((total_fish - 1) / 5)
                if total_fish % 5 == 1 and total_fish > 1:
                    total_fish = total_fish - ((total_fish - 1) / 5)
                    if total_fish % 5 == 1:
                        total_fish = total_fish - ((total_fish - 1) / 5)
                        if total_fish % 5 == 1:
                            total_fish = total_fish - ((total_fish - 1) / 5)
                            if total_fish % 5 == 1:
                                enough = True
                                break
                            else:
                                print("five")
                                fish += 1
                        else:
                            print("four")
                            fish += 1
                    else:
                        print("three")
                        fish += 1
                else:
                    print("two")
                    fish += 1
            else:
                print("one")
                fish += 1

        if enough:
            print(fish)
            break


def third():
    # 鱼从1条开始算
    fish = 1
    # 无限循环计算
    while True:
        # 赋值一个变量算分鱼的情况
        total_fish = fish
        # 满足鱼的数量判断
        enough = True
        # 五个人分，人不重要，使用_代替
        for _ in range(5):
            # pass
            # 鱼分完5份还剩一条
            if total_fish % 5 == 1:
                # 剩下的鱼总量 = 总量-1 分成5份，然后剩下4份
                total_fish = ((total_fish - 1) / 5) * 4
                # 剩下鱼的总量 = 总量-1 - 5份中的1份
                # total_fish = (total_fish - 1) - ((total_fish - 1) / 5)
            else:
                # 鱼不够分的
                enough = False
                # 结束for循环，进行下一轮计算
                break
        # 鱼够了
        if enough:
            # 有多少鱼
            print(fish)
            # 跳出while循环
            break
        # 鱼加一条
        fish += 1


# def four():
#     # 数据倒推
#     """
#     设 x = 鱼的总数数量
#     y = 每人拿走的鱼的数量
#     假设最后一个人可以平均分5份鱼多一条 x = 5y + 1
#     倒数第二个人拿走鱼的数量为 (x / 4) * 5 + 1
#      以此类推
#
#     :return:
#     """
#     _x = 6
#     enough = True
#     while True:
#         x = _x
#         # print(x)
#         if x % 5 == 1:
#             # 倒数第二人拿走的数量
#             if isinstance(x / 4, int):
#                 # print(x)
#                 x = x / 4 * 5 + 1
#                 # 倒数第三人拿走的数量
#                 if isinstance(x / 4, int):
#                     x = x / 4 * 5 + 1
#                     # 倒数第四人拿走的数量
#                     if isinstance(x / 4, int):
#                         x = x / 4 * 5 + 1
#                         # 倒数第五人拿走的数量
#                         if isinstance(x / 4, int):
#                             x = x / 4 * 5 + 1
#                             x = x * 5 + 1
#                             break
#                     else:
#                         _x += 1
#                 else:
#                     _x += 1
#             else:
#                 _x += 1
#         else:
#             _x += 1
#
#     print(x)



if __name__ == '__main__':
    # once()
    # main()
    # twice()
    third()
#     https://github.com/geekcomputers/Python/issues
