"""
Python中的多进程

Unix和Linux操作系统上提供了fork()系统调用来创建进程，调用fork()函数的是父进程，
创建出的是子进程，子进程是父进程的一个拷贝，但是子进程拥有自己的PID。
fork()函数非常特殊它会返回两次，父进程中可以通过fork()函数的返回值得到子进程的PID，
而子进程中的返回值永远都是0。Python的os模块提供了fork()函数。
由于Windows系统没有fork()调用，因此要实现跨平台的多进程编程，
可以使用multiprocessing模块的Process类来创建子进程，
而且该模块还提供了更高级的封装，
例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等
"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    # download_task('Python从入门到住院.pdf')
    # download_task('Peking Hot.avi')
    # 使用多进程的方式将两个下载任务放到不同的进程中
    """
    通过Process类创建了进程对象，
    通过target参数我们传入一个函数来表示进程启动后要执行的代码，
    后面的args是一个元组，它代表了传递给函数的参数。
    Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
    """
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    # 阻塞主线程
    p1.join()
    p2.join()

    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()