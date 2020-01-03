"""
通过yield关键字将一个普通函数改造成生成器函数
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        print('********', a)
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()