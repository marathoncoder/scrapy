# -*- coding: utf-8 -*-

# 定义需要抓取的数据

from scrapy.item import Item, Field

class SimpleItems(Item):
    article_name = Field()
    article_url = Field()
