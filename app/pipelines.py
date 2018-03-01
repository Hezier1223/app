# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Toutiao

engine = create_engine('mysql://root:root@localhost:3306/app?charset=utf8', echo=True)
DBSession = sessionmaker(bind=engine)

Toutiao.metadata.create_all(engine)


class AppPipeline(object):
    def process_item(self, item, spider):
        return item


class ToutiaoPipeline(object):
    def process_item(self, item, spider):
        print(item)
        # print(type(item))
        # session = DBSession()
        # article = Toutiao(**item)
        # session.add(article)
        # session.commit()
        # session.close()
        return item
