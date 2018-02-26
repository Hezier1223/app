# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from app.items import ArticleItem


class ArticleSpider(scrapy.Spider):
    name = 'article'
    # allowed_domains = ['www.toutiao.com']
    start_urls = ['https://www.toutiao.com/group/6525947280254566926/']

    def parse(self, response):
        print(response)
        loader = ItemLoader(item=ArticleItem(), response=response)
        loader.add_css('title', '.article-title::text')
        # loader.add_css('media', '.article-box .article-sub span:nth-child(1)::text')
        # loader.add_css('pub_time', '.article-box h1.article-title:nth-child(2)')
        # loader.add_css('content', '.article-box .article-content::text')
        article = loader.load_item()
        yield article
