"""
单线程+异步I/O
如果充分利用操作系统提供的异步I/O支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型。

在Python语言中，单线程+异步I/O的编程模型称为协程，有了协程的支持，
就可以基于事件驱动编写高效的多任务程序。
协程最大的优势就是极高的执行效率，因为子程序切换不是线程切换，而是由程序自身控制，
因此，没有线程切换的开销。协程的第二个优势就是不需要多线程的锁机制，
因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不用加锁，
只需要判断状态就好了，所以执行效率比多线程高很多。
如果想要充分利用CPU的多核特性，最简单的方法是多进程+协程，既充分利用多核，
又充分发挥协程的高效率，可获得极高的性能。

将耗时间的任务放到线程中以获得更好的用户体验。
如下所示的界面中，有“下载”和“关于”两个按钮，
用休眠的方式模拟点击“下载”按钮会联网下载文件需要耗费10秒的时间，
如果不使用“多线程”，我们会发现，
当点击“下载”按钮后整个程序的其他部分都被这个耗时间的任务阻塞而无法执行了，
这显然是非常糟糕的用户体验，代码如下所示。
"""
import time
import tkinter
import tkinter.messagebox


def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')


def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 王二狗(v1.0)')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()