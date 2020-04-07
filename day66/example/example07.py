"""
解析动态内容
使用Selenium
自动化测试工具Selenium，它提供了浏览器自动化的API接口，这样就可以通过操控浏览器来获取动态内容
首先安装selenium，conda install selenium
以“阿里V任务”的“直播服务”为例，来演示如何使用Selenium获取到动态内容并抓取主播图片
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 运行下面的程序会发现没有任何的输出，因为页面的HTML代码上根本找不到<img>标签
def before():

    resp = requests.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup)
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src'])

# 使用Selenium来获取到页面上的动态内容，再提取主播图片
def after():
    # 要么加入PATH环境变量，要么指定到可执行驱动的名字，因为application文件权限问题
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for img_tag in soup.body.select('img[src]'):
        print(img_tag.attrs['src'])


def main():
    # 之前的
    # before()
    # 使用Selenium来获取到页面上的动态内容，再提取主播图片
    after()

if __name__ == '__main__':
    main()
