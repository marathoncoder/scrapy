# -*- coding: utf-8 -*-

# 单一网址的爬虫

import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, FormRequest

from scrapy.http import Request
from scrapy.selector import Selector

from scrapy_py.items import SimpleItems
from scrapy_py.items import ZhihuItem



class SimpleScrapy(scrapy.Spider):
    # 爬虫名称,必须
    # name = 'SimpleScrapy'
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

class MockLoginSpider(CrawlSpider):
    name = 'MockLoginSpider'
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        "http://www.zhihu.com"
    ]
    rules = (
        Rule(LinkExtractor(allow=('/question/\d+#.*?',)), callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=('/question/\d+',)), callback='parse_page', follow=True)
    )
    # 模拟头部
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Referer": "https://www.zhihu.com/"
    }

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("https://www.zhihu.com/login/phone_num", meta={'cookiejar': 1}, callback=self.post_login)]

    # FormRequeset出问题了
    def post_login(self, response):
        print 'Preparing login'
        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print xsrf
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,  # "http://www.zhihu.com/login",
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.headers,  # 注意此处的headers
                                          formdata={
                                              '_xsrf': xsrf,
                                              'email': '1095511864@qq.com',
                                              'password': '123456'
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        print item['name']
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer'] = problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        return item
