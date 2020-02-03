"""
使用subprocess模块中的类和函数来创建和启动子进程，然后通过管道来和子进程通信

启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个。
"""

from multiprocessing import Process, Queue
from time import sleep


def sub_task(string, q):
    while q.qsize() <= 10:
        print(string, end='', flush=True)
        q.put(1)
        sleep(0.01)


def main():
    q = Queue(10)
    Process(target=sub_task, args=('Ping', q,)).start()
    Process(target=sub_task, args=('Pong', q,)).start()


if __name__ == '__main__':
    main()