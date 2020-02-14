"""
网络编程 网络协议的三要素是：语法、语义和时序
TCP/IP模型
TCP/IP是一个四层模型，也就是说，该模型将我们使用的网络从逻辑上分解为四个层次，
自底向上依次是：网络接口层、网络层、传输层和应用层
TCP全称传输控制协议，它是基于IP提供的寻址和路由服务而建立起来的负责实现端到端可靠传输的协议，
之所以将TCP称为可靠的传输协议是因为TCP向调用者承诺了三件事情：
1、数据不传丢不传错（利用握手、校验和重传机制可以实现）。
2、流量控制（通过滑动窗口匹配数据发送者和接收者之间的传输速度）。
3、拥塞控制（通过RTT时间以及对滑动窗口的控制缓解网络拥堵）。

网络应用模式
1、C/S模式和B/S模式。这里的C指的是Client（客户端），
通常是一个需要安装到某个宿主操作系统上的应用程序；而B指的是Browser（浏览器），
它几乎是所有图形化操作系统都默认安装了的一个应用软件；通过C或B都可以实现对S（服务器）的访问。
2、去中心化的网络应用模式。不管是B/S还是C/S都需要服务器的存在，
服务器就是整个应用模式的中心，而去中心化的网络应用通常没有固定的服务器或者固定的客户端，
所有应用的使用者既可以作为资源的提供者也可以作为资源的访问者。

requests库
Requests是唯一的一个非转基因的Python HTTP库，
使用requests库可以非常方便的使用HTTP，避免安全缺陷、冗余代码以及“重复发明轮子”

套接字可以分为三类：流套接字（TCP套接字）、数据报套接字和原始套接字。
TCP套接字：
TCP套接字就是使用TCP协议提供的传输服务来实现网络通信的编程接口，
Python中可以通过创建socket对象并指定type属性为SOCK_STREAM来使用TCP套接字。

一个提供时间日期的服务器
"""
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(AF_INET, SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('30.25.209.172', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()


if __name__ == '__main__':
    main()
