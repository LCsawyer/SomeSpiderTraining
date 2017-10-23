# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from zhilianSpider.items import ZhilianspiderItem

class ZlspiderSpider(scrapy.Spider):
	name = 'zlspider'
	allowed_domains = ['sou.zhaopin.com']
	#start_urls = ['http://sou.zhaopin.com/']
	baseurl = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=全国&sm=0&p="
	def start_requests(self):
		for i in range(1,11):
			url = self.baseurl + str(i)
			yield Request(url,callback=self.parse)

	def parse(self, response):
		items = ZhilianspiderItem()
		#alljob = response.xpath('//table[@class="newlist"]')
		items['job'] = response.xpath('//td[@class="zwmc"]/div/a/text()').extract()
		items['compy'] = response.xpath('//td[@class="gsmc"]/a/text()').extract()
		items['salary'] = response.xpath('//td[@class="zwyx"]/text()').extract()
		items['locate'] = response.xpath('//td[@class="gzdd"]/text()').extract()
		return items
		
