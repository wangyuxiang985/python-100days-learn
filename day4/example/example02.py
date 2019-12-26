"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，
这一点在使用嵌套的循环结构需要引起注意。除了break之外，
还有另一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
"""
from random import randint
answer = randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入1~100的整数：'))
    if number > answer:
        print('大了')
    elif number < answer:
        print('小了')
    else:
        print('猜对了')
        break
print('总共猜了%d次' % counter)
if counter >= 7:
    print('太蠢了')
