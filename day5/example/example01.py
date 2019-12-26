from random import randint
def roll_dice(n=2):
    """
    摇色子
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a=1, b=2, c=3):
    """
    求和
    """
    return a + b + c

# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(roll_dice(-1))

print(add())
print(add(1))
print(add(1, 3))
print(add(1, 3, 4))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
print(add(c=10))