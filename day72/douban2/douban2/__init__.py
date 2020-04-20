"""
scrapy startproject douban2 //创建一个douban2工程
scrapy crawl <spider> //执行爬虫
scrapy crawl <spider> -o result.json //将爬虫结果储存在result.json文件中
注意，是<spider>而不是runspider命令的<spider_file.py>，准确的说<spider>是一个 爬虫程序的名称——爬虫类里面的name属性（必须required，且在项目中具有唯一性unique）

1.在items.py文件中定义字段，这些字段用来保存数据
2.在spiders文件夹中编写自己的爬虫。
3.在pipelines.py中完成对数据进行持久化的操作。
    利用Pipeline我们可以完成以下操作：
        清理HTML数据，验证爬取的数据。
        丢弃重复的不必要的内容。
        将爬取的结果进行持久化操作。
4.修改settings.py文件对项目进行配置。
"""