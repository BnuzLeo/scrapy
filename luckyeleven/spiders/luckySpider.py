import scrapy

from luckyeleven.items import Result
import random


class BlogSpider(scrapy.Spider):
    name = 'lucklySpider'
    start_urls = [
                  # 'https://www.jsh365.com/award/gp-gdsyxu/2019-03-08.html',
                  # 'https://www.jsh365.com/award/gp-gdsyxu/2019-03-07.html',
                  # 'https://www.jsh365.com/award/gp-gdsyxu/2019-03-06.html',
                  # 'https://www.jsh365.com/award/gp-gdsyxu/2019-03-05.html',
                  # 'https://www.jsh365.com/award/gp-gdsyxu/2019-03-04.html',
                  # 'https://www.jsh365.com/award/gp-gdsyxu/2019-03-03.html',
                  # 'https://www.jsh365.com/award/gp-gdsyxu/2019-03-02.html',
                  'https://www.jsh365.com/award/gp-gdsyxu/2019-03-01.html'
                  ]

    def parse(self, response):
        # print(response.url)
        # for tab in response.css('._tab'):
        #     for item in tab.css('tr'):
        #         if len(item.css('td')) == 0:
        #             continue
        #         result = Result()
        #         url = response.url
        #         result['date'] = url[url.find('u/') + 2:url.find('.html')]
        #         result['item'] = int(item.css('td')[0].css('div::text').get())
        #         result['time'] = item.css('td')[1].css('::text').get()
        #         i = 0
        #         for div in item.css('td')[2].css('div'):
        #             i = i + 1
        #             index = 'num' + str(i)
        #             result[index] = int(div.css('::text').get())
        #         yield result


        i = 1
        while(i<=43):
            print(i,random.sample(range(1,11),5))
            i = i + 1
