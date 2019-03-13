# Simple Example

## 实现一个简单的爬虫
### 新建爬虫
1. 创建一个spiders文件夹，新建爬虫：quotes_spider.py 
```python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

### 定义的一些 attributes and methods，  
具体参考：[spiders](https://docs.scrapy.org/en/latest/topics/spiders.html#generic-spiders)

### 如何执行爬虫
1. 指定爬虫执行：
```text
scrapy crawl quotes
``` 
注意：这个qutoes指的是上面爬虫的name