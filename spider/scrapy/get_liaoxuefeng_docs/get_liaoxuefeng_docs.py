import scrapy, pdfkit, requests, random, time
class html_to_pdf(scrapy.Spider):
    name = 'html_to_pdf'
    start_urls = ['https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000']
    # def get_menu():
        # urls = 'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
        # headers = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36'
        # response = requests.get(url=urls, headers=headers)
        # menu = response.css('.x-wiki-index-item *::text').extract()
        # filename = 'liaoxuefeng'
        # for i in menu:
            # with open(filename, 'a+') as f:
                # f.write(i)
    nb = 0
    def parse(self, response):
        if self.nb == 1:
            menu = response.css('.x-wiki-index-item *::text').extract()
            filename = 'liaoxuefeng'
            for i in menu:
                with open(filename, 'a+') as f:
                    f.write(i)
            self.nb = 1
        else:
            pass
        page =  response.css('.x-wiki-content *::text').extract()
        filename = 'liaoxuefeng'
        for i in page:
            with open(filename, 'a+') as f:
                f.write(i)
        # next_page = response.xpath("//div[@class='rst-footer-buttons']//@href").extract_first()
        next_pages = response.xpath("//ul[@class='uk-nav uk-nav-side']//@href").extract()
        if next_pages is not None:
            for next_page in next_pages:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)