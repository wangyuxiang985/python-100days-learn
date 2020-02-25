"""
requests库
通过requests来实现一个访问网络数据接口并从中获取美女图片下载链接然后下载美女图片到本地的例子程序
"""
from threading import Thread
import requests

# 继承Thread类创建自定义的线程类
class DownloadHandler(Thread):

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('E:\\alibabawb\\tmp\\' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/?key=24e962ba9fc2a33fec29500c2125378d&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm in data_model['newslist']:
        url = mm['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHandler(url).start()

if __name__ == '__main__':
    main()
    