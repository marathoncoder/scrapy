# scrapy
网络爬虫练手项目

url: http://baike.baidu.com/view/3974030.htm

toDo:

+ 深度自动爬取
+ 登录模拟
+ 验证码模拟
+ ajax爬取
+ 多线程处理
+ 分步式处理
+ 暂停、重启
+ 自动限束

+ <del>ban 处理[settings处理]
    - settings处理cookie  如:COOKIES_ENABLED = False
    - download_delay = 1 设置延迟时间
+ <del>网页解析器Xpath运用
    - 可以用开发者工具copy xpath来生成
    - 在开发者工具里面用$x()来测试取到的是不是对的,如$x('//*[@id="post-81320"]/div[3]/h3[5]')
+ <del>熟悉items,pieline spiders api运用
+ <del>存储【json、moogooDB】
+ <del>输出日志文件
    - 启运的时候加上即可,如:scrapy crawl SimpleScrapy --set LOG_FILE=log
+ <del>去重
    - 使用 from scrapy.exceptions import DropItem

