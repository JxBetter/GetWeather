# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class TqSpider(scrapy.Spider):
    name = 'tq'
    allowed_domains = ['weather.com.cn']
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10771.400'}
    url = 'http://www.weather.com.cn/weather/101210301.shtml'
    def start_requests(self):
        yield Request(self.url,headers=self.head,callback=self.parse)

    def parse(self, response):
        day = response.xpath('//li/h1/text()').extract()
        w = response.xpath('//li/p/@title').extract()
        ht = response.xpath('//li/p[@class="tem"]/span/text()').extract()
        lt = response.xpath('//li/p[@class="tem"]/i/text()').extract()
        print(day+w+ht+lt)
