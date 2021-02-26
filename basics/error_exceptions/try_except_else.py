"""
try...except...else
else只能出现在except子句之后
"""
import sys

# print(sys.argv)
for arg in sys.argv[:]:
    print(arg)
    try:
        f = open(arg, 'r', encoding='utf-8')
    except IOError:
        # print('cannot open', arg)
        print('IOError')
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        print('echo else')
        f.close()