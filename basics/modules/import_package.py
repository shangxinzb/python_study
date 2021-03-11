"""
引用包文件
"""

if __name__ == "__main__":
    # 包名.模块名
    import demo_package.demo

    for name in dir(demo_package.demo.Who):
        print(name)

    # 引入指定类名
    from demo_package.demo import Who
    for name in dir(demo_package.demo.Who):
        print(name)

    from demo_package.demo import You as you
    for name in dir(you):
        print(name)

    # 引用的包，最后一个必须是包或者模块，是一个类
    # from demo_package.demo.You import head

    print(you.body(self=""))
    # print(echo())


