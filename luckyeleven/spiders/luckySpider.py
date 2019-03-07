import scrapy


class BlogSpider(scrapy.Spider):
    name = 'lucklySpider'
    start_urls = ['https://www.jsh365.com/award/gp-gdsyxu/2019-03-06.html']

    def parse(self, response):
        for tab in response.css('._tab'):
            i = 0
            for item in tab.css('tr>td>div'):
                if i == 0:
                    print(item.css('::text').get())
                else:
                    print(item.css('::text').get()),
