# -*- coding: utf-8 -*-
import scrapy
import numpy as np
from doubansp.items import DoubanspItem
from scrapy.http import Request
import re
count = 0
class DbspiderSpider(scrapy.Spider):
	name = 'dbspider2'
	allowed_domains = ['movie.douban.com']
	baseurl = 'http://movie.douban.com/top250'
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
	headers = { 'User-Agent' : user_agent}
	#start_urls = ['http://movie.douban.com/top250']
	def start_requests(self):
		for num in np.linspace(0,225,10):
			url = self.baseurl + '?start='+str(int(num))+'&filter='
			yield Request(url,callback=self.parse,headers=self.headers)

	def parse(self, response):
		movieps = response.xpath('//div[@class="info"]')
		for moviep in movieps:
			global count
			count += 1
			item = DoubanspItem()
			namesel = moviep.xpath('div[@class="hd"]/a/span/text()').extract()
			namestr = ''
			for names in namesel:
				namestr += names
			item['name'] = namestr.replace(' ', '').replace('\n', '')
			movieInfo1 = moviep.xpath('div[@class="bd"]').extract()
			pattern = re.compile('<p class="">(.*?)</p>',re.S)
			item['movieInfo'] = re.findall(pattern,movieInfo1[0])[0].replace(' ', '').replace('\n', '')
			#item['movieInfo'] = movieInfo1
			item['count'] = count
			item['star'] = moviep.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()
			item['quote'] = moviep.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
			yield item
	













