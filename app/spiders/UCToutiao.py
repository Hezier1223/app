# -*- coding: utf-8 -*-
import scrapy

# https://m.sm.cn/s?app_name=ucnews-iflow&from=wh10339&q=何欢
from scrapy.loader import ItemLoader

from app.items import MyItemLoader, UCArticleItem


class UCtoutiaoSpider(scrapy.Spider):
    name = 'UCToutiao'
    allowed_domains = ['m.sm.cn/s']

    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) ' \
                 'Version/9.0 Mobile/13B143 Safari/601.1 '

    def start_requests(self):
        yield scrapy.Request(
            'https://m.sm.cn/s?app_name=ucnews-iflow&from=wh10339&safe=1&q=古天乐&by=next&layout=html&page=4',
            headers={'User-Agent': self.user_agent})

    def parse(self, response):
        loader = ItemLoader(item=UCArticleItem(), response=response)
        loader.add_xpath('title', '//p[contains(@class, "y-feed-title"]')
        articles = loader.load_item()
        yield articles
        # f = open('test.html', 'w')
        # f.write(response.text)
        # f.close()
