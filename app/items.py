# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import json

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose

from utils.common import date_convert


class AppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MyItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ToutiaoItem(scrapy.Item):
    media_name = scrapy.Field()
    abstract = scrapy.Field()
    create_time = scrapy.Field(
        input_processor=MapCompose(date_convert),
        output_processor=TakeFirst()
    )
    keywords = scrapy.Field()
    title = scrapy.Field()
    article_url = scrapy.Field()
    publish_time = scrapy.Field(
        input_processor=MapCompose(date_convert),
        output_processor=TakeFirst()
    )
    id = scrapy.Field()


# 页面占位列表
class LocationItem(scrapy.Item):
    fetchTime = scrapy.Field()  # 爬取时间
    type = scrapy.Field()  # 类型 location
    data = scrapy.Field(serializer=json.dumps)  # 具体占位数据
    origin = scrapy.Field(serializer=json.dumps)  # 采集源信息

    def __init__(self):
        scrapy.Item.__init__(self)
        self['type'] = 'location'


# 占位具体信息
class LocationDetailItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    content = scrapy.Field()  # 概要
    url = scrapy.Field()  # URL
    pageNum = scrapy.Field()  # 页码
    location = scrapy.Field()  # 当前第几页
    uuid = scrapy.Field()  # 平台唯一ID
    uuidType = scrapy.Field()  # UUID类型
    parentId = scrapy.Field()  # 父唯一ID


# 文章详情
class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    media = scrapy.Field()
    publish_time = scrapy.Field(
        input_processor=MapCompose(date_convert)
    )
    content = scrapy.Field()
