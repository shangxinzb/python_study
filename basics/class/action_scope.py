"""
作用域
L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等。，最后被搜索
规则顺序： L –> E –> G –>gt; B。
"""


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    # 局部作用域，只在方法体内有效（局部变量）
    do_local()  # test spam
    print(spam)
    # 非局部作用域
    do_nonlocal()  # nonlocal spam
    print(spam)
    # 虽然声明了全局作用域global，但是搜索顺序是非全局->全局，所以这里是nonlocal spam
    do_global()  # nonlocal spam
    print(spam)


scope_test()
# 全局作用域 global spam的值
print("in global scope:", spam)
