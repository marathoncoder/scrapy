# -*- coding: utf-8 -*-

# 定义需要抓取的数据

from scrapy.item import Item, Field

class SimpleItems(Item):
    article_name = Field()
    article_url = Field()

class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()  # 保存抓取问题的url
    title = Field()  # 抓取问题的标题
    description = Field()  # 抓取问题的描述
    answer = Field()  # 抓取问题的答案
    name = Field()  # 个人用户的名称
