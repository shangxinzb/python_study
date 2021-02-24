class Who:
    """
    包引用demo文件
    """

    def echo_self(self, str_self):
        """
        返回传过来的字符串
        :return: string
        """
        return str_self

    def hello(self):
        """
        一个返回hello的方法
        :return: string
        """
        return "hello"


class You:
    """
    你自己的一些属性
    """


    def hair(self):
        """
        头发的属性
        :return: dict
        """
        return {
            'color': 'black',
            'length': '10cm',
        }

    def body(self):
        """
        身体的属性
        :return: dict
        """
        return {
            'weight': '75KG',
            'height': '172cm'
        }

    def foot(self):
        """
        脚的属性
        :return: dict
        """
        return {
            'size': 42
        }