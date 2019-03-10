# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymysql
from luckyeleven import settings


class LuckyelevenPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class insertToDBPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            db=settings.MYSQL_DBNAME)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "insert into result(date,item,time,num1,num2,num3,num4,num5) value (%s,%s,%s,%s,%s,%s,%s,%s)",
                (item['date'], item['item'], item['time'], item['num1'], item['num2'], item['num3'], item['num4'],
                 item['num5'])
            )

            self.connect.commit()
        except Exception as error:
            print(error)
        return item
