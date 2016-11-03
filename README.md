# scrapy
网络爬虫练手项目

## toDo:

+ 验证码模拟


## Done:

+ 启动
    - scrapy crawl SimpleScrapy
+ 多线程处理
    - REACTOR_THREADPOOL_MAXSIZE = 10 默认进程数是10,可以调整
+ 分步式处理
 - 解决方案:https://github.com/rolando/scrapy-redis
+ 自动限束
    - settings 当中有如下设置,调整或开启就可以了:
    - AUTOTHROTTLE_ENABLED = True
    - AUTOTHROTTLE_START_DELAY = 5
    - AUTOTHROTTLE_MAX_DELAY = 60
    - AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
    - AUTOTHROTTLE_DEBUG = False
+ ban 处理[settings处理]
    - settings处理cookie  如:COOKIES_ENABLED = False
    - download_delay = 1 设置延迟时间
+ 网页解析器Xpath运用
    - 可以用开发者工具copy xpath来生成
    - 在开发者工具里面用$x()来测试取到的是不是对的,如$x('//*[@id="post-81320"]/div[3]/h3[5]')
+ 熟悉items,pieline spiders api运用
+ 存储【json、moogooDB】
+ 输出日志文件
    - 启运的时候加上即可,如:scrapy crawl SimpleScrapy --set LOG_FILE=log
+ 去重
    - 使用 from scrapy.exceptions import DropItem
+ 暂停、重启
    - 通过 JOBDIR 设置 job directory 选项,如scrapy crawl somespider -s JOBDIR=crawls/somespider-1
    - 关闭 control + C
    - 重启:再次输入上面的命令 scrapy crawl somespider -s JOBDIR=crawls/somespider-1
+ ajax爬取
    - 对于采集来说的动态网页是那些需要经过js,ajax动态加载来获取数据的网页，采集数据的方案分为两种：
    - 1.通过抓包工具分析js,ajax的请求，模拟该请求获取js加载后的数据。
    - 2.调用浏览器的内核，获取加载后的网页源码，然后对源码经行解析
+ 运行多个scrapy
+ 深度自动爬取
    - CrawlSpider 替代scrapy.Spider
    - CrawlSpider 多了一个Rule可以配置一个符合LinkExtractor提取器规则的正则,与回调
+ 登录模拟
    - FormRequest.from_response 模拟提交表单及cookie信息

