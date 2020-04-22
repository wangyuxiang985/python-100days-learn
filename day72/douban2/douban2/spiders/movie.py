# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# from day72.douban2.douban2.items import Douban2Item

"""
我们通过Scrapy提供的爬虫模板创建了Spider，其中的rules中的LinkExtractor对象会自动完成对新的链接的解析，
该对象中有一个名为extract_link的回调方法。Scrapy支持用XPath语法和CSS选择器进行数据解析，
对应的方法分别是xpath和css，上面我们使用了XPath语法对页面进行解析

在Scrapy框架中，我们自定义的蜘蛛都继承自scrapy.spiders.Spider，这个类有一系列的属性和方法，具体如下所示：
name：爬虫的名字。
allowed_domains：允许爬取的域名，不在此范围的链接不会被跟进爬取。
start_urls：起始URL列表，当我们没有重写start_requests()方法时，就会从这个列表开始爬取。
custom_settings：用来存放蜘蛛专属配置的字典，这里的设置会覆盖全局的设置。
crawler：由from_crawler()方法设置的和蜘蛛对应的Crawler对象，Crawler对象包含了很多项目组件，利用它我们可以获取项目的配置信息，如调用crawler.settings.get()方法。
settings：用来获取爬虫全局设置的变量。
start_requests()：此方法用于生成初始请求，它返回一个可迭代对象。该方法默认是使用GET请求访问起始URL，如果起始URL需要使用POST请求来访问就必须重写这个方法。
parse()：当Response没有指定回调函数时，该方法就会被调用，它负责处理Response对象并返回结果，从中提取出需要的数据和后续的请求，该方法需要返回类型为Request或Item的可迭代对象（生成器当前也包含在其中，因此根据实际需要可以用return或yield来产生返回值）。
closed()：当蜘蛛关闭时，该方法会被调用，通常用来做一些释放资源的善后操作。
"""

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Referer': 'https://movie.douban.com/top250',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        }
    }
    rules = (
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'https://movie.douban.com/subject/\d+')), callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        item = Douban2Item()
        item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year'] = sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['score'] = sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        item['director'] = sel.xpath('//*[@id="info"]/span[1]/a/text()').extract()
        item['classification'] = sel.xpath('//span[@property="v:genre"]/text()').extract()
        item['actor'] = sel.xpath('//*[@id="info"]/span[3]/a[1]/text()').extract()
        return item

class Douban2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    score = scrapy.Field()
    director = scrapy.Field()
    classification = scrapy.Field()
    actor = scrapy.Field()