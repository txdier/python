import scrapy
class k8s(scrapy.Spider):
    name = 'new_k8s'
    start_urls = ['https://www.kubernetes.org.cn/docs']
    filename = 'new_k8s_docs'
    def parse(self, response):
        '''parse用来获取url列表，然后通过for循环取值传递给get_doc来获取页面内容'''
        urls = response.xpath("//div[@class='pageside']//@href").extract()[1:]
        title = response.css('.pageside *::text').extract()[1]
        with open(self.filename, 'a+') as f:
            f.write(title + '\n')
        # print(urls)
        for url in urls:
            yield scrapy.Request(url, callback=self.get_doc)
    def get_doc(self, response):
        '''获取页面内容并保存'''
        page = response.css('.content *::text').extract()[1:-63]
        for p in page:
            with open(self.filename, 'a+') as f:
                f.write(p)