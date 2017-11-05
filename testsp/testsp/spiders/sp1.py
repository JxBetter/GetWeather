# -*- coding: utf-8 -*-
import scrapy


class Sp1Spider(scrapy.Spider):
    name = 'sp1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.url)
        pass
