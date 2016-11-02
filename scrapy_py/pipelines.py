# -*- coding: utf-8 -*-

# 当数据抓取后,对数据进行一些处理,通常会有以下操作:
# 清理HTML数据
# 验证爬取的数据(检查item包含某些字段)
# 查重(并丢弃)
# 将爬取结果保存到数据库中
# http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/item-pipeline.html

# 为了启用一个Item Pipeline组件，你必须将它的类添加到在settings.py中添加 ITEM_PIPELINES 配置
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
# mongo依赖
from pymongo import MongoClient

# settings获取
from scrapy.conf import settings
# 丢弃不合法的数据,一旦丢弃爬虫将不再处理
from scrapy.exceptions import DropItem
# log 依赖
from scrapy import log

# TODO: mongo存储
class MongoPipeline(object):
    def __init__(self):
        #建立mongoDB数据库连接
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item

# json存储
class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('nodejs.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))

        return item
    pass








