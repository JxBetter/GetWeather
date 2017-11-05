# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request

class AutotqSpider(CrawlSpider):
    name = 'autotq'
    allowed_domains = ['weather.com.cn']
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10771.400'}
    url = 'http://www.weather.com.cn/weather/101210301.shtml'

    rules = (
        Rule(LinkExtractor(allow='http://www.weather.com.cn/weather1d/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        yield Request(self.url,headers=self.head,callback=self.parse)

    def parse_item(self, response):
        area = response.xpath('//title/text()').extract()
        date = response.xpath('//li/h1/text()').extract()
        w = response.xpath('//li/p/@title').extract()
        t = response.xpath('//li/p[@class="tem"]/span/text()').extract()
        if int(t[0]) >20:

            print(area[0]+'\n'+date[1]+w[1]+t[0])
            print('----------------------------------------------------')
