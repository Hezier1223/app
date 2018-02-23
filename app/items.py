# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

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
