# -*- coding: utf-8 -*-
import json

import scrapy

from app.items import MyItemLoader, LocationDetailItem, ArticleItem


class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    # allowed_domains = ['is.snssdk.com', 'toutiao.com']
    page_num = 10
    query = {
        'keyword': '古天乐', 'device_id': 41296383123, 'cur_tab': 1, 'offset': 0, 'count': 10
    }

    start_url = 'https://is.snssdk.com/2/wap/search_content/?device_id={device_id}&keyword={keyword}&count={' \
                'count}&cur_tab={cur_tab}&format=json&offset={offset}'

    article_url = 'https://m.toutiao.com/i{id}/info/?i={id}'

    def start_requests(self):
        for i in range(0, self.page_num):
            self.query['offset'] = i * self.query['count']
            yield scrapy.Request(self.start_url.format(**self.query), meta={'location': i})

    def parse(self, response):
        details = json.loads(response.text)
        location = response.meta.get('location')

        if len(details['data']) != 0:
            for index, detail in enumerate(details['data']):
                if 'cell_type' not in detail:
                    location_item = LocationDetailItem()
                    location_item['title'] = detail.get('title')
                    location_item['content'] = detail.get('abstract')
                    location_item['url'] = detail.get('article_url')
                    location_item['pageNum'] = index
                    location_item['location'] = location
                    location_item['uuid'] = detail.get('id')
                    location_item['uuidType'] = detail.get('id')  # TODO
                    location_item['parentId'] = detail.get('id')  # TODO
                    print(location_item)
                    # item_loader = MyItemLoader(item=ToutiaoItem())
                    # item_loader.add_value('media_name', [detail.get('media_name')])
                    # item_loader.add_value('abstract', [detail.get('abstract')])
                    # item_loader.add_value('create_time', [detail.get('create_time')])
                    # item_loader.add_value('title', [detail.get('title')])
                    # item_loader.add_value('article_url', [detail.get('article_url')])
                    # item_loader.add_value('publish_time', [detail.get('publish_time')])
                    # item_loader.add_value('id', [detail.get('id')])
                    # yield item_loader.load_item()
                    if detail['id']:
                        yield scrapy.Request(self.article_url.format(id=detail['id']), callback=self.parse_article,
                                             meta={'article_type': detail['article_type']})

    # 解析文章详情
    def parse_article(self, response):
        loader = MyItemLoader(item=ArticleItem())
        article_json = json.loads(response.text)
        article_detail = article_json['data']
        loader.add_value('title', [article_detail.get('title')])
        loader.add_value('media', [article_detail.get('detail_source')])
        loader.add_value('publish_time', [article_detail.get('publish_time')])
        loader.add_value('content', [article_detail.get('content')])
        article = loader.load_item()
        yield article
