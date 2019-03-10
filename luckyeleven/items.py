# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LuckyelevenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Result(scrapy.Item):
    date = scrapy.Field()
    item = scrapy.Field()
    time = scrapy.Field()
    num1 = scrapy.Field()
    num2 = scrapy.Field()
    num3 = scrapy.Field()
    num4 = scrapy.Field()
    num5 = scrapy.Field()
    pass
