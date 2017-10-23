# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	name = scrapy.Field()
	movieInfo = scrapy.Field()
	star = scrapy.Field()
	quote = scrapy.Field()
	#synopsis = scrapy.Field()
	count = scrapy.Field()
