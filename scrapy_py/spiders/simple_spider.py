# -*- coding: utf-8 -*-

# 单一网址的爬虫

import scrapy

from scrapy.http import Request
from scrapy.selector import Selector

from scrapy_py.items import SimpleItems

class SimpleScrapy(scrapy.Spider):
    # 爬虫名称,必须
    name = 'SimpleScrapy'
    # 减慢爬取速度 为1s
    #download_delay参数设置为1，将下载器下载下一个页面前的等待时间设置为1s，也是防止被ban的策略之一。主要是减轻服务器端负载。
    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        # 第一篇文章地址
        "http://blog.csdn.net/u012150179/article/details/11749017"
    ]

    def parse(self, response):
        sel = Selector(response)
        # 获得文章url和标题
        item = SimpleItems()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        item['article_name'] = [n.encode('utf-8') for n in article_name]
        item['article_url'] = article_url.encode('utf-8')

        yield item

        urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()
        for url in urls:
            #print 调试作用
            print url
            url = "http://blog.csdn.net" + url
            print url
            # 也就是将新获取的request返回给引擎，实现继续循环。也就实现了“自动下一网页的爬取”。
            yield Request(url, callback=self.parse)
