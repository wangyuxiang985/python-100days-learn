"""
输入两个正整数计算最大公约数和最小公倍数
"""
x = int(input('请输入一个正整数：'))
y = int(input('请输入另一个正整数：'))
if x > y:
    print(x, y)
    x, y = y, x
    print(x, y)
for n in range(x, 0, -1):
    if x % n == 0 and y % n == 0:
        print('%d和%d的最大公约数是%d' % (x, y, n))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // n))
        break