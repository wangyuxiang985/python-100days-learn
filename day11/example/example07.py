"""
JSON
json模块主要有四个比较重要的函数，分别是：

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，
这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，
可以利用这些字节来产生原始对象的副本（拷贝）。
与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）”。

使用requests模块（封装得足够好的第三方网络访问模块）访问网络API获取国内新闻，
如何通过json模块解析JSON数据并显示新闻标题
"""
import requests
import json
def main():

    response = requests.get('http://api.tianapi.com/guonei/?key=24e962ba9fc2a33fec29500c2125378d&num=10')
    print(response.text)
    json_loads = json.loads(response.text)
    print(json_loads)
    for news in json_loads['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()