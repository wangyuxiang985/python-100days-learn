"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
from math import sqrt
a = float(input("请输入a边长："))
b = float(input("请输入b边长："))
c = float(input("请输入c边长："))
if a + b > c and a + c > b and b + c > a:
    l = a + b + c
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    print('周长：%f' % l)
    print('面积：%f' % area)
else:
    print('%f和%f和%f三边构不成三角形' % (a, b, c))