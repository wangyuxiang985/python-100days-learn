"""
实现计算求最大公约数和最小公倍数的函数
"""
def gcd(x, y):
    if x > y:
        x, y = y, x
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i
def gic(x, y):
    return x * y // gcd(x, y)

print(gcd(6, 9))
print(gic(9, 6))


