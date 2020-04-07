"""
用面向对象的方式实现一个爬取“手机搜狐网”的多线程爬虫。
python用redis (conda install redis + conda install redis-py)
"""
from _sha1 import sha1
from enum import unique, Enum
from random import random
from threading import current_thread, local, Thread
from time import sleep
from urllib.parse import urlparse

import redis
import requests
from bs4 import BeautifulSoup


@unique
class SpiderStatus(Enum):
    IDLE = 0
    WORKING = 1

#重试
class Retry(object):

    def __init__(self, *, retry_times=3,
                 wait_secs=5, errors=(Exception, )):
        self.retry_times = retry_times
        self.wait_secs = wait_secs
        self.errors = errors

    def __call__(self, fn):

        def wrapper(*args, **kwargs):
            for _ in range(self.retry_times):
                try:
                    return fn(*args, **kwargs)
                except self.errors as e:
                    print(e)
                    sleep((random() + 1) * self.wait_secs)
            return None

        return wrapper
# 解码页面
def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
    return page_html

class Spider(object):
    # 初始化spider状态为空闲
    def __init__(self):
        self.status = SpiderStatus.IDLE

    @Retry()
    def fetch(self, current_url, *, charsets=('utf-8',),
              user_agent=None, proxies=None):
        thread_name = current_thread().name
        print(f'[{thread_name}]: {current_url}')
        headers = {'user-agent': user_agent} if user_agent else {}
        resp = requests.get(current_url,
                            headers=headers, proxies=proxies)
        return decode_page(resp.content, charsets) \
            if resp.status_code == 200 else None

    def parse(self, html_page, *, domain='m.sohu.com'):
        soup = BeautifulSoup(html_page, 'lxml')
        for a_tag in soup.body.select('a[href]'):
            parser = urlparse(a_tag.attrs['href'])
            scheme = parser.scheme or 'http'
            netloc = parser.netloc or domain
            if scheme != 'javascript' and netloc == domain:
                path = parser.path
                query = '?' + parser.query if parser.query else ''
                full_url = f'{scheme}://{netloc}{path}{query}'
                redis_client = thread_local.redis_client
                if not redis_client.sismember('visited_urls', full_url):
                    redis_client.rpush('m_sohu_task', full_url)

    def extract(self, html_page):
        pass

    def store(self, data_dict):
        # redis_client = thread_local.redis_client
        # mongo_db = thread_local.mongo_db
        pass

#爬虫线程
class SpiderThread(Thread):

    def __init__(self, name, spider):
        super().__init__(name=name, daemon=True)
        self.spider = spider

    def run(self):
        redis_client = redis.Redis()
        # mongo数据库
        # mongo_client = pymongo.MongoClient(host='1.2.3.4', port=27017)
        # thread_local.mongo_db = mongo_client.msohu
        thread_local.redis_client = redis_client
        while True:
            current_url = redis_client.lpop('m_sohu_task')
            while not current_url:
                current_url = redis_client.lpop('m_sohu_task')
            self.spider.status = SpiderStatus.WORKING
            current_url = current_url.decode('utf-8')
            if not redis_client.sismember('visited_urls', current_url):
                redis_client.sadd('visited_urls', current_url)
                html_page = self.spider.fetch(current_url)
                if html_page not in [None, '']:
                    hasher = hasher_proto.copy()
                    hasher.update(current_url.encode('utf-8'))
                    # 存入mongo数据库
                    doc_id = hasher.hexdigest()
                    # sohu_data_coll = mongo_client.msohu.webpages
                    # if not sohu_data_coll.find_one({'_id': doc_id}):
                    #     sohu_data_coll.insert_one({
                    #         '_id': doc_id,
                    #         'url': current_url,
                    #         'page': Binary(zlib.compress(pickle.dumps(html_page)))
                    #     })
                    self.spider.parse(html_page)
            self.spider.status = SpiderStatus.IDLE

# 判断爬虫线程是否空闲
def is_any_alive(spider_threads):
    return any([spider_thread.spider.status == SpiderStatus.WORKING
                for spider_thread in spider_threads])

thread_local = local()
hasher_proto = sha1()

def main():
    print('爬取手机搜狐网')
    # 创建redis链接 默认：localhost:6379 0库密码
    redis_client = redis.Redis()
    # redis中m_sohu_task key不存在则放入'm_sohu_task', 'http://m.sohu.com/'
    if not redis_client.exists('m_sohu_task'):
        redis_client.rpush('m_sohu_task', 'http://m.sohu.com/')
    print(redis_client.exists('m_sohu_task'))
    # 创建爬虫线程池 利用面向对象的方式实现，需要将爬虫类Spider传入，因此需要先实现Spider类
    # spider_threads = [SpiderThread('thread-%d' % i, Spider())
    #                   for i in range(10)]
    # 开启线程
    # for spider_thread in spider_threads:
    #     spider_thread.start()
    # 一个主线程执行
    SpiderThread('thread-%d' % 1, Spider()).run()
    # 判断是否终止程序，条件：redis中是否还存在m_sohu_task key键，以及是否还有存活线程
    # while redis_client.exists('m_sohu_task') or is_any_alive(spider_threads):
    #     sleep(5)

    print("over!")


if __name__ == '__main__':
    main()
