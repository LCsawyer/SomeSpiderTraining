# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as ps
import datetime
'''
class DoubanspPipeline(object):
	def open_spider(self,spider):
		self.file = open('doubanmovie.txt','w+')
	def close_spider(self,spider):
		self.file.close()
	def process_item(self, item, spider):
		name = item['name'].encode('utf-8')
		movieInfo = item['movieInfo'][0].replace('<br>','').encode('utf-8')
		star = item['star'][0].encode('utf-8')
		if len(item['quote']) >0:
			quote = item['quote'][0].encode('utf-8')
		else:
			quote = ''
		synopsis = str(item['count'])+': '+item['synopsis'][0].replace('<br>','').encode('utf-8')
		textstr = 'name : '+name.strip()+'\n'+'movieInfo : '+movieInfo.strip()+'\n'+'star : '+star.strip()+'\n'+'quote : '+quote.strip()+'\n'+'synopsis : '+synopsis.strip()+'\n'
		self.file.write(textstr)
		self.file.write('--------------------------------------------------------\n')
		return item
'''

class DoubanspPipelineDB(object):
	def __init__(self):
		self.conn = ps.connect(host='localhost',user='sawyer',password='210013',db='movie',charset='utf8')
		self.cursor = self.conn.cursor()
		self.cursor.execute("truncate table movie")
        	self.conn.commit()
	def close_spider(self,spider):
		self.conn.close()

	def process_item(self, item, spider):
		name = item['name'].strip().encode('utf-8')
		movieInfo = item['movieInfo'].replace('<br>','').strip().encode('utf-8')
		star = item['star'][0].strip().encode('utf-8')
		if len(item['quote']) >0:
			quote = item['quote'][0].strip().encode('utf-8')
		else:
			quote = ''
		id1 = str(item['count'])
		createTime = str(datetime.datetime.now())
		self.cursor.execute('insert into movie values (%s,%s,%s,%s,%s,%s)',(id1,name,movieInfo,star,quote,createTime))
		self.conn.commit()
		return item



















