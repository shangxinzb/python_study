"""
文档快速生成注释的方法介绍,首先我们要用到__all__属性
在Py中使用为导出__all__中的所有类、函数、变量成员等
在模块使用__all__属性可避免相互引用时命名冲突
"""
__all__ = ['Login', 'check', 'Shop', 'upDateIt', 'findIt', 'deleteIt', 'createIt']


class Login:
    """
    原文链接：https://www.cnblogs.com/cookie1026/p/6093188.html
    一个方法内只能有一个\"\"\"注释
    '#'注释不能被help方法解析
    测试注释一可以写上此类的作用说明等
    例如此方法用来写登录
    """

    def __init__(self):
        """
        初始化你要的参数说明
        那么登录可能要用到
        用户名username
        密码password
        """
        a = 10

    # 方法外注释
    def check(self):
        # 方法内#注释
        """
        协商你要实现的功能说明
        功能也有很多例如验证
        判断语句，验证码之类的
        test
        """
        """
        第二个注释
        这个注释不能被展示出来
        """
        pass


class Shop:
    """
    商品类所包含的属性及方法
    update改/更新
    find查找
    delete删除
    create添加
    """

    def __init__(self):
        """
        初始化商品的价格、日期、分类等
        """
        pass

    def upDateIt(self):
        """
        用来更新商品信息
        """
        pass

    def findIt(self):
        """
        查找商品信息
        """
        pass

    def deleteIt(self):
        """
        删除过期下架商品信息
        """
        pass

    def createIt(self):
        """
        创建新商品及上架信息
        """
        pass





