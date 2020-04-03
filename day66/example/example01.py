"""
网络爬虫和相关工具
一个简单的爬虫
一个基本的爬虫通常分为数据采集（网页下载）、数据处理（网页解析）和数据存储（将有用的信息持久化）三个部分的内容，
当然更为高级的爬虫在数据采集和处理时会使用并发编程或分布式技术，这就需要有调度器（安排线程或进程执行对应的任务）、
后台管理程序（监控爬虫的工作状态以及检查数据抓取的结果）等的参与。
爬虫的工作流程包括以下几个步骤：
1.设定抓取目标（种子页面/起始页面）并获取网页。
2.当服务器无法访问时，按照指定的重试次数尝试重新下载页面。
3.在需要的时候设置用户代理或隐藏真实IP，否则可能无法访问页面。
4.对获取的页面进行必要的解码操作然后抓取出需要的信息。
5.在获取的页面中通过某种方式（如正则表达式）抽取出页面中的链接信息。
6.对链接进行进一步的处理（获取页面并重复上面的动作）。
7.将有用的信息进行持久化以备后续的处理。

一个从“搜狐体育”上获取NBA新闻标题和链接的爬虫
"""

from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl

from pymysql import Error


# 通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)
def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


# 获取页面的HTML代码(通过递归实现指定次数的重试操作)
def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


# 从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)
def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


# 开始执行爬虫程序并对指定的数据进行持久化操作
def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    conn = pymysql.connect(host='localhost', port=3306,
                           database='crawler', user='root',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            # 通过下面的字典避免重复抓取并控制抓取深度
            visited_url_list = {seed_url: 0}
            while url_list:
                current_url = url_list.pop(0)
                depth = visited_url_list[current_url]
                if depth != max_depth:
                    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    links_list = get_matched_parts(page_html, match_pattern)
                    param_list = []
                    for link in links_list:
                        if link not in visited_url_list:
                            visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_matched_parts(page_html, r'<h1>(.*)<span')
                            if headings:
                                param_list.append((headings[0], link))
                    cursor.executemany('insert into tb_result values (default, %s, %s)',
                                       param_list)
                    conn.commit()
    except Error:
        pass
        # logging.error('SQL:', error)
    finally:
        conn.close()


def main():
    # 设置全局的取消证书验证
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('https://sports.sohu.com/s/nba',
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth=2)


if __name__ == '__main__':
    main()