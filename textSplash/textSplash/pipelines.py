# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TextsplashPipeline(object):
	def open_spider(self,spider):
		self.file = open('testdata.txt','w+')
	def close_spider(self,spider):
		self.file.close()
	def process_item(self, item, spider):
		name = item['name']
		text = item['text']
		alldata = zip(name,text)
		for adt in alldata:
			Ttext = adt[1].replace('<p>','').replace('</p>','')
			str1 = 'Title: '+ adt[0] + '\n' + 'Article: ' + Ttext + '\n'
			self.file.write(str1)
			self.file.write('----------------------------------------------------------\n')
		return item
