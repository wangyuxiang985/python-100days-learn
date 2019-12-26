"""
输入半径计算圆的周长和面积
"""
import math

r = float(input("请输入圆的半径："))
l = 2 * math.pi * r
s = math.pi * r * r
print('周长：%.2f' % l)
print('%f 半径的圆面积为：%.2f' % (r, s))