"""
生成器 - 数据的生产者。
生成器还可以叠加来组成生成器管道，
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，
但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
"""

from time import sleep

# 倒计数生成器 生成器
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 叠加生成器来组成生成器管道
# Fibonacci数生成器
def fib():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a

# 偶数生成器
def even(gen):
    for var in gen:
        if var % 2 == 0:
            yield var

def main():
    # for num in countdown(5):
    #     print(f'Countdown: {num}')
    #     sleep(1)
    gen = even(fib())
    print(gen)
    for _ in range(10):
        print(next(gen))


if __name__ == '__main__':
    main()