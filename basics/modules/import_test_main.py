"""
引入test_main模块。测试__name__属性
"""

import test_mian

if __name__ == '__main__':
    print("import_test_main file")
else:
    print('other')
