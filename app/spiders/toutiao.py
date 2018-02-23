# -*- coding: utf-8 -*-
import json

import scrapy

from app.items import ToutiaoItem, MyItemLoader


class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['is.snssdk.com']
    page_num = 10
    query = {
        'keyword': '古天乐', 'device_id': 41296383364, 'cur_tab': 1, 'offset': 0, 'count': 10
    }

    start_url = 'https://is.snssdk.com/2/wap/search_content/?device_id={device_id}&keyword={keyword}&count={' \
                'count}&cur_tab={cur_tab}&format=json&offset={offset}'

    def start_requests(self):
        for i in range(0, self.page_num):
            self.query['offset'] = i * self.query['count']
            yield scrapy.Request(self.start_url.format(**self.query))

    def parse(self, response):
        self.logger.info(response.url)
        details = json.loads(response.text)

        if len(details['data']) != 0:
            for detail in details['data']:
                if 'cell_type' not in detail:
                    item_loader = MyItemLoader(item=ToutiaoItem())
                    item_loader.add_value('media_name', [detail.get('media_name')])
                    item_loader.add_value('abstract', [detail.get('abstract')])
                    item_loader.add_value('create_time', [detail.get('create_time')])
                    item_loader.add_value('title', [detail.get('title')])
                    item_loader.add_value('article_url', [detail.get('article_url')])
                    item_loader.add_value('publish_time', [detail.get('publish_time')])
                    item_loader.add_value('id', [detail.get('id')])
                    yield item_loader.load_item()
