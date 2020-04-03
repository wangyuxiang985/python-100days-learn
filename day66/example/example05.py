"""
协程 - 数据的消费者。
"""

# 生成器 - 数据生产者
from time import sleep


def countdown_gen(n, consumer):
    # 在一个生成器对象没有执行next方法之前，由于没有yield语句被挂起，所以执行send方法会报错。 当send方法的参数为None时，它与next方法完全等价。
    #在调用send()方法时，要么先调用一次next()到函数挂起的位置，或者直接send(None)。
    consumer.send(None)
    while n > 0:
        consumer.send(n)
        n -= 1
    consumer.send(None)

# 协程 - 数据消费者
def countdown_con():
    while True:
        n = yield
        if n:
            print(f'Countdown {n}')
            sleep(1)
        else:
            print('Countdown Over!')

def main():
    countdown_gen(5, countdown_con())


if __name__ == '__main__':
    main()