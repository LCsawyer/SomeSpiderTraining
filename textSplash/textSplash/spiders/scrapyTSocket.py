# -*- coding: UTF-8 -*-

import scrapy
from scrapy_splash import SplashRequest
from scrapy.http import Request
from textSplash.items import TextsplashItem

class TencentStockSpider(scrapy.Spider):
	name = "TencentS"
	def start_requests(self):
		urls = ['http://stock.qq.com/l/stock/ywq/list20150423143546.htm']
		for url in urls:
			yield SplashRequest(url, self.parse, args={'wait': 0.5})

	def parse(self,response):
		item = TextsplashItem()
		urls = response.xpath('//ul[@class="listInfo"]/li/div[@class="info"]/h3/a/@href').extract()
		#for item in items:
		#	print item
		item['name'] = response.xpath('//ul[@class="listInfo"]/li/div[@class="info"]/h3/a/text()').extract()
		for url in urls:
			yield SplashRequest(url, self.after_parse, args={'wait': 0.5},meta={'keys':item})

	def after_parse(self,response):
		item = response.meta['keys']
		item['text'] = response.xpath('div[@class="bd"]/div/text()').extract()
		return item
		
        
       
