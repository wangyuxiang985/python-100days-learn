"""
1.下载数据 - urllib / requests / aiohttp。
2.解析数据 - re / lxml / beautifulsoup4（bs4）/ pyquery。
3.缓存和持久化 - pymysql / sqlalchemy / peewee/ redis / pymongo。
4.生成数字签名 - hashlib。
5.序列化和压缩 - pickle / json / zlib。
6.调度器 - 进程（multiprocessing） / 线程（threading） / 协程（coroutine）。

四种采集方式
抓取方法	    速度	    使用难度	    备注
正则表达式	快	          困难	  常用正则表达式/在线正则表达式测试
lxml	    快	          一般	  需要安装C语言依赖库/唯一支持XML的解析器
Beautiful 较快/较慢（取决于解析器）	简单	
PyQuery	    较快	        简单	Python版的jQuery
---
Beautiful的解析器包括：Python标准库（html.parser）、lxml的HTML解析器、lxml的XML解析器和html5lib。

缓存知乎发现上的链接和页面代码
"""
import pickle
import zlib
from hashlib import sha1
from http import client
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import re


def main():
    # 指定种子页面
    base_url = 'https://www.zhihu.com/'
    send_url = urljoin(base_url, 'explore')
    print(send_url)
    # 设置用户代理（否则访问被拒绝）
    headers = {'user-agent': 'Baiduspider'}
    # 通过requests模块发送GET请求并指定用户代理
    response = requests.get(send_url, headers=headers)
    # print(response.text)
    # 创建BeautifulSoup对象并指定使用lxml作为解析器 conda install lxml
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    href_regex = re.compile(r'^/question')
    # print(href_regex)
    # 将URL处理成SHA1摘要(长度固定更简短)
    hasher_proto = sha1()
    # print(hasher_proto)
    # 查找所有href属性以/question打头的a标签

    for a_tag in soup.find_all('a', {'href': href_regex}):
        # 获取a标签的href属性值并组装完整的URL
        href = a_tag.attrs['href']
        full_url = urljoin(base_url, href)
        # 传入URL生成SHA1摘要
        hasher = hasher_proto.copy()
        hasher.update(full_url.encode('utf-8'))
        field_key = hasher.hexdigest()
        # 如果Redis的键'zhihu'对应的hash数据类型中没有URL的摘要就访问页面并缓存
        if not client.hexists('zhihu', field_key):
            html_page = requests.get(full_url, headers=headers).text
            # 对页面进行序列化和压缩操作
            zipped_page = zlib.compress(pickle.dumps(html_page))
            # 使用hash数据类型保存URL摘要及其对应的页面代码
            # client.hset('zhihu', field_key, zipped_page)
    # 显示总共缓存了多少个页面
    # print('Total %d question pages found.' % client.hlen('zhihu'))



if __name__ == '__main__':
    main()
