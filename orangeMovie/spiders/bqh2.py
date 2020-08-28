# -*- coding: utf-8 -*-
from tkinter import Tk

import scrapy
from ..items import OrangemovieItem


class Bqh2Spider(scrapy.Spider):
    name = 'bqh2'
    # allowed_domains = ['bqh2.com/index/home.html']

    start_urls = ['https://www.bqh2.com/shipin/list-亚洲电影.html'] + \
                 [f'https://www.bqh2.com/shipin/list-亚洲电影-{i}.html' for i in range(2, 70)]

    def parse(self, response):
        aList = response.xpath('//ul/div[@id="tpl-img-content"]/li/a')
        for ai in aList:
            item = OrangemovieItem()
            item['title'] = ai.xpath('.//h3[@class="text-ellipsis"]/@title').extract()[0]
            item['imgSrc'] = ai.xpath('.//img[@class="lazy"]/@data-original').extract()[0]
            item['href'] = 'https://www.bqx4.com' + ai.xpath('./@href').get()
            requestUrl = 'https://www.bqh2.com' + ai.xpath('./@href').get()
            yield scrapy.Request(requestUrl, callback=self.parse_orange_movie_detail, meta={'item': item})

    def parse_orange_movie_detail(self, response):
        item = response.meta['item']
        detail = response.xpath('//tbody/tr/td/input[@id="lin1k1"]/@value').get()
        if detail is None:
            item['downloadUrl'] = '本电影暂无下载地址'
        else:
            item['downloadUrl'] = detail
        yield item
