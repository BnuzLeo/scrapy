import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://11xuan5.cjcp.com.cn/guangdong/kaijiang/']

    def parse(self, response):
        i = 0
        for tr in response.css('.kjjg_table>tr'):
            print('')
            for td in tr.css('td'):
                items = td.css('.kjjg_hm_bg')
                if len(items) == 0:
                    print(td.css('::text').get()),
                else:
                    for item in items.css('.hm_bg ::text'):
                        print(item.get()),