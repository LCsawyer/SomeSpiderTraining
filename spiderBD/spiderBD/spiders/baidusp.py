# -*- coding: utf-8 -*-
import scrapy
from spiderBD.items import SpiderbdItem

class BaiduspSpider(scrapy.Spider):
	name = 'baidusp'
	allowed_domains = ['news.baidu.com']
	start_urls = ['http://news.baidu.com/']

	def parse(self, response):
		items = SpiderbdItem()
		items['name'] = response.xpath('//li[@class="hdline0"]/strong/a/text()').extract()
		print items['name'][0].encode('utf-8')
		return items
