#-*- coding:utf8 -*-
import urllib2
import json
from lxml import html
import lxml
import re
from connectDB import Con

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Parser:
	#解析用户喜欢这个页面
	@classmethod
	def parseLike(cls, people_id, content):
		page = html.fromstring(content)
		titleSet = page.find_class('title')
		con = Con()
		for title_item in titleSet:
			title = title_item.xpath('./a/text()[1]')[0]
			url = title_item.xpath('./a')[0].get('href')
			Type = ''
			if 'widget' in url:
				Type = 'photo_note'
			elif 'photo' in url:
				Type = 'photo'
			elif 'note' in url:
				Type = 'note'
			print title
			con.insert_people_like((people_id, title.encode('utf8'), Type, url))
		con.close()

	def contactParser(self, content):
		# 主要作用就是解析用户关注/被关注人的信息
		cp = re.compile('<dd><a href="([^"]+)">([^<]+)</a></dd>')
		contactList = cp.findall(content)
		peopleList = [ item[1] for item in contactList ]
		return peopleList



