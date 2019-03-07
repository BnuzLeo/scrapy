import scrapy


class BlogSpider(scrapy.Spider):
    name = 'lucklySpider'
    start_urls = ['https://www.jsh365.com/award/gp-gdsyxu/2019-03-06.html',
                  'https://www.jsh365.com/award/gp-gdsyxu/2019-03-05.html',
                  'https://www.jsh365.com/award/gp-gdsyxu/2019-03-04.html',
                  'https://www.jsh365.com/award/gp-gdsyxu/2019-03-03.html',
                  'https://www.jsh365.com/award/gp-gdsyxu/2019-03-02.html',
                  'https://www.jsh365.com/award/gp-gdsyxu/2019-03-01.html'
                  ]

    def parse(self, response):
        print(response.url)
        for tab in response.css('._tab'):
            i = 1
            for item in tab.css('tr>td>div'):
                if i % 6 == 0:
                    print(item.css('::text').get())
                else:
                    print(item.css('::text').get()),
                i = i + 1
