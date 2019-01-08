先新建一个scrapy项目，

scrapy startproject djiango_test

然后修改项目目录中items.py文件，增加如下内容

class DailiIpsItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    position = scrapy.Field()
    type = scrapy.Field()
    speed = scrapy.Field()
    last_check_time = scrapy.Field()
    
进到spiders目录，执行get_xici.py
