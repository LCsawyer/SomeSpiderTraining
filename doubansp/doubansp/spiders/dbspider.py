# -*- coding: utf-8 -*-
import scrapy
import numpy as np
from doubansp.items import DoubanspItem
from scrapy.http import Request
import re
count = 0
#根据需要调整item
class DbspiderSpider(scrapy.Spider):
	name = 'dbspider'
	allowed_domains = ['movie.douban.com']
	baseurl = 'http://movie.douban.com/top250'
	#start_urls = ['http://movie.douban.com/top250']
	def start_requests(self):
		for num in np.linspace(0,225,10):
			url = self.baseurl + '?start='+str(int(num))+'&filter='
			yield Request(url,callback=self.parse)

	def parse(self, response):
		movieps = response.xpath('//div[@class="info"]')
		for moviep in movieps:
			global count
			count += 1
			item = DoubanspItem()
			namesel = moviep.xpath('div[@class="hd"]/a/span/text()').extract()
			url = moviep.xpath('div[@class="hd"]/a/@href').extract()
			namestr = ''
			for names in namesel:
				namestr += names
			item['name'] = namestr
			movieInfo1 = moviep.xpath('div[@class="bd"]').extract()
			pattern = re.compile('<p class="">(.*?)</p>',re.S)
			item['movieInfo'] = re.findall(pattern,movieInfo1[0])
			#item['movieInfo'] = movieInfo1
			item['count'] = count
			item['star'] = moviep.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()
			item['quote'] = moviep.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
			request = Request(url[0],callback=self.synopsis_parse,meta={'keys':item})
			yield request
	
	def synopsis_parse(self,response):
		item = response.meta['keys']
		selectss = response.xpath('//div[@class="indent"]')
		selectss1 = selectss.xpath('span[@class="all hidden"]').extract()
		if len(selectss1) != 0:
			pattern = re.compile('>(.*?)</span>',re.S)
			item['synopsis'] = re.findall(pattern,selectss1[0])
		else:
			item['synopsis'] = selectss.xpath('span[1]/text()').extract()
		return item
		
