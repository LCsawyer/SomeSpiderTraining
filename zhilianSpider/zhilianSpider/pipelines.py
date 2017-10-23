# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhilianspiderPipeline(object):
	def open_spider(self,spider):
		self.file = open('zhilian.txt','w+')
	def close_spider(self,spider):
		self.file.close()
	def process_item(self, item, spider):
		job = item['job']
		compy = item['compy']
		salary = item['salary']
		locate = item['locate']
		alldata = zip(job,compy,salary,locate)
		count = 1
		for adt in alldata:
			txt = str(count) + '职位: ' + adt[0].encode('utf-8') + ' ' + '公司: '+ adt[1].encode('utf-8') + ' ' + '薪水: '+adt[2].encode('utf-8') + ' '+'工作地点: '+adt[3].encode('utf-8')+'\n'
			self.file.write(txt)
			count +=1
		#self.file.write(str(count))
		return item
