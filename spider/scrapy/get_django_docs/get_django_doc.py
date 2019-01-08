import scrapy
class django(scrapy.Spider):
    name = 'get_django'
    start_urls = ['https://docs.djangoproject.com/zh-hans/2.0/']
    def parse(self, response):
        #抓取指定标签中的文本内容，这里定义的是div 名称为section的标签，
        page = response.css('.section *::text').extract()    
        filename = 'first_page'
        #将抓取到的文本依次写入指定文件中
        for p in page:
            with open(filename, 'a+') as f:
                f.write(p)
        #判断是否有下一页，如果有，过滤出下一页的路径        
        next_page = response.xpath("//div[@class='right']//@href").extract_first()
        '''
        将过滤出来的路径（相对路径）通过urljoin进行拼接，例如获取到的是/intro路径，
        加上start_usrls后next_page就是https://docs.djangoproject.com/zh-hans/2.0/intro/ 
        '''
        if next_page is not None:
            next_page = response.urljoin(next_page)
            '''
            爬取下一页的内容 方法：scrapy.Request()  下一页的路径（链接）：next_page，通过callback将链接交给处理的函数，也就是parse函数（即本函数，所以用了self.）
            '''
            yield scrapy.Request(next_page, callback=self.parse)
'''
抓取本网站时会出现："DEBUG: Forbidden by robots.txt......"，这是因为爬取时网站的robot.txt阻止了部分页面不让爬虫进行抓取。
在setting.py中将ROBOTSTXT_OBEY=True 的值改为Flase即可
'''