"""
并发下载
threading.local类
使用线程时最不愿意遇到的情况就是多个线程竞争资源，在这种情况下为了保证资源状态的正确性，我们可能需要对资源进行加锁保护的处理，
这一方面会导致程序失去并发性，另外如果多个线程竞争多个资源时，还有可能因为加锁方式的不当导致死锁。要解决多个线程竞争资源的问题，
其中一个方案就是让每个线程都持有资源的副本（拷贝），这样每个线程可以操作自己所持有的资源，从而规避对资源的竞争。

要实现将资源和持有资源的线程进行绑定的操作，最简单的做法就是使用threading模块的local类，
在网络爬虫开发中，就可以使用local类为每个线程绑定一个MySQL数据库连接或Redis客户端对象，这样通过线程可以直接获得这些资源，
既解决了资源竞争的问题，又避免了在函数和方法调用时传递这些资源。
------
concurrent.futures模块
python3.2带来了concurrent.futures 模块，这个模块包含了线程池和进程池、管理并行编程任务、处理非确定性的执行流程、进程/线程同步等功能。
-----
分布式进程
使用多进程的时候，可以将进程部署在多个主机节点上，Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程部署到多个节点上。
当然，要部署分布式进程，首先需要一个服务进程作为调度者，进程之间通过网络进行通信来实现对进程的控制和调度
=============
协程和异步I/O
协程（coroutine）通常又称之为微线程或纤程，它是相互协作的一组子程序（函数）。所谓相互协作指的是在执行函数A时，可以随时中断去执行函数B，
然后又中断继续执行函数A。注意，这一过程并不是函数调用（因为没有调用语句），整个过程看似像多线程，然而协程只有一个线程执行。
协程通过yield关键字和 send()操作来转移执行权，协程之间不是调用者与被调用者的关系。
协程的优势在于以下两点：
1.执行效率极高，因为子程序（函数）切换不是线程切换，由程序自身控制，没有切换线程的开销。
2.不需要多线程的锁机制，因为只有一个线程，也不存在竞争资源的问题，当然也就不需要对资源加锁保护，因此执行效率高很多。
PS:协程适合处理的是I/O密集型任务，处理CPU密集型任务并不是它的长处，如果要提升CPU的利用率可以考虑“多进程+协程”的模式。
"""